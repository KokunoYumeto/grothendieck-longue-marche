from pathlib import Path
import json,datetime
p=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_071/R2')
r=json.loads((p/'report.json').read_text())
def clean(v):
 if isinstance(v,str): return v.replace("\\'", "'")
 if isinstance(v,list): return [clean(x) for x in v]
 if isinstance(v,dict): return {k:clean(x) for k,x in v.items()}
 return v
r=clean(r)
by={d['id']:d for d in r['differences']}
by['R2-10'].update(c=r'\mathcal F',h=r'\mathfrak{F}',reading=r'\mathcal F')
by['R2-30'].update(c='M',h=r'\mathcal{M}',reading='M')
by['R2-34'].update(c='x',h='X',reading='x')
# Graphic rows refer only to their named graphic components; neighbouring words are independently collated.
by['R2-05']['reading']='% R2-margin-marks in reading.tex: the two groups of \\fill and \\draw commands only.'
by['R2-09']['reading']=r'\draw (5.32,-0.04) .. controls (5.85,0.13) and (6.75,0.31) .. (7.08,0.54);'
by['R2-16']['reading']=r'\draw (1.91,0.33)--(1.96,0.49)--(2.03,0.38);'
tex=(p/'reading.tex').read_text()
start=tex.index(r'\unsure{\begin{tikzpicture}')
end=tex.index(r'\end{tikzpicture}}',start)+len(r'\end{tikzpicture}}')
by['R2-20']['reading']=tex[start:end]
by['R2-25']['reading']='% R2-cancelled-draft in reading.tex: rotated placement of the eight text nodes and all following \\draw commands (boundary and cancellation strokes).'
for x in r['c_doubts']:
 if x['location'] in ['Leftmost marginal group','Second marginal group']:
  x['reading']=by['R2-05']['reading']
 if x['location']=='Restatement, punctuation after leq': x['reading']=by['R2-20']['reading']
r['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z')
(p/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
with (p/'inspection_log.txt').open('a') as f:
 f.write('Final report consistency correction: literal apostrophes in source quotations restored; repeated alphabet rows scoped only to their glyphs; drawing rows scoped only to named marks/layout. No new image views or mathematical checks.\nFinal completion UTC: '+r['finished_utc']+'\n')
print('Complete: 38 differences; 28 C/context dispositions; 26 inventory entries; 17 remaining doubts; 20 own crops. No compilation or mathematical validation.')
