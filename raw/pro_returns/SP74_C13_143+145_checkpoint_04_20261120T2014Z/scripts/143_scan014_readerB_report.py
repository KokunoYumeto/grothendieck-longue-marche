import json
from pathlib import Path
root=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
prefix='crops/143_scan014_readerB_'
boxes={'les_appl':[470,413,672,522],'hom_ending':[1390,1285,1650,1392],'first_aut_map':[600,1390,1645,1537],'cancelled_peut_se':[900,1753,1215,1861],'lower_group_maps':[640,1950,1645,2165],'final_clause':[375,2160,1565,2250],'final_deduite':[370,2242,1050,2310],'final_envisagees':[1050,2235,1662,2314]}
def row(place,C,H,final,ac,ah,kind,ink,confidence='high',crop=None,marked=False,consequential=False):
    return dict(place=place,C=C,H=H,final=final,against_C=ac,against_H=ah,kind=kind,ink=ink,confidence=confidence,crop=prefix+crop+'.png' if crop else 'page',box=boxes.get(crop),marked_in_H=marked,consequential=consequential)
changes=[]
for x in ['I','J']:
    changes.append(row('First display, '+x+' row, contracted-product index',"Y'("+x+r")\simeq\widetilde X'("+x+r")\mathbin{\wedge}_{\pi_1}E",r"\mathcal{Y}'("+x+r")\simeq\widetilde{\mathfrak{X}}'("+x+r")\wedge^{\pi_1}E","Y'("+x+r")\simeq\widetilde{\mathfrak X}'("+x+r")\mathbin{\wedge}_{\pi_1}E",False,True,'misread symbol or index','The pi-one is visibly lower and to the right of the wedge, below the baseline of the adjacent E. All primes and tildes in this row were inspected.',consequential=True))
changes.append(row('After first display: live les and cancelled following word',r'et \unsure{les} \deleted{\unsure{appl.}}',r'et \struck{les appl.}',r'et les \deleted{\unsure{appl.}}',False,True,'deletion state','The tall l, looped e and final s of les stand entirely to the left of the dark horizontal cancellation. That cancellation starts in the following a-p-like word; its interior ending is too obscured to certify appl.','high','les_appl'))
changes.append(row('End of isomorphismes (11) sentence','des iso.','des isom.','des iso.',False,True,'abbreviation expanded or spelling modernised','The new line contains dotted i, s, a rounded o, then a detached dot. No m follows the o.'))
for x in ['I','J']:
    midC=r'B_\gamma' if x=='I' else r'(B_\gamma)'
    midH=r'\mathcal B_\gamma' if x=='I' else r'(\mathcal B_\gamma)'
    C=r"\widetilde X'("+x+r")\mathbin{\wedge}_{\pi_1}E\simeq(\widetilde X'("+x+r")\mathbin{\wedge}_{\pi_1}"+midC+r')\mathbin{\wedge}_{\pi_1}E'
    H=r"\widetilde{\mathfrak X}'("+x+r")\wedge^{\pi_1}E\simeq(\widetilde{\mathfrak X}'("+x+r")\wedge^{\pi_1}"+midH+r')\wedge^{\pi_1}E'
    final=C.replace(r'\widetilde X',r'\widetilde{\mathfrak X}')
    changes.append(row('Second display, '+x+' row, all three contracted-product indices',C,H,final,False,True,'misread symbol or index','Each of the three pi-one labels sits below its wedge: left of the isomorphism sign, inside the parenthesis, and after its close. The extra parentheses around B-gamma occur only in the J row and are preserved.',consequential=True))
changes.append(row('Prose introducing the third display',"qu'on peut décrire à l'aide d'isom.",r"qui proviennent à \uncertain{droite} d'isom.","qu'on peut décrire à l'aide d'isom.",False,True,'misread word','The opening has the q-descender and short on trace, then a separate p-descender and eu-t strokes. Décrire has the initial tall d and the crir/e sequence. The next words show l-apostrophe-aide, rather than droite.','high',None,True))
changes.append(row('Right pi-one sets abbreviation',r'$\pi_1$-ens',r'$\pi_1$-ens.',r'$\pi_1$-ens',False,True,'text not on the page','The short ens trace is followed directly by the separated à; no dark full stop lies between them.'))
for x in ['I','J']:
    C=r"\widetilde X'("+x+r")\simeq\widetilde X'("+x+r")\mathbin{\wedge}_{\pi_1}B_\gamma"
    H=r"\widetilde{\mathfrak X}'("+x+r")\simeq\widetilde{\mathfrak X}'("+x+r")\wedge^{\pi_1}\mathcal B_\gamma"
    changes.append(row('Third display, '+x+' row, contracted-product index',C,H,C.replace(r'\widetilde X',r'\widetilde{\mathfrak X}'),False,True,'misread symbol or index','The pi-one is below the wedge; the B-gamma follows at the higher ordinary baseline. All primes, tildes and I/J arguments in the row were inspected.',consequential=True))
changes.append(row('Before first Aut map, ending abbreviation',"d'hom.","d'homs","d'hom",True,True,'misread word','After the tall h and low o, the final m is a joined two-hump stroke ending in a downturned exit. There is no separate final s and no detached punctuation after that exit.','high','hom_ending'))
changes.append(row('First B-gamma to Aut map, connector',r'B_\gamma \arrow[r,dash]',r'\mathcal{B}_{\gamma} \longrightarrow',r'B_\gamma \arrow[r,"{\unsure{}}" description]',True,False,'drawing or diagram','The horizontal shaft ends in a small raised dark wedge. A pointed head is plausible by comparison with the lower map on this same page, whose head is drawn above the shaft, but the first tip is thick and locally ambiguous. The candidate carries an explicit uncertainty mark on the arrow.','medium','first_aut_map',False,True))
changes.append(row('First Aut, detached short stroke over initial A',r'\operatorname{Aut}',r'\mathrm{Aut}',r'{\unsure{\overline{\mathrm A}|\mathrm A}\mathrm{ut}}',True,True,'omission','A short detached curved horizontal stroke sits directly over the A, shorter than the full word Aut. It may be an overbar or part of the formation of this capital; the candidate marks that choice rather than asserting a new mathematical operator.','low','first_aut_map',False,True))
changes.append(row('First Aut, cancelled lower index',r'\operatorname{Aut}_{\deleted{\unsure{\mathrm{ens}}}}',r'\mathrm{Aut}; note: sous « Aut », sur la troisième accolade, un mot surchargé',r'{\unsure{\overline{\mathrm A}|\mathrm A}\mathrm{ut}}_{\deleted{\unsure{\mathrm{ens}}}}',False,True,'omission','Below Aut there is a small word crossed by several oblique strokes. Its initial e-loop survives. The rest is compatible with ns but cannot be independently read through the hatching.','low','first_aut_map',True))
changes.append(row('Et itou row, closing delimiter',r"et itou pour $\widetilde X'(J)$",r"et itou pour $\widetilde{\mathfrak{X}}'(J))$",r"et itou pour $\widetilde{\mathfrak X}'(J)$",False,True,'text not on the page','Only the closing parenthesis belonging to the opening before J is present. There is no additional closing parenthesis after it.'))
changes.append(row('Compatibility sentence, abbreviation','les op de','les op. de','les op de',False,True,'text not on the page','The descending p of op is followed by de without a separate punctuation dot.'))
changes.append(row('Following paragraph opening','Or la donnée de ces applications','On a donc là des applications','Or la donnée de ces applications',False,True,'misread word','The first word has round O followed by a short r; then a separate looped l-a. The following long word has d-on-née, followed by de and ces. The strokes do not match On a donc là des.'))
changes.append(row('Following paragraph, equivalence verb','équivaut','équivalant','équivaut',False,True,'misread word','The end after équiva is a low u and a small raised terminal t-hook; no intervening l-ant sequence is visible.'))
changes.append(row('Cancelled wording after équivaut',r'\deleted{\unsure{peut se}}',r'\struck{\ill{}}',r'\deleted{\unsure{peut se}}',False,True,'readable ink left as \\ill{}','The cancellation leaves a long returning p-descender, a separate tall t near the middle, and an e-like loop at the far right after a space. Peut se remains tentative because the low internal letters coincide with the strike.','low','cancelled_peut_se',True))
changes.append(row('Lower pair of maps, source group',r"\mathcal E'_{\Gamma'}=\displaystyle\bigcup_{\gamma\in\Gamma'}B_\gamma",r"\Sigma'_{\Gamma'}=\bigcup_{\gamma\in\Gamma'}\mathcal B_\gamma",r"\unsure{\mathcal E'|\Sigma'}_{\Gamma'}=\displaystyle\bigcup_{\gamma\in\Gamma'}B_\gamma",False,True,'misread symbol or index','The source glyph is rounded and two-lobed, with a separate prime and Gamma-prime below. It supplies no explicit letter-name evidence to settle E versus Sigma, so the shared uncertain convention is retained. The union label is gamma in Gamma-prime, and the summand is B-gamma.','low','lower_group_maps'))
changes.append(row('Lower pair of maps, punctuation after first target',r"\operatorname{Aut}_{\mathrm{ens}}(\widetilde X'(I))",r"\mathrm{Aut}_{\mathrm{ens}}(\widetilde{\mathfrak{X}}'(I)),",r"\operatorname{Aut}_{\mathrm{ens}}(\widetilde{\mathfrak X}'(I))",False,True,'text not on the page','The first target ends at its closing parentheses, followed by blank paper. The second map lies on the next line; no comma separates the rows in the ink.','high','lower_group_maps'))
changes.append(row('Final paragraph, singular clause',r"\unsure{celle qu'on cherche est}","celles qu'on cherche sont","celle qu'on cherche est",False,True,'misread word','Celle ends with the flat exit from e, without the additional downturned s visible in celles on the next line. The short verb has a low e/s trace and a terminal t-hook, rather than the longer sont sequence.','high','final_clause'))
changes.append(row('Final paragraph, extension-group glyph',r"de $\mathcal E'$",r"de $\Sigma'$",r"de $\unsure{\mathcal E'|\Sigma'}$",False,True,'misread symbol or index','The lower-left final-line glyph repeats the rounded two-lobed form with a separate prime. No new evidence here settles the shared E/Sigma question.','low'))
changes.append(row('Final punctuation',r"\widetilde X'(J)\ldots.",r"\widetilde{\mathfrak{X}}'(J)\ldots",r"\widetilde{\mathfrak X}'(J)\ldots.",False,True,'omission','Four separate dark dots follow the final closing parenthesis.'))
changes.append(row('Bottom-left page number',r'\mspage{13}','[no witness]',r'\mspage{13}',False,True,'omission','The bottom-left corner has a graphite 13, with a narrow 1 and a double-curved 3. The upper-right 7 is also retained.'))

def inv(n,kind,pos,words,hand='his hand'):
    return dict(sheet_kind='text',hand=hand,element=f'E{n:02d}',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes')
report={
'key':'143_scan014','reader':'B','stage':'first','image_views':['original','half1','half2'],'changes':changes,
'decisions':[
 {'id':'M0670','decision':'first','reading':'les','ink':'The l-e-s strokes lie wholly to the left of the cancellation on the following word. All three letters are readable and live.','crop':prefix+'les_appl.png','box':boxes['les_appl'],'confidence':'high'},
 {'id':'M0671','decision':'first','reading':"celle qu'on cherche est",'ink':'The first noun-like form ends in e with no added s; the verb is the compact est with a terminal t-hook. Compare the separately visible plural celles on the following line.','crop':prefix+'final_clause.png','box':boxes['final_clause'],'confidence':'high'},
 {'id':'M0672','decision':'first','reading':'déduite','ink':'The first d is partly approached by a descender from the line above; the next sequence has é, another tall d, a low u, dotted i, t-rise and final e. The wavy stroke below belongs to the tilde-X on the next line, not an underline.','crop':prefix+'final_deduite.png','box':boxes['final_deduite'],'confidence':'medium'},
 {'id':'M0673','decision':'first','reading':'envisagées','ink':'The low env trace leads to a dotted i, s and small a, then a clear g-loop with descender; an accent and the terminal ées sequence remain at the right.','crop':prefix+'final_envisagees.png','box':boxes['final_envisagees'],'confidence':'high'}
],
'inventory':[
 inv(1,'margin note','upper-right corner','7','pencil hand, unassigned'),
 inv(2,'text','top line',"En fait, si Y-prime corresponds to E, on a"),
 inv(3,'display','first displayed pair, I row',"Y-prime(I) isomorphic to tilde-X-prime(I) wedge_pi-one E"),
 inv(4,'display','first displayed pair, J row',"Y-prime(J) isomorphic to tilde-X-prime(J) wedge_pi-one E"),
 inv(5,'text','line below first pair and continuation iso.',"et les ... isomorphismes (11) reviennent à des iso."),
 inv(6,'deletion','between les and isomorphismes','appl. uncertain'),
 inv(7,'display','first left brace, I row','isomorphism involving contracted products with B-gamma and E'),
 inv(8,'display','first left brace, J row','isomorphism involving contracted products with (B-gamma) and E'),
 inv(9,'text','two lines following first brace',"qu'on peut décrire à l'aide d'isom. de pi-one-ens à droite"),
 inv(10,'display','second left brace, I row','tilde-X-prime(I) isomorphic to its contracted product with B-gamma'),
 inv(11,'display','second left brace, J row','tilde-X-prime(J) isomorphic to its contracted product with B-gamma'),
 inv(12,'text','above third brace',"lesquels reviennent à la donnée d'hom"),
 inv(13,'diagram','third brace, first row','B-gamma to Aut(tilde-X-prime(I))=Bij(tilde-X-prime(I),tilde-X-prime(I))'),
 inv(14,'deletion','below first Aut','small cross-hatched index, ens uncertain'),
 inv(15,'insertion','just over initial A of first Aut','short detached bar; relation to letter formation uncertain'),
 inv(16,'text','third brace, second row','et itou pour tilde-X-prime(J)'),
 inv(17,'text','line below third brace','compatibles avec les op de pi-one à g. et à dr.'),
 inv(18,'text','following paragraph, three lines',"Or la donnée de ces applications, pour gamma in Gamma-prime variable, équivaut ... à la donnée d'...applications"),
 inv(19,'deletion','after équivaut','peut se uncertain'),
 inv(20,'deletion','between apostrophe after d and applications','une'),
 inv(21,'diagram','lower two-row map diagram','extension-group prime sub Gamma-prime = union B-gamma to Aut_ens(tilde-X-prime(I)); second map to Aut_ens(tilde-X-prime(J))'),
 inv(22,'text','final three lines',"et celle qu'on cherche est justement l'opération déduite par celles déjà envisagées de extension-group-prime sur the two tilde-X-prime sets"),
 inv(23,'margin note','bottom-left corner','13','pencil hand, unassigned')
],
'remaining_doubts':[
 {'place':'cancelled word after live les','reading':r'\deleted{\unsure{appl.}}','alternatives':'abbreviated application word; exact internal ending not recoverable','confidence':'low','reason':'The initial a and a p-descender are visible, but the rest coincides with thick cancellation.'},
 {'place':'first B-gamma to Aut connector','reading':r'\arrow[r,"{\unsure{}}" description]','alternatives':r'\arrow[r,dash]','confidence':'medium','reason':'The tip is a small raised dark wedge. It resembles the above-shaft lower arrowhead but is thick enough to remain ambiguous.'},
 {'place':'short stroke over first Aut initial','reading':r'\unsure{\overline{\mathrm A}|\mathrm A}\mathrm{ut}','alternatives':'bar over A; or an element of the handwritten capital A rather than a mathematical accent','confidence':'low','reason':'The small curved stroke is detached from the A. The page does not explain any accented Aut notation.'},
 {'place':'cancelled index under first Aut','reading':r'\deleted{\unsure{\mathrm{ens}}}','alternatives':'short index beginning with e; remainder cross-hatched','confidence':'low','reason':'The e loop is readable, but crossing strokes obscure independent n/s outlines.'},
 {'place':'cancelled phrase after équivaut','reading':r'\deleted{\unsure{peut se}}','alternatives':'short phrase with p-like initial, t-upright, and terminal e-like loop','confidence':'low','reason':'Most low letters lie on the cancellation stroke.'},
 {'place':'extension-group glyph in lower diagram and final line','reading':r"\unsure{\mathcal E'|\Sigma'}",'alternatives':r"\mathcal E' or \Sigma'",'confidence':'low','reason':'The rounded two-lobed form repeats, but the page offers no explicit identifying name or decisive contrast settling this shared notation.'}
],
'certainty_resolutions':[
 {'place':'M0670','C':r'\unsure{les}','final':'les','ink':'The three letters stand uncancelled to the left of the strike through the following word.'},
 {'place':'M0671','C':r"\unsure{celle qu'on cherche est}",'final':"celle qu'on cherche est",'ink':'Singular celle and short est are supported by the final-clause crop.'},
 {'place':'M0672','C':r'\unsure{déduite}','final':'déduite','ink':'The d-é-d-u-i-t-e sequence is recoverable, including the second ascender, i dot and terminal t/e.'},
 {'place':'M0673','C':r'\unsure{envisagées}','final':'envisagées','ink':'Dotted i, g-loop/descender, accent and the final letter sequence are visible.'}
],
'notation':[
 {'form':r'\mathbin{\wedge}_{\pi_1}','meaning':'contracted-product notation used by the author','evidence':'All ten pi-one labels are physically below their wedges on this page; H repeatedly places them above.'},
 {'form':r"\widetilde{\mathfrak X}'(I),\ \widetilde{\mathfrak X}'(J)",'meaning':'the two collections of lifted points used in the formulas','evidence':'Every displayed occurrence has the tilde and prime inspected; the mathfrak encoding follows the current supplied notation table.'},
 {'form':r"Y',\ E,\ B_\gamma",'meaning':'the cover/object corresponding to E, and the B-gamma objects appearing in the contracted products','evidence':'The initial line explicitly pairs Y-prime and E. B-gamma has an ordinary rounded capital B shape here. C encodings Y and B are retained; the H calligraphic wrappers alone are not treated as distinct source variables.'},
 {'form':r"\unsure{\mathcal E'|\Sigma'}_{\Gamma'}=\bigcup_{\gamma\in\Gamma'}B_\gamma",'meaning':'source of the pair of lower maps','evidence':'The primed rounded group glyph, Gamma-prime subscript, union sign and gamma-in-Gamma-prime label are visible. This page does not settle the E/Sigma identification.'},
 {'form':r'\operatorname{Aut}_{\mathrm{ens}}','meaning':'automorphism group of the indicated underlying set','evidence':'The two lower subscripts are compressed e-n-s traces; the analogous first subscript has been cross-hatched. The short stroke over the first A remains separately uncertain.'}
],
'abbreviations':[
 {'form':'appl.','expansion':'applications (cancelled reading uncertain)'},
 {'form':'iso.','expansion':'isomorphismes'},
 {'form':'isom.','expansion':'isomorphismes'},
 {'form':'ens','expansion':'ensembles'},
 {'form':'hom','expansion':'homomorphismes'},
 {'form':'op','expansion':'opérations'},
 {'form':'g.','expansion':'gauche'},
 {'form':'dr.','expansion':'droite'},
 {'form':'Aut','expansion':'automorphismes'},
 {'form':'Bij','expansion':'bijections'}
],
'hand_log':[
 {'habit':'The pi-one index of a contracted product is placed well below and slightly right of a very small wedge.','places':'All six equation rows, ten wedge occurrences in total.','scope':'All ten inspected on scan014.','misreadings':'H gives superscripts at all ten positions; C subscripts are supported.'},
 {'habit':'A long straight map shaft can have a very small head drawn mainly above the shaft.','places':'First B-gamma map and both lower maps.','scope':'All three connectors inspected, including a tight first-map crop and the lower-map crop.','misreadings':'The first connector is uncertain between C dash and H arrow; the two lower connectors have visible heads.'},
 {'habit':'A final s may be a short downturned hook after a long e exit, while singular celle ends with a flat exit.','places':'celle in the final first line; celles in the final second line.','scope':'Both occurrences compared directly.','misreadings':'H pluralizes the first celle and substitutes sont for the compact est.'},
 {'habit':'Terminal t may form a tiny raised triangular hook after a long low exit.','places':'reviennent in the prose; équivaut; est; justement.','scope':'The cited occurrences on this page were inspected; no universal claim outside the page.','misreadings':'H gives équivalant and sont where the shorter word forms are visible.'},
 {'habit':'Cross-hatching preserves a readable initial letter while destroying the internal letters of a short word.','places':'appl.-like cancellation, first Aut subscript, and peut se cancellation.','scope':'All three inspected at one tight crop each; uncertainty retained.','misreadings':'Neither agreement nor a conventional expected term was used to certify obscured letters.'},
 {'habit':'The rounded extension-group glyph remains two-lobed and does not identify its own alphabet.','places':'Lower map source and final line.','scope':'Both inspected on scan014; no claim that this settles other pages.','misreadings':'C reads calligraphic E and H Sigma; current shared uncertainty retained.'}
],
'notes':[
 {'id':'143_scan014-N1','text':'The page starts by pairing Y-prime with E and expressing Y-prime(I) and Y-prime(J) as contracted products. It says the isomorphismes (11) amount to the next pair of isomorphisms, then describes these through isomorphisms of right pi-one sets. These are accounts of what the source states; no equivalence has been independently proved in this reading pass.'},
 {'id':'143_scan014-N2','text':'The source then says those data amount to hom maps from B-gamma to automorphisms/bijections, compatible with the pi-one actions on the left and right. The first Aut lower index is crossed out, and a short detached stroke above its A remains unexplained. The map connector itself is locally doubtful. The uncertainty is visual, and no expected mathematical construction was used to add an arrowhead or define an accented operator.'},
 {'id':'143_scan014-N3','text':'The following paragraph starts Or la donnée de ces applications and uses équivaut. A phrase tentatively read peut se is crossed out; une is crossed out in d\'une applications. The pair of lower maps has the union of the B-gamma as source and the two underlying-set automorphism groups as targets. Both lower arrows have heads, including the small head mainly above the lower shaft.'},
 {'id':'143_scan014-N4','text':'The final sentence is retained with the author\'s singular wording celle qu\'on cherche est and the later plural celles déjà envisagées. It describes an opération déduite par the operations already considered. The wording is not grammatically regularized. The last punctuation consists of four dots.'},
 {'id':'143_scan014-N5','text':'Both page numbers are transcribed: 7 at the upper right and 13 in graphite at the bottom left. Their relationship or authorship is not established by this one-page reading. The lower group glyph does not settle the shared calligraphic-E/Sigma uncertainty.'}
],
'check_events':[
 {'statement_id':'143_scan014-N1','type':'carried as background without fault found','outcome':'The displayed identifications and the asserted equivalence of isomorphism data were visually collated. No independent proof, formal verification or algebraic computation was performed.'},
 {'statement_id':'143_scan014-N2','type':'carried as background without fault found','outcome':'The asserted correspondence with equivariant maps into bijections was transcribed, not proved. Only the ink and the same-page arrow-tip comparison informed the connector reading.'},
 {'statement_id':'143_scan014-N3','type':'carried as background without fault found','outcome':'The union/source and action maps were read from the diagram; no compatibility or action law was independently verified.'},
 {'statement_id':'143_scan014-N4','type':'carried as background without fault found','outcome':'The final identification is reported as the author\'s statement. Its correctness was not established by the transcription.'}
],
'unresolved_for_main':[
 {'place':'First Aut map: small possible arrowhead and detached stroke over A','crop':prefix+'first_aut_map.png','question':'Adjudicate the raised shaft tip against the established arrow convention and the tiny bar over A against the author\'s capital-letter formation. Both are explicitly doubtful in the candidate.'},
 {'place':'First Aut cancelled index','crop':prefix+'first_aut_map.png','question':'Initial e is visible; ens remains tentative under cross-hatching.'},
 {'place':'Cancelled appl.-like word','crop':prefix+'les_appl.png','question':'Les is live and settled; the following word remains unsure{appl.}.'},
 {'place':'Cancelled peut se','crop':prefix+'cancelled_peut_se.png','question':'P-descender, t-upright and terminal e-like loop survive, but the low letters remain obscured.'},
 {'place':'Rounded extension-group glyph','crop':prefix+'lower_group_maps.png','question':'No explicit identifying name appears; the shared E/Sigma uncertainty remains.'}
],
'raw_difference_disposition':'All packet differences were inspected against the original and both full-resolution halves, and every word/sign/index/deletion/mark was read even where the witnesses agree. All ten subscript-versus-superscript differences are covered in the six separate equation rows. Material prose, abbreviation, punctuation, deletion-state, connector and glyph differences are listed above. H editorial notes, page wrappers, array/aligned/gathered choices, line breaks, and font wrappers encoding the same handwritten Y/B or the already-established mathfrak X convention were excluded as markup-only differences. Certainty-only resolutions are separately recorded for all four packet marks. Eight unique crops were inspected, one per unresolved place or compact expression; no other page, web research, OCR or TeX compilation was used.'
}
path=root/'reviews'/'143_scan014_readerB.json'
path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
required=['key','reader','stage','image_views','changes','decisions','inventory','remaining_doubts','certainty_resolutions','notation','abbreviations','hand_log','notes','check_events','unresolved_for_main','raw_difference_disposition']
assert all(k in report for k in required)
assert [d['id'] for d in report['decisions']]==['M0670','M0671','M0672','M0673']
print(f'Wrote {path}; {len(changes)} changes; {len(report["inventory"])} inventory elements; all required fields and four packet decisions present. No compilation.')
