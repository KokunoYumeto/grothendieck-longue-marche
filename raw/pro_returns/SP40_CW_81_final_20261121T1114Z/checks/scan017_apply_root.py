"""Apply only the scan017 root journal's explicit selections to clerk records.

Source-only: no images, reader scripts, arithmetic placement maps, compiler or
renderer are executed. Final page spans are attached only from the dedicated
assembler's supplied current map/hash. Root retains approval and commit.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import re
from scan017_build_record import json_text, fingerprint, exact, span, table

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'out'
CHECKS=OUT/'checks'


def root_sections(text):
    heads=list(re.finditer(r'^## (\d+) — (.+)$',text,re.M))
    return {int(m.group(1)):{'number':int(m.group(1)),'heading':m.group(2),
                            'start':m.start(),'end':heads[i+1].start() if i+1<len(heads) else len(text),
                            'text':text[m.start():heads[i+1].start() if i+1<len(heads) else len(text)]}
            for i,m in enumerate(heads)}


CHOICES={}
def choose(key,section,final,confidence,C,H,kind='other',status=None,doubt=None,source=None,**extra):
    CHOICES[key]={'section':section,'final':final,'confidence':confidence,
                  'diff_C':C,'diff_H':H,'kind':kind,'C_doubt_status':status,
                  'doubt':doubt,'source_choice':source}
    CHOICES[key].update(extra)


choose('D01a',1,r'\unsure{E_i|\Sigma_i}','low',False,False,status='retained',
       doubt=('E_i',[r'\Sigma_i'],'Cancellation does not settle the complete subject; both indexed candidates remain.'),source='B opening subject')
choose('D01b',1,r'\unsure{est|soit}','low',False,True,'misread word','retained',
       ('est',['soit'],'Connected and cancelled stems do not settle the short verb.'),source='All three literal proposals; root count confirmation')
choose('D01c',1,'rare','medium',True,False,status='resolved',source='A/C adjective')
choose('H01',1,'si','high',False,True,'misread word',source='All three si readings')
choose('H02',1,'dans $X$.','high',False,True,'omission',source='All three cancelled-clause endpoint points')
choose('H03',1,r'\inserted{on ait}','high',False,True,'insertion or placement',source='All three raised opening insertion states')
choose('D02',2,r'\deleted{Alors on \unsure{trouve} que}','medium',False,False,status='retained',
       doubt=('trouve',[],'The long cancellation obscures the central letter sequence.'),source='B/C qualification; root source-only count correction')
choose('S01',3,r'\overline{\Sigma_i^+}','high',False,False,source='Current C/H and every reader; S confirmation')
choose('S02',3,r'\overline{\Sigma_i^-}','high',False,False,source='Current C/H and every reader; S confirmation')
choose('H04',3,'No comma after first displayed E_i','high',False,True,'text not on the page',source='C and all three reader first endpoints')
choose('G13',3,'C M01: exact locally qualified triangular fill with period alternative, represented once','low',True,True,'drawing or diagram',
       doubt=('literal triangular point',['period interpretation'],'Shape is clear; attachment, punctuation role and hand remain unestablished.'),
       source='C complete M01 with its hspace placement',shape_confidence='high',role_confidence='low',hand='undetermined hand')
choose('P01',3,'Two successive equality rows in aligned; H horizontal source order preserved','high',False,False,
       source='C/all reader aligned layout; root noncount layout audit',confidence_scope='Root explicitly assigns high confidence to the clearly observed two-row layout; zero counts and log retained.')
choose('H05',4,"Alors je dis qu'on a",'high',False,True,'misread word',source='C and all three readings')
choose('S03',5,r'\overline{\Sigma_{12}}','high',False,False,source='Current C/H and every reader; S confirmation')
choose('D03',5,'Retraced cup: C G01 exact three-path graphic, outer unsure/amalg alternative removed','medium',True,True,'drawing or diagram','resolved',
       source='C three-component G01 paths and bounding box; A/B resolved cup interpretation')
choose('D03-shape',5,'C G01 shared left stem, inner return and outer return; all three exact draw commands','medium',False,False,'drawing or diagram',
       source='C G01 literal component bodies')
choose('G02',6,'C G02 complete bowed separator figure and wide fixed rectangle','medium',True,True,'drawing or diagram',source='C G02 exact figure')
choose('H06',7,'introduire','medium',False,True,'misread word',source='A/B and witness C marginal word')
choose('D04a',7,r'\unsure{\Pi|\pi}_j','medium',False,False,status='retained',
       doubt=(r'\Pi_j',[r'\pi_j'],'The high top and curved right return retain local case uncertainty.'),source='A marginal source')
choose('D04b',7,r'\deleted{\unsure{\Sigma}}E_j','low',False,False,'omission','retained',
       ('cancelled Sigma',[],'Crowded overlay hides the predecessor contour.'),source='A complete marginal formula',H_count_parent='017-H-MARGIN-ILL')
choose('G12',7,'B-reported wedge is the existing lower-left S return in Soit; no separate marginal glyph','medium',False,False,'other',
       source='Root attachment choice using A/C complete margin and existing Soit',component_of='017-I12',hand='his hand')
choose('H-MARGIN-ILL',7,'One H marginal parent: qualified crossed predecessor plus unspecified trailing ill; no further word supplied','low',False,True,r'readable ink left as \ill{}',
       source='Root groups omitted predecessor and unspecified placeholder once, without a positional-identity claim')
choose('N03',8,'Considerons','medium',True,True,'abbreviation expanded or spelling modernised',source='A unaccented first word')
choose('G03',9,'A G03 complete upper Pi_J insertion, one live de node, fixed origin and hooked guide','medium',True,True,'drawing or diagram',source='A complete G03 group')
choose('D05',10,r'\deleted{definie}','medium',True,True,'misread word','resolved',source='A/B cancelled unaccented word')
choose('N04',10,'definie','medium',True,True,'abbreviation expanded or spelling modernised',source='A/B following live unaccented word')
choose('D07a',11,r'\deleted{\unsure{\Sigma}}E_j','low',False,True,'omission','retained',
       ('cancelled Sigma',[],'Earlier diagonal and return remain partly merged into live E and cancellation.'),source='C qualified predecessor; original table scope retained')
choose('D06a',12,r'\unsure{\deleted{et}|et}','low',True,True,'deletion state (struck given live or live given struck)','mixed',
       (r'\deleted{et}',['et'],'Et letters are supported; the merged joining/crossing stroke leaves cancellation state uncertain.'),source='C complete-state et proposal',
       local_component_statuses=[{'component':'et letters','status':'resolved','original_C_scope':True},
                                 {'component':'cancellation target','status':'retained','new_qualification':True}],
       source_doubt_component_status='mixed: original et letters resolved; new cancellation-state qualification retained')
choose('D06b',12,r'\unsure{intersection|Intersection}','low',False,False,'other','retained',
       ('intersection',['Intersection'],'Word identity is supported; initial case remains crowded and qualified.'),source='B/C lowercase primary with A capital alternative',
       local_component_statuses=[{'component':'word identity','status':'supported'}, {'component':'initial case','status':'retained'}],H_count_parent='017-D06a')
choose('G04',13,'A G04 complete ternaires Pi_j insertion, one de node and bent guide; X follows outside','medium',True,True,'drawing or diagram',source='A complete G04 group')
choose('N05',14,'definies','medium',True,True,'abbreviation expanded or spelling modernised',source='A/B unaccented plural word')
choose('D07b',15,r'\unsure{\deleted{\in}|\deleted{E}|\notin}','low',True,False,r'readable ink left as \ill{}','retained',
       (r'\deleted{\in}',[r'\deleted{E}',r'\notin'],'Rounded body and strong slash leave both glyph and complete-state alternatives open.'),
       source='B complete later-sign alternatives',H_count_parent='017-H-LATER-ILL')
choose('H-LATER-ILL',15,r'\unsure{\deleted{\in}|\deleted{E}|\notin}','low',False,True,r'readable ink left as \ill{}',source='One H body ill parent for the selected later sign/state cluster')
choose('G05',16,'C complete M03 cluster: Sigma with dotless j, alpha, translated qualified point node and exact fill','low',True,True,'drawing or diagram',
       doubt=('literal upper point',['prime-shaped mark','point interpretation','attachment as j dot'],
              'One high point is visible; attachment as the j dot or an independent upper mark remains unresolved.'),
       source='C complete M03 outer and inner groups',hand='undetermined hand')
choose('G05-index',16,r'\Sigma_{\jmath}^{\alpha} with the single translated M03 point','low',False,False,'other',source='C complete dotless-index component, counted within G05')
choose('G11',16,'C M02a/M02b exact two-fill group with original hspace/raisebox placement and local qualification','low',True,True,'drawing or diagram',
       doubt=('two literal dark pieces',[],'The two shapes are visible; role, hand and surface origin remain undetermined.'),source='C complete M02 group',hand='undetermined hand')
choose('G11-upper',16,'C M02a exact upper-right fill','low',False,False,'drawing or diagram',source='C first M02 fill; noncount pair component')
choose('G11-lower',16,'C M02b exact lower-left fill','low',False,False,'drawing or diagram',source='C second M02 fill; noncount pair component')
choose('N06',17,'definie','medium',True,True,'abbreviation expanded or spelling modernised',source='A/B final-paragraph unaccented word')
choose('G06',18,'B G06 exact locally qualified quadrilateral fill/mathord group before first bigcup','low',True,True,'drawing or diagram',
       doubt=('literal baseline point',['period character'],'Role and hand remain undetermined despite clear point presence.'),source='B exact G06 group',shape_confidence='high',hand='undetermined hand')
choose('D08a',19,r'\Pi_J^{\unsure{\circ|0}}','medium',False,True,'misread symbol or index','retained',
       (r'\circ',['0'],'The first raised ring remains locally circle/zero.'),source='B complete lower Pi group, same first-ring qualification in all readers')
choose('G07',19,'B G07 complete inserted lower Pi_J ring, one de node and exact guide','medium',True,True,'drawing or diagram',source='B complete G07 group')
choose('D11',19,'C G06 complete cup/transverse-stroke graphic with local unsure, limits and E_j','low',True,True,'drawing or diagram','resolved',source='C complete G06 group',
       local_component_statuses=[{'component':'transverse stroke presence','status':'resolved','confidence':'high'},
                                 {'component':'mathematical role','status':'retained','confidence':'low'}])
choose('D11-shape',19,'C G06 exact cup contour and separate transverse draw command','high',False,False,'drawing or diagram',source='C two literal G06 paths; stroke presence resolved')
choose('D11-role',19,'Local unsure on the literal middle-union graphic; function unassigned','low',False,False,'other',
       doubt=('literal cup and transverse stroke',['barred-union interpretation','unassigned extra stroke interpretation'],
              'Visible stroke presence is resolved; its function remains unassigned.'),source='C G06 local qualifier retained by root')
choose('D08b',20,r'\Pi_{J,j}^{\circ} (local circle/zero doubt retained through first-occurrence convention)','medium',False,True,'misread symbol or index','retained',
       (r'\circ',['0'],'The second physical ring remains separately uncertain; only the first occurrence carries the TeX wrapper.'),
       source='All-reader literal circ plus root source-only first-occurrence correction')
choose('G09',20,'B G09 complete inserted condition, one induites node and continuous hooked guide','medium',True,True,'drawing or diagram',source='B complete G09 group')
choose('G09-open',20,'H opening-parenthesis reading belongs to the selected continuous induites guide','medium',False,False,'text not on the page',source='Local interpretation component of G09')
choose('D12',21,r'U_{\unsure{\deleted{J}J|\deleted{j}J|J}}','low',True,True,'deletion state (struck given live or live given struck)','retained',
       (r'\deleted{J}J',[r'\deleted{j}J','J'],'Overlapping lower returns leave predecessor case and corrected/retraced state unresolved.'),source='All-reader full subscript alternatives in B selected U group')
choose('D12-final',21,'Final capital J in every retained complete-state alternative','high',False,False,'other',source='Root final-J confirmation; A extra named component retained')
choose('G10',21,'B G10 complete raised U expression, one sur node and descending full guide','medium',True,True,'drawing or diagram',source='B complete G10 group; one placement/guide parent')
choose('G10-state',21,'Raised U expression insertion state within selected B G10 parent','medium',False,False,'insertion or placement',source='Root combines C D33/D34 under the placement/guide parent')
choose('D09',22,r'\unsure{g|j}','low',False,True,'misread symbol or index','retained',
       ('g',['j'],'Dense loop and long hooked stem retain the local g/j alternatives.'),source='All-reader retained final variable')
choose('H07',22,r'$(\unsure{g|j}\in J)$.','high',False,True,'text not on the page',source='Single closing parenthesis and point')
choose('D10',22,'Pour','medium',True,False,'other','resolved',source='All-reader final word, resolved on this page')
choose('ARCHIVE',23,'% archive sheet number: 16','high',False,False,'other',source='Existing C comment; root numeral confirmation and metadata/inventory repair',hand='undetermined hand')


INVENTORY_FINAL={
 'I01':('Cas particuliers; one underline',1),
 'I02':(r'Supposons que forall i in I; si Sigma_i+ Sigma_i-; comp. conn.; X\Sigma_i',1),
 'I03':(r'Cancelled unsure E_i|Sigma_i; unsure est|soit; rare dans X.',1),
 'I04':('Raised on ait',1),
 'I05':(r'Cancelled Alors on unsure trouve que',2),
 'I06':('Two successive signed-Sigma closure equalities; first has no comma; second endpoint is I39',3),
 'I39':('C M01 one qualified triangular point with period interpretation alternative',3),
 'I07':("Alors je dis qu'on a",4),
 'I08':('Barred Sigma12 equality with one firm retraced-cup cluster and ordinary second cup',5),
 'I26':('C G01 three paths: shared left stem, inner return, outer return; cup resolved',5),
 'I27':('C G02 bowed divider and hooked endpoint with fixed left placement',6),
 'I09':(r'introduire la partition unsure Pi|pi_j = {deleted unsure Sigma E_j, Sigma_j+, Sigma_j-}',7),
 'I10':(r'Cancelled unsure Sigma beneath marginal E_j',7),
 'I28':('Lower-left return of the S in existing Soit; no separate marginal glyph',7),
 'I11':('Cancelled Supposons',7),
 'I12':('Soit J subset I tel que I = J amalg {i}.',7),
 'I13':(r'Considerons la partition; definie; unsure cancelled et|live et; unsure intersection|Intersection; definies',12),
 'I14':('Inserted Pi_J',9),
 'I29':('A G03 exact bent guide, with one live de node',9),
 'I15':('Cancelled definie, unaccented',10),
 'I16':('Qualified cancelled Sigma predecessor beneath first main E_j',11),
 'I17':('Et letters resolved; cancelled et primary/live et alternative',12),
 'I18':('Inserted ternaires Pi_j',13),
 'I30':('A G04 continuous bent guide with both arms; one de inside, X outside',13),
 'I19':(r'Complete states: deleted membership; deleted E; integral notin',15),
 'I20':('X = E_j amalg indexed coproduct; C M03 complete dotless-j, alpha and single-point cluster',16),
 'I31':('C M03 single upper point with unresolved j-dot/independent-mark attachment',16),
 'I32':('C M02a/M02b upper-right and lower-left qualified dark pieces; exact two fills',16),
 'I21':(r"c'est aussi la partition definie; indexed unions; two local circle/zero doubts; induced partition; g|j; Pour",22),
 'I33':('B G06 qualified baseline quadrilateral point before first indexed union',18),
 'I22':('Inserted Pi_J with first explicit circle/zero qualification',19),
 'I34':('B G07 lower Pi_J guide and one live de node',19),
 'I35':('C G06 literal cup and visible transverse stroke; role locally qualified',19),
 'I23':('Inserted (j in J)',20),
 'I36':('B G09 continuous hooked guide over one live induites node',20),
 'I24':(r'Raised U with deleted-J/J, deleted-j/J and single-retraced-J alternatives, equals',21),
 'I25':('Qualified U predecessor case and corrected/retraced state; final J confirmed',21),
 'I37':('B G10 full descending guide and one live sur node',21),
 'I38':('Archive numeral 16, comment only; hand undetermined',23),
}

LOCAL_EVIDENCE={
 'D01a':'A left upright with overlapping horizontal and diagonal passes remains under cancellation. Root retains E_i with Sigma_i as the alternative.',
 'D01b':'Connected and cancelled stems leave the short est/soit sequence uncertain. The explicit soit alternative retains the prior C uncertainty; H has soit as its primary.',
 'D01c':'The short r-like opening, rounded middle and final re support root’s resolved rare reading.',
 'H01':'The parenthetical opening shows the connected s and dotted i of si.',
 'H02':'A distinct dark point follows the cancelled X and remains inside the cancelled clause.',
 'H03':'The words on ait occupy a raised baseline above the crossed clause.',
 'D02':'The long cancellation obscures the central letters after the tall t and low connected strokes. Root retains trouve as doubtful; section24 corrects the H count to zero because the primary word is unchanged.',
 'S01':'A long separate horizontal rule lies above the complete Sigma_i-plus form. Current C/H already print this overline.',
 'S02':'A long separate horizontal rule lies above the complete Sigma_i-minus form. Current C/H already print this overline.',
 'H04':'The visible points at the first E_i belong to its dotted index; the following space carries no recovered comma.',
 'G13':'The detached second-row point has a peaked top and broad base. Root retains its literal triangular shape once, with period interpretation and attachment uncertain.',
 'P01':'The two equalities occupy successive physical rows. The selected aligned source preserves their reading order; the layout audit carries zero witness counts.',
 'H05':'The prose has q’s long descender, an apostrophe, a low on run and a separate final a: Alors je dis qu’on a.',
 'S03':'A distinct long horizontal rule lies above the complete left Sigma12. Current C/H already print this overline.',
 'D03':'The first join has a thick left upright and two curved lower/right returns. Root resolves the cup reading and selects C’s three literal component paths.',
 'D03-shape':'C’s selected paths preserve the separate left stem, inner return and outer return. They remain components of the single counted join.',
 'G02':'The separator rises gently, undulates shallowly and turns down at the right end. Root selects C’s exact curved path and fixed left-placement rectangle.',
 'H06':'The marginal word ends with a short rising connector and final curved e, supporting introduire.',
 'D04a':'The marginal letter has a high top, two legs and a curved right return. Root retains the Pi/pi case qualification.',
 'D04b':'Sigma-like diagonal and lower strokes remain crowded beneath the heavy marginal E_j. The predecessor stays qualified and is covered by the one H marginal parent.',
 'G12':'The reported wedge continues into the loop and stem of the S in main-text Soit. Root retains it once through that word, with medium attachment confidence and the same hand attribution.',
 'H-MARGIN-ILL':'The marginal note closes with its brace. Root groups the qualified crossed predecessor and the unspecified trailing H ill under one H parent without asserting an exact positional identity for the placeholder.',
 'N03':'The e region in Considerons has open paper above it and no recovered detached accent. Root selects the local unaccented spelling.',
 'G03':'The guide rises from its low left start, runs shallowly rightward above de and ends in a short upward hook. A’s selected group contains the raised Pi_J and one live de.',
 'D05':'The cancelled word shows d, low e, descending f and the following i/n/i/e sequence. The detached point belongs over a later i; root selects cancelled definie.',
 'N04':'The following live defining word has no recovered acute over its e. Root retains unaccented definie at this separate word position.',
 'D07a':'Extra diagonal and angular lower strokes remain within the live E_j. Their overlap leaves the Sigma predecessor qualified under the original table’s scope.',
 'D06a':'The e loop and tall t-like stem support et. The heavy connection merges with the apparent crossing, so its cancellation state remains qualified while its letters are resolved.',
 'D06b':'The internal sequence and tion ending support intersection. The initial entry is crowded; root keeps lowercase primary and capital-I alternative in one live word.',
 'G04':'A fine left arm descends to a low vertex and the longer right arm rises diagonally. A’s selected group preserves both arms, one de node and the following X outside.',
 'N05':'The plural word’s e precedes the tall f without a recovered acute; the detached points lie over the later i positions. Root selects definies.',
 'D07b':'The isolated sign has a rounded body, short middle return and strong rising slash. Root retains deleted membership, deleted E and integral slashed-membership complete states.',
 'H-LATER-ILL':'The one H body ill covers the selected later isolated sign/state cluster. Its local glyph and state alternatives contribute no additional H count.',
 'G05':'One high point lies left of alpha and above the hooked subscript stem. Root retains C’s complete dotless-j and translated-point group, with j-dot versus independent-mark attachment unresolved.',
 'G05-index':'The selected C node uses dotless j beside alpha and carries the single point in its translated qualified node. This index component stays within G05’s count.',
 'G11':'Two compact dark pieces lie diagonally apart at the far right. Root retains C’s two exact fills and placement, with role, hand and surface origin undetermined.',
 'G11-upper':'The selected first C fill represents the upper-right piece within the one qualified pair.',
 'G11-lower':'The selected second C fill represents the lower-left piece within the one qualified pair.',
 'N06':'The lower defining word has low e before tall f, with its detached points over the later i positions. Root selects unaccented definie.',
 'G06':'A detached roughly quadrilateral point lies between celle de and the first indexed union. Root selects B’s literal qualified fill; role and hand stay undetermined.',
 'D08a':'The first raised Pi_J ring is small and rounded with a partly open contour. Root retains the local circle/zero alternatives.',
 'G07':'The lower Pi guide curves beneath the raised name and above de, then rises into a short hooked endpoint. Root selects B’s complete group with one live de.',
 'D11':'A near-horizontal stroke crosses the upper-left side of the middle cup and extends across much of its width. Its presence is resolved; the selected literal graphic keeps the role qualified.',
 'D11-shape':'The selected C group has one cup contour and one separate transverse draw command. Stroke presence has high confidence and remains within the single union count.',
 'D11-role':'The transverse stroke is present, while its function remains unassigned. Root preserves the local unsure wrapper around the literal graphic.',
 'D08b':'The binary partition name has its own small raised ring, independently retained as circle/zero. Section25 restores first-occurrence-only TeX qualification while keeping this second local doubt explicit in the record.',
 'G09':'The guide curves beside induites, extends across its upper line and ends with a short upward/backward hook. B’s selected group preserves the raised condition and one live induites.',
 'G09-open':'The curve represented by H as an opening parenthesis is continuous with the selected induites guide. This interpretation is a noncount component of G09.',
 'D12':'Overlapping lower returns share the final capital-J material. Root retains cancelled J plus J, cancelled j plus J, and a single retraced J as complete states.',
 'D12-final':'The final J has a clear top and lower return in every retained complete-state alternative. Root records this confirmation without a new count.',
 'G10':'The U expression is raised; its guide runs beneath the subscript, bends right and descends beside sur. B’s complete group supplies one placement/guide count and one live sur.',
 'G10-state':'The raised U insertion state is preserved inside the selected B G10 group. Root combines C-reader’s insertion and guide flags under that one parent.',
 'D09':'The final quantified letter has a dense head/loop and long hooked descender. Root retains g primary with j alternative.',
 'H07':'One closing parenthesis follows J, then a separate point. The selected ending preserves that single close.',
 'D10':'The final word has a large P, small rounded o trace and connected ur ending. Root resolves Pour from this page; H already has that primary.',
 'ARCHIVE':'The faint numeral shows an upright 1 followed by looped 6. Root retains the existing comment-only 16; its individual hand remains undetermined.',
}

CORRECTION_MAP={
 'D01a':[24],'D01b':[24],'D01c':[24],'D04a':[24],'D02':[24],
 'D08b':[25],'G12':[26],
}


def apply():
    record_path=CHECKS/'scan017_record_draft.json'
    record=json.loads(record_path.read_text())
    journal_path=CHECKS/'scan017_main_decisions.md'
    journal=journal_path.read_text();sections=root_sections(journal)
    assert all(i in sections for i in range(1,24)), 'Root sections01–23 required.'
    assert set(CHOICES)=={d['id'][4:] for d in record['decisions']}, 'Canonical choice coverage differs.'
    corrections=[v for k,v in sections.items() if k>23]
    # Source-only corrections are retained as exact journal sections. Their
    # canonical decisions are also explicitly listed below for traceability.
    byid={d['id'][4:]:d for d in record['decisions']}
    root_doubts=[]
    for key,choice in CHOICES.items():
        d=byid[key];sec=sections[choice['section']]
        for field in ['final','confidence','diff_C','diff_H','kind','C_doubt_status']:
            d[field]=copy.deepcopy(choice[field])
        d['main_approved']=False
        d['root_ink_choice_applied']=True
        d['root_decision_section']=sec['number'];d['root_decision_heading']=sec['heading']
        d['evidence']=LOCAL_EVIDENCE[key]
        d['root_evidence_source']=span(journal,sec['start'],sec['end'],'root.main_decisions.md',section=sec['number'],heading=sec['heading'])
        d['root_crop_paths']=re.findall(r'Viewed `([^`]+)` once\.',sec['text'])
        d['crop']=d['root_crop_paths'][0] if d['root_crop_paths'] else None
        d['root_source_choice']=choice['source_choice']
        d['confidence_status']='Root supplied local confidence and scope in cited journal section.'
        d['count_status']='Root-selected physical-cluster Boolean; final record approval remains with root.'
        d['remaining_doubt']=bool(choice['doubt'])
        d['log_decision']=True
        d['marked_in_H']=key in {'H-MARGIN-ILL','D04b','G12','H-LATER-ILL','D07b','D10'}
        if key in {'D04b','G12','D07b'}:
            d['marked_in_H_scope']='Covered source-placeholder locus; the marginal parent makes no exact positional-identity claim.'
        for field,value in choice.items():
            if field not in {'section','final','confidence','diff_C','diff_H','kind','C_doubt_status','doubt','source_choice'}:
                d[field]=copy.deepcopy(value)
        d.pop('root_source_only_corrections',None)
        relevant=[sections[n] for n in CORRECTION_MAP.get(key,[]) if n in sections]
        if relevant:
            d['root_source_only_corrections']=[span(journal,c['start'],c['end'],'root.main_decisions.md',section=c['number'],heading=c['heading']) for c in relevant]
        if choice['doubt']:
            reading,alternatives,reason=choice['doubt']
            components=[]
            for row in record['source_doubt_crosswalk']:
                if d['id'] in row['loci']:
                    components.append({'reader':row['reader'],**copy.deepcopy(row)})
            root_doubts.append({'decision_id':d['id'],'location':d['location'],'reading':reading,
                                'alternatives':alternatives,'confidence':d['confidence'],'reason':reason,
                                'reader_components':components,'final_status':'root-selected uncertainty retained',
                                'root_decision_section':sec['number'],'crop':d['crop'],'root_page_sources':[],
                                'local_component_statuses':copy.deepcopy(d.get('local_component_statuses',[]))})
    record['doubts']=root_doubts

    for item in record['inventory']:
        key=item['element'][4:];words,section=INVENTORY_FINAL[key]
        item['first_words_or_objects']=words;item['transcribed']='yes'
        item['hand']='undetermined hand' if key in {'I31','I32','I33','I38','I39'} else 'his hand'
        item['hand_status']='Selected source label and root-local attribution; raw original hand labels retained in source_rows.'
        item['selection_status']='Root ink selection applied; selected-source attachment pending assembler.'
        item['root_decision_section']=section
        if key=='I28':
            item['kind']='text';item['component_of']='017-I12'
            item['coverage_only']=True
            item['root_source_only_hand_clarification_section']=26
        if key in {'I17','I19','I25'}:
            item['state']='Primary cancellation representation with explicit complete-state alternatives; see selected words and decision.'
    for source in record['actual_C_doubt_map']:
        ids=source['primary_local_decision_ids']
        source['local_statuses']={identifier:byid[identifier[4:]]['C_doubt_status'] for identifier in source['local_status_decision_ids']}
        source['local_component_statuses']={identifier:copy.deepcopy(byid[identifier[4:]].get('local_component_statuses',[])) for identifier in ids}
        source['status']='Every primary local ink choice supplied by root; original source identity retained.'

    record['source_counting_constraints']=[
        {'parent':'017-H-MARGIN-ILL','witness':'H','count':True,'children':['017-D04b','017-G12'],'local_children_H_count':False,
         'status':'Root section07: predecessor and unspecified placeholder grouped once without claiming exact positional identity.'},
        {'parent':'017-H-LATER-ILL','witness':'H','count':True,'children':['017-D07b'],'local_children_H_count':False},
        {'parent':'017-D06a','witness':'H','count':True,'children':['017-D06b'],'local_children_H_count':False},
        {'parent':'017-G10','witness':'H','count':True,'children':['017-G10-state'],'local_children_H_count':False,
         'status':'Root section21 combines C-reader D33 insertion and D34 guide flags into one placement/guide count.'},
        {'parents':['017-D03','017-D11','017-D12','017-G11','017-G05'],'scope':'One count per physical cluster per witness; exact path/index/state children are noncount log rows.'}]
    record['notes']=(
        "The page is headed Cas particuliers with one underline. Its opening writes `X\\setminus\\Sigma_i` and the two equalities "
        "`\\overline{\\Sigma_i^+}=\\Sigma_i^+\\cup E_i` and `\\overline{\\Sigma_i^-}=\\Sigma_i^-\\cup E_i`. "
        "The second endpoint is one qualified triangular point with period interpretation retained. After the words Alors je dis qu'on a, "
        "the page writes `\\overline{\\Sigma_{12}}=\\Sigma_{12}\\cup E_1\\cup E_2`; the first cup is reproduced by the selected three retraced paths. "
        "The lower writing includes `I=J\\amalg\\{i\\}` and `X=E_j\\amalg\\coprod_{\\alpha\\in\\pi_0(X\\setminus E_j)}\\Sigma_j^\\alpha`; "
        "the selected display represents the one high point with a dotless-j text node and its qualified translated fill. "
        "The final prose begins c'est aussi la partition definie and ends Pour. Both raised partition rings retain local circle/zero doubts; "
        "the first occurrence carries the explicit TeX qualification under the standing source convention. "
        "The middle indexed union retains its literal transverse stroke and an unassigned role. Et's letters are resolved with cancellation state qualified; "
        "intersection's identity is supported with its case retained as intersection|Intersection. The margin-edge wedge is retained once within Soit. "
        "The three displayed Sigma closure bars already occur in C/H and are confirmed locally under S SA01-K81-06 without current-witness counts. "
        "No written date or additional author page number is supplied. The archive numeral16 remains a comment with undetermined hand. "
        "These are reports of the written formulas and words. No mathematical proof is claimed. Reader B's existing four-point coordinate conversion "
        "is recorded once as SP40-017-SOURCE-COORDINATES with its exact stored inputs/map/outputs and placement scope; it was not rerun."
    )
    record['workflow_note']=(
        "Three fresh independent readers A/B/C used briefv15; their complete returns and actual timestamps are preserved by textual fingerprints. "
        "Their crop totals are A20, B19 and C14. Root completed23 successful distinct local crop views and one earlier unsuccessful unseen delivery of A01; "
        "the same existing A01 file was then delivered once. Root viewed neither the whole scan nor a supplied half. "
        "The clerk examined source text only, performed no image operation, OCR, compiler/render invocation, numerical geometry or theorem check, "
        "and did not rerun the recorded B calculation. Root sections01–23 and the transparent source-only corrections supply all ink/count choices. "
        "Dedicated assembly supplies the selected final-source map; root alone approves and commits the main record."
    )
    counts={w:sum(d['diff_'+w] for d in record['decisions']) for w in ['C','H']}
    record['counts']={'status':'All root local ink/count choices applied; final record approval pending.',**counts,
                      'by_witness_confidence':{w:{level:sum(d['diff_'+w] and d['confidence']==level for d in record['decisions']) for level in ['high','medium','low']} for w in ['C','H']},
                      'remaining_doubt_loci':len(root_doubts),'inventory_elements':len(record['inventory'])}
    primary=[byid[key[4:]] for row in record['actual_C_doubt_map'] for key in row['primary_local_decision_ids']]
    record['C_doubt_resolution_counts']={
        'actual_rows':12,'physical_primary_clusters':18,
        'resolved_physical_primary_clusters':sum(d['C_doubt_status']=='resolved' for d in primary),
        'retained_physical_primary_clusters':sum(d['C_doubt_status']=='retained' for d in primary),
        'mixed_original_glyph_resolved_new_state_retained_clusters':sum(d['C_doubt_status']=='mixed' for d in primary),
        'loci_retaining_some_local_qualification':sum(d['C_doubt_status'] in {'retained','mixed'} for d in primary),'pending_primary_local':0,
        'original_et_glyph_component_resolved':True,'intersection_identity_supported_case_retained':True,
        'middle_union_stroke_presence_resolved_role_retained':True,
        'scope_note':"Twelve original rows and18 primary clusters:5 fully resolved,12 retained and1 mixed. The mixed et locus has its original letters resolved and a newly qualified cancellation state. Thus13 loci retain some local qualification; the original et glyph doubt is never described as wholly unresolved. R11 stroke presence is resolved and its new role doubt is separate. A's final-J component and B's two descriptions of D12 create no new original row or count. Both R08 ring loci remain retained; first-occurrence-only source formatting is applied."}
    record['source_counts'].pop('approved_remaining_doubt_clusters',None)
    record['source_counts']['root_selected_remaining_doubt_clusters']=len(root_doubts)
    record['source_counts']['remaining_doubt_clusters']=len(root_doubts)
    record['root_choices_applied_through_section']=max(sections)
    record['root_sections_present']=len(sections)
    record['root_approved_decision_entries']=0
    record['root_ink_decision_entries']=len(CHOICES)
    record['root_approval_status']='Pending root final record review and approval.'
    record['pending_root_decision_ids']=[]
    record['root_ink_pass']={'successful_crop_views':23,'unsuccessful_unseen_delivery_attempts':1,
                             'whole_scan_views':0,'supplied_half_views':0,'source':'checks/scan017_main_decisions.md',
                             'clerk_image_views':0}
    record['root_actions_pending']=['Attach dedicated assembler exact current map/hash.','One final targeted source QA pass.','Root approval and commit.']
    record['main_adjudicated']=False
    record['root_source_only_corrections']=[span(journal,c['start'],c['end'],'root.main_decisions.md',section=c['number'],heading=c['heading']) for c in corrections]
    record['mechanical_verification']['status']='Root choices applied; final selected-source attachment/QA pass pending.'
    record['mechanical_verification']['all_ink_choices_supplied_by_root']=True

    manifest_path=CHECKS/'scan017_reader_fingerprints.json'
    manifest=json.loads(manifest_path.read_text())
    manifest['files']['root.main_decisions.md']=fingerprint(journal_path)
    manifest['root_files']['main_decisions']=manifest['files']['root.main_decisions.md']
    manifest['files']['clerk.apply_root.py']=fingerprint(Path(__file__))
    union='# Scan017 source union and root choices\n\n'
    union+='All three independent returns are preserved. Root sections01–23 and the source-only corrections supply the selected readings. Main record approval/commit remains with root; no image bytes were read by the clerk.\n\n'
    union+='## Current counts\n\n```json\n'+json.dumps(record['counts'],ensure_ascii=False,indent=2)+'\n```\n\n'
    union+='## Complete decision crosswalk\n\n'+table(['ID','Location','A','B','C-reader','Root selected','C count','H count','Original doubt status','Root section'],[
        (d['id'],d['location'],*[d['readers'].get(r,[]) or ['TeX: '+x['attachment']['excerpt'] for x in d.get('reader_tex_proposals',{}).get(r,[])] for r in 'ABC'],
         d['final'],d['diff_C'],d['diff_H'],d['C_doubt_status'],d['root_decision_section']) for d in record['decisions']])
    union+='\n## Original C rows and local states\n\n'+table(['Original row','Primary loci','Local states','Component statuses'],[(r['source_row'],r['primary_local_decision_ids'],r['local_statuses'],r['local_component_statuses']) for r in record['actual_C_doubt_map']])
    union+='\n## Physical-parent count policy\n\n'+table(['Parent','Witness','Children','Selected treatment'],[(r.get('parent',r.get('parents')),r.get('witness','C/H'),r.get('children',[]),r.get('status',r.get('scope'))) for r in record['source_counting_constraints']])
    union+='\n## Source completeness and prior computation\n\n'
    union+='The draft retains113 raw differences,45 raw reader doubts and136 raw inventory rows, with their original identities and verbatim JSON spans. Forty literal drawing commands and all reader TeX characters have source mappings. Report-silent word choices and mark/qualifier representations have exact supplemental spans. The original twelve doubtful-reading rows contain eighteen primary loci; A names one extra noncount final-J component and B separately describes two aspects of its one D12. One existing B P03 coordinate event is preserved with exact source linkages and restricted placement scope; no calculation was rerun. Selected final-source attachments await the dedicated assembler current map/hash.\n'
    record_path.write_text(json_text(record));manifest_path.write_text(json_text(manifest));(CHECKS/'scan017_union.md').write_text(union)
    print(json_text({'root_sections':list(sections),'decisions':len(CHOICES),'counts':record['counts'],
                     'doubt_scope':record['C_doubt_resolution_counts'],'main_adjudicated':record['main_adjudicated'],
                     'final_attachments':'pending assembler map/hash'}))


if __name__=='__main__':
    apply()
