from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, re
root=Path('/workspace/scratch/4770596940a0')
rows=[]
def d(id,place,C,H,reading,ink,confidence,kind,crop,against_C=False,against_H=True,marked_in_H=False,review_only=False):
    rows.append(dict(id=id,place=place,C=C,H=H,reading=reading,ink=ink,confidence=confidence,kind=kind,crop='crops/R2/scan029_'+crop+'.png',against_C=against_C,against_H=against_H,marked_in_H=marked_in_H,review_only=review_only))
d('D01','first proposition: F',r'\unsure{F|\mathcal F}','F','F','A simple upright with two rightward arms and no script loop; its shape agrees with the plain F of the product.','high','other','top',True,False)
d('D02','first heading',r'\uline{Proposition}',r'\textbf{Proposition}',r'\uline{Proposition}','One underline below the word, laid down in adjacent strokes; no second complete underline.','high','other','top')
d('D03','first proposition, after ll',"on … l'appelle","qu'on appelle","on … l'appelle",'The on is a small rounded stroke and separate low n; no q descender. The live l and apostrophe stand before appelle.','high','misread word','top_deletion')
d('D04','first proposition, cancelled letter before l’appelle',r'\deleted{\unsure{y|l}}','omitted',r'\deleted{\unsure{y|l}}','A rubbed/retraced descending stem with an upper branch survives before the new l. y and l cannot be separated securely.','low','omission','top_deletion')
d('D05','name figure intersection: quotation marks',"``figure intersection''",'« figure intersection »',"``figure intersection''",'Two short strokes at each end; no angled guillemet shapes.','high','other','top')
d('D06','warning: n’est pas',r'\uline{n\text{’}est pas}','n’est pas, no underline',r"\uline{n'est pas}",'A single rule runs under the complete negative expression and stops at pas.','high','other','warning')
d('D07','warning: interlinear insertion',r'\inserted{\unsure{en général}}',r'\add{en général}',r'\inserted{\unsure{en général}}','en-like low wave, g descender, high accent, compressed middle and final rising letter; linking sweep places it before la figure. The compressed middle remains uncertain.','medium','other','insertion')
d('D08','warning: la figure', 'live la figure',r'\struck{la figure}','live la figure','The long rising sweep belongs to the interlinear insertion and passes above the words. Neither word is struck through.','high','deletion state','warning')
d('D09','warning: cancelled word after F cap G',r'\deleted{\unsure{intersection|inter.}}',r'\struck{\ill{}}',r'\deleted{\unsure{inter.|intersection}}','Initial short dotted stroke and medial t-like peak survive. The short run has a distinct terminal dot, favouring abbreviated inter.; full intersection remains possible under the horizontal cancellation.','low','readable ink left as \\ill{}','warning_deleted',True,True,True)
d('D10','warning: connecting words','en se rappelant','où on rappelle','en se rappelant','Separate low en, short se, then r and two descending p strokes, looped l and final raised ending. The ink is longer than rappelle and has no où accent.','high','misread word','warning')
d('D11','warning: F overwritten by G',r'F,\deleted{\unsure{F}}G','F,G',r'F,\deleted{F}G','The smaller upright and two crossbars remain inside the larger round G. The lower letter can be read as F.','high','omission','warning_symbols',True,True)
d('D12','warning: powerset letter alphabet',r'\unsure{\mathfrak P|\mathscr P|\mathbb P}',r'\mathfrak P',r'\unsure{\mathfrak P|\mathscr P|\mathbb P}','Tall descending shaft crosses a broad upper enclosure and a lower left hook. P is clear, but the hand does not securely distinguish these alphabet renderings.','low','other','warning_symbols')
d('D13','warning: live argument of powerset','L',r'\mathcal L','L','Angular upright with a rightward foot, without the large loop of a script L.','high','misread symbol or index','warning_symbols')
d('D14','warning: argument of cancelled powerset expression','L',r'\mathcal L','L','Despite two horizontal cancellation strokes, the angled stem and right foot remain; no separately visible loop.','medium','misread symbol or index','warning_symbols')
d('D15','end of warning after cancelled G subset P(L)','no final point','final point','no final point','The closing parenthesis reaches toward the right margin; there is no separate full stop after it. The comma before the cancelled expression is present.','high','text not on the page','warning_symbols')
d('D16','paragraph boundary before Nous n’allons','new paragraph','same paragraph as warning','new paragraph','Nous begins a new block at the left body margin below the warning, with its own continuation lines.','medium','other','middle')
d('D17','Donc paragraph: article before F.G','le','la','le','Tall l ends in a short open e-shaped foot; there is no closed a body.','high','misread word','middle')
d('D18','Donc paragraph: after En fait','ça marche','se construit','ça marche','A curved ç-like beginning and small a precede the m-a-r-c-h-e run, with a distinct tall h. No constructed sequence of consonants supports construit.','high','misread word','middle')
d('D19','lower paragraph: verb after ll',r"\unsure{s'apparente}","l'apparente",r"\unsure{s'apparente|l'apparente}",'Initial narrow hooked stroke can be reduced s or l, followed by a clear apostrophe. The p strokes are retraced; the rest supports apparente. I retain s first, but the ink does not exclude H’s l.','low','misread word','verb',True,True)
d('D20','lower paragraph: cancelled phrase and placement',r'\deleted{\unsure{la propriété|la présentation}} before à',r'\struck{\ill{}} after de',r'\deleted{\unsure{la propriété|la présentation}} before à','A looped article, p descender and a tall ending with accent survive beneath one horizontal stroke. The cancelled phrase precedes the separate à une propriété de; it is not between de and the quoted term.','low','readable ink left as \\ill{}','moderation',False,True,True)
d('D21','lower paragraph: underlined quoted term',r'\uline{\unsure{modération|médiation}}',r'\uncertain{demi-treillis}',r'\uline{modération}','Low initial m, separate small o, looped d and accented following e are visible; then reduced r/a and tall t with i/on ending. Single continuous word, with a rule beneath it.','high','misread word','quoted_word',True,True,True)
d('D22','lower paragraph: quotation marks',"``modération''",'« demi-treillis »',"``modération''",'Two short opening strokes and two closing strokes stand above the baseline; these are double quotation marks, not guillemets.','high','other','quoted_word')
d('D23','foot: heading',r'\uline{Propriété}',r'\textbf{Proposition}',r'\uline{Propriété}','P-r-o, then descending p, r/i and the tall té ending with accent. A single rule lies below the word.','high','misread word','foot')
d('D24','foot: whole statement cancellation',r'\deleted{whole statement}','body live; editorial note says it is cancelled',r'\deleted{whole statement}','Several long oblique strokes pass through all three lines, including the heading, formulas, parenthesis and final sentence. They are not mathematical strokes.','high','deletion state','foot')
d('D25','foot: material between F prime and first order sign','no separate cancelled token',r"F' \struck{\ill{}} \preccurlyeq F",r"F'\preceq F",'The first order sign is looped/retraced. I cannot isolate an additional cancelled word or symbol before it; the extra ink is contiguous with the sign. No independent deleted token is asserted.','medium','text not on the page','footer_condition',False,True,True)
d('D26','foot: internal cancellation after first F',r'\deleted{\unsure{, et des}}',r'\struck{\ill{}}',r'\deleted{\unsure{, et des|, et de}}','A comma-like downward hook, low e/t run with a tall peak, and looped d survive. The final tail can be des or de; the horizontal strokes obscure its exact endpoint.','low','readable ink left as \\ill{}','footer_condition',True,True,True)
d('D27','foot: parenthetical initial word',r'\unsure{Immédiat|Immédit|immédite}',r'\uncertain{Immédiat}',r'\unsure{Immédiat|Immédit|immédite}','Tall barred initial I, two low m groups, accent, d loop and final tall t survive. The cancellation crosses the i/a region, so I retain C’s ending alternatives.','medium','other','foot',False,True,True)
d('D28','foot: parenthetical supports','supports',r'\ill{}','supports','Angular s, low u, two descenders of pp and final r/t/s run remain legible through the oblique cancellation.','high','readable ink left as \\ill{}','foot',False,True,True)
d('D29','foot: induite emphasis',r'\uline{induite}',r'\emph{induite}',r'\uline{induite}','A distinct long rule runs immediately below the word. It is separate from the steep cancellation stroke.','high','other','footer_lastline')
d('D30','foot: final preposition','sur','par','sur','The first small comma-shaped s is crossed by the long oblique cancellation; the following letter is an open u, not a closed a. The long descender at its left belongs to cancellation, not p.','high','misread word','footer_lastline')
d('D31','foot: relation signs',r'\preceq, \preceq',r'\preccurlyeq, \preccurlyeq',r'\preceq, \preceq','Both are the round-backed precedence relation with a second lower stroke; the first is heavily retraced. I retain the notation already used in my page stream. The two witness commands are treated here as renderings of this same relation, not a new mathematical difference.','medium','other','footer_condition',False,False,False,True)

cd=[
('C01','F / calligraphic F','D01','resolved','Plain F.'),
('C02','cancelled y / l','D04','retained','Neither cancelled letter is secure.'),
('C03','inserted en général','D07','retained','Compressed middle remains uncertain.'),
('C04','cancelled intersection / inter.','D09','revised','Both retained; visible final point and short span favour inter. first.'),
('C05','overwritten F under G','D11','resolved','Two arms on the older upright are legible.'),
('C06','powerset alphabet','D12','retained','P clear, alphabet unsettled.'),
('C07',"s’apparente",'D19','revised','Retain s first and add l alternative permitted by initial hooked stroke.'),
('C08','cancelled la propriété / la présentation','D20','retained','Strike crosses the middle of the noun.'),
('C09','modération / médiation','D21','resolved','Separate o before d decides modération.'),
('C10','cancelled , et des','D26','revised','Add , et de as possible ending under the strike.'),
('C11','Immédiat / Immédit / immédite','D27','retained','Final internal vowel sequence remains obscured.')]
cd=[dict(id=a,locus=b,difference_id=c,status=d,reason=e) for a,b,c,d,e in cd]
inv=[]
def item(element,kind,position,first,details=''):
    inv.append(dict(scan=29,sheet_kind='text',hand='his hand',element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes',details=details))
item('page number','text','top centre','28')
item('false start','deletion','top left','Alors','Thick horizontal cancellation.')
item('new opening','text','below false start','Ainsi')
item('intersection proposition','text','upper block','Proposition On a construit','Heading underlined; full three-line statement and product F.G.')
item('discarded letter','deletion','upper proposition before l’appelle','y|l','Rubbed/retraced stem.')
item('warning','text','below proposition','Attention, ce n’est pas','Underline under n’est pas; F cap G and inclusion preserved.')
item('qualification','insertion','above la figure','en général','Interlinear linking sweep; placed before la figure.')
item('deleted intersection word','deletion','warning after F cap G','inter.|intersection')
item('overwritten capital','deletion','warning in F,G','F','Older F beneath live G.')
item('repeated inclusion','deletion','warning right end','G subset P(L)','Two horizontal strokes.')
item('compatibility paragraph','text','middle upper','Nous n’allons considérer','No sont supplied between G and compatibles.')
item('arbitrary-family paragraph','text','middle','Donc la bonne notion','le F.G; ça marche; famille quelconque de figures.')
item('support formula','display','middle lower','|bigwedge Fi| = bigcap |Fi|','Both index ranges i in I; two i subscripts; all four support bars and final point.')
item('comparison paragraph','text','lower','Cette propriété d’existence','Inf, relation ll, uncertain initial of apparente.')
item('discarded phrase','deletion','lower paragraph before à une','la propriété|la présentation','One horizontal stroke.')
item('quoted term','text','lower paragraph last line','modération','Double quotes, underline and full stop.')
item('cancelled property','deletion','foot, all three lines','Propriété Si F prime preceq F','Entire block under oblique hatching; full formulas and parenthesis retained.')
item('internal false continuation','deletion','foot first line after F',', et des|, et de','Within the larger deleted block.')
item('support parenthesis','text','foot second line','(Immédiat sur supports)','Inside cancelled block; colon follows.')
item('final explanatory sentence','text','foot second/third lines','Subdivision induite sur un raffinement','Inside cancelled block; induite underlined; final point.')

manifest=json.loads((root/'out/readers/R2/crops029.json').read_text())
images=[dict(path=f'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan029{s}.jpg',role=role) for s,role in [('', 'whole'),('_a','upper half'),('_b','lower half')]]
images += [dict(path=x['path'],role='enlarged crop') for x in manifest]
tex=(root/'out/readers/R2/scan029.tex').read_text()
# Syntax-only validation: no compilation, no OCR.
body=re.sub(r'%[^\n]*','',tex)
depth=0
for i,ch in enumerate(body):
    if ch=='{' and (i==0 or body[i-1]!='\\'): depth+=1
    if ch=='}' and (i==0 or body[i-1]!='\\'): depth-=1
    assert depth>=0
assert depth==0
assert body.count('\\[')==body.count('\\]')==1
assert len(re.findall(r'(?<!\\)\$',body))%2==0
report=dict(
 scan=29,manuscript_page=28,reader='R2',model='inherited; no separate model identifier used',effort='inherited',
 start_utc=(root/'out/readers/R2/start029.txt').read_text().strip(),end_utc=datetime.now(timezone.utc).isoformat(),
 independence='Only supplied witnesses, the page images and my own outputs were read. No other reader files or root decisions inspected; no later scan advanced.',
 procedure='Whole image, upper half, lower half, line-by-line reading and enlargement of disagreements, C doubts, decisive notation and every cancelled block. A truncated earlier multi-image tool response was not counted; every listed image was subsequently emitted and viewed explicitly.',
 comparison_policy='against_C and against_H include changes to uncertainty markers/candidate sets and diplomatic state; equivalent macro syntax alone is ignored. All C doubt decisions have entries, including retained reviews. H preccurlyeq versus C preceq is recorded as same relation rendering at D31.',
 images_viewed=images,crops=manifest,differences=rows,C_doubt_resolutions=cd,
 S_row_decisions=[dict(row_id=None,decision='not applicable',reason='No row of 156-5_CORRECTIONS.tsv covers scan029.')],
 inventory=inv,absences=['No marginal or sideways note','No diagram or drawing','No title or date','No archive sheet number distinct from manuscript page 28'],
 remaining_doubts=[dict(id=x['id'],difference_id=x['difference_id'],locus=x['locus'],reason=x['reason']) for x in cd if x['status']!='resolved'],
 notation=[
  dict(locus='first proposition and lower paragraph',latex=r'\ll',ink='Two open left-pointing wedges; distinct from foot order sign.'),
  dict(locus='first proposition and product formulas',latex='F.G',ink='Separate low dot between plain capital F and rounded G.'),
  dict(locus='warning, two occurrences',latex=r'\subset, \unsure{\mathfrak P|\mathscr P|\mathbb P}(L)',ink='Open-right curved inclusion; P alphabet uncertain at first occurrence; ordinary angular L.'),
  dict(locus='support display',latex=r'\left|\bigwedge_{i\in I}F_i\right|=\bigcap_{i\in I}|F_i|',ink='Angular meet versus round cap; both indices dotted i, short membership sign and barred capital I; Fi has lower i each time.'),
  dict(locus='foot formulas',latex=r"F'\preceq F,\quad F'.G\preceq F.G",ink='Elevated single primes; round-backed order signs with lower stroke; low product dots. First order sign retraced.'),
  dict(locus='quoted names',latex="``…''",ink='Paired small strokes, not guillemets.')],
 notes_while_reading=[
  'The live proposition calls the constructed Inf for ll the figure intersection F.G. This is a report of the manuscript claim, not a proof check.',
  'The warning distinguishes that figure from the literal family intersection F cap G; the next paragraph says they coincide for compatible figures. It omits sont after F et G; the omission is retained.',
  'The page extends the construction to an arbitrary indexed family and writes the support of its meet as the intersection of its supports.',
  'The next paragraph describes existence of an Inf using the quoted term modération; H’s demi-treillis is not supported by the letters.',
  'The cancelled property asserts F prime preceq F implies F prime.G preceq F.G, calls this immediate on supports, and describes subdivision induced on a refinement. Its cancellation is part of the diplomatic text.',
  'The relation in the meet construction is ll, while the cancelled property uses the different precedence relation. I did not infer one from the other or use the expected mathematics to choose a letter.',
  'No mathematical proof, counterexample or computation was attempted on this page. Formula parsing and symbol comparison were reading checks only.'
 ],
 mathematical_checks_actually_performed=[],
 check_events=[dict(statement_id=f'156-5-029-R2-{k}',type='carried as background without fault found',outcome=v) for k,v in [
 ('claim1','Read the stated meet construction; not independently verified.'),
 ('claim2','Read the compatibility claim; not independently verified.'),
 ('claim3','Read the arbitrary-meet support formula; not independently verified.'),
 ('cancelled-claim','Read the cancelled monotonicity assertion; not independently verified.')]],
 syntax_validation=dict(braces_balanced=True,math_dollars_even=True,display_pairs=1,compiled=False),
 proposed_tex='out/readers/R2/scan029.tex',proposed_tex_sha256=hashlib.sha256(tex.encode()).hexdigest(),
 summary=dict(difference_or_review_rows=len(rows),C_doubts_reviewed=len(cd),C_doubts_resolved=sum(x['status']=='resolved' for x in cd),remaining_doubts=sum(x['status']!='resolved' for x in cd),inventory_elements=len(inv),crops_viewed=len(manifest),against_C=sum(x['against_C'] for x in rows),against_H=sum(x['against_H'] for x in rows))
)
(root/'out/readers/R2/scan029.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report['summary'],ensure_ascii=False))
print('Saved',report['proposed_tex'],'and out/readers/R2/scan029.json')
