"""One-shot root decisions for 042 blind differences."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1];p='149_scan042';rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text());pp=R/'pages'/f'{p}.tex';s=pp.read_text();cmp={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())};f={b:x['first'] for b,x in cmp.items()}
repls=[(r'\unsure{en}',r'\unsure{en|sur}'),(r"\unsure{\pi_{\overline{K'}}|\pi^{\wedge}_{K'}}",r"\unsure{\pi_{\overline{K'}}|\pi^{\wedge}_{K'}|\pi_{\widehat K'}}"),(r'\unsure{\pi_{\overline K}|\pi^{\wedge}_K|\pi^{\wedge}_{\overline K}}',r'\unsure{\pi_{\overline K}|\pi^{\wedge}_K|\pi^{\wedge}_{\overline K}|\pi_{\widehat K}}'),(r"\unsure{n'auront|n'auraient}","n'auront"),('manifestement','manifeste-ment')]
for old,new in repls:
 assert old in s,old;s=s.replace(old,new,1)
 for b in f:f[b]=f[b].replace(old,new)
pp.write_text(s)
def coords(b):return next(x['coords'] for x in r['audit_boxes'] if x['box']==b)
r['rows'][2].update(final=r'\deleted{\unsure{en|sur}}',scan_shows='The short old word is densely crossed. The left rounded remnant and low joined middle support en, while a three-letter sur division is also possible. Add sur without resolving the cancellation.',crop=f'crops/{p}_second_B03.jpg',box=coords('B03'))
for i,j in [(3,1),(4,2)]:
 r['rows'][i]['final']=repls[j][1];r['rows'][i]['scan_shows']+=' Blind audit: a hat attached directly to K is also explicitly admitted because the mark lies over the lowered letter; the bar reading remains primary.'
r['rows'][5].update(final="n'auront",scan_shows='After n-apostrophe and au/r, a distinct small rounded o is followed by one low n course and the tall final t. There is no separate i stem/dot or extra e return needed for aient. Resolve the complete word to n’auront after re-reading the adjoining full formula.',crop=f'crops/{p}_second_B04.jpg',box=coords('B04'),confidence='high')
r['rows'].append(dict(place='Parenthetical same-meaning clause, physical line-end hyphen',C='manifestement',H='manifestement',final='manifeste-ment',against_C=True,against_H=True,kind='other',error_category='Other',scan_shows='The first line ends manifeste followed by a separate short horizontal hyphen; the next begins ment. Retain the written hyphen in the reflowed fragment. It is a source line-division mark, not an asserted nonstandard lexical spelling.',crop=f'crops/{p}_second_B06.jpg',box=coords('B06'),confidence='high',marked_in_H=False,consequential=False))
for d in r['decisions']:
 if d['id']=='M1095':d.update(decision='alternative',reading="n'auront",ink='A separate rounded o followed by n and tall t is visible after aur; no extra i/e sequence occurs. The complete word resolves to the mark’s listed alternative.',crop=f'crops/{p}_second_B04.jpg',box=coords('B04'),confidence='high')
r['doubts']=[d for d in r['doubts'] if d['place']!='L7, M1095']
for d in r['doubts']:
 if d['place']=='L6, cancelled word after Bien':d.update(reading=r'\unsure{en|sur}',alternatives='sur',reason='The left curve and obscured middle admit a second division as sur; the cancellation remains unresolved.')
 if d['place']=='L7, first term of the π map':d.update(reading=repls[1][1],alternatives=r"\pi^{\wedge}_{K'} / \pi_{\widehat K'}")
 if d['place']=='L7, second term of the π map':d.update(reading=repls[2][1],alternatives=r'\pi^{\wedge}_K / \pi^{\wedge}_{\overline K} / \pi_{\widehat K}')
r['notes']=r['notes'].replace('M1095 remains unresolved, with n’auront now first because its rounded loop and nt ending fit the ink better; no verbal expectation resolves it.','M1095 is resolved in the blind audit to n’auront, on the separate o and nt strokes; this is the listed alternative to C’s first n’auraient.')
r['notes']+='\n\n[Blind audit] A direct hat-on-K interpretation is added to the already unresolved upper decorations of the full pi map. The pi forms have the same curved top return and short oblique legs as the nearby lower-case kernel notation; no capital substitution is made solely from their three-stroke skeleton. The cancelled word after Bien now admits en/sur. The physical line break in manifeste-/ment has a separately written hyphen, retained as manifeste-ment in the reflowed fragment and explicitly treated as line division, not a spelling claim. Décrète has the visible d, accented e, c/r, accented e, t and final e; no new doubt is needed. The final sinon curve belongs to n and is not a comma. No mathematical check was undertaken.'
inks={
'B02':'Both readings show the section sign, theorem number 3, projective-line exponent/index and three dots after troué. Section-symbol encoding, order of independent subscript/superscript, and ellipsis macro are formatting only.',
'B03':'The low old word is covered by a dense stroke. Its left curve and joined low remnants admit en or sur; keep en primary and add sur. Do not resolve a cancelled word without its internal letters.',
'B04':'The pi shapes have a curved top return and short oblique legs matching the adjacent lower-case kernel notation, not the large straight boxed capital of the initial previous-page map. The upper decorations remain retraced; in addition to bar and wedge alternatives, explicitly allow hats attached to the lowered K letters. The arrow has a full head. After it the word has n-apostrophe, aur, a separate rounded o, one n and tall t: resolve n’auront, not n’auraient. The entire two-term map and prime positions were examined.',
'B06':'The shorthand consists of two flat bars with a single initial bend, not m arches; keep = and M1097’s resolution. A detached short hyphen follows manifeste at the right edge, and ment starts the next line. Preserve that physical line-division mark as manifeste-ment in the reflowed text, documenting its function. The remaining words and punctuation agree.',
'B09':'Both pi symbols repeat the short oblique-legged kernel form; keep lowercase. The connector is headless. Décrète has the d stem, accented e, c/r, accented e, tall crossed t and final e; retain it without new doubt. The long final curve is joined to the n of sinon, with no detached comma. Dash-length encoding is typographical.'}
reviews=[]
for b,x in cmp.items():
 if not x['different']:continue
 changed=f[b]!=x['first'];reviews.append(dict(box=b,decision=('mark doubt' if b=='B03' else 'correct') if changed else ('formatting' if b=='B02' else 'keep'),final=f[b],ink=inks[b],changed=changed))
(R/'second'/f'{p}_review.json').write_text(json.dumps({'box_reviews':reviews},ensure_ascii=False,indent=2)+'\n');rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
