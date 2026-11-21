from pathlib import Path
import json
root=Path('/workspace/scratch/f28c4f52d3ec');page='148_scan065'
boxes=json.loads((root/f'proposed/{page}_crop_boxes.json').read_text())
changes=[]
def change(place,c,h,final,diff_c,diff_h,kind,error_kind,evidence,crop,confidence='high',marked_in_h=False,consequential=False):
 changes.append(dict(id=f'{page}-{len(changes)+1:02d}',place=place,c=c,h=h,final=final,diff_c=diff_c,diff_h=diff_h,kind=kind,error_kind=error_kind,evidence=evidence,crop=f'crops/{page}_{crop}.png',box=boxes[crop],confidence=confidence,marked_in_h=marked_in_h,consequential=consequential))
change('Quotation marks around the first modèle',"``modèle''",'« modèle »',"``modèle''",False,True,'misread symbol or index','Other','Both ends have paired short raised pen ticks, joined in a shallow u-like shape; there are no opposing angle-shaped guillemets. The word has a visible accent stroke.','quoted_modele')
change('Raised parenthetical words',r'\inserted{(moyennant déformations)}',r'(\ill{} \ill{})',r'\inserted{(moyennant déformations)}',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','Inside the round parentheses the first run has the low m/o/y/en/nant sequence. The second has the initial d loop, accented e, descending f and the tall t before the low ions ending. Both words are legible at crop scale.','parenthesis_cordes')
change('Insertion state of the parenthesis',r'\inserted{(moyennant déformations)}',r'(\ill{} \ill{})',r'\inserted{(moyennant déformations)}',False,True,'insertion or placement','Insertions put in the wrong place','The smaller parenthetical row is placed above the full-size underlined toutes les cordes, between that row and the preceding line. It qualifies the containment statement before toutes.','parenthesis_cordes')
change('Article before foulée','la','le',r'\unsure{la|le}',False,True,'misread word','Words','A looped l is followed by one long low exit and a downward terminal hook. The a/e distinction is not independently clear in that flat run; la is retained first, with le kept explicitly.','la','medium')
change('Opening words of the lower main row','foulée, avec',r'\ill{}, \ill{}','foulée, avec',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','Foulée has a tall crossed f with descender, low ou, a looped l and a distinct accent above the first e; a separate comma follows. Avec is the adjacent low a/v/e/c run.','foulee_avec')
change('Article and number of the main modèle',r'\unsure{les modèles|le modèle}',r'le \uncertain{modèle}','le modèle',True,False,'misread word','Words','The article has one l loop and e exit without a separate s. The noun ends in l followed by one short e hook. The extra final s seen in the inserted modèles below is absent from this upper occurrence.','model_clause_insertion_pi',marked_in_h=True)
change('Words between le modèle and desire',"qu'on",r'\ill{}',"qu'on",False,True,r'readable ink left as \ill{}','Readable ink left as illegible','The q has a closed upper bowl and long descender; the following u is followed by a separate apostrophe and the low o/n run.','model_clause_insertion_pi')
change('Verb after qu’on',r'\unsure{désire|cherche}',r'\ill{}','desire',True,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','The opening is a looped d, not c/h; the later i has a separate dot and the last r/e run ends in a hook. No separate accent stroke is visible above the first e within the ample crop. The literal unaccented desire is retained.','model_clause_insertion_pi')
change('Punctuation after desire',r'\unsure{désire|cherche},',r'\ill{}','desire',True,False,'text not on the page','Text that is not on the page','The last e ends in a downward finishing hook, followed by blank paper. There is no independent comma after the word.','model_clause_insertion_pi')
change('Lower folio annotation',r'\mspage{64}','absent',r'\mspage{64}',False,True,'omission','Omissions','The first digit has a closed lower bowl on a curved 6 stem. The second has an upright left stroke, a cross-stroke and a separate descending right stem, giving 4. No attribution is inferred from the pale appearance.','lower_number')

def decision(i,which,reading,evidence,crop,confidence='high'):
 return dict(id=i,decision=which,reading=reading,evidence=evidence,crop=f'crops/{page}_{crop}.png',box=boxes[crop],confidence=confidence)
decisions=[
 decision('M0781','first','cordes','The word has an open c followed by closed o, a low r, and a tall looped d before the final e/s. The d is not a crossed t, so cartes is excluded.','parenthesis_cordes'),
 decision('M0782','alternative','le modèle','The article has no separate s; the upper noun lacks the additional final s that is visibly present in the inserted modèles below.','model_clause_insertion_pi'),
 decision('M0783','other','desire','The d opening and dotted i exclude cherche. No detached accent is visible above the first e, so the word is preserved without C’s supplied acute accent.','model_clause_insertion_pi'),
]
implicit_decisions=[decision('I01','undecided',r'\unsure{la|le}','The letter after the l is reduced to a flat connected stroke and terminal hook; the a/e distinction remains open.','la','medium')]
doubts=[dict(place='Article before foulée',reading='la',alternatives='le',confidence='medium',reason='The looped l is clear, but the connected final a/e run is too flat to decide independently. The grammar has not been used to force it.')]
inventory=[
 dict(element='E01',sheet_kind='text',hand='his hand',kind='text',position='Top centre',first_words_or_objects='21',transcribed='yes'),
 dict(element='E02',sheet_kind='text',hand='his hand',kind='text',position='Opening main paragraph, three full-size baseline rows',first_words_or_objects='elle exigerait d’avoir un modèle',transcribed='yes'),
 dict(element='E03',sheet_kind='text',hand='his hand',kind='insertion',position='Smaller row above the underlined phrase',first_words_or_objects='(moyennant déformations)',transcribed='yes'),
 dict(element='E04',sheet_kind='text',hand='his hand',kind='text',position='Third full-size row, two underline segments',first_words_or_objects='toutes les cordes',transcribed='yes'),
 dict(element='E05',sheet_kind='text',hand='his hand',kind='text',position='Second paragraph, five full-size rows',first_words_or_objects='Mais quand même on doit pouvoir',transcribed='yes'),
 dict(element='E06',sheet_kind='text',hand='his hand',kind='insertion',position='Above the gap between des and Pi-one, with curved attachment stroke',first_words_or_objects='modèles des',transcribed='yes'),
 dict(element='E07',sheet_kind='text',hand='unnamed hand (folio annotation; attribution uncertain)',kind='text',position='Pale lower left folio annotation',first_words_or_objects='64',transcribed='yes'),
]
notes=[
 dict(id=f'{page}-N01',text='The first paragraph says that the contemplated model for S T-top plus/minus would have to be large enough to contain all chords, allowing deformations, and remarks on its size. The second expects that, alongside the desired S T D-top model, one can determine models for Pi-one(X,R) and their functorial dependence on (X,R). This is a proposed construction programme; the page supplies no construction or proof.'),
 dict(id=f'{page}-N02',text='The capital Pi with subscript 1 is read in the usual fundamental-groupoid sense for a space X with designated points R. This is interpretive background for the final clause, not an independently proved claim on this sheet. The capital Pi, the numeric 1, both pair entries and the parentheses were checked together in the complete formula.'),
 dict(id=f'{page}-N03',text='H appends a heading beginning Découpage de cartes en “pantalons” généralisés, followed by its own explanation associating that title with a cover. No such heading is present anywhere on this supplied leaf. The appended material is treated as a source-page mismatch and is excluded from both the transcription and the count of current-leaf reading corrections. No other leaf was consulted.'),
 dict(id=f'{page}-N04',text='Both category superscripts are plus/minus. In the first occurrence the plus and its lower minus are separate; in the later occurrence the upright reaches between the two bars, producing an I-like form. The apparent possibility of a plain plus at first view was settled by the full formula crop; neither witness needs a correction there.'),
 dict(id=f'{page}-N05',text='The source writes singular le modèle in the main clause and plural modèles in the later insertion. The word desire has no visible acute accent, and no independent comma follows it. The two underline segments beneath toutes and les cordes are retained. The curved attachment around modèles des points into the gap after the live des and before Pi-one; it does not cancel either des.'),
 dict(id=f'{page}-N06',text='The head numeral is 21 and the pale lower folio is 64. The lower annotation is assigned to an unnamed hand with attribution uncertain. Apart from that folio, the lower prepared half is blank; fine incidental sheet traces are not treated as text or diagrams.'),
]
check_events=[
 dict(statement_id=f'{page}-N01',type='carried as background without fault found',outcome='The proposed modelling programme was transcribed and its two paragraphs interpreted. No proof of existence, functoriality or compatibility with chord deformations was performed.'),
 dict(statement_id=f'{page}-N02',type='carried as background without fault found',outcome='The standard fundamental-groupoid interpretation was carried as background. Visual confirmation of capital Pi and index 1 is not a mathematical proof check or a formal certificate.'),
]
notation=[
 dict(sign=r'\pm',meaning_or_form='The first occurrence has a distinct plus above a detached lower bar; the second has an upright joining two bars, resembling capital I.',places='S T-top in the first paragraph; S T D-top in the second',universality='Both occurrences on this sheet were checked independently on complete formula crops.',witness_errors='Neither witness is wrong at these signs; the initially open plain-plus possibility is excluded by the visible lower bar.'),
 dict(sign=r'\Pi_1',meaning_or_form='Two tall straight uprights joined by an upper bar form capital Pi; a smaller capped upright below the right side is the numeral 1.',places='Pi-one(X,R) following the insertion modèles des',universality='One occurrence on this sheet.',witness_errors='Both witnesses preserve the capital Pi and numeric index; the whole formula was checked rather than inferred from the context.'),
 dict(sign='Terminal singular/plural ending',meaning_or_form='The main modèle ends in one short e hook; inserted modèles has an additional distinct final s turn.',places='le modèle qu’on desire; inserted modèles des',universality='The two occurrences are different and are preserved separately.',witness_errors='C leads with the plural les modèles in the main clause; the crop supports singular le modèle.'),
 dict(sign='Curved insertion connector',meaning_or_form='A broad curve beneath the raised words turns downward at its middle to the gap after des and before Pi-one.',places='Insertion modèles des',universality='One insertion attachment on this sheet; the smaller parenthetical insertion has no equivalent connector.',witness_errors='Both witnesses locate the words as inserted; the scan confirms that the live baseline des survives.'),
 dict(sign='la / le',meaning_or_form='A large l loop joins a long flat exit with a terminal hook, leaving the following a/e distinction uncertain.',places='Before foulée',universality='This ambiguity is local; the separately cropped le before modèle is not treated as the same unresolved occurrence.',witness_errors='C gives la and H le; both remain explicitly represented.'),
]
abbreviations=[dict(form='top',expansion='topologique')]
second_boxes=[]
def audit(kind,box,reading):
 second_boxes.append(dict(box=f'B{len(second_boxes)+1:02d}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
audit('handwritten number',[802,25,888,83],r'\mspage{21}')
audit('different words',boxes['quoted_modele'],"``modèle''")
audit('doubtful formula',boxes['first_formula'],r'$S\mathcal T_{\mathrm{top}}^\pm$')
audit('insertion',boxes['parenthesis_cordes'],r'\inserted{(moyennant déformations)} \uline{toutes} \uline{les cordes}')
audit('different words',boxes['la'],r'\unsure{la|le}')
audit('insertion',[285,630,1635,1048],r"foulée, avec le modèle qu'on desire pour $S\mathcal TD_{\mathrm{top}}^\pm$, des \inserted{modèles des} $\Pi_1(X,R)$, et leur dépendance fonctorielle en $(X,R)$\ldots")
audit('handwritten number',boxes['lower_number'],r'\mspage{64}')
agreed_ink_checks=[
 dict(place='Complete first category formula',reading=r'S\mathcal T_{\mathrm{top}}^\pm',evidence='The plus has a detached, clearly inked horizontal bar below it; S, calligraphic T and the small t/o/p subscript were read together.',crop=f'crops/{page}_first_formula.png',box=boxes['first_formula'],confidence='high'),
 dict(place='Complete second category formula',reading=r'S\mathcal TD_{\mathrm{top}}^\pm',evidence='S, calligraphic T and a separate full-height D precede the t/o/p subscript. The exponent has an upright between two horizontal bars.',crop=f'crops/{page}_second_formula.png',box=boxes['second_formula'],confidence='high'),
 dict(place='Inserted models and complete Pi-one expression',reading=r"des \inserted{modèles des} $\Pi_1(X,R)$, et leur",evidence='The raised words stand above a curved attachment into the gap after live des. Capital Pi has two straight uprights and an upper bar; the one index, X, comma, R, parentheses and following comma are clear.',crop=f'crops/{page}_model_clause_insertion_pi.png',box=boxes['model_clause_insertion_pi'],confidence='high'),
]
obj=dict(page=page,reader='reader_c',lines_read=12,line_count_note='Eight full-size body rows, two separate insertion rows and two numeral-only rows were read; the remainder of the lower half is blank.',changes=changes,decisions=decisions,implicit_decisions=implicit_decisions,doubts=doubts,inventory=inventory,notes=notes,check_events=check_events,notation=notation,abbreviations=abbreviations,second_boxes=second_boxes,agreed_ink_checks=agreed_ink_checks)
(root/f'proposed/{page}.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print(f'{len(changes)} material rows; {len(decisions)} supplied marks; {len(implicit_decisions)} implicit decisions; {len(doubts)} doubts; {len(inventory)} inventory elements; {len(second_boxes)} audit units.')
