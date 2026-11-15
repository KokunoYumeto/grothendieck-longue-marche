from pathlib import Path
import csv,json,re
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_11_002-042'

def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def macro_args(s,macro):
    key='\\'+macro+'{'; start=0
    while True:
        i=s.find(key,start)
        if i<0: return
        j=i+len(key); k=j; depth=1
        while k<len(s) and depth:
            if s[k]=='{' and (k==0 or s[k-1]!='\\'): depth+=1
            elif s[k]=='}' and (k==0 or s[k-1]!='\\'): depth-=1
            k+=1
        yield i,s[j:k-1]
        start=k

def rebuild():
    records=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('page[0-9][0-9][0-9].json'))]
    fields=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
    with (ROOT/(PREFIX+'_inventory.csv')).open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for r in records:
            for n,(kind,pos,first) in enumerate(r['elements'],1):
                w.writerow(dict(cote='11',scan=r['scan'],sheet_kind=r['sheet_kind'],element=f'{n:02}',kind=kind,position=pos,first_words_or_objects=first,transcribed='yes'))
    notation=(ROOT/'records/notation.md').read_text(encoding='utf-8')
    out=[notation,'\n## Doubts\n\nPositions refer to the source block comments in the page fragments; numbers after “TeX line” are locators in those fragments, not manuscript line numbers. All uncertain readings remain visibly marked in the transcription. Confidence concerns the proposed reading: low includes competing glyphs, long weak phrases, cancellations and the most crowded passages; medium means one proposed reading with some unresolved strokes. No uncertain reading is promoted to high confidence merely because it fits the mathematics.\n\n| Cote | Scan | Approximate line / position | Reading | Alternatives | Confidence |\n|---|---|---|---|---|---|']
    for r in records:
        s=(ROOT/'pages'/f'{PREFIX}_11_scan{r["scan"]:03}.tex').read_text()
        for macro in ['unsure','illegible']:
            for idx,arg in macro_args(s,macro):
                pos=s[:idx].count('\n')+1
                reading,sep,alt=arg.partition('|')
                if macro=='illegible': reading=f'Physically unreadable: approximately {arg} word(s)'; alt=''; conf='low'
                else:
                    in_deletion=any(di < idx < di+len(da)+len('\\deleted{}') for di,da in macro_args(s,'deleted'))
                    conf='low' if sep or in_deletion or len(reading)>28 or r['scan'] in (21,34,42) else 'medium'
                esc=lambda x:x.replace('|','&#124;').replace('\n',' ')
                out.append(f'| 11 | {r["scan"]:03} | TeX line {pos} | `{esc(reading)}` | `{esc(alt)}` | {conf} |')
    out.append('\n## Abbreviations encountered\n\n'+(ROOT/'records/abbreviations.md').read_text())
    out.append('\n## Legibility and trust\n\nAll 39 retained scan pages were read visually by the same reader, first as a whole and then in both supplied full-resolution halves; all 39 received a second visual reading against their fragments before the freeze. Additional crops and rotations were used for small or sideways writing, with no OCR and no context material. The reused typescript is generally clearer than the handwriting, but its inserted formulas, uneven strikes and superposed letters still carry doubts. The audit is a second pass by the original reader, not an independent human authentication.\n\nThe weakest areas are the compressed parenthesis on 003, heavily revised formula labels on 005 and 013, the subcategory margin on 021, the transition into the Poincaré definitions on 027, the sign correction and abbreviated prose on 029, the small lower and marginal writing on 034, the argument notation on 038, and the crowded Poincaré sentence, tiny degree subscript and top/margin notes on 042. Cancelled wording is frequently less secure than the live line. These places remain transcribed with explicit tentative readings rather than being completed from expected mathematics. No claim is made that the remaining unmarked wording is error-free.\n\nIndex order, surprising degree bounds, repeated words, mismatched source/target expressions and the author’s own grammatical slips have been preserved where the ink supports them. The register and each local doubt distinguish the observed form from an alternative; the later research notes can raise new reading questions but cannot change the frozen transcription.\n')
    (ROOT/(PREFIX+'_doubts.md')).write_text('\n'.join(out),encoding='utf-8')

def save_page(scan,tex,elements,sheet_kind='text',observations=''):
    p=ROOT/'pages'/f'{PREFIX}_11_scan{scan:03}.tex'
    if p.exists(): raise RuntimeError('Use explicit revision, not duplicate completion')
    p.write_text(tex.strip()+'\n',encoding='utf-8')
    (ROOT/'records'/f'page{scan:03}.json').write_text(json.dumps(dict(scan=scan,sheet_kind=sheet_kind,elements=elements),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    rebuild()
    if observations:
        with (ROOT/'records/transcription_observations.md').open('a',encoding='utf-8') as f: f.write(f'\n## Scan {scan:03}\n\n{observations}\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f: f.write(f'11 scan {scan:03} done {now()}\n')
    print(f'Saved scan {scan:03}; {len(elements)} inventory elements; {now()}')
