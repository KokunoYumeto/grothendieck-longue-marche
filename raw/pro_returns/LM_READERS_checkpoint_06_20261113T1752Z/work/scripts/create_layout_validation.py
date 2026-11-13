"""Validate repaired historical trouble scans in the common book preamble."""
from pathlib import Path
import re,json
from layout_repairs import repair
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'work/layout_probes'
P=ROOT/'work/scripts/book_preamble.tex'
pre=P.read_text();pre=pre.replace('% LUA CODE','\\begin{luacode*}\n'+(ROOT/'work/scripts/book_links.lua').read_text()+'\n\\end{luacode*}')
pre=pre.replace('% CYRILLIC DEFINITIONS','\n'.join(r'\newunicodechar{%s}{{\cyrfont\char"%04X}}'%(c,ord(c)) for c in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'))
pre+=r'\providecommand\LMmathnotice[1]{\textsuperscript{\textcolor{gray}{[M1]}}}'+'\n'
pre+='\n\\LMform=0\n\\begin{document}\n'
recs=json.loads((ROOT/'work/data/layout_pass_sites.json').read_text());want={}
for r in recs:want[(r['cote'],r['scan'])]=r['package']
for lang in ['en','fr']:
 if lang=='en':readers=[ROOT/'sources/draft_readers/LaLongueMarche_English.tex']
 else:readers=[ROOT/f'sources/draft_readers/LM_reader_draft_140-{i}.tex' for i in range(1,5)]
 blocks={}
 for rd in readers:
  t=rd.read_text();ms=list(re.finditer(r'\\scanpage\{(\d+)[^}]*\}',t))
  for i,m in enumerate(ms):
   cote=list(re.finditer(r'\\LMcote\{(140-\d)\}',t[:m.start()]))[-1][1];scan=int(m[1]);key=(cote,scan)
   if key not in want:continue
   end=ms[i+1].start() if i+1<len(ms) else t.index(r'\end{document}',m.end());body=t[m.start():end]
   # Remove only editorial reader section headings that follow the prior scan.
   body=re.split(r'\\subsection\*\{Scans|\\clearpage\s*\\LMcote',body)[0]
   # A terminal package heading can include addcontentsline but no text is lost.
   body=re.sub(r'\\addcontentsline[^\n]*\n','',body)
   body=re.sub(r'% package[^\n]*\n','',body)
   new,changes=repair(body,want[key],lang)
   blocks[key]=new
 parts=[pre]
 for (cote,scan),body in sorted(blocks.items()):
  parts+=['\\clearpage\n\\LMcote{'+cote+'}\n',r'\typeout{LMLAYOUTSCAN '+cote+' '+str(scan)+'}\n',body]
 parts+=['\\end{document}\n'];(D/f'layout_validation_{lang}.tex').write_text(''.join(parts))
 print(lang,'scans',len(blocks))
