"""Repair TeX token boundaries after V encoding alignment; no reading change.

The sealed first TSVs remain byte-for-byte unchanged. Their corresponding
canonical final-box representations are recorded separately for audit use.
"""
from pathlib import Path
import re,json,csv,datetime
W=Path(__file__).resolve().parents[1]
pat=re.compile(r'(?<!\\)\\(qquad|Longleftrightarrow|cap|cup)V(?![A-Za-z])')
def fix(s):return pat.sub(lambda m:'\\'+m[1]+' V',s)
def fields(obj):
    if isinstance(obj,list):return [fields(x) for x in obj]
    if not isinstance(obj,dict):return obj
    out={}
    for k,v in obj.items():
        if k in {'C','H','second_boxes','first','second'}:out[k]=v;continue
        if k in {'final','reading','first_words_or_objects'} and isinstance(v,str):v=fix(v)
        elif isinstance(v,(dict,list)):v=fields(v)
        out[k]=v
    return out
changed=[];box_representations={}
for p in sorted((W/'pages').glob('*.tex')):
    old=p.read_text();new=fix(old)
    if new==old:continue
    p.write_text(new);(W/'records'/p.name).write_text(new)
    rp=W/'records'/f'{p.stem}.json';r=fields(json.loads(rp.read_text()));rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    changed.append(p.stem)
    for b in csv.DictReader((W/'second'/f'{p.stem}_first.tsv').open(),delimiter='\t'):
        final=fix(b['reading'])
        if final!=b['reading']:box_representations.setdefault(p.stem,{})[b['box']]=final
(W/'records/v_encoding_repairs.json').write_text(json.dumps(box_representations,ensure_ascii=False,indent=2)+'\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (W/'records/notation_consistency.md').open('a') as out:
    out.write(f'\nStatic TeX token inspection at {stamp} found missing lexical spaces after qquad, Longleftrightarrow, cap and cup where removal of a preceding mathcal command had joined the following V to that command name. Those spaces were repaired in final page representations and current final-reading fields. This is an encoding repair only, with no changed symbol or reading. The already sealed first TSVs were not edited: their exact bytes are retained for the blind comparison, and the corrected box representations are listed in records/v_encoding_repairs.json. No compilation was performed.\n')
with (W/'progress.log').open('a') as out:out.write(f'Static V token-boundary repair {stamp}: {", ".join(changed)}; sealed first readings untouched; no reading changed.\n')
print(changed,box_representations.keys())
