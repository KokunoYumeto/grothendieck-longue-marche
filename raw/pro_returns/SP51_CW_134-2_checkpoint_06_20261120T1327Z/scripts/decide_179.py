from decision_helpers import *
import copy
r=load_reports(179)
diffs=[row(r,'A',i) for i in range(16)]
cm={0:'C/l1_cancelled_morp.png',1:'B/L1_article_after_fleches.png',2:'B/L2_diagrammes_ending.png',3:'C/l4_overwritten_article.png',4:'C/l5_opening_brackets.png',5:'C/l9_elementaire_ending.png',6:'C/l9_elementaire_ending.png',7:'C/l9_cancelled_and_inserted_words.png',8:'C/l9_cancelled_and_inserted_words.png',9:'C/l14_closing_marks.png',10:'C/l14_closing_marks.png',11:'C/l14_reconstitue_accent.png',12:'C/l20_finis_insertion.png',13:'C/l20_precise_ending.png',14:'C/l22_partition_capital.png',15:'A/l22_second_P.png'}
for i,p in cm.items():diffs[i]['crop']='crops/scan179/'+p
diffs[1].update(final='des',differs_C=True,differs_H=False,evidence='The d bowl and rising stroke are followed by a small e return and a long s ending with a downward hook. Root selects B over C’s du and A’s retained alternative. The separately read noun ending does not govern this article.',confidence='high')
diffs[2]['evidence']+=' Root selects A/C over B: the final small rise flows into a horizontal exit, with no separate low s-hook. The distinct s-hooks in L18–L19 are inspected independently in crops/scan179/B/L19_terminal_punctuation.png. The resulting des diagramme is preserved without grammatical repair.'
diffs[2]['confidence']='medium'
diffs[3]['evidence']+=' Root selects A/B’s preferred order, while retaining the opposite order as alternatives: the broad dark high loop is more l-like, and the small broken left bowl is lighter. The chronological assignment remains uncertain.'
diffs[4]['evidence']=diffs[4]['evidence'].replace('The top half shows','The main crop shows')
diffs[5]['evidence']+=' Root selects A’s resolved plural over B/C’s retained singular alternative: the low final e trail and the following descending s-hook are separately visible; the comma is farther right and lower.'
diffs[6]['final']="``…''"
diffs[8]['evidence']+=' Root includes the whole visibly raised run in the insertion. The cancellation lies on the ordinary baseline below it; no separate destination for toutes is visible. This physical grouping does not assert an order of pen strokes.'
diffs[12]['evidence']+=' Root selects A/B’s doubt over C’s resolution: the final gray curve remains broken and weak.'
diffs[13]['evidence']+=' Root selects A’s first candidate, retains C’s précisée as the alternative, and rejects B’s unaccented précise alternative because the terminal acute is distinct.'
diffs[14]['kind']='other'
comparisons=[
 {'place':'L1 article after flèches','A':'des / du retained','B':'des resolved','C':'du resolved','decision':'Select B: d bowl, small e return and a long s with a downward terminal hook are visible. The following noun was decided separately (B/L1_article_after_fleches.png).'},
 {'place':'L2 diagramme(s)','A':'diagramme','B':'diagrammes','C':'diagramme','decision':'Select A/C. The low final rise has one horizontal exit, without the separate lower hook visible on the actual terminal s-forms at L18–L19. Preserve des diagramme without grammatical repair (B/L2_diagrammes_ending.png; B/L19_terminal_punctuation.png).'},
 {'place':'L4 overwritten article','A':'underlying des/les; live les/des','B':'underlying des/les; live les/des','C':'underlying les/des; live des/les','decision':'Prefer A/B: the darker broad high loop is l-like; the smaller broken left bowl favours an older d. Both readings remain alternatives for both layers, because the actual writing sequence cannot be securely separated (C/l4_overwritten_article.png).'},
 {'place':'L9 élémentaire(s)','A':'élémentaires resolved','B':'élémentaires / élémentaire retained','C':'élémentaires / élémentaire retained','decision':'Select A. A separate descending hooked s follows the pale low e trail and precedes the paired high quotation ticks. It is distinct from the later comma (C/l9_elementaire_ending.png).'},
 {'place':'L9a insertion scope of toutes','A':'included in the raised replacement','B':'included, but alternative baseline attachment retained','C':'included in the raised replacement','decision':'Select A/C’s grouping. The word continues the raised run, descending toward the live baseline les, above the cancellation. No separate lower destination is indicated. Its letters remain doubtful, but the physical replacement group is preserved as one insertion (C/l9_cancelled_and_inserted_words.png).'},
 {'place':'L20a finis','A':'one-reading doubt','B':'one-reading doubt','C':'resolved finis','decision':'Retain A/B. The f and dotted positions are clearer than the fragmented gray middle and terminal s; no competing word is invented (C/l20_finis_insertion.png).'},
 {'place':'L20 adjective ending','A':'précisé / précisée','B':'précisée / précise','C':'précisée / précisé','decision':'Select A’s preferred order. A single final open e-body is clearer than an additional e; the final acute excludes unaccented précise, while compressed exit strokes still allow précisée (C/l20_precise_ending.png).'},
 {'place':'L18 comma alleged in C line-coverage ledger','A':'no comma','B':'no comma','C':'final reading has no comma; coverage entry says final comma','decision':'No comma. The terminal stroke belongs to the final s, with no independent punctuation after it; the next line’s s is likewise distinct. Treat C’s coverage sentence as a reporting inconsistency, not a new manuscript mark (B/L19_terminal_punctuation.png).'},
 {'place':'Inventory treatment of overwriting','A':'one record for each overwritten article/delimiter site','B':'separate underlying and live inventory rows, live layers classified as insertions','C':'one record for each overwritten article/delimiter site','decision':'Use A/C’s combined-site inventory, documenting both live and superseded forms within each entry. The text keeps deleted old forms followed by live replacements; no extra insertion wrappers or independent new objects are inferred.'}
]
unresolved=copy.deepcopy(r['A']['unresolved'])
unresolved=[u for u in unresolved if u['place']!='L1, article after flèches']
uc=['C/l1_cancelled_morp.png','C/l4_overwritten_article.png','C/l4_overwritten_article.png','C/l9_cancelled_and_inserted_words.png','C/l9_cancelled_and_inserted_words.png','C/l20_finis_insertion.png','C/l20_precise_ending.png','C/l22_partition_capital.png']
for u,p in zip(unresolved,uc):u['crop']='crops/scan179/'+p
review=[]
qc={1:'C/l1_cancelled_morp.png',2:'C/l4_overwritten_article.png',3:'C/l4_overwritten_article.png',4:'C/l9_cancelled_and_inserted_words.png',5:'C/l9_cancelled_and_inserted_words.png',6:'C/l9_cancelled_and_inserted_words.png',7:'C/l22_partition_capital.png',9:'C/l5_opening_brackets.png',10:'C/l20_precise_ending.png',11:'C/l22_partition_capital.png'}
for i,q in enumerate(r['A']['C_doubt_review'],1):
 ev=q['evidence']
 if i in [2,3]:ev=diffs[3]['evidence']
 if i==6:ev=diffs[8]['evidence']
 if i==7:ev+=' Main independently inspected the second form in crops/scan179/A/l22_second_P.png.'
 if i==9:ev+=' Main inspected the replacement in crops/scan179/C/l9_cancelled_and_inserted_words.png and the closing marks in crops/scan179/C/l14_closing_marks.png.'
 if i==10:ev=diffs[13]['evidence']+' Added finis remains doubtful; main inspected crops/scan179/C/l20_finis_insertion.png. The hyphen and inserted X are confirmed by all three half readings.'
 if i==11:ev+=' The second form is independently confirmed in crops/scan179/A/l22_second_P.png.'
 if i in qc:ev+=' Main inspected crops/scan179/'+qc[i]+'.'
 else:ev+=' All three independent full-resolution half readings agree.'
 review.append({'place':q['question'],'earlier':q['question'],'decision':q['decision']+': '+q['final'],'evidence':ev})
inv=copy.deepcopy(r['A']['inventory'])
notes=r'''**S179-notes.** The page continues the description of diagrams whose spaces are manifolds with boundary. Their arrows are said to be “pour l'essentiel” locally trivial fibrations between such manifolds, with manifolds with boundary as fibres, and boundary inclusions. A bracketed qualification beginning “en fait” allows “des inclusions légèrement plus générales”: boundaries may have an elementary cellular decomposition whose closed strata are again manifolds with boundary, glued along common boundary portions. The author also includes inclusions among these pieces. These are source assertions; no construction or proof is supplied on this sheet.

Reconstruction of the space “par recollement” is asserted, followed by a canonical description-dévissage of compact moderate spaces, “éventuellement munis” of equisingular stratifications with nonsingular strata, through diagrams of the stated sort. The qualifier finis is visibly inserted but its last letters remain an editorial reading doubt. The last sentence starts the application to P-constructible sheaves, complexes and n-champs for a fixed stratification and continues after dont il at the foot. No continuation is supplied here. There is no explicit authorial question or confession of uncertainty on this page.

All three readers report no mathematical proof, computation or local type deduction; their check_events arrays are empty. Reading the geometric claims and identifying X, n and the partition capitals was visual transcription. No expected grammatical or mathematical form settled a doubtful word. The final text preserves **des diagramme**: the article crop supports des, while the noun crop lacks a separate final s-hook. It also preserves the quoted plural **élémentaires** despite singular cellulaire. The adjective after de nature is **précisé/précisée**, with the final acute visible and the vowel count unresolved.

The overwritten article is represented with underlying des/les and live les/des. These are preferred visual layers, not a secure chronology: the dark large high loop favours l, while the paler small left bowl favours d. Both alternatives remain. The raised phrase i.e. dont toutes forms one replacement above the cancelled baseline en cellules/éléments. Dont and cancelled en resolve; toutes and the cancelled noun remain doubtful. Both curved original parentheses are preserved beneath the square bracket replacements, and four points precede the closing mark. The accent in réconstitue is retained. The two partition capitals were independently inspected and use calligraphic P as the preferred alphabet, with plain P retained at the first occurrence.

There are 24 main baselines and seven attached additions. This is one continuing prose paragraph; En d'autres termes begins within L15, with no new paragraph cue. The only underline is the single rule under et; long rules at par recollement and the sheaf alternatives are attachment guides. No diagram, display, independent margin annotation, nontext drawing or footnote occurs. The sheet carries author page **34** and archive pencil **179**, with no date, title, closing or signature. C's reader coverage ledger alone mentions a comma after équisingulières, while its complete reading omits it; root inspected the saved crop and found only the terminal s. No extra comma was introduced. Supplied references to an English version were not consulted or used.
'''
text=(ROOT/'records/scan179/A/reading.tex').read_text().replace(r'flèches \unsure{des|du}', 'flèches des')
viewed=['C/l1_cancelled_morp.png','B/L1_article_after_fleches.png','B/L2_diagrammes_ending.png','C/l4_overwritten_article.png','C/l5_opening_brackets.png','C/l9_elementaire_ending.png','C/l9_cancelled_and_inserted_words.png','C/l14_closing_marks.png','C/l14_reconstitue_accent.png','C/l20_finis_insertion.png','C/l20_precise_ending.png','C/l22_partition_capital.png','A/l22_second_P.png','B/L19_terminal_punctuation.png']
d=write_decision(179,'A',[],diffs,comparisons,unresolved,inv,notes,r['A']['abbreviations'],review,['crops/scan179/'+p for p in viewed],brief='briefs/brief_v10_scan179.md',workflow_note='Three fresh independent readers each inspected whole/a/b once and covered 24 main baselines, seven additions and all 11 C questions. A made 14 crops, B 13, C 11. Main read all three complete readings and every report section before adjudicating, reused 14 saved crops and made no new crop. Every successful root inspection occurred once; there was no failed display or recropping. Article, noun ending, overwritten layers, plural ending, insertion scope, finis, terminal accent/vowel count, both P forms and the C coverage comma inconsistency were decided on these crops. All three report only structural text validation and no mathematical proof or TeX operation.',text_override=text)
by={}
for rep in r.values():
 for c in rep['crops']:by[c.get('path',c.get('crop',''))]=c.get('bbox')
for x in d['differences']:
 cp=x['crop'];m=(ROOT/cp).with_suffix('.json');box=json.loads(m.read_text()).get('bbox') if m.exists() else by.get(cp)
 if box:
  if x.get('bbox')!=box:x['reader_report_bbox']=x.get('bbox')
  x['bbox']=box
(ROOT/'records/scan179/decision.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
add_notation([
 ('Partition capital',r'\unsure{\mathcal P|P}, then \mathcal P','179 L22: each occurrence has a full long returning oval and bowed upper arm, independently inspected. Same preferred calligraphic family, with print-alphabet doubt retained.'),
 ('Overwritten articles','underlying des/les; live les/des','179 L4: preferred dark high l-like loop and lighter low d-like bowl. Layer chronology is uncertain and both orders remain supported; do not normalize by grammar.'),
 ('Four-point close',r'\ldots.\deleted{)}]','179 L14: four distinct short horizontal points; a curved parenthesis survives inside an angular bracket. No separate syntactic role is assigned to point four.'),
 ('Literal word endings',r'des diagramme; élémentaires; \unsure{précisé|précisée}','179 L1–L2/L9/L20: article, noun and adjective endings are each read independently; grammatical agreement does not supply missing strokes.'),
 ('Abbreviation stops','loc.; i.e.; sing.','179 L3/L9a/L19: stops visible after loc and sing and both i.e. letters. Cancelled morp/morph is not expanded in the text.')
])
register_note_statements(179,[
 {'place':'L1–L5; notes paragraph 1','statement':'Diagram spaces are manifolds with boundary and the arrows chiefly locally trivial fibrations and boundary inclusions.'},
 {'place':'L5–L14; notes paragraph 1','statement':'The qualification allows elementary cellular pieces whose closed strata are manifolds with boundary glued along common boundary parts, together with inclusions among the pieces.'},
 {'place':'L14–L21; notes paragraph 2','statement':'Reconstruction by gluing and a canonical description-dévissage of compact moderate spaces by finite diagrams of the stated kind are asserted; the word finis has a reading doubt.'},
 {'place':'L21–L24; notes paragraph 2','statement':'The author begins an application to constructible sheaves, complexes and n-champs for a fixed stratification; the sentence is incomplete on this sheet.'}
])
