from pathlib import Path
from datetime import datetime, timezone
import json, re
R=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_070/R3')
P=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_070')
meta=json.loads((P/'metadata.json').read_text()); images=meta['images']; whole,half_a,half_b=images
crops=json.loads((R/'crop_manifest.json').read_text())
tex=(R/'reading.tex').read_text(); ctex=(P/'C.tex').read_text(); htex=(P/'H.tex').read_text()
D=[]
def diff(loc,c,h,reading,shows,kind='other',confidence='high',hc='no',cc=False,ch=False,n=None,bbox=None,source=None,math=False):
    crop=crops[n-1] if n else None
    D.append(dict(id=f'R3-D{len(D)+1:02d}',location=loc,c=c,h=h,reading=reading,scan_shows=shows,confidence=confidence,kind=kind,marked_in_h=hc,change_c=cc,change_h=ch,crop=crop['path'] if crop else None,bbox=bbox or (crop['bbox'] if crop else None),bbox_image=source or (crop['source'] if crop else None),math_consequential=math))
# Opening paragraph. All quoted witness strings are scoped to the relevant manuscript locus.
diff('Opening, rel before d\'ordre','rel','rel.','rel','The final l has a descending return but no separate abbreviation point in the following blank.',ch=True,n=1)
diff('Opening order relation',r'\unsure{\preceq|\leqslant}',r'\preccurlyeq',r'\preceq','The upper angle and bowed lower stroke are visibly distinct from the final straight less-than-or-equal sign. H uses an equivalent bowed-order macro; only C\'s unresolved straight-sign alternative changes here.',kind='misread symbol or index',cc=True,n=1,math=True)
diff('After (subdivision)','(subdivision),','(subdivision)','(subdivision),','A separate comma lies below and after the closing parenthesis at the far right.',ch=True,n=1)
diff('Opening, de nature très',r'\unsure{très|trs}','très',r'\unsure{très|trs}','A t, reduced middle wave and last short stroke are visible; the small raised mark does not isolate a complete e securely. H\'s unqualified reading is stronger than the ink.',confidence='medium',ch=True,n=1)
diff('Opening, after Il n\'y',r'\unsure{aura}','a','aura','The low au group is followed by a separate ra group on the same baseline. These are the four letters of aura, despite the internal gap.',kind='misread word',cc=True,ch=True,n=1)
diff('Opening, cancelled noun after deux',r'\deleted{\unsure{éléments|élémen}}',r'\struck{\ill{}}',r'\deleted{\unsure{éléments|élémen}}','The opening accented loop and tall l, a second accented group, and the reduced remaining noun are visible under one long cancellation. Its final letters remain covered; no unqualified plural ending is asserted.',kind=r'readable ink left as \ill{}',confidence='low',hc='yes',ch=True,n=2)
diff('Opening, live figures after cancelled noun','figures','','figures','A full live word figures stands at the start of the following baseline, below the raised F labels. H omits this live word.',kind='omission',ch=True,n=3,bbox=[250,525,470,625])
diff('Opening, raised formula over figures',r'\inserted{$F\',F\'\'\preceq-$}',r'\add{$F\'$, $F\'\'$} \struck{$\preccurlyeq$}',r'\inserted{$F\',F\'\'\,\unsure{\preceq|\deleted{\preceq}}-$}','One and two primes are distinct. The relation lies on the same raised level and has heavy retracing, but no independently secure cancelling stroke. A short separate dash follows it. Both the ink state and its raised placement are preserved.',kind='deletion state (struck given live or live given struck)',confidence='low',cc=True,ch=True,n=3,math=True)
diff('Opening, word after figures and the raised condition',r'\unsure{en général|en position}','toujours','toujours','The long slant at the start is the t stroke; reduced ou precedes a descending j, followed by the low ours sequence. There is no tall terminal l as in général. This supports toujours from the ink.',kind='misread word',confidence='high',cc=True,n=3,math=True)
diff('Opening, dotted explanation group',r'\unsure{(i.e.|liée.|lire.}','(i.e.','(i.e.','The first stroke is an open parenthesis, then a short dotted i and the separate stops around the reduced e. There is no separate initial l stem.',kind='misread word',cc=True,n=3)
diff('Opening, initial of Subdivisions','Subdivisions','subdivisions','Subdivisions','The initial S is a separate tall capital form, larger than the following small letters.',ch=True,n=2,bbox=[1070,485,1435,560])
diff('Opening, between une and figure',r'\unsure{=|même}','même','=','Two short parallel strokes occupy this space; there is no letter sequence même.',kind='misread symbol or index',cc=True,ch=True,n=3,bbox=[440,620,535,675])
diff('Opening, punctuation after figure F',r'figure $F$,',r'figure $F$),',r'figure $F$,','A comma follows F, without a closing parenthesis. The opening (i.e. remains unmatched on the page.',kind='text not on the page',ch=True,n=3,bbox=[875,570,1010,670])
# Second paragraph.
diff('Second paragraph, deux subdivision','deux subdivision','deux subdivisions','deux subdivision','The word ends in the single extended n sweep before the blank and F; no separate plural s is visible.',kind='abbreviation expanded or spelling modernised',ch=True,n=5,bbox=[960,765,1390,840])
diff('Second paragraph, second F label',r"F',\unsure{F'''|F''}",r"$F'$, $F''$",r"F',F'''",'Three short separate prime strokes stand beside the second F. The first F has one. This is a name change within the sentence, not a mathematical validation or a claim of changed truth conditions.',kind='misread symbol or index',cc=True,ch=True,n=5,bbox=[1410,745,1585,835])
diff('Second paragraph, underlined overwritten adjective',r'\uline{comp\deleted{\unsure{ati|atib}}\unsure{ara|ati|ata}bles}',r'\emph{\uncertain{compatibles}}',r'\uline{comp\deleted{\unsure{ati|atib}}\unsure{ara|ati|ata}bles}','One word-sized cluster has a readable comp and bles around heavily worked middle letters. Upright and dotted older strokes remain under new loops. The old and final middle are both uncertain; no second full older word is invented.',kind='deletion state (struck given live or live given struck)',confidence='low',hc='yes',ch=True,n=4,math=True)
diff('Second paragraph, cancelled phrase following adjective',r'\deleted{\unsure{on dit|c.à.d.} que \unsure{sub}}',r'\struck{quand et que seulement}',r'\deleted{\unsure{quand et|on dit} que \unsure{seul|sub}}','Before the clear que, joined low strokes and two tall strokes best fit quand et but can still be segmented as on dit. The final group has s, a low joined middle and one final tall stem; a full seulement is not recoverable beyond it.',kind='misread word',confidence='low',cc=True,ch=True,n=5,bbox=[1050,840,1625,955])
diff('Second paragraph, quotation marks around compatibles',"``compatibles''",'« compatibles »',"``compatibles''",'Two small ticks precede and two follow the word; these are double quotation strokes, not angle guillemets.',ch=True,n=5,bbox=[795,950,1240,1035])
diff('Second paragraph, causal word after quoted adjective','vu','car','vu','A low v followed by u is visible before que; there is no three-letter car group.',kind='misread word',ch=True,n=5,bbox=[1310,955,1405,1010])
# Diagram and upper note.
cdiag=ctex[ctex.index('\\diagram{'):ctex.index('% slanted')].strip()
rdiag=tex[tex.index('\\diagram{'):tex.index('% slanted')].strip()
diff('Diamond, complete arrangement and worked upper-right relation',cdiag,r"$F''' \preccurlyeq F' \preccurlyeq F$, \ $F''' \preccurlyeq F'' \preccurlyeq$",rdiag,'The objects are F triple prime at left, F prime above, F double prime below, and one unprimed F at right, nearly level with the upper object. Four bowed signs have no connecting shafts. The upper-right sign has a doubled upper arm, without a secure independent strike: the deleted-older-sign interpretation stays doubtful. The shared right F is visible; H\'s editorial remark about an unwritten last term is not manuscript text.',kind='drawing or diagram',confidence='medium',hc='yes',cc=True,ch=True,n=7,math=True)
diff('Upper slanted note, full text',r'\margin{On sera amené à renforcer encore cette condition sur les contrées modérées !}',r'\marginal{On sera amené à \ill{} \ill{} \ill{} les contrées modérées !}',r'\margin{On sera amené à renforcer encore cette condition sur les contrées modérées !}','The complete rotated note reads On sera amené / à renforcer encore / cette condition / sur les contrées / modérées !. This one row accounts for all three H unreadable placeholders and the extra recoverable sur, without separately counting local omissions.',kind=r'readable ink left as \ill{}',hc='yes',ch=True,n=6)
# Definition and cancelled continuation.
diff('Definition, contrée and its two underlines',r'\uuline{\unsure{contrée|contrie}}','contrée',r'\uuline{\unsure{contrée|contrie}}','Two separate underlines are clear. The reduced penultimate letter has a small high point-like mark; its e/accent versus i/dot identity remains uncertain at this occurrence.',confidence='medium',ch=True,n=8)
diff('Definition, modérée underline count',r'\uuline{modérée}',r'\emph{modérée}',r'\uuline{modérée}','Two distinct long strokes run below modérée.',ch=True,n=8)
diff('Definition, placement of subdivisions','subdivisions',r'\add{subdivisions}','subdivisions','The word begins the next regular line of the paragraph, on the same baseline as the following corrected phrase. No insertion leader or separate raised line marks it as an addition.',kind='insertion or placement',ch=True,n=None,source=half_b,bbox=[275,300,700,375])
diff('Definition, overwritten d-un(e) group and repetition sign',r"\deleted{\unsure{d'un}} \unsure{d'une =|d'un =} $F$",r"\struck{\ill{}} de $F$",r"\unsure{\deleted{d'}d'une|d'une|d'un} = $F$",'There is one word-sized group, with worked d/apostrophe strokes at its start and a low joined un(e) continuation. Only a possible older prefix d\' can be separated; a complete separate old d\'un is not established. A distinct two-stroke repetition sign stands before F.',kind='deletion state (struck given live or live given struck)',confidence='low',hc='yes',cc=True,ch=True,n=9)
diff('Definition, terminal comparables','comparables',r'\uncertain{comparables}','comparables','The c-o-m-p-a-r-a-b-l-e-s sequence is clear and unworked at this lower occurrence, unlike the earlier overwritten adjective.',hc='yes',ch=True,n=None,source=half_b,bbox=[270,375,720,465])
diff('Cancelled Dans clause',r'\deleted{Dans le cas qui vient,}',r'\struck{Dans le cas général,}',r'\deleted{Dans le cas qui vient,}','After cas, the descending q and dotted i form qui; a separate following group has the strokes of vient and a comma. The single strike runs through the full clause.',kind='misread word',ch=True,n=9,bbox=[785,1440,1600,1555])
diff('Cancelled on a before Je, H first unreadable deletion',r'\deleted{on a}',r'\struck{\ill{}}',r'\deleted{on a}','The small group above the cancelled C5 has an initial rounded o, reduced n and a separate a under the cancellation. This is the first H unreadable deletion before Je, not an extra lost word.',kind=r'readable ink left as \ill{}',hc='yes',ch=True,n=10,bbox=[265,1590,435,1660])
pointtex=tex[tex.index('\\figure{'):tex.index('\n\n% The cancelled')].strip()
diff('Two detached points after cancelled on a','.','',pointtex,'Two distinct points are visible, the second slightly lower and to the right. They are reproduced as two TikZ points beside the cancelled words, without assigning them a colon or sentence-stop function.',kind='drawing or diagram',cc=True,ch=True,n=10,bbox=[455,1598,505,1640])
diff('Cancelled C5, H second unreadable deletion before aucune',r'\deleted{\uline{C5}}',r'\struck{\ill{}}',r'\margin{\deleted{\uline{C5}}}','An underlined C5 stands at the left below the Je...donner line and above aucune; diagonal cancellation strokes cross it. H\'s second unreadable deletion corresponds to this label. There is no need to invent an extra deleted word after donner. The label is retained at the margin of the properties paragraph.',kind='insertion or placement',hc='yes',cc=True,ch=True,n=10,bbox=[270,1655,455,1765])
# Properties paragraph.
diff('Properties paragraph, seul','seul','seule','seul','The final l rises and returns directly to the stop. No further e is visible.',kind='misread word',ch=True,n=None,source=half_b,bbox=[485,670,685,760])
diff('Properties paragraph, ses/les before relations','ses','les',r'\unsure{ses|les}','The compact first stroke is worked and looped, followed by reduced es. Its small size favours s, but a shortened l cannot be excluded. Both witnesses are too definite locally.',kind='misread word',confidence='low',cc=True,ch=True,n=11,bbox=[880,1845,965,1920])
diff('Properties paragraph, placement of avec','avec',r'\add{avec}','avec','Avec stands on the same baseline and at the same text size between relations and the straight order sign; no raising or insertion leader is visible.',kind='insertion or placement',ch=True,n=11,bbox=[1290,1820,1440,1915])
# Lower note and C5.
diff('Lower slanted note, entire note',r'\margin{\unsure{Reporter|Rejeter} après C6, $C7_0$ \unsure{ces|mes} axiomes de \uline{disjonction}}',r'\marginal{\ill{} après C6, C7, \ill{} des disjonctions}',r'\margin{\unsure{Reporter|reporter} après C6, $C7_0$ ces axiomes de \uline{disjonction}}','The first word has a long p descender and the later tall t: Reporter/reporter, with capitalization left open, rather than Rejeter. C6 has a comma; C7 has a small oval at its foot, not a following comma. The small group ces is separate from axiomes. The last phrase is de disjonction, singular, with its underline. This whole-note row accounts for both H unreadable placeholders and its C7/punctuation/number/underline differences without double counting them.',kind='misread word',confidence='medium',hc='yes',cc=True,ch=True,n=12)
bars=tex[tex.index('% R3-C5-BARS:'):].strip()
diff('C5, double vertical margin rules','',r'\note{double trait vertical en marge de C5}',bars,'Two long separate rules stand to the left of the lower three axiom lines. They bend slightly at their feet. H describes these editorially but does not transcribe the drawing; C omits it. The final figure reproduces both rules with the adjoining axiom text once.',kind='drawing or diagram',hc='yes',cc=True,ch=True,n=12,bbox=[244,2085,305,2320])
diff('C5, abbreviation before figure',r'\unsure{tte}','toute','tte','Two tall t strokes share the compact crossed cluster, followed by a small e. The full ou sequence of toute is not written.',kind='abbreviation expanded or spelling modernised',cc=True,ch=True,n=13,bbox=[1400,1980,1535,2090])
diff('NB, possible older F under G',r'\deleted{\unsure{F}}','',r'\deleted{\unsure{F}}','Straight upright and bar-like strokes remain within the rewritten letter. They can be read as an older F, but the overwritten layer remains uncertain. H omits this visible correction state.',kind='omission',confidence='medium',ch=True,n=14,bbox=[725,2275,790,2343])
diff('NB, live rewritten G',r'\unsure{G|F}','G','G','The live outer curve returns inward with a short inner stroke, establishing G; the straight old strokes do not make the final letter F.',kind='misread symbol or index',cc=True,n=14,bbox=[725,2275,790,2343],math=True)
diff('NB, crossed letter after equals',r'\unsure{X|x}','X',r'\unsure{X|x}','The crossed strokes are clear, but their size and curved left component do not settle uppercase X against lowercase x. No subscript is present.',confidence='medium',ch=True,n=14,bbox=[785,2280,830,2344])
diff('NB, alphabet of M','M',r'\mathcal{M}','M','The letter has plain pointed stems and no independent calligraphic return. The alphabet is plain M.',kind='misread symbol or index',ch=True,n=14,bbox=[827,2275,890,2344])

# Dispositions of every C unsure occurrence, plus explicit local C_context notation checks.
CD=[]
def doubt(loc,c,r,status,shows,n=None,bbox=None,source=None,rows=None):
    cp=crops[n-1] if n else None
    CD.append(dict(id=f'R3-C{len(CD)+1:02d}',location=loc,c=c,reading=r,status=status,scan_shows=shows,crop=cp['path'] if cp else None,bbox=bbox or (cp['bbox'] if cp else None),bbox_image=source or (cp['source'] if cp else None),context_rows=rows or []))
doubt('First order sign',r'\unsure{\preceq|\leqslant}',r'\preceq','resolved','An upper angle and bowed lower arm distinguish it from the later straight sign.',1,rows=[1,5])
doubt('Très in opening',r'\unsure{très|trs}',r'\unsure{très|trs}','retained','Reduced middle lettering and a high short mark do not establish a separate e.',1,rows=[6])
doubt('Aura in opening',r'\unsure{aura}','aura','resolved','The separated au and ra groups have four recoverable letters.',1,rows=[7])
doubt('Cancelled elements noun',r'\unsure{éléments|élémen}',r'\unsure{éléments|élémen}','retained','The final letters remain covered by the long strike.',2,rows=[8])
doubt('Word after figures',r'\unsure{en général|en position}','toujours','revised','The initial slant forms t, followed by reduced ou and a descending j with low ours; no final l is present.',3,rows=[9])
doubt('Explanation group',r'\unsure{(i.e.|liée.|lire.}','(i.e.','resolved','Open parenthesis, dotted i and e with separate stops are distinguishable.',3,rows=[9])
doubt('First repetition sign',r'\unsure{=|même}','=','resolved','Two bars, not a lettered word.',3,bbox=[440,620,535,675],rows=[3,10])
doubt('Second subdivision label',r"\unsure{F'''|F''}",r"F'''",'resolved','Three distinct raised ticks follow the second F.',5,bbox=[1500,745,1585,835],rows=[11])
doubt('Overwritten adjective, older middle',r'\deleted{\unsure{ati|atib}}',r'\deleted{\unsure{ati|atib}}','retained','Tall and dotted old strokes can be segmented ati or atib, without a separate older whole word.',4,rows=[12,24])
doubt('Overwritten adjective, live middle',r'\unsure{ara|ati|ata}',r'\unsure{ara|ati|ata}','retained','New loops do not settle r against the surviving t/i traces.',4,rows=[12,24])
doubt('Cancelled phrase, opening groups',r'\unsure{on dit|c.à.d.}',r'\unsure{quand et|on dit}','revised','Joined low strokes and two tall strokes favour quand et; on dit remains possible. The dot sequence needed for c.à.d. is not visible.',5,rows=[13])
doubt('Cancelled phrase, final group',r'\unsure{sub}',r'\unsure{seul|sub}','revised','The final tall stem and low joined middle admit seul or sub, not a securely complete seulement.',5,rows=[13])
doubt('Upper-right diamond relation, old sign and state',r'\deleted{\unsure{\leq|\prec}}\preceq',r'\unsure{\preceq|\deleted{\leq}\preceq|\deleted{\prec}\preceq}','revised','An extra upper arm is visible; no separate strike securely establishes the extra arm as a deleted older complete sign.',7,rows=[21])
doubt('Definition contrée',r'\unsure{contrée|contrie}',r'\unsure{contrée|contrie}','retained','The reduced penultimate letter and high mark remain e/accent versus i/dot. This uncertainty is confined to the definition occurrence.',8,rows=[14])
doubt('Definition, alleged full older d\'un',r"\deleted{\unsure{d'un}}",r"\unsure{\deleted{d'}d'une|d'une|d'un}",'revised','Only worked initial d/apostrophe strokes separate from the final low continuation; no second complete old word is established.',9,rows=[15])
doubt('Definition, final d-un(e) and following sign',r"\unsure{d'une =|d'un =}",r"\unsure{\deleted{d'}d'une|d'une|d'un} =",'revised','The final low un(e) is reduced; the equal-like repetition mark itself has two clear bars.',9,rows=[16])
doubt('Lower note, first word',r'\unsure{Reporter|Rejeter}',r'\unsure{Reporter|reporter}','revised','The long p descender and later t favour reporter; only its initial capitalization remains open.',12,rows=[17])
doubt('Lower note, ces',r'\unsure{ces|mes}','ces','resolved','The first small curve is c, followed by e and the short terminal s, not initial m humps.',12,rows=[18])
doubt('C5 abbreviation',r'\unsure{tte}','tte','resolved','Two tall t strokes and a final e; no ou.',13,rows=[19])
doubt('NB older letter',r'\deleted{\unsure{F}}',r'\deleted{\unsure{F}}','retained','Old straight stem/bar strokes are compatible with F but crowded by the live G.',14)
doubt('NB live letter',r'\unsure{G|F}','G','resolved','The outer curve and inner return establish live G.',14,rows=[20])
doubt('NB crossed letter',r'\unsure{X|x}',r'\unsure{X|x}','retained','Crossed strokes and no index are clear; capital/lowercase form remains unresolved.',14,rows=[22])
doubt('Context: diamond objects and unconnected signs',r"F''',F',F'',F",r"F''',F',F'',F",'resolved','The left, upper, lower and right labels have respectively three, one, two and zero primes. All four relations are signs without connecting shafts. Right F is almost level with upper F\'.',7,rows=[1,2])
doubt('Context: C5 bowed sign',r"F'\preceq F",r"F'\preceq F",'resolved','The same locally visible bowed lower arm is present between F prime and F.',13,rows=[1])
doubt('Context: property relation and final straight sign',r'\preceq; \leq',r'\preceq; \leq','resolved','The relation after particulière has the bowed lower stroke on half b. The relation after avec has straight arms, confirmed by crop 11. Crop 11 does not frame the earlier relation; that earlier occurrence is decided only from the half.',None,bbox=[1495,540,1610,835],source=half_b,rows=[1,5])
doubt('Context: C5 G, F prime, X without subscript and ssi',r"G,F',X,\mathrm{ssi}",r"G,F',\unsure{X|x},\mathrm{ssi}",'revised','Both body G letters are plain and clear; the body F prime has one tick; ssi remains the three-letter abbreviation. The NB X/x distinction remains local and uncertain, with no subscript.',14,rows=[4])
doubt('Context: upper-note contrées',r'contrées','contrées','resolved','After rotation the upper marginal word is legible with its plural ending. The uncertainty in the separate doubly underlined definition is not propagated to it.',6,rows=[14])
doubt('Context: singular-looking subdivision',r'deux subdivision','deux subdivision','resolved','The final n is an extended single sweep with no distinct following s.',5,rows=[23])
doubt('Context: quoted adjective versus earlier overwritten word',r'``compatibles\'\'',r'``compatibles\'\'','resolved','The quoted word compatibles is clear and independent of the still-unresolved earlier overwritten underlined adjective. The lower comparables is also clear.',5,rows=[24])
doubt('Context/audit: lower C7 foot',r'C7_0',r'C7_0','resolved','A small oval sits below the seven at its foot; this decision uses only this page\'s rotated crop, not the prior audit\'s mention of a later sheet.',12)

I=[]
def inv(element,kind,pos,words):
    I.append(dict(element=element,kind=kind,position=pos,first_words_or_objects=words,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('I01','text','top centre','69')
inv('I02','text','upper body, first paragraph',"J'en viens à la rel d'ordre")
inv('I03','deletion','upper paragraph after deux','éléments / élémen')
inv('I04','insertion','raised above figures',r"F', F'', \preceq, short dash")
inv('I05','deletion','possible cancellation within raised formula',r'\unsure{\preceq|\deleted{\preceq}}')
inv('I06','text','second paragraph','On dit que deux subdivision')
inv('I07','deletion','worked middle of underlined adjective','ati / atib beneath ara / ati / ata')
inv('I08','deletion','after underlined adjective','quand et / on dit que seul / sub')
inv('I09','diagram','middle left',r"F''', F', F'', F and four bowed relations")
inv('I10','deletion','possible older relation within diagram upper-right sign',r'possible \leq or \prec under \preceq; state uncertain')
inv('I11','margin note','slanted left note beside diamond','On sera amené à renforcer encore')
inv('I12','text','definition to right of diamond continuing below','On dit que la contrée est modérée')
inv('I13','deletion','worked beginning of d-un(e) after subdivisions',"possible older d' prefix only")
inv('I14','deletion','after comparables','Dans le cas qui vient,')
inv('I15','deletion','left at next line before Je','on a')
inv('I16','drawing','immediately after cancelled on a','two points, second down and right')
inv('I17','deletion','left below opening Je...donner line','underlined C5 crossed diagonally')
inv('I18','text','properties paragraph','Je ne saurais donner aucune propriété particulière')
inv('I19','deletion','properties paragraph before seul','tout')
inv('I20','margin note','slanted lower left beside live C5','Reporter/reporter après C6, C7_0 ces axiomes de disjonction')
inv('I21','text','bottom axiom block','underlined C5; Soit F prime precedes F')
inv('I22','drawing','left of lower three lines of C5','two long vertical rules')
inv('I23','text','bracketed NB within bottom axiom','NB Il suffit de le poser pour')
inv('I24','deletion','within rewritten NB letter','possible older F below live G')

RD=[
('Opening, très',r'\unsure{très|trs}',['très','trs'],'medium','The middle lettering is reduced and the raised mark does not securely establish e plus accent.'),
('Opening, cancelled noun',r'\unsure{éléments|élémen}',['éléments','élémen'],'low','The strike covers the terminal letters.'),
('Raised formula relation state',r'\unsure{\preceq|\deleted{\preceq}}',[r'\preceq',r'\deleted{\preceq}'],'low','Heavy retracing may include a cancellation, but there is no independently secure strike.'),
('Underlined adjective, older middle',r'\deleted{\unsure{ati|atib}}',['ati','atib'],'low','The old tall/dotted strokes are interwoven with new ink.'),
('Underlined adjective, final middle',r'\unsure{ara|ati|ata}',['ara','ati','ata'],'low','The rewritten central strokes do not yield a unique final spelling.'),
('Cancelled phrase, first groups',r'\unsure{quand et|on dit}',['quand et','on dit'],'low','The same joined low traces and tall strokes can be segmented in either way.'),
('Cancelled phrase, final group',r'\unsure{seul|sub}',['seul','sub'],'low','The last tall stem can be l or b and the low middle is covered.'),
('Upper-right diagram relation',r'\unsure{\preceq|\deleted{\leq}\preceq|\deleted{\prec}\preceq}',[r'\preceq',r'\deleted{\leq}\preceq',r'\deleted{\prec}\preceq'],'low','The extra upper arm may be a retrace or an older overwritten sign; cancellation is not established.'),
('Definition, penultimate letter of contrée',r'\unsure{contrée|contrie}',['contrée','contrie'],'medium','Small high mark and short lower stroke leave e/accent versus i/dot unresolved.'),
('Definition, single worked d-un(e) group',r"\unsure{\deleted{d'}d'une|d'une|d'un}",[r"\deleted{d'}d'une","d'une","d'un"],'low','Only a possible old prefix separates; the final un(e) continuation is reduced.'),
('Properties paragraph before relations',r'\unsure{ses|les}',['ses','les'],'low','The worked initial is a small loop: s is first choice, shortened l remains possible.'),
('Lower margin initial capitalization',r'\unsure{Reporter|reporter}',['Reporter','reporter'],'medium','The word reporter is recovered, but the first tall r/R form does not decide case.'),
('NB older overwritten letter',r'\deleted{\unsure{F}}',['F'],'medium','Straight older strokes suggest F but lie within the live G.'),
('NB crossed letter',r'\unsure{X|x}',['X','x'],'medium','Height and curved strokes do not settle case; there is no index.')]
remaining=[dict(location=a,reading=b,alternatives=c,confidence=d,reason=e) for a,b,c,d,e in RD]
notation=[
 dict(sign='bowed order',latex=r'\preceq',appearance='Upper left-facing angle, lower stroke bowed down toward the right; locally clear except worked variants.',location='opening; diamond; properties paragraph; C5',alternatives=[r'\leqslant at opening rejected',r'worked relation state retained at two local occurrences']),
 dict(sign='straight order',latex=r'\leq',appearance='Straight upper angle and straight lower bar.',location='after avec in properties paragraph',alternatives=[]),
 dict(sign='figure letters and primes',latex=r"F,F',F'',F'''",appearance='Plain F with upper and middle bars; primes are separate upright ticks.',location='raised formula; second paragraph; diamond; C5',alternatives=[]),
 dict(sign='repetition mark',latex='=',appearance='Two short near-horizontal strokes, sometimes joined by a small left return.',location='une = figure F; d-un(e) = F',alternatives=[]),
 dict(sign='NB rewritten letter',latex=r'\deleted{\unsure{F}}G',appearance='Live outer curve and inner return surround older straight strokes.',location='NB before equals',alternatives=['older F uncertain; live G resolved']),
 dict(sign='crossed variable',latex=r'\unsure{X|x}',appearance='Two crossed strokes with a curved left component; no subscript.',location='NB after equals',alternatives=['X','x']),
 dict(sign='ambient letter',latex='M',appearance='Plain pointed capital, no separate script flourish.',location='NB membership',alternatives=[]),
 dict(sign='number at foot of C7',latex=r'C7_0',appearance='Small hollow oval low at the foot of the seven.',location='lower slanted note',alternatives=[]),
 dict(sign='double vertical rule',latex='R3-C5-BARS TikZ figure',appearance='Two long parallel strokes, slightly bent at their lower ends.',location='left of C5 lower lines',alternatives=[]),
 dict(sign='detached two points',latex='R3-ON-A-POINTS TikZ figure',appearance='Second point lies slightly lower and farther right than first.',location='after cancelled on a',alternatives=['no punctuation function assigned'])]
notes=dict(summary='Handwritten page 69 introduces the subdivision order, discusses common subdivisions and the word for comparability, defines a moderated contrée, and states C5 on disjointness. Two slanted notes concern strengthening the condition and moving disjunction axioms. The page contains worked corrections, a four-object diagram, and no date or title.',math_reading_decisions='No theorem was proved or independently re-proved. Mathematical structure only prompted checking the prime counts, bowed versus straight order signs, the shared right-hand F in the diagram, and the corrected G in the NB. Those decisions follow visible strokes; the unusual F triple prime in the prose and the unmatched (i.e. are preserved. The transcribed claim about Sup/inf was not validated.',author_checks='The cancelled on a and cancelled underlined C5 explain the two H unreadable deletions around Je...donner; no additional deleted word was invented. The single worked d-un(e) group is not expanded into two complete words. Both slanted notes were framed in full before rotation. The upper-right relation has an extra arm whose deletion state remains open. H editorial remarks were treated as editorial remarks, not manuscript wording.',title_dates_pagination='Visible manuscript number 69, retained with scanpage 70. No title, date, cote marker or archive sheet number is supplied by this page. One C5 label is cancelled and another is live and underlined.')
# Correct intended crop reason to distinguish what is actually framed.
crops[10]['reason']='tout deletion, seul, ses-relations lettering and avec placement, final straight order sign; earlier relation after particulière is outside this crop and was read on half b'
report=dict(reader='R3',cote='156-4',scan='070',brief_version='v06',started_utc=(R/'started.txt').read_text().strip(),finished_utc=datetime.now(timezone.utc).isoformat(),image_views=images,reading_file=str(R/'reading.tex'),differences=D,c_doubts=CD,inventory=I,remaining_doubts=remaining,notation=notation,abbreviations=[dict(form='rel',expansion='relation'),dict(form='i.e.',expansion='id est'),dict(form='Sup',expansion='supremum'),dict(form='inf',expansion='infimum'),dict(form='tte',expansion='toute'),dict(form='ssi',expansion='si et seulement si'),dict(form='NB',expansion='nota bene'),dict(form='sub (possible cancelled reading)',expansion='possibly subdivision; the expansion is not asserted in the transcript')],notes=notes,check_events=[],crops=crops,workflow_feedback=['The brief does not explicitly say whether H editorial observations about graphics count as marked_in_h. Here yes is used for H unreadable/uncertain loci and explicit editorial flags, while the editorial wording itself is not counted as manuscript text.','The upper-right diagram relation is one worked glyph: a diplomatic macro cannot exactly separate retracing from a deleted older sign. The full alternatives are retained at the one locus and the crop is the adjudication source.'])
# Raw single-quoted Python literals above need apostrophe delimiters unescaped in LaTeX.
def clean_quotes(obj):
    if isinstance(obj,str):
        return obj.replace("\\'", "'")
    if isinstance(obj,list):
        return [clean_quotes(x) for x in obj]
    if isinstance(obj,dict):
        return {k:clean_quotes(v) for k,v in obj.items()}
    return obj
report=clean_quotes(report)
# H places its diagram inside the same marginal macro. Quote only the note's
# exact words here, so this note row and the diagram row have disjoint scopes.
note_row=next(x for x in report['differences'] if x['location']=='Upper slanted note, full text')
note_row['c']='On sera amené à renforcer encore cette condition sur les contrées modérées !'
note_row['h']=r'On sera amené à \ill{} \ill{} \ill{} les contrées modérées !'
note_row['reading']='On sera amené à renforcer encore cette condition sur les contrées modérées !'
(R/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
# Record actual observed views, in their actual order. The timestamp is when the batched log was written, not a fabricated exact display time.
evidence=[
'Opening rel lacks a point; bowed relation; comma after subdivision; très/trs retained; aura resolved.',
'Cancelled éléments/élémen retained; capital S in following Subdivisions.',
'F prime and double prime, raised worked relation and dash; toujours; open (i.e.; first =; comma without closing parenthesis.',
'One overwritten adjective with comp and bles; middle old/final alternatives retained.',
'Singular subdivision; three primes on second F; cancelled first groups and final seul/sub remain uncertain; quoted double ticks; vu.',
'Whole upper note read after clockwise rotation; no clipped continuation of target note.',
'Four objects and four unconnected bowed signs; extra upper-right arm; shared right F near level with top F.',
'Double underlines; contrée/contrie remains local doubt; modérée read.',
'One worked d-un(e) group, =, complete cancelled Dans le cas qui vient comma.',
'Cancelled on a and two detached points; cancelled underlined C5 below opening line; both H placeholders accounted for by these two groups.',
'Cancelled tout, seul, ses/les unresolved, baseline avec, final straight order sign. Earlier relation after particulière is not framed here and was read on half b.',
'Complete lower slanted note after clockwise rotation; reporter word, capitalization open; ces; C7 foot oval; singular underlined disjonction; both bars fully present.',
'C5 bowed relation and tte; F and ssi.',
'NB live G, possible old F, unresolved X/x, plain M and complete closing bracket at page foot.']
log_prefix=(R/'inspection_log.txt').read_text().split('\nCrop views below',1)[0]
with (R/'inspection_log.txt').open('w') as f:
 f.write(log_prefix)
 f.write('\nCrop views below were all actually displayed successfully, once each, in five tool batches (01–03, 04–06, 07–09, 10–12, 13–14). Log recorded '+datetime.now(timezone.utc).isoformat()+'.\n')
 for k,(cp,ev) in enumerate(zip(crops,evidence),start=4):
  f.write(f'VIEW {k}: {cp["path"]}\n  Source: {cp["source"]}; original bbox: {cp["bbox"]}; scale after rotation: {cp["scale"]}; rotation degrees: {cp["rotation"]}.\n  Transformations: '+ '; '.join(cp['transforms'])+'\n  Evidence: '+ev+'\n')
 f.write('No OCR, external research, LaTeX compilation, other readers, or other pages used. No recrop or repeated crop display. Fourteen own crops; three supplied image views.\n')
print(json.dumps({'differences':len(D),'c_doubt_dispositions':len(CD),'remaining_doubts':len(remaining),'inventory':len(I),'crops':len(crops)},ensure_ascii=False))
