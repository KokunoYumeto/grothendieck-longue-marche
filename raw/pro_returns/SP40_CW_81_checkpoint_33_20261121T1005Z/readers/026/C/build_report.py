from pathlib import Path
import json,re,hashlib,itertools

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[3]
C=BASE.joinpath('packets/026/C.tex').read_text()
H=BASE.joinpath('packets/026/H.tex').read_text()
source=BASE.joinpath('packets/026/C_doubts.txt').read_text()
sm=json.loads(ROOT.joinpath('source_map_base.json').read_text())
g={x['id']:x for x in sm['groups']}
crops=json.loads(ROOT.joinpath('crop_audit.json').read_text())
views=json.loads(ROOT.joinpath('image_audit.json').read_text())
diff=[]
def row(ident,loc,c,h,reading,evidence,kind='other',dc=False,dh=False,status=None,crop=None,bbox=None,source_rows=None,confidence='medium',**extra):
    r={'id':ident,'location':loc,'C':c,'H':h,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':dc,'diff_H':dh,'C_doubt_status':status,'readers_crop':('crops/'+crop+'.png') if crop else None,'bbox':{'system':'full scan; top-left origin, x right/y down','coordinates':bbox} if bbox else None,'source_rows':source_rows or [],**extra}
    diff.append(r);return r

def expand_unsure(text):
    """Source-only enumeration of complete local alternatives, preserving their surrounding text."""
    start=text.find(r'\unsure{')
    if start<0:return [text]
    left=start+len(r'\unsure{');level=1;end=left
    while end<len(text) and level:
        ch=text[end]
        if ch=='{' and (end==0 or text[end-1]!='\\'):level+=1
        elif ch=='}' and (end==0 or text[end-1]!='\\'):level-=1
        end+=1
    if level:return [text]
    body=text[left:end-1];parts=[];last=0;level=0
    for j,ch in enumerate(body):
        if ch=='{' and (j==0 or body[j-1]!='\\'):level+=1
        elif ch=='}' and (j==0 or body[j-1]!='\\'):level-=1
        elif ch=='|' and level==0:
            parts.append(body[last:j]);last=j+1
    parts.append(body[last:])
    out=[]
    for part in parts:out.extend(expand_unsure(text[:start]+part+text[end:]))
    return list(dict.fromkeys(out))

row('D01','opening definition term',r'\uline{décomposition binaire}',r'\emph{disposition binaire}',r'\uline{\unsure{décomposition|dècomposition|decomposition|disposition} binaire}','The long word has a high initial d, a reduced middle before the descending p, and a small raised mark after the initial. The first candidate remains décomposition; the compressed middle and raised mark keep the full alternatives. The underline extends through binaire.','misread word',True,True,crop='01_title',bbox=[873,119,1400,190],qualification='H disposition is retained as an alternative; this is a qualified primary difference, not a conclusive rejection of H.',candidate_states=[{'complete_reading':w+' binaire','hand':'his hand','role':'complete underlined term','attachment':'opening definition'} for w in ['décomposition','dècomposition','decomposition','disposition']])
row('D02','opening family Sigma',r'\Sigma_\alpha^\alpha',r'\Sigma^\alpha',r'\Sigma_\alpha^\alpha with the complete literal short head/body group','A raised alpha and a separate low alpha are both visible; the low one has a small low loop and right tail. The Sigma has a detached short upper run, retained literally. Its head/retrace versus independent-run allocation remains qualified.','omission',True,True,crop='02_family',bbox=[602,290,686,346],source_groups=['C026-S01'],confidence='high',qualification='Glyph and both alpha placements high confidence; role of detached upper run remains unresolved.',physical_parent_for=['G-S01'])
row('D03','family index after membership',r'\unsure{\mathcal E|\mathscr E|\varepsilon}',r'\omega; note: \alpha\in\omega or \alpha\in\varepsilon',r'\unsure{\mathcal E|\mathscr E|\varepsilon}','The terminal has two stacked curved lobes and a low rightward sweep. These support the retained calligraphic/script-E and epsilon candidates; the source H omega primary is different.','misread symbol or index',False,True,'retained','02_family',[743,317,781,352],['C026-R01'],qualification='H epsilon survives in the reader alternatives; the H primary difference is qualified.')
row('D04','second ens, after X est un',r'ens',r'ens.',r'ens','The final short horizontal letter run is followed by open paper before de; no separate stop is visible. The first ens. retains its stop independently.','abbreviation expanded or spelling modernised',False,True,bbox=[565,230,681,274],confidence='high',evidence_view='half_a')
row('D05','after topologique, before les',r"on s'intéresse au cas où",r'on \uncertain{suppose} \ill{} \ill{} que',r"on \unsure{s'intéresse|s'intèresse|s'interesse} au cas où",'The initial on, s, apostrophe, tall t and reduced intéresse continuation are visible, followed by au cas où. The raised mark within intéresse remains locally qualified for accent direction/allocation.','readable ink left as \\ill{}',True,True,crop='03_topological_prose',bbox=[628,704,1415,790],candidate_states=[{'complete_reading':'on '+w+' au cas où','hand':'his hand','role':'complete prose clause','attachment':'between topologique and les'} for w in ["s'intéresse","s'intèresse","s'interesse"]],H_parent_scope='the contiguous suppose/ill/ill/que phrase is one recovered passage')
row('D06','hémisphères before the main Sigma_alpha',r'hémisphères',r'\struck{hémisphères} les',r'live hémisphères with local initial crossing run | \deleted{h}émisphères','A short horizontal and oblique run cross the initial looped h; the rest of the word has no continuous cancellation through it. The whole word is retained, with the initial-cross allocation left open. The preceding les is on the preceding physical line.','deletion state (struck given live or live given struck)',True,True,crop='17_hemispheres',bbox=[281,857,655,931],source_groups=['C026-G01'],candidate_states=g['C026-G01']['candidate_states'])
row('D07','raised de before plus',r'\inserted{de}',r'\add{de}',r'(et \inserted{de} plus, with a complete curved guide','The guide rises from the gap after et, bends right under the added de, and ends above plus. Both the initial parenthesis and terminal comma are retained.','drawing or diagram',True,True,crop='18_de_plus',bbox=[1328,776,1596,895],source_groups=['C026-G02'],qualification='Wording and insertion state agree with both witnesses; this row records their omitted explicit guide geometry.')
row('D08','whole raised equation before connexes',r'\inserted{\Sigma_\alpha^\alpha et \Sigma_{\deleted{\unsure{\alpha}}}^\alpha\setminus E=\Sigma_{\deleted{\unsure{\alpha}}}^{\deleted{\unsure{\alpha}}\alpha,\unsure{0|\circ|o}}}',r'\note{interligne ... \Sigma^\alpha et \Sigma^\alpha\smallsetminus E=\Sigma^{\alpha,0}}','Complete first double-alpha Sigma; second Sigma with lower alpha state; third Sigma with lower and upper predecessor/trace states; all local alternatives in R02 and R15','The first inserted Sigma has both upper and lower alpha. The second has a dark low alpha-shaped cluster. The third has a dark low cluster and a separate upper dark patch before its live alpha/comma/ring. H supplies the formula but omits these lower and predecessor forms.','omission',False,True,crop='04_inserted_formula',bbox=[672,875,1041,942],source_groups=['C026-S03','C026-S04','C026-S05'],H_parent_scope='one physical inserted equation; local variable states below have diff_H=false to avoid counting that omission repeatedly')
row('D09a','inserted equation, second Sigma low cluster',r'\Sigma_{\deleted{\unsure{\alpha}}}^\alpha',r'\Sigma^\alpha',r'\Sigma_{\deleted{\alpha}}^\alpha | \Sigma_\alpha^\alpha','The lower patch keeps a pointed loop and down-right tail; its darkness does not settle a separate cancellation state. The complete glyph is drawn once.','deletion state (struck given live or live given struck)',True,False,'retained','04_inserted_formula',[824,886,890,939],['C026-R02'],source_part='R02-a',source_groups=['C026-S04'],H_count_parent='D08',raw_diff_H=True,new_qualification='C already doubts the alpha glyph, but prints its deletion state firmly. This reader also qualifies that state.')
row('D09b','inserted equation, third Sigma low cluster',r'\Sigma_{\deleted{\unsure{\alpha}}}^{...}',r'\Sigma^{\alpha,0}',r'lower \deleted{\alpha} | live lower \alpha, each with the complete third Sigma state','A dark low hooked/looped cluster sits below the right end of the body. The retained shape supports alpha; its overwritten/cancelled allocation remains open.','deletion state (struck given live or live given struck)',True,False,'retained','04_inserted_formula',[959,874,1041,930],['C026-R02'],source_part='R02-b',source_groups=['C026-S05'],H_count_parent='D08',raw_diff_H=True,physical_cluster='third inserted Sigma')
row('D09c','inserted equation, third Sigma upper patch',r'\Sigma^{\deleted{\unsure{\alpha}}\alpha,0}',r'\Sigma^{\alpha,0}',r'upper \deleted{\alpha} before live \alpha,0 | independent upper dark trace with live \alpha,0','The upper dark patch has a triangular/rounded body and short foot, separated from the short Sigma head. The old-alpha reading survives, but the visible patch alone leaves its alphabetic role and cancellation allocation unsettled.','misread symbol or index',False,False,'retained','04_inserted_formula',[966,874,987,891],['C026-R02'],source_part='R02-c',source_groups=['C026-S05'],H_count_parent='D08',raw_diff_H=True,physical_cluster='third inserted Sigma',C_count_parent='D09b',raw_diff_C=True,candidate_hand='his hand for the cancelled-alpha candidate; undetermined hand for an independent upper-trace candidate')
row('D10','after connexes in the parenthesis',r'\deleted{\unsure{$\Sigma_\alpha$|les}}',r'\ill{}',r'\deleted{$\Sigma_\alpha$}','The surviving body has an upper return, diagonal waist and low foot, followed by a small low alpha. Distinct crossing strokes traverse it; the les candidate is no longer needed.','readable ink left as \\ill{}',True,True,'resolved','04_inserted_formula',[1048,936,1117,991],['C026-R03'],source_groups=['C026-S06'],confidence='medium',H_parent_scope='one complete ill placeholder')
row('D11','after that cancellation, before E nonempty',r'et où',r'et \uncertain{si}',r'et où','The next word has the two low pieces and raised mark of où, after a readable et.','misread word',False,True,bbox=[1157,931,1362,979],confidence='medium',evidence_view='half_a')
row('D12','following si les, Sigma lower cluster',r'\Sigma_{\deleted{\unsure{\alpha}}}^\alpha',r'\Sigma^\alpha',r'\Sigma_{\deleted{\alpha}}^\alpha | \Sigma_\alpha^\alpha','The low dark patch has a left lobe and descending right tail under the clear raised alpha. Its separate cancellation state remains unresolved.','deletion state (struck given live or live given struck)',True,True,'retained','05_following_si',[785,1001,886,1072],['C026-R02'],source_part='R02-d',source_groups=['C026-S07'])
row('D13','same line, relation between E and empty-set sign',r'\unsure{\ne|+}',r'\neq',r'\ne | +, as one literal three-run relation','A long middle horizontal intersects a slanted upright; the small upper run extends chiefly to the right. Both source candidates remain, with ne primary.','other',False,False,'retained','05_following_si',[1355,1000,1394,1036],['C026-R12'],source_groups=['C026-G04'])
row('D14','replacement over les Sigma connexes',r'\deleted{les $\Sigma_\alpha^{\alpha,0}$ connexes}, \inserted{$X$ connexe, \deleted{et}}',r'\struck{\ill{}} si \struck{les $\Sigma^{\alpha,0}$ connexes}',r'raised X connexe, deleted et; deleted les Sigma_alpha^(alpha,0) connexes; bent guide and lower strike','X connexe, is legible above the long crossed clause. The raised et is locally crossed. The lower clause contains a low alpha under its Sigma as well as the raised alpha/comma/ring. A pale bent guide and the heavier lower cancellation are separate visible runs.','readable ink left as \\ill{}',True,True,crop='06_corrected_connexe',bbox=[600,1068,1140,1174],source_groups=['C026-G05','C026-S08'],H_parent_scope='complete corrected clause including H’s struck-ill placeholder and its omitted replacement; no second H count for the local lower alpha',qualification='C wording/state retained; C difference records explicit guide/cancellation geometry.')
row('D15','cancelled word after on conclut',r'\deleted{\unsure{aussitôt}}',r'\struck{aussitôt}',r'\deleted{\unsure{aussitôt|aussitot}}','The au opening and tall final letter strokes survive the cancellation. The circumflex allocation cannot be settled through the crossing, so both complete accent states remain.','other',False,False,'retained','07_aussitot',[1462,1054,1644,1115],['C026-R04'])
row('D16','entire left marginal diagram',r'\margin{\diagram{...}}',r'\marginal{diagramme \struck{\ill{}} : un segment, $\Sigma^-\supset E\subset\Sigma^+$}; \drawing{...}',r'complete literal oblique two-point diagram, diagramme, cancelled B/E/Sigma, E_alpha legend and one detached point','The whole rotated crop supplies both filled endpoints, their plain connecting segment, the word diagramme, the upper crossed character, the complete lower legend and a small point below the segment. H describes this one diagram instead of reproducing it.','drawing or diagram',False,True,crop='08_oblique_diagram',bbox=[45,956,248,1365],source_groups=['C026-G06'],H_parent_scope='one whole diagram description replacement; all independently variable details remain in child rows',classification_note='H’s orientation/descriptive captions and note syntax are editorial apparatus, not invented manuscript prose.')
row('D17','diagram upper crossed character',r'\deleted{\unsure{E|\Sigma|B}}',r'\struck{\ill{}}',r'\deleted{B} | \deleted{E} | \deleted{\Sigma}','The dark character has a left upright and two right returning lobes, with several crossing diagonals. B is the strongest local reading; E and Sigma survive under the overmark.','misread symbol or index',True,False,'retained','08_oblique_diagram',[105,1170,151,1224],['C026-R05'],H_count_parent='D16',raw_diff_H=True,source_groups=['C026-G06'],candidate_states=[{'complete_reading':r'\deleted{'+x+'}','hand':'his hand','role':'cancelled diagram label','attachment':'above the segment'} for x in ['B','E',r'\Sigma']])
row('D18','diagram E low attachment',r'E_{\unsure{\alpha|{}}}',r'E',r'E_\alpha','The low right attachment contains a small closed loop and a returning right tail beneath the E foot. The alpha reading is selected; its low position is retained.','other',True,False,'resolved','08_oblique_diagram',[143,1208,193,1260],['C026-R06'],H_count_parent='D16',raw_diff_H=True,source_groups=['C026-G06'],confidence='medium')
row('D19','small point just below diagram segment',r'no separate point',r'no separate point in the description','one detached point, with character/role/hand/surface origin unestablished','A small isolated dark point has white separation from the segment. It is preserved once without treating it as punctuation or a label index.','omission',True,False,crop='08_oblique_diagram',bbox=[120,1244,135,1260],H_count_parent='D16',raw_diff_H=True,source_groups=['C026-G06'],hand='undetermined hand',shape_confidence='high')
row('D20','parenthesis: after et, before Sigma',r'et $\Sigma^{\alpha,0}$',r'et \uncertain{si} $\Sigma^{\alpha,0}$',r'et $\Sigma^{\alpha,0}$','The gap between et and the Sigma contains no second word. The separate words after Sigma begin ne peut.','text not on the page',False,True,crop='09_parenthetic_prose',bbox=[281,1360,536,1423],confidence='high')
row('D21','parenthesis: after Sigma, before à la fois',r'ne peut être',r'une partie',r'ne peut \unsure{être|etre}','The low ne is followed by a p with long descender and the reduced peut continuation. The next word has the tall tr sequence; its accent is left qualified. The crop clips the lower end of the p descender, disclosed in the image audit.','misread word',True,True,crop='09_parenthetic_prose',bbox=[555,1338,893,1430],candidate_states=[{'complete_reading':'ne peut '+x,'hand':'his hand','role':'complete prose phrase','attachment':'after Sigma, before à/: la fois'} for x in ['être','etre']])
row('D22','parenthesis: mark before la fois',r'à',r'à',r'\unsure{à|:}','The mark consists of two separated small strokes/points one above the other. à remains primary; colon-shaped allocation remains an alternative.','other',True,False,crop='09_parenthetic_prose',bbox=[902,1344,931,1375],candidate_states=[{'complete_reading':'à','hand':'his hand','role':'primary word reading','attachment':'before la fois'},{'complete_reading':':','hand':'his hand','role':'alternative two-point reading','attachment':'same sign'}])
row('D23','parenthesis: first open/closed adjective',r'ouvert',r'ouverte',r'ouvert','The reduced word ends in an upturned terminal t run; no further e loop follows it before et.','misread word',False,True,crop='09_parenthetic_prose',bbox=[1155,1335,1323,1369],confidence='medium')
row('D24','parenthesis: second open/closed adjective',r'fermé',r'fermée',r'fermé','After the tall f, the low continuation ends in one accented e, with no second final e.','misread word',False,True,crop='09_parenthetic_prose',bbox=[1396,1313,1594,1428],confidence='medium')
row('D25','final car clause within parenthesis',r'car $\Sigma^{...,0}$, est un ouvert $\ne\varnothing$ et $\ne X$)',r'...fermée $\neq\emptyset$ et $\neq X$) ... \uncertain{car} $\Sigma^{\alpha,0}$ est un \uncertain{ouvert} \ill{}',r'car $\Sigma^{...,0}$, est un ouvert $\ne\varnothing$ et $\ne X$)','The car clause continues below the preceding phrase and rises to the final two conditions and closing parenthesis at the right. H moves car to a separate suspended fragment and places the conditions before it. All written content is retained in the page order.','insertion or placement',False,True,crop='10_parenthetic_end',bbox=[275,1400,1510,1545],H_parent_scope='one integrated ordering difference; H’s final ill placeholder is mapped to this already accounted ending, without a second invented manuscript word')
row('D26','Sigma superscript in final car clause',r'\unsure{-,0|\alpha,0|-\alpha,0}',r'\alpha,0',r'\unsure{-,0|\alpha,0|-\alpha,0}','The first high stroke is nearly horizontal with a small return. A clear comma and small ring follow it. The minus primary remains qualified with the two original alternatives.','misread symbol or index',False,True,'retained','10_parenthetic_end',[451,1471,580,1527],['C026-R07'],source_groups=['C026-S14'],qualification='H alpha,0 remains an alternative; qualified primary difference only.')
row('D27','low comma after final car Sigma',r'\Sigma^{...,0},',r'\Sigma^{\alpha,0}',r'\Sigma^{...,0},','A long low curved comma follows the upper ring, separate from the internal superscript comma.','omission',False,True,crop='10_parenthetic_end',bbox=[557,1485,580,1526],confidence='high')
row('D28','traces below un in final car clause',r'no separate marks',r'no separate marks','one short dark slash and three faint points, all role/hand/surface origin unresolved','The enlarged line contains a short oblique mark and a few separated smaller gray points below un. They are drawn without supplying a word or operation.','omission',True,True,crop='10_parenthetic_end',bbox=[731,1520,755,1537],source_groups=['C026-M02'],confidence='medium',hand='undetermined hand')
row('D29','lower paragraph heading',r'décompositions binaires',r'dispositions binaires',r'décompositions binaires','The initial dé is followed by a separate curved c and a long compressed om run before the descending p; the ending positions and plural s remain visible.','misread word',False,True,crop='11_lower_heading',bbox=[970,1530,1658,1608],confidence='high')
row('D30','second binary pair opening delimiter',r'\unsure{(|[}',r'\{',r'\unsure{[|(}','The high short horizontal entry and nearly upright left side support a rounded bracket primary, with an opening parenthesis retained. There is no visible waist at midheight.','misread symbol or index',True,True,'retained','12_pairs_and_guides',[313,1645,342,1696],['C026-R13'],source_groups=['C026-G08'],qualification='C candidates retained in reversed order. H brace does not have a supported waist in the inspected shape.')
row('D31','cancelled distinctes after pairs',r'\deleted{\unsure{distinctes}}',r'\struck{distinctes}',r'\deleted{distinctes}','Surviving initial d/i strokes, the tall t sequence and terminal es are recoverable through the oblique crossings. The deletion is certain; the word is selected with medium confidence.','other',True,False,'resolved','12_pairs_and_guides',[507,1627,706,1688],['C026-R08'],source_groups=['C026-G08'])
row('D32','de X after the pairs',r'\inserted{de $X$,}',r'de $X$,',r'\inserted{de $X$,} with complete bent guide','The words and comma lie below the pair line; a guide begins low left, bends up across the gap and continues toward the deleted word.','insertion or placement',True,True,crop='12_pairs_and_guides',bbox=[225,1684,600,1752],source_groups=['C026-G08'],qualification='C inserted wording retained; its explicit guide geometry is added.')
row('D33','underlined non adjective',r'non \unsure{panachées|penchées|parallèles}',r'\emph{non parallèles}',r'non \unsure{panachées|penchées|parallèles}','The long descending p is followed by a small loop, a reduced middle and one high late shoulder with smaller following rise. The complete three word candidates remain; panachées is primary.','misread word',False,True,'retained','13_non_adjective',[1180,1620,1633,1704],['C026-R09'],source_groups=['C026-G07'],qualification='H parallèles survives as an alternative; no conclusive lexical correction is claimed.')
row('D34','two points below underlined term',r'no separate marks',r'no separate marks','two small detached points below the right end of the underline','The two dark points are separately visible below the rule and below the word. No attachment to the word or punctuation role is established.','omission',True,True,crop='13_non_adjective',bbox=[1580,1679,1592,1697],source_groups=['C026-G07'],hand='undetermined hand',shape_confidence='high')
row('D35','inserted distinctness qualification',r'si \inserted{elles sont \uline{distinctes}, et si} on peut trouver',r'\add{si elles sont \emph{distinctes}, et} si on peut trouver',r'si \inserted{elles sont \uline{distinctes}, et si} on peut trouver, with complete guide','The first si is on the lower main baseline. Above on peut trouver stand elles sont distinctes, et si; distinctes has its own underline. The long guide turns down immediately before on and ends after the raised final si.','insertion or placement',True,True,crop='12_pairs_and_guides',bbox=[280,1716,939,1858],source_groups=['C026-G09'],qualification='C word/state allocation retained, with guide geometry added; H gives different si insertion boundaries.')
row('D36','reduced on before peut trouver',r'on',r'on','on | three reduced separate traces without established lexical reading','Only three short pale/dark runs make up this group. The on reading is primary, but the exact letter allocation remains qualified.','other',True,False,crop='12_pairs_and_guides',bbox=[384,1824,460,1844],source_groups=['C026-G09a'],candidate_states=g['C026-G09a']['candidate_states'])
row('D37','phrase before the final inclusions',r'on a alors',r'on a donc',r'on a alors','After on a, the word begins with a low loop and tall l, followed by the reduced ors ending.','misread word',False,True,bbox=[302,2081,588,2138],confidence='high',evidence_view='half_b')
row('D38','first lower inclusion relation',r'\unsure{\deleted{\cap}\subset|\subset}',r'\subset',r'\deleted{\cap}\subset | \subset | \in, one literal overdrawn group','The open upper/lower curve is crossed at its lower left by an extra prong that turns through a small inner loop. The whole old/live state remains qualified; a membership-shaped reading is also retained.','deletion state (struck given live or live given struck)',True,True,'retained','14_first_lower_relation',[748,2100,797,2146],['C026-R14'],source_groups=['C026-G10'],qualification='H subset survives as an alternative. C’s sequential glyphs are replaced by one shared literal cluster; no chronology is established.')
row('D39','cancelled nonemptiness after Sigma2 minus',r'\deleted{\unsure{\ne\varnothing}}',r'\note{après ... un « \neq\emptyset » biffé}',r'\deleted{\ne\varnothing}','The first dark cluster retains two horizontal levels and a diagonal; the second retains a loop crossed by a long slash. The readable pair is selected, while the overmark is drawn separately.','other',True,False,'resolved','14_first_lower_relation',[899,2093,987,2150],['C026-R10'],source_groups=['C026-G11'],qualification='H’s integrated note already supplies this cancellation and reading.')
row('D40','second explanatory abbreviation',r'\unsure{i.e.|ie}',r'i.e.',r'\unsure{i.e|i.e.|ie}','The i stem and its upper mark are separate; a small intermediate mark follows it. The e has a long terminal run, without an independently separated final stop. A joined terminal-stop reading remains possible.','misread word',True,True,'retained','15_second_ie',[1007,2187,1080,2220],['C026-R11'],qualification='H i.e. remains an alternative; the primary loses only the final point.',candidate_states=[{'complete_reading':x,'hand':'his hand','role':'complete explanatory abbreviation','attachment':'before second equality'} for x in ['i.e','i.e.','ie']])
row('D41','bottom defining label',r'\overset{\mathrm{def}}{=}',r'\overset{\text{déf}}{=}',r'\overset{\mathrm{déf}}{=} | def with independent raised point over e, above equals','A small dark upright/oval mark is visibly raised above the e position. The accent reading is primary; an independent point interpretation remains. The point is retained once in either state.','other',True,False,crop='16_def',bbox=[610,2250,653,2312],source_groups=['C026-G12'],candidate_states=g['C026-G12']['candidate_states'],qualification='H has the same primary déf reading; qualifier difference alone is not an H count.')
row('D42','small slash below first final intersection',r'no separate mark',r'no separate mark','one short gray slash below the first intersection sign in the final row','A narrow gray oblique run is visible below the cap. It is drawn once with role, attachment, hand and surface origin unresolved.','omission',True,True,crop='16_def',bbox=[749,2314,761,2330],source_groups=['C026-M04'],hand='undetermined hand',shape_confidence='medium')
row('D43','first raised ring and its seven later local recurrences',r'\unsure{0|\circ|o} at the first insertion occurrence; 0 at recurrences',r'0',r'\unsure{0|\circ|o}','The first inserted third-Sigma ring is small and open/rounded at the alpha-comma level. The later seven rings retain their individually inspected local 0/circle/o uncertainty. The first-occurrence printing convention marks only S05.','other',False,False,'retained','04_inserted_formula',[1017,882,1040,905],['C026-R15'],source_groups=['C026-S05','C026-S08','C026-S09','C026-S10','C026-S11','C026-S12','C026-S13','C026-S14'],candidate_states=[{'complete_reading':x,'hand':'his hand','role':'raised-ring glyph reading','attachment':'first occurrence in the complete third inserted Sigma; complete later glyph states are separately mapped'} for x in ['0',r'\circ','o']])
row('D44','complete E_alpha glyph in the oblique legend',r'E_{\unsure{\alpha|{}}}',r'E',r'E_\alpha with detached top arm | E_\alpha with independent upper run','The E has a separated short upper run, lower stem/foot and middle arm. The low loop/tail shares the foot and is retained as alpha. The upper-run role is a separate question from the resolved original subscript doubt.','drawing or diagram',False,False,crop='08_oblique_diagram',bbox=[143,1208,193,1260],source_groups=['C026-E01'],candidate_states=g['C026-E01']['candidate_states'],H_count_parent='D16',raw_diff_H=True,C_count_parent='D18',raw_diff_C=True,qualification='D18 resolves C’s original E-index row. This additional top-arm qualification remains separate in scope; no second physical E correction count is proposed.')

# Every actual source-table row keeps its source position, compound scope, and statuses.
source_rows=[];inside=False
for lineno,line in enumerate(source.splitlines(),1):
    if line=='## Doubtful readings':inside=True;continue
    if inside and line.startswith('## '):break
    if inside and line.startswith('| 26 |'):
        n=len(source_rows)+1
        fields=[x.strip() for x in line.split('|')[1:-1]]
        source_rows.append({'id':f'C026-R{n:02d}','source_file':'packets/026/C_doubts.txt','source_section':'Doubtful readings','source_table_row':n,'source_line':lineno,'source_exact':line,'source_fields':fields})
scope={
1:('opening family alphabet after membership',['family index'],['retained']),
2:('inserted equation and following si, including all four dark predecessor/index places',['second inserted Sigma low alpha','third inserted Sigma low alpha','third inserted Sigma upper predecessor/trace','following-si Sigma low alpha'],['retained','retained','retained','retained']),
3:('whole cancelled item after connexes',['cancelled Sigma_alpha versus les'],['resolved']),
4:('whole cancelled word after on conclut',['aussitôt including accent'],['retained']),
5:('whole cancelled upper diagram glyph',['B/E/Sigma candidate and cancellation'],['retained']),
6:('complete low E attachment in diagram',['E_alpha versus E without a subscript'],['resolved']),
7:('complete raised pair in final car clause',['minus,0 / alpha,0 / minus-alpha,0'],['retained']),
8:('whole cancelled distinctes after both pairs',['distinctes'],['resolved']),
9:('whole underlined non adjective',['non panachées / non penchées / non parallèles'],['retained']),
10:('both cancelled signs after first lower Sigma2 minus',['deleted ne varnothing'],['resolved']),
11:('complete second explanatory abbreviation, including both possible stops',['i.e / i.e. / ie'],['retained']),
12:('one relation between E and varnothing in following si clause',['ne / plus'],['retained']),
13:('one opener of the second binary pair',['[ / ('],['retained']),
14:('whole shared first lower relation and old/live state',['deleted cap then subset / subset / membership-shaped reading'],['retained']),
15:('first inserted third-Sigma ring and all later independently inspected alpha-comma-ring recurrences',['S05','S08','S09','S10','S11','S12','S13','S14'],['retained']*8)
}
for rr in source_rows:
    n=rr['source_table_row']; sc,parts,statuses=scope[n]
    rr.update(complete_scope=sc,local_parts=[{'part':p,'status':s} for p,s in zip(parts,statuses)],status='resolved' if all(s=='resolved' for s in statuses) else 'retained',difference_ids=[d['id'] for d in diff if rr['id'] in d['source_rows']],count_source_row_once=True)

# Ring state and detached-head role remain local, even where the repeated primary is unmarked.
ring_ids=['S05','S08','S09','S10','S11','S12','S13','S14']
ring_occurrences=[]
for sid in ring_ids:
    gg=g['C026-'+sid]
    ring_occurrences.append({'source_group':'C026-'+sid,'location':gg['observed_bbox'],'reading':'0','alternatives':[r'\circ','o'],'confidence':'medium','evidence':'small round/open-ring form at raised alpha/comma level, inspected locally','printed_unsure':sid=='S05','first_occurrence_rule':'first candidate 0 printed at later occurrences','source_row':'C026-R15','hand':'his hand','role':'raised glyph shape; numeric/circle/letter allocation unresolved','attachment':'same raised pair at this individual Sigma'})
source_rows[14]['local_parts']=ring_occurrences

head_occurrences=[]
for gg in sm['groups']:
    if not gg['id'].startswith('C026-S'):continue
    sid=gg['id'].split('-')[-1]
    # Keep whole state alternatives, dropping the bare core duplicated before head-role alternatives.
    candidates=gg['candidate_states']
    if gg.get('head_connection')=='detached':
        qualified=[x for x in candidates if ' with short upper head/retrace' in x['complete_reading'] or ' with independent short upper run' in x['complete_reading'] or ' with short head/retrace' in x['complete_reading']]
        if qualified:candidates=qualified
    if sid in ring_ids:
        expanded=[]
        for st in candidates:
            rr=st['complete_reading']
            # Whole printed annotations may include the editorial ring macro; expand it locally.
            rr=rr.replace(r'\unsure{0|\circ|o}','0')
            for ring in ['0',r'\circ','o']:
                tmp=dict(st)
                tmp['complete_reading']=rr.replace(',0',','+ring)
                tmp['ring_candidate']=ring
                expanded.append(tmp)
        candidates=expanded
    fully_expanded=[]
    for st in candidates:
        for whole in expand_unsure(st['complete_reading']):
            copy=dict(st);copy['complete_reading']=whole
            hand_parts=['his hand for the live glyph, its indices and signs']
            if 'independent upper dark trace' in whole:hand_parts.append('undetermined hand for the independent upper dark trace')
            if 'independent short upper run' in whole:hand_parts.append('undetermined hand for the independent short upper run')
            copy['hand']='; '.join(hand_parts)
            fully_expanded.append(copy)
    candidates=fully_expanded
    gg['candidate_states']=candidates
    head_occurrences.append({'source_group':gg['id'],'location':gg['observed_bbox'],'connection':gg.get('head_connection'),'printed_head_qualifier':sid=='S01','candidate_states':candidates,'evidence_view':gg['evidence_view']})
    # Head-body placement is a local drawing difference where the head is detached.
    if gg.get('head_connection')=='detached':
        parent={'S01':'D02','S04':'D09a','S05':'D09b','S15':'D16','S16':'D16'}.get(sid)
        ev=gg['evidence_view'];cp=None if ev.startswith('half') else ev
        dd=row('G-'+sid,'Sigma '+sid+': complete detached head/body group','ordinary Sigma glyph; no separately retained upper-run role','ordinary Sigma glyph or diagram description',gg['ownership']+' with two complete head-role candidates','A short upper run is separated by visible white space from the upper body arm. The literal upper run, body, index and raised sign occur once. Existing closure roofs on S09/S10/S11 are separately retained and are not new bar corrections.','drawing or diagram',not bool(parent),not bool(parent),crop=cp,bbox=gg['observed_bbox'],source_groups=[gg['id']],candidate_states=candidates,physical_count_parent=parent,raw_diff_C=True,raw_diff_H=True,qualification='Complete glyph/head-retrace primary versus the same glyph with independent upper run; independent-run hand alone remains undetermined.')
        if sid in ['S15','S16']:
            dd['diff_C']=True;dd['H_count_parent']='D16';dd['physical_count_parent']=None

sm['original_C_comments']=[x for x in C.splitlines() if x.lstrip().startswith('%')]
sm['complete_source_reconstruction_policy']='Each source_exact equals the corresponding reading.tex byte span exactly; nested groups intentionally overlap their owning parent excerpt. No literal path is copied into the final page twice through that metadata overlap.'
sm['C_uncertainty_rows']=source_rows
sm['recurring_ring_occurrences']=ring_occurrences
sm['all_Sigma_occurrences']=head_occurrences
sm['original_reader_comments']=[{'line':i,'text':l} for i,l in enumerate(ROOT.joinpath('reading.tex').read_text().splitlines(),1) if l.lstrip().startswith('%')]
ROOT.joinpath('source_map.json').write_text(json.dumps(sm,ensure_ascii=False,indent=2)+'\n')

# Literal witness source excerpts accompany every condensed reading comparison.
# Full local clauses are retained when a single physical word is embedded in a compound source span.
def between(text,left,right=None):
    a=text.index(left);z=len(text) if right is None else text.index(right,a)
    return text[a:z]
def source_command(text,needle):
    a=text.index(needle);brace=text.index('{',a);depth=1;j=brace+1
    while j<len(text) and depth:
        if text[j]=='{' and text[j-1]!='\\':depth+=1
        elif text[j]=='}' and text[j-1]!='\\':depth-=1
        j+=1
    return text[a:j]
C_top=C.splitlines()[1]
C_diag=between(C,'% margin note written sideways',"(car ")
C_car=between(C,'(car ', '\n\nConsidérons')
C_lower=between(C,'Considérons','\n\\[\n')
C_disjoint_start=C.index('\\[\n',C.index('Considérons'))
C_disjoint=C[C_disjoint_start:C.index('\\]',C_disjoint_start)+2]
C_final=between(C,'on a alors','% archive sheet number:')
H_top=between(H,'Soit ',r'\note{interligne')
H_insert=source_command(H,r'\note{interligne')
H_car=between(H,r'\uncertain{car}',r'\marginal')
H_diag=between(H,r'\marginal','\n\nConsidérons')
H_lower=between(H,'Considérons','\n\\[\n')
H_disjoint_start=H.index('\\[\n',H.index('Considérons'))
H_disjoint=H[H_disjoint_start:H.index('\\]',H_disjoint_start)+2]
H_final=between(H,'on a donc')
def source_anchor(src,excerpt,file):
    a=src.index(excerpt);z=a+len(excerpt)
    return {'file':file,'start_character':a,'end_character_exclusive':z,'start_utf8_byte':len(src[:a].encode()),'end_utf8_byte_exclusive':len(src[:z].encode()),'start_line':src[:a].count('\n')+1,'end_line':src[:z].count('\n')+1,'exact':excerpt,'sha256':hashlib.sha256(excerpt.encode()).hexdigest()}
for dd in diff:
    ident=dd['id'];num=int(ident[1:]) if re.fullmatch(r'D\d+',ident) else None
    ca=C_top;ha=H_top
    if ident.startswith('D09') or ident in ['D08','D43']:ha=H_insert
    if ident in ['D16','D17','D18','D19','D44']:ca=C_diag;ha=H_diag
    if num and 20<=num<=28:ca=C_car;ha=H_top if num<=24 else H[H.index('et \\uncertain{si}'):H.index(r'\marginal')]
    if num and 29<=num<=36:ca=C_lower;ha=H_lower
    if num and 37<=num<=42:ca=C_final;ha=H_final
    if ident.startswith('G-S'):
        sn=int(ident.split('S')[-1])
        if sn in [15,16]:ca=C_diag;ha=H_diag
        elif 9<=sn<=14:ca=C_top if sn==9 else C_car;ha=H_top if sn<14 else H_car
        elif 17<=sn<=22:ca=C_lower;ha=H_lower
        elif sn in [23,24]:ca=C_disjoint;ha=H_disjoint
        elif sn>=25:ca=C_final;ha=H_final
        elif sn in [3,4,5]:ha=H_insert
    dd['C_reading_summary']=dd['C'];dd['H_reading_summary']=dd['H']
    dd['C_anchor']=source_anchor(C,ca,'packets/026/C.tex');dd['H_anchor']=source_anchor(H,ha,'packets/026/H.tex')
    dd['C']=ca;dd['H']=ha
    dd['witness_excerpt_policy']='C/H are literal source excerpts. The *_reading_summary fields retain condensed comparison labels; no ellipsis in a summary is claimed as manuscript ink.'

inventory=[]
def inv(element,kind,pos,words,hand='his hand',**extra):
    inventory.append({'sheet_kind':'text','hand':hand,'element':element,'kind':kind,'position':pos,'first_words_or_objects':words,'transcribed':'yes',**extra})
inv('T01','text','top, opening two lines','Soit X un ens. Une ... binaire de X est un ens de deux parties de X')
inv('U01','text','under opening term','single underline through definition term binaire',source='D01')
inv('F01','display','below opening two lines','(Sigma_alpha^alpha)_{alpha in E-like sign}; (les hémisphères)')
inv('T02','text','top-to-middle main paragraph','dont la réunion est X ... Quand X est un espace topologique')
inv('DEL01','deletion','before aucune','l’intersection')
inv('T03','text','after topologique','on s’intéresse au cas où les hémisphères Sigma_alpha sont fermés')
inv('CROSS01','drawing','initial h of hémisphères','two local crossing/retrace runs; live/cancelled-initial state qualified',source_group='C026-G01')
inv('INS01','insertion','above et plus','de; curved guide',source_group='C026-G02')
inv('T04','text','line beginning le plus souvent','le plus souvent, connexes ... et où E nonempty')
inv('INS02','insertion','above connexes','complete three-Sigma equation with predecessor clusters and bent guide',source_group='C026-G03')
for k,part in [('DEL02','second inserted Sigma low alpha'),('DEL03','third inserted Sigma low alpha'),('DEL04','third inserted Sigma upper old-alpha/independent-trace cluster')]:
    inv(k,'deletion','inside inserted equation',part+'; complete qualified state retained',hand='his hand; independent upper-trace candidate has undetermined hand' if k=='DEL04' else 'his hand')
inv('DEL05','deletion','after connexes','Sigma_alpha, two explicit crossing paths',source_group='C026-S06')
inv('T05','text','following si clause','si les Sigma connexes et E ... emptyset, X est connexe, si')
inv('DEL06','deletion','following-si Sigma','low alpha, cancelled/live state qualified',source_group='C026-S07')
inv('F02','display','within following si prose','literal ne/plus relation',source_group='C026-G04')
inv('INS03','insertion','above crossed les Sigma connexes','X connexe,; complete pale bent guide',source_group='C026-G05')
inv('DEL07','deletion','end of raised replacement','et, crossed locally',source_group='C026-G05')
inv('DEL08','deletion','under replacement','les Sigma_alpha^(alpha,0) connexes, heavy lower strike',source_group='C026-G05')
inv('T06','text','before first closure formula','on conclut ... que')
inv('DEL09','deletion','after on conclut','aussitôt/aussitot')
inv('F03','display','first closure assertion and parenthetic equalities','closure Sigma alpha0 cap E nonempty; closure equality with setminus')
inv('MARGIN01','margin note','left, rising obliquely','diagramme',source_group='C026-G06')
inv('DIAG01','diagram','left margin beside closure assertion','two filled vertices, plain segment, whole legend Sigma^- superset E_alpha subset Sigma^+',source_group='C026-G06')
inv('C026-E01','drawing','within oblique legend','complete E, shared foot/alpha loop and detached upper run',hand='his hand; independent upper-run candidate alone has undetermined hand',source_group='C026-E01',candidate_states=g['C026-E01']['candidate_states'])
inv('DEL10','deletion','above oblique segment','B/E/Sigma, crossed',source_group='C026-G06')
inv('MARK01','drawing','below oblique segment','small detached point',hand='undetermined hand',source_group='C026-G06')
inv('T07','text','end of first parenthesis','et Sigma ne peut être/etre à/: la fois ouvert et fermé car Sigma, est un ouvert nonempty and not X')
inv('MARK02','drawing','below un in final car clause','one short slash and three faint points',hand='undetermined hand',source_group='C026-M02')
inv('T08','text','lower paragraph heading','Considérons deux décompositions binaires')
inv('F04','display','binary pair line','both signed pairs, qualified [/( opener and firm right brace',source_group='C026-G08')
inv('DEL11','deletion','after second pair','distinctes, explicit oblique crossing runs',source_group='C026-G08')
inv('INS04','insertion','below binary pairs','de X, with bent guide',source_group='C026-G08')
inv('T09','text','lower main line','on dit qu’elles sont non panachées/penchées/parallèles')
inv('U02','text','under non adjective','single rising underline',source_group='C026-G07')
inv('MARK03','drawing','below right end of underline','two detached points',hand='undetermined hand',source_group='C026-G07')
inv('INS05','insertion','above on peut trouver','elles sont distinctes, et si with long bent guide',source_group='C026-G09')
inv('U03','text','under raised distinctes','single underline',source_group='C026-G09')
inv('ON01','text','before peut trouver','on / three reduced traces',hand='his hand for on; undetermined hand for nonlexical-traces candidate',source_group='C026-G09a')
inv('T10','text','after qualification','si ... on peut trouver Sigma1+ dans l’une, Sigma2+ dans l’autre, tels que')
inv('F05','display','below tels que','Sigma1+ cap Sigma2+ empty; (d’où E1 cap E2 empty)')
inv('T11','text','above final inclusion rows','on a alors')
inv('F06','display','bottom three rows','two inclusions and explanatory equalities; defining Sigma12 equation and final nonemptiness')
inv('DEL12','deletion','first lower relation','possible old cap in a complete literal cap/subset/membership-shaped state',source_group='C026-G10')
inv('DEL13','deletion','after first lower Sigma2-','ne varnothing',source_group='C026-G11')
inv('LABEL01','text','above final equals','déf / def with independent raised point',hand='his hand; point hand undetermined in independent-point candidate',source_group='C026-G12')
inv('MARK04','drawing','below first final cap','short gray slash',hand='undetermined hand',source_group='C026-M04')
inv('ARCHIVE','text','bottom-left corner','25; recorded only in archive-number comment',hand='undetermined hand',provenance='archive numeral is visually legible; no named-writer attribution established')
# Add individual complete glyph component records, sorted into page order below.
for gg in sm['groups']:
    if gg['id'].startswith('C026-S'):
        inv(gg['id'],'drawing',str(gg['observed_bbox']),gg['ownership'],source_group=gg['id'],hand='his hand; independent upper-run candidates alone keep undetermined hand',components=[x.get('literal_source') for x in gg.get('components',[])],candidate_states=gg['candidate_states'])

def ysort(item):
    sg=item.get('source_group')
    if sg in g:return g[sg]['observed_bbox'][1]
    ys={'T01':120,'U01':175,'F01':290,'T02':350,'DEL01':350,'T03':700,'T04':960,'T05':1010,'T06':1100,'DEL09':1060,'F03':1175,'MARGIN01':956,'DIAG01':1150,'DEL10':1170,'MARK01':1244,'T07':1320,'T08':1530,'T09':1630,'T10':1750,'F05':1940,'T11':2090,'F06':2100,'ARCHIVE':2303,'DEL02':915,'DEL03':910,'DEL04':878}
    return ys.get(item['element'],1000)
inventory.sort(key=ysort)

doubts=[]
for d in diff:
    if d.get('C_doubt_status')=='retained' or d.get('candidate_states') or d['id'] in ['D19','D28','D34','D42']:
        candidates=d.get('candidate_states')
        if candidates:
            rs=[x['complete_reading'] for x in candidates]
        else:
            rs=[]
            for x in d['reading'].split(' | '):rs.extend(expand_unsure(x.strip()))
            rs=list(dict.fromkeys(rs))
            candidates=[{'complete_reading':x,'hand':d.get('hand','his hand'),'role':'complete local candidate; qualification described in evidence','attachment':d['location']} for x in rs]
        doubts.append({'id':d['id'],'location':d['location'],'reading':rs[0],'alternatives':rs[1:],'complete_qualified_reading':d['reading'],'confidence':d['confidence'],'reason':d['evidence'],'crop':d['readers_crop'],'source_rows':d['source_rows'],'candidate_states':candidates,'source_groups':d.get('source_groups',[])})

report={'scan':26,'reader':'C','start_utc':'2026-11-21 07:37:18 UTC','end_utc':None,'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
'differences':diff,'doubts':doubts,'C_uncertainty_rows':source_rows,'inventory':inventory,
'notes':{'page_content':'The manuscript defines a binary decomposition using two hemispheres and their equator. It gives connectedness and closure assertions, then introduces the qualified adjective read primarily non panachées for a pair of decompositions, with a disjointness condition and three displayed consequence/definition rows. These are attributed readings of the manuscript.','authors_own_uncertainty':'No explicit à vérifier, sauf erreur, je présume, admis, or question-mark proof qualification is read on this sheet. Its crossed clauses and interlinear changes are retained in place.','title_date_page_counts':'No separate title, date, manuscript page number or written page count is seen. Archive sheet numeral 25 appears at the lower left; scan number is 26.','mathematics_led_reading_decisions':'No formula was repaired or selected by mathematical expectation. The sheet’s i.e. labels are transcribed as its own claimed relationships. No proof, theorem or mathematical correspondence was checked.'},
'notation':[{'location':'opening and all later Sigma occurrences','proposed_LaTeX':'complete literal Sigma groups; head-role qualifier first at S01','evidence':'individual upper head/body connection recorded for all 39 occurrences','source_groups':[x['source_group'] for x in head_occurrences]},
{'location':'inserted third Sigma and seven later rings','proposed_LaTeX':r'first \unsure{0|\circ|o}, then 0','evidence':'each raised ring inspected separately; all later candidates retained in recurring_ring_occurrences'},
{'location':'first and second ens','proposed_LaTeX':'ens.; ens','evidence':'first separate stop visible, second absent'},
{'location':'both explanatory equalities','proposed_LaTeX':r'i.e.; \unsure{i.e|i.e.|ie}','evidence':'first two stops visible; second terminal run leaves final-stop allocation unresolved'},
{'location':'bottom definition','proposed_LaTeX':'literal déf/def-with-independent-point above equals','evidence':'one raised mark above e; candidate-specific hand scope in G12'},
{'location':'all closure expressions','proposed_LaTeX':'literal outer rules in S09/S10/S11','evidence':'existing C/H closure bars retained; they are separately visible above the short Sigma heads'},
{'location':'parenthetic final Sigma','proposed_LaTeX':r'\Sigma^{\unsure{-,0|\alpha,0|-\alpha,0}},','evidence':'nearly horizontal first superscript; one low comma separate from internal raised comma'}],
'check_events':[], 'crops':crops,
'brief_feedback':['The brief heading says v24 while its last named revision section is v22 after scan023; the full 265-line supplied file was read and followed.','The prompt’s generic thirds and repeated-reading workflow is superseded here by the assigned whole/a/b-once and one-crop-per-unresolved-target workflow.','Several small marks have clear shape but unresolved attachment/role/hand. Complete candidate-specific states and source ownership are preserved; mathematical reading alone supplies no proof check.','Manual path and text-node dimensions were reviewed only as source. No rendered alignment or metric validation is claimed.'],
'provenance':{'packet_files_read':['packets/026/C.tex','packets/026/H.tex','packets/026/metadata.json','packets/026/C_doubts.txt','packets/026/C_notes.txt','packets/026/C_inventory.json','packets/026/notation.md'],'brief_read':'out/briefs/brief_v24_scan026.md, complete 265 lines','conventions_read':['source/SP40_CW_81_witnesses/codex/J81-03/PREAMBLE.tex','source/SP40_CW_81_witnesses/codex/J81-03/PROMPT.md'],'image_audit_file':'image_audit.json','crop_plan_file':'crop_plan.json','source_map_file':'source_map.json','view_counts':views['counts'],'failed_unseen_deliveries':views['failed_unseen_deliveries'],'processing_notes':views['processing_notes'],'source_scope':'Only assigned packet, its three images, brief, preamble and supplied notation/prompt were read. No other reader or page image was inspected.','mathematical_computation':'none','image_processing_computation':'PIL crop in listed full-scan bbox, autocontrast cutoff 0; one -50 degree BICUBIC expand rotation for diagram; 2800-pixel-width LANCZOS resize with rounded aspect height. All inputs and resulting sizes in crop_audit.json. No pixel alignment or content-difference calculation performed.','source_only_checks':'Pending final source reconstruction and delimiter audit; no compilation or rendering.'},
'recurring_ring_occurrences':ring_occurrences,'all_Sigma_occurrences':head_occurrences,
'H_collation_policy':{'has':'text','their_page':25,'emph_to_uline':'same emphasis reading where span agrees; no macro-only count','uncertain_markers':'editorial; same primary with different qualifier alone gives no H count','description_parent':'D16 covers H’s one whole diagram-description replacement','integrated_notes':'H’s raised equation and cancelled nonemptiness note are included as witness text','count_flags':'diff_C/diff_H are local proposed flags, with raw flags and parent links preserved for physically shared or whole-placeholder clusters'}}
ROOT.joinpath('report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

audit_lines=[
('1–2','Soit X un ens. Une ... binaire de X est un ens de deux parties de X.','First ens. and second ens retained separately; opening definition noun/initial mark qualified in D01.'),
('3','Opening parenthesized family and les “hémisphères”.','Both alphas on first Sigma; outer alpha in E-like sign; full E alphabet uncertainty retained.'),
('4','dont la réunion est X, et dont deleted l’intersection aucune.','Cancellation and live aucune retained; comma after X visible.'),
('5','n’est contenue dans l’autre — on désigne par E.','No expansion or mathematical repair; long dash retained.'),
('6–7','“équateur”, l’intersection, parenthesis on emptiness; Quand X est un espace.','Quoted words and all parentheses/period retained.'),
('8–9','topologique, on s’intéresse au cas où les hémisphères Sigma_alpha sont fermés, (et de plus,','Accent qualification in s’intéresse; local initial h crossing state; raised de and complete guide.'),
('10','le plus souvent, inserted equation, connexes, deleted Sigma_alpha, et où.','All three inserted Sigmas, their low/upper clusters, E and first ring retained; guide turns before connexes.'),
('11','E nonempty); si les Sigma connexes et E relation emptyset, X est.','Following-si low alpha state and ne/plus relation remain qualified.'),
('12','connexe, si corrected les Sigma connexes, on conclut cancelled aussitôt.','Raised X connexe, crossed et, lower long strike, pale bent guide, final comma all retained.'),
('13','que closure Sigma alpha0 cap E nonempty; car closure equality.','Three outer closure rules and their separate Sigma heads recorded; unbarred final setminus member remains unbarred.'),
('margin','diagramme; filled-endpoint segment; cancelled upper letter; lower signed-Sigma/E_alpha legend.','B/E/Sigma upper reading retained; E_alpha attachment selected; isolated point added with unresolved hand/role.'),
('14','et Sigma alpha0 ne peut être/etre à/: la fois ouvert et fermé.','H si absent; ne peut words recovered; two local accent/sign qualifications; lower descender clipping disclosed.'),
('15','car Sigma raised -,0/alpha,0/-alpha,0, est un ouvert nonempty et not X).','Low comma retained; clause remains inside parenthesis; short slash and three faint points below un retained.'),
('16','Considérons deux décompositions binaires.','Lower decomposition word selected from its own c/om/p strokes.'),
('17','Two signed pairs, crossed distinctes, inserted de X, on dit qu’elles sont non ...','Second opener [/( qualified; distinctes recovered; complete de X guide.'),
('18','si; inserted elles sont distinctes, et si; reduced on peut trouver first signed Sigma dans l’une, second dans.','Actual baseline/insertion si boundaries and underline retained; reduced on keeps complete trace alternative; guide drawn once.'),
('19','l’autre, tels que; disjointness display and parenthesized E1/E2 condition.','Every index, sign, intersection, equality, empty set and closing parenthesis retained.'),
('20','on a alors; first inclusion, crossed nonemptiness, first i.e. equality.','Alors from ink; complete overdrawn relation states; cancelled pair selected; first i.e. both points.'),
('21','Second inclusion and second explanatory equality.','Second label i.e/i.e./ie retains terminal-point uncertainty.'),
('22','Sigma12, defining label above equals, intersection containing E1 union E2, final nonemptiness.','Déf versus def plus independent point qualified; bottom slash retained independently. Archive 25 comment only.')]
md=['# Independent reading — scan 026, reader C','','Start: **2026-11-21 07:37:18 UTC**, recorded before the packet was read.','',
'The manuscript defines a binary decomposition using two hemispheres and an equator. It records connectedness and closure assertions, then a condition on two decompositions and the displayed inclusions/equalities below it. These are manuscript-attributed readings. No mathematical proof or correspondence was checked.','',
'## Line audit','', '| Physical line/region | Complete content checked | Reading decision |','| --- | --- | --- |']
for a,b,c in audit_lines:md.append('| '+a+' | '+b.replace('|','/')+' | '+c.replace('|','/')+' |')
md+=['','## Original C uncertainty rows','', 'There are **15 actual rows** in the supplied “Doubtful readings” section. Notation and spelling rows are excluded. The four local parts of R02 and eight individually inspected ring occurrences of R15 retain their original row identities.','', '| Source identity | Complete original scope | Disposition | Local decisions |','| --- | --- | --- | --- |']
for rr in source_rows:
    md.append('| '+rr['id']+' | '+rr['complete_scope'].replace('|','/')+' | '+rr['status']+' | '+', '.join(rr['difference_ids'] or ['recurrence map in report'])+' |')
md+=['','## Complete remaining candidates','', 'The source map supplies the complete glyph/state groups with their original comments, native units, fixed origins, baselines and exact source excerpts. Candidate-specific hand, role and attachment are also retained there; later recurring symbols print only the primary under the first-occurrence rule.','']
for d in doubts:
    if d['id'].startswith('G-'):continue
    md.append('### '+d['id']+' — '+d['location']+'\n')
    md.append('Reading: `'+d['complete_qualified_reading']+'`. '+d['reason']+'\n')
    if d.get('candidate_states'):
        for st in d['candidate_states']:
            md.append('- `'+st['complete_reading']+'` — hand: '+st['hand']+'; role: '+st['role']+'; attachment: '+st['attachment']+'.')
        md.append('')
md+=['','## Recurring glyphs and complete state scope','',
'All **39 Sigma occurrences**, including the two oblique diagram labels, have an individual source map record. Detached head/run candidates keep the entire glyph, its indices and raised marks together. The glyph/body hand is his hand; only the independent-upper-run candidate has undetermined hand for that run. The existing outer closure rules on S09–S11 are separate from their short heads and remain present.','',
'The third inserted Sigma keeps four complete predecessor/trace states: lower deleted alpha with upper deleted alpha; lower live alpha with upper deleted alpha; lower deleted alpha with an independent upper trace; lower live alpha with an independent upper trace. Each also retains the raised ring’s 0/circle/o candidates and local head-role qualification. The two other dark low-alpha loci have separate cancelled/live alternatives.','',
'The raised rings occur at S05, S08, S09, S10, S11, S12, S13 and S14. Each retains 0, circle and o locally. The first printed qualifier is at S05. S14 additionally retains the complete minus,0 / alpha,0 / minus-alpha,0 superscript states; none supplies an expected formula.','',
'## Viewing and source audit','',
'Successful inspections: **1 whole page + 1 half a + 1 half b + 18 distinct close crops = 21**. Each was displayed once. One mistyped-path attempt for crop02 delivered no image; the existing correct crop was then displayed once. No decided target was reopened. The complete structured audit records that failed unseen attempt.','',
'The parenthetic prose crop clips the low continuation of the peut p and fois f descenders. The deciding bodies and the complete à/: mark remain present. This boundary limitation is retained; no replacement crop was made.','',
'Crop boxes use original full-scan coordinates. The diagram crop alone was rotated by −50 degrees before enlargement. The corresponding diagram placement is a manual 50-degree rotation. Exact image-processing transforms and output sizes are in crop_audit.json. The lower half origin is bottom-anchored at y = 2370 − 1265 = 1105; no image alignment computation was performed.','',
'No OCR, text recognition, external research, another reader directory, another page image, compilation, rendering, package installation, or mathematical check was used. The drawings are manual source approximations; no rendered or metric validation is claimed.','',
'## Abbreviations and written slips','',
'The text retains ens. and ens without expansion; their likely expansion is ensemble. It retains the two separately read i.e. forms and the qualified defining label. The opening Sigma has both a low and high alpha. The second pair keeps its [/( opener and right brace. The following-si clause contains no supplied sont. The final car Sigma is followed by its visible low comma.','',
'## Author’s own qualification and sheet metadata','',
'No explicit proof-warning phrase or manuscript question mark is recovered. The corrections and interlinear material are fully retained. There is no separate title, date, manuscript page number or page-count statement. The lower-left archive number is 25 and is recorded only as a comment.']
ROOT.joinpath('reading.md').write_text('\n'.join(md)+'\n')
print('Wrote report with',len(diff),'local difference/qualification records,',len(inventory),'inventory entries and',len(source_rows),'actual C uncertainty rows.')
