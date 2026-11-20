from pathlib import Path
from datetime import datetime, timezone
import json,re
p=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_070/R2')
r=json.loads((p/'report.json').read_text())
s=(p/'reading.tex').read_text()
for d in r['differences']:
    if d['kind'].startswith('readable ink left as '): d['kind']=r'readable ink left as \ill{}'
hsource=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_070/H.tex').read_text()
next(d for d in r['differences'] if d['id']=='D21')['h']=hsource.split('\\quad ',1)[1].split('}\n',1)[0]
byname={Path(c['path']).stem:c for c in r['crops']}
cd=next(d for d in r['c_doubts'] if d['id']=='CD29')
cr=byname['c07_worked_adjective'];cd.update(crop=cr['path'],bbox=cr['bbox'],bbox_image=cr['source'])
cd['secondary_crop']=byname['c11_definition_corrections']['path']
cd['scan_shows']='The quoted word is clear in c07_worked_adjective; the separate lower comparables is clear in c11_definition_corrections. Neither is used to fill the worked middle of the earlier adjective.'
next(d for d in r['c_doubts'] if d['id']=='CD06')['secondary_evidence']={'bbox_image':r['image_views'][2],'bbox':[305,1010,1570,1195],'description':'C5 G, single-prime F and ssi were read in the lower supplied half; c16 concerns the separate NB X case.'}
# Structural checks only. No compilation or mathematical validation.
assert s.startswith('\\scanpage{70}\\mspage{69}')
assert '\\cotefile' not in s
clean='\n'.join(line.split('%',1)[0] for line in s.splitlines())
level=0
for i,ch in enumerate(clean):
    if ch in '{}':
        n=0;j=i-1
        while j>=0 and clean[j]=='\\':n+=1;j-=1
        if n%2: continue
        level+=1 if ch=='{' else -1
        assert level>=0,('Unmatched brace',i)
assert level==0
assert clean.count('$')%2==0
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
    op,env=m.groups()
    if op=='begin':stack.append(env)
    else:assert stack and stack.pop()==env,('Environment mismatch',env)
assert not stack
assert s.count('\\unsure{')==len(r['remaining_doubts'])==17
assert s.count('Soit $F\'\\preceq F$')==1
assert s.count('On sera amené')==1
assert s.count('Reporter après')==1
kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
for d in r['differences']:
    assert d['kind'] in kinds,(d['id'],d['kind'])
    for k in ['change_c','change_h','math_consequential']:assert type(d[k]) is bool,(d['id'],k)
    assert d['marked_in_h'] in ['yes','no']
    assert d['change_c'] or d['change_h']
    assert d['bbox'] and len(d['bbox'])==4
    if d['crop']:assert Path(d['crop']).exists()
    for k in ['c','h','reading']:assert "\\'" not in d[k],(d['id'],k)
for d in r['c_doubts']:
    assert d['status'] in ['resolved','retained','revised']
    if d['crop']:assert Path(d['crop']).exists()
for item in r['inventory']:
    assert item['kind'] in ['text','display','diagram','drawing','margin note','insertion','deletion']
    assert item['sheet_kind']=='text' and item['hand']=='his hand' and item['transcribed']=='yes'
for c in r['crops']:assert Path(c['path']).exists()
assert len({c['path'] for c in r['crops']})==16
assert len({d['id'] for d in r['differences']})==45
observations=[
'Bowed first relation and comma after (subdivision) visible. Très/trs and the reduced two-part aura remain uncertain; rel has no detached point.',
'Cancelled noun has accented e, l and a later upright; the long strike hides the ending, retained as éléments/élémen.',
'F prime and F double prime are raised above figures. The worked relation plus short dash is separate; cancellation versus retracing remains open. The long oblique arm is distinct. The following en-like group and reduced descender-led word remain uncertain.',
'Opening curved parenthesis, dotted i, low point, e-like stroke and detached final point establish (i.e. Capital Subdivisions visible. F is followed by a comma without closing parenthesis.',
'Two parallel repetition strokes before figure and the comma after F are clear. Inf and its terminal point are present.',
'Final subdivision has no independently visible plural s. Second prose F has three distinct prime ticks, whereas the first has one.',
'One underlined worked adjective has comp and bles readable, central old/final letters unresolved. Cancelled clause contains secure que but uncertain first and final groups. Quoted compatibles uses paired strokes; vu is clear.',
'Four F objects and four bowed relations are visible. Sole right-hand F is at the upper F prime level; lower-right sign ends into blank space. Upper-right sign has an extra upper diagonal, not a separately readable complete older glyph.',
'Entire rotated oblique note read as On sera amené à renforcer encore cette condition sur les contrées modérées ! Highest continuation and lowest final word fit within the saved original rectangle.',
'Double underlines below contrée/contrie and modérée are explicit. The first word remains uncertain at its penultimate mark.',
'Subdivisions is on the ordinary baseline. A single dense d\'une/d\'un word-sized group precedes the repetition mark; its initial state is uncertain. Lower comparables is clear. Cancelled clause reads Dans le cas qui vient, with final comma.',
'Cancelled on a and two detached diagonal points are visible. Cancelled underlined C5 is readable. No additional cancelled word occurs after donner before aucune.',
'Seul ends after l, with separate stop. First letter of ses/les before relations remains ambiguous. Avec is on the ordinary baseline; final ≤ is straight.',
'Rotated complete lower note: Reporter après C6, C7 with a small closed low oval, ces/mes axiomes de disjonction. First reduced ces/mes group remains open. Underline and both long bars are visible; no continuation is clipped.',
'Two tall stems plus small e give tte. The nearby ssi is a three-letter group. No ou group supports toute.',
'Surviving NB letter is G over F-like older strokes. Equals, X/x without index, membership, and plain M are present. X case and the older F remain uncertain. The target formula is wholly framed; parts of the surrounding upper line are outside the tight rectangle.'
]
log=(p/'inspection_log.md').read_text().split('## Actual crop views')[0]
log+='## Actual crop views\n\nThe following 16 saved crops were each displayed successfully once, in this order. None was truncated in tool output, and none was re-cropped or re-viewed. Each uses the whole scan as its coordinate source.\n\n'
for j,(c,obs) in enumerate(zip(r['crops'],observations),start=4):
    log+=f"{j}. `{c['path']}`\n\n   Source: `{c['source']}`; original bbox `{c['bbox']}`; post-rotation scale `{c['scale']:.8f}`; rotation `{c['rotation']}°`. {c['transforms']}.\n\n   Visible evidence: {obs}\n\n"
now=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
r['finished_utc']=now
r['structural_checks']={'performed':'balanced braces, paired math delimiters, properly nested environments, required markers, 17 uncertainty occurrences matched to 17 remaining-doubt entries, report fields and enum values, boolean types, crop existence and unique IDs','latex_compiled':False,'ocr_used':False,'mathematics_validated':False}
log+=f"## Completion\n\nFinished at {now}. Structural checks passed: balanced braces and math delimiters, nested environments, required scan/page markers, no new cote marker, one complete C5 axiom, all report crop paths present, valid booleans and prescribed inventory/kind values, 17 unsure occurrences with 17 remaining-doubt entries. No LaTeX compilation, OCR, mathematical proof, outside research, or other-reader access was performed.\n"
(p/'inspection_log.md').write_text(log)
(p/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print('Finalized:',now)
print('45 differences; 31 C/context dispositions; 17 remaining doubts; 16 crops; 23 inventory items; 19 total successful image views.')
