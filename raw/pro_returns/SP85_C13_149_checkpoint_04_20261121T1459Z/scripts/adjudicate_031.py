"""Manual main-reader adjudication of scan031, using the blind crops."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1];p='149_scan031'
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text());pp=R/'pages'/f'{p}.tex';s=pp.read_text()
cmp={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())};f={b:x['first'] for b,x in cmp.items()}
repls=[
 (r'\unsure{dérivées|diverses}',r'\unsure{dérivées|diverses|divisées}'),
 (r"\unsure{des hypothèses|l'hypothèse}",r"\unsure{l'hypothèse|de l'hypothèse}"),
 (r'H_1(\overline X)\longrightarrow H_1(\overline Y\unsure{)}',r'H_1(\overline X)\unsure{-|\longrightarrow}H^1(\overline Y\unsure{)}'),
 (r'H_1(\overline X,\widehat{\mathbb Z}_\ell)$ resp. $H_1(\overline Y,\widehat{\mathbb Z}_\ell)',r'H_{\unsure{1|n}}(\overline X,\widehat{\mathbb Z}_\ell)$ resp $H_{\unsure{1|n}}(\overline Y,\widehat{\mathbb Z}_\ell)'),
 (r'pour tt $x\in X(K)$ (car,',r'pour \unsure{$\forall$|tt} $x\in X(K)$ Car,'),
 (r'\deleted{étendre}',r'\deleted{\unsure{étendre}}'),
 (r'\deleted{puis tt extension de corps}',r'\deleted{puis \unsure{$\forall$|tt} extension de \deleted{\unsure{base}} \inserted{\unsure{corps|corps de}}}'),
 (r'\inserted{pour $x\in X(\overline K)$}).',r'\inserted{pour $x\in X(\overline K)$).}'),
 (r'\deleted{\unsure{faire}}',r'\deleted{\unsure{faire|finie}}'),
 ('scindages de',r'\unsure{Scindages|scindages} de'),
 (r'\mathcal E_{\unsure{\overline X|X}/K}',r'\mathcal E_{\overline X/K}'),
]
for old,new in repls:
 assert old in s,old;s=s.replace(old,new,1)
 for b in f:f[b]=f[b].replace(old,new)
pp.write_text(s)
r['rows'][2]['final']=repls[0][1];r['rows'][2]['scan_shows']+=' Blind B03: divisées is an additional possible segmentation of the three small upper marks and low medial strokes; no option is resolved.'
r['rows'][5].update(final=repls[1][1],against_C=True,against_H=False,scan_shows='Blind B05 shows a detached apostrophe after the tall looped opening. There is no securely separate es before the noun and no clear final plural s. L’hypothèse is now primary, with de l’hypothèse retained for the intertwined initial loop; the des hypothèses segmentation is rejected.',crop=f'crops/{p}_second_B05.jpg',box=next(x['coords'] for x in r['audit_boxes'] if x['box']=='B05'))
r['rows'][7]['final']=r'H^1(\overline Y\unsure{)}$ on'
r['rows'][7]['scan_shows']+=' The blind crop additionally shows the index 1 in the upper half of the final H; that index correction is recorded separately. No comma is supplied.'
r['rows'][10]['final']=r'\deleted{\unsure{étendre}}';r['rows'][10]['confidence']='medium';r['rows'][10]['scan_shows']+=' The strike overlaps medial letters, so the readable old étendre outline is now explicitly doubtful rather than declared fully secure.'
r['rows'][13].update(final=r'\unsure{$\forall$|tt} extension de \deleted{\unsure{base}} \inserted{\unsure{corps|corps de}}',against_C=True,scan_shows='Blind B09 and the enlarged layers detail show a tall looped b and low ase-like sequence under a separate upper strike, above the lower corps outline. The long strike cancels the whole draft. Preserve nested deleted base and the lower replacement corps; a low loop below corps could be its flourish or an additional de, so that is not silently decided. The crossed angular two-stem form before extension permits a universal sign or tt; retain both.',crop=f'crops/{p}_second_B09.jpg',box=next(x['coords'] for x in r['audit_boxes'] if x['box']=='B09'))
r['rows'][14]['final']=r'\deleted{\unsure{faire|finie}}';r['rows'][14]['scan_shows']+=' The residual short f-initial cluster also permits finie under the cancellation; no letter sequence is resolved.'
r['rows'][15].update(final=r'\mathcal E_{\overline X/K}',confidence='high',scan_shows='Blind B11: a separate short horizontal bar sits above the complete dark X, at the same relative height as the clear bar over K in the next extension label. It does not pass through X. Retain barred X as written despite the expected unbarred X in the usual extension notation.',crop=f'crops/{p}_second_B11.jpg',box=next(x['coords'] for x in r['audit_boxes'] if x['box']=='B11'))
def row(place,C,H,final,ink,b,kind='misread symbol or index',cat='Symbols and indices',confidence='high',consequential=False):
 return dict(place=place,C=C,H=H,final=final,against_C=True,against_H=True,kind=kind,error_category=cat,scan_shows=ink,crop=f'crops/{p}_second_{b}.jpg',box=next(x['coords'] for x in r['audit_boxes'] if x['box']==b),confidence=confidence,marked_in_H=False,consequential=consequential)
r['rows'].extend([
 row('first homology map, connector before final H',r'\longrightarrow',r'\to',r'\unsure{-|\longrightarrow}','The shaft has only a short downward return at its right end; no upper head branch is separable. A bare stroke is primary, with a small arrowhead still possible. Both adjacent groups and the equality were read as one formula.','B06',confidence='medium'),
 row('first homology map, index of its rightmost H',r'H_1(\overline Y)',r'H_1(\overline Y)',r'H^1(\overline Y\unsure{)}','The short 1 is visibly high on the right of H, unlike the low 1 on H(Xbar) immediately to its left. Preserve this raised index; the closing parenthesis remains clipped and doubtful.','B06',consequential=True),
 row('between the two homology-kernel expressions','resp.','resp.','resp','After the p descender there is a clean gap before the next H, with no independent stop.','B07',kind='text not on the page',cat='Abbreviations expanded, spelling modernised'),
 row('proof opening, quantifier after pour','tt','tt',r'\unsure{$\forall$|tt}','The first tall stroke turns at the bottom and the second rises diagonally, with a common cross stroke, resembling the clear universal sign at the end of B07. Two joined t letters remain possible, so the literal sign is primary with tt explicit.','B09',confidence='medium'),
 row('proof opening, Car after X(K)','(car','(car','Car','There is one large open C followed by low a-r. A separate opening parenthesis and a second c are not present; preserve capital Car and leave the later closing parenthesis as written.','B09',kind='text not on the page',cat='Text that is not on the page'),
 row('end punctuation of raised point condition',r'\inserted{pour $x\in X(\overline K)$}).',r'pour $x\in X(\overline K)$).',r'\inserted{pour $x\in X(\overline K)$).}','The closing parenthesis and following dot are on the raised pour-x line above the old cancelled baseline. They belong to that insertion.','B09',kind='insertion or placement',cat='Insertions put in the wrong place'),
 row('word after inserted conjugaison de','scindages','scindages',r'\unsure{Scindages|scindages}','The initial curved stroke reaches well above the following lower-case bodies and ends in a large lower hook, favouring capital S; a stretched lower-case s cannot be excluded.','B10',kind='misread word',cat='Words',confidence='medium'),
])
r['doubts']=[d for d in r['doubts'] if d['place']!='subscript of first extension in the point paragraph']
for d in r['doubts']:
 if d['place']=='first-line adjective':d.update(reading=repls[0][1],alternatives='dérivées / diverses / divisées')
 if d['place']=='article before homology equality':d.update(reading=repls[1][1],alternatives='l’hypothèse / de l’hypothèse',reason='A distinct apostrophe follows the intertwined opening loop; only the possible extra de remains unclear.')
 if d['place']=='small separate cancelled faire':d.update(reading=repls[8][1],alternatives='faire / finie',reason='The crossed letters after the initial f admit both low sequences.')
for place,reading,alts,why in [
 ('first homology map connector','-',r'\longrightarrow','The endpoint is a small return without a separate upper head branch.'),
 ('first homology kernel index','1','n','The index joins the H foot in an n-like form; the repeated homology notation favours 1 but does not remove the local ambiguity.'),
 ('second homology kernel index','1','n','The same joined foot occurs at the second H; retain the same alternatives.'),
 ('proof opening, after pour',r'\forall','tt','The angled two-stem form resembles the nearby universal sign but may be joined t letters.'),
 ('cancelled extension phrase quantifier',r'\forall','tt','The same angular form is partly crossed; its letter/sign status remains doubtful.'),
 ('cancelled old verb','étendre','','The straight strike obscures some medial parts.'),
 ('cancelled upper word above corps','base','','The tall b and low ase-like remainder are crossed by a separate horizontal stroke.'),
 ('lower replacement after crossed base','corps','corps de','The low loop below the word can be a descending flourish or a separate de; attachment remains local to the cancelled draft.'),
 ('after conjugaison de','Scindages','scindages','The initial s-shaped stroke is tall, but its case is not completely secure.')]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='low' if 'cancelled' in place or 'replacement' in place else 'medium',reason=why))
r['notes']=r['notes'].replace('A short bar-like stroke above the X in the lower first extension is retained doubtfully rather than corrected to the mathematically expected unbarred X.','The blind B11 crop resolves the short independent bar over X in the lower first extension; barred X is preserved rather than corrected to the mathematically expected unbarred X.')
r['notes']+='\n\n[Blind audit] The rightmost H in the first map has a raised 1, while the preceding H labels have low indices. H^1 is preserved as an apparent inconsistency in this homology line; no theorem is inferred or repaired. The two homology-kernel indices remain 1/n doubtful, with 1 primary from the local notation. The final quantifier is clearly ell in P, not ell unequal p. A stop after resp is not visible. The point proof begins Car without an opening parenthesis; its later closing parenthesis remains. In the cancelled old extension phrase, a separately crossed base-like word and lower corps replacement were omitted from the first reading; both layers are now recorded, with a possible lower de left uncertain. The angular forms at pour and in the crossed draft allow a universal sign / joined tt; they are not expanded. The lower shorthand M1070 remains unresolved. All twelve differing boxes, plus the saved cancellation-layer detail and wider attachment crop, were examined.'
for e in r['inventory']:
 if e['element']=='E09':e['first_words_or_objects']='puis [universal sign / tt] extension de [crossed base] [lower corps / corps de]'
 if e['element']=='E10':e['first_words_or_objects']='pour x ∈ X(bar K)). with closing punctuation on the inserted line'
r['inventory'].append(dict(element='E16',kind='deletion',position='upper layer within the cancelled extension phrase',first_words_or_objects='base (?)',sheet_kind='text',hand='his hand',transcribed='yes'))
r['inventory'].append(dict(element='E17',kind='insertion',position='below crossed base in the cancelled extension phrase',first_words_or_objects='corps / corps de (?)',sheet_kind='text',hand='his hand',transcribed='yes'))
r['hand_log'].append(dict(habit='Raised versus low 1 must be kept even inside one homology line',places='149_scan031, rightmost H in the first map, B06',scope='One raised index; the preceding H indices are lower.',witness_errors='Both witnesses normalised the last label to H_1.'))
r['hand_log'].append(dict(habit='Separate cancellation layers can hide a prior base and its lower corps replacement',places='149_scan031, B09 and saved layers/scope details',scope='Local layered revision; not inferred for unrelated retracing.',witness_errors='Both witnesses omitted the upper base-like word.'))
for a in r['abbreviations']:
 if a['form']=='resp.':a['form']='resp'
inks={
'B01':'The bold number has a straight 1 and a detached top bar plus lower curved body of 5. Both read 15; the author-page wrapper is already in the page.',
'B02':'The initial r hook, low e/m sequence, tall crossed t and low er ending remain visible. There is no accented plural ending. Retain resolved remonter at M1069 and the separate en des; the blind certainty change does not overturn the visible letters.',
'B03':'Three small upper marks and the low medial curves permit an additional divisées segmentation. Retain dérivées primary with diverses and divisées explicit. De nature is raised and attaches to arithmético-, whose written hyphen remains.',
'B04':'The curved stroke above seulement belongs to the insertion leader. The reference ends with a baseline 1, a separate descending comma, a small a-like loop and closing parenthesis followed by another comma. It is not a superscript degree sign. Retain cor. 1, a), and the live seulement.',
'B05':'A detached apostrophe follows the intertwined tall opening loop. There is no distinct es before the noun and no securely separate final s. Change the primary reading to l’hypothèse, with de l’hypothèse retained for the complex initial loop, rather than des hypothèses.',
'B06':'The punctuation has an upper dot and lower descending comma, so keep a semicolon. The map shaft ends in a small downward return without a separate upper branch: bare shaft is primary, arrow alternative explicit. Crucially the rightmost 1 is high on H, unlike the low preceding indices; set H^1 and keep the clipped closing parenthesis doubtful. Bars over f,g,X,Y are present; bar/overline macros are equivalent.',
'B07':'The field separator is the same nearly upright slash used in the adjacent extension notation, retained consistently. Both homology indices join the H foot and are n-like; mark 1/n with 1 primary from the repeated local notation. No detached stop follows resp. At the end the membership sign has an open curved vertical part and middle bar, without a crossing diagonal; the following P is a large dark doubled upright/bowl. Retain forall ell in P and both visible stops. The leading de is context already present.',
'B09':'The live angular two-stem form after pour resembles the nearby universal sign, with joined tt still possible. One large C followed by ar has no preceding parenthesis; retain Car. The crossed étendre receives a local doubt, while reste ends without an additional ra. Puis has its p descender and i-dot, not the r-ending of pour. A separate upper strike crosses a b/ase-like word, with corps below; the extra low loop may be flourish or de, recorded as an alternative. Preserve these nested layers inside the outer cancellation. The raised pour-x line includes its closing parenthesis and dot. The separate crossed f-initial fragment admits faire/finie.',
'B10':'The first stroke of scindages rises far above the following letter bodies and has a large lower hook; capital Scindages is primary with lower-case alternative. The old d’autre part is crossed, while conjugaison de is a live insertion whose curved leader reaches this word.',
'B11':'The short bar over X is independent of the X body and matches the relative bar position on the next K. Resolve to barred X. The extra comma, et and next-line extension words in the blind reading are outside the compared snippet and already occur in the page; no surrounding text is removed.',
'B12':'The upper shorthand stroke is straight, but the lower one has a small hooked/bowed entry. It still admits a flattened barred m as well as equals; keep both, M1070 undecided. The following classe de and both f(x),g(x) agree.',
'B13':'The thin foliation has a two-curve 3 and a closed 0. Its margin wrapper is already in the page; no reading changes.'}
reviews=[]
for b,x in cmp.items():
 if not x['different']:continue
 changed=f[b]!=x['first'];reviews.append(dict(box=b,decision=('correct' if b in ['B05','B06','B07','B09','B11'] else 'mark doubt') if changed else ('formatting' if b in ['B01','B13'] else 'keep'),final=f[b],ink=inks[b],changed=changed))
(R/'second'/f'{p}_review.json').write_text(json.dumps({'box_reviews':reviews},ensure_ascii=False,indent=2)+'\n');rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
