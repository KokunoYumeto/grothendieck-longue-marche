"""Reversible editorial annotation of the checked LM package texts.

Only explicit author cancellations and insertions are resolved. No doubtful
reading is resolved. The source projection of every generated annotation is
byte-identical (after Python's text newline normalization) to its input.

Run from the directory holding sources/ and work/. Public records use only
paths inside the supplied archives. This module neither compiles nor edits
its source files.
"""
from __future__ import annotations
import argparse, collections, csv, hashlib, json, re
from pathlib import Path
from typing import Any

COMMAND = re.compile(r'\\([A-Za-z@]+|.)', re.S)
TARGET = re.compile(r'\\(deleted|inserted|unsure|illegible|margin|mspage|scanpage)\b\s*\{')
SCAN = re.compile(r'\\scanpage\{(\d+)\}')
URL = 'https://grothendieck.umontpellier.fr'
KINDS = {'deleted':'deletion','inserted':'insertion'}
CODES = {'deleted':'D','inserted':'I'}
REASONS = {
 'fr': {'deleted': "Passage biffé dans le manuscrit : la suppression suit l'état final de l'auteur; les doutes de lecture restent signalés.",
        'inserted': "Ajout explicite de l'auteur : intégré à l'endroit indiqué par la transcription, sans modifier sa lecture."},
 'en': {'deleted': "Cancelled in the manuscript: omission follows the author's final state; uncertainty in the cancelled material remains marked.",
        'inserted': "Explicit authorial insertion: integrated at the position recorded by the transcription, without changing its reading."}}


def blank_comments(s: str) -> str:
    """Mask TeX comments without changing offsets, including escaped percent."""
    out=list(s); i=0
    while i<len(s):
        if s[i]=='\\':
            m=COMMAND.match(s,i); i=m.end() if m else i+2
        elif s[i]=='%':
            j=s.find('\n',i)
            if j<0:j=len(s)
            out[i:j]=' '*(j-i);i=j
        else:i+=1
    return ''.join(out)


def brace_end(s: str, start: int) -> int:
    """Return the index immediately after a balanced TeX group."""
    assert s[start]=='{', (start,s[start:start+30])
    depth=1;i=start+1
    while i<len(s):
        if s[i]=='\\':
            m=COMMAND.match(s,i);i=m.end() if m else i+2
        elif s[i]=='%':
            j=s.find('\n',i);i=len(s) if j<0 else j+1
        elif s[i]=='{':depth+=1;i+=1
        elif s[i]=='}':
            depth-=1;i+=1
            if not depth:return i
        else:i+=1
    raise ValueError(f'Unclosed TeX group at character {start}')


def spans(s: str, names: set[str]|None=None) -> list[dict[str,Any]]:
    mask=blank_comments(s);result=[]
    for m in TARGET.finditer(mask):
        if names and m[1] not in names:continue
        opening=m.end()-1;end=brace_end(s,opening)
        result.append(dict(name=m[1],start=m.start(),argstart=opening+1,argend=end-1,end=end,
                           argument=s[opening+1:end-1],raw=s[m.start():end]))
    return result


def package_info(package: str) -> dict[str,str]:
    # Cache metadata without requiring an absolute build path.
    if not hasattr(package_info,'cache'):
        with Path('sources/fr/records/CURRENT_TEXT_INDEX.tsv').open() as f:
            package_info.cache={r['package']:r for r in csv.DictReader(f,delimiter='\t')}
    return package_info.cache[package]


def at_scan(s: str,pos:int) -> int:
    before=list(SCAN.finditer(blank_comments(s[:pos])))
    return int(before[-1][1]) if before else 0


MATH_ENVS={'equation','equation*','displaymath','math','align','align*','alignat','alignat*','flalign','flalign*','aligned','alignedat','gather','gather*','gathered','multline','multline*','split','tikzcd','array','matrix','pmatrix','bmatrix','Bmatrix','vmatrix','Vmatrix','smallmatrix','cases'}
TEXT_ENVS={'tabular','tabular*','tabularx','minipage','tikzpicture','picture'}
# (number of mandatory arguments, forced modes by one-based argument index).
# Font commands such as operatorname and mathrm stay in mathematics; textsf
# and the other text commands enter text mode even when called inside math.
FORCED_ARGUMENTS={
    **{name:(1,{1:False}) for name in ('text','textrm','textnormal','textsf','texttt','textit','textbf','textsc','emph','mbox','hbox','vbox','vtop','vcenter','makebox','framebox','shortstack','fbox','footnote','footnotetext','caption')},
    'parbox':(2,{2:False}), 'raisebox':(2,{2:False}),
    'colorbox':(2,{2:False}), 'fcolorbox':(3,{3:False}),
    'rotatebox':(2,{2:False}), 'scalebox':(2,{2:False}), 'resizebox':(3,{3:False}),
    'ensuremath':(1,{1:True}),
}


def _forced_arguments(s: str) -> dict[int,bool]:
    mask=blank_comments(s);forced={}
    rx=re.compile(r'\\('+'|'.join(FORCED_ARGUMENTS)+r')\b\*?')
    for m in rx.finditer(mask):
        number,modes=FORCED_ARGUMENTS[m[1]];pos=m.end()
        for argument in range(1,number+1):
            while pos<len(s) and mask[pos].isspace():pos+=1
            # Optional arguments can occur before or between mandatory ones:
            # parbox[pos][height][inner]{width}{text}, raisebox{lift}[h][d]{text}.
            while pos<len(s) and mask[pos]=='[':
                depth=1;pos+=1
                while pos<len(s) and depth:
                    if mask[pos]=='\\':
                        q=COMMAND.match(mask,pos);pos=q.end() if q else pos+2;continue
                    depth+= {'[':1,']':-1}.get(mask[pos],0);pos+=1
                while pos<len(s) and mask[pos].isspace():pos+=1
            if argument==1 and m[1] in ('hbox','vbox','vtop','vcenter') and mask[pos:pos+1]!='{':
                q=re.match(r'(?:to|spread)\b[^{}]*',mask[pos:])
                if q:pos+=q.end()
            if pos>=len(s) or mask[pos]!='{':break
            end=brace_end(s,pos)
            if argument in modes:forced[pos]=modes[argument]
            pos=end
    return forced


from functools import lru_cache

@lru_cache(maxsize=8)
def math_mode_map(s: str) -> tuple[bool,...]:
    r"""Lexical TeX modes, including explicit text-box argument positions.

    A parbox's second mandatory argument is text even inside an array; its
    dimension argument does not change the surrounding mode. Explicit math
    inside text boxes is honored. Comments are True so compile normalization
    never rewrites commented control sequences. This scanner intentionally
    makes no assumptions about arbitrary user-defined macro expansion.
    """
    forced=_forced_arguments(s);mask=[False]*len(s);mode=False;i=0
    groups=[];environments=[];delimiters=[]
    while i<len(s):
        start=i;c=s[i]
        if c=='%':
            end=s.find('\n',i);end=len(s) if end<0 else end
            mask[i:end]=[True]*(end-i);i=end;continue
        if c=='\\':
            m=COMMAND.match(s,i)
            if not m:mask[i]=mode;i+=1;continue
            cmd=m[1];i=m.end();mask[start:i]=[mode]*(i-start)
            if cmd in ('(','['):delimiters.append((cmd,mode));mode=True
            elif cmd in (')',']'):mode=delimiters.pop()[1] if delimiters else False
            elif cmd in ('begin','end'):
                q=re.match(r'\s*\{([^}]*)\}',s[i:])
                if q:
                    end=i+q.end();mask[i:end]=[mode]*(end-i);i=end;name=q[1]
                    if cmd=='begin':
                        environments.append((name,mode))
                        if name in MATH_ENVS:mode=True
                        elif name in TEXT_ENVS:mode=False
                    else:
                        for k in range(len(environments)-1,-1,-1):
                            if environments[k][0]==name:
                                mode=environments[k][1];del environments[k:];break
            continue
        if c=='$':
            width=2 if s[i:i+2]=='$$' else 1;mask[i:i+width]=[True]*width;i+=width
            if delimiters and delimiters[-1][0]=='$'*width:mode=delimiters.pop()[1]
            else:delimiters.append(('$'*width,mode));mode=True
            continue
        mask[i]=mode
        if c=='{':
            groups.append(mode)
            if i in forced:mode=forced[i]
        elif c=='}':
            if groups:mode=groups.pop()
        i+=1
    return tuple(mask)


def math_mode_at(s: str,pos:int) -> bool:
    if pos<0 or pos>=len(s):return False
    return math_mode_map(s)[pos]


def maximal_doubts(s: str,start:int,end:int) -> list[dict[str,Any]]:
    result=[];until=-1
    for d in spans(s,{'unsure','illegible'}):
        if d['start']<start or d['end']>end or d['start']<until:continue
        q=dict(d);q['math_mode']=math_mode_at(s,d['start']);result.append(q);until=d['end']
    return result


def doubt_fragments(s:str,start:int,end:int) -> tuple[str,list[dict[str,Any]]]:
    ds=maximal_doubts(s,start,end)
    pieces=[]
    for d in ds:
        frag=d['raw']
        if d['math_mode']:frag=r'\('+frag+r'\)'
        pieces.append(frag)
    return r'\quad '.join(pieces),ds


def archive_footers(s:str,package:str,language:str='fr') -> tuple[str,list[dict[str,Any]]]:
    """Give every archive footer a reversible wrapper; print its number once.

    Footer numbers already independently transcribed immediately before the
    institutional block are retained at that pre-existing place. A number not
    otherwise present is retained as a manuscript-page marker. Comments never
    printed before, and remain comments. All original institutional strings
    remain in the annotated master or source records, never as manuscript.
    """
    info=package_info(package);mask=blank_comments(s);out=[];records=[];last=0
    macros=spans(s,{'margin'})
    occurrences=list(re.finditer(re.escape(URL),s))
    used_end=-1
    for nth,m in enumerate(occurrences,1):
        if m.start()<used_end:continue
        scan=at_scan(s,m.start());line=s.count('\n',0,m.start())+1
        comment=mask[m.start():m.end()].strip()==''
        if comment:
            a=s.rfind('\n',0,m.start())+1
            # Include contiguous source-comment lines identifying the footer.
            prev=a
            while prev>0:
                endprev=prev-1;startprev=s.rfind('\n',0,endprev)+1
                rawline=s[startprev:endprev]
                if not rawline.lstrip().startswith('%'):break
                prev=startprev
            a=prev;b=s.find('\n',m.end())
            if b<0:b=len(s)
            else:b+=1
            while b<len(s) and s[b:s.find('\n',b) if '\n' in s[b:] else len(s)].lstrip().startswith('%'):
                q=s.find('\n',b);b=len(s) if q<0 else q+1
            original=s[a:b]
            number_match=re.search(r'^%\s*(\d+[A-Za-z]*)\s*$',original,re.M)
            number=number_match[1] if number_match else ''
            retained=''
            # No mutation needed: comments preserve the original exactly.
            replacement=original
            action='Already nonprinting comments; institutional text remains excluded. Manuscript number remains at its original independent marker.'
        else:
            containers=[x for x in macros if x['start']<=m.start()<x['end']]
            if containers:
                outer=min(containers,key=lambda x:x['start']);a=outer['start'];b=outer['end']
            else:
                a=mask.rfind(r'\begin{center}',0,m.start())
                if a<0:raise ValueError(f'Footer container not found: {package} scan {scan}')
                b=mask.find(r'\end{center}',m.end())
                if b<0:raise ValueError(f'Footer end not found: {package} scan {scan}')
                b+=len(r'\end{center}')
                # Include an outer {\small ...} group when that group wraps center.
                pre=re.search(r'\{\\small\s*$',mask[:a])
                if pre:
                    groupend=brace_end(s,pre.start())
                    if groupend>=b:a=pre.start();b=groupend
            original=s[a:b]
            numpart=original[:original.index(URL)]
            candidates=re.findall(r'(?<![A-Za-z0-9])([0-9]+(?:bis|ter|[A-Za-z])?)\s*\\\\',numpart)
            if not candidates:raise ValueError(f'Footer page number not found: {package} scan {scan}')
            number=candidates[-1]
            prior=s[max(0,a-250):a]
            old_marker=re.search(r'\\(?:margin|mspage)\{'+re.escape(number)+r'\}\s*(?:%[^\n]*\n\s*)*$',prior)
            retained='' if old_marker else r'\mspage{'+number+'}'
            fid=f"{info['cote']}-s{scan:03d}-F{nth:02d}"
            replacement=r'\LMarchivefooter{'+original+'}{'+retained+'}{'+fid+'}'
            action=('Manuscript number '+number+' retained once at its preceding independent marker; institutional lines omitted.' if old_marker else
                    'Manuscript number '+number+' retained as \\mspage{'+number+'}; institutional lines omitted.')
        if a<last:raise ValueError(f'Overlapping footer at {package}:{scan}')
        out.append(s[last:a]);out.append(replacement);last=b;used_end=b
        record=dict(package=package,cote=info['cote'],scan=scan,source_line=line,language=language,
                    source_path=('fr/texts/'+package+'.tex' if language=='fr' else 'en/packages/'+package+'_en.tex'),
                    text=original,number=number,retained=retained,comment=comment,action=action,
                    start=a,end=b)
        records.append(record)
    out.append(s[last:])
    return ''.join(out),records


def carryover(entry: dict[str, Any], copy_macro: str = 'LMdoubtcopy') -> str:
    r"""Visible cancelled uncertainty, without repeating nested fragments.

    A deletion inside an enclosing unsure inherits uncertainty over its whole
    argument. In that case the entire argument is carried once, including any
    inner unsure/illegible marks, under a non-counting color/link wrapper.
    LMdoubtcopy should inherit the source scan link and print in blue while
    leaving the source unsure counter alone: the outer unsure remains on its
    dagger in the running text. Otherwise maximal original doubt fragments
    suffice and their individual original lexical modes are retained.
    """
    if entry.get('kind')!='deletion':return ''
    if entry.get('inherited_doubt'):
        frag='\\'+copy_macro+'{'+entry['argument']+'}'
        return r'\('+frag+r'\)' if entry.get('math_mode') else frag
    pieces=[]
    for d in entry.get('doubts',[]):
        frag=d['raw']
        if d.get('math_mode'):frag=r'\('+frag+r'\)'
        pieces.append(frag)
    return r'\quad '.join(pieces)


def semantic_final(s: str) -> str:
    """Select authorial final wording without adding edition or doubt sigla."""
    out=[];last=0
    for x in spans(s,{'deleted','inserted'}):
        if x['start']<last:continue
        out.append(s[last:x['start']])
        if x['name']=='inserted':out.append(semantic_final(x['argument']))
        last=x['end']
    out.append(s[last:]);return ''.join(out)


def annotate(text:str,package:str,language:str='fr') -> tuple[str,list[dict[str,Any]],dict[str,Any]]:
    language=language.lower();info=package_info(package)
    marks=spans(text,{'deleted','inserted','unsure','illegible','margin','scanpage','mspage'})
    edit=[x for x in marks if x['name'] in KINDS];counter=collections.Counter();entries=[]
    for x in edit:
        scan=at_scan(text,x['start']);key=(scan,x['name']);counter[key]+=1
        x['scan']=scan;x['id']=f"{info['cote']}-s{scan:03d}-{CODES[x['name']]}{counter[key]:03d}"
        parents=[p for p in edit if p['start']<x['start'] and p['end']>=x['end']]
        x['parent']=max(parents,key=lambda p:p['start']) if parents else None
        x['cancelled_ancestor']=any(p['name']=='deleted' for p in parents)
        x['inherited_doubt']=any(p['name'] in ('unsure','illegible') and p['start']<x['start'] and p['end']>=x['end'] for p in marks)
    # Build only variants whose reading can affect the final state. Edits inside
    # an enclosing cancelled passage belong to that cancellation's one entry.
    effective=[x for x in edit if not x['cancelled_ancestor']]
    bystart={x['start']:x for x in effective}
    def transform(a:int,b:int):
        parts=[];last=a
        local=[x for x in effective if a<=x['start'] and x['end']<=b]
        for x in local:
            if x['start']<last:continue
            parts.append(text[last:x['start']]);name=x['name']
            if name=='deleted':
                fragments,ds=doubt_fragments(text,x['argstart'],x['argend'])
                if x['inherited_doubt']:
                    corr=r'\LMuncertaindeletion{'+x['id']+'}'+(r'\LMdoubtdata{'+fragments+'}' if fragments else '')
                else:
                    corr=(r'\LMcancelledDoubts{'+fragments+'}' if fragments else '')
                semcorr=''
            else:
                corrected_arg=transform(x['argstart'],x['argend'])
                corr=r'\LMadded{'+corrected_arg+'}'
                semcorr=semantic_final(x['argument']);ds=[]
            replacement=r'\var{'+x['raw']+'}{'+corr+'}{'+KINDS[name]+'}{'+x['id']+'}'
            parts.append(replacement);last=x['end']
            entry=dict(id=x['id'],package=package,cote=info['cote'],scan=x['scan'],language=language,
                       source_line=text.count('\n',0,x['start'])+1,place=x['id'],
                       source_path=('fr/texts/'+package+'.tex' if language=='fr' else 'en/packages/'+package+'_en.tex'),
                       manuscript=x['raw'],corrected=semcorr,corrected_tex=corr,kind=KINDS[name],
                       reason=REASONS[language][name],argument=x['argument'],
                       math_mode=math_mode_at(text,x['start']),inherited_doubt=x['inherited_doubt'],
                       doubts=[{k:d[k] for k in ('name','raw','argument','math_mode','start','end')} for d in ds],
                       parent_id=x['parent']['id'] if x['parent'] else '',
                       start=x['start'],end=x['end'])
            entries.append(entry)
        parts.append(text[last:b]);return ''.join(parts)
    annotated=transform(0,len(text))
    entries.sort(key=lambda e:e['start'])
    # Footer annotation is independent of authorial revision: same projection
    # in all printed forms, since the institution's footer is not manuscript.
    annotated,footer_records=archive_footers(annotated,package,language)
    # Source provenance of footers must refer to source positions, not expanded
    # variant offsets; fetch those from the original input.
    _,source_footers=archive_footers(text,package,language)
    for r,sr in zip(footer_records,source_footers):
        for k in ('source_line','start','end','text'):r[k]=sr[k]
    counts=collections.Counter(x['name'] for x in marks)
    metadata=dict(package=package,cote=info['cote'],language=language,
                  source_sha256=hashlib.sha256(text.encode()).hexdigest(),counts=dict(counts),
                  scan_sequence=[int(x['argument']) for x in marks if x['name']=='scanpage'],
                  editorial_count=len(entries),subsumed_edits=sum(x['cancelled_ancestor'] for x in edit),
                  footers=footer_records)
    assert project(annotated,'source')==text, f'Source round trip failed: {language}/{package}'
    return annotated,entries,metadata


def project(s:str,form:str='source') -> str:
    """Resolve editorial wrappers only; used for exact source verification."""
    names=re.compile(r'\\(var|LMarchivefooter)\b')
    mask=blank_comments(s);out=[];last=0
    for m in names.finditer(mask):
        if m.start()<last:continue
        n=4 if m[1]=='var' else 3;args=[];pos=m.end()
        for _ in range(n):
            while pos<len(s) and s[pos].isspace():pos+=1
            if pos>=len(s) or s[pos]!='{':raise ValueError('Malformed annotation '+s[m.start():m.start()+80])
            e=brace_end(s,pos);args.append(s[pos+1:e-1]);pos=e
        choose=0 if form=='source' else (0 if form=='diplomatic' and m[1]=='var' else 1)
        out.append(s[last:m.start()]);out.append(project(args[choose],form));last=pos
    out.append(s[last:]);return ''.join(out)


def write_tsv(path:Path,fields:list[str],rows:list[dict]):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore',lineterminator='\n')
        w.writeheader();w.writerows(rows)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write-packages',action='store_true');args=ap.parse_args()
    records=Path('work/records');data=Path('work/data');records.mkdir(parents=True,exist_ok=True);data.mkdir(parents=True,exist_ok=True)
    with Path('sources/fr/records/CURRENT_TEXT_INDEX.tsv').open() as f:index=list(csv.DictReader(f,delimiter='\t'))
    allentries={};allmeta={}
    for language in ('fr','en'):
        el=[];ml=[]
        for row in index:
            p=row['package'];path=Path('sources/fr/texts')/(p+'.tex') if language=='fr' else Path('sources/en/packages')/(p+'_en.tex')
            text=path.read_text();ann,entries,meta=annotate(text,p,language);el.extend(entries);ml.append(meta)
            if args.write_packages:
                dst=Path('work/packages')/language/(p+'_annotated.tex');dst.parent.mkdir(parents=True,exist_ok=True);dst.write_text(ann)
        allentries[language]=el;allmeta[language]=ml
        (data/f'editorial_{language}.json').write_text(json.dumps({'entries':el,'packages':ml},ensure_ascii=False,indent=2)+'\n')
        write_tsv(records/('CHANGES_'+language.upper()+'.tsv'),['id','cote','scan','package','place','source_path','source_line','manuscript','corrected','kind','reason'],el)
    fr_ids=[e['id'] for e in allentries['fr']];en_ids=[e['id'] for e in allentries['en']]
    assert fr_ids==en_ids,'Paired editorial variants do not agree'
    footers=[]
    for mf,me in zip(allmeta['fr'],allmeta['en']):
        assert len(mf['footers'])==len(me['footers']),mf['package']
        for f,e in zip(mf['footers'],me['footers']):
            assert f['scan']==e['scan'] and f['number']==e['number']
            rec={k:f[k] for k in ('package','cote','scan','source_line','text','number')}
            rec['english_source_line']=e['source_line'];rec['source_status']='comment' if f['comment'] else 'printed'
            for reader in ('LM_FR_diplomatique','LM_FR_corrige_apparat','LM_FR_texte_de_lecture','LM_EN_corrected_apparatus','LM_EN_reading'):rec[reader]=f['action']
            footers.append(rec)
    write_tsv(records/'ARCHIVE_FOOTERS.tsv',['package','cote','scan','source_line','english_source_line','source_status','text','number','LM_FR_diplomatique','LM_FR_corrige_apparat','LM_FR_texte_de_lecture','LM_EN_corrected_apparatus','LM_EN_reading'],footers)
    report=['# Apparatus counts','', 'Counts cover effective authorial cancellations and insertions. A revision wholly inside an enclosing cancellation is subsumed in the enclosing entry, whose manuscript reading preserves it exactly. No new doubtful reading has been resolved.','', '| Language | Cote | Deletions | Insertions | Total |','|---|---|---:|---:|---:|']
    for language,es in allentries.items():
        for cote in ('140-1','140-2','140-3','140-4'):
            co=collections.Counter(e['kind'] for e in es if e['cote']==cote)
            report.append(f"| {language.upper()} | {cote} | {co['deletion']} | {co['insertion']} | {sum(co.values())} |")
    report.extend(['', 'The corrected-apparatus and annotated-master forms print one entry per listed variant. Diplomatic and reading forms print no apparatus entries. Reading forms retain residual uncertainty markers for cancelled passages; these are not new textual readings.','', 'Any later contextual slips or layout-placement variants must be added to these totals by the final build.'])
    (records/'APPARATUS_COUNTS.md').write_text('\n'.join(report)+'\n')
    summary={l:{'packages':len(allmeta[l]),'scans':sum(len(m['scan_sequence']) for m in allmeta[l]),'variants':len(allentries[l]),'kinds':dict(collections.Counter(e['kind'] for e in allentries[l])),'footers':sum(len(m['footers']) for m in allmeta[l]),'subsumed_edits':sum(m['subsumed_edits'] for m in allmeta[l]),'source_round_trip':'PASS'} for l in ('fr','en')}
    (data/'editorial_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
