"""Isolated diagram measurements for source-local layout patch discovery."""
from pathlib import Path
import re,json,sys,subprocess,csv
ROOT=Path(__file__).resolve().parents[2]
D=ROOT/'work/layout_probes';D.mkdir(exist_ok=True)
manifest=json.loads((ROOT/'sources/en/MANIFEST.json').read_text())
cov={r['package']:r for r in manifest['packages']}
# Identify scans affected by the previous pass, with exact after-reader source anchors.
targets=[]
for r in csv.DictReader((ROOT/'sources/typeset/TYPESET_PASS_CHANGES.tsv').open(),delimiter='\t'):
 p=ROOT/'sources/draft_readers'/(r['reader']+'.tex'); ls=p.read_text().splitlines(); n=int(r['input line of the reader source']); before='\n'.join(ls[:n]);
 scan=int(list(re.finditer(r'\\scanpage\{(\d+)',before))[-1][1]); cote=list(re.finditer(r'\\LMcote\{([^}]+)',before))[-1][1]
 pkg=next(k for k,p in cov.items() if p['cote']==cote and int(p['scans'].split('-')[0])<=scan<=int(p['scans'].split('-')[1]))
 targets.append({**r,'package':pkg,'cote':cote,'scan':scan,'line_text':ls[n-1]})
(ROOT/'work/data/layout_pass_sites.json').write_text(json.dumps(targets,ensure_ascii=False,indent=2))
# All diagrams in the affected scans, measured at their original size.
wanted={(r['package'],r['scan']) for r in targets}
all_diagrams=[]
for lang,folder,suffix in [('en','en/packages','_en'),('fr','fr/texts','')]:
 for pkg,p in cov.items():
  t=(ROOT/'sources'/folder/(pkg+suffix+'.tex')).read_text()
  for typ in ('tikzcd','tikzpicture'):
   pat=re.compile(r'\\begin\{'+typ+r'\}(.*?)\\end\{'+typ+r'\}',re.S)
   for i,m in enumerate(pat.finditer(t),1):
    scans=list(re.finditer(r'\\scanpage\{(\d+)',t[:m.start()]));scan=int(scans[-1][1]) if scans else 0
    if (pkg,scan) not in wanted: continue
    all_diagrams.append(dict(id=len(all_diagrams)+1,lang=lang,package=pkg,cote=p['cote'],scan=scan,environment=typ,index=i,source_line=t[:m.start()].count('\n')+1,old=m[0]))
(D/'diagrams.json').write_text(json.dumps(all_diagrams,ensure_ascii=False,indent=2))
pre=(ROOT/'sources/build/wrap.tex').read_text().split('\\begin{document}')[0]
pre=pre.replace('marginparwidth=20mm','marginparwidth=20mm,marginparsep=10pt')
pre+=r'''
\setmathfont{Latin Modern Math}
\usepackage{newunicodechar}
\newfontfamily\cyrfont{DejaVu Serif}[Scale=MatchLowercase]
\let\oldGamma\Gamma\renewcommand\Gamma{\ensuremath{\oldGamma}}
\let\oldsimeq\simeq\renewcommand\simeq{\ensuremath{\oldsimeq}}
\renewcommand\margin[1]{\parbox{120pt}{\footnotesize #1}}
\setbox0=\hbox{test}
'''
pre+='\n'.join(r'\newunicodechar{%s}{{\cyrfont\char"%04X}}'%(c,ord(c)) for c in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя')+'\n'
# One isolated TeX file per language minimizes conflict between independent diagrams.
for lang in ('en','fr'):
 parts=[pre+'\\begin{document}\n']
 for d in all_diagrams:
  if d['lang']!=lang: continue
  parts+=['\\typeout{LMSTART '+str(d['id'])+'}\n',r'\setbox0=\hbox\bgroup'+'\n',d['old'],'\n\\egroup\n\\typeout{LMWIDTH '+str(d['id'])+r' \the\wd0 HEIGHT \the\ht0 DEPTH \the\dp0}'+'\n']
 parts+=['\\end{document}\n']
 (D/f'measure_{lang}.tex').write_text(''.join(parts))
print('targeted scans',len(wanted),'diagrams',len(all_diagrams))
