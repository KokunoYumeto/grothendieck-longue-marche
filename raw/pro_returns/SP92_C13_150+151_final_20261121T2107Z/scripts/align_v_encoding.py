"""Before blind sealing, align one handwritten alphabet's TeX encoding.

This changes no readings and never changes either witness excerpt.
The source glyphs and every substantive local distinction remain recorded.
"""
from pathlib import Path
import re, json, csv
from datetime import datetime, timezone

W=Path(__file__).resolve().parents[1]
assert not (W/'second/first_reading_hashes.tsv').exists()
pattern=re.compile(r'\\mathcal\s*\{V\}|\\mathcal\s+V(?![A-Za-z])')
def align(s):return pattern.sub(' V',s)
fields={'final','reading','alternatives','first_words_or_objects'}
def selected(obj):
    if isinstance(obj,list):return [selected(x) for x in obj]
    if not isinstance(obj,dict):return obj
    result={}
    for k,v in obj.items():
        if k in fields:
            if isinstance(v,str):v=align(v)
            elif isinstance(v,list):v=[align(x) if isinstance(x,str) else x for x in v]
        elif isinstance(v,(dict,list)):v=selected(v)
        result[k]=v
    return result

changed=[]
for f in sorted((W/'pages').glob('*.tex')):
    p=W/'records'/f.name
    original=p.read_text();updated=align(original)
    if updated==original:continue
    p.write_text(updated);f.write_text(updated)
    rp=p.with_suffix('.json');r=selected(json.loads(rp.read_text()))
    r['style_encoding']='Rounded handwritten V encoded uniformly as V after root cross-page image comparison; witness excerpts preserved. This is not a reading change.'
    rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    with (W/'second'/f'{p.stem}_first.tsv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=['box','reading'],delimiter='\t',extrasaction='ignore')
        writer.writeheader();writer.writerows(r['second_boxes'])
    changed.append(p.stem)
p=W/'notation.md';p.write_text(align(p.read_text()))
stamp=datetime.now(timezone.utc).isoformat()
note=f'''# Cross-page notation comparison before blind sealing

Root comparison at {stamp}. All candidate pages had already been read and the relevant local crop evidence reviewed. The existing crops for150_scan079 formula60,095 formula94,096 formula98,097 formula101,098 formula107 and099 formula109 were reopened together for the recurring rounded V. Each has the same rounded bottom and outward upper return; no contrasting V alphabet is established in these pages. The later four candidates had retained witness C's calligraphic macro, while the rest used plain V. Their encoding has now been aligned to V, consistently with the table begun on079. This is a macro representation change only: neither witness excerpt nor any reading-change count was altered. The page files, candidate records, final-reading fields and still-unsealed first-reading TSVs were updated together. Pages affected: {', '.join(changed)}.

Other differences were checked during root's recorded local crop review: phi with a projecting stem is retained where written, while the oval0 on094 and the slashed empty-set forms elsewhere remain distinct; loc! with a separate point is retained on089,091,097, while the raised crossed t on095 stays raised t. The doubtful flat/natural superscripts on087 and098 remain local doubts; their different cancellation alternatives reflect different surviving strokes, not competing global conventions. Horizontal limits, arrowed limits, hooks with and without heads, long continuation rules and separate points retain the locally observed distinctions. The open G-shaped group glyph is consistent across all live occurrences on151003,005,007; crossed labels retain their own doubts. The clear sigma3 slip on003 is not harmonized to the clear sigma1 on005/007. The1|3 ambiguity at005's final formula was resolved only after its full-formula crop and the recorded coordinate check. No unfamiliar reader receives this comparison or the notation table in the blind phase.
'''
(W/'records/notation_consistency.md').write_text(note)
with (W/'progress.log').open('a') as out:out.write(f'Cross-page notation encoding aligned {stamp}; rounded V only; no reading changed and no witness excerpt edited.\n')
print('Aligned:',','.join(changed))
