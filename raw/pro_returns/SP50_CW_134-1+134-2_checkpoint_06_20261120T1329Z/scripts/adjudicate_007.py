from pathlib import Path
import copy,json

O=Path(__file__).resolve().parents[1]; K='134-1_scan007'
R={r:json.loads((O/'readers'/K/r/'report.json').read_text()) for r in ['r1','r2','r3']}
d=copy.deepcopy(R['r1'])
d.update(adjudication_complete=True,brief='v04',readers=['/root/s007_r1','/root/s007_r2','/root/s007_r3'])
t=(O/'readers'/K/'r1/reading.tex').read_text()
t=t.replace(r'\unsure{v.|t.|r.} f.', 'v. f.')
t=t.replace(r'\inserted{(p ex.),}',r'\inserted{(\unsure{p|par} ex.)\unsure{!|;|,}}')
t=t.replace(r'\unsure{T|J}',r'\unsure{J|T}')
t=t.replace("des variantes ``",r"des \unsure{variantes|variante} ``")
t=t.replace('% Two curved impressions', '% Isolated raised points above the question sequence label and between ils and connu have no established textual function.\n% Two curved impressions')
(O/'pages/H134-01_134-1_scan007.tex').write_text(t)

mp={1:'r1/01_clipped_opening',2:'r1/01_clipped_opening',3:'r1/01_clipped_opening',4:'r1/01_clipped_opening',5:'r1/03_module_A',6:'r1/02_les_punctuation',9:'r1/04_abbreviation_insertion',10:'r1/04_abbreviation_insertion',11:'r1/04_abbreviation_insertion',12:'r1/04_abbreviation_insertion',13:'r1/04_abbreviation_insertion',14:'r2/03_split_construction_and_fourni',15:'r2/03_split_construction_and_fourni',16:'r2/03_split_construction_and_fourni',17:'r1/06_epingle_accent',18:'r1/07_deleted_word',19:'r1/08_middle_term',20:'r1/08_middle_term',21:'main/middle_continuation',23:'r1/09_fonctorialites',25:'r1/10_triangle_et',26:'r1/10_triangle_et',27:'r2/08_exact_sequence_label',28:'main/sont_ils',29:'r1/12_connu',30:'r1/12_connu',31:'r1/13_competences',32:'r1/13_competences',33:'r2/09_connu',34:'r1/14_connaissent',35:'r1/15_variantes',36:'main/superieures_quotes',37:'main/geometrique_quotes',38:'main/pour_en',40:'r1/16_nec',41:'main/folio64'}
for n,x in enumerate(d['changes'],1):
    x['id']=f'{K}.{n:02d}'
    if n in mp:
        x['crop']=f'evidence/{K}/{mp[n]}.jpg'
        x['decision']='The main reader inspected this crop and accepts the recorded reading and state.'
    else:
        x['decision']='All three independent readers agree on this feature, checked on the supplied half; no further crop was required.'
def ch(n,**kw):d['changes'][n-1].update(kw)
ch(6,readers={'r1':'les','r2':'les','r3':r'\unsure{les|les,}'},decision='The detached terminal hook is the s after l and e. No separate further s supports an added comma. Retain les without new punctuation.')
ch(9,against_h=False,decision='The preposition is readable; its H difference is counted once with the whole unreadable span in entry 10, rather than twice for one H placeholder.')
ch(10,location='de and abbreviated qualification after projectifs',c=r'de \unsure{v.|t.|r.} f.',h=r'\ill{}',final='de v. f.',against_c=True,against_h=True,confidence='medium',readers={'r1':r'de \unsure{v.|t.|r.} f.','r2':r'de \unsure{v.|t.|r.} f.','r3':'de v. f.'},evidence='The preposition has a looped d and low e. The first abbreviated letter has a clear V-shaped trough, an oblique descending left stroke and upright right return, without a t crossbar or r shoulder. Separate stops and the following f are visible.',decision='Resolve the literal abbreviated letters to v. f., accepting r3. Do not replace them with a conventional mathematical abbreviation or expand them in the text.')
ch(11,final=r'\unsure{p|par}',against_c=False,against_h=True,confidence='medium',readers={'r1':'p','r2':r'\unsure{p|par}','r3':r'\unsure{p|par}'},evidence='The descending p stem has a low joined tail before ex.; compressed a-r cannot be excluded inside that tail. There is no independent stop after p.',decision='Retain p first and par as an alternative; reject the fully resolved p of r1 and the added stop in H.')
ch(12,c='interlinear insertion',h='inline parenthesis without insertion state',final='interlinear insertion',decision='The raised parenthesis and guide establish insertion. Wording and punctuation are counted separately in entries 11 and 13, avoiding duplicate C counts.')
ch(13,final=r'\unsure{!|;|,} after the closing parenthesis',against_c=True,against_h=True,confidence='low',readers={'r1':',','r2':r'\unsure{,|;|!}','r3':','},evidence='A long upper stroke and a detached lower component follow the closing parenthesis. The upper stroke is relatively upright; the lower component and nearby copying flecks leave a broken semicolon or comma possible.',decision='Put the exclamation mark first from the two-part vertical form, retain semicolon and comma alternatives, and do not substitute H’s period.')
ch(15,evidence='The end-of-line letters begin constru-; the next line contributes the short -ion continuation. Both line ends are visible in the selected wide crop. The interior joins remain compressed.',decision='Retain construction with C’s doubt. The H word raisonnement is not supported by the visible sequence.')
ch(16,decision='The final dotted i and low exit are visible without a final t ascender or r. Resolve to fourni, preserving the written grammatical slip.')
ch(17,readers={'r1':r'\unsure{e|é}pinglé','r2':'épinglé','r3':'épinglé'},decision='No independent acute can be isolated above the initial vowel, although it could be fused with the upper loop. The final é has a separate acute. Retain the new initial-accent uncertainty, unaccented e first.')
ch(20,crop=f'evidence/{K}/r1/08_middle_term.jpg; evidence/{K}/main/middle_continuation.jpg',evidence='N is followed by the copied right edge without a closing parenthesis. The next line starts with de and the separate (*) reference, with no postponed closer.',decision='Retain the visibly unclosed argument list. Both sides of the line break were inspected; the parenthesis supplied by H is not imported.')
ch(25,final=r'(\unsure{J|T})',against_c=True,against_h=True,confidence='medium',readers={'r1':r'(\unsure{T|J})','r2':r'(\unsure{T|J})','r3':r'(\unsure{T|J})'},evidence='The upper bar lies predominantly right of the descending stem and the foot curls strongly left. These are J-like features; a hooked T remains possible.',decision='Reverse the preference to J first from the local strokes. The earlier triangle label does not overrule this occurrence.',math_consequential=True,consequence='The exact-triangle reference remains ambiguous, with J now preferred visually over T; the contextual expectation T is retained only as an alternative.')
ch(28,evidence='The end of sont and beginning of ils are separated by blank baseline space; there is no intervening horizontal hyphen.',decision='Keep the literal sont ils against H’s supplied hyphen.')
ch(30,final='comment: raised point, no established textual function',readers={'r1':'no additional punctuation','r2':'no additional punctuation','r3':'comment: raised point; intentional status uncertain'},decision='The high isolated point has no paired baseline mark. Preserve the observation in a neutral comment without creating punctuation or counting a word omission.')
ch(31,readers={'r1':'...tences','r2':'...tences','r3':'...tences'},decision='The open c-like bowl and following low e and terminal s settle the noun ending. The accent is a separate feature in entry 32.')
ch(32,readers={'r1':r'\unsure{è|é}','r2':'é','r3':r'\unsure{è|é}'},decision='The short accent slopes down to the right, favouring grave, but its thickness prevents certainty. Keep the two accents in place; ordinary spelling does not choose.')
ch(33,crop=f'evidence/{K}/r2/09_connu.jpg; evidence/{K}/main/illusie_start.jpg',evidence='The low exit after Breen has no detached comma. The following line starts directly with the capital I of Illusie, followed by the name and three points.',decision='Keep Breen Illusie without adding the comma in H. Both sides of the line break were inspected.')
ch(35,final=r'\unsure{variantes|variante}',against_c=False,against_h=True,confidence='medium',readers={'r1':'variantes','r2':r'\unsure{variantes|variante}','r3':r'\unsure{variantes|variante}'},evidence='The end of the word is a flat joined run ending in a hook; an independent final s cannot be separated securely.',decision='Retain C’s ending uncertainty, rejecting r1’s resolution to the plural.')
ch(36,evidence='Two short high strokes open and close the word; they are comma-like quotation marks without angle shapes.')
ch(37,evidence='The opening pair is partly joined and the closing pair consists of two high strokes; neither has a guillemet angle shape.')
ch(38,evidence='A low e-like entry runs into the n rise and terminal return. There is no tall l ascender at the beginning.',decision='Retain en from the strokes against H’s les.')
ch(40,decision='The n, accented e, open c and detached stop are individually visible. Resolve néc. without expanding it.')
ch(41,evidence='The light lower-left pencil numerals are a looped 6 and an open 4 with horizontal cross-stroke.',decision='Keep archive foliation 64 as a comment, not an author manuscript page number.')
extra=copy.deepcopy(next(x for x in R['r3']['changes'] if x['id']=='s007-r3-31'))
extra.update(id=f'{K}.42',crop=f'evidence/{K}/r2/08_exact_sequence_label.jpg',readers={'r1':'no additional exponent or punctuation','r2':'no additional exponent or punctuation','r3':'comment: raised point; intentional status uncertain'},decision='A raised point is visible, but no textual attachment is established. Preserve the physical observation in a neutral comment; do not add an exponent.')
d['changes'].append(extra)
d['main_viewed']=list(dict.fromkeys(p.strip() for x in d['changes'] for p in x['crop'].split(';') if p.strip().startswith('evidence/')))

d['doubts']=[x for x in d['doubts'] if x['location']!='Abbreviation before the inserted parenthesis']
for x in d['doubts']:
    x['crop']=x['crop'].removeprefix('out/')
    if x['location']=='Word split between the end of line 5 and start of line 6':
        x.update(crop=f'evidence/{K}/r2/03_split_construction_and_fourni.jpg',reason='Both physical line ends support construction, but compressed internal joins still prevent an entirely certain reading.')
    if x['location']=='Triangle reference in Question':
        x.update(reading='J',alternatives=['T'],reason='A rightward top bar and strongly left-hooked foot favour J; a hooked T remains possible. Context does not settle the letter.')
    if x['location']=='Exact-sequence reference in Question':x['crop']=f'evidence/{K}/r2/08_exact_sequence_label.jpg'
d['doubts'] += [
 dict(location='First word of the interlinear example',reading='p',alternatives=['par'],confidence='medium',reason='The low joined tail after the p stem could contain compressed a-r; no independent stop is visible.',crop=f'evidence/{K}/r1/04_abbreviation_insertion.jpg'),
 dict(location='Punctuation after the inserted example',reading='!',alternatives=[';',','],confidence='low',reason='A long upper stroke and detached lower component favour an exclamation mark, but copying interruption leaves semicolon or comma possible.',crop=f'evidence/{K}/r1/04_abbreviation_insertion.jpg'),
 dict(location='Ending of variantes',reading='variantes',alternatives=['variante'],confidence='medium',reason='The low terminal hook does not independently settle final s.',crop=f'evidence/{K}/r1/15_variantes.jpg')]
for x in d['inventory']:
    x['sheet_kind']='letter'
    if x['hand']=='main manuscript hand':x['hand']='Grothendieck’s hand (continuation of the letter)'
    if x['element']=='Interlinear parenthetical example':x['first_words_or_objects']=r'(\unsure{p|par} ex.)\unsure{!|;|,}'
    if x['element']=='Question paragraph':x['first_words_or_objects']=r'Question : Le triangle exact (\unsure{J|T}) ...'
d['inventory'].append(dict(sheet_kind='letter',hand='unassigned ink or copying traces',element='Two isolated raised points',kind='text',position='Above the question star and between ils and connu',first_words_or_objects='Neutral TeX comment; no established textual function',transcribed='yes'))
d['notes']=r'''**Document and claims (134-1.007.note.document).** This is a handwritten continuation of the letter. It introduces a ring on X and sheaves M,N as K⁰ and K¹ associated to the additive champ of projective modules with the literal abbreviated qualification “v. f.”. It attributes a construction to Mme Sinh and claims that it supplies a Picard champ pinned by M,N and a canonical section of a middle term. “NB” asserts evident functorialities in M,N,X. These are author assertions reported from the page; no construction or functoriality theorem is proved here.

**Questions and qualifications (134-1.007.claim.questions).** Under “Question”, the author asks whether the exact triangle and sequence are known to the named people (Quillen, Breen, Illusie) and whether higher “supérieures” variants are known. The final parenthesis proposes a “géométrique” principle through n-champs de Picard “non néc. stricts”. The interrogative marks and “pourrait” expressly qualify this suggestion. The phrase and abbreviations remain literal in the transcription.

**Mathematics and reading (134-1.007.note.readings).** The clipped first A does not settle its alphabet; the A before Modules is independently visible as calligraphic. The degrees 0 and 1 were separately checked by each reader. The middle-term capital remains P/F, and no closing parenthesis is supplied after N because neither side of the line break shows one. The question’s triangle label has a rightward top bar and strongly leftward foot: J is now preferred to T, with both retained. The clear first star and fused second star were assessed independently; only the latter retains a doubt. No isolated raised point was assigned an exponent. These are reading decisions, not mathematical proof checks.

**Writing states, slips and limits.** The example in parentheses is interlinear, and the word after section is cancelled. “fourni” is resolved from the visible final i without correcting it to fournit. The initial accent in épinglé and the direction of the accent in compétences remain uncertain; the noun ending itself is resolved. “sont ils” has no hyphen, and the ending of connu/connus is not repaired from agreement. The clipped heading, clipped opening verb, several compressed words and tiny insertion punctuation remain doubtful. There is no new date or author page number; the archive pencil foliation is 64, retained only in a comment. Copying traces and two isolated raised points are neutrally recorded without inventing a drawing or textual mark.'''
d['checks']=[
 dict(statement_id='134-1.007.note.document',type='carried as background without fault found',outcome='The page’s document features and author assertions were used to describe it. Inspection establishes the transcription evidence only, not the claimed Sinh construction, section or functorialities.'),
 dict(statement_id='134-1.007.claim.questions',type='carried as background without fault found',outcome='The questions and the modal pourrait were reported as questions and a tentative proposal. No assertion about known higher variants or existence of the suggested n-champs construction was proved or refuted.')]
d['abbreviations']=[dict(abbreviation='Mme',proposed_expansion='Madame'),dict(abbreviation='NB',proposed_expansion='nota bene'),dict(abbreviation=r'\unsure{p|par} ex.',proposed_expansion='par exemple; no separate stop after the initial p is visible'),dict(abbreviation='v. f.',proposed_expansion='Meaning unresolved. A qualification related to finite type may be intended, but neither a conventional expansion nor a change to t. f. is justified by the literal letters.'),dict(abbreviation='néc.',proposed_expansion='nécessairement')]
for k in ['reader','page','started_utc','finished_utc','model','effort','view_log','coverage','notation']:d.pop(k,None)
(O/'decisions'/f'{K}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (O/'notation.md').open('a') as f:
    f.write('| 134-1 / 007 | Ring alphabet | <code>\\unsure{\\mathcal{A}&#124;\\mathscr{A}&#124;A}</code> first; calligraphic A before Modules | The first is clipped; the second independently has a calligraphic flourish. Do not force their evidential certainty to agree. |\n')
    f.write('| 134-1 / 007 | Question triangle label | <code>\\unsure{J&#124;T}</code> | Rightward top bar and left-curled foot favour J in this occurrence, despite the contextual T. |\n')
    f.write('| 134-1 / 007 | Qualification after projectifs | `v. f.` | V-shaped first letter, no t crossbar or r shoulder. Literal reading resolved; meaning remains unclear. |\n')
    f.write('| 134-1 / 007 | First and second star references | First clear; second <code>\\unsure{*}</code> | Second crossing is fused to the parenthesis; a raised speck is not assigned an exponent. |\n')
with (O/'workflow_observations.md').open('a') as f:
    f.write('\n## Scan 007\n\nAll three independent readings were compared before main adjudication. The main reader used seventeen existing reader crops and seven new missing-locus crops, including both sides of the missing parenthesis and name punctuation at line breaks. A truncated tool output did not deliver two requested crops; the same files were then displayed individually, without recropping. The literal abbreviation and final verb were resolved; clipped or fused strokes remained doubtful. Isolated raised points were retained as physical observations without inventing textual function. The brief already covered the relevant disagreements, so v04 remains suitable for the next page.\n')
print('Adjudicated',K,len(d['changes']),'loci',len(d['doubts']),'doubts',len(d['main_viewed']),'main crop views')
