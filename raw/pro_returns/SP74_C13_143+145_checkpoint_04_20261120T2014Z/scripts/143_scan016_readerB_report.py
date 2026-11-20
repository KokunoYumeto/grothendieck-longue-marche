import json
from pathlib import Path
base=Path('/workspace/scratch/8f839dff4bf0')
root=base/'SP74_C13_143+145_work'
packet=json.loads((base/'reader_packets/143_scan016.json').read_text())
Csrc,Hsrc=packet['witness_C'],packet['witness_H']
finalsrc=(root/'reviews/143_scan016_readerB.tex').read_text()
prefix='crops/143_scan016_readerB_'
boxes={'first_isom_display':[375,138,1662,400],'hom_tors_prose':[840,515,1647,605],'cancelled_comme':[315,635,538,726],'cancelled_les_operations':[294,909,675,1018],'action_diagram':[420,1505,1665,1862],'bitorseur_definition':[650,1935,1665,2061],'final_isom_pair':[545,2154,1280,2357]}
def row(place,C,H,final,ac,ah,kind,ink,confidence='high',crop=None,marked=False,consequential=False):
    assert C=='[no witness]' or C in Csrc,('C not literal',place,C)
    assert H=='[no witness]' or H in Hsrc,('H not literal',place,H)
    return dict(place=place,C=C,H=H,final=final,against_C=ac,against_H=ah,kind=kind,ink=ink,confidence=confidence,crop=prefix+crop+'.png' if crop else 'page',box=boxes.get(crop),marked_in_H=marked,consequential=consequential)
changes=[
row('Opening sentence, future verb','on aura donc','on a donc','on aura donc',False,True,'misread word','After on, the source has an a followed by distinct low u-r-a strokes before donc; it is longer than the single a given by H.'),
row('First Isom, extra groupoid subscript M0688',r'\Pi_{1,\unsure{\mathrm{é}|\phi}}',r'\mathrm{Isom}_{\Pi_1}(j, j\')'.replace("\\'","'"),r'\Pi_{1,\unsure{\mathrm f|\phi}}',True,True,'misread symbol or index','A comma and a separate small glyph follow Pi-one. The glyph has an ascending hook, an upright extending below a short cross/returning loop, and no detached accent over an e-shaped bowl. A cursive f or phi is plausible; the candidate remains explicitly uncertain. H omits the extra material.','low','first_isom_display',False,True),
row('Definition label above first equality',r'\overset{\mathrm{dfn}}=',r'\overset{\mathrm{df}}{=}',r'\overset{\mathrm{dfn}}{=}',False,True,'omission','The d-loop is followed by a tall f stroke and a low n-like returning exit to the right. The small final n is retained.','medium','first_isom_display'),
row('First display, tors abbreviation punctuation',r'\pi_1\text{-tors à droite}',r'\pi_1\text{-tors.\ à droite}',r'\pi_1\text{-tors à droite}',False,True,'text not on the page','The short s ends before a clear gap; the following small strokes belong to à. There is no separate abbreviation point after tors in this subscript.','high','first_isom_display'),
row('Composition sentence, hom punctuation','des hom de',r'des hom.\ de','des hom de',False,True,'text not on the page','Hom ends in the long low exit of m, followed by a gap and de; no detached full stop occurs.','high','hom_tors_prose'),
row('Composition sentence, shortened tors and possible point',r'$\pi_1$-tors à droite.',r'$\pi_1$-torseurs à droite.',r'$\pi_1$-tors\unsure{.} à droite.',True,True,'abbreviation expanded or spelling modernised','Only the t-o-r-s strokes occur, without the eur sequence required by torseurs. A very short low horizontal trace after the s may be an abbreviation point or its terminal exit, so the point is localized as doubtful.','medium','hom_tors_prose'),
row('Cancelled word before On a donc',r'\deleted{\unsure{Comme}}',r'\struck{\ill{}}',r'\deleted{\unsure{Comme}}',False,True,'readable ink left as \\ill{}','An open capital C and an o-loop survive, with low m-like joined traces and a terminal e-like turn beneath the cancellation. Comme remains tentative because the middle strokes coincide with the strike.','low','cancelled_comme',True),
row('Cancelled restart before Comment',r'\deleted{les opérations}',r'\struck{[Les opérations}',r'\deleted{[les opérations}',True,True,'omission','A separate tall opening bracket with upper and lower turns stands before the word les. The following l is a separate smaller upright; les and opérations remain readable beneath the two long cancellation strokes. The bracket is not the initial letter itself.','high','cancelled_les_operations'),
row('Factorisation parenthesis, extension-group letter',r"celle de $\mathcal E'$",r"celle de $\Sigma'$",r"celle de $\unsure{\mathcal E'|\Sigma'}$",False,True,'misread symbol or index','The rounded two-lobed group glyph has a detached prime. It repeats the unresolved E/Sigma form specified by the shared notation table; this page does not name its letter.','low'),
row('Action diagram, upper arrow and stacked labels',r'\arrow[r,"g_{\Pi_1}","\sim"\']'.replace("\\'","'"),r'\xrightarrow{\ g_{\Pi_1}\ }',r'\arrow[r,"{\substack{g_{\Pi_1}\\[-.3ex]\sim}}"]',True,True,'insertion or placement','The arrow has a definite right head. Both the g-sub-Pi-one label and the separate tilde indicating isomorphism stand above the shaft, with the tilde between g and the shaft. C puts the tilde below; H omits it.','high','action_diagram',False,True),
row('Action diagram, lower arrow and stacked labels',r'\arrow[r,"?","\sim"\']'.replace("\\'","'"),r'\overset{?}{\simeq}',r'\arrow[r,"{\substack{?\\[-.3ex]\sim}}"]',True,True,'drawing or diagram','A short horizontal shaft terminates in a right arrowhead. A separate tilde lies above that shaft and the author\'s question mark above the tilde. C moves the tilde below; H gives an isomorphism relation without the head.','high','action_diagram',False,True),
row('Bitorseur definition, marks between B-g and inclusion',r"B_g\subset\mathcal E'",r"\mathcal{B}_g \subset \Sigma'",r"B_g\unsure{:}\subset\unsure{\mathcal E'|\Sigma'}",True,True,'omission','Two small dark spots lie separately to the right of the g subscript and before the inclusion sign, at slightly different heights. They may be a low colon, but their function in the expression is unclear and they could be incidental ink. The candidate keeps only a localized unsure colon. The following group glyph follows the shared E/Sigma uncertainty.','low','bitorseur_definition'),
row('Bitorseur definition, inverse-image abbreviation',r'\text{image inv. de }g',r'\text{image inverse de } g',r'\text{image inv. de }g',False,True,'abbreviation expanded or spelling modernised','After image the source has the compact inv trace and a small terminal point, followed by de. The extra erse strokes are absent.','high','bitorseur_definition'),
row('Bitorseur definition, final connector and group glyph',r"\mathcal E'\mathbin{-}\mathcal G'",r"\Sigma' \to \mathcal{G}'",r"\unsure{\mathcal E'|\Sigma'}\unsure{\mathbin{-}|\longrightarrow}\mathcal G'",False,True,'drawing or diagram','The link is a horizontal shaft with a tiny dark terminal blot. Unlike the clear diagram heads above, this terminal mark does not securely resolve into a directional head; a bare shaft is the first reading and a small-headed arrow remains possible. The source group retains the shared E/Sigma uncertainty.','low','bitorseur_definition',False,True),
row('Sentence introducing the final pair',r"On \unsure{note|voit} que l'on a",r"On note par l'\uncertain{hyp.}","On note que l'on a",False,True,'misread word','The opening verb has a low n, rounded o, tall crossed t and terminal e. It is followed by a q-descender with ue, then a separate l-apostrophe-on and a. There is no par l\'hyp. sequence.'),
row('Opening enclosure before grâce','(grâce','[grâce','(grâce',False,True,'misread symbol or index','The opening stroke is smoothly curved, not a square bracket. The closing mark after the I-expression is visibly a square bracket and remains unchanged.'),
row('Operation parenthesis, extension-group letter',r"de $\mathcal E'$ sur",r"de $\Sigma'$ sur",r"de $\unsure{\mathcal E'|\Sigma'}$ sur",False,True,'misread symbol or index','The rounded two-lobed primed group glyph is retained with the same E/Sigma uncertainty as its other occurrences.','low')
]
Clines=[l.removesuffix(r'\\') for l in Csrc.splitlines() if l.startswith(r"\widetilde X'(g")]
Hlines=[l.strip().removesuffix(r'\\').rstrip() for l in Hsrc.splitlines() if l.strip().startswith(r"\widetilde{\mathfrak{X}}'(g")]
Flines=[l.removesuffix(r'\\') for l in finalsrc.splitlines() if l.startswith(r"\widetilde{\mathfrak X}'(g")]
assert len(Clines)==len(Hlines)==len(Flines)==2
for idx,(c,h,f) in enumerate(zip(Clines,Hlines,Flines)):
    changes.append(row('Final displayed pair, '+('gj' if idx==0 else "gj-prime")+' row, product index',c,h,f,False,True,'misread symbol or index','The pi-one sits below and to the right of its wedge. The g subscript of B is visible; the first one is heavily retraced, with no securely separable cancelled previous character. All primes and argument letters in this row were inspected.','high','final_isom_pair',False,True))
changes.append(row('Bottom-left manuscript page number',r'\mspage{15}','[no witness]',r'\mspage{15}',False,True,'omission','The bottom-left graphite number is 15; both digits are visible. The separate upper-right 8 is also retained.'))
def inv(i,kind,position,objects,hand='his hand'):
    return dict(sheet_kind='text',hand=hand,element=f'E{i:02d}',kind=kind,position=position,first_words_or_objects=objects,transcribed='yes')
report={
'key':'143_scan016','reader':'B','stage':'first','image_views':['original','half1','half2'],'changes':changes,
'decisions':[
 {'id':'M0688','decision':'undecided','reading':r'\unsure{\mathrm f|\phi}','ink':'The extra glyph after Pi-one and a comma has a connected upper hook, upright, and short middle loop/cross. It does not display a separate accent above an e bowl. Cursive f and phi remain possible; H omits the glyph altogether.','crop':prefix+'first_isom_display.png','box':boxes['first_isom_display'],'confidence':'low'},
 {'id':'M0689','decision':'first','reading':'note','ink':'The word has n-o, a clearly tall crossed t, and an e exit. The following words read que l\'on a.','crop':'page','box':None,'confidence':'high'}
],
'inventory':[
 inv(1,'margin note','upper-right corner','8','pencil hand, unassigned'),
 inv(2,'text','first line',"Ceci noté, on aura donc, si j,j-prime in J=Ob Pi-one"),
 inv(3,'display','first displayed line','Isom with Pi-one plus extra doubtful subscript; equals by dfn Isom of the square-bracketed tilde-X-prime objects'),
 inv(4,'display','second displayed line','isomorphic to Isom of right pi-one torsors, with parenthesized j and j-prime'),
 inv(5,'text','two lines below first display','la composition des chemins étant la composition des hom de pi-one-tors à droite.'),
 inv(6,'deletion','before On a donc reconstruit','Comme uncertain'),
 inv(7,'text','reconstruction paragraph, three lines','On a donc reconstruit Pi-one à l\'aide de tilde-X-prime(J) et de l\'opération libre (à droite) de pi-one'),
 inv(8,'insertion','over reconstruit Pi-one, with attachment toward Pi-one','le groupoïde'),
 inv(9,'deletion','beginning of following paragraph','[les opérations'),
 inv(10,'text','question and object-action explanation, four lines','Comment reconstituer l\'opération de G-prime sur Pi-one ? L\'opération sur Ob Pi-one=J n\'est autre que l\'opération donnée'),
 inv(11,'text','end of explanation and diagram introduction','factorisant celle de the primed rounded group; Soit g in G-prime, explicitons'),
 inv(12,'diagram','central two-by-two diagram','Top: Isom_Pi-one(j,j-prime) to Isom(gj,gj-prime), with g_Pi-one above tilde above arrow; two vertical equality marks; lower pi-one Isom pair with question mark above tilde above right arrow'),
 inv(13,'text','below action diagram','Pour ceci, considérons le bitorseur'),
 inv(14,'insertion','above bitorseur','pi-one-'),
 inv(15,'display','bitorseur definition','B-g, possible low colon, inclusion in primed rounded group; image inv. de g par group-to-G-prime connector'),
 inv(16,'text','line before final pair','On note que l\'on a (grâce à l\'op. de the rounded primed group sur tilde-X-prime(I)]'),
 inv(17,'display','final pair, first row','tilde-X-prime(gj) isomorphic to tilde-X-prime(j) wedge_pi-one B-g; subscript g heavily retraced'),
 inv(18,'display','final pair, second row','tilde-X-prime(gj-prime) isomorphic to tilde-X-prime(j-prime) wedge_pi-one B-g'),
 inv(19,'margin note','bottom-left corner','15','pencil hand, unassigned')
],
'remaining_doubts':[
 {'place':'M0688, first groupoid subscript','reading':r'\Pi_{1,\unsure{\mathrm f|\phi}}','alternatives':r'\mathrm f; \phi; C also proposed accented é','confidence':'low','reason':'The connected hook/upright/middle loop admits f or phi; an accented e is less compatible with the absence of a detached accent. No new notation is defined on this sheet to settle it.'},
 {'place':'Composition prose, possible point after tors','reading':r'tors\unsure{.}','alternatives':'tors with an abbreviation point; tors ending in a short detached exit stroke','confidence':'medium','reason':'A short low horizontal trace follows the s. It is not securely separable as punctuation rather than a terminal letter stroke.'},
 {'place':'Cancelled word before On a donc','reading':r'\deleted{\unsure{Comme}}','alternatives':'Comme; another word with C/o opening and similar low middle strokes','confidence':'low','reason':'The first capital and o-loop survive, but the cancellation intersects most middle letters.'},
 {'place':'Two spots after B-g in the definition','reading':r'B_g\unsure{:}\subset','alternatives':'low colon; incidental ink spots','confidence':'low','reason':'Two separate dark marks occur at different heights, but their placement is lower than the inclusion sign and their grammatical/mathematical function is not established.'},
 {'place':'Definition connector from rounded group-prime to G-prime','reading':r'\unsure{\mathbin{-}|\longrightarrow}','alternatives':'bare horizontal shaft; arrow with a very small terminal head','confidence':'low','reason':'The endpoint is a tiny dark blot without a securely identifiable head outline.'},
 {'place':'Rounded extension/action-group glyph, four occurrences','reading':r"\unsure{\mathcal E'|\Sigma'}",'alternatives':r"\mathcal E' or \Sigma'",'confidence':'low','reason':'The shared uncertain letter convention is retained; this page does not identify its alphabet explicitly.'}
],
'certainty_resolutions':[
 {'place':'M0689','C':r'\unsure{note|voit}','final':'note','ink':'The low n-o followed by a tall crossed t and final e supports note, before the readable que l\'on a.'}
],
'notation':[
 {'form':r'\Pi_1','meaning':'groupoid whose objects are J','evidence':'The opening line explicitly writes J=Ob Pi-one. The tiny extra suffix in the first Isom subscript remains uncertain.'},
 {'form':r"\widetilde{\mathfrak X}'[j]\,,\ \widetilde{\mathfrak X}'(j)",'meaning':'two differently bracketed objects in the first identification','evidence':'The first Isom uses square brackets around j and j-prime; the right-torsor Isom below uses parentheses. The mathfrak X encoding follows the supplied notation table, without claiming a mathematical correction.'},
 {'form':r'\pi_1\text{-tors à droite}','meaning':'right pi-one torsors','evidence':'Written as the subscript of the second Isom and abbreviated again in the composition prose.'},
 {'form':r'B_g','meaning':'the pi-one-bitorsor described as the inverse image of g','evidence':'The prose declares g in G-prime and then defines B-g by image inv. de g. The first final B-g subscript is retraced, but g remains its readable current character.'},
 {'form':r'\mathbin{\wedge}_{\pi_1}','meaning':'contracted product notation in the final pair','evidence':'Both pi-one labels lie below their wedge signs.'},
 {'form':r"\unsure{\mathcal E'|\Sigma'}",'meaning':'extension/action-group glyph appearing in the factorisation, bitorsor definition and operation parenthesis','evidence':'The repeated rounded two-lobed form remains undecided under the current notation table.'},
 {'form':r'\operatorname{Isom}_{\pi_1}','meaning':'the lower-row Isom notation in the diagram','evidence':'The two lower subscripts are retained as pi-one; the right one is thickly retraced, while the source text anchors the right pi-one torsor interpretation. No separate overwritten index can be read.'}
],
'abbreviations':[
 {'form':'Ob','expansion':'objets'}, {'form':'Isom','expansion':'isomorphismes'}, {'form':'dfn','expansion':'definition'}, {'form':'hom','expansion':'homomorphismes'}, {'form':'tors','expansion':'torseurs'}, {'form':'inv.','expansion':'inverse'}, {'form':'op.','expansion':'opération'}
],
'hand_log':[
 {'habit':'The capital I in Isom can have a short top serif detached from the vertical stroke.','places':'First two Isom operators and the four Isom operators of the action diagram.','scope':'All six operators on scan016 inspected. This observation concerns I, not an automatic identification of other detached strokes elsewhere.','misreadings':'No extra overbar is supplied over these capital-I forms.'},
 {'habit':'The tilde indicating an isomorphism can lie above an arrow shaft, below another stacked label.','places':'Both horizontal arrows in the action diagram.','scope':'Both connectors inspected in a single diagram crop.','misreadings':'C puts both tildes below the arrows. H omits the upper one and loses the lower arrowhead.'},
 {'habit':'An opening bracket may survive immediately before a cancelled word block.','places':'Cancelled [les opérations.','scope':'This single locus inspected in a tight crop.','misreadings':'C omits the bracket; H preserves it but capitalizes the following les.'},
 {'habit':'Short words and abbreviation endings may have long flat exits, distinct from additional complete letters.','places':'aura, hom, tors, inv., note.','scope':'All cited occurrences inspected; the possible point after prose tors remains doubtful.','misreadings':'H shortens aura, expands tors and inv., and inserts punctuation after hom and the first display\'s tors.'},
 {'habit':'A g subscript may be heavily retraced, producing multiple loops and crossings without a separate deleted character.','places':'First B-g in the final pair; compared with the definition B-g and the second final B-g.','scope':'All three B-g occurrences inspected, with the final pair cropped.','misreadings':'No separately cancelled previous letter was inferred from the retracing.'},
 {'habit':'The rounded extension-group glyph retains two open lobes but has no self-identifying alphabet here.','places':'All four primed occurrences on this page.','scope':'All inspected; shared E/Sigma uncertainty retained.','misreadings':'C versus H alphabet disagreement is not treated as settled.'}
],
'notes':[
 {'id':'143_scan016-N1','text':'The source begins J=Ob Pi-one and identifies morphisms in the groupoid with isomorphisms of two square-bracketed objects and then with isomorphisms of right pi-one torsors. It states that path composition is composition of the torsor hom maps. These are source statements, not independently proved claims in this reading pass. The extra groupoid suffix in the first Isom is unresolved.'},
 {'id':'143_scan016-N2','text':'The author says the groupoid has thus been reconstructed from tilde-X-prime(J) and its free right pi-one action, then asks how to reconstruct the G-prime action. The source question is Comment reconstituer l\'opération de G-prime sur Pi-one ? The question mark above the lower diagram arrow is the author\'s own mark and is preserved separately from transcription uncertainty.'},
 {'id':'143_scan016-N3','text':'The page defines B-g as the inverse image of g, with pi-one- inserted before bitorseur. The source has image inv., not an expanded inverse. The two spots after B-g and the tip of the subsequent group connector remain visually doubtful; no expected mathematical construction was used to supply punctuation or a head.'},
 {'id':'143_scan016-N4','text':'The author next writes On note que l\'on a and an asymmetrically enclosed parenthesis starting (grâce and ending with a square bracket. Inside it the argument is explicitly I in tilde-X-prime(I), although the adjacent formulas concern j and j-prime in J. I is retained rather than corrected; any expected J belongs to interpretation, not transcription. The final pair asserts identifications with contracted products by B-g.'},
 {'id':'143_scan016-N5','text':'The page carries 8 at the upper right and 15 at the bottom left. Both pencil marks are included without deciding their authorship or numbering system. The mathfrak X encoding follows the common notation convention and is not classified as a consequential mathematical correction.'}
],
'check_events':[
 {'statement_id':'143_scan016-N1','type':'carried as background without fault found','outcome':'The Isom identifications and composition assertion were collated visually. No independent re-proof or computation was performed.'},
 {'statement_id':'143_scan016-N2','type':'carried as background without fault found','outcome':'The groupoid-reconstruction statement and action question were transcribed, not verified mathematically.'},
 {'statement_id':'143_scan016-N3','type':'used and rechecked in this run','outcome':'The explicit local declaration g in G-prime and the image-inverse wording were used only as a notation anchor: all three B subscripts were compared with the visible g. This is a source-notation check, not proof of any bitorsor property.'},
 {'statement_id':'143_scan016-N4','type':'carried as background without fault found','outcome':'The literal I and both final equations were read from the ink. No action law, torsor identity, or contracted-product assertion was independently established.'}
],
'unresolved_for_main':[
 {'place':'M0688, extra suffix in first Isom subscript','crop':prefix+'first_isom_display.png','question':'The glyph is f/phi-like, with a connected upper hook and upright. Candidate retains unsure{f|phi}; please compare with established notation elsewhere.'},
 {'place':'Possible abbreviation point after prose tors','crop':prefix+'hom_tors_prose.png','question':'Short low terminal stroke may be a point or the s exit.'},
 {'place':'Cancelled Comme','crop':prefix+'cancelled_comme.png','question':'Initial C/o survive; middle letters remain obscured.'},
 {'place':'Possible colon and final connector in bitorsor definition','crop':prefix+'bitorseur_definition.png','question':'Two low dark spots after B-g are kept as unsure colon; E-prime/G-prime link is unsure dash or arrow. Both doubts are localized.'},
 {'place':'Shared rounded group glyph','crop':prefix+'bitorseur_definition.png','question':'No new decisive alphabet evidence; E/Sigma uncertainty retained.'}
],
'raw_difference_disposition':'All packet differences were inspected, together with every agreement, against the original once and each native half once. Seven unique tight crops resolve or document the remaining loci. All C/H excerpts in the comparison rows were programmatically verified to be literal substrings of the assigned packet, apart from the explicit [no witness] marker. The apparent comma differences after Ob arise from H\'s TeX thin-space command and are not source punctuation. Equivalent scan/page/note wrappers, insertion annotations, aligned/array choices, spacing, and the established mathfrak-X alphabet encoding were excluded as markup-only differences. No standalone font-only X correction is claimed; confidence/consequence flags on the equation and diagram rows concern the material index/arrow differences. Decisions contain exactly the two supplied MARKS ids. New doubts are listed only in remaining_doubts, with no invented MARKS ids. No other page, web research, OCR or TeX compilation was used.'
}
path=root/'reviews/143_scan016_readerB.json'
path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
required=['key','reader','stage','image_views','changes','decisions','inventory','remaining_doubts','certainty_resolutions','notation','abbreviations','hand_log','notes','check_events','unresolved_for_main','raw_difference_disposition']
assert all(k in report for k in required)
assert [d['id'] for d in report['decisions']]==['M0688','M0689']
print(f'Wrote {path}; {len(changes)} comparison rows; {len(report["inventory"])} inventoried elements; literal C/H excerpt checks passed; no compilation.')
