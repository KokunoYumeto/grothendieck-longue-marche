from pathlib import Path
import json
import csv

BASE = Path('/workspace/scratch/9d0bd22e5d3a/work/SP86_C13_149')
PACKET = Path('/workspace/scratch/9d0bd22e5d3a/packets/149_scan073')
PAGE = '149_scan073'
manifest_path = BASE / 'readings' / f'{PAGE}_crop_manifest.json'
manifest = json.loads(manifest_path.read_text())
crop_by_id = {entry['id']: entry for entry in manifest}
crop_by_id['P24']['subject'] = 'E_K right arrow E_U_Ox before correspondent; complete open U, lower K/x tips at crop border and verified in native view'
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')

tex = r'''\scanpage{73}
\mspage{36}
\diagram{\((9)\qquad\begin{tikzcd}[ampersand replacement=\&,column sep=small]
U_S \arrow[r,no head] \arrow[d,no head] \& U_{O_x} \arrow[r,no head] \arrow[d,no head] \& U_K \arrow[r,no head] \arrow[d,no head] \& U_{\overline K} \arrow[r,no head] \arrow[d,no head] \& \widetilde U_S \\
S \arrow[r,no head] \& \underline O_x \arrow[r,no head] \& K \arrow[r,no head] \& \overline K \&
\end{tikzcd}\)}
\diagram{\((10)\qquad\begin{tikzcd}[ampersand replacement=\&]
E_{U_S} \arrow[d] \& E_{U_{O_x}} \arrow[l] \arrow[d] \& E_{U_K} \arrow[l] \arrow[d] \\
E_S \& E_{\underline O_x} \arrow[l] \& E_K \arrow[l] \arrow[ul,dashed,"\varphi_x"']
\end{tikzcd}\)}
avec des carrés cartésiens, et des flèches horizontales surjectives. L'hom $E_K\longleftarrow E_{U_S}$ est composé d'un relèvement $E_K-E_{U_{O_x}}$ de $E_K\longrightarrow E_{O_x}$, avec l'hom canonique $\widehat E_{U_{O_x}}-E_{U_S}$. (Les \inserted{\deleted{\unsure{derniers|dernier}}} relèvements $E_K\longrightarrow E_{U_{O_x}}$ correspondent biuniv.$^{\mathrm t}$ aux sections de $E_{U_{\unsure{\eta|K}}}$ sur $E_K$, ou aux rel$^{\mathrm t}_{\mathrm s}$ de $E_K-E_S$ en $E_K-E_{U_S}$\ldots)

Ceci dit, j'ai envie de prouver que $\varphi_x:E_K\longrightarrow E_{U_{O_x}}$ s'annule \unsure{sur|dans} $I_x$, i.e. provient d'une section de $E_{U_{O_x}}$ sur $\underline O_x$ sss la section rationnelle corresp.$^{\mathrm t}$ * de $U_S/S$ est définie en $x$. Ceci impliquera
\margin{\uline{NB} Le quotient de $E_K$ par le \unsure{s.}groupe engendré par $\unsure{I_x|\overline I_x}$ n'est autre que $E_{\underline O_x}=\pi_1(\operatorname{Spec}\unsure{O_x|\underline O_x})$}
\margin{72}
'''
(BASE / 'readings' / f'{PAGE}.tex').write_text(tex)

changes = []

def change(identifier, crop_id, place, C, H, final, evidence, confidence='high', against_C=False, against_H=True, kind='misread symbol or index', category='Symbols and indices', marked_in_H=False, consequential=False):
    crop = crop_by_id[crop_id]
    changes.append(dict(id=identifier, place=place, C=C, H=H, final=final, evidence=evidence, crop=crop['path'], box=crop['box'], confidence=confidence, against_C=against_C, against_H=against_H, kind=kind, error_category=category, marked_in_H=marked_in_H, consequential=consequential))

def u_change(identifier, crop_id, place, C, H, final, observation):
    change(identifier, crop_id, place, C, H, final,
           observation + ' The upper entry remains open. Plain U records that source form; H renders this occurrence with mathcal U. This row concerns this U occurrence only. The established E and O font wrappers alone are not counted here.')

u_change('P01u1', 'P01', 'diagram (9), first upper node', r'U_S', r'\mathcal{U}_S', r'U_S', 'The large U has two long sides joined by a rounded lower turn, and a short open entry at the upper left; S is below/right.')
u_change('P01u2', 'P01', 'diagram (9), second upper node', r'U_{O_x}', r'\mathcal{U}_{\mathcal{O}_x}', r'U_{O_x}', 'The second U repeats the open two-sided form. Its O is a small oval with a lower/right x and no separate underline.')
u_change('P01u3', 'P01', 'diagram (9), third upper node', r'U_K', r'\mathcal{U}_K', r'U_K', 'The third U has a short upper-left entry, deep lower turn, and ascending right side; the small K has the closed-angle form.')
u_change('P01u4', 'P01', 'diagram (9), fourth upper node', r'U_{\overline K}', r'\mathcal{U}_{\overline K}', r'U_{\overline K}', 'The fourth U has an open upper entry. Its K index carries a distinct separate upper bar, also present on the lower-row K at this column.')
u_change('P01u5', 'P01', 'diagram (9), fifth upper node', r'\widetilde U_S', r'\widetilde{\mathcal{U}}_S', r'\widetilde U_S', 'The fifth U has an open upper-left entry and the same lower bowl. S is below/right. Its tilde was fully inspected in the native page and upper half; the saved crop includes the U but clips part of the upper tilde.')
change('P01b', 'P01', 'diagram (9), second lower node', r'\underline O_x', r'\mathcal{O}_x; H editorial note says O_x is underlined', r'\underline O_x', 'A separate horizontal stroke lies under the O oval and ends before the lower/right x. H mentions the underline in its editorial note but omits it from the diagram object.', kind='drawing or diagram', category='Drawings and diagrams')

u_change('P02u1', 'P02', 'diagram (10), first upper node', r'E_{U_S}', r'\mathcal{E}_{\mathcal{U}_S}', r'E_{U_S}', 'The nested U has two open upper ends, a low connecting turn, and lower/right S.')
u_change('P02u2', 'P02', 'diagram (10), second upper node', r'E_{U_{O_x}}', r'\mathcal{E}_{\mathcal{U}_{\mathcal{O}_x}}', r'E_{U_{O_x}}', 'The nested U has an open entry; the next nested O is a closed oval with a separate small x, without an underline at this upper node.')
u_change('P02u3', 'P02', 'diagram (10), third upper node', r'E_{U_K}', r'\mathcal{E}_{\mathcal{U}_K}', r'E_{U_K}', 'The small U remains open at the upper left. Its K is a compact stem-and-angle form below/right.')
change('P02b', 'P02', 'diagram (10), lower middle node', r'E_{\underline O_x}', r'\mathcal{E}_{\mathcal{O}_x}', r'E_{\underline O_x}', 'The lower-node O oval has a visibly detached underline. The short x is outside that underline at the lower right.', kind='drawing or diagram', category='Drawings and diagrams')
change('P02c', 'P02', 'diagram (10), label of dashed lower-right to upper-middle diagonal', r'\arrow[ul,dashed,"\varphi_x"]', r'\arrow[ul,dashed,"\varphi_x"\x27]', r'\arrow[ul,dashed,"\varphi_x"\x27]', 'The dashed shaft starts by lower-right E_K and points up-left into the upper-middle node. The complete phi_x label is on the northeast/right side of this diagonal. The swapped label side in H matches that placement; C puts it on the other side.', against_C=True, against_H=False, kind='drawing or diagram', category='Drawings and diagrams')
# A literal apostrophe in the final two TikZ snippets above, kept separate from Python quoting.
for row in changes:
    if row['id'] == 'P02c':
        row['H'] = row['H'].replace(r'\x27', "'")
        row['final'] = row['final'].replace(r'\x27', "'")

change('P04a', 'P04', 'main line 2, first L\x27hom', "L'hom", "L'hom.", "L'hom", 'The tall L, separate apostrophe, tall h, small rounded o and compressed m are followed by clear white space. No independent full stop follows the m.', kind='text not on the page', category='Text that is not on the page')
u_change('P23u', 'P23', 'main line 3, target in E_K left arrow E_U_S', r'E_K\longleftarrow E_{U_S}', r'\mathcal{E}_K\leftarrow\mathcal{E}_{\mathcal{U}_S}', r'E_K\longleftarrow E_{U_S}', 'The U after the right E has a short bent upper-left entry, a long descending side, a low turn and a rising right side; S is below/right. The connector has a single left-pointing head.')
change('P05a', 'P05', 'main line 4, first relèvement expression', r'E_K-E_{U_{O_x}}', r'\mathcal{E}_K\to\mathcal{E}_{\mathcal{U}_{\mathcal{O}_x}}', r'E_K-E_{U_{O_x}}', 'The horizontal connector ends in a rounded dark cap. Neither endpoint supplies a paired arrowhead. E, K, nested U and nested O_x are read across the complete expression.', consequential=True)
u_change('P05u', 'P05', 'main line 4, U in first relèvement expression', r'E_{U_{O_x}}', r'\mathcal{E}_{\mathcal{U}_{\mathcal{O}_x}}', r'E_{U_{O_x}}', 'The nested U has an open upper-left entry and low rounded turn; the inner O_x is unlined.')
change('P06a', 'P06', 'main line 4, second l\x27hom', "l'hom", "l'hom.", "l'hom", 'The short l entry rises into its long stem; the apostrophe, h stem, small o and flattened m remain visible. The m tail ends without a detached period.', kind='text not on the page', category='Text that is not on the page')
change('P07a', 'P07', 'main line 5, initial symbol of canonical expression; M1200', r'\unsure{\widehat E}', r'\mathcal{E}', r'\widehat E', 'Two inner sloping segments meet as a peak within/against the upper lobe of E. They can be traced separately from the outer curved E contour, though they touch it. The whole following U_{O_x}-E_{U_S} expression was inspected with the marked symbol.', confidence='medium', against_C=True, marked_in_H=False, consequential=True)
u_change('P07u1', 'P07', 'main line 5, U in the left term of canonical expression', r'\widehat E_{U_{O_x}}', r'\mathcal{E}_{\mathcal{U}_{\mathcal{O}_x}}', r'\widehat E_{U_{O_x}}', 'The U nested below the hatted E has an open upper entry and rounded lower return. The hat decision is recorded independently in P07a.')
change('P07b', 'P07', 'main line 5, connector in canonical expression', r'\widehat E_{U_{O_x}}-E_{U_S}', r'\mathcal{E}_{\mathcal{U}_{\mathcal{O}_x}}\to\mathcal{E}_{\mathcal{U}_S}', r'\widehat E_{U_{O_x}}-E_{U_S}', 'The shaft is horizontal, with a single short upturned cap at the right end. No corresponding lower wing makes a paired head. A separate period follows the right E_{U_S}.', consequential=True)
u_change('P07u2', 'P07', 'main line 5, U in the right term of canonical expression', r'E_{U_S}', r'\mathcal{E}_{\mathcal{U}_S}', r'E_{U_S}', 'The right nested U has open upper ends and its own rounded lower turn; the small S sits below/right.')
change('P08a', 'P08', 'above main line 5, canceled insertion attached between Les and relèvements', r'Les \inserted{\deleted{derniers}} relèvements', r"l'hom. \struck{dernier} canonique", r'Les \inserted{\deleted{\unsure{derniers|dernier}}} relèvements', 'A canceled interlinear word has d and the subsequent compressed ernier bodies, with the final s obscured by the strike. Its long curved attachment runs down/left and ends between the live Les and relèvements. The attachment does not end after hom. Added doubt within the canceled letters is certainty-only against C.', confidence='medium', kind='insertion or placement', category='Insertions put in the wrong place')
change('P08b', 'P08', 'main line 5, opening of the parenthesis', r'(Les', r'(\struck{Les} Les', r'(Les', 'There is one legible live Les after a separate opening parenthesis. The lower heavy stroke is continuous with the foot of the L. A second independent canceled Les cannot be separated from these same strokes; the separately canceled material lies above and is recorded in P08a.', confidence='medium', kind='deletion state', category='Struck text')
u_change('P24u', 'P24', 'main line 6, target of the relèvements arrow', r'E_K\longrightarrow E_{U_{O_x}}', r'\mathcal{E}_K\to\mathcal{E}_{\mathcal{U}_{\mathcal{O}_x}}', r'E_K\longrightarrow E_{U_{O_x}}', 'The nested U has two tall open ends and a rounded low turn. The connector has one detached right-pointing head. The saved crop includes the complete U; low K/x extremities touch its lower border and were fully read in the native half.')
change('P09a', 'P09', 'main line 6, abbreviation before aux', r'biuniv.$^{\mathrm t}$', r'\uncertain{biunivoquement}', r'biuniv.$^{\mathrm t}$', 'The tall b and dotted i are followed by low u/n strokes, another small i and final v. A detached point follows the v. A small crossed t stands above the baseline to the right of the point; aux follows separately.', kind='abbreviation expanded or spelling modernised', category='Abbreviations expanded, spelling modernised', marked_in_H=True)
u_change('P10u', 'P10', 'main line 7, U in the sections expression', r'E_{U_\eta}', r'\mathcal{E}_{\mathcal{U}_K}', r'E_{U_{\unsure{\eta|K}}}', 'The U has an open entry and low return. Its smaller nested index has a joined eta/n-like angle; locally secure K forms also sometimes close this angle. The index therefore remains eta|K. This row counts the U alphabet departure only; adding the index doubt is certainty-only against C.')
change('P11a', 'P11', 'main line 7, conjunction before aux', 'ou aux', r'\uncertain{comme aux}', 'ou aux', 'The conjunction consists of a tiny closed o followed by one long flattened u return. The next word has a small a, low u and crossed x. The visible short two-letter conjunction reads ou.', kind='misread word', category='Words', marked_in_H=True)
change('P11b', 'P11', 'main line 7, abbreviation after ou aux', r'relt$^{\mathrm s}$', 'relèvements', r'rel$^{\mathrm t}_{\mathrm s}$', 'The r and low e lead to a tall looped l. A separate t stands raised to the right, with its foot above the rel baseline. The smaller s lies farther right and substantially lower, extending below the rel baseline. The literal raised t and lowered s are both preserved; no period follows.', against_C=True, kind='abbreviation expanded or spelling modernised', category='Abbreviations expanded, spelling modernised')
change('P12a', 'P12', 'main line 8, E_K-E_S expression', r'E_K-E_S', r'\mathcal{E}_K\to\mathcal{E}_S', r'E_K-E_S', 'The K has a visible split stem/diagonal form. The connector is one horizontal unheaded segment with one short downward cap at its right end; no upper wing pairs with it.', consequential=True)
change('P13a', 'P13', 'main line 8, E_K-E_U_S expression', r'E_K-E_{U_S}', r'\mathcal{E}_K\to\mathcal{E}_{\mathcal{U}_S}', r'E_K-E_{U_S}', 'The connector is one unheaded horizontal dash. The right term has E, nested U and S. Three separate dark dots follow the expression, then one closing parenthesis; the ellipsis itself agrees between witnesses.', consequential=True)
u_change('P13u', 'P13', 'main line 8, U in the expression before the ellipsis', r'E_{U_S}', r'\mathcal{E}_{\mathcal{U}_S}', r'E_{U_S}', 'The U has a simple open entry and low bowl with S below/right. The three following dots and closing parenthesis are separately visible.')
u_change('P14u', 'P14', 'main line 10, target of phi_x', r'\varphi_x:E_K\longrightarrow E_{U_{O_x}}', r'\varphi_x:\mathcal{E}_K\to\mathcal{E}_{\mathcal{U}_{\mathcal{O}_x}}', r'\varphi_x:E_K\longrightarrow E_{U_{O_x}}', 'The target U has an open upper-left entry and rounded lower turn. The whole formula has phi with a long descender, x, a two-point colon and one large arrowhead. A short upper kink at the shaft end does not supply a second paired head.')
change('P15a', 'P15', 'main line 10, overwritten preposition before I_x; M1201', r'\unsure{sur|dans}', r'\struck{sur} \uncertain{sur}', r'\unsure{sur|dans}', 'The one overwritten cluster contains a tall d-like upright, low crossed/retraced letter bodies and a final cup/s-like return. The strokes support dans as a local alternative, but do not separate complete old and new word extents or establish their order. A single local doubt therefore preserves the cluster without reconstructing two complete sur tokens.', confidence='low', kind='deletion state', category='Struck text', marked_in_H=True)
u_change('P17u', 'P17', 'main line 11, U in E_U_Ox before sur', r'E_{U_{O_x}}', r'\mathcal{E}_{\mathcal{U}_{\mathcal{O}_x}}', r'E_{U_{O_x}}', 'The U has an open upper entry and low connecting turn. The O_x inside this nested index is unlined; the separate final O after sur has the underline recorded in P17a.')
change('P17a', 'P17', 'main line 11, O_x after sur', r'\underline O_x', r'\mathcal{O}_x', r'\underline O_x', 'A detached horizontal stroke runs beneath the O oval and ends before the small x at its lower right. The underline belongs to this final O, not to the preceding nested O.', consequential=True)
change('P18a', 'P18', 'main line 12, three-letter shorthand', 'sss', 'ssi', 'sss', 'There are three separate sinuous s forms. Each has an upper turn and lower hooked return. The third has a rounded upper loop and a dark lower return; there is no separate dot/stem pair in that third position.', kind='abbreviation expanded or spelling modernised', category='Abbreviations expanded, spelling modernised')
change('P19a', 'P19', 'main line 12, abbreviation before star', r'correspond$^{\mathrm t}$', 'correspondante', r'corresp.$^{\mathrm t}$', 'The ink shows joined c-o, two separate low r returns, a flattened joined e-s stretch and the long p descender. A distinct point follows p; after it comes a long-entry raised t. Separate baseline o-n-d bodies do not occur between p and the point/t. The compressed e-s stretch makes the exact abbreviation medium confidence.', confidence='medium', against_C=True, kind='abbreviation expanded or spelling modernised', category='Abbreviations expanded, spelling modernised')
change('P19b', 'P19', 'main line 12, mark after abbreviated word', '*', '(nothing)', '*', 'A separate multi-ray asterisk lies to the right of the raised t. It is independent of the abbreviation and survives as a visible mark.', kind='omission', category='Omissions')
u_change('P25u', 'P25', 'main line 13, U_S/S', r'U_S/S', r'\mathcal{U}_S/S', r'U_S/S', 'The large U starts with a bent upper-left hook that stays open, descends to a deep bowl and rises on the right. Its small S sits below/right; a separate slash and full-size S follow.')
change('P20a', 'P20', 'main line 13, final word; M1202', r'\unsure{impliquera|implique}', 'impliquera', 'impliquera', 'After i, flattened m, descending p, tall l, dotted i, descending q and low u, the written e-r-a returns continue clearly to the right. The word reaches its final a before the paper edge; no terminal punctuation follows.', against_C=True, against_H=False, kind='misread word', category='Words')
change('P21a', 'P21', 'oblique note, NB heading', r'\uline{NB}', 'NB', r'\uline{NB}', 'The N and B stand above a separate horizontal underline. Its right end is dark and stops below the B.', kind='omission', category='Omissions')
change('P21b', 'P21', 'oblique note, opening article', 'Le', 'La', 'Le', 'The tall L is followed by a short open low e return; the second letter has the compressed open form visible in the nearby le on the next line.', kind='misread word', category='Words')
change('P21c', 'P21', 'oblique note, opening noun', 'quotient', 'quantité', 'quotient', 'The noun begins with a looped q whose long descender crosses the next line. The middle bodies are tightly flattened; toward the end the tall t and short i/e/n returns lead into a final crossed/returned t before de. These contours support quotient. The compressed middle is retained as medium confidence.', confidence='medium', kind='misread word', category='Words')
change('P21d', 'P21', 'oblique note, abbreviation after par le; M1203', r'\unsure{s.groupe}', r'\ill{}', r'\unsure{s.}groupe', 'The initial s-like body is crossed by the descending q of quotient from the line above. A small separate point follows it. The following g has a large descending loop; the low r/o/u bodies, p descender and final e can be traced across groupe. Uncertainty is confined to s.; the legible groupe is retained.', confidence='medium', kind=r'readable ink left as \ill{}', category='Readable ink left as illegible')
change('P21e', 'P21', 'oblique note, left side of final equality', r'E_{\underline O_x}', r'\mathcal{E}_{\mathcal{O}_x}', r'E_{\underline O_x}', 'The O below/right of E is a rounded oval with a detached lower horizontal stroke; x follows outside that underline. The equals sign has two separate short bars. This first underline is securely visible; the final O in Spec remains locally doubtful.', consequential=True)
change('P21f', 'P21', 'oblique note, end after closing parenthesis', ')', ').', ')', 'The final parenthesis has a long upper curve and a dark lower return. No separate full stop follows it in the rotated crop; nearby main-line strokes are at a different angle.', kind='text not on the page', category='Text that is not on the page')
change('P22a', 'P22', 'bottom-left thin foliation', r'\margin{72}', '(nothing)', r'\margin{72}', 'The thin 7 has a curved top and a crossing stroke; the 2 has an upper arch, diagonal descent and long baseline. Their narrow pen and small size differ from the autograph head number and main writing.', kind='omission', category='Omissions')

def decision(mid, status, reading, crop_id, evidence, confidence):
    cp = crop_by_id[crop_id]
    coords = ','.join(str(v) for v in cp['box'])
    return dict(id=mid, cote='149', scan='73', decision=status, reading=reading, evidence=evidence, crop=f"{cp['path']} ({coords})", confidence=confidence)

decisions = [
    decision('M1200', 'first', r'\widehat E', 'P07', 'Two short inner sloping strokes form a peak against the outer upper E lobe. Both peaked segments can be separated from the curved outer contour, despite their contact. The entire following formula was read with this decoration.', 'medium'),
    decision('M1201', 'undecided', r'\unsure{sur|dans}', 'P15', 'A tall d-like stroke and a final s/cup favor dans locally, but crossing and retraced low bodies leave sur/dans and overwrite chronology unresolved. No complete second word is reconstructed.', 'low'),
    decision('M1202', 'first', 'impliquera', 'P20', 'The e-r-a ending continues visibly after qu. The final a is present before the edge; the shorter implique alternative leaves those written returns unaccounted for.', 'high'),
    decision('M1203', 'undecided', r'\unsure{s.}groupe', 'P21', 'The q descender from quotient crosses the initial s-like body. A small point and the following groupe are legible. The retained doubt is narrowed to s.; no full resolution of the supplied mark is claimed.', 'medium'),
    decision('M1204', 'undecided', r'\unsure{I_x|\overline I_x}', 'P21', 'One short horizontal cap lies above the I stem with a small gap. No second independent top cap can be isolated, so the relation of that stroke to I as a serif or overbar remains unresolved. The lower foot and x are legible.', 'low'),
    decision('M1205', 'undecided', r'\unsure{O_x|\underline O_x}', 'P21', 'The final O has an open/overlapped upper contour, and a short low horizontal return is close to its lower edge. That return cannot be separated securely as an underline. The small x and closing parenthesis remain visible. The separate underline on the first O of the equality is clear.', 'low'),
]

inventory = [
    dict(element='E01', kind='margin note', position='head near centre; [850,24,930,79]', first_words_or_objects='36', sheet_kind='text', hand='his hand', transcribed='yes'),
    dict(element='E02', kind='diagram', position='upper part; [170,40,1130,310]', first_words_or_objects=r'(9): U_S, U_{O_x}, U_K, U_{\overline K}, \widetilde U_S; lower S, \underline O_x, K, \overline K', sheet_kind='text', hand='his hand', transcribed='yes'),
    dict(element='E03', kind='diagram', position='below diagram (9); [180,425,840,705]', first_words_or_objects=r'(10): E_{U_S}, E_{U_{O_x}}, E_{U_K}; lower E_S, E_{\underline O_x}, E_K; dashed diagonal \varphi_x', sheet_kind='text', hand='his hand', transcribed='yes'),
    dict(element='E04', kind='text', position='main lines 1–8, approximately y725–1835', first_words_or_objects='avec des carrés cartésiens, et des flèches', sheet_kind='text', hand='his hand', transcribed='yes'),
    dict(element='E05', kind='insertion', position='above main line 5; [1110,1220,1595,1395]; curved leader ends between Les and relèvements', first_words_or_objects=r'\inserted{\deleted{\unsure{derniers|dernier}}}', sheet_kind='text', hand='his hand', transcribed='yes'),
    dict(element='E06', kind='deletion', position='same interlinear word as E05; strike passes through the word above main line 5', first_words_or_objects=r'\deleted{\unsure{derniers|dernier}}', sheet_kind='text', hand='his hand', transcribed='yes'),
    dict(element='E07', kind='text', position='main lines 9–13, approximately y1850–2364', first_words_or_objects="Ceci dit, j'ai envie de prouver que", sheet_kind='text', hand='his hand', transcribed='yes'),
    dict(element='E08', kind='text', position='overwritten cluster in main line 10; [1050,1945,1325,2060]', first_words_or_objects=r'\unsure{sur|dans} I_x', sheet_kind='text', hand='his hand', transcribed='yes'),
    dict(element='E09', kind='margin note', position='oblique lower-left note, five short lines; [20,1860,420,2320]', first_words_or_objects=r'\uline{NB} Le quotient de E_K', sheet_kind='text', hand='his hand', transcribed='yes'),
    dict(element='E10', kind='margin note', position='bottom left; [160,2288,230,2355]', first_words_or_objects='72', sheet_kind='text', hand='another hand', transcribed='yes'),
]

doubts = [
    dict(place='above main line 5, canceled insertion', reading=r'\inserted{\deleted{\unsure{derniers|dernier}}}', alternatives='derniers | dernier', confidence='low', reason='The strike covers several joined bodies and the final s. Placement is separately established by the curved leader; the exact canceled ending is retained as uncertain.'),
    dict(place='main line 7, nested index in E_U', reading=r'E_{U_{\unsure{\eta|K}}}', alternatives=r'\eta | K', confidence='low', reason='The small joined index has eta/n-like turns. Secure K on this same page ranges from a closed angle in adjacent E_K and the diagrams to a split stem/diagonal at P12. The local variation prevents a certain letter assignment.'),
    dict(place='main line 10, overwritten preposition; M1201', reading=r'\unsure{sur|dans}', alternatives='sur | dans', confidence='low', reason='The tall d-like upright and final cup are visible, but the intervening crossed low strokes do not establish separate word extents or chronology.'),
    dict(place='oblique note, abbreviated prefix; M1203', reading=r'\unsure{s.}groupe', alternatives='s. remains uncertain; groupe is legible', confidence='medium', reason='The q descender from quotient passes through the initial s-like body. The following point and groupe remain separately readable.'),
    dict(place='oblique note, I_x after engendré par; M1204', reading=r'\unsure{I_x|\overline I_x}', alternatives=r'I_x | \overline I_x', confidence='low', reason='One horizontal cap sits above a slightly separated stem; the source does not securely distinguish the cap as a serif or as a separate overbar.'),
    dict(place='oblique note, final O_x in equality; M1205', reading=r'E_{\underline O_x}=\pi_1(\operatorname{Spec}\unsure{O_x|\underline O_x})', alternatives=r'O_x | \underline O_x', confidence='low', reason='The final O has an open upper contour and a low horizontal return that may belong to the body or an underline. The first O underline in this equality is separately clear.'),
]

notes = [
    '[S073.1; source diagrams and following sentence] The page contains diagrams numbered (9) and (10). The following source words call the squares cartésiens and the horizontal arrows surjectives. This is a report of the author\x27s wording; no mathematical verification was performed.',
    '[S073.2; source first paragraph] The author describes the written E_K left-arrow E_U_S expression as a composition involving a relèvement and a canonical expression. The parenthesis contains the correspondence phrased correspondent biuniv. with raised t, then sections and the abbreviated rel with raised t and lowered s. The literal connectors are retained individually.',
    '[S073.3; source second paragraph] The author writes "j\x27ai envie de prouver que" before the phi_x expression and the overwritten preposition before I_x. The following source wording includes literal sss and corresp. with raised t. It is preserved as the author\x27s stated objective, without presenting it as an established result.',
    r'[S073.4; source oblique note] The NB note begins Le quotient de E_K and gives the written equality E_{\underline O_x}=\pi_1(\operatorname{Spec}\unsure{O_x|\underline O_x}). The s. prefix and the I_x bar relation remain local reading doubts. No mathematical derivation is supplied by this transcription.',
    '[S073.5; physical page ending] The final main-text words are Ceci impliquera. There is no terminal stop and no completion supplied beyond this sheet.',
    'All thirteen main-text lines and all five short lines of the oblique note were read against both witnesses in the native halves. The diagrams, all agreed words, abbreviations, punctuation, accents, indices, decorations, endpoints and source numbers were inspected. P03 confirms the detached accent in flèches; P16 separates provient from the overlapping marginal parenthesis.',
    'Diagram (9) has five upper objects and four lower objects, with four upper horizontal, three lower horizontal and four vertical unheaded segments. The r/l syntax differences in the witnesses draw the same unheaded connections. Diagram (10) has three upper and three lower objects, four leftward horizontal arrows, three downward arrows, and one dashed up-left diagonal. All seven horizontal/vertical arrows have one head; the diagonal points into the upper-middle object. Its phi_x label lies northeast/right of the diagonal.',
    'The ordinary U observations are recorded per source occurrence in the change log. The two-lobed E and simple O font wrappers alone are treated as established typographic renderings; explicit hats, bars and underlines are independently transcribed and counted.',
    'The canceled insertion has a curved attachment ending between Les and relèvements. The live Les is written once. The star after corresp. with raised t is retained as a separate mark; no additional attachment from that star to the oblique note is invented.',
    'The initial crop P01 clips part of the far-right tilde, which was fully read in the original/native view. Its audit box includes the full tilde. P14 reaches the lower phi-descender edge, and P24 reaches the lower K/x tips; the complete glyphs were read in the native half, and the audit boxes extend below those crop borders. Existing crops were not replaced.',
    'Twenty-two first crops were prepared for the original mandatory/open places. Three further first crops, P23–P25, document the distinct ordinary-U formula places otherwise covered only by native views. They do not repeat an already saved place.',
]

hand = [
    dict(form='ordinary U', observation='A short entry or open hook at the upper left leads into a long side, a low rounded bowl and an ascending right side. No closed upper-left loop is formed at the eighteen occurrences read on this sheet. The large final U_S/S has an especially clear open hook.', places='diagram (9), five upper objects; diagram (10), three upper objects; main lines 3, 4, 5 twice, 6, 7, 8, 10, 11 and 13', scope='all eighteen U occurrences on scan073, compared locally and with the supplied notation distinction', witness_errors='H consistently renders these occurrences with mathcal U; each source occurrence has its own material row.'),
    dict(form='two-lobed E', observation='The upper curved lobe joins a longer lower lobe. The ordinary E rendering follows the established supplied notation mapping. The inner peaked pair on the initial E of canonique is separately visible and retained as a hat.', places='both diagrams and every E expression; hat at P07', scope='all observed E forms on this sheet', witness_errors='E/mathcal-E wrappers alone are not counted; H omits the distinct hat at P07.'),
    dict(form='K / eta-like small index', observation='Some K forms close the diagonal into a joined n-like angle; P12 has a visibly split stem and diagonal. The nested index at P10 resembles the joined forms closely enough to keep eta|K.', places='P02, P05, P10, P12, P23, P24', scope='local comparison only; no global regularization', witness_errors='The differing C eta / H K readings are retained as one local index doubt; no resolved index error is counted.'),
    dict(form='unheaded connectors', observation='A short shaft may finish with one small upturned or downward cap. Those single caps remain literal unheaded connectors; the paired detached heads on P23/P24 and the large head on P14 are separately identifiable.', places='unheaded P05/P07/P12/P13; headed P23/P24/P14; diagrams P01/P02', scope='each endpoint inspected independently', witness_errors='H supplies right arrows at the four unheaded body connectors.'),
    dict(form='hat touching upper E lobe', observation='Two inner sloping segments form a peak and touch the upper E contour. Their independent angled paths distinguish the decoration while its physical overlap is retained in the evidence.', places='P07, M1200', scope='this single E only', witness_errors='C doubted the hat; H omitted it.'),
    dict(form='raised t / lowered s', observation='The terminal t of rel is raised above the letter baseline. The following small s lies farther right and reaches below that baseline. In biuniv. and corresp. the t is likewise raised, after an explicit point.', places='P09, P11, P19', scope='these three abbreviated forms', witness_errors='C places the t/s levels differently in rel and reads too many baseline letters in corresp.; H expands the abbreviated words.'),
    dict(form='compressed e-s and p', observation='In corresp. the two r returns are separate; the following e-s bodies are flattened into a short connected stretch before the clear p descender. A separate point immediately follows the p.', places='P19', scope='this single abbreviated word; medium confidence in the compressed middle', witness_errors='C supplies baseline ond after p; H expands the abbreviation and omits the following star.'),
    dict(form='accent / stop / pen return', observation='The accent above the first e of flèches is detached and dark. Both hom tokens end at the m return without a stop. Three separate dots precede the closing parenthesis at P13. The last main word and marginal parenthesis have no terminal stop.', places='P03, P04, P06, P13, P20, P21', scope='each named place inspected locally', witness_errors='H adds stops after both hom tokens and after the marginal parenthesis.'),
    dict(form='q descender crossing marginal prefix', observation='The long descender of q in quotient reaches into the next line and crosses the s-like initial of s.groupe. Its origin remains visible; it is not treated as a cancellation.', places='P21, first two marginal lines', scope='local overlap', witness_errors='H reads quantité and leaves the following abbreviated word as ill; the s. prefix remains doubtful.'),
    dict(form='overwritten preposition', observation='A tall d-like upright, low crossed or retraced bodies and final s-like cup occupy a single compact cluster. Complete old/new token extents cannot be assigned securely.', places='P15, M1201', scope='this word only', witness_errors='H gives separate canceled and live sur; the proposed reading preserves one local sur|dans doubt.'),
    dict(form='thin foliation versus autograph numbers', observation='The small bottom-left 72 uses a thin pen, with a crossed 7 and a looped/diagonal 2. The head 36 is larger autograph writing; diagram labels 9 and 10 are autograph.', places='header; diagram numbers; P22', scope='all source numbering on this sheet', witness_errors='H omits the bottom-left 72; its note records the autograph36.'),
]

notation = [
    dict(form=r'\widetilde U_S', meaning='Far-right upper object of source diagram (9); the tilde is visible in the native image.', places='diagram (9)'),
    dict(form=r'\varphi_x:E_K\longrightarrow E_{U_{O_x}}', meaning='The expression after the source words j\x27ai envie de prouver que; phi_x also labels the dashed up-left diagonal of diagram (10).', places='diagram (10); main line 10'),
    dict(form=r'\widehat E_{U_{O_x}}-E_{U_S}', meaning='The literal expression following the source word canonique; the initial E carries the peaked decoration and the connector is unheaded.', places='main line 5, P07'),
    dict(form=r'E_{U_{\unsure{\eta|K}}}', meaning='Expression in the source phrase sections de; the nested index remains graphically unresolved.', places='main line 7, P10'),
    dict(form=r'E_{\underline O_x}=\pi_1(\operatorname{Spec}\unsure{O_x|\underline O_x})', meaning='Equality written at the end of the source NB note. The first O underline is clear; the decoration of the final O remains uncertain.', places='oblique note, P21'),
]

abbreviations = [
    dict(written='hom', expansion='homomorphisme', places='main lines 2 and 4; neither written occurrence has a stop'),
    dict(written=r'biuniv.$^{\mathrm t}$', expansion='biunivoquement', places='main line 6, P09'),
    dict(written=r'rel$^{\mathrm t}_{\mathrm s}$', expansion='relèvements', places='main line 7, P11'),
    dict(written='i.e.', expansion='id est', places='main line 10'),
    dict(written='sss', expansion='si et seulement si; the literal written shorthand remains sss', places='main line 12, P18'),
    dict(written=r'corresp.$^{\mathrm t}$', expansion='correspondante', places='main line 12, P19'),
    dict(written=r'\unsure{s.}groupe', expansion='sous-groupe; initial s. remains a reading doubt', places='oblique note, P21'),
    dict(written='NB', expansion='nota bene', places='underlined opening of oblique note'),
]

audit_boxes = []
def audit(number, kind, coords, reading):
    audit_boxes.append(dict(box=f'B{number:02d}', kind=kind, coords=coords, reading=reading))

audit(1, 'handwritten number', [850,24,930,79], r'\mspage{36}')
audit(2, 'handwritten number', [170,40,1130,310], r'(9): top U_S - U_{O_x} - U_K - U_{\overline K} - \widetilde U_S; lower S - \underline O_x - K - \overline K; four unheaded vertical segments below the first four upper objects')
audit(3, 'handwritten number', [180,425,840,705], r'(10): top E_{U_S} \longleftarrow E_{U_{O_x}} \longleftarrow E_{U_K}; lower E_S \longleftarrow E_{\underline O_x} \longleftarrow E_K; three downward arrows; dashed E_K to upper-middle E_{U_{O_x}}, head up-left, label \varphi_x northeast/right of diagonal')
audit(4, 'C/H word disagreement', crop_by_id['P04']['box'], "L'hom")
audit(5, 'C/H word disagreement', crop_by_id['P05']['box'], r'E_K-E_{U_{O_x}}')
audit(6, 'C/H word disagreement', crop_by_id['P06']['box'], "l'hom")
audit(7, 'formula with doubt', crop_by_id['P07']['box'], r'\widehat E_{U_{O_x}}-E_{U_S}.')
audit(8, 'insertion', crop_by_id['P08']['box'], r'(Les \inserted{\deleted{\unsure{derniers|dernier}}} relèvements; curved attachment ends between Les and relèvements')
audit(9, 'struck passage', crop_by_id['P08']['box'], r'\inserted{\deleted{\unsure{derniers|dernier}}}; one live Les on baseline')
audit(10, 'C/H word disagreement', crop_by_id['P09']['box'], r'biuniv.$^{\mathrm t}$ aux')
audit(11, 'formula with doubt', crop_by_id['P10']['box'], r'E_{U_{\unsure{\eta|K}}} sur E_K')
audit(12, 'C/H word disagreement', crop_by_id['P11']['box'], r'ou aux rel$^{\mathrm t}_{\mathrm s}$')
audit(13, 'C/H word disagreement', crop_by_id['P12']['box'], r'E_K-E_S')
audit(14, 'C/H word disagreement', crop_by_id['P13']['box'], r'E_K-E_{U_S}\ldots)')
audit(15, 'struck passage', crop_by_id['P15']['box'], r'\unsure{sur|dans} I_x; single overwritten cluster, separate old/new word extents unresolved')
audit(16, 'C/H word disagreement', crop_by_id['P17']['box'], r'E_{U_{O_x}} sur \underline O_x')
audit(17, 'C/H word disagreement', crop_by_id['P18']['box'], 'sss')
audit(18, 'lower confidence departure', crop_by_id['P19']['box'], r'corresp.$^{\mathrm t}$ *')
audit(19, 'C/H word disagreement', crop_by_id['P20']['box'], 'impliquera')
margin_reading = r'\uline{NB} Le quotient de $E_K$ par le \unsure{s.}groupe engendré par $\unsure{I_x|\overline I_x}$ n\x27est autre que $E_{\underline O_x}=\pi_1(\operatorname{Spec}\unsure{O_x|\underline O_x})$'
margin_reading = margin_reading.replace(r'\x27', "'")
audit(20, 'margin note', crop_by_id['P21']['box'], margin_reading)
audit(21, 'formula with doubt', crop_by_id['P21']['box'], margin_reading)
audit(22, 'handwritten number', crop_by_id['P22']['box'], r'\margin{72}')
audit(23, 'C/H word disagreement', crop_by_id['P23']['box'], r'E_K\longleftarrow E_{U_S}')
audit(24, 'C/H word disagreement', [305,1420,775,1580], r'E_K\longrightarrow E_{U_{O_x}}')
audit(25, 'C/H word disagreement', crop_by_id['P25']['box'], r'U_S/S')
audit(26, 'C/H word disagreement', [300,1930,805,2085], r'\varphi_x:E_K\longrightarrow E_{U_{O_x}}')

coverage = {
    1: ('editorial page marker', 'The scan marker and H editorial p. marker are not source prose; the visible autograph36 is preserved.'),
    2: ('editorial page marker', 'H de l\x27auteur belongs to its editorial page note. The source header is36.'),
    3: ('macro syntax only', 'ampersand replacement is a TikZ syntax option, with no additional source token.'),
    4: ('equivalent typography', 'The first upper edge in (9) is unheaded; moving its command to the neighboring node preserves the same segment. The local U alphabet is separately recorded at P01u1/P01u2.'),
    5: ('equivalent typography', 'The second upper-node r/l difference draws the same unheaded connection. The U forms are separately recorded per occurrence.'),
    6: ('equivalent typography', 'The third upper-node r/l difference draws the same unheaded connection.'),
    7: ('equivalent typography', 'The fourth upper-node r/l difference draws the same unheaded connection.'),
    8: ('macro syntax only', 'The aligned lower-row S is present in both diagrams; this difference is induced by edge-command/node alignment.'),
    9: ('equivalent typography', 'The S to underlined O_x segment is unheaded; r/l command direction is not an arrow direction. The underline is recorded separately at P01b.'),
    10: ('macro syntax only', 'The lower-row S is the same written object in both witnesses, shifted in the token alignment.'),
    11: ('equivalent typography', 'The lower O_x to K segment is unheaded and connects the same objects.'),
    12: ('equivalent typography', 'The lower K to barred K segment is unheaded and connects the same objects.'),
    13: ('equivalent typography', 'The final lower-row command is attached to the opposite endpoint of the same unheaded segment.'),
    14: ('macro syntax only', 'Display and diagram wrapper boundaries supply no source token.'),
    15: ('macro syntax only', 'The ampersand replacement option affects TeX parsing only.'),
    16: ('material; P02c', 'The prime swaps the phi_x label to the observed northeast/right side of the up-left diagonal.'),
    17: ('macro syntax only', 'H explanatory note is editorial, not copied into the source text. Its observation of the underline is incorporated in the diagram; actual source underline rows are P01b/P02b.'),
    18: ('material; P04a', 'The first hom has no following stop.'),
    19: ('macro syntax only', 'H sic note is editorial. The source left arrow itself was read in P23.'),
    20: ('material; P05a', 'The source connector is unheaded, with one rounded terminal cap.'),
    21: ('material; P06a/P08a', 'The second hom has no stop; the canceled word is attached between Les and relèvements by its curved leader.'),
    22: ('material; P07a/P07b', 'The canonical expression has a visible hat and an unheaded connector. Both are independently recorded.'),
    23: ('material; P08a/P08b', 'One live Les is followed by the attached canceled interlinear word, whose ending remains doubtful.'),
    24: ('material; P09a', 'Source biuniv. has a detached point and raised t; H expands it.'),
    25: ('certainty only', 'C eta and H K remain alternatives in one local nested-index doubt. The ordinary-U alphabet at this place is separately material in P10u.'),
    26: ('material; P11a', 'The short two-letter conjunction reads ou before aux.'),
    27: ('material; P11b', 'The source abbreviated rel has raised t and lowered s, preserving both written script positions.'),
    28: ('material; P12a', 'The connector has one downward cap and no paired head.'),
    29: ('material; P13a', 'The second connector in the parenthesis is likewise unheaded.'),
    30: ('equivalent typography', 'Both witnesses represent the same three source dots, with ldots versus the ellipsis character. The source has three dots and one closing parenthesis.'),
    31: ('material; P21a/P21b/P21c/P21d/P21e/P21f', 'The long alignment mismatch arises from different placement of the same margin note relative to the main paragraph; it is not a wholesale omission. The note\x27s actual lexical, underline and punctuation departures are separately recorded.'),
    32: ('material; P15a', 'The crossed word remains one sur|dans cluster. Separate old/new word extents cannot be read securely.'),
    33: ('material; P18a', 'All three letters are s-shaped; literal sss is retained.'),
    34: ('material; P19a/P19b', 'Source corresp. has raised t followed by a separate star. C has extra baseline letters; H expands the abbreviation and omits the star.'),
    35: ('material; P20a/P21a/P21b/P21c/P21d/P21e/P21f/P22a', 'M1202 resolves to impliquera. The margin note is fully transcribed despite alignment order, with its local M1203–M1205 doubts; the thin bottom foliation72 is retained.'),
}
diff_coverage = [dict(row=n, status=status, reason=reason) for n,(status,reason) in coverage.items()]

review = [
    r'C \inserted{\deleted{derniers}}: the interlinear word is visibly canceled, but its struck ending remains uncertain. The proposal retains \inserted{\deleted{\unsure{derniers|dernier}}}.',
    'The curved attachment of that insertion was traced from the canceled word to the gap between the live Les and relèvements. Its path is recorded independently of the word reading.',
    'The baseline Les appears once and is live. The heavy lower stroke belongs to its L foot; no additional complete canceled Les is reconstructed.',
    'The H canceled dernier after hom is reassigned to the visible interlinear insertion using the source leader. Both hom tokens have no terminal stop.',
    'The overwritten preposition before I_x has unresolved old/new extents. It is transcribed as a single sur|dans doubt; neither a complete canceled sur nor a separate replacement word is invented.',
    'The q descender from quotient crosses the s-like marginal prefix. It remains attached to q and does not cancel that prefix.',
    'The main word provient is crossed spatially by the oblique note\x27s final parenthesis. The main word remains live; the crossing parenthesis is part of the separate marginal formula.',
]

report = dict(
    page=PAGE, scan=73, reader='reader_a', line_count=13,
    changes=changes, decisions=decisions, inventory=inventory, doubts=doubts,
    notes=notes, check_events=[], hand=hand, notation=notation,
    abbreviations=abbreviations, audit_boxes=audit_boxes,
    diff_coverage=diff_coverage, deletion_insertion_review=review,
    open_issues=[
        'Six local reading doubts are retained in place: canceled derniers/dernier, eta/K, overwritten sur/dans, the s. prefix, the I_x cap/bar relation, and the final O_x lower-stroke relation. Root reviewed and agreed to retain each.',
        'Root has reviewed all 25 saved crops, including the three final ordinary-U formula crops. No additional unreviewed crop or reading decision remains.',
    ],
    viewed=['page', 'top half', 'bottom half'] + [entry['path'] for entry in manifest]
)

def restore_quotes(obj):
    if isinstance(obj, str):
        return obj.replace('\\x27', "'")
    if isinstance(obj, list):
        return [restore_quotes(x) for x in obj]
    if isinstance(obj, dict):
        return {k: restore_quotes(v) for k,v in obj.items()}
    return obj

report = restore_quotes(report)
report_path = BASE / 'readings' / f'{PAGE}.json'
report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')

expected_marks = [row['id'] for row in csv.DictReader((PACKET/'marks.tsv').open(), delimiter='\t')]
assert [row['id'] for row in report['decisions']] == expected_marks
assert len(report['diff_coverage']) == 35
assert [row['row'] for row in report['diff_coverage']] == list(range(1,36))
assert len({row['id'] for row in changes}) == len(changes)
assert all((BASE/row['crop']).exists() for row in changes)
assert all(len(row['box']) == 4 and row['box'][0] < row['box'][2] and row['box'][1] < row['box'][3] for row in changes)
assert all(0 <= b['coords'][0] < b['coords'][2] <= 1680 and 0 <= b['coords'][1] < b['coords'][3] <= 2364 for b in audit_boxes)
assert tex.count('{') == tex.count('}')
assert tex.count(r'\unsure') == 6
assert len(manifest) == 25
print(json.dumps(dict(page=PAGE, changes=len(changes), against_C=sum(x['against_C'] for x in changes), against_H=sum(x['against_H'] for x in changes), decisions=len(decisions), crops=len(manifest), audit_boxes=len(audit_boxes), doubts=len(doubts)), indent=2))
