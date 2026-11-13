#!/usr/bin/env python3
"""Reproducible concordance of supplied terminology against aligned package paragraphs.
Run from the edition workspace: python work/scripts/glossary_audit.py.
Source references in outputs use paths inside the source ZIPs.
"""
from __future__ import annotations
import csv,json,re,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'sources'
OUT=ROOT/'work'

def records(name):
    out=[]
    for line in (SRC/'en/glossary'/name).read_text(encoding='utf-8-sig').splitlines():
        if line.strip() and not line.startswith('#'):
            out.append([x.strip() for x in re.split(r'\s;;(?:\s|$)',line)])
    return out

def uncomment(s):
    return re.sub(r'(?<!\\)%[^\n]*','',s)

def prose(s):
    s=uncomment(s)
    # Preserve wording in math text boxes, but not mathematical identifiers.
    maths=[]
    def math(m):
        maths.append(m.group(0));return ' ◇ '
    s=re.sub(r'\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$.*?(?<!\\)\$',math,s,flags=re.S)
    # The detached text is concordance evidence only, never a text replacement.
    inner=' '.join(re.findall(r'\\(?:text|textit|textup|mbox|textrm|hbox)\{([^{}]*)\}',' '.join(maths)))
    s+=' '+inner
    s=re.sub(r'\\(?:scanpage|mspage|illegible)\{[^{}]*\}',' ',s)
    s=re.sub(r'\\(?:begin|end)\{[^{}]*\}',' ',s)
    s=re.sub(r'\\[A-Za-z@]+\*?','',s)
    s=s.replace('{','').replace('}','').replace('~',' ').replace('\\',' ')
    return re.sub(r'\s+',' ',s).strip()

def scans(s):
    ms=list(re.finditer(r'\\scanpage\{([^}]+)\}',s));out=[]
    for i,m in enumerate(ms):
        end=ms[i+1].start() if i+1<len(ms) else len(s)
        out.append((m.group(1),m.start(),s[m.start():end]))
    return out

def french_matches(s,entries):
    spans=[]
    for name,rx,*_ in entries:
        if rx=='-':continue
        for m in re.finditer(r'(?<![^\W\d_])(?:'+rx+')',s,re.I):
            spans.append((name,m.start(),m.end(),m.group(0)))
    return [(n,a,b,w) for n,a,b,w in spans if not any(n!=n2 and a2<=a and b<=b2 and b2-a2>b-a for n2,a2,b2,w2 in spans)]

def main():
    entries=records('entries_LM.txt');terms={a[0]:a[1:] for a in records('terms_LM.txt')}
    assert len(entries)==116 and len(terms)==117
    # Additional supplied decision absent from the attached French matching table.
    entries.append(['automorphisme à lacets',r'(?:automorphismes?|homomorphismes?|isomorphismes?|autom\.?|hom\.?|isom\.?) (?:à|a) lacets','loop automorphism; loop homomorphism; loop isomorphism','en/glossary/terms_LM.txt','Additional decision; supplied in terms but absent from entries.'])
    manifest=json.loads((SRC/'en/MANIFEST.json').read_text())
    details=[];summary={a[0]:{'french_occurrences':0,'english_candidates':collections.Counter(),'unmatched_paragraphs':0,'references':collections.defaultdict(list)} for a in entries}
    unpaired=[];scancount=0
    for meta in manifest['packages']:
        pkg=meta['package'];fr=(SRC/'fr/texts'/(pkg+'.tex')).read_text();en=(SRC/'en/packages'/(pkg+'_en.tex')).read_text()
        fs=scans(fr);es=scans(en);assert [x[0] for x in fs]==[x[0] for x in es]
        for (scan,fpos,ft),(scan2,epos,et) in zip(fs,es):
            scancount+=1
            fp=[p for p in re.split(r'\n\s*\n',uncomment(ft)) if p.strip()]
            ep=[p for p in re.split(r'\n\s*\n',uncomment(et)) if p.strip()]
            if len(fp)!=len(ep):
                unpaired.append({'package':pkg,'cote':meta['cote'],'scan':scan,'french_paragraphs':len(fp),'english_paragraphs':len(ep)})
                pairs=[('scan',ft,et)]
            else:pairs=[(i+1,a,b) for i,(a,b) in enumerate(zip(fp,ep))]
            for para,a,b in pairs:
                af,bf=prose(a),prose(b)
                fm=french_matches(af,entries)
                byname=collections.defaultdict(list)
                for n,st,en_,w in fm:byname[n].append(w)
                for n,words in byname.items():
                    if n not in terms:continue
                    rx=terms[n][1];matches=list(re.finditer(rx,bf,re.I)) if rx!='-' else []
                    forms=[m.group(0).lower().strip() for m in matches]
                    data=summary[n];data['french_occurrences']+=len(words)
                    if not forms:data['unmatched_paragraphs']+=1
                    for form in forms:
                        data['english_candidates'][form]+=1
                        ref=f"{meta['cote']}:{scan} ({pkg}, paragraph {para})"
                        if ref not in data['references'][form]:data['references'][form].append(ref)
                    details.append({'term':n,'package':pkg,'cote':meta['cote'],'scan':scan,'paragraph':para,'french_forms':' | '.join(words),'english_candidates':' | '.join(forms),'french_context':af,'english_context':bf,'method':'aligned paragraph' if para!='scan' else 'whole scan fallback'})
    dpath=OUT/'records/GLOSSARY_CONCORDANCE.tsv';dpath.parent.mkdir(parents=True,exist_ok=True)
    with dpath.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(details[0]),delimiter='\t');w.writeheader();w.writerows(details)
    result={'glossary_entries':116,'translation_term_lines':117,'scan_blocks':scancount,'source_packages':len(manifest['packages']),'alignment_fallbacks':unpaired,'entries':{n:{**d,'english_candidates':dict(d['english_candidates']),'references':dict(d['references'])} for n,d in summary.items()}}
    (OUT/'data/glossary_concordance.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    short=[]
    for n,d in summary.items():
        if len(d['english_candidates'])>1:
            short.append(n+': '+', '.join(f'{a} ({b})' for a,b in d['english_candidates'].most_common()))
    (OUT/'data/glossary_candidate_forms.txt').write_text('\n'.join(short)+'\n')
    print(json.dumps({'packages':len(manifest['packages']),'scan_blocks':scancount,'terms':len(entries),'concordance_rows':len(details),'paragraph_alignment_fallbacks':len(unpaired),'terms_with_multiple_literal_candidates':len(short)}))
if __name__=='__main__':main()
