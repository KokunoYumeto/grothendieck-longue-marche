r"""Inventory original note contexts and safe deferred-note contents.

Read source packages only. A queue preserves the original mode of each note:
math fragments get explicit math delimiters; text fragments retain their own
inline mathematics. The table is a source-local record, not a blanket scaling
or fitting pass.
"""
import csv, collections, json, re
from pathlib import Path
import editorial

BOXED_ENVS={'tabular','tabular*','tabularx','minipage','tikzpicture','tikzcd','array','picture','matrix','pmatrix','bmatrix','Bmatrix','vmatrix','Vmatrix','gathered','aligned','smallmatrix'}
BOX_MACROS={'hbox':1,'vbox':1,'vtop':1,'mbox':1,'text':1,'makebox':1,'framebox':1,'parbox':2,'raisebox':2,'shortstack':1,'margin':1,'footnote':1,'footnotetext':1,'fbox':1,'colorbox':2,'fcolorbox':3,'overbrace':1,'underbrace':1,'overset':2,'underset':2,'substack':1,'mathclap':1,'mathllap':1,'mathrlap':1,'smash':1,'phantom':1,'hphantom':1,'vphantom':1}


def containers(text):
    mask=editorial.blank_comments(text);envs=[];stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',mask):
        if m[1]=='begin':stack.append((m[2],m.start()))
        else:
            for k in range(len(stack)-1,-1,-1):
                if stack[k][0]==m[2]:
                    name,a=stack[k];envs.append((a,m.end(),name));del stack[k:];break
    boxes=[]
    for m in re.finditer(r'\\('+'|'.join(BOX_MACROS)+r')\b',mask):
        a=m.end();n=0
        for _ in range(BOX_MACROS[m[1]]):
            q=re.match(r'\s*(?:\[[^]]*\]\s*)*',mask[a:]);a+=q.end()
            if a>=len(text) or text[a]!='{':break
            a=editorial.brace_end(text,a);n+=1
        if n==BOX_MACROS[m[1]]:boxes.append((m.start(),a,m[1]))
    return envs,boxes


def inventory(text,package,language):
    info=editorial.package_info(package);envs,boxes=containers(text);counter=collections.Counter();rows=[];inner_pages=[]
    for x in editorial.spans(text,{'margin','mspage'}):
        pos=x['start'];scan=editorial.at_scan(text,pos);mode=editorial.math_mode_at(text,pos)
        es=[n for a,b,n in envs if a<pos<b and n in BOXED_ENVS]
        bs=[n for a,b,n in boxes if a<pos<b]
        kind='math' if mode else ('inner text' if es or bs else 'outer text')
        if x['name']=='mspage':
            if kind!='outer text':inner_pages.append({'package':package,'scan':scan,'context':kind,'argument':x['argument']})
            continue
        counter[scan]+=1;noteid=f"NOTE-{info['cote']}-s{scan:03d}-N{counter[scan]:03d}"
        queue=r'\('+x['argument']+r'\)' if mode else x['argument']
        action=('Defer with a numbered anchor at the original diagram cell; preserve the argument as explicit mathematics.' if mode else
                'Defer with a numbered anchor at the original text label; preserve the argument as text with its existing inline mathematics.' if kind=='inner text' else
                'Measure the source note: retain in the margin when it fits in three lines; otherwise use a breakable labelled block at its anchor.')
        if editorial.URL in x['argument']:
            action='Institutional archive footer excluded in every form; retain the independent source page-number marker. See ARCHIVE_FOOTERS.tsv.'
        rows.append({'id':noteid,'language':language,'package':package,'cote':info['cote'],'scan':scan,
                    'source_path':('fr/texts/'+package+'.tex' if language=='fr' else 'en/packages/'+package+'_en.tex'),
                    'source_line':text.count('\n',0,pos)+1,'context_kind':kind,'math_mode':str(mode).lower(),
                    'environment_context':'; '.join(es),'box_macro_context':'; '.join(bs),
                    'original_argument':x['argument'],'queue_argument':queue,'action':action})
    return rows,inner_pages


def main():
    with Path('sources/fr/records/CURRENT_TEXT_INDEX.tsv').open() as f:packages=[r['package'] for r in csv.DictReader(f,delimiter='\t')]
    rows=[];pages=[]
    for lang in ('fr','en'):
        for package in packages:
            source=Path('sources/fr/texts')/(package+'.tex') if lang=='fr' else Path('sources/en/packages')/(package+'_en.tex')
            rs,ps=inventory(source.read_text(),package,lang);rows.extend(rs)
            pages.extend(dict(p,language=lang) for p in ps)
    fields=['id','language','package','cote','scan','source_path','source_line','context_kind','math_mode','environment_context','box_macro_context','original_argument','queue_argument','action']
    editorial.write_tsv(Path('work/records/MARGINAL_NOTE_CONTEXTS.tsv'),fields,rows)
    summary={lang:dict(collections.Counter(r['context_kind'] for r in rows if r['language']==lang)) for lang in ('fr','en')}
    out={'margin_counts':summary,'mspage_inner_or_math_contexts':pages,'inner_margin_cases':[{k:r[k] for k in fields if k!='original_argument'} for r in rows if r['context_kind']!='outer text']}
    Path('work/data/editorial_margin_contexts.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
