import json,re,difflib
from pathlib import Path
from PIL import Image

ROOT=Path('/workspace/scratch/6d55c8c3e5a7')
OUT=ROOT/'work/readers/025/A'
tex=(OUT/'reading.tex').read_text()
ctex=(ROOT/'work/inputs/025/C.tex').read_text()
report=json.loads((OUT/'report.json').read_text())
body='\n'.join(s.split('%',1)[0] for s in tex.splitlines())

def braced_at(text,start):
    assert text[start]=='{'
    depth=1
    j=start+1
    while depth:
        if text[j]=='{' and text[j-1]!='\\': depth+=1
        if text[j]=='}' and text[j-1]!='\\': depth-=1
        j+=1
    return text[start+1:j-1]

nodes=[]
for match in re.finditer(r'\\node(?:\[[^\]]*\])?\s+at\s+\([^)]*\)\s*\{',body):
    nodes.append(braced_at(body,match.end()-1))
actual=' '.join(nodes)
# Reconstitute the one written opening parenthesis that is drawn geometrically.
actual=actual.replace(r'\inserted{Cond',r'\inserted{(Cond')
expected=ctex.replace(r'\scanpage{25}','')
expected='\n'.join(s.split('%',1)[0] for s in expected.splitlines())
replacements=[
    (r'``surely',r"\unsure{``|'}surely"),
    (r'\deleted{p\unsure{23}}',r'\deleted{p23}'),
    (r'\unsure{not|nor}','not'),
    ('p245.','p245'),
    (r'\unsure{l.14}','l.14'),
    (r'i_{\unsure{0|i}}',r'i_0'),
    (r'$(i_0\colon N)$',r'$(i_{\unsure{0|i}}\colon N)$'),
    (r'\inserted{also};',r';'),
    (r"l12 ``is aspheric''",r"l12 ``is aspheric'' \inserted{also}"),
    (r'``\uline{handwritten}',r"\unsure{``|'}\uline{handwritten}"),
    (r'\deleted{\unsure{-13}}',r'-\deleted{\unsure{13}}'),
    (r'\& \unsure{-}2',r'\& 2'),
    (r'allow\unsure{s}',r'allow\unsure{e|s}'),
    (r"\unsure{'}l12",r"'l12"),
    (r"isn't the use",r"\unsure{isn't|is'nt} the use"),
    (r'\unsure{not} $\pi_0,\pi_1$',r'not $\pi_0,\pi_1$')
]
for old,new in replacements:
    assert old in expected,old
    expected=expected.replace(old,new,1)

def norm(t):
    t=' '.join(t.split())
    return re.sub(r'\s+([:;])',r'\1',t)

text_equal=norm(actual)==norm(expected)
if not text_equal:
    print('\n'.join(difflib.unified_diff(norm(expected).split(),norm(actual).split(),fromfile='C_after_reported_changes',tofile='reading_node_text',lineterm='')))

allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
balance=0
brace_ok=True
for i,ch in enumerate(body):
    if i and body[i-1]=='\\': continue
    if ch=='{': balance+=1
    if ch=='}': balance-=1
    if balance<0: brace_ok=False
brace_ok=brace_ok and balance==0

source_boxes_ok=True
for row in report['changes']+report['c_doubts']:
    assert Path(row['source']).exists()
    w,h=Image.open(row['source']).size
    x1,y1,x2,y2=row['bbox']
    source_boxes_ok=source_boxes_ok and 0<=x1<x2<=w and 0<=y1<y2<=h
    assert row['crop'] is None or Path(row['crop']).exists()
logs=[json.loads(s) for s in (OUT/'crops/crops.jsonl').read_text().splitlines()]
decisions=json.loads((OUT/'crop_decisions.json').read_text())
frozen=json.loads((OUT/'unresolved_before_crops.json').read_text())
crop_once=len(logs)==len(decisions)==len(frozen['loci'])==28 and len({z['output'] for z in logs})==28
crop_widths_ok=all(Image.open(z['output']).size[0]==2400 for z in logs)

result={
 'latex_compilation_attempted':False,
 'brace_balance':balance,
 'braces_balanced':brace_ok,
 'environments':re.findall(r'\\(begin|end)\{([^}]+)\}',body),
 'math_dollar_count':len(re.findall(r'(?<!\\)\$',body)),
 'all_text_matches_C_after_documented_changes':text_equal,
 'text_comparison_note':'Node text was extracted with balanced braces, whitespace collapsed, and the one drawn opening parenthesis reconstituted. Only the explicitly listed reading changes were applied to C. No language correction or silent text change was allowed.',
 'all_change_kinds_allowed':all(z['kind'] in allowed for z in report['changes']),
 'all_C_change_literals_present':all(not z['c'] or z['c'] in ctex for z in report['changes']),
 'all_C_doubt_literals_present':all(z['c'] in ctex for z in report['c_doubts']),
 'all_H_comparisons_absent':all(z['h'] is None and not z['diff_h'] and not z['marked_in_H'] for z in report['changes']),
 'all_evidence_boxes_valid':source_boxes_ok,
 'one_crop_per_frozen_locus':crop_once,
 'all_crops_width_2400':crop_widths_ok,
 'every_generated_crop_displayed_once':all(z['displayed'] and z['display_count']==1 for z in decisions),
 'whole_and_halves_recorded_once':len(report['viewed'])==len(set(report['viewed']))==3,
 'C_explicit_unsure_occurrences':len(re.findall(r'\\unsure\{',ctex)),
 'reading_unsure_occurrences':len(re.findall(r'\\unsure\{',body)),
 'changes':len(report['changes']),
 'C_context_doubt_decisions':len(report['c_doubts']),
 'resolved_or_confirmed_doubt_decisions':sum(z['resolved'] for z in report['c_doubts']),
 'remaining_doubts':len(report['remaining_doubts']),
 'inventory_rows':len(report['inventory']),
 'actual_math_check_events':len(report['math_checks'])
}
(OUT/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
assert brace_ok and text_equal and source_boxes_ok and crop_once and crop_widths_ok
