"""Main reader's crop decisions for scan033; written after all 30 differing crops were inspected."""
from pathlib import Path
import hashlib,json
r=Path(__file__).resolve().parents[1];n=33
p=r/'pages/J156-5-04_156-5_scan033.tex';rec=json.loads((r/'review/scan033_adjudicated.json').read_text())
comp=json.loads((r/'second/J156-5-04_156-5_scan033_comparison.json').read_text())
state=r'\unsure{\deleted{\unsure{\prime|\ast|?}}|\varphi|q}'
phrase=r'\unsure{str.$^{t}$-ouvert|str.t-ouvert|strate ouverte} pour \deleted{$\unsure{F|A|la}$} $F\prime$'
# Apostrophe is the edition's prime convention.
phrase=phrase.replace(r'F\prime',"F'")
oldphrase=r"strate ouverte \deleted{dans \unsure{la}} de $F'$"
edits=[
 {'old':r'\deleted{\unsure{R|P|Or}} 1°)', 'new':r'\deleted{\unsure{R|P|Or}} $\Rightarrow$ 1°)'},
 {'old':r'\deleted{On a} Soit', 'new':r'\deleted{\unsure{On a}} Soit'},
 {'old':r'\unsure{\subset|\in}', 'new':r'\unsure{\subset|\in|\subseteq}'},
 {'old':r'A^{\deleted{\unsure{\prime|\ast|?}}}', 'new':'A^{'+state+'}'},
 {'old':r'A^{\deleted{\unsure{\prime|\ast|?}}\circ(F)}', 'new':'A^{'+state+r'\circ(\unsure{F}}'},
 {'old':oldphrase,'new':phrase},
 {'old':r'est une \uline{'+phrase,'new':r'est un \uline{'+phrase},
 {'old':'Sinon on aurait','new':r'\unsure{Sinon|Si} on aurait'},
 {'old':r'\deleted{Posons}','new':r'\deleted{\unsure{Posons}}'},
 {'old':r'\unsure{\ast|k|+}','new':r'\unsure{\ast|k|+|\leftarrow}','count':2}]
def final(s):
 for e in edits:s=s.replace(e['old'],e['new'])
 return s
observations={
 '033-number':('19:28:17','The numeral has two clear digits, 3 and 2, followed by a dense point. Both readings encode the same ink; keeping the point inside mspage is only a macro-boundary choice.','high',False),
 '033-top_initial':('19:28:17','Two horizontal shaft strokes lead from the overwritten initial to a distinct right-pointing head before 1°). Restore the omitted live implication arrow. The initial remains R/P/Or doubtful: its loop and diagonal are crossed.','high',True),
 '033-top_deleted_A':('19:28:17','The deleted group retains the two oblique legs and crossbar of A, followed by an open membership curve and short middle bar. The heavy crossing cancels that group, not the following parenthesis. Retain A membership without adding a character doubt.','high',False),
 '033-two_start':('19:28:35','The 2, raised round ordinal mark, parenthesis, both primes and open subset sign agree. Textual degree versus math superscript is encoding only; no terminal point appears before Soit.','high',False),
 '033-two_on_a':('19:28:35','The initial O loop is plain, but the broad horizontal cancellation covers the bodies after it. On a remains the preferred two-word reading; restore a doubt because not every cancelled letter can be separated. Omission of the clipped following le in the second excerpt is not an edition change.','low',True),
 '033-two_underlined_formula':('19:28:35','The complete pair has a shared lower bracket with upturned ends. The first subset-shaped relation is retraced heavily, admitting membership or subset-equal. Each A is followed by a compact elevated angular/looped mark: a cancelled prime remains preferred, but a live phi/q-like glyph cannot be excluded, so its state is now explicit. The right edge cuts through the final F exponent; no closing parenthesis can be recovered there, and it is no longer supplied.','low',True),
 '033-two_conclusion':('19:29:12','The relation between A-prime and A has two heavy horizontal bars; their joined left ends match this hand’s retraced equals, not a separate membership middle bar. The d ascender, apostrophe, low ou and final accent support d’où. The following crossed On a/Or remains doubtful. The first excerpt begins slightly earlier than the blind excerpt.','medium',False),
 '033-margin':('19:29:12','The opening has a low v valley and a separate rounded a, followed by the short se group. The long word has the m/p sequence, tall l/f, and an extended -ier tail; there is no final accented-é configuration. The final word has a b ascender and low a/s continuation. Retain va se simplifier, cf plus bas.','high',False),
 '033-jedis_mais':('19:29:12','The cancelled word retains the two tall M strokes, rounded a, dotted i and terminal s curl; the horizontal strike does not erase those discriminating parts. Retain Mais without another doubt.','high',False),
 '033-jedis_et':('19:29:30','The small cancelled group has an e loop and rising t stem with its transverse stroke. The following large Il belongs to the live baseline. Retain et; the extra F-prime and en in the first excerpt are boundary context.','medium',False),
 '033-jedis_insertion':('19:29:30','The interlinear word has two tall f stems and an extended sequence after the dotted i before its final t, favouring suffirait over the shorter suffit. The relation is two successive left angles, clearly much-less. The old closing parenthesis is crossed at the attachment, with cf lemme below; retain the first reading.','medium',False),
 '033-jedis_relation':('19:29:30','The baseline order sign has the established bent upper and separate lower strokes of preceq; the adjoining F remains live. The long thin line above them is the insertion leader. The local cancellation is on the old closing parenthesis, not a strike through the whole F-prime relation.','medium',False),
 '033-jedis_et_bien':('19:29:47','The additional short line lies below the b/i/e/n bodies, supporting the preferred underline. The old deletion interpretation remains an explicit alternative. The leading parenthesis in the second excerpt is adjacent context.','low',False),
 '033-jedis_last_formula':('19:29:47','The cancelled sign has a left upright and rightward bars; its base is entangled with the slash. F/E/membership remain viable, whereas an unambiguous universal quantifier is not visible. The two A terms, primes and subset sign are clear; ce qui has the dotted i tail. Retain the first alternatives.','low',False),
 '033-donc_begin':('19:29:47','The faint intervening words are two small low groups, so on a remains marked doubtful. The A-prime is written over a separate upright/cap structure, supporting the retained deleted F/A residue omitted by the blind reader.','low',False),
 '033-donc_parenthesis':('19:29:56','The old right parenthesis has a distinct crossing stroke; a comma-like descending mark survives beside it. The following q has a deep descender, then a small e and tall looped d: qed, not cqd. The live close and following point remain in the edition.','high',False),
 '033-donc_sinon':('19:29:56','Low connected strokes after Si favour the fuller Sinon, but their compression prevents a secure letter-by-letter separation from Si. Add that alternative, retaining Sinon first. The following word has an extra low u/r sequence before -ait, supporting aurait.','low',True),
 '033-cancel_insert':('19:29:56','The interlinear On suppose b) and i.e. precede a three-part phi and the readable induit sequence. The arrow has a single shaft, right head and tilde above. The broad diagonal cancellations include this insertion; xrightarrow versus overset-longrightarrow changes no ink.','medium',False),
 '033-cancel_underlined':('19:30:12','The opening is compressed str., followed by a slightly raised t and a separate short hyphen; the next word has ouvert without a secure terminal e. A deep p descender and rounded following loops identify pour, not de/dans. The tightly hatched next group is one compact residue, plausibly F/A/la, not securely the words dans la. Replace the first phrase with the blind reading’s preferred structure, preserving explicit alternatives for the short form and residue.','low',True),
 '033-cancel_de':('19:30:12','The small locally crossed word has a looped d ascender and low e return, before the tall t of tel. Its local deletion is distinct from the paragraph’s diagonal cancellation. Retain de.','medium',False),
 '033-cancel_equality':('19:30:12','Every long diagonal ends above this Prouvons line; no one crosses its letters or equality. The first live state remains preferred, with cancellation of the whole argument retained as an explicit alternative. The blind reader’s broad scope is possible but is not forced by the visible stroke endpoints.','low',False),
 '033-bottom_start':('19:30:31','Both arrowheads of the equivalence are visible. The cancelled Posons retains P and round o bodies, but the final connected letters lie under a thick horizontal stroke. Add a doubt to that cancelled word. The support formula, U and comma agree; math wrappers differ only in encoding.','low',True),
 '033-bottom_indices':('19:30:31','Both raised marks repeat a short upright and rightward transverse/diagonal arms. Star remains preferred, but a left-arrow-like form is now admitted alongside k/plus; the same alternatives apply to I and I-prime. The crossed patch between F-prime and G-prime remains separate from the preferred live difference slash.','low',True),
 '033-bottom_ens':('19:30:31','The top stroke is the serif of I itself, with a hooked end; there is no clearly separate arrow above an otherwise complete I. Retain plain I. The next cancelled form is triangular, admitting A/Delta; the following F/P loop remains unresolved.','low',False),
 '033-two_first_relation':('19:30:50','The dense lower return can conceal either a membership middle bar or an extra lower line; subset remains preferred with both alternatives. The compact raised mark has a short top loop/angle and thick downward part, so live phi/q remains a state alternative to the preferred cancelled prime. The shared bracket was checked in the complete formula crop.','low',True),
 '033-jedis_deleted_symbol':('19:30:50','The left stem and two rightward arms are visible before the long diagonal cancellation. Its bottom turn can belong to that cancellation; retain F/membership/E uncertainty. A universal-quantifier shape with two converging upper arms is not established.','low',False),
 '033-donc_formula':('19:30:50','The whole two-line implication confirms both primes, the difference slash and live implication arrow. The earlier faint on a and overwritten F/A under A-prime remain doubtful rather than being silently removed. The blind excerpt additionally includes the next Prouvons clause, already present in the edition.','low',False),
 '033-cancel_block':('19:31:00','The wider crop confirms est un before the abbreviated str.t-ouvert pour wording, and confirms that the local hatched residue is compact. It also shows the insertion leader and all five diagonal cancellation endpoints above the final Prouvons line. Apply the phrase correction while retaining the explicitly doubtful live state of that last line.','low',True),
 '033-bottom_F':('19:31:17','The top horizontal stroke belongs to the I serif, with a turned end rather than a separate vector arrow. The cancelled triangular glyph retains an A/Delta-like apex and crossbar. The looped next capital still permits F/P; no change is supported.','low',False),
 '033-margin-rule':('19:31:17','The long headless bowed stroke separates the marginal words from the body; both codings approximate that geometry. The writing has va se and a long -ifier ending, followed by cf plus bas. Retain the first wording and its integrated TikZ placement; the blind geometry alone supplies no different stroke.','high',False)}
dec=[]
for x in comp:
 if not x['different']:continue
 tm,evidence,confidence,changed=observations[x['box']]
 dec.append({'box':x['box'],'changed':changed,'final':final(x['first']),'evidence':evidence,'confidence':confidence,'crop':f'crops/second_scan033_{x["box"]}.png','viewed_utc':'2026-11-20 '+tm+' UTC'})
updates=[]
for c in rec['changes']:
 z=final(c['final'])
 if z!=c['final']:updates.append({'id':c['id'],'fields':{'final':z,'second_evidence':'See the corresponding scan033 independent-reading adjudication; preferred readings, state alternatives and clipped edge were rechecked on the full formula/phrase crop.'}})
updates.extend([
 {'id':'033-08','fields':{'final':'A^{'+state+'}','second_evidence':'Both blind formula crops admit a live phi/q-like form; cancellation remains preferred but is no longer asserted without an alternative.'}},
 {'id':'033-09','fields':{'C':r'A^{\deleted{\unsure{\prime|\ast|?}}\circ(F)}','H':r'A^{\circ(F)}','final':'A^{'+state+r'\circ(\unsure{F}}','against_C':True,'against_H':True,'kind':'misread symbol or index','confidence':'low','second_evidence':'Right edge clips the final exponent; the first supplied closing parenthesis is removed. Elevated-mark state remains doubtful. Whole formula inspected in second_scan033_033-two_underlined_formula.png.'}},
 {'id':'033-21','fields':{'final':r'\unsure{Sinon|Si}','confidence':'low','second_evidence':'Retain Sinon preferred, but compressed final low strokes admit the blind reader’s Si alternative.'}},
 {'id':'033-25','fields':{'against_C':False,'against_H':False,'certainty_only':False,'review_only':True,'merged_into':'033-27','final':r'\unsure{str.$^{t}$-ouvert|str.t-ouvert|strate ouverte}','second_evidence':'Superseded and counted once within the full underlined-phrase correction033-27.'}},
 {'id':'033-26','fields':{'against_C':False,'against_H':False,'certainty_only':False,'review_only':True,'merged_into':'033-27','final':r'\deleted{$\unsure{F|A|la}$}','second_evidence':'Superseded and counted once within033-27; the supposed words dans la are not securely present.'}},
 {'id':'033-27','fields':{'place':'cancelled b⇒c, article and underlined abbreviated phrase','C':r"est une \uline{strate ouverte \deleted{dans \unsure{la}} de $F'$}",'H':r"est une strate \ill{} de $F'$",'final':r'est un \uline{'+phrase+'}','against_C':True,'against_H':True,'H_marked':True,'confidence':'low','kind':'misread word','evidence':observations['033-cancel_underlined'][1],'crop':'crops/second_scan033_033-cancel_block.png','box':[250,1630,1650,2060],'main_decision':'Blind pass overturns the earlier full-word expansion and preposition. Exact shortened form and hatched residue remain doubtful; the visible pour is retained.','second_evidence':'Narrow underlined crop and whole cancelled block inspected independently; same locus counted once, replacing033-25/26/27 overlap.'}}])
new=[{'id':'033-BL01','place':'opening, arrow before 1°)','C':'(omitted)','H':'(omitted)','final':r'$\Rightarrow$','evidence':observations['033-top_initial'][1],'crop':'crops/second_scan033_033-top_initial.png','box':[240,70,905,155],'confidence':'high','kind':'omission','against_C':True,'against_H':True,'H_marked':False,'certainty_only':False,'consequential':False,'main_decision':'Restored after independent blind reading and main-reader crop inspection.'}]
u=[]
for x in rec['unresolved']:
 if x['place']=='cancelled b⇒c, local word after dans':continue
 if 'cancelled superscript' in x['place']:
  x={**x,'reading':r'\deleted{\unsure{\prime|\ast|?}}','alternatives':[r'\varphi','q'],'reason':'Dense raised glyph may be a cancelled earlier sign or a live looped symbol; both character and deletion state remain open.'}
 if x['place']=='2°), first underlined relation':x={**x,'alternatives':[r'\in',r'\subseteq']}
 if 'I superscript' in x['place'] or 'superscript on I and I′' in x['place']:
  x={**x,'reading':r'\ast','alternatives':['k','+',r'\leftarrow'],'confidence':'low','reason':'Both repeated raised glyphs show an upright and rightward arms; the arrow-like possibility from the blind reading is retained without changing the preferred star.'}
 u.append(x)
u.extend([
 {'place':'2°), cancelled On a before Soit','reading':'On a','alternatives':[],'confidence':'low','reason':'Broad horizontal strike conceals the final letter bodies; the preferred words are not certain.'},
 {'place':'2°), clipped end of right underlined exponent','reading':r'\circ(\unsure{F}','alternatives':[],'confidence':'low','reason':'The original scan ends through the F region; no closing parenthesis is recoverable and none is supplied.'},
 {'place':'cancelled b⇒c, abbreviated underlined phrase','reading':r'str.$^{t}$-ouvert','alternatives':['str.t-ouvert','strate ouverte'],'confidence':'low','reason':'The small form after str. and the separate hyphen favour an abbreviation; a full expansion is not certain.'},
 {'place':'cancelled b⇒c, hatched residue after pour','reading':'F','alternatives':['A','la'],'confidence':'low','reason':'Several crossing lines obscure one compact group; the earlier dans la reconstruction is not supported.'},
 {'place':'Donc, compressed conditional opening','reading':'Sinon','alternatives':['Si'],'confidence':'low','reason':'Additional low strokes favour -non but cannot all be separated.'},
 {'place':'bottom, cancelled Posons','reading':'Posons','alternatives':[],'confidence':'low','reason':'The thick horizontal cancellation obscures the ending; preferred word retained with doubt.'}])
out={'scan':33,'page_before_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'decisions':dec,'edits':edits,'record_updates':updates,'new_changes':new,'unresolved_replace':u,'changed_loci':['033-BL01','033-BL02-cancelled-On-a','033-BL03-upper-formula','033-BL04-abbreviated-phrase','033-BL05-Sinon-certainty','033-BL06-Posons-certainty','033-BL07-index-alternatives'],'notes_append':['The blind pass recovered the live implication arrow before 1°), omitted by both witnesses and the first consolidated reading. The cancelled lower argument reads est un followed by an abbreviated str.t-ouvert-like form and pour; the first expansion to une strate ouverte … de was withdrawn. The abbreviated form and intervening hatched glyph remain doubtful. At the right edge of the upper bracketed pair, the exponent is clipped; a closing parenthesis formerly supplied is no longer transcribed. These are ink decisions, not mathematical repairs.'],'abbreviations_append':[]}
out['hand_habits_append']=[{'habit':'A serif and its hooked end may resemble a vector arrow; dense raised overwritten marks can resemble live phi/q.','evidence':'033 bottom I and the two upper A superscripts; independent crops inspected19:28–19:31UTC.','holds_every_occurrence':False,'witness_effect':'Blind reader proposed vector I and live phi/q. Plain I retained; elevated-mark state kept explicitly open.'}]
out['abbreviations_append']=[{'form':r'str.$^{t}$-ouvert','expansion':'Unresolved shortened adjective, possibly strictement-ouvert; no expansion is substituted in the transcription.'}]
(r/'second/scan033_adjudication_input.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Prepared',len(dec),'crop decisions and',len(edits),'explicit text edits.')
