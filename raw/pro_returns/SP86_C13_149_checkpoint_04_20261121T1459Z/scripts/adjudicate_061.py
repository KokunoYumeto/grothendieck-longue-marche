"""Root visual adjudication of all ten different scan-061 boxes."""
import json
from pathlib import Path
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan061';p=B/'pages'/f'{page}.tex';rp=B/'reviews'/f'{page}.json'
r=json.loads(rp.read_text());assert not r.get('audit');t=p.read_text()
for a,b in [(r'est $=$ vrai',r'est $\unsure{=|\overline m}$ vrai'),(r'\deleted{signifie}',r'\deleted{\unsure{signifie}}')]:
 assert t.count(a)==1;t=t.replace(a,b)
p.write_text(t)
c={x['id']:x for x in r['changes']}
c['P01'].update(final=r'$\unsure{=|\overline m}$',against_C=False,confidence='medium',evidence='A detached short upper bar lies above a lower stroke with a deep left cup, a central rise and a long flat right return. This recurring prose shorthand admits both the equals and compressed barred-m readings; the crop leaves its glyph identity open. The abbreviation remains unexpanded.')
for d in r['decisions']:
 if d['id']=='M1166':d.update(decision='undecided',reading=c['P01']['final'],evidence=c['P01']['evidence'],crop='crops/149_scan061_B02_second.png (767,169,1128,270)',confidence='medium')
sigev='The straight cancellation crosses the full baseline word. The initial looping s, dotted i, g oval and long descender, and later f-like long stroke remain visible, but the thin internal n/i and final e strokes merge with the cancellation and with the inserted q descender. Signifie is retained under a whole-word doubt; the live comma and raised implique remain outside its cancellation.'
r['doubts'].extend([dict(place='line 2, prose shorthand',reading=c['P01']['final'],alternatives=r'=|\overline m',reason=c['P01']['evidence'],confidence='medium'),dict(place='line 6, cancelled signifie',reading=r'\deleted{\unsure{signifie}}',alternatives='signifie remains tentative under cancellation',reason=sigev,confidence='medium')])
for x in r['inventory']:
 if x['element']=='E04':x['first_words_or_objects']=r'\deleted{\unsure{signifie}}'
r['deletion_insertion_review'][1]=sigev
for h in r['hand']:
 if h['form']=='=':h.update(form=r'\unsure{=|\overline m}',observation=c['P01']['evidence'])
for n in r['notation']:
 if n['form']=='=':n.update(form=r'\unsure{=|\overline m}',meaning='Two-level prose shorthand with cupped lower entrance; the glyph remains uncertain and is not expanded.')
r['notes'].append('Blind audit: the prose shorthand is reopened, and the cancelled signifie is marked uncertain because its internal and final strokes remain overlapped. The whole formulas retain the observed upper Gamma-circle and lower Gamma_0 placements. The word sequences qu\'on a alors and d\'une action are confirmed by their local letter strokes.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(n,decision,evidence):D[n]=dict(keep_first=True,changed=False,decision=decision,evidence=evidence)
def change(n,final,decision,evidence):D[n]=dict(final=final,changed=True,decision=decision,evidence=evidence)
change('B02',r'est $\unsure{=|\overline m}$ vrai','Reopen the two-level shorthand',c['P01']['evidence'])
keep('B04','Retain the inserted word with its baseline context','The raised f, dotted i, crossing x and low e are clear. A curved leader reaches the gap between baseline point, with p descender and dotted i, and sera, with its initial looped s and low continuation. The second reading quotes only the inserted word; its attachment agrees with this position.')
keep('B05','Retain the des/de ending doubt','The d oval and tall loop join a low e body. The thick terminal return could include s, but the individual contour remains inseparable. The following pts has its p descender, tall t and short upper cross-stroke.')
change('B06',r'\deleted{\unsure{signifie}}\inserted{implique},','Qualify the crossed word',sigev)
keep('B07','Retain qu\'on a alors','The first letter has a closed q bowl and long descender, followed by a low u run and high apostrophe. A separate low on run and a small a-like curved body precede alors. The two visible separated groups after the apostrophe support qu\'on a; the opening has no separately dotted i or s sequence for puisque.')
keep('B08','Retain the formula and comma','Pi, the raised Gamma with its higher round loop, two equality bars, parenthesized 1 and the separate comma are visible. Dollar delimiters and the second reading\'s parenthesis math delimiters surround the identical formula tokens.')
keep('B09','Retain the lowered zero in the Gamma exponent','The round zero is beside the lower end of the raised Gamma. Equality and L with dotted lower i follow. Both readers transcribe precisely this lowered mark; only math delimiters differ.')
keep('B10','Retain full hautement without an added stop','Two elevated quote ticks precede h. After the first tall crossed t, the low e, separate long m/n run and second terminal t support hautement. The tiny detached mark sits above the word baseline, with a weak small footprint compared with the terminal stroke. Its position and weight do not establish a following full stop.')
keep('B12','Retain d\'une action','After d and the apostrophe the short word has several low joined u/n/e strokes. The next word has a small a/c opening, a tall t loop, a separate i dot, rounded o and long n return. This sequence supports action and does not supply the repeated e/v/m run of relèvement.')
keep('B13','Retain the tentative abbreviated tt under the strike','Gamma is followed by a compact crossed group with two upright ends and a low joining stroke. The sloping strike obscures its internal detail. No separate o bowl and u minims are recoverable; tt stays tentative and is not expanded to tout. Entier and the comma lie to the right outside the strike.')
main(dict(page=page,root_viewed=[f'crops/{page}_{n}_second.png' for n in D],decisions=D));record(page);assign('reader_b')
