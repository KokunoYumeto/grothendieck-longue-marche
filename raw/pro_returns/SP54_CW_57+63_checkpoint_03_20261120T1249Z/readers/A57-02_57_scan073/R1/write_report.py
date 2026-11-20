from pathlib import Path
from datetime import datetime, timezone
import json
base=Path('/workspace/scratch/b9993b8b5640')
inputs=base/'work/inputs/A57-02_57_scan073'
out=base/'out/readers/A57-02_57_scan073/R1'
page=json.loads((inputs/'page.json').read_text())
a=page['half_a']; b=page['half_b']
c=(inputs/'C.tex').read_text()
reading=c.replace('rather different for (i) and (ii)',r'rather different for (\unsure{i|1}) and (ii)')
assert reading != c
(out/'reading.tex').write_text(reading)
cp=lambda name:str(out/'crops'/name)
crops=[]
for name in ['trivial','intro_i','then_f']:
    d=json.loads((out/'crops'/f'{name}.json').read_text())
    d['scaling']=d['output_size'][0]/(d['bbox'][2]-d['bbox'][0])
    d['view_count']=1
    crops.append(d)
changes=[]
def change(id,place,c,h,reading,kind,scan_shows,source,bbox,confidence='high',crop=None,consequence=None):
    changes.append(dict(id=id,place=place,c=c,h=h,reading=reading,differs_c=(c!=reading),differs_h=(h!=reading),kind=kind,h_marked='no',confidence=confidence,scan_shows=scan_shows,evidence={'source':source,'bbox':bbox},crop=crop,mathematical_consequence=consequence))
change('R1-01','Date', 'July 18, I962','July 18, 1962','July 18, I962','misread symbol or index','The year begins with a full-width serifed capital I; the 1 in 18 has a different upper approach.',a,[1391,145,1634,185])
change('R1-02','Opening paragraph, after geometric fibers','fibers,(at','fibers, (at','fibers,(at','other','Comma and opening parenthesis are adjacent typed characters; there is no intervening full typed space.',a,[292,680,471,718])
change('R1-03','Opening paragraph, after beautiful','beautiful) ,','beautiful),','beautiful) ,','other','One character-width interval separates the closing parenthesis and following comma.',a,[643,731,858,770])
change('R1-04','Opening paragraph, first parenthesized reference in different for', '(i)','(i)',r'(\unsure{i|1})','misread symbol or index','The narrow glyph has a broad foot and a fused, hooked upper body. The dot/stem separation is obscured. Its appearance admits i or 1; no separate earlier character can be recovered securely from this one crop.',a,[622,890,990,1025],confidence='low',crop=cp('intro_i.png'),consequence='The reference label remains uncertain; no mathematical correction has been made.')
change('R1-05','Statement (i), adjective after S','neetherian','noetherian','neetherian','abbreviation expanded or spelling modernised','Both first and second vowels show horizontal e crossbars; the first is not a closed o.',b,[1041,87,1233,126])
change('R1-06','Statement (i), S - morphism',r'$S$ - morphism',r'$S$-morphism',r'$S$ - morphism','other','The hyphen has a typed blank interval on both sides.',b,[481,140,709,178])
change('R1-07','Statement (i), then before f',r'the\handwritten{n}','the',r'the\handwritten{n}','omission','A continuous dark handwritten n occupies the interval after typed the and before typed f. The added letter is not a superscript attached to f.',b,[590,137,1260,282],crop=cp('then_f.png'))
change('R1-08','Statement (i), label on Picard homomorphism','f',r'f^{\cdot}','f','text not on the page','The typed f is followed by blank space and a colon. The region above and to its right has no distinct raised dot or other superscript.',b,[590,137,1260,282],crop=cp('then_f.png'),consequence='The transcription preserves the visible plain f as the map label.')
change('R1-09','Statement (i), before subset M','i. e.a',r'i.e.\ a','i. e.a','other','There is a typed blank after the first full stop; e, the next full stop and a follow without a full typed blank.',b,[1230,242,1348,279])
change('R1-10','Bottom-right continuation mark',r'\hfill .../...\par','',r'\hfill .../...\par','omission','Three dots, an oblique slash and three further dots are visible at bottom right.',b,[1505,994,1639,1038])
inv=[]
def item(element,hand,kind,position,first):
    inv.append({'sheet_kind':'letter','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
item('073-R1-01','typewriter','text','top right','July 18, I962')
item('073-R1-02','typewriter','text','upper left, salutation','My dear Murre,')
item('073-R1-03','typewriter','text','opening paragraph, fourteen lines','I recently had some thought')
item('073-R1-04','typewriter','text','opening paragraph, fifth line',r'\underline{\mathrm{pic}}^{P}_{X/S}; lower-case p, raised P, lowered X/S')
item('073-R1-05','typewriter','text','opening paragraph, twelfth line',r'(\unsure{i|1}), followed by (ii); dark first label')
item('073-R1-06','typewriter','text','statement (i), five lines','(i) Let X, Y be proper over S neetherian')
item('073-R1-07','another unnamed hand','insertion','statement (i), first line, between X and Y','right arrow')
item('073-R1-08','typewriter','text','statement (i), second line','surjective, with one underline; S - morphism')
item('073-R1-09','another unnamed hand','insertion','statement (i), third line, after the','n completing then')
item('073-R1-10','typewriter','text','statement (i), third line',r'f:\underline{\mathrm{Pic}}_{Y/S} to \underline{\mathrm{Pic}}_{X/S}; typed symbols and single underlines')
item('073-R1-11','another unnamed hand','insertion','statement (i), third line, between the two Pic terms','right arrow')
item('073-R1-12','typewriter','text','statement (i), fifth line',r'\underline{\mathrm{Pic}}_{Y/S} and \underline{\mathrm{Pic}}_{X/S}')
item('073-R1-13','typewriter','text','statement (ii), four lines','(ii) The same conclusion holds')
item('073-R1-14','another unnamed hand','insertion','statement (ii), first line, between X and Y','right arrow')
item('073-R1-15','another unnamed hand','insertion','statement (ii), second line, before 3',r'\geqslant')
item('073-R1-16','typewriter','text','statement (ii), fourth line',r'sheaf \underline{L}, with one underline')
item('073-R1-17','typewriter','text','connected-result paragraph, two lines','A connected result is that for any X/S proper, and integer')
item('073-R1-18','another unnamed hand','insertion','connected-result paragraph, second line, between n and 0',r'\ne')
item('073-R1-19','typewriter','text','final paragraph, seven lines','I tell you about this, namely (i)')
item('073-R1-20','typewriter','text','bottom right','.../...')
item('073-R1-21','another unnamed hand','margin note','bottom left','archive sheet number 72; preserved as comment')
notation=[
 {'sign':'lowercase pic with raised P and lower X/S','latex':r'\underline{\mathrm{pic}}^{P}_{X/S}','place':'Opening paragraph, pieces','visible_shape':'Lowercase p descends below the i/c body; one continuous underline; upper capital P and lower X/S.','alternatives':[]},
 {'sign':'Pic with lower Y/S and X/S','latex':r'\underline{\mathrm{Pic}}_{Y/S},\ \underline{\mathrm{Pic}}_{X/S}','place':'Statement (i), homomorphism and quasi-compactness sentence','visible_shape':'Capital P and lowercase ic, each singly underlined; source subscript Y/S, target subscript X/S in both occurrences.','alternatives':[]},
 {'sign':'plain f','latex':'f','place':'Statement (i), Picard homomorphism label','visible_shape':'Typed f; no separate raised mark to its upper right in the enlarged crop.','alternatives':[]},
 {'sign':'right arrows','latex':r'\handwritten{\to}','place':'Statement (i), X to Y and Pic to Pic; statement (ii), X to Y','visible_shape':'Hand-drawn horizontal strokes with right-facing arrowheads.','alternatives':[]},
 {'sign':'dimension relation','latex':r'\handwritten{\geqslant}3','place':'Statement (ii), second line','visible_shape':'Right-facing angle with a separate lower oblique stroke parallel to the lower arm; followed by typed 3.','alternatives':[]},
 {'sign':'invertible sheaf L','latex':r'\underline{L}','place':'Statement (ii), last line','visible_shape':'Plain capital L, one underline, no recoverable overwritten letter.','alternatives':[]},
 {'sign':'unequal relation','latex':r'n\handwritten{\ne}0','place':'Connected result','visible_shape':'Two horizontal hand strokes crossed by an oblique stroke, between typed n and 0.','alternatives':[]},
 {'sign':'first introduction reference label','latex':r'\unsure{i|1}','place':'Opening paragraph, different for','visible_shape':'Heavy narrow character with broad foot and fused upper body.','alternatives':['i','1']},
 {'sign':'date year initial','latex':'I962','place':'Date','visible_shape':'Serifed capital I before 962.','alternatives':[]}
]
prior_flags=[
 {'place':'Opening, some thought','prior':'Singular thought flagged against thoughts','decision':'Confirmed singular thought from half_a; retained.'},
 {'place':'Opening, developped','prior':'Double p flagged against developed','decision':'Confirmed double p from half_a; retained.'},
 {'place':'Date','prior':'I962 flagged against 1962','decision':'Capital I retained; H difference recorded.'},
 {'place':'Statement (i), neetherian','prior':'neetherian flagged against noetherian','decision':'Both e crossbars visible; retained.'},
 {'place':'Statement (i), i. e.a','prior':'Unusual spacing flagged','decision':'Spacing retained from the ink.'},
 {'place':'Statement (i), then and f','prior':'Handwritten n and absence of raised f mark','decision':'Confirmed in then_f crop.'},
 {'place':'Opening pic and statement (ii) L','prior':'Alphabet/case and underlining','decision':'Lowercase initial pic, plain upper P, lower X/S and singly underlined L retained.'},
 {'place':'Statement (ii) and connected result','prior':'Handwritten inequalities','decision':'Slanted lower bar of greater-than-or-equal and crossed equals retained.'}
]
report={
 'page':page['page'],'cote':'57','our_scan':'73','reader':'R1',
 'start_utc':'2026-11-20T10:48:50Z','end_utc':datetime.now(timezone.utc).isoformat(),
 'model':'GPT-6 Astra Pro (identity exposed by developer instructions)','effort':'not exposed',
 'images_viewed':[page['whole'],a,b], 'image_view_counts':{page['whole']:1,a:1,b:1},
 'crops':crops,
 'coverage':{'all_lines_read':True,'all_elements_included':True,'concise_block_list':['Date','Salutation','Opening paragraph, fourteen lines, including all formulas and four references to (i)/(ii)','Statement (i), five lines, handwritten arrows and n, underlining and indices','Statement (ii), four lines, arrow, relation and sheaf letter','Connected result, two lines, crossed equals','Closing paragraph, seven lines','Continuation mark','Archive pencil 72']},
 'changes':changes,'c_doubts':[],
 'remaining_doubts':[{'place':'Opening paragraph, first parenthesized label in different for','reading':r'\unsure{i|1}','alternatives':['i','1'],'confidence':'low','reason':'The enlarged single crop shows a fused upper body and heavy lower serif. A separate earlier typed layer cannot be identified securely; no cancellation state has been asserted.','crop':cp('intro_i.png')}],
 'inventory':inv,
 'notes':{
  'summary':'The letter addresses Murre, reports improved finiteness results concerning Picard preschemes, gives labelled claims (i) and (ii), adds a power-homomorphism result, and introduces a further theorem via discussion of non flat descent. This describes the page; no proof is verified here.',
  'reading_decisions':[],
  'author_checks':['at least if these are normal','for simplicity of the statement','I do not have any good effectivity criterion','as I understand it'],
  'titles_dates_pagination':{'date':'July 18, I962','salutation':'My dear Murre,','title':None,'author_pagination':None,'archive_sheet_number':'72','continuation':'.../...'},
  'crowded_ink':['The trivial crop resolves compressed t/r bodies as the letters tr, followed by ivial. No crossing stroke or independently recoverable cancelled character was identified; trivial remains live.','The first introductory (i) has an unresolved fused upper body; the proposed reading marks i/1 uncertainty.'],
  'authorship':'Typewritten letter with additions in an unnamed hand. The page is addressed to Murre and carries no signature; no named attribution is added.',
  'physical_features':'Upper-left staple/rust trace and the horizontal sheet fold carry no readable inscription. No independent drawing, diagram, display, stamp, or signature was identified.',
  'c_doubt_accounting':'C contains zero in-text \\unsure, \\illegible or \\ill macros. Prior prose flags are recorded separately.',
  'equivalent_encodings':'H page{72} corresponds to supplied scan 73; emphasis/single underline, handwritten provenance wrappers, \u2260/\\ne/\\neq, and inline mathematical colon/spacing encodings do not create textual change rows.'
 },
 'notation':notation,
 'abbreviations':[{'abbreviation':'i. e.','proposed_expansion':'that is','place':'Statement (i), before a subset M'}],
 'check_events':[],
 'prior_flags':prior_flags
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
rows=[
 ('01','A 145–185','July 18, I962','Capital I retained.'),
 ('02','A 280–315','My dear Murre,','Salutation and comma read.'),
 ('03','A 382–415','I recently … for Picard','Every word read; thought singular.'),
 ('04','A 433–466','preschemes, … in the last','Every word and comma read.'),
 ('05','A 483–514','section … for a simple','Every word and full stop read.'),
 ('06','A 535–567','projective … the pieces','Every word and opening parenthesis read.'),
 ('07','A 570–630','pic with P/X/S … the case','Lowercase pic, upper P, lower X/S, underline read.'),
 ('08','A 634–665','where instead … geometric','Both plain f occurrences read.'),
 ('09','A 685–718','fibers,(at … of which','No typed blank before opening parenthesis.'),
 ('10','A 735–770','is quite … assumption,','Blank before comma after beautiful) retained.'),
 ('11','A 786–818','and even … of','Theorem 4.1. and parentheses read.'),
 ('12','A 836–870','the two first … The key','Crowded trivial inspected once in crop; letters retained.'),
 ('13','A 888–922','results … technical,','Every word read.'),
 ('14','A 936–970','and rather … to reduce','First label cropped; i/1 remains doubtful; following (ii), (ii), (i) read.'),
 ('15','A 987–1020','to the normal … equivalence','(ii), semicolon, apostrophe read.'),
 ('16','A 1036–1067','criteria … Seminar):','developped and terminal punctuation read.'),
 ('17','B 87–126','(i) Let X, Y … be a','neetherian, typed f : X and hand right arrow to Y read.'),
 ('18','B 140–178','surjective … that the','Single underline and spaces around S - morphism read.'),
 ('19','B 190–238','Picard preschemes … finite type','Added n, plain f, both Pic indices and hand arrow checked in crop.'),
 ('20','B 242–279','(and in fact … M of','Parentheses, i. e.a spacing and M read.'),
 ('21','B 292–340','Pic Y/S … Pic X/S is.','Both indices, underlines and quasi-compact read.'),
 ('22','B 341–377','(ii) The same … X to Y,','Label, entire text and hand right arrow read.'),
 ('23','B 391–434','if Y/S … dimension >= 3,','Y/S, all words, hand slanted lower bar and 3 read.'),
 ('24','B 441–476','and if X … invertible','X, sub-scheme, Y and every word read.'),
 ('25','B 492–529','sheaf L … S.','Plain singly underlined L read.'),
 ('26','B 542–579','A connected … integer','Every word, X/S and comma read.'),
 ('27','B 591–632','n unequal 0 … finite type.','Hand crossed equals, n. th and full sentence read.'),
 ('28','B 641–681','I tell you … of','(i), commas and every word read.'),
 ('29','B 691–729','proof, … fact that','non flat, full stop and every word read.'),
 ('30','B 742–780','I do not … recalling','Full effectivity-criterion clause read.'),
 ('31','B 791–832','what … out that','Full descent-datum clause read.'),
 ('32','B 841–882','by a slightly … the','Every word and comma read.'),
 ('33','B 892–934','following theorem, … recently,','Every word and commas read.'),
 ('34','B 943–980','and to some … it.','Every word and final full stop read.'),
 ('35','B 994–1038','.../...','Three dots each side of slash.'),
 ('36','B 1098–1132','72','Pencil archive number, retained as comment.')]
obs='''# R1 — cote 57, scan 073

Start: 2026-11-20 10:48:50 UTC. Model: GPT-6 Astra Pro (exposed identity); effort not exposed.

Whole image viewed once for layout, then half_a once and half_b once. Each of three crops viewed once. No OCR, web, other page, or other reader material was used. A/B coordinates below are pixel y ranges in the supplied halves; the overlap was covered during those single views.

## Ordered coverage

| Unit | Source position | Line anchor | Reading coverage |
|---|---|---|---|
'''
obs+='\n'.join('| '+' | '.join(row)+' |' for row in rows)
obs+='''

## Crop decisions

- `crops/trivial.png`: half_a box [505, 783, 1030, 883], width 3000, scale 5.714285714, rotation 0°. Compressed t/r letter bodies remain read as `trivial`; no cancellation is established.
- `crops/intro_i.png`: half_a box [622, 890, 990, 1025], width 3000, scale 8.152173913, rotation 0°. Heavy first reference label remains `\\unsure{i|1}`. A recoverable separate earlier letter and its state could not be established.
- `crops/then_f.png`: half_b box [590, 137, 1260, 282], width 3000, scale 4.477611940, rotation 0°. The added n completes then; the typed map label f has no raised dot. Source Y/S and target X/S remain secure.

## Accounting

C has no in-text doubt macros. Prior prose flags were checked separately. One new C uncertainty concerns the first introductory label; the rest of C is retained. Differences from H include the date initial, neetherian, the added n, the unmarked f, source spacing, and the continuation mark. Ordinary handwritten-provenance and underline wrapper differences are excluded.

No independent drawings, diagrams, displayed formulas, title, author page number, signature or recoverable cancellation were identified. The upper-left physical staple/rust trace is not an inscription. Mathematical notation was followed while reading, but no theorem or proof was checked; `check_events` is empty.
'''
(out/'observations.md').write_text(obs)
print(json.dumps({'reading':str(out/'reading.tex'),'report':str(out/'report.json'),'observations':str(out/'observations.md'),'changes':len(changes),'remaining_doubts':len(report['remaining_doubts']),'c_doubts':0,'crops':len(crops)},indent=2))
