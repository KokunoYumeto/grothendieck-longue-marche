"""Manual scan037 decisions, after all complete returns and 23 local views."""
from pathlib import Path
import copy, datetime, json

w = Path(__file__).resolve().parents[1]
rs = [json.loads((w / f'readers/scan037/R{k}/return.json').read_text()) for k in (1,2,3)]
maps = {
1:[1,1,2,3,4,5,6,7,8,9,None,10,11,12,13,14,15,15,16,17,17,18,19,20,21,22,23,23,24,25,26,27,30,31,32,33,34,None,None,35],
3:[1,1,2,3,4,8,5,6,7,9,None,10,11,12,13,14,15,16,[18,19],20,21,22,23,24,25,27,28,26,29,30,31,34,36,37,38,40,39,None,None,41]
}
text_loci = {11:r'\Sigma_1^+',38:r'\Sigma_1^+,\Sigma_1^-,\Sigma_2^+,\Sigma_2^-',39:r'\Sigma_1^+,\Sigma_1^-,\Sigma_2^+,\Sigma_2^-'}

obs = {
1:'The heading ends in a low r return, with no detached point. Cor is underlined; C’s punctuation doubt is resolved.',
2:'White space follows the three heading letters. The letters ollaire supplied by H have no corresponding ink.',
3:'The broad D is crossed by a long rising oblique, independently of the heading underline. The low ans continues to its right without a crossing through those letters. R3’s deleted D with shared live ans is adopted. R1’s live-D alternative and R2’s cancelled-ans alternative are not retained. H’s note acknowledges the crossed D, but its body duplicates a complete Dans.',
4:'The rotated note contains one compact high-starting word with compressed medial strokes and a final s-like return. Strictes remains uncertain; H’s two-part ci-dessus does not match the visible group.',
5:'Two enclosing curves surround the compact crossed centre before soient. The parenthesized asterisk is resolved.',
6:'The line ends in inclu- and the next begins sion entre. No additional non triviales group lies between the two observed segments.',
7:'The fourth marginal low suffix ends in a short attached descent without the preceding clear 2’s low right foot. All three readers put 1 first. The same order, 1 then 2, is retained under uncertainty.',
8:'The tall hooked f has no detached point after it. The following et and short s with a point are visible; the written group is il f et s.',
9:'The small raised contraction contains joined shoulders and tightly merged uprights. Mutlt. remains first with R1/R3; R2’s mult. is retained as an explicit alternative. No expanded word replaces the ink.',
10:'The end of distincts is a connected return, without a separate low comma before the next-line et. C’s comma is removed.',
11:'The first high sign in (*) has a short cap and descending stem. The lower row’s plus has an upper rise, visible in the same crop. Top is first here, with plus retained. The same cap-and-downstem shape occurs at the later four recorded positions; the first occurrence carries the recurring uncertainty according to the supplied convention.',
12:'The local two-line crop contains inverses with its comma and the next beginning par hypothèse. No additional word or illegible ink span stands between them.',
13:'The underline begins under a and extends under pas, crossing its descender. H’s emphasis scope includes only pas.',
14:'The relation has an open upper and lower contour, a doubled left curve and a short internal upright. Subset remains first and membership remains possible; neither the grammar nor the formulas resolves the extra stroke.',
15:'Two Sigma bodies survive the zigzag cancellation. The first has a high crossed mark. Beside the second, no high sign separates securely from that cancellation. The cancelled first Sigma1-plus is followed by an uncertain Sigma1 with plus and minus alternatives, in that order. R2’s bare second term is adopted as primary; the other two complete readings are recorded.',
16:'The crop shows de followed by two separate horizontal bars. The lower bar has a hooked left start. The written two-bar abbreviation is retained as de =.',
17:'The target has a detached cap, angled return and low base, together with a thick central upright. Sigma remains first, E remains possible. The extra upright’s possible older state is recorded separately.',
18:'The target’s joined suffix has a rounded shoulder and downward terminal, without a separate rightward foot. R2’s 1-first order is adopted, with 2 retained against R1/R3’s 2-first order.',
19:'After puisque the second Sigma foot turns down without a detached numeral. Bare Sigma remains first. Its high mark is a cap with a downward stem, matching the first display’s top-shaped mark. The common ambiguity is marked at that first display and this occurrence uses top. Removing the common plus from C’s ordered pair of alternatives gives the two base alternatives, and appending it recovers C exactly; that reversible factoring alone is not a change. The visible superscript choice is a separate reading decision.',
20:'The local two-line band shows ou at the prior right end and a dotted initial i at the following left beginning inclusion. No l or apostrophe precedes that i.',
21:'After inverse and its comma there is one compact on followed by lit. H’s additional or has no separate written group. H’s doubt is on lit, not on the extra or; the final marked_in_H flag for this extra-word difference is no.',
22:'The old low word has a c-like opening and connected returns beneath the inserted p-descender and a cancellation. Cela remains uncertain.',
23:'The inserted article has a tall l and low a. Première has an accented vowel and a final low e-return after r. La première is resolved; H’s note already acknowledges its interlinear position.',
24:'The inserted p, two points and e/x strokes are readable. Their compact separation does not settle the spacing choice. R3’s p.ex. / p. ex. uncertainty is retained; R1 and R2’s different resolved spacings are both recorded. H’s explicit TeX space is not counted as a separate primary-text difference.',
25:'The long thin arch runs above the body of signifierait and attaches the interlinear qualification; it touches the tall f. The word body and que remain live. The later equation is crossed by its own straight line. The H rewriting note does not override this visible stroke geometry.',
26:'The cancelled operator has an independent wave above a short straight bar. The longer cancellation crosses the formula separately. Simeq is resolved.',
27:'The short cancelled connective begins with a d-like bowl and tall stroke, followed by a high trace and a crossed low ending. D’où remains first; R1’s de alternative is retained. H’s et is a different reading.',
28:'The broad revision crop includes the gap between the cancelled short connective and the live Sigma2-minus formula. No additional live implique letter group occupies that gap.',
29:'The next word has an open c and one low e-return before que. The visible group is ce, without H’s extra a/s sequence.',
30:'No point follows the heading f, resolving C’s terminal-point doubt. Above e, a short roof has a raised centre and two lower ends. R2’s Dêf is first, with Déf retained as a new accent uncertainty; R1/R3’s acute reading is recorded.',
31:'The first Pi has one cap and two long descending legs. Pi/pi uncertainty is retained at this first occurrence. This page supplies no separate contrasting case sample that would resolve it.',
32:'The underlined continuation has a descending p, low ana strokes, c/h and the accented ending ées. Panachées is retained. H’s parallèles differs here and again in the interlinear group, recorded separately.',
33:'One tall live l precedes doubled low loops and a heavy low crossing. The possible old es is local to the ending; no second l is visible. The chosen l plus uncertain deleted es plus live es follows R1/R3. R2’s shared le with only older s is recorded. Identity and cancellation versus reinforcement remain open.',
34:'The short group after distincts has a tall crossed final stroke and a detached low point, with an ambiguous opening/high speck. Et. remains first and i.e. remains possible with R1/R2; R3’s resolved et. is recorded. The final point is absent from H.',
35:'Two nested open curves stand between si and de. Both are retained with double opening parentheses first and c as the alternative; no closing partner is supplied.',
36:'The crop has a dotted i, one internal point and an e-return, then a broad blank before si. No terminal point follows e. The written form is i.e.',
37:'The article before ensembles has a tall looped l and low es. It reads les; H supplies ces.',
38:'In the first lower list, the first high mark has a cap and downstem. The third has a visibly crossed plus. The first follows the earlier top-shaped mark; its recurring plus alternative remains documented at the first occurrence.',
39:'In the repeated lower list, the first and third high marks each have a cap with a downward stem and no separately visible rise. They follow the first display’s top-shaped reading; the recurring alternative remains marked there.',
40:'The word following dit starts with a tall looped d, then low connected on and an open c. Donc is resolved; no initial a followed by a separate tall l is visible.',
41:'A thick additional upright traverses the target capital from its upper return to its base. It is preserved as an uncertain possibly deleted vertical stroke with R1/R3. R2’s account treats it within the live Sigma/E uncertainty. Its independent older identity and state remain open.',
42:'The second capital in the definition has a cap curling down to the right and an oblique descending branch. Pi remains first, with the R-like alternative retained from R3. R1/R2’s plain Pi is recorded.',
43:'The initial s of strictement is a large loop joined to t. Lowercase remains first and uppercase S remains possible, as R3 reports. R1/R2 resolve lowercase; this adds no H primary-text difference.',
44:'The added line repeats panachées with its p descent, low ana group, h and accented ending. H’s note correctly acknowledges the entire interlinear group; only the different word parallèles is counted.',
45:'The first low Pi suffix in (21) is a narrow downward stroke with an upward hook near the photographed lower edge. Its shape is less separated than the next 2. R3’s 1-first uncertainty with 2 retained is adopted.',
46:'Two detached points stand after non, one slightly lower and to the left of the other, above the underline. The colon-first reading with a period alternative reported by R1 is retained. R2/R3 omit these points in their complete texts.',
47:'The complete narrow rotated crop shows the long slightly wavering marginal rule, with a small break and offset near its middle. Both endpoints are visible. R1’s two-segment TikZ trace is adopted. C’s much shorter single typeset rule does not preserve the observed full extent. H’s explicit note acknowledges the vertical mark beside the definition; no additional H difference is counted from its note-to-mark representation alone.'
}

def src(k,n):
    return rs[k-1]['findings'][n-1]

def attach(f,k,nums,text=None):
    if nums is None:
        f['readers'][f'R{k}'] = text
        f['reader_source_ids'][f'R{k}'] = ['reading.tex, same locus']
    else:
        nums = nums if isinstance(nums,list) else [nums]
        f['readers'][f'R{k}'] = ' ; '.join(src(k,n)['reading'] for n in nums)
        f['reader_source_ids'][f'R{k}'] = [src(k,n)['id'] for n in nums]

def rpath(k,name): return f'readers/scan037/R{k}/crops/{name}.png'
def mpath(name): return f'crops/scan037/main_{name}.png'
crops = {**{i:rpath(3,'02_slanted_margin') for i in range(4,11)},1:rpath(3,'01_heading'),2:rpath(3,'01_heading'),3:rpath(3,'01_heading'),11:rpath(2,'15_first_display_sign'),12:mpath('inverses_par'),13:rpath(3,'03_proof_underline'),14:rpath(3,'04_second_relation'),15:rpath(3,'05_deleted_sigmas'),16:mpath('de_equal'),17:rpath(3,'06_sigma_target'),18:rpath(3,'06_sigma_target'),19:rpath(3,'07_puisque_sigmas'),20:mpath('ou_inclusion_on'),21:mpath('ou_inclusion_on'),**{i:rpath(1,'07_revised_proof') for i in range(22,30)},30:rpath(3,'11_definition_start'),31:rpath(2,'11_definition_pis'),32:mpath('panachees'),33:rpath(3,'13_old_les'),34:rpath(3,'14_et_si_marks'),35:rpath(3,'14_et_si_marks'),36:mpath('ie'),37:mpath('les_ensembles_later_signs'),38:mpath('lower_first_list'),39:mpath('les_ensembles_later_signs'),40:rpath(1,'12_bottom_display'),41:rpath(3,'06_sigma_target'),42:rpath(2,'11_definition_pis'),43:rpath(3,'12_definition_term'),44:mpath('panachees'),45:rpath(1,'12_bottom_display'),46:rpath(3,'12_definition_term'),47:mpath('marginal_rule')}

d={'scan':37,'folder':'J81-05','their_page':36,'hua_has':'text','filename':'J81-05_81_scan037.tex','status':'decided','findings':[]}
for i,raw in enumerate(rs[1]['findings'],1):
    f=copy.deepcopy(raw)
    f.update(id=f'SP41-037-{i:03d}',readers={},reader_source_ids={})
    for k in (1,3): attach(f,k,maps[k][i-1],text_loci.get(i))
    attach(f,2,i)
    f['marked_in_H']='yes' if f['marked_in_H'] else 'no'
    f['crop']=crops[i]
    f['evidence']='Main reader, personally viewed local crop(s): '+obs[i]
    f['main_adjudication']='All three complete texts and detailed returns, inventories, notes and metadata compared. The source IDs give every corresponding independent finding; see decisions/scan037_main_observations.md.'
    if i==2: f['kind']='abbreviation expanded or spelling modernised'
    if i==3: f.update(reading=r'\deleted{D}ans',confidence='high')
    if i==9: f['reading']=r'\inserted{\unsure{mutlt.|mult.}}'
    if i==15: f['reading']=r'\deleted{\Sigma_1^+,\unsure{\Sigma_1|\Sigma_1^+|\Sigma_1^-}}'
    if i==21: f['marked_in_H']='no'
    if i==24: f.update(reading=r'\unsure{p.ex.|p. ex.}',against_C=False,c_doubt_status='retained',confidence='medium',kind='other')
    if i==27: f.update(reading=r"\deleted{\unsure{d'où|de}}",against_C=True)
    if i==32: f.update(place='Definition, underlined panachées',bbox=[303,1790,585,1873]); f.pop('component_bboxes',None)
    if i==33: f['reading']=r'l\unsure{\deleted{es}}es'
    if i in (7,11,18,19,32,38,39): f['consequential']='The written primary form is retained from its observed strokes; no replacement based on the surrounding mathematical argument is supplied.'
    d['findings'].append(f)

extras=[
(41,3,17,{1:(15,None),2:(17,None),3:(17,None)}),
(42,3,32,{1:(26,None),2:(31,None),3:(32,None)}),
(43,3,33,{1:(None,'strictement'),2:(None,'strictement'),3:(33,None)}),
(44,3,35,{1:(29,None),2:(32,None),3:(35,None)}),
(45,3,42,{1:(None,r'\Pi_1'),2:(None,r'\Pi_1'),3:(42,None)}),
(46,1,28,{1:(28,None),2:(None,'absent'),3:(None,'absent')})]
for i,k,n,mapping in extras:
    f=copy.deepcopy(src(k,n)); f.update(id=f'SP41-037-{i:03d}',readers={},reader_source_ids={})
    for rk,(rn,txt) in mapping.items(): attach(f,rk,rn,txt)
    f['marked_in_H']='yes' if f['marked_in_H'] else 'no'
    f.update(crop=crops[i],evidence='Main reader, personally viewed local crop(s): '+obs[i],main_adjudication='All three complete texts and detailed returns compared; exact source IDs and text loci recorded.')
    if i==41: f['reading']=r'\unsure{\deleted{\vert}}'
    d['findings'].append(f)
d['findings'].append({'id':'SP41-037-047','place':'Long left rule beside the definition','c':r'\rule[-9ex]{.4pt}{10.5ex}','h':"la définition est marquée d'un trait vertical dans la marge",'reading':'Two long, slightly wavering TikZ segments beside the definition, with the small intervening break retained.','against_C':True,'against_H':False,'kind':'drawing or diagram','marked_in_H':'no','confidence':'high','evidence':'Main reader, personally viewed complete local crop: '+obs[47],'bbox':[263,1739,288,2318],'crop':crops[47],'c_doubt_status':'none','c_doubt_ids':[],'mathematical_note':'','readers':{'R1':'Two-segment TikZ trace, with a small break','R2':r'\rule[-30ex]{.4pt}{32ex}','R3':r'\rule[-30ex]{.4pt}{31.5ex}'},'reader_source_ids':{'R1':['reading.tex and marginal-rule inventory'],'R2':['reading.tex and marginal-rule inventory'],'R3':['reading.tex and marginal-rule inventory']},'main_adjudication':'The complete crop supports the two-segment trace and long extent.'})

coverage={}
for k in (1,2,3):
    used={s for f in d['findings'] for s in f['reader_source_ids'][f'R{k}'] if s.startswith('scan037-')}
    expected={f['id'] for f in rs[k-1]['findings']}
    assert used==expected,(k,expected-used,used-expected)
    coverage[f'R{k}']={'raw_findings':len(expected),'mapped_findings':len(used),'all_mapped':True}
d['reader_finding_coverage']=coverage

t=(w/'readers/scan037/R1/reading.tex').read_text()
replacements={
r'\unsure{\deleted{D}|D}ans':r'\deleted{D}ans',
r'\inserted{\unsure{mutlt.}}':r'\inserted{\unsure{mutlt.|mult.}}',
r'\Sigma_1^+&\subset\Sigma_2^-':r'\Sigma_1^{\unsure{\top|+}}&\subset\Sigma_2^-',
r'\deleted{\unsure{\Sigma_1^+,\Sigma_1^+|\Sigma_1^+,\Sigma_1^-|\Sigma_1^+,\Sigma_1}}':r'\deleted{\Sigma_1^+,\unsure{\Sigma_1|\Sigma_1^+|\Sigma_1^-}}',
r'{\unsure{\Sigma|E}}_{\unsure{2|1}}^-':r'{\unsure{\Sigma|E}}_{\unsure{1|2}}^-',
r'\unsure{\Sigma|\Sigma_2}^{\unsure{\top|+}}':r'\unsure{\Sigma|\Sigma_2}^{\top}',
r'\inserted{la première p.ex.}':r'\inserted{la première \unsure{p.ex.|p. ex.}}',
r'\uline{Déf}':r'\uline{\unsure{Dêf|Déf}}',
r'\unsure{\Pi|\pi}_1,\Pi_2':r'\unsure{\Pi|\pi}_1,\unsure{\Pi|R}_2',
r'\uline{strictement non':r'\uline{\unsure{strictement|Strictement} non',
r'\text{on dit donc que }\Pi_1':r'\text{on dit donc que }\Pi_{\unsure{1|2}}'
}
for old,new in replacements.items():
    assert t.count(old)==1,(old,t.count(old))
    t=t.replace(old,new)
anchor='si l'+r'\unsure{\deleted{es}}es quatre ensembles '
a,b=t.split(anchor)
b=b.replace(r'$\Sigma_1^+,\Sigma_1^-,\Sigma_2^+,\Sigma_2^-$',r'$\Sigma_1^\top,\Sigma_1^-,\Sigma_2^+,\Sigma_2^-$',1)
old=r'$\Sigma_1^+,\Sigma_1^-,\Sigma_2^+,\Sigma_2^-$'
assert b.count(old)==1
b=b.replace(old,r'$\Sigma_1^\top,\Sigma_1^-,\Sigma_2^\top,\Sigma_2^-$')
t=a+anchor+b

d['inventory']=copy.deepcopy(rs[2]['inventory'])
for e in d['inventory']:
    name=e['element']
    if name=='Cancelled initial Sigma pair': e['first_words_or_objects']=r'\Sigma_1^+,\unsure{\Sigma_1|\Sigma_1^+|\Sigma_1^-}'
    if name=='Definition heading': e['first_words_or_objects']='Dêf / Déf'
    if name=='Paired inclusion display': e['first_words_or_objects']='(*) Sigma1-top/plus subset Sigma2-minus; Sigma2-plus subset Sigma1-minus'
    if name=='Long marginal emphasis rule beside definition':
        e.update(kind='drawing',position=[263,1739,288,2318],first_words_or_objects='two long wavering segments with a small break',representation='TikZ trace in narrow left minipage')
        e.pop('classification',None)

u=copy.deepcopy(rs[2]['unresolved'])
for z in u:
    if z['place']=='Raised marginal contraction': z['alternatives']=['mult.']
    if z['place']=='Cancelled two-Sigma starter': z.update(reading=r'\Sigma_1^+,\Sigma_1',alternatives=[r'\Sigma_1^+,\Sigma_1^+',r'\Sigma_1^+,\Sigma_1^-'],reason=obs[15])
    if z['place']=='That target’s low numeral': z.update(reading='1',alternatives=['2'],reason=obs[18])
    if z['place']=='High sign on that Sigma': z.update(place='First top-shaped superscript in (*), recurring at four later recorded positions',reason=obs[11]+' '+obs[19]+' '+obs[38]+' '+obs[39])
    if z['place']=='Cancelled connective before final equality': z['alternatives']=['de']
u.extend([
{'place':'Definition heading accent','reading':'Dêf','alternatives':['Déf'],'confidence':'medium','reason':obs[30]},
{'place':'Punctuation after non','reading':':','alternatives':['.'],'confidence':'low','reason':obs[46]},
{'place':'Connector after distincts','reading':'et.','alternatives':['i.e.'],'confidence':'low','reason':obs[34]}
])
d['unresolved']=u
assert t.count(r'\unsure{')==len(u),(t.count(r'\unsure{'),len(u))
d['notation']=[{'scan':37,'form':f['place'],'evidence':f['evidence'],'reading':f['reading']} for f in d['findings'] if int(f['id'].split('-')[-1]) in [7,9,11,14,15,16,17,18,19,26,30,31,33,34,35,38,39,41,42,45,46]]
d['abbreviations']=copy.deepcopy(rs[2]['abbreviations'])
for z in d['abbreviations']:
    if z['form']=='Déf': z['form']='Dêf / Déf'
    if z['form']=='mutlt.': z['form']='mutlt. / mult. (uncertain)'
notes=[
'This handwritten sheet has an underlined Cor heading, a lower definition heading, display labels (*) and (21), and pencil archive number 36. No authored date, separate page number, question mark or verification instruction was observed. A long broken marginal rule marks the definition and is reproduced with its small break.',
'The opening source statement uses Card with empty braces and 4, followed by the inserted two exclusion conditions. No members are supplied in the empty braces. The slanted Sous forme : passage retains il f et s., the parenthesized asterisk, and the uncertain raised contraction. Its fourth Sigma index has 1 first, with 2 still possible; the list pattern does not decide it.',
'The proof discusses inverse and same-index inclusions. Its wording includes par hypothèse, car on aurait and Il reste à voir. It refers to le diagramme (14), without a diagram on this sheet. These are accounts of the written argument, not independently checked implications.',
'The high marks in the first display, the second Sigma after puisque, the first member of the first lower list and the first and third members of the repeated lower list have a cap and downward stem. These five locations are linked by their observed shape in the crops. Top is the first reading and plus remains the alternative at the first occurrence, following the supplied convention. Other visible crossed plus marks remain plus. No semantic interpretation is assigned to the top-shaped glyph.',
'In the cancelled pair, the second exponent is obscured by the zigzag. The transcription puts the bare second Sigma1 first, retaining plus and minus alternatives. A later target preserves the possible older vertical, Sigma/E and a 1/2 index doubt. The base after puisque remains bare Sigma first with Sigma2 possible. None of these choices is inferred from the expected pair symmetry.',
'The interlinear la première is resolved, while p.ex. / p. ex. spacing remains uncertain. Signifierait que is live beneath the insertion leader; the separate equation is cancelled and its simeq is resolved. The following cancelled d’où/de remains uncertain. The source concludes Sigma2-minus = X, ce que l’on a exclu. H’s extra implique is not supported by the visible band.',
'The definition twice writes panachées. The initial case of strictement, dots after non, Pi case, the second Pi/R form and the accent of Dêf/Déf remain uncertain. The possible old es in les shares one live l. Et./i.e. and the two curved marks before de plus remain uncertain. The later article reads les and the written abbreviation has no terminal point after i.e. The final parenthesis reads on dit donc que; its first low Pi suffix retains 1/2 uncertainty.',
'Every C doubt ID has a decision: seven resolved and fourteen retained. There are twenty-two uncertainty macros and twenty-two unresolved entries. All three complete texts and all detailed returns were compared, and every raw finding has an explicit correspondence in the final record. The main reader inspected twenty-three local crops. The source accounts and stroke comparisons are not mathematical proof checks; no OCR, external research or compilation was performed.'
]
d['notes']=[{'id':f'scan037-note-{i:02d}','text':n} for i,n in enumerate(notes,1)]
d['check_events']=[{'statement_id':n['id'],'date':'2026-11-20','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader scan037','type':'carried as background without fault found','outcome':'Source-account and ink/witness comparison only; no independent mathematical verification claimed.'} for n in d['notes']]
d['sweep']=[]
d['main_crop_views']={'R1':[7,12],'R2':[11,15],'R3':[1,2,3,4,5,6,7,11,12,13,14],'main_new':8,'total':23}
d['crop_counts']={'R1':12,'R2':15,'R3':15,'main':8,'total':50}
d['decided_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
record='# Scan037 main-reader local observations\n\nAll three complete texts and every detailed finding, inventory, note and metadata field were read. Root viewed only local crops.\n\n'
record+='\n\n'.join(f'{i}. {obs[i]}\n\n   Crop: `{crops[i]}`' for i in sorted(obs))
record+='\n\nThe root’s first attempted view of R3 crop01 returned only an output-truncation message and supplied no image; its later successful delivery is the counted view. No image was recreated by that failure. New crops contain each target completely; adjacent context may be cut. The final line is close to the source’s physical edge.\n'
(w/'decisions/scan037_main_observations.md').write_text(record)
(w/'decisions/drafts/scan037_main_draft.tex').write_text(t)
(w/'pages'/d['filename']).write_text(t)
(w/'decisions/scan037.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print(json.dumps({'findings':len(d['findings']),'against_C':sum(f['against_C'] for f in d['findings']),'against_H':sum(f['against_H'] for f in d['findings']),'unresolved':len(u),'coverage':coverage}))
