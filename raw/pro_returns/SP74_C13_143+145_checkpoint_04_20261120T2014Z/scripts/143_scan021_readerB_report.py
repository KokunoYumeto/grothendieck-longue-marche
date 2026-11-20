import json
from pathlib import Path
base=Path('/workspace/scratch/8f839dff4bf0')
root=base/'SP74_C13_143+145_work'
pkt=json.loads((base/'reader_packets/143_scan021.json').read_text())
Csrc,Hsrc=pkt['witness_C'],pkt['witness_H']
prefix='crops/143_scan021_readerB_'
boxes={'cancelled_fibres':[930,270,1640,433],'live_groupoid_glyphs':[468,1093,1175,1310],'components_restart':[339,1525,1455,1748],'centralise_assumption':[329,1865,1660,2085],'final_tail':[340,2087,1650,2345]}
def row(place,C,H,final,ac,ah,kind,ink,confidence='high',crop=None,marked=False,consequential=False):
    assert C=='[no witness]' or C in Csrc,('C not literal',place,C)
    assert H=='[no witness]' or H in Hsrc,('H not literal',place,H)
    return dict(place=place,C=C,H=H,final=final,against_C=ac,against_H=ah,kind=kind,ink=ink,confidence=confidence,crop=prefix+crop+'.png' if crop else 'page',box=boxes.get(crop),marked_in_H=marked,consequential=consequential)
def alph(place,C=r'\tau',H=r'\mathcal{T}',final=r'\unsure{\tau|\mathcal T}',crop=None):
    return row(place,C,H,final,False,True,'misread symbol or index','The set glyph has a curled flag-like upper stroke and one broad curved lower return. C encodes it as tau and H as calligraphic T. Neither alphabet is certified here, so both are retained locally. This is an alphabet-encoding question, not a consequential mathematical correction.','medium',crop)
changes=[
 alph('Cancelled passage, set glyph in the first fibre symbol',r'\tau_j',r'\mathcal{T}_j',r'\unsure{\tau|\mathcal T}_j','cancelled_fibres'),
 row('Cancelled passage, orbit-set notation after j in',r'\unsure{\tau/\pi|\tau_\pi}',r'\mathcal{T}/\pi',r'\unsure{\tau_\pi|\mathcal T_\pi|\tau/\pi|\mathcal T/\pi}',True,True,'misread symbol or index','The pi is low at the right of the set glyph. No independent slash is securely separable from the rising exit of that glyph, so a subscript pi is the first reading. A quotient remains possible. The tau/calligraphic-T alphabet choice is separately open; the four alternatives preserve both uncertainties without claiming different mathematics.','low','cancelled_fibres'),
 alph('Cancelled passage, bare set glyph after dans',crop='cancelled_fibres'),
 row('Cancelled passage, punctuation after dans the set',r'dans $\tau$ \deleted{puis}',"dans $\\mathcal{T}$,\n\\struck{puis}",r'dans $\unsure{\tau|\mathcal T}$',False,True,'text not on the page','The set glyph ends in its broad lower exit followed by blank paper. No separate comma appears before the next line\'s locally cancelled puis.','high','cancelled_fibres'),
 alph('Cancelled passage, set glyph in t in the fibre',r'\tau_j',r'\mathcal{T}_j',r'\unsure{\tau|\mathcal T}_j'),
 row('Last cancelled line, initial word',r'alors $\pi_t$ centralise',r'dont $\pi_t$ centralise',r'alors $\pi_t$ centralise',False,True,'misread word','The word has a low a, a tall l, then joined or-s strokes. It does not have the initial tall d and terminal t of dont.'),
 row('Live restriction paragraph, extension/action-group glyph',r"l'opération de $\mathcal E$",r"l'opération de $\Sigma$",r"l'opération de $\unsure{\mathcal E|\Sigma}$",False,True,'misread symbol or index','The group glyph has a rounded upper lobe and a heavier retraced lower lobe. It is distinct from the adjacent set glyph, but its E/Sigma identification remains unresolved under the shared convention.','medium','live_groupoid_glyphs'),
 alph('Live restriction paragraph, set acted upon',crop='live_groupoid_glyphs'),
 alph('Live restriction paragraph, groupoid expression',r'\langle\tau,\pi\rangle',r'\langle \mathcal{T}, \pi \rangle',r'\langle\unsure{\tau|\mathcal T},\pi\rangle','live_groupoid_glyphs'),
 row('Live restriction paragraph, first ens abbreviation',"dont l'ens des",r"dont l'ens.\ des","dont l'ens des",False,True,'text not on the page','No detached dot follows ens before des. The exit of s belongs to the word itself.'),
 alph('Live restriction paragraph, object set',r'est $\tau$',r'est $\mathcal{T}$',r'est $\unsure{\tau|\mathcal T}$'),
 row('Live restriction paragraph, second ens abbreviation',"l'ens des",r"l'ens.\ des","l'ens des",False,True,'text not on the page','The second ens, before the Isom expression, likewise has no separate abbreviation point.'),
 row('Cancelled restart before the component formula',r'\deleted{\unsure{Les composantes|La composition}}',r'\struck{La composition}',r'\deleted{\unsure{Les composantes|La composition}}',False,True,'misread word','The cancellation leaves an initial L, low following traces, a c-loop and a p-like descender. The last letters are crossed too closely to distinguish composantes from composition reliably. The candidate keeps both alternatives and does not certify H\'s reading.','low','components_restart'),
 row('Live restart after the cancellation','On a',r'\ill{}.','On a',False,True,'readable ink left as \\ill{}','A large looped O with a low n exit is followed by a small separate compact a-like mark. The reading On a is supported, though the final a is written very shortly.','medium','components_restart'),
 alph('Component formula, groupoid argument',r'\pi_0\langle\tau,\pi\rangle',r'\pi_0 \langle \mathcal{T}, \pi \rangle',r'\pi_0\langle\unsure{\tau|\mathcal T},\pi\rangle','components_restart'),
 alph('Component formula, quotient numerator',r'\tau/\pi',r'\mathcal{T}/\pi',r'\unsure{\tau|\mathcal T}/\pi','components_restart'),
 row('Component formula, definition label',r'\overset{\mathrm{dfn}}=',r'\overset{\mathrm{df}}{=}',r'\overset{\mathrm{dfn}}{=}',False,True,'omission','The label shows d with a loop, a tall f-like stroke and a low n-like return extending right. The final n is retained.','medium','components_restart'),
 alph('Fundamental-group formula, pointed set argument',r'\pi_1(\tau,t)',r'\pi_1(\mathcal{T}, t)',r'\pi_1(\unsure{\tau|\mathcal T},t)'),
 row('Centralisation sentence, live versus cancelled centralise',r'$\pi_t$ centralise',r'$\pi_t$ \struck{centralise}',r'$\pi_t$ centralise',False,True,'deletion state','The initial c/e strokes are dark and partly retraced, but no independent cancellation continues across centralise. The remaining letters, including their ascenders and exits, are live.','high','centralise_assumption'),
 row('Punctuation after the centralised subgroup',r'$\Phi(t)(T)\subset\pi$.',r'$\Phi(t)(T) \subset \pi$ :',r'$\Phi(t)(T)\subset\pi$.',False,True,'misread symbol or index','A distinct dark point is present at the baseline after pi. Several much smaller isolated spots sit high above it; these are not treated as a second punctuation point. The candidate retains the period.','medium','centralise_assumption'),
 row('Transition to the commutativity assumption','On suppose',"\\ill{},\n\\uncertain{supposons}",'On suppose',False,True,'misread word','On is partly crowded by the descender of que on the previous line, but its loop and low n survive. The following word has s-u, two descending p strokes, and the compact o-s-e ending; no final ons is present.','high','centralise_assumption',True),
 row('Dash after the live Phi-t isomorphism','---','[no witness]','---',False,True,'omission','A separate short horizontal dash follows pi-t at the right of the line, before the next line\'s cancelled du.','high','final_tail'),
 row('After d\'autres termes, punctuation',"d'autres termes on suppose","d'autres termes, on suppose","d'autres termes on suppose",False,True,'text not on the page','The final exit of termes is followed by a gap and on; no comma intervenes.','high','final_tail'),
 row('Final paragraph, donné ending','donné,','donnée,','donné,',False,True,'misread word','After d, the low o-n-n sequence leads to the terminal accented e-like rise. There is no further e before the visible comma.','medium','final_tail'),
 alph('Final paragraph, set supplied in addition',r'en plus de $\tau$',r'en plus de $\mathcal{T}$',r'en plus de $\unsure{\tau|\mathcal T}$','final_tail'),
 row('Final paragraph, extension/action-group glyph',r'\mathcal E',r'\Sigma',r'\unsure{\mathcal E|\Sigma}',False,True,'misread symbol or index','The final group glyph has two open rounded lobes, differing from the adjacent flag-topped set glyph. The E/Sigma alphabet identification remains open under the shared convention.','medium','final_tail'),
 row('Final paragraph, first -ens abbreviation punctuation',r'$\mathcal E$-ens',r'$\Sigma$-ens.',r'$\unsure{\mathcal E|\Sigma}$-ens',False,True,'text not on the page','A short leading hyphen is followed by the ens trace; its final exit is followed by blank space and de, with no detached period.','high','final_tail'),
 row('M0699, word before pi-ens',r'\unsure{donc|de}',r"de $\pi$-ens.",'de',True,False,'misread word','The short word consists of a tall d with a small lower loop followed by a low e exit. The extra on-c strokes needed for donc are absent.','high','final_tail',True),
 row('Final pi-ens abbreviation punctuation',r'$\pi$-ens,',r'$\pi$-ens.',r'$\pi$-ens,',False,True,'text not on the page','The final ens has no separate full stop; it is followed by a long descending comma.','high','final_tail'),
 row('Bottom-left page number',r'\mspage{20}','[no witness]',r'\mspage{20}',False,True,'omission','A graphite 20 stands at the bottom-left, with a curved 2 and closed 0.')
]

def inv(i,kind,pos,words,hand='his hand'):
    return dict(sheet_kind='text',hand=hand,element=f'E{i:02d}',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes')
report={
'key':'143_scan021','reader':'B','stage':'first','image_views':['original','half1','half2'],'changes':changes,
'decisions':[
 {'id':'M0699','decision':'alternative','reading':'de','ink':'The word has an ascender and loop for d, followed by one low e exit; it is too short for donc and has none of its extra letter strokes.','crop':prefix+'final_tail.png','box':boxes['final_tail'],'confidence':'high'}
],
'inventory':[
 inv(1,'deletion','top block, first four lines; entire block crossed by two long oblique strokes','pi-torseurs. Pour j in J, le pi-torseur correspondant P-j s\'envoie dans the set fibre; fibre de j in the orbit-set notation dans the set'),
 inv(2,'deletion','top block, left of la fibre','puis, separately struck before the whole-block cancellation'),
 inv(3,'deletion','top block, middle three lines','la fibre de P-j en t in the set fibre étant le torseur sous le stabilisateur pi-t de t dans pi suivant : on considère'),
 inv(4,'diagram','inside the cancelled block, on the on considère line','Phi(t):T to pi, all deleted with the surrounding block'),
 inv(5,'deletion','last line of the top cancelled block','alors pi-t centralise'),
 inv(6,'text','live restriction paragraph after the cancelled block','Considérons la restriction de l\'opération of the extension/action group on the set to pi; action groupoid and object/morphism sets'),
 inv(7,'display','morphism-set definition at the end of the restriction paragraph','pi-sub-t-to-t-prime={lambda in pi | lambda t=t-prime}.'),
 inv(8,'deletion','before On a','Les composantes / La composition, unresolved'),
 inv(9,'text','after that cancellation','On a'),
 inv(10,'display','component formula','pi-zero of the action groupoid = set/pi = by dfn J'),
 inv(11,'display','fundamental-group formula','pi-one(set,t)=pi-t (stabilisateur de t dans pi)'),
 inv(12,'text','centralisation assertion and new assumption','et on trouve que pi-t centralise Phi(t)(T) subset pi. On suppose'),
 inv(13,'text','right end of the assumption line, underlined once','T commutatif'),
 inv(14,'deletion','following line, after et','pi-t=Phi-t(T)'),
 inv(15,'display','same line, live map followed by a dash','Phi-t:T isomorphic to pi-t'),
 inv(16,'deletion','start of penultimate prose line','du'),
 inv(17,'text','final two prose lines','d\'autres termes on suppose donné, en plus de the set, extension/action-group-ens de pi-ens,'),
 inv(18,'margin note','bottom-left corner','20','pencil hand, unassigned')
],
'remaining_doubts':[
 {'place':'Set glyph, all eleven occurrences','reading':r'\unsure{\tau|\mathcal T}','alternatives':r'\tau or \mathcal T','confidence':'medium','reason':'The graph has a curled flag-like upper stroke and one broad lower return. It differs from the separately supplied description of the three-like Z glyph on other pages. This page does not settle whether its alphabet should be tau or calligraphic T.'},
 {'place':'Cancelled first orbit-set notation after j in','reading':r'\unsure{\tau_\pi|\mathcal T_\pi|\tau/\pi|\mathcal T/\pi}','alternatives':'low subscript pi; quotient slash and pi, with either set-glyph alphabet','confidence':'low','reason':'The pi is low and there is no independent slash clearly separable from the set glyph\'s rising exit. The later quotient formula does have a clear separate slash, but that does not authorize regularizing the earlier notation.'},
 {'place':'Cancelled phrase before On a','reading':r'\deleted{\unsure{Les composantes|La composition}}','alternatives':'Les composantes; La composition','confidence':'low','reason':'The single cancellation crosses most low letters. Initial L, c-loop and p-like descender survive, but the word endings do not separate reliably.'},
 {'place':'Extension/action-group letter, both occurrences','reading':r'\unsure{\mathcal E|\Sigma}','alternatives':r'\mathcal E or \Sigma','confidence':'medium','reason':'The glyph retains two rounded lobes, with retracing in its first occurrence. The shared E/Sigma question remains unresolved; no third letter is inferred.'}
],
'certainty_resolutions':[
 {'place':'Cancelled du at start of the final prose','C':r'\deleted{\unsure{du}}','final':r'\deleted{du}','ink':'The crop shows a d ascender and lower loop followed by a short u-like low exit beneath the cancellation.'}
],
'notation':[
 {'form':r'\unsure{\tau|\mathcal T}','meaning':'set on which the extension/action group and its subgroup pi act','evidence':'All eleven occurrences share a flag-topped curled form with one broad lower return. C uses tau; H uses calligraphic T. Both encodings remain open, and the provisional mathfrak Z from other pages is not transferred.'},
 {'form':r'T','meaning':'group assumed commutative and identified with the stabilizers via Phi-t','evidence':'The source explicitly underlines T commutatif and writes Phi-t:T to pi-t with an isomorphism sign. Its plain T graph differs from the set glyph.'},
 {'form':r'\pi_t','meaning':'stabilizer of t in pi','evidence':'The parenthetical definition says stabilisateur de t dans pi. The same subscript t is visible in the cancelled and live passages.'},
 {'form':r"\pi_{t\to t'}=\{\lambda\in\pi\mid\lambda t=t'\}",'meaning':'the action-groupoid morphism set as stated on the page','evidence':'The formula gives the lambda condition literally; its arrow and both t-primes were inspected.'},
 {'form':r'\Phi(t)\,,\ \Phi_t','meaning':'two displayed notations for the maps from T','evidence':'The cancelled map and centralisation sentence use Phi(t); the cancelled equality and live final isomorphism use the subscripted Phi-t. These source variants are preserved.'},
 {'form':r'\unsure{\mathcal E|\Sigma}','meaning':'the extension/action-group glyph','evidence':'The first graph is partly retraced; the last graph has two rounded lobes. The current shared uncertainty is preserved.'},
 {'form':r'\pi_0\langle\unsure{\tau|\mathcal T},\pi\rangle=\unsure{\tau|\mathcal T}/\pi=J','meaning':'the source\'s component/orbit-set identification','evidence':'The later formula has a clear separate quotient slash and defines J with a dfn label.'}
],
'abbreviations':[
 {'form':'ens','expansion':'ensemble / ensembles, according to the local phrase'},
 {'form':'Isom','expansion':'isomorphismes'},
 {'form':'dfn','expansion':'definition'}
],
'hand_log':[
 {'habit':'The set glyph has a curled flag-like top and one broad lower return, differing from the plain capital T.','places':'Four occurrences in the cancelled block, three in the restriction paragraph, two in the component formula, one in the fundamental-group formula, and one in the final prose.','scope':'All eleven graphs inspected. The page alone does not settle tau versus calligraphic T.','misreadings':'C/H alphabet alternatives are recorded at every occurrence at non-consequential confidence; the Z encoding described for other pages was not transferred.'},
 {'habit':'A low pi after the set glyph can be hard to distinguish from quotient notation because the set glyph\'s exit rises.','places':'Cancelled orbit-set notation; compared with the later explicitly slashed quotient.','scope':'Both occurrences inspected in their respective crops.','misreadings':'The first construction remains uncertain and is not silently normalized to the later slash form.'},
 {'habit':'Retraced opening letters can resemble a cancellation even when the rest of the word is live.','places':'centralise in the live centralisation sentence.','scope':'The whole word and surrounding line inspected in one crop.','misreadings':'H marks centralise as struck; no separate cancellation across the word is visible.'},
 {'habit':'The descender from the previous line can crowd the beginning of a new phrase.','places':'On suppose beneath the descender of que.','scope':'This single locus.','misreadings':'H leaves preceding material illegible and proposes supposons; the crop supports On suppose.'},
 {'habit':'The abbreviation ens has a long final exit but no necessary abbreviation point.','places':'Two ens occurrences in the restriction paragraph, extension/action-group-ens and pi-ens at the end.','scope':'All four instances inspected; no separate periods are visible.','misreadings':'H supplies a point at each of these four positions.'},
 {'habit':'The small a of On a may be a very compact closed mark.','places':'Live restart before the component formula.','scope':'This local reading is medium confidence.','misreadings':'H leaves the restart as ill{}.; C\'s On a is retained.'}
],
'notes':[
 {'id':'143_scan021-N1','text':'The top passage is cancelled as a whole by two long oblique strokes. It begins pi-torseurs, describes the fibres of a torsor P-j over a set fibre, and reaches the map Phi(t):T to pi followed by alors pi-t centralise. Puis was separately struck before the larger cancellation. H\'s terminal note explicitly acknowledges the two oblique strokes; its different placement of deletion markup is therefore not treated as an independent reading correction.'},
 {'id':'143_scan021-N2','text':'The live text restricts an action of the extension/action group to pi and describes the resulting action groupoid: its objects are the set and its morphisms t to t-prime are the lambda satisfying lambda t=t-prime. It then writes component and fundamental-group formulas. These are source accounts; no action-groupoid theorem or identification has been independently proved in this reading pass.'},
 {'id':'143_scan021-N3','text':'The source says pi-t centralise Phi(t)(T) subset pi and then On suppose T commutatif, with the latter phrase underlined once. It cancels the equality pi-t=Phi-t(T) and writes a live isomorphism Phi-t:T to pi-t. The word centralise is live, and the two uses Phi(t) versus Phi-t are preserved exactly rather than regularized.'},
 {'id':'143_scan021-N4','text':'The last prose reads d\'autres termes on suppose donné, en plus de the set, extension/action-group-ens de pi-ens,. The word de, although donc might be a smoother transition, is what the visible short d/e sequence supports. No comma is supplied after termes, and no extra e is supplied in donné. The source ends with a comma and continues beyond this page; no continuation was inspected.'},
 {'id':'143_scan021-N5','text':'The set glyph is not automatically identified with the provisional mathfrak Z described for other pages. Its tau/calligraphic-T alternatives remain open at each occurrence. These alphabet rows are medium confidence and non-consequential; they are not claims of mathematical correction. The first orbit-set notation separately remains uncertain between a low pi subscript and a slash construction.'},
 {'id':'143_scan021-N6','text':'After the centralised-subgroup formula, the candidate retains the distinct baseline period. Several very small high spots above it are treated as incidental ink rather than promoted into an additional punctuation point. The graphite 20 at the bottom left is retained.'}
],
'check_events':[
 {'statement_id':'143_scan021-N1','type':'carried as background without fault found','outcome':'The cancelled torsor discussion and its map were transcribed visually. No torsor/fibre assertion was independently verified.'},
 {'statement_id':'143_scan021-N2','type':'carried as background without fault found','outcome':'The action-groupoid definition and the pi-zero/pi-one identifications were collated, not re-proved. No external assumptions were introduced to change the notation.'},
 {'statement_id':'143_scan021-N3','type':'carried as background without fault found','outcome':'The centralisation assertion and the commutativity/isomorphism assumptions were read as source statements. Their mathematical validity was not established by transcription.'}
],
'unresolved_for_main':[
 {'place':'Set alphabet and the first orbit-set notation','crop':prefix+'cancelled_fibres.png','question':'Keep tau/calligraphic-T alternatives open. The first low pi is provisionally subscripted; quotient remains possible.'},
 {'place':'Live set glyph and first extension/action-group glyph','crop':prefix+'live_groupoid_glyphs.png','question':'These distinguish the flag-topped set graph from the two-lobed group graph, but do not alone settle either alphabet.'},
 {'place':'Cancelled Les composantes / La composition','crop':prefix+'components_restart.png','question':'The crossed word ending remains insufficiently separated; both alternatives retained.'},
 {'place':'Punctuation after the centralised subgroup','crop':prefix+'centralise_assumption.png','question':'Reader B retains the baseline period and treats the much smaller high spots as incidental ink. Please include this in the punctuation review.'}
],
'raw_difference_disposition':'All packet differences and all agreements were inspected against the original once and both native halves once, followed by five unique tight crops. Every C/H comparison excerpt below was verified as a literal substring of the assigned packet, except the explicit [no witness] marker. All eleven set-glyph occurrences are individually represented, including the first construction where alphabet and index-versus-slash uncertainties coincide; alphabet-only rows are medium confidence and non-consequential. Both extension/action-group occurrences are also represented. H\'s note acknowledges the top block\'s two cancellation strokes, so its alternative wrapper placement is treated as markup rather than a new source reading; the candidate nevertheless marks all of that block, its map and the separately struck puis as deleted. Equivalent diagram/display/paragraph wrappers, font/spacing macros beyond the recorded alphabet questions, editorial continuation notes and end{document} are not source additions. Decisions contain only M0699. Other open loci are recorded in remaining_doubts with no invented MARKS ids. No other page, OCR, web research or TeX compilation was used.'
}
path=root/'reviews/143_scan021_readerB.json'
path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
assert [x['id'] for x in report['decisions']]==['M0699']
assert len([x for x in report['changes'] if x['place'] in [
'Cancelled passage, set glyph in the first fibre symbol','Cancelled passage, orbit-set notation after j in','Cancelled passage, bare set glyph after dans','Cancelled passage, set glyph in t in the fibre','Live restriction paragraph, set acted upon','Live restriction paragraph, groupoid expression','Live restriction paragraph, object set','Component formula, groupoid argument','Component formula, quotient numerator','Fundamental-group formula, pointed set argument','Final paragraph, set supplied in addition']])==11
print(f'Wrote {path}; {len(changes)} literal-excerpt comparison rows; {len(report["inventory"])} inventory elements; 11 set-glyph occurrences; original MARKS id only; no compilation.')
