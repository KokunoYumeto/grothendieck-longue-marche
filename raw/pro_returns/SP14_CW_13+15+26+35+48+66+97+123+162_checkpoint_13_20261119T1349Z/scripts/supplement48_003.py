import sys,json
from pathlib import Path
sys.path.insert(0,'out/scripts');from work import render,now
p=Path('out/decisions/H48-01_48_scan003.json');d=json.loads(p.read_text())
for place,c,h,final,ink in [
('chapter and title rules','underlined Chap. VI; overline on VI; title underlined','no rules','underlined Chap. VI; overline on VI; title underlined','chap/title1/oldtitle crops: heavy lower stroke beneath chapter rubric, upper bar over VI, long fine rule beneath the entire title.'),
('section8 number punctuation','colon','none','colon','whole/s8: two separated points follow8.'),
('section9 number punctuation','period','none','period','whole/s9: a small separate point stands just after9.'),
('section12 number punctuation','period','none','period','s12: a low detached dot follows12.'),
('lower C heading ending','period after fini','no period','period after fini','ptsfini: a detached black point stands to the right of the underlined final word.')]:
 d['changes'].append(dict(place=place,c=c,h=h,final=final,ink=ink,confidence='high',against_c=False,against_h=True,kind='drawing or diagram' if 'rules' in place else 'omission',marked_in_H='no'))
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with Path('out/progress.log').open('a') as f:f.write('cote48 scan003 completion-log supplement '+now()+' before proceeding: title rules and four punctuation differences\n')
render()
