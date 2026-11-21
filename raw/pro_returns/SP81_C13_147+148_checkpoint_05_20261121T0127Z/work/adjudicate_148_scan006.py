from pathlib import Path
import json
root=Path(__file__).resolve().parents[1];page='148_scan006'
f=root/'work'/f'{page}_final.json';r=json.loads(f.read_text());p=root/'pages'/f'{page}.tex';t=p.read_text()
comp=json.loads((root/'second'/f'{page}_comparison.json').read_text());ds={d['box']:d for d in comp['differences']}
old=ds['B08']['first'];new=ds['B08']['second'].replace('x=0.0024cm,y=-0.0024cm','x=0.0013cm,y=-0.0013cm').replace(r'\end{tikzpicture}',r'\node[anchor=west] at (2430,850) {$\unsure{\phantom{A}}$};'+'\n'+r'\end{tikzpicture}')
new=r'\handwritten{'+new+'}'
assert old in t;t=t.replace(old,new);p.write_text(t)
c=next(c for c in r['changes'] if c['id'].endswith('-02'));c['final']=new;c['crop']=page+'_second_B08.png';c['evidence']+=' The blind crop records short gaps within the large loop, at its rising terminal, in the separate left vertical and along the lower flourish. These interruptions and the forked left end of the lower flourish are now reproduced directly, together with the small upper hook and detached dark marks. No letters are supplied from the printed name.'
r['notes']+=' The blind audit confirms the keyed rows of 13 circumflex marks and 56 equals signs, the two dates, reference number, baseline 3e and marginal 5. The signature drawing now preserves its visible short gaps and forked lower flourish. A very pale trace between lieu and de has no dark keyed-bar footprint comparable to the surrounding type and remains outside the transcription. No claim was mathematically checked.'
f.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
ev={
'B01':('The three letterhead lines and thirteen separate circumflex strokes agree; the second serialization uses textasciicircum for the same keyed marks. The page already preserves that row literally.','high'),
'B03':('Diffusion, Liste A, MA/gs and N° 4375 agree. Line break and spacing commands account for the token difference.','high'),
'B06':('Date,-heure has both a dark comma and hyphen. The pale trace between lieu and de does not have the dark typewriter footprint of the neighboring keyed characters or the clear hyphen. No extra punctuation is added there. The date, time, room number and university line agree.','high'),
'B08':('The signature has a large open loop, inner loop, long rising sweep, detached left vertical, upper hook, short detached marks and a lower flourish with forked left end. Its exposed gaps are now drawn more closely from the independent tracing. The alphabetic name remains unresolved with the same in-place doubt.','medium'),
'B09':('The lower-left numeral has a top bar, descending left segment, horizontal middle and large lower curve: 5. The margin wrapper records its placement without changing that reading.','high')}
choices=[]
for d in comp['differences']:
 it=dict(box=d['box'],choice='literal' if d['box']=='B08' else 'first',changed=d['box']=='B08',evidence=ev[d['box']][0],confidence=ev[d['box']][1])
 if d['box']=='B08':it['final']=new
 choices.append(it)
(root/'work'/f'{page}_audit_choices.json').write_text(json.dumps(dict(reader='audit_c',choices=choices),ensure_ascii=False,indent=2)+'\n')
