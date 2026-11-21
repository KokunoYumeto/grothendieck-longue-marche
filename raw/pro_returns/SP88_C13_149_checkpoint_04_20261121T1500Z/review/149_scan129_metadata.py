"""Frozen first-reader metadata for scan129; reads only this reader's page files."""
from pathlib import Path
import importlib.util
import json

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan129'
spec = importlib.util.spec_from_file_location('crops129', ROOT / f'edition/review/{PAGE}_crop.py')
cropmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cropmod)
tex = (ROOT / f'edition/review/{PAGE}.tex').read_text()

def change(id, crop, place, C, H, final, evidence, confidence='high', vs_C=False, vs_H=True,
           kind='misread word', category='Words', H_marked=False, consequential=False):
    return dict(id=id, place=place, C=C, H=H, final=final, evidence=evidence,
                crop=f'crops/{PAGE}_{crop}.png', bbox=cropmod.CROPS[crop]['bbox'],
                confidence=confidence, vs_C=vs_C, vs_H=vs_H, kind=kind,
                error_category=category, H_marked=H_marked, consequential=consequential)

changes = [
 change('p18a','p18','Opening continuation, between au and dessus', 'au-dessus', 'au-dessus', 'au dessus',
        'The complete opening line has a clear blank gap between the compressed au and the rising d of dessus. No independent horizontal stroke lies in that gap; the horizontal-looking tail at the end of au belongs to that compressed word, not to an intervening hyphen.',
        vs_C=True,kind='text not on the page',category='Text that is not on the page'),
 change('p02a','p02','First shaft of (34)',r'1\mathrel{\text{---}}T^{I(x)}',r'1\to T^{I(x)}',r'1\mathrel{\text{---}}T^{I(x)}',
        'The long first shaft ends in a small terminal return; there is no independently legible two-arm right head. The other three arrows in the same formula have distinct angular heads. The written shaft is retained without supplying its possible intended arrowhead.',
        confidence='medium',kind='misread symbol or index',category='Symbols and indices'),
 change('p03a','p03','End of the definition of T',r'T=T_\infty(\bar L^*)',r'T=T_\infty(\bar L^*),',r'T=T_\infty(\bar L^*)',
        'The final curved parenthesis is followed by blank paper; there is no separate comma. A real comma is visible after the preceding closing set brace. The thin spaces inside H’s set braces are TeX syntax and are not additional punctuation differences.',
        kind='text not on the page',category='Text that is not on the page'),
 change('p04a','p04','Parenthetical description of the field', 'corps des fonctions', 'corps des fractions', 'corps des fonctions',
        'After the f, the rounded o and following n/c run precede the crossed t and ion ending. There is no independent r/a sequence required by fractions.'),
 change('p04b','p04','First prose occurrence of tilde O_x',r'\tilde O_x',r'\widetilde{\underline{O}}_x',r'\widetilde{\underline{O}}_x',
        'A separate short horizontal stroke lies below the closed O, with a thin white gap between that stroke and the lower curved body of O. The upper wavy stroke is the tilde; the lower stroke is retained independently.',
        vs_C=True,vs_H=False,kind='omission',category='Symbols and indices'),
 change('p14a','p14','Word following qui fait donc fonction',r'\illegible{1}','[absent]',r'\unsure{égalt|egalt}',
        'The repair contains the whole large looped g descender. Before it is a small e/é-like loop; after it is a compressed rise compatible with a/l followed by a long thin terminal ending in a dark knot. The exact abbreviated ending and accent are not separately secure, so égalt|egalt remains a doubtful proposal rather than an expansion. The word is unquestionably present.',
        confidence='low',vs_C=True,kind=r'readable ink left as \ill{}',category='Readable ink left as illegible'),
 change('p14b','p14','End of the first paragraph',r'K_x',r'\widetilde K_x',r'K_x',
        'The tall crossed K has its small x at lower right; the space above the K is blank. No tilde is visible here, although the earlier K_x in the same paragraph has a distinct wavy mark.',
        kind='misread symbol or index',category='Symbols and indices'),
 change('p06a','p06','After Supp D', 'on aura,', 'on a,', 'on aura,',
        'The connected word contains the low u/r sequence after a and an additional terminal a before the written comma. The intervening letters cannot be reduced to a alone.'),
 change('p07a','p07','Introduction of S', 'pour', 'posant', 'pour',
        'A p descender is followed by a short rounded ou run and a final r return. There is no tall t or the additional sa/n sequence of posant.'),
 change('p07b','p07','Attachment of the raised hensélisé phrase',r"d'où $\tilde S$ \inserted{(hensélisé)}",r'on a, \add{(\uncertain{hensélisé})} posant',r"d'où $\tilde S$ \inserted{(hensélisé)}",
        'The raised phrase is above the interval after tilde S. Its continuous curved leader comes down to that interval, before du pt; it is not attached before pour. Separate outer parentheses surround the raised hensélisé itself.',
        kind='insertion or placement',category='Insertions put in the wrong place',H_marked=True),
 change('p07c','p07','Before du pt', '(du pt', r'(de p\supplied{oin}t', 'du pt',
        'The apparent opening curve at the left of du continues into the long insertion leader above pt and toward the raised hensélisé. No independent opening parenthesis remains once that continuous stroke is traced.',
        vs_C=True,kind='text not on the page',category='Text that is not on the page'),
 change('p07d','p07','Short form before générique', 'du pt',r'de p\supplied{oin}t', 'du pt',
        'The second letter after d has a u-shaped low turn. The following short form consists of p with its descender and crossed t; no oin is written. The abbreviation is preserved as pt.',
        kind='abbreviation expanded or spelling modernised',category='Abbreviations expanded, spelling modernised'),
 change('p07e','p07','Between tilde eta and une factorisation',r'$\tilde\eta$ une',r'$\widetilde\eta$), une',r'$\tilde\eta$ une',
        'After the eta body and descender, the line proceeds to une on the next written baseline. There is no independent closing parenthesis or comma in the intervening space.',
        kind='text not on the page',category='Text that is not on the page'),
 change('p08a','p08','Parenthesis introducing the composed path', 'composé', 'compatible', 'composé',
        'After comp the word has a rounded o, short s and final accented e. It has neither the extra ati sequence nor the tall b/l strokes of compatible.'),
 change('p08b','p08','Middle relation in the parenthetical path',r'\eta=\operatorname{Spec}(L)',r'\eta\in\operatorname{Spec}(L)',r'\eta=\operatorname{Spec}(L)',
        'Two short, separated horizontal strokes connect eta to Spec(L). They are not a curved membership sign.',
        kind='misread symbol or index',category='Symbols and indices',consequential=True),
 change('p08c','p08','Shaft in the clause after car',r'\tilde\eta\mathrel{\text{---}}U',r'\tilde\eta\to U',r'\tilde\eta\mathrel{\text{---}}U',
        'The short connecting stroke has no distinct oblique terminal arms. Nearby arrows in the composed path have legible right heads. A possible intended map is not supplied as a written head.',
        confidence='medium',kind='misread symbol or index',category='Symbols and indices'),
 change('p08d','p08','Agreement of the verb after the eta–U shaft', 'induite', 'induit', 'induite',
        'The crossed t is followed by a separate low final e loop before the gap leading to par; the final letter is retained.'),
 change('p09a','p09','T definition: second prose tilde O_x',r'\tilde O_x',r'\widetilde{\underline{O}}_x',r'\tilde O_x',
        'This O has its closed lower curve and small lower-right x, but no separate horizontal stroke beneath it. Its top tilde is distinct. The first occurrence has an underline; this occurrence does not.',
        kind='misread symbol or index',category='Symbols and indices'),
 change('p15a','p15','Prose map immediately before (35)',r'\mathcal E_{\tilde\eta}^{L}\longrightarrow\mathcal E_U^{L}',r'\mathcal E_{\widetilde\eta}^{\overline L}\to\mathcal E_U^{\overline L}',r'\mathcal E_{\tilde\eta}^{L}\longrightarrow\mathcal E_U^{L}',
        'Both exponents are plain tall L forms with a foot; neither has a separate upper bar. The tilde below the first L belongs to eta. In (35), by contrast, all three L exponents have visibly separate horizontal bars. The local plain/barred distinction is preserved.',
        kind='misread symbol or index',category='Symbols and indices'),
 change('p11a','p11','Cancelled cluster beneath the middle group in (35)',r'\deleted{\unsure{N_x}}',r'[note: sous le second terme de (35), un symbole biffé, illisible, avant « $N_x$ ».]',r'\deleted{\unsure{\parallel}}\quad\deleted{\unsure{N_x}}',
        'At the left of the live upright pair and live N_x, long diagonal cancellation strokes traverse an upper cluster compatible with an earlier upright pair, then a lower capital-N-like outline and small x. The upper pair and individual letters of the lower deleted label are not all secure under the hatch; both layers remain doubtful. The live upright pair and N_x to their right are clear.',
        confidence='low',vs_C=True,kind='omission',category='Struck text',H_marked=True),
 change('p16a','p16','Dots after the final bar L',r'$\bar L$\ldots',r'$\overline L$…',r'$\bar L$....',
        'Four separate dark marks stand between the L and the closing parenthesis: three short slanted/horizontal marks followed by a fourth compact dot. The stop after the closing parenthesis is separate from these four.',
        vs_C=True,kind='misread symbol or index',category='Symbols and indices'),
 change('p13a','p13','Thin lower-left foliation',r'\margin{128}','[absent]',r'\margin{128}',
        'The slanted leading 1, curved 2 with a lower horizontal foot, and two-loop 8 are legible in the thinner numbering hand.',
        kind='omission',category='Omissions'),
]

decisions = [
 dict(id='M0163',cote='149',scan='129',decision='undecided',reading=r'\unsure{égalt|egalt}',
      evidence='A whole g descender and preceding small e/é-like loop are visible; the compressed a/l-like rise and long knotted terminal do not decide the precise short form or accent. The word is present and provisionally readable, but the proposal remains open.',
      crop=f'crops/{PAGE}_p14.png',bbox=cropmod.CROPS['p14']['bbox'],confidence='low'),
 dict(id='M0164',cote='149',scan='129',decision='first',reading='est',
      evidence='The low connected e/s run ends in a short upright with a transverse t stroke. The sur X leader attaches before this live word and is not a cancellation of it.',
      crop=f'crops/{PAGE}_p06.png',bbox=cropmod.CROPS['p06']['bbox'],confidence='medium'),
 dict(id='M0165',cote='149',scan='129',decision='first',reading='générique',
      evidence='The compact word has the g descender, accented initial e and n/ér run followed by i/q/ue. It lacks the separate high t and longer omét sequence required by géométrique. The whole du pt générique tilde-eta context is present in the crop.',
      crop=f'crops/{PAGE}_p07.png',bbox=cropmod.CROPS['p07']['bbox'],confidence='medium'),
 dict(id='M0166',cote='149',scan='129',decision='first',reading=r'\mathrm{dfn}',
      evidence='The label beside the live upright pair has a d loop with ascender, a tall descending f, and a low final n. There is neither a detached accent nor a separate terminal abbreviation stop. Both neighboring groups, the two horizontal arrows, the upright pairs and lower labels were inspected in the same whole-diagram crop.',
      crop=f'crops/{PAGE}_p11.png',bbox=cropmod.CROPS['p11']['bbox'],confidence='high'),
]

def item(n,kind,position,words,hand='his hand'):
    return dict(sheet_kind='text',hand=hand,element=f'e{n:02}',kind=kind,position=position,
                first_words_or_objects=words,transcribed='yes')

inventory = [
 item(1,'text','Top, standalone author number','64'),
 item(2,'text','Opening continuation above (34)',r'$\bar L$ au dessus de $\tilde U_x$, bien sûr, et'),
 item(3,'display','Upper formula (34)',r'$(34)\quad1\mathrel{\text{---}}T^{I(x)}\longrightarrow\mathcal E_{\tilde U_x}^{\bar L}\longrightarrow\mathcal E_{k(x)}^{\overline{k(x)}}\longrightarrow1$'),
 item(4,'text','Below (34)','où'),
 item(5,'deletion','After où',r'$I(x)$'),
 item(6,'display','Definitions following où',r'$I(x)=\{i\in I\mid x\in D_i\},\quad T=T_\infty(\bar L^*)$'),
 item(7,'text','First prose paragraph',r'$\overline{k(x)}$ étant la clôture alg. de $k(x)$'),
 item(8,'text','Middle paragraph','Ceci dit, pour'),
 item(9,'insertion','Above centre x, attached after x',r'sur $X$'),
 item(10,'insertion','Above interval following tilde S','(hensélisé)'),
 item(11,'deletion','After Donc',r"l'image $N_V$ de"),
 item(12,'insertion','Raised above the deleted image phrase',r"l'hom. induit"),
 item(13,'deletion','After the prose E-map and est','contenue dans celle de'),
 item(14,'insertion','Raised above the latter deleted phrase','un composé'),
 item(15,'diagram','Lower display (35)',r'$(35)\quad\mathcal E_{\tilde\eta}^{\bar L}\longrightarrow\mathcal E_{\tilde U_x}^{\bar L}\longrightarrow\mathcal E_U^{\bar L}$'),
 item(16,'deletion','Below middle group, left of the live vertical relation',r'\unsure{$\parallel$}'),
 item(17,'deletion','Below the cancelled vertical cluster, left of live N_x',r'\unsure{$N_x$}'),
 item(18,'text','Final parenthesis and unfinished clause',r"(l'image de $\mathcal E_{\tilde U_x}^{\bar L}\longrightarrow\mathcal E_U^{\bar L}$"),
 item(19,'margin note','Bottom left, separate thin foliation','128',hand='thin foliation hand'),
]

doubts = [
 dict(place='First paragraph, word after fonction (M0163)',reading=r'\unsure{égalt|egalt}',
      alternatives='The exact abbreviated ending and initial accent remain unresolved; the initial e/é-like loop and g are readable. No expansion is printed.',confidence='low'),
 dict(place='Before the eta–U shaft in the middle paragraph',reading=r'\unsure{car|par}',
      alternatives='car preferred; par possible from the heavy descending/looped first stroke. No separate cancelled underletter is securely identifiable.',confidence='medium'),
 dict(place='Cancelled upper cluster under the middle group in (35)',reading=r'\deleted{\unsure{\parallel}}',
      alternatives='An earlier pair of upright strokes is proposed under the diagonal hatching; their complete individual paths are not secure.',confidence='low'),
 dict(place='Cancelled lower label under the middle group in (35)',reading=r'\deleted{\unsure{N_x}}',
      alternatives='N_x is retained as C’s doubtful proposal; crossing strokes prevent every part of N and the subscript attachment from being separately plain.',confidence='low'),
]

formula34 = tex.split('\\[',1)[1].split('\\]',1)[0].strip()
body_start = tex.index('où ')
body_end = tex.index('\\diagram{')
pre_diagram = tex[body_start:body_end].strip()
end_body = tex[body_end:tex.index('\\margin{128}')].strip()
audit_boxes = [
 dict(box='b01',kind='handwritten number',bbox=cropmod.CROPS['p01']['bbox'],reading='64'),
 dict(box='b02',kind='handwritten number; doubtful formula; C/H symbol difference',bbox=cropmod.CROPS['p02']['bbox'],reading='\\[\n'+formula34+'\n\\]'),
 dict(box='b03',kind='insertion; deletion; doubtful formula; C/H word difference; less-than-high C departure',bbox=[235,310,1679,1790],reading=pre_diagram),
 dict(box='b04',kind='diagram; deletion; handwritten number; doubtful formula; less-than-high C departure',bbox=[195,1788,1679,2360],reading=end_body),
 dict(box='b05',kind='handwritten number; margin note',bbox=cropmod.CROPS['p13']['bbox'],reading=r'\margin{128}'),
 dict(box='b06',kind='handwritten number; doubtful formula',bbox=[150,0,1679,285],reading=r'64 $\bar L$ au dessus de $\tilde U_x$, bien sûr, et'+'\n\\[\n'+formula34+'\n\\]'),
]

data = dict(
 page=PAGE,scan=129,reader='reader_b',line_count=27,
 line_count_detail=dict(main=18,diagram=3,margin=0,insertion=4,standalone_numbers=2),
 changes=changes,decisions=decisions,inventory=inventory,doubts=doubts,audit_boxes=audit_boxes,
 notes=[
  'The sheet continues a construction involving tilde U_x, the index set I(x), a valuation ring V, and the induced group maps (34) and (35). This is a diplomatic reading; none of that argument has been independently verified here.',
  'The opening compound is written au dessus with a blank gap and no hyphen. Both witnesses supplied the hyphen. The additional p17 was requested for this previously uncropped detail; its complete-letter contextual repair is p18.',
  'The word after fonction is present but only partly secure. The candidate uses doubtful égalt|egalt and does not expand it to également or omit it.',
  'The first O_x in the paragraph has an independent underline; the second O_x in the definition of tilde T does not. The final K_x of the first paragraph is plain, although the earlier K_x has a tilde. Those local distinctions remain unnormalized.',
  'The hensélisé insertion retains its own real outer parentheses. Its curved attachment leader is not an opening parenthesis before du pt. No closing parenthesis or comma is supplied after the following eta, and the resulting literal wording remains syntactically rough.',
  'The first letter in car is heavy and p-like; car|par remains local uncertainty. The T in the tilde-S to tilde-T to X path is retraced, but no distinct independent underletter can be securely isolated, so none is invented.',
  'Both L exponents in the prose E-map before (35) are plain; the three exponents in (35) are barred. The manuscript distinction may be an authorial omission, but the transcription preserves it without mathematical repair.',
  'The two clear vertical relations in (35) are represented as upright pairs, not as horizontal equalities or directional arrows. An additional struck upper pair is proposed to the left of the second live pair; that upper pair and its lower N_x remain doubtful. There is no supplied MARKS identifier for either cancelled cluster.',
  'The final parenthesis is followed by a real stop. Four dots precede its closing parenthesis. The last written clause is L’étude de l’hom composé; no completion is inferred from another page.',
  'Four contextual repair crops were declared and retained beside their originals: p14 restores the g-descender clipped by p05; p15 includes the full raised un composé and lower eta clipped by p10; p16 restores the upper exponent bars and complete paper-edge ending clipped by p12; p18 restores the opening-line letter tops clipped by the newly requested p17. They repair incomplete target contexts rather than re-enlarge settled readings.',
  'The first combined display attempt for p10–p13 returned an output-context truncation and no visible images. Each was then successfully inspected separately. The inspection list records those actual successful views, not the failed display attempt.',
  'The all-logical-baseline count was reconciled with root’s reconstruction from the required crop suite: eighteen main prose/display baselines, the three rows of diagram (35), four raised insertion baselines and separate author64/folio128 numbering elements. Formula34 and formula35 numbers are already included on their formula rows; inline indices and exponents are not separate lines.',
  'The audit uses a continuous pre-diagram body box and a continuous diagram-plus-ending box so interleaved insertions, descenders, cancellation layers and raised group bars are retained with complete actual text rather than clipped isolated words. The separate foliation has its own box.',
 ],
 checks=[],
 hand_observations=[
  dict(habit='An insertion leader can resemble an opening parenthesis at its lower end.',places='After tilde S and before du pt; p07',holds='The stroke here is continuous with the raised hensélisé attachment; that phrase’s actual outer parentheses are separate.',witness_errors='C adds an opening parenthesis before du pt; H also puts the insertion before posant and supplies surrounding punctuation.'),
  dict(habit='Some horizontal connections have only a small terminal return or no visible head.',places='First shaft in (34), p02; eta–U connection after car, p08',holds='The adjacent headed maps in both contexts have distinct angular arms; the two plain shafts are retained literally.',witness_errors='H regularizes both shafts as arrows.'),
  dict(habit='Underlines and overbars must be separated from adjacent curved letter bodies and tildes.',places='First/second tilde O_x, p04/p09; prose versus displayed L exponents, p15/p11',holds='Underline present only at the first O; separate bars present in (35) but absent in the preceding prose map.',witness_errors='C omits the first underline; H adds the second underline and bars to the prose exponents.'),
  dict(habit='The short form dfn has a tall descending f and a low final n.',places='Beside the second live upright pair in (35), p11',holds='The local three-letter label is readable without an accent or stop.',witness_errors='C offers déf. as an alternative; the crop supports its first dfn reading.'),
  dict(habit='Retouching alone does not establish a cancelled predecessor.',places='Initial letter of car, p08; T in the factorization, p09',holds='The heavy first letter remains ambiguous; the retraced T is recognizable. Neither supports a definite separate underletter.',witness_errors='The newly localized car|par doubt does not count as a correction of the shared base reading.'),
 ],
 notation=[
  dict(written=r'I(x)=\{i\in I\mid x\in D_i\}',meaning_or_use='Index set explicitly defined on this page.',places='Definition after (34).'),
  dict(written=r'T=T_\infty(\bar L^*)',meaning_or_use='The T notation explicitly defined beside I(x).',places='Definition after (34).'),
  dict(written=r'\mathcal E_{\tilde\eta}^{L}\longrightarrow\mathcal E_U^{L}',meaning_or_use='Literal plain-L prose map; the corresponding displayed groups in (35) have barred L.',places='Immediately before (35).'),
  dict(written=r'\parallel',meaning_or_use='Two upright strokes between vertically stacked group and N labels, with dfn beside the middle one.',places='Two live lower relations in (35); a further cancelled pair is uncertain.'),
 ],
 abbreviations=[
  dict(written='alg.',expansion='algébrique'),dict(written='sép.',expansion='séparable'),
  dict(written='pt',expansion='point'),dict(written="l'hom.",expansion="l'homomorphisme"),
  dict(written="l'hom",expansion="l'homomorphisme; the final occurrence has no written stop"),
  dict(written='dfn',expansion='définition'),
  dict(written=r'\unsure{égalt|egalt}',expansion='Possibly a short form for également; the written form remains doubtful and is not expanded in the text.'),
 ],
 inspection=dict(whole=True,halves=['top','bottom'],crops=[f'crops/{PAGE}_{name}.png' for name in cropmod.CROPS],deletions_insertions_checked=True),
)

if __name__ == '__main__':
    dest = ROOT / f'edition/review/{PAGE}.json'
    if dest.exists():
        raise FileExistsError(f'Refusing to overwrite frozen metadata: {dest}')
    dest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(f'{PAGE}: {len(changes)} changes, {len(decisions)} supplied mark decisions, {len(cropmod.CROPS)} crops, {len(doubts)} doubts')
