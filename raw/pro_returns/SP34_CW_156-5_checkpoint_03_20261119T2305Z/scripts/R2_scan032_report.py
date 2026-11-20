from pathlib import Path
from datetime import datetime,timezone
import json,re
root=Path('/workspace/scratch/4770596940a0');base=root/'out/readers/R2'
D=[]
def add(id,place,C,H,reading,ink,confidence,kind,crop,against_C,against_H,marked_in_H=False):
 D.append(dict(id=id,place=place,C=C,H=H,reading=reading,ink=ink,confidence=confidence,kind=kind,crop=crop,against_C=against_C,against_H=against_H,marked_in_H=marked_in_H))
add('D01','opening F before set difference',r'\unsure{F|\mathcal F}','F',r'\unsure{F|\mathcal F}','Straight upright and two arms, with a substantial return curve at left. Ordinary F remains preferred, but the extra loop leaves the alphabet distinction uncertain.',.68,'C_doubt_retained',['initial_F','top'],False,True)
add('D02','cancelled opening Reste',r'\deleted{\unsure{Reste}}',r'\struck{Reste}',r'\deleted{Reste}','Large initial R, low middle strokes and tall t remain above the horizontal cancellation.',.92,'C_doubt_resolved',['reste'],True,False)
add('D03','raised mark after strate, before de F',r'\inserted{\unsure{$G$|$\in$}}',r'\add{de $G$}',r'\inserted{$G$}','Curved G body with an inward bar and downturned right terminal. It touches the descending end of réunion above. No separate de precedes the raised letter; the diagonal stroke at right is its placement leader.',.84,'C_doubt_resolved;H_added_word',['raised_G','top'],True,True)
add('D04','deleted On after Soit A cette strate de F',r'\deleted{\unsure{On}}',r'\struck{On}',r'\deleted{On}','Looped O with long entry and connected low n is crossed by a separate horizontal line.',.94,'C_doubt_resolved',['deleted_On_top'],True,False)
add('D05','left of corollary, first word',r'\unsure{Ultra}','Ultra','Ultra','After rotation the long U, tall l/t and final short ra movement can be followed.',.94,'C_doubt_resolved',['ultra_rot'],True,False)
add('D06','corollary article',r'\unsure{Le|La}','La','Le','Large L followed by an open small e with a horizontal exit; no closed a bowl. Retain the grammatical mismatch after replacement subdivision.',.97,'C_doubt_resolved;C_H_word',['cor_article'],True,True)
add('D07','cancelled a), inserted un plus grand ...',r'\unsure{élémt|élément|élt}','élément',r'\unsure{élémt|élément|élt}','Small opening e/l, medial sweep and terminal t intersect the large cross. Exact contraction remains unsettled.',.65,'C_doubt_retained;abbreviation',['a_insert_rot'],False,True)
add('D08','starred gloss, after au =',r'\unsure{parmi|pour}','pour','parmi','Tall p, low a/r movement, two m humps and a final short dotted/raised i are visible in the rotated crop.',.89,'C_doubt_resolved;C_H_word',['star_rot'],True,True)
add('D09','long oblique note, deleted item before b)c)d)',r'\deleted{\unsure{a)}}','omitted',r'\deleted{\unsure{a)}}','Dark overstruck oval/angle and closing curved remnant before clear b), c), d); a) remains plausible but not securely recoverable.',.52,'C_doubt_retained;H_omission',['margin1_detail'],False,True)
add('D10','long oblique note, conjunction before impliquées',r'\unsure{et}',r'\uncertain{et équivalentes à a), lesquelles}',r'\unsure{et}','Two joined strokes are heavily retraced at the line start; a short e/t reading remains uncertain.',.57,'C_doubt_retained',['margin1_detail'],False,True,True)
add('D11','long oblique note, underlined word',r'\uline{\unsure{impliquées}}',r'\uncertain{équivalentes à a)...}',r'\uline{impliquées}','Initial i, long p/l, q descender, u and accented ending can be followed independently of the curved crossing stroke. A separate straight underline lies beneath the word.',.91,'C_doubt_resolved;H_wording',['margin1_detail'],True,True,True)
add('D12','long oblique note, after par a)',r'\unsure{lesquelles|laquelle}',r'\uncertain{lesquelles}','lesquelles','Initial les, q descender, paired tall l loops and short plural ending are visible after rotation.',.88,'C_doubt_resolved',['margin2_detail'],True,True,True)
add('D13','long oblique note, verb before la subdivision',r'\unsure{caractérisent|caractérise}',r'conditions \ill{}',r'\unsure{caractérisent|caractérise}','The carac-/téri- stem is visible, but its ending is crowded by body text. Plural versus singular ending remains unresolved; it is longer and differently formed than a simple conditions here.',.62,'C_doubt_retained;H_wording',['margin2_detail','margin_end_context'],False,True,True)
add('D14','long oblique note, word after construite and crossed terminal mark',r'\unsure{précédemment}',r'construite${}^{\#}$, no following word',r'\unsure{précédemment|précédemment\textsuperscript{\#}}','pré- and a long contracted middle run precede a small double-upright crossed terminal. Prefer a retraced final t belonging to précédemment; a distinct hash-like call cannot be excluded. It is not silently dropped.',.57,'C_doubt_revised;H_omission;terminal_mark',['margin2_detail','margin_terminal_mark'],True,True)
add('D15','long oblique note, after trois',r'\unsure{cond.}',r'\ill{}',r'\unsure{cond.}','Short co-/n-like group with tall final stroke and tiny point; overlap prevents a secure exact abbreviation.',.63,'C_doubt_retained;H_partial_reading',['margin3_detail','margin_end_context'],False,True,True)
add('D16','long oblique note, before d’impliquer a)',r'\unsure{loin}',r'\ill{}',r'\unsure{loin}','The final clause crosses the canonical-map arrow and upright body text. Some tall/low traces fit loin, but I cannot isolate every letter with confidence.',.48,'C_doubt_retained;H_partial_reading',['long_margin_full_rot','margin_end_context'],False,True,True)
add('D17','b), after application',r'\unsure{can.}',r'\uncertain{canonique}','can.','Distinct c, a/n movement and a separate dot; no written -onique follows.',.95,'C_doubt_resolved;abbreviation',['b_can_full'],True,True,True)
add('D18','NB, abbreviation before surj.',r'\unsure{tjrs|tojrs}','toujours',r'\unsure{tjrs|tojrs}','Tight t, possible small intervening o-like loop, long j descender and short rs. Retain both short spellings without expanding to toujours.',.66,'C_doubt_retained;abbreviation',['NB_abbrev','NB'],False,True)
add('D19','under Dém, alleged first cancelled On',r'\deleted{\unsure{On}}','none','no separate cancelled On','One long O entry rises across the heading underline; there is one O/n word below, not a second independent struck word. No cancellation stroke crosses that word.',.95,'C_doubt_rejected;deletion_state',['dem_on'],True,False)
add('D20','under Dém, live On',r'\unsure{On}','On','On','Single looped O plus dark retraced n. Compare the clearly cancelled On at the top: here the independent cancellation bar is absent.',.96,'C_doubt_resolved',['dem_on','deleted_On_top'],True,False)
add('D21','proof introduction, after prouver',r'\unsure{p. ex}','omitted','p. ex','Long p stem and separate point, followed by e curve and crossed x.',.96,'C_doubt_resolved;H_omission',['pex'],True,True)
add('D22','deleted second Dém before d⇒b',r'\deleted{\uline{\unsure{Dém}}}',r'\struck{Dém.}',r'\deleted{\uline{Dém}}','D outline, é and terminal m survive heavy cancellation; separate underline remains. No final punctuation dot is visible to its right.',.89,'C_doubt_resolved;underline;H_punctuation',['bottom_dem'],True,True)
add('D23','bottom, older word under inclusion',r'\deleted{\unsure{identité}}','identité live',r'\deleted{\unsure{identité}}','Older t stem and final accent-like remnant protrude through the darker new word; identité remains an uncertain older reading, not the live word.',.62,'C_doubt_retained;H_revision_state',['inclusion'],False,True)
add('D24','bottom, live word after l’',r'\unsure{inclusion}','identité','inclusion','Darker sequence has i/n, tall looped l, u and s/i/o/n ending; it overlays older strokes including the t. The visual decision preceded the local mathematical check.',.90,'C_doubt_resolved;H_wording',['inclusion'],True,True)
add('D25','bottom, small inserted abbreviation over trivial',r'\unsure{can.}','car','can.','Open c, a loop, low n ending and separate point. The final letter is not an r shoulder.',.94,'C_doubt_resolved;H_word',['can_arrow'],True,True)
add('D26','opening live clause after struck Reste','reste à voir que une strate','Reste : voir qu’une strate','reste à voir que une strate','Live r is small; the following small mark has a rounded lower body plus accent, consistent with à. que and une are separate written groups with no apostrophe.',.92,'H_case_punctuation_elision',['reste'],False,True)
add('D27','first upper case, exclusion','A∉G′','A∉G','A∉G′','Distinct short elevated prime immediately after the G.',.98,'H_missing_prime;C_note_review',['primes'],False,True)
add('D28','same case, set difference','F\\G′⊂F′','F\\G⊂F′','F\\G′⊂F′','Second independent elevated prime after G before the subset; subsequent F also has its prime. The unexpected G′ is preserved.',.98,'H_missing_prime;C_note_review',['primes'],False,True)
add('D29','upper first-case difference, small lower hook under backslash','omitted','omitted','small downward-left curved hook/arrow-like mark, drawn in TikZ below the difference sign','Separate curved stroke descends left and meets a short angular return. It is distinct from the thick set-difference slash. Its function is uncertain; no letter interpretation supplied.',.91,'omitted_graphic;uncertain_function',['prime_line_lower_mark','primes'],True,True)
add('D30','end of upper argument','et on gagne encore','et on a gagné encore','et on gagne encore','After on, the next glyph begins the g descender of gagne; no intervening a. Terminal word has no é accent.',.93,'H_added_word_and_tense',['end_gagne'],False,True)
add('D31','Corollaire heading',r'\uline{Corollaire}',r'\textbf{Corollaire}',r'\uline{Corollaire}','A single independent baseline rule runs under the heading.',.98,'H_underline_state',['corollary'],False,True)
add('D32','corollary, insertion before des propriétés',r'\inserted{chacune} des propriétés',r'\add{des} propriétés',r'\inserted{chacune} des propriétés','chacune is written above with a curved placement leader landing before des. des itself remains on the body line.',.94,'H_missing_word;insertion_destination',['chacune','cor_article'],False,True)
add('D33','cancelled a), relative verb','qui induit G′','qui induise G′','qui induit G′','Terminal tall t with horizontal exit after indui; no se group.',.94,'H_wording',['a_induit'],False,True)
add('D34','cancelled a), maximal',r'\deleted{\uline{maximal}}',r'\struck{maximal}',r'\deleted{\uline{maximal}}','Heavy strike crosses maximal and a separate fine underline remains below it.',.95,'H_missing_underline',['a_insert_rot'],False,True)
add('D35','cancelled a), abbreviation l’ens','l’ens','l’ens.','l’ens','No separate point between final s sweep and the next line des subdivisions.',.86,'H_added_punctuation',['a','a_dans'],False,True)
add('D36','starred gloss, second line','cela revient','il revient','cela revient','First group has c/e and tall l followed by a; the rotated word is substantially longer than il.',.94,'H_wording',['star_rot'],False,True)
add('D37','starred gloss, third line','au $=$','au même','au $=$','Two literal parallel strokes, not written letters of même.',.99,'H_expanded_shorthand',['star_rot'],False,True)
add('D38','starred gloss, last line',r"d'une $=$ $F$","d'un même F",r"d'une $=$ $F$",'Written une ends with a low e/sweep; another literal pair of parallel strokes precedes F.',.96,'H_expanded_shorthand;gender',['star_rot'],False,True)
add('D39','long oblique note, par a) after impliquées','par a)','à a) in uncertain clause','par a)','Small p stem and joined ar follow the underlined word, with a) on the next portion of the line.',.82,'H_wording',['margin1_detail','margin2_detail'],False,True,True)
add('D40','long oblique note, its overall curved crossing stroke','unmarked live margin note','note says cut by curved stroke, text remains live','whole note probably cancelled; full text retained inside deleted, function uncertainty recorded','Long curve crosses several successive words and lines, has no arrowhead or clear insertion endpoint, and does not stay outside the text as a boundary. Cancellation is preferred; grouping stroke remains possible.',.70,'revision_state;uncertain_function',['long_margin_rot','long_margin_full_rot'],True,True)
add('D41','long oblique note, after Mais','ces trois','c) très','ces trois','The small first group and following t-r-o-i-s form a running prose phrase; these are not the body c) label and the word très.',.80,'H_wording',['margin2_detail','margin3_detail'],False,True)
add('D42','long oblique note, parenthesized series and final verb','(b,c,d) sont ... d’impliquer a)','(b,c,d) followed by ill.','(b,c,d) sont ... d’impliquer a)','Parenthesized letters and short sont traces at the left; d’impliquer a) is visible at the far right across the mapping line. The uncertain intervening loin remains D16.',.75,'H_partial_reading',['long_margin_full_rot','margin_end_context'],False,True,True)
add('D43','NB, underlined injectivité',r"l'\uline{injectivité}",'l’injectivité without underline',r"l'\uline{injectivité}",'Straight separate underline lies beneath the full word.',.98,'H_missing_underline',['NB'],False,True)
add('D44','NB, final word','prouver ici','prouver','prouver ici','Final short i-c-i sequence with two upright/dot marks is visible at right end of the third line.',.93,'H_omitted_word',['NB'],False,True)
add('D45','NB, left boundary rule','omitted','omitted','left vertical rule with small bottom hook, rendered in TikZ beside full note','Thin continuous near-vertical stroke spans all NB lines, then bends slightly at bottom.',.98,'omitted_drawing',['NB'],True,True)
add('D46','c), old cancelled sentence',r"\deleted{Les strates ouvertes de $F'$ qui ne sont}",r"two \struck{\ill{}} fragments placed within/after new sentence",r"\deleted{Les strates ouvertes de $F'$ qui ne sont}",'Old line is continuous beneath the replacement: Les strates ouvertes de F′ qui ne sont, crossed by long horizontal strokes.',.94,'H_deletion_extent_and_reading',['c_deletion'],False,True,True)
add('D47','c), raised replacement sentence','live sentence without insertion macro','live sentence with ouverte omitted/illegible deletions',r"\inserted{$\forall A\in F\setminus G$, $A^\circ$ est une strate ouverte de $F'$}",'New ∀ line is above the cancelled old line; ouverte is legible at its right. de F′ continues below at left. Treat the full replacement as an insertion.',.94,'insertion_state;H_omitted_word',['c_d','c_deletion'],True,True,True)
add('D48','proof heading Dém',r'\uline{Dém}',r'\textbf{Dém.}',r'\uline{Dém}','Heading has one separate underline and no final dot after m.',.96,'H_underline_and_punctuation',['dem_on'],False,True)
add('D49','bottom, parenthesized trivial',r'\deleted{(trivial)}','omitted',r'\deleted{(trivial)}','Parentheses and trivial survive beneath the thin strike; replacement can. and map are above.',.92,'H_missing_deletion',['proof','can_arrow'],False,True)
add('D50','bottom inserted map',r'F\setminus G\hookrightarrow F',r'F\smallsetminus G\subset F',r'F\setminus G\hookrightarrow F','After G, a left hook joins a horizontal shaft and distinct right arrowhead before F. It is an inclusion map arrow, not just a subset relation.',.95,'H_math_arrow',['can_arrow'],False,True)
add('D51','cancelled a), angular mark immediately below qui','omitted','omitted','E-like angular mark and detached upper tick, reproduced as a small TikZ graphic below qui','Left stem, lower arm, separate middle arm, faint upper arm and short upright above/right are separate from the q descender. Lexical value E′/F′ versus correction mark is unresolved; no letter is imposed.',.94,'omitted_graphic;uncertain_reading',['a_unknown'],True,True)
add('D52','cancelled union, second lower index; C wording note','B≤F','B≤F','B≤F','Both lower letters in B∈F and B≤F have an upright plus two arms. The lower glyph is F, not A, despite the displayed union being for A.',.98,'C_note_review;math_index',['union'],False,False)
add('D53','cancelled a), worked-over beginning of dans','dans','dans','dans; no independently recoverable older word added','The first letter is strongly retraced and has a long lower loop. Current dans is readable, but I cannot securely separate a former p or older word from the d formation.',.76,'revision_review_no_text_change',['a_dans'],False,False)

statuses={1:'retained',2:'resolved',3:'resolved',4:'resolved',5:'resolved',6:'resolved',7:'retained',8:'resolved',9:'retained',10:'retained',11:'resolved',12:'resolved',13:'retained',14:'revised and retained',15:'retained',16:'retained',17:'resolved',18:'retained',19:'rejected: no separate cancelled word',20:'resolved',21:'resolved',22:'resolved',23:'retained',24:'resolved',25:'resolved'}
Crows=[dict(occurrence=i,source_locus=D[i-1]['place'],source_C=D[i-1]['C'],status=statuses[i],difference_id=D[i-1]['id'],reading=D[i-1]['reading'],confidence=D[i-1]['confidence']) for i in range(1,26)]
I=[]
def inv(id,kind,position,first,state,crop):I.append(dict(id=id,kind=kind,position=position,first_words_or_objects=first,state=state,crop=crop))
inv('I01','handwritten','top centre','31','manuscript page number',['whole'])
inv('I02','text','opening line','Si A∈F\\G, A∩B est réunion de strates de F','live continuation',['top'])
inv('I03','deletion','second line start','Reste','crossed word',['reste'])
inv('I04','text','second and third lines','reste à voir que une strate ... de F est réunion de strates de F′. Soit A cette strate de F','live body',['top','reste'])
inv('I05','insertion','between strate and de F','G','raised letter and placement leader',['raised_G'])
inv('I06','deletion','end of third line','On','crossed word',['deleted_On_top'])
inv('I07','display','upper left','A=union B circle; limits B∈F, B≤F','cancelled formula; left end of strike thickened',['union'])
inv('I08','text','upper first case','Si A∉G′, alors A∈F\\G′⊂F′, et on gagne','live body; primes preserved',['primes','cases'])
inv('I09','drawing','under first-case set-difference slash','small curved downward-left hook/arrow-like mark','uninterpreted graphic, TikZ',['prime_line_lower_mark'])
inv('I10','text','upper second case','Si A∈G, alors (comme G′≼G) A est réunion de strates de G′','live body',['cases'])
inv('I11','text','end of upper paragraph','qui sont des strates de F′, et on gagne encore','live body',['cases','end_gagne'])
inv('I12','margin note','left beside corollary, slanted','Ultra faux','live warning',['ultra_rot'])
inv('I13','text','corollary heading','Corollaire','underlined',['corollary'])
inv('I14','text','corollary first line','Le ... précédente F′ de F est caractérisée par ... des propriétés équivalentes suivantes','live body with revisions',['corollary','cor_article'])
inv('I15','deletion','corollary first line','raffinement','crossed former noun',['cor_article'])
inv('I16','insertion','above raffinement','subdivision','replacement',['cor_article'])
inv('I17','insertion','before des propriétés','chacune','raised text with curved leader',['chacune'])
inv('I18','deletion','central a) block','a) Pour toute subdivision F″ de F qui induit G′ sur G, on a F″≼F′ -- i.e. ...','entire condition crossed by large X',['a'])
inv('I19','deletion','within a), after F′ est','maximal','underlined then crossed',['a_insert_rot'])
inv('I20','insertion','within a), above maximal','un plus grand [élémt|élément|élt]','replacement inside overall cancellation',['a_insert_rot'])
inv('I21','text','within a), ending','pour ≼*, dans l’ens des subdivisions de F qui induisent G′ sur G','inside overall cancellation; raised star call',['a','a_dans'])
inv('I22','drawing','under qui in last long line of a)','E-like angular mark with separate upper tick','unresolved graphic, preserved with qui in TikZ',['a_unknown'])
inv('I23','margin note','left of a), slanted and starred','* ou pour ≪, cela revient au = parmi des subdivisions d’une = F','full gloss; literal equals shorthand',['star_rot'])
inv('I24','margin note','long oblique note, left into body','les conditions [a) deleted] b)c)d) sont équivalentes','probably overall cancelled; state uncertain',['margin1_detail'])
inv('I25','text','same long note, next clause','[et] impliquées par a), lesquelles [caractérisent|caractérise] la subdivision construite','impliquées underlined; overall cancellation preferred',['margin1_detail','margin2_detail'])
inv('I26','text','same long note, after construite','[précédemment; terminal crossed mark uncertain]','terminal t/hash question retained',['margin2_detail','margin_terminal_mark'])
inv('I27','text','same long note, final clause','Mais ces trois [cond.] (b,c,d) sont [loin] d’impliquer a)','full clause retained despite overlaps',['long_margin_full_rot','margin_end_context'])
inv('I28','deletion','across successive lines of long oblique note','long curved crossing stroke','probable cancellation; grouping-stroke alternative recorded',['long_margin_rot','long_margin_full_rot'])
inv('I29','text','b) introduction','b) L’application can. associée à F′≼F','live body',['b','b_can_full'])
inv('I30','display','below b) introduction','φ:F′→F','live mapping; overlapped by oblique-note writing',['b','margin_end_context'])
inv('I31','text','before b) bijection','induit une bijection','live body',['b','margin_end_context'])
inv('I32','display','b) bijection','F′\\G′ →~ F\\G','single rightward arrow with elevated tilde',['b'])
inv('I33','margin note','right of b)','NB. c’est [tjrs|tojrs] surj. donc c’est l’injectivité qu’il faut prouver ici','injectivité underlined',['NB','NB_abbrev'])
inv('I34','drawing','left of NB','vertical rule with small bottom hook','boundary rule, TikZ',['NB'])
inv('I35','deletion','c) lower old line','Les strates ouvertes de F′ qui ne sont','long horizontal cancellation',['c_deletion'])
inv('I36','insertion','c), above old line and continuation below','∀A∈F\\G, A circle est une strate ouverte de F′','full replacement sentence',['c_d','c_deletion'])
inv('I37','text','d)','d) F′⊃F\\G, i.e. ∀A∈F\\G, on a A∈F′','live body',['c_d'])
inv('I38','text','proof heading','Dém','underlined',['dem_on'])
inv('I39','text','proof introduction','On va prouver p. ex','one live On; no extra deleted On',['dem_on','pex'])
inv('I40','display','proof implication chain','d)⇒b)⇒c)⇒a)⇒d)','four rightward double-shaft arrows, all labels retained',['proof'])
inv('I41','deletion','start of first implication','Dém','underlined and heavily crossed',['bottom_dem'])
inv('I42','text','first implication setup','d)⇒b) Si (F\\G)⊂F′, alors φ|F\\G est l’...','live body',['proof'])
inv('I43','deletion','bottom overwritten word','[identité]','older uncertain word beneath inclusion',['inclusion'])
inv('I44','text','same overwritten locus','inclusion','live darker word',['inclusion'])
inv('I45','deletion','after inclusion','(trivial)','cancelled parenthesis',['can_arrow','proof'])
inv('I46','insertion','above trivial','can. F\\G↪F','small raised words and hooked inclusion arrow',['can_arrow'])
inv('I47','deletion','after inclusion insertion','donc','first donc crossed',['proof'])
inv('I48','text','bottom continuation','donc il reste à prouver','live repetition',['proof'])
inv('I49','display','bottom edge','F\\G=F′\\G′.','live equality with both right-hand primes',['proof'])

recipes=json.loads((base/'crops032.json').read_text())
for c in recipes:
 c['path']=str((root/c['path']).resolve());c['source']=str((root/c['source']).resolve());c['viewed']=True
 c['rotation_degrees']=c.get('rotation',0)
 if 'derived_from' in c:c['derived_from']=str((root/c['derived_from']).resolve())
tex=(base/'scan032.tex').read_text();Ctext=(root/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/pages/J156-5-04_156-5_scan032.tex').read_text()
clean='\n'.join(line.split('%',1)[0] for line in tex.splitlines())
b=0;minimum=0
for i,ch in enumerate(clean):
 if ch not in '{}':continue
 n=0;j=i-1
 while j>=0 and clean[j]=='\\':n+=1;j-=1
 if n%2:continue
 b += 1 if ch=='{' else -1;minimum=min(minimum,b)
assert b==minimum==0
assert clean.count('$')%2==0
assert clean.count('\\[')==clean.count('\\]')==5
for env in ['tikzpicture','scope']:
 assert clean.count('\\begin{'+env+'}')==clean.count('\\end{'+env+'}')
assert len(re.findall(r'\\unsure\{',Ctext))==25
assert len(Crows)==25
for c in recipes:assert Path(c['path']).exists()
ids={c['id'] for c in recipes}
for d in D:
 assert set(d['crop'])<=ids
 assert all(isinstance(d[k],bool) for k in ['against_C','against_H','marked_in_H'])
now=datetime.now(timezone.utc).isoformat()
who='R2; model inherited/not otherwise exposed; effort inherited; run scan032'
checks=[
 dict(statement_id='R2.scan031.least_containing_F_cell_rule',date=now,who=who,type='carried as background without fault found',outcome='Used the least-containing-cell characterization read independently in scan031 to interpret the canonical map φ. Existence of the minimum and the general refinement theorem were not re-proved.'),
 dict(statement_id='R2.scan032.bottom.restriction_is_inclusion',date=now,who=who,type='targeted proof check',outcome='Conditional local check only: assume φ(A) is the least B∈F with A⊆B and d) gives F\\G⊂F′. For A∈F\\G, A is itself in F and in F′. It is an admissible containing F-cell and is contained in every other admissible B, so φ(A)=A. Hence φ restricted to F\\G is the inclusion into F. This does not prove d)⇒b), which still needs the bottom equality. The ink reading inclusion was made before this check.')
]
report=dict(scan='032',manuscript_page='31',reader='R2',effort='inherited',start_utc=(base/'start032.txt').read_text().strip(),end_utc=now,
 sources=dict(C=str(root/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/pages/J156-5-04_156-5_scan032.tex'),H=str(root/'working/H/scan032.tex'),C_doubts=str(root/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/J156-5-04_doubts.md'),C_notes=str(root/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/J156-5-04_notes.md')),
 independence=dict(other_reader_files_read=False,root_decisions_read=False,later_scan_opened=False,OCR_used=False,external_research_used=False),
 images_viewed=[dict(source=str(root/f'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan032{s}.jpg'),role=role,order=i) for i,(s,role) in enumerate([('','whole'),('_a','upper half'),('_b','lower half')],1)],
 crops=recipes,differences=D,C_doubt_resolutions=Crows,
 S_row_decisions=dict(relevant_rows=[],decision='No scan032 row in the supplied sweep3 corrections table; exact scan filter checked.'),
 inventory=I,
 remaining_doubts=[dict(difference_id=d['id'],place=d['place'],reading=d['reading']) for d in D if ('retained' in d['kind'] or 'uncertain_' in d['kind'])],
 notation=[
  'Initial F versus script F remains uncertain; subsequent ordinary F/G/A/B retained as written.',
  'Both first-case G primes are visible and retained despite the following case using unprimed G. The lower union index is B≤F, not normalized to A.',
  'Order relations are transcribed with the established preceq convention; double wedge ≪ remains distinct in the starred gloss.',
  'Literal equals signs in the starred gloss are preserved instead of expanding them to même.',
  'F double-prime in a), single primes in b), elevated tilde over the bijection arrow, A-circle in c), superset in d), and restriction bar after φ were each checked visually.',
  'The two tiny uninterpreted graphics are drawn in TikZ instead of forcing a letter or mathematical interpretation; the NB boundary rule is also retained.',
  'Large X through a) and the long curved marginal cancellation are revision marks, not mathematical arrows. The latter function remains uncertain.'
 ],
 reading_notes=[
  'All body lines, agreed formulas and revisions were read visually, whole then halves, with 40 enlarged/rotated crop recipes.',
  'The upper paragraph concludes the preceding subdivision discussion. The page proposes a corollary with conditions a)–d), but the author marks Ultra faux and crosses a).',
  'The long oblique note says b),c),d) are equivalent and implied by a), and denies the converse; several abbreviated or overlapped words remain doubtful. Its curved stroke is treated as probable cancellation, with grouping still possible.',
  'The NB singles out injectivity. The displayed implication chain is preserved even though a) is crossed and the margin disputes its relation to the other conditions.',
  'The prime discrepancy and the union index prompted closer ink review. Neither was corrected to the form suggested by the argument.',
  'One On appears below the proof heading; its long entry crosses the underline of Dém but is not a second cancelled word.',
  'No proof of the whole corollary, no re-proof of equivalence b/c/d, and no counterexample search was performed. Only the precisely stated local restriction-map check is in check_events.'
 ],
 check_events=checks,
 visual_checks=[
  dict(type='visual_reading',scope='Whole page then both halves, line by line including agreements',outcome='Completed.'),
  dict(type='enlarged_and_rotated_review',scope='All 25 C doubts, every C/H difference, all marginal/slanted/deleted/inserted ink and decisive math symbols',outcome='40 actual crops emitted and viewed; recipes include post-rotation cropping where used.'),
  dict(type='inventory_review',scope='Text, displays, revisions, marginal notes, underlines and otherwise omitted marks',outcome='49 entries; no later page viewed.')
 ],
 syntax_checks=dict(group_braces_balanced=True,dollar_delimiters_even=True,display_pairs=5,tikz_and_scope_environments_balanced=True,all_crop_paths_exist=True,all_C_doubt_occurrences_accounted_for=25,flags_are_booleans=True,crop_cross_references_valid=True,compiled=False),
 flag_semantics='against_C/against_H compare submitted wording, uncertainty candidate set/order, and revision state. Equivalent TeX commands, spacing, and purely equivalent preceq/preccurlyeq or setminus/smallsetminus choices are not differences. marked_in_H means a local explicit uncertainty/illegibility marker, not merely struck text or historical notes.',
 summary=dict(differences_and_review_rows=len(D),C_doubt_occurrences=25,resolved_or_rejected_C_doubts=15,retained_or_revised_C_doubts=10,inventory_entries=len(I),crop_recipes=len(recipes),mathematical_check_events=len(checks),full_tex=str(base/'scan032.tex')))
(base/'scan032.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report['summary'],ensure_ascii=False))
