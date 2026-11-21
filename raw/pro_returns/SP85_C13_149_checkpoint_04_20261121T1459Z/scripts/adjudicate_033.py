"""Root's manual blind-crop adjudication; no automated reading choices."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1];p='149_scan033'
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text());pp=R/'pages'/f'{p}.tex';s=pp.read_text()
cmp={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())};f={b:x['first'] for b,x in cmp.items()}
repls=[
 (r'\deleted{16}',r'\deleted{\unsure{16|46}}'),
 (r'un groupe alg. \inserted',r'un groupe alg \inserted'),
 (r'0\longrightarrow {}_nG\longrightarrow G\xrightarrow{n\operatorname{id}_G}G\longrightarrow1',r'0-{}_nG\longrightarrow G\xrightarrow{n\operatorname{id}_G}G-1'),
 (r'0\longrightarrow H^0(K,G)_n\longrightarrow H^1(K,{}_nG)\longrightarrow {}_nH^1(K,G)\longrightarrow0',r'0-H^0(K,G)_n\longrightarrow H^1(K,{}_nG)\longrightarrow {}_nH^1(K,G)-0'),
 ('Le composé de (16)',r'\unsure{Le|La} \unsure{composé|composée} de (16)'),
]
for old,new in repls:
 assert old in s,old;s=s.replace(old,new,1)
 for b in f:f[b]=f[b].replace(old,new)
pp.write_text(s)
r['rows'][1]['final']=r'\deleted{\unsure{16|46}}';r['rows'][1]['confidence']='medium';r['rows'][1]['scan_shows']+=' Blind B03: the crossing obscures the left digit enough that 4 cannot be excluded; the number remains transcribed, now locally doubtful.'
def row(place,C,H,final,ink,b):
 return dict(place=place,C=C,H=H,final=final,against_C=True,against_H=True,kind='misread symbol or index',error_category='Symbols and indices',scan_shows=ink,crop=f'crops/{p}_second_{b}.jpg',box=next(x['coords'] for x in r['audit_boxes'] if x['box']==b),confidence='high',marked_in_H=False,consequential=False)
r['rows'].append(dict(row('stop after alg before inserted G','alg.','alg.','alg','The g ends in its descending loop; the following diagonal belongs to the inserted G leader and the comma is beyond that leader. No separate abbreviation stop is present.','B04'),kind='text not on the page',error_category='Abbreviations expanded, spelling modernised'))
for place,old,new,b in [
 ('Kummer sequence, first connector',r'0\longrightarrow {}_nG',r'0-{}_nG','B07'),
 ('Kummer sequence, final connector',r'G\longrightarrow1',r'G-1','B07'),
 ('cohomology sequence, first connector',r'0\longrightarrow H^0(K,G)_n',r'0-H^0(K,G)_n','B08'),
 ('cohomology sequence, final connector',r'{}_nH^1(K,G)\longrightarrow0',r'{}_nH^1(K,G)-0','B08')]:
 r['rows'].append(row(place,old,old.replace(r'\longrightarrow',r'\to'),new,'The endpoint stroke is a short horizontal shaft with a slight terminal return, without the two angled branches visible on the internal arrows in the same formula. Preserve a bare connector. The whole formula, including zero/one, n positions and the neighbouring heads, was re-read.','B07' if b=='B07' else 'B08'))
for place,reading,alts,why in [
 ('cancelled second handwritten number','16','46','The dense cancellation obscures whether the left figure has a separate cross-arm; the right 6 bowl survives.'),
 ('line before the canonical comparison, article','Le','La','The low joined end of the initial L can be an e loop or flattened a; it does not independently resolve the article.'),
 ('line before the canonical comparison, noun','composé','composée','The accent is visible, but the final low return is not enough to decide whether a further e was written.')]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='medium',reason=why))
r['notes']=r['notes'].replace('the straight L of Le composé lower on this sheet','the straight L of the lower Le/La composé/composée line').replace('a separate cancelled 16 below the opening sentence','a separate cancelled 16/46 below the opening sentence')
r['notes']+='\n\n[Blind audit] The first and last connectors in each of the two short exact-sequence displays are bare horizontal strokes, unlike their headed interior arrows. Both witnesses supplied heads at these four endpoints. The subsequent inverse-limit display was additionally checked for this recurrence: its first connector has a distinct pointed head, so it is retained as an arrow. The stop after alg was supplied by both witnesses and is removed. The crossed number and Le/La composé/composée remain locally doubtful. The two later H indices keep 1 primary with n as an explicit alternative: the visible joined form alone is n-like, while the earlier separated H_1 and the written identity with the n-torsion limit support the same homology notation; no new calculation was undertaken. Hom has a terminal retracing flourish, not an extra lexical letter or a stop.'
r['hand_log'].append(dict(habit='Short endpoint connectors can lack heads while interior maps are headed',places='149_scan033, both ends of the Kummer and first cohomology sequences; compare the following limit sequence',scope='Four bare endpoints confirmed; the next sequence has a visible head at its left endpoint.',witness_errors='C and H supplied four arrowheads.'))
for a in r['abbreviations']:
 if a['form']=='alg.':a['form']='alg'
inks={
'B03':'The cancellation crosses the left digit’s central junction, so a 4-like cross-arm cannot be excluded from the first 1 reading; retain 16/46 doubtful. The right figure has the lower closed 6 bowl. This is distinct from the clear live authorial 16 elsewhere.',
'B04':'The g ends in its descending loop. The following diagonal comes from the raised G insertion, and a separate comma lies beyond that leader; there is no abbreviation stop after alg. Remove the supplied period. Lui-barred-m, the hyphen, G insertion and ext. agree.',
'B05':'The two upright equality strokes are below G(K), and the headed horizontal arrow leaves the G(K) row toward H^1. Both readings encode that structure. Extra est un is context already in the page; display/inline delimiters, array alignment and row spacing are typesetting only.',
'B07':'At 0 to nG and final G to 1, the short shafts end with mere returns, without two head branches. The middle arrows have distinct angled heads, including the n id_G label. Correct only the two endpoints to bare strokes; operatorname/roman id and spacing are formatting.',
'B08':'The first and last strokes lack the two head branches plainly visible on both internal arrows. Correct the two endpoint connectors to bare strokes. The zeroes, H degrees, subscript n on H^0, and left n on the torsion H^1 term remain unchanged.',
'B10':'The joined little form after the initial L is compatible with e or a; after the clearly accented composé outline the final return may or may not include another e. Mark both local uncertainties rather than choosing the grammatical pair. Formula-number math wrappers do not alter the ink.',
'B11':'The old p-like descender and crossed low letters remain too obscured to resolve composé. Canonique is a live raised replacement. The joined inner index is n-like but the earlier separated H_1 and repeated local identity support keeping 1 primary with n explicit. Both readers retain exactly these alternatives; only their order and math wrappers differ. The comparison shaft remains headless.',
'B12':'The same short joined form occurs at H’s right foot, with a dark wavy bar over G. Read with the full identity and the earlier H_1: keep 1 primary and n alternative, without claiming the isolated stroke resolves it. The n under the limit and before G remains in place; no formula is regularised.',
'B13':'The word has a tall h, low o and connected m body; the small descending final loop is a finishing retrace rather than unreadable text, so keep hom without a new doubt. H^0(K) still lacks a G argument, the two limits have no written n, and the last map has a left hook and right head. The two hook macros are equivalent.',
'B09':'Recurrence check after B07/B08: unlike the bare endpoints above, the initial 0-to-limit connector has two converging branches forming a distinct point. Both subsequent arrows are headed too. No change to this agreed box.'}
reviews=[]
for b,x in cmp.items():
 if not x['different'] and b!='B09':continue
 changed=f[b]!=x['first']
 reviews.append(dict(box=b,decision=('correct' if b in ['B04','B07','B08'] else 'mark doubt') if changed else ('formatting' if b=='B05' else 'keep'),final=f[b],ink=inks[b],changed=changed))
(R/'second'/f'{p}_review.json').write_text(json.dumps({'box_reviews':reviews},ensure_ascii=False,indent=2)+'\n')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
