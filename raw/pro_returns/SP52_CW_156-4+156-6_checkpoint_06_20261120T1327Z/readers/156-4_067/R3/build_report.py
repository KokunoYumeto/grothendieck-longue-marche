from pathlib import Path
import json
from datetime import datetime, timezone

OUT=Path(__file__).parent
ROOT=Path('/workspace/scratch/6644f30583f9')
meta=json.loads((ROOT/'page_packets/156-4_067/metadata.json').read_text())
whole,a,b=meta['images']
crops=json.loads((OUT/'crop_manifest.json').read_text())
diffs=[]

def diff(location,c,h,reading,evidence,n=None,confidence='high',kind='other',marked='no',cc=False,ch=True,math=False,bbox=None,source=None):
    cr=crops[n-1] if n else None
    diffs.append(dict(id=f'D{len(diffs)+1:03d}',location=location,c=c,h=h,reading=reading,
      scan_shows=evidence,confidence=confidence,kind=kind,marked_in_h=marked,
      change_c=cc,change_h=ch,crop=cr['path'] if cr else None,
      bbox=bbox or (cr['bbox'] if cr else None),bbox_image=source or whole,
      math_consequential=math))

# Every repeated alphabet difference is grouped by its explicitly named block.
diff('Top first definition: family initial, operator subscript, family after membership, and raised inclusion',r"\mathcal F',\mathcal F,\mathcal F,\mathcal F",r"\mathfrak{F}',\mathfrak{F},\mathfrak{F},\mathfrak{F}",r"\mathcal F',\mathcal F,\mathcal F,\mathcal F",'Hooked or curved family capitals differ from the straight member F; no Gothic alphabet is indicated.',1,kind='misread symbol or index')
diff('Top first operator',r'\unsure{\operatorname{cosup}|\operatorname{cosupp}}',r'\operatorname{cosupp}',r'\operatorname{cosup}','One terminal descending p stroke, without a second p stem.',1,kind='abbreviation expanded or spelling modernised',cc=True)
diff('First disjoint clause',r'\unsure{des|de}','des',r'\unsure{des|de}','The terminal reduced horizontal has a thick return; it does not settle an s.',2,'low','misread word')
diff('First relation after H_i',r'H_i\unsure{\vdash|\in}\Phi',r'H_i\in\Phi',r'H_i\vdash\Phi','A straight upright carries one short rightward tick, unlike a rounded membership sign.',2,kind='misread symbol or index',cc=True,math=True)
diff('Raised inclusion in first definition',r'\Phi\inserted{\subset\mathcal F}\,\}',r'\Phi\rbrace\quad(\subset\mathfrak{F})',r'\Phi\,\}\quad\inserted{\subset\mathcal F}','The inclusion stands above the line and its short descending leader reaches the Phi before the closing brace; there are no ordinary parenthesis glyphs around the insertion.',2,kind='insertion or placement')
diff('Enclosure and leader around raised top inclusion','','',r'\figure{\begin{tikzpicture}\draw ...;\end{tikzpicture}}','A long rounded arm under the raised inclusion extends right and down beside the closing brace, with a second short descending leader. These are reproduced in the top TikZ group.',2,kind='drawing or diagram',cc=True)
diff('Top second definition: M prime, operator subscript and ambient M',r"M',M,M",r"\mathcal{M}',\mathcal{M},\mathcal{M}",r"M',M,M",'Each M has two plain peaks, with no separate ornamental alphabet.',1,kind='misread symbol or index')
diff('Top second operator',r'\operatorname{cosup}_{M}',r'\operatorname{cosupp}_{\mathcal{M}}',r'\operatorname{cosup}_{M}','A single long terminal p descender.',1,kind='abbreviation expanded or spelling modernised')
diff('Second disjoint clause',r'\unsure{de|des}','des',r'\unsure{de|des}','Short reduced ending after the d loop; no definite separate s.',2,'low','misread word')
diff('Phi at end of second set',r'\unsure{\Phi|\varphi}',r'\Phi',r'\unsure{\varphi|\Phi}','Small oval atop a descending stem with a curved rightward foot, without the clear straight base of the nearby capitals.',2,'low','misread symbol or index',cc=True,math=True)
diff('Closing strokes of second set',r'\unsure{)|\}}\,\}',r'\rbrace',r'\unsure{\rbrace|)\rbrace}','The upper stroke is rounded and meets the lower brace-like hook. A single irregular brace is possible; an extra round close before a brace cannot be excluded.',2,'low','misread symbol or index',cc=True)
diff('Third top equality: insertion state',r'\inserted{=M\cap\operatorname{cosup}_{\mathcal F}(\Phi)\subset M}',r'=\mathcal{M}\cap\operatorname{cosupp}_{\mathfrak{F}}(\Phi)\subset\mathcal{M}',r'\inserted{=M\cap\operatorname{cosup}_{\mathcal F}(\Phi)\subset M}','The additional equality is below the two main definitions and connected by the long spanning arm.',3,kind='insertion or placement')
diff('Third top equality: both M and the family operator subscript',r'M,\mathcal F,M',r'\mathcal{M},\mathfrak{F},\mathcal{M}',r'M,\mathcal F,M','Plain peaked M forms and the hooked family F.',3,kind='misread symbol or index')
diff('Third top operator',r'\operatorname{cosup}_{\mathcal F}',r'\operatorname{cosupp}_{\mathfrak{F}}',r'\operatorname{cosup}_{\mathcal F}','One terminal p downstroke.',3,kind='abbreviation expanded or spelling modernised')
diff('Long connector over third top equality','','',r'\figure{\begin{tikzpicture}\draw ...;\end{tikzpicture}}','A line curls at the far right of the preceding line, runs above the added equality and curves down to its left.',3,kind='drawing or diagram',cc=True)
diff('Cancelled prose after first Donc',r'\deleted{\unsure{on aura|on a}}',r'\struck{\ill{}}',r'\deleted{\unsure{on aura|on a}}','Two word-sized groups remain, but the middle strokes are hidden by two cancellation lines.',4,'low','readable ink left as \\ill{}','yes')
diff('Cancelled prose after F membership',r'pour $F\in\mathcal F$ posant',r'pour $F\in\mathfrak{F}$, posant',r'pour $F\in\mathcal F$ posant','No separate comma is visible between the membership expression and posant.',4,kind='text not on the page')
diff('First cancelled operator',r'\operatorname{cosup}_{\mathcal F}',r'\operatorname{cosupp}_{\mathfrak{F}}',r'\operatorname{cosup}_{\mathcal F}','The word at the far right of the first cancelled line has one p descender.',4,kind='abbreviation expanded or spelling modernised')
diff('Cancelled repeated family definition and its separate placement',r"\deleted{\mathcal F'=\operatorname{cosup}_{\mathcal F},}\quad\deleted{\mathcal F'=\operatorname{cosupp}_{\mathcal F}(\Phi),}",r"\struck{\mathfrak{F}'=\operatorname{cosupp}_{\mathfrak{F}}(\Phi)}",r"\deleted{\mathcal F'=\operatorname{cosup}_{\mathcal F},}\quad\deleted{\mathcal F'=\operatorname{cosupp}_{\mathcal F}(\Phi),}",'There is a family-prime definition at the end of the prose line and a repeated family-prime definition on the line below. Only the second has the visible Phi argument.',4,kind='omission')
diff('Isolated cancelled phi at left of cancelled formula row',r'\deleted{\unsure{\phi|\Phi}}',r'\struck{\Phi}',r'\deleted{\unsure{\phi|\Phi}}','Small oval, a slight rise above it and a long descender without a clear base; cancellation crosses the loop.',4,'low','misread symbol or index')
diff('Lower left cancelled operator',r'\operatorname{cosup}',r'\operatorname{cosupp}',r'\operatorname{cosup}','One p descender is visible before the residual subscript stroke.',4,kind='abbreviation expanded or spelling modernised')
diff('Residual subscript in cancelled F membership',r'_{\unsure{,|\mathcal F}}','',r'_{\unsure{,|\mathcal F}}','A short curved remnant survives below the strike after the p; too little remains to distinguish a comma-like stroke from family F.',4,'low','omission')
diff('Cancelled lower right operator and overwritten subscript',r'\operatorname{cosup}_{\deleted{\unsure{\mathcal F}}M}',r'\operatorname{cosupp}_{\mathcal{M}}',r'\operatorname{cosup}_{\deleted{\unsure{\mathcal F}}M}','The operator has one p. A hooked lower remnant lies under the M subscript; the earlier family reading remains uncertain.',4,'low','omission')
diff('All family-capital occurrences in the cancelled prose and formula block',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','The family capitals in F membership, both repeated family-prime definitions, their subscripts, the intersection and final argument have curved tops or hooked feet. The residual and overwritten subscript doubts are separately recorded.',4,kind='misread symbol or index')
diff('All M occurrences in cancelled block: M prime, intersection M, final operator subscript',r"M',M,M",r"\mathcal{M}',\mathcal{M},\mathcal{M}",r"M',M,M",'Plain peaked M shapes; the prime is raised.',4,kind='misread symbol or index')
diff('Position of isolated cancelled phi and F membership',r'\deleted{\unsure{\phi|\Phi}}\qquad\deleted{F\in\operatorname{cosup}_{\unsure{,|\mathcal F}}}',r'\struck{\Phi}\ \struck{F\in\operatorname{cosupp}}',r'\deleted{\unsure{\phi|\Phi}}\qquad\deleted{F\in\operatorname{cosup}_{\unsure{,|\mathcal F}}}','The phi is at far left of the upper cancelled formula row, and F membership is below-left. H places both after its combined long cancelled statement.',4,kind='insertion or placement')
diff('Live Donc pour: family alphabet',r'F\in\mathcal F',r'F\in\mathfrak{F}',r'F\in\mathcal F','The member F is straight; the family letter has the curved family shape.',bbox=[290,600,975,698],source=a,kind='misread symbol or index')
diff('Left note initial capital','Ainsi,','ainsi,','Ainsi,','A large crossed initial A, followed by the reduced remainder and a separate comma.',5,kind='abbreviation expanded or spelling modernised')
diff('Left note M and family alphabets',r"M'\text{ et }\mathcal F'",r"\mathcal{M}'\text{ et }\mathfrak{F}'",r"M'\text{ et }\mathcal F'",'Plain M and a hooked family F, each with a separate prime.',5,kind='misread symbol or index')
diff('Left note accent in déterminent','déterminent','déterminent',r'\unsure{déterminent|determinent}','The reduced letter sequence can be followed; a short rising stroke near the first e may be its accent or part of the adjoining letter.',5,'low','misread word',cc=True)
diff('Left note last word',r'\unsure{mutuellement}','mutuellement',r'\unsure{mutuellement}','The long word has the expected tall middle stem and later loop, but several linking letters remain flattened.',5,'medium','misread word')
diff('Left note terminal arrow/hook','','',r'\unsure{\longrightarrow}','A horizontal extension ends in an angled head towards the brace. It may instead include the terminal t hook; the TikZ group marks the arrow uncertain. H describes an arrow in an editorial note but does not draw it.',5,'low','drawing or diagram',cc=True)
diff('Braced display: both family-prime occurrences',r"\mathcal F',\mathcal F'",r"\mathfrak{F}',\mathfrak{F}'",r"\mathcal F',\mathcal F'",'Curved top on the first family F and a looped top on the second; the member F and barred F are plain.',6,kind='misread symbol or index')
diff('Braced display: both M primes and intersection M',r"M',M',M",r"\mathcal{M}',\mathcal{M}',\mathcal{M}",r"M',M',M",'Plain peaked M at all three positions.',6,kind='misread symbol or index')
diff('Low point in second braced line',r"M'=\unsure{.|\cdot}\mathcal F'\cap M",r"\mathcal{M}'=\mathfrak{F}'\cap\mathcal{M}",r"M'=.\mathcal F'\cap M",'A small separate dot sits below the lower equals stroke and close to the baseline, not at the height of a multiplication dot.',6,kind='omission',cc=True,math=True)
diff('Right note: family-prime in NB, family in pair, and separate family-prime above Stable',r"\mathcal F',\mathcal F,\mathcal F'",r"\mathfrak{F}',\mathfrak{F},\mathfrak{F}'",r"\mathcal F',\mathcal F,\mathcal F'",'Hooked and locally retraced family letters; the separate family-prime belongs above the Stable line.',7,kind='misread symbol or index')
diff('Right note: M prime and final M',r"M',M",r"\mathcal{M}',\mathcal{M}",r"M',M",'Plain M shapes; the final period is separate.',7,kind='misread symbol or index')
diff('H unread item before separate family-prime in right note','',r'\ill{}','','No additional word-sized group stands between the completed NB text and the separate family-prime. The marks are the connecting enclosure.',7,kind='text not on the page',marked='yes')
diff('Right note Stable ending and capitalization',r'\unsure{Stable|Stables}','stables','Stable','A large initial S, followed by table; the final e runs to a downward return without a separately legible s.',7,'medium','misread word',cc=True)
diff('Right note Sup initial','Sup.','sup.','Sup.','Capital S and a separate terminal full stop.',7,kind='abbreviation expanded or spelling modernised')
diff('Parentheses around Stable in H',r'\uline{\unsure{Stable|Stables} par Sup.}',r'(stables par sup.)',r'\uline{Stable par Sup.}','The strokes are an open enclosure and underline, not paired round parentheses enclosing the phrase.',7,kind='text not on the page')
diff('Underline of right note Stable par Sup.',r'\uline{\unsure{Stable|Stables} par Sup.}',r'(stables par sup.)',r'\uline{Stable par Sup.}','Dark underlining is visible below Stable and continues beneath par Sup.; the separate surrounding line is reproduced as a drawing.',7,kind='omission')
diff('Right note enclosure and connecting arms','','',r'\figure{\begin{tikzpicture}\draw ...;\end{tikzpicture}}','An angular lower-and-right arm adjoins the separate family-prime. A longer line approaches from the left, bends below Stable, and runs under the note before falling to the right.',7,kind='drawing or diagram',cc=True)
diff('Double-prime definitions: all family letters (initial, two family subscripts and both arguments)',r"\mathcal F'',\mathcal F,\mathcal F',\mathcal F,\mathcal F'",r"\mathfrak{F}'',\mathfrak{F},\mathfrak{F}',\mathfrak{F},\mathfrak{F}'",r"\mathcal F'',\mathcal F,\mathcal F',\mathcal F,\mathcal F'",'Family capitals have curved top arms or hooked lower strokes. The two primes are discrete raised marks.',8,kind='misread symbol or index')
diff('Double-prime definitions: M double-prime and both M operator subscripts',r"M'',M,M",r"\mathcal{M}'',\mathcal{M},\mathcal{M}",r"M'',M,M",'Plain M shapes, with two separate ticks at the initial M.',8,kind='misread symbol or index')
diff('First definition label over equals',r'\text{def}',r'\text{déf}',r'\text{def}','The small d/e/f group has no detached accent above the e.',8,kind='abbreviation expanded or spelling modernised')
diff('Second definition label over equals',r'\text{def}',r'\text{déf}',r'\text{def}','The second small label likewise lacks an independently visible accent.',8,kind='abbreviation expanded or spelling modernised')
diff('M double-prime defining operator',r'\operatorname{cosup}_{M}',r'\operatorname{cosupp}_{\mathcal{M}}',r'\operatorname{cosup}_{M}','One p descender; the adjacent first definition has two clearly separate p stems.',8,kind='abbreviation expanded or spelling modernised')
diff('Short word after On a',r'\unsure{bien|vu|la|là}','donc',r'\unsure{vu|bien|la|là}','A short initial rise bends into a long flat run. It does not show the d-o-n-c groups; the residual strokes do not settle the shorter candidates.',9,'low','misread word',cc=True)
diff('Two family double-primes in On a paragraph',r"\mathcal F'',\mathcal F''",r"\mathfrak{F}'',\mathfrak{F}''",r"\mathcal F'',\mathcal F''",'Hooked family letters, the first heavily retraced; two raised primes at each occurrence.',10,kind='misread symbol or index')
diff('Sup/Supp in On a paragraph',r'\unsure{Sup|Supp}','Sup.',r'\unsure{Sup|Supp}','The p region is heavily retraced and contains two nearby descending strokes; a second p versus retracing is not decided.',10,'low','misread word',math=True)
diff('Punctuation after Sup/Supp',',','.',',','A separate small descending comma follows the word.',10,kind='misread symbol or index')
diff('Cancelled contient',r'\deleted{contient $\Phi$}',r'\struck{\ill{} $\Phi$}',r'\deleted{contient $\Phi$}','The c opening, t stem, i dot, compressed ending and final t are visible beneath the strike.',11,'medium','readable ink left as \\ill{}','yes')
diff('After passage',r'\unsure{à|:} une','aux',r'\unsure{à|:} une','Two small detached marks precede a separate three-hump word; they can be a reduced à with accent or a colon. The following word is une, not part of aux.',10,'low','misread word')
diff('Number of sous-figure','sous-figure','sous-figures','sous-figure','The word ends in a small e followed by a separate stop, without a final s.',11,kind='misread word')
diff('Cancelled letter before barred Phi in union',r'\deleted{\unsure{M}}','',r'\deleted{\unsure{M}}','A heavily cancelled capital-sized group with two rising strokes remains before the barred Phi; M is plausible but not secure.',12,'low','omission')
diff('Lower first equation: left operator',r'\operatorname{cosup}',r'\operatorname{cosupp}',r'\operatorname{cosup}','One terminal p stroke.',13,kind='abbreviation expanded or spelling modernised')
diff('Lower first equation: right operator',r'\operatorname{cosup}',r'\operatorname{cosupp}',r'\operatorname{cosup}','One terminal p stroke before the family subscript.',13,kind='abbreviation expanded or spelling modernised')
diff('Lower second equation: operator',r'\operatorname{cosup}',r'\operatorname{cosupp}',r'\operatorname{cosup}','One terminal p stroke before the corrected subscript.',13,kind='abbreviation expanded or spelling modernised')
diff('Lower first equation: both family operator subscripts',r'\mathcal F,\mathcal F',r'\mathfrak{F},\mathfrak{F}',r'\mathcal F,\mathcal F','Small hooked family F forms.',13,kind='misread symbol or index')
diff('Lower equations: M with barred-Phi subscript in first equation, second operator M, and both ambient M in set builder',r'M_{\overline\Phi},M,M,M_{\overline\Phi}',r'\mathcal{M}_{\overline{\Phi}},\mathcal{M},\mathcal{M},\mathcal{M}_{\overline{\Phi}}',r'M_{\overline\Phi},M,M,M_{\overline\Phi}','Plain two-peaked M letters; the Phi bars sit inside the M subscripts.',13,kind='misread symbol or index')
diff('Lower second equation: earlier subscript underneath M',r'\deleted{\unsure{\mathcal F}}','',r'\deleted{\unsure{\mathcal F}}','A hooked lower curve and crossed stem survive beneath the final M.',13,'low','omission')
diff('Two points after corrected lower operator subscript','','',r'\unsure{\ldotp\ldotp|:}','Two small detached ink points occur after the corrected M and before the Phi argument. Their diagonal alignment and function remain uncertain; incidental pen points are also possible.',13,'low','omission',cc=True)
diff('Small cancelled group before lower set-builder X',r'\deleted{\unsure{\varnothing|x}}','',r'\deleted{\unsure{\varnothing|x}}','A small crossed loop beside the opening brace precedes the full X.',13,'low','omission')
diff('Sign after disjoint de in lower set builder',r'\unsure{\mathrm{tt}|\forall}',r'\mathrm{tt}',r'\unsure{\forall|\mathrm{tt}}','Two tall strokes and a shared crossbar make a V-like crossed form; two connected t letters remain possible.',13,'low','misread symbol or index',cc=True)
diff('Word before à des constructions',r'\unsure{ramené|revenu}','ramené','ramené','The ending has a separate rising accent and the middle consists of low m/n humps, supporting ramené.',14,'medium','misread word',cc=True,ch=False)
diff('Mark after dans M.',r'\unsure{\S|?}',r'\S',r'\S','A narrow continuous double-loop mark; no separate question-mark point.',14,'high','misread symbol or index',cc=True,ch=False)
diff('M in dans M.',r'M',r'\mathcal{M}',r'M','A plain two-peaked M.',14,kind='misread symbol or index')
diff('Raised family-zero in first saturated definition',r'\inserted{$\mathcal F_0$}',r'\struck{$\mathfrak{F}_0$}',r'\inserted{$\mathcal F_0$}','The family-zero is above the baseline, between saturée and de, without a deletion stroke through that group.',15,kind='deletion state (struck given live or live given struck)',math=True)
diff('Extent of underlined first heading',r'\uline{Partie saturée \inserted{$\mathcal F_0$} de} $\deleted{\unsure{M}}\mathcal F$',r'\emph{Partie saturée de $\mathfrak{F}$}',r'\uline{Partie saturée \inserted{$\mathcal F_0$} de} $\deleted{\unsure{M}}\mathcal F$','The underline runs from Partie through de and ends before the overwritten final capital.',15,kind='insertion or placement')
diff('Earlier M under final family letter of first heading',r'\deleted{\unsure{M}}','',r'\deleted{\unsure{M}}','Two peaked vertical strokes lie under the final heavily drawn hooked family capital; the earlier M reading remains uncertain.',15,'low','omission')
diff('Position of p. r. à parenthesis in first definition',r'cosupport de son cosupport ($\text{p. r. à }\mathcal F$)',r'cosupport (\uncertain{p.r. à} $\mathfrak{F}$) de son cosupport',r'cosupport de son cosupport ($\text{p. r. à }\mathcal F$)','The parenthesis follows the second cosupport, on the lower line of the first definition.',15,kind='insertion or placement',marked='yes')
diff('p. r. à inside first-definition parenthesis',r'\text{p. r. à }',r'\uncertain{p.r. à}',r'\text{p. r. à }','The p, two separate following points and reduced r and à can be followed independently.',15,'medium','misread word','yes')
diff('First saturated definition: raised family-zero, final family letter and parenthetical family letter',r'\mathcal F_0,\mathcal F,\mathcal F',r'\mathfrak{F}_0,\mathfrak{F},\mathfrak{F}',r'\mathcal F_0,\mathcal F,\mathcal F','Hooked or curved family capitals, with a low oval zero in the raised insertion.',15,kind='misread symbol or index')
diff('Second saturée occurrence',r'\unsure{saturée}','saturée',r'\unsure{saturee|saturée}','The reduced letter sequence is legible, but no detached acute can be isolated confidently over the ending.',16,'low','abbreviation expanded or spelling modernised',cc=True)
diff('Second saturated definition: inserted M-zero and both M in the sentence',r'M_0,M,M',r'\mathcal{M}_0,\mathcal{M},\mathcal{M}',r'M_0,M,M','Plain peaked M forms and a low oval zero; the M-zero is raised with a descending insertion stroke.',16,kind='misread symbol or index')
diff('Second saturated definition: support',r'cosupport de son support',r'cosupport de son cosupport',r'cosupport de son support','The second word begins with s directly before the u/p strokes; there is no initial co group.',16,kind='misread word',math=True)
diff('Final mutuellement',r'\unsure{mutuellement}','mutuellement','mutuellement','The crossed middle t and the two later l stems are visible, with a continuous final -ment sequence.',16,'medium','misread word',cc=True,ch=False)
diff('Final par and possible cancellation',r'\unsure{par}','par',r'\unsure{par|\deleted{par}}','A p bowl and long horizontal remainder form one word-sized group. The heavy horizontal may be the flattened ar or a cancellation through it; no second word is invented.',16,'low','deletion state (struck given live or live given struck)',cc=True)
diff('Final display: all three M occurrences',r'M_0,M,M_0',r'\mathcal{M}_0,\mathcal{M},\mathcal{M}_0',r'M_0,M,M_0','Plain M letters with low oval zeros where written.',bbox=[650,1120,1320,1245],source=b,kind='misread symbol or index')
diff('Final display: both family-zero occurrences and family after membership',r'\mathcal F_0,\mathcal F_0,\mathcal F',r'\mathfrak{F}_0,\mathfrak{F}_0,\mathfrak{F}',r'\mathcal F_0,\mathcal F_0,\mathcal F','Family capitals have slanted or curved arms and hooked lower strokes; the plain member F differs.',bbox=[650,1120,1320,1245],source=b,kind='misread symbol or index')
diff('Final set builder: bar over F',r'\overline F\subset M_0',r'F\subset\mathcal{M}_0',r'\overline F\subset M_0','A detached horizontal bar lies above the F before the inclusion.',bbox=[1040,1140,1170,1240],source=b,kind='omission',math=True)
diff('Final display: vertical arrangement',r'\begin{aligned}M_0&=\mathcal F_0\cap M\\\mathcal F_0&=\{\,F\in\mathcal F\mid\overline F\subset M_0\,\}\end{aligned}',r'\mathcal{M}_0=\mathfrak{F}_0\cap\mathcal{M},\qquad\mathfrak{F}_0=\lbrace F\in\mathfrak{F}\mid F\subset\mathcal{M}_0\rbrace.',r'\begin{aligned}M_0&=\mathcal F_0\cap M\\\mathcal F_0&=\{\,F\in\mathcal F\mid\overline F\subset M_0\,\}\end{aligned}','The two equations stand one below the other.',bbox=[650,1120,1320,1245],source=b,kind='insertion or placement')
diff('After first final equation','',',','','No comma is visible after the terminal M of the upper line.',bbox=[900,1120,1020,1190],source=b,kind='text not on the page')
diff('After final brace','','.','','No separate stop follows the final closing brace.',bbox=[1270,1160,1340,1245],source=b,kind='text not on the page')

doubts=[]
def cd(location,c,reading,status,evidence,n=None,bbox=None,source=None):
    cr=crops[n-1] if n else None
    doubts.append(dict(location=location,c=c,reading=reading,status=status,scan_shows=evidence,
       crop=cr['path'] if cr else None,bbox=bbox or (cr['bbox'] if cr else None),bbox_image=source or whole))
cd('C.tex doubt 1: first cosup',r'\unsure{\operatorname{cosup}|\operatorname{cosupp}}',r'\operatorname{cosup}','resolved','One p descender.',1)
cd('C.tex doubt 2: first disjoint ending',r'\unsure{des|de}',r'\unsure{des|de}','retained','Reduced final return does not settle the s.',2)
cd('C.tex doubt 3: relation after first H_i',r'\unsure{\vdash|\in}',r'\vdash','resolved','Straight vertical and one right tick.',2)
cd('C.tex doubt 4: second disjoint ending',r'\unsure{de|des}',r'\unsure{de|des}','retained','Short ending without a decisive s.',2)
cd('C.tex doubt 5: second tiny phi',r'\unsure{\Phi|\varphi}',r'\unsure{\varphi|\Phi}','revised','Small loop and descending hook, not a definite straight base.',2)
cd('C.tex doubt 6 and context duplicate: second set closure',r'\unsure{)|\}}\,\}',r'\unsure{\rbrace|)\rbrace}','revised','A connected irregular brace is possible; an extra rounded close remains possible.',2)
cd('C.tex doubt 7: cancelled wording after Donc',r'\unsure{on aura|on a}',r'\unsure{on aura|on a}','retained','Two cancelled word groups with obscured middle strokes.',4)
cd('C.tex doubt 8: isolated cancelled phi',r'\unsure{\phi|\Phi}',r'\unsure{\phi|\Phi}','retained','Oval with long descender and no definite base.',4)
cd('C.tex doubt 9: cancelled lower-left residual subscript',r'\unsure{,|\mathcal F}',r'\unsure{,|\mathcal F}','retained','Only a short curled remnant survives below the strike.',4)
cd('C.tex doubt 10: overwritten subscript in cancelled right equation',r'\deleted{\unsure{\mathcal F}}M',r'\deleted{\unsure{\mathcal F}}M','retained','A hooked residual group under M is insufficient for certainty.',4)
cd('C.tex doubt 11: left note mutuellement',r'\unsure{mutuellement}',r'\unsure{mutuellement}','retained','Tall middle stem and later loop survive, but linking letters are flattened.',5)
cd('C.tex doubt 12: low dot before family-prime',r'\unsure{.|\cdot}',r'.','resolved','Separate point below the lower equals line at baseline height.',6)
cd('C.tex doubt 13: Stable ending',r'\unsure{Stable|Stables}',r'Stable','resolved','Terminal e has a return but no additional distinct s.',7)
cd('C.tex doubt 14: On a short word',r'\unsure{bien|vu|la|là}',r'\unsure{vu|bien|la|là}','revised','Short rise and flattened run remain insufficient; vu is the best visual reading.',9)
cd('C.tex doubt 15: Sup/Supp',r'\unsure{Sup|Supp}',r'\unsure{Sup|Supp}','retained','Two nearby descenders may be retracing of one p.',10)
cd('C.tex doubt 16: passage à/colon',r'\unsure{à|:}',r'\unsure{à|:}','retained','Two separate small strokes before the clearly separate une.',10)
cd('C.tex doubt 17: cancelled M before barred Phi',r'\deleted{\unsure{M}}',r'\deleted{\unsure{M}}','retained','Two rises are present in the crossed group.',12)
cd('C.tex doubt 18: overwritten subscript in live lower equation',r'\deleted{\unsure{\mathcal F}}M',r'\deleted{\unsure{\mathcal F}}M','retained','Hooked remnants remain under the final M.',13)
cd('C.tex doubt 19: small cancelled group before X',r'\deleted{\unsure{\varnothing|x}}',r'\deleted{\unsure{\varnothing|x}}','retained','Small crossed loop adjoining the brace, distinct from the full X.',13)
cd('C.tex doubt 20 and context notation check: tt/forall',r'\unsure{\mathrm{tt}|\forall}',r'\unsure{\forall|\mathrm{tt}}','revised','A V-like pair of uprights crossed together; two t letters are not excluded.',13)
cd('C.tex doubt 21: ramené/revenu',r'\unsure{ramené|revenu}',r'ramené','resolved','Terminal acute and low m/n humps support ramené.',14)
cd('C.tex doubt 22: final section mark',r'\unsure{\S|?}',r'\S','resolved','A continuous double-loop form, no separate dot.',14)
cd('C.tex doubt 23: overwritten M in first heading',r'\deleted{\unsure{M}}',r'\deleted{\unsure{M}}','retained','Peaked earlier strokes under the hooked live family letter.',15)
cd('C.tex doubt 24: second saturée',r'\unsure{saturée}',r'\unsure{saturee|saturée}','revised','Letters are reduced but recognizable; the accent is not independently identifiable.',16)
cd('C.tex doubt 25: final mutuellement',r'\unsure{mutuellement}',r'mutuellement','resolved','Crossed t, two l stems and ending -ment can be followed.',16)
cd('C.tex doubt 26: terminal par',r'\unsure{par}',r'\unsure{par|\deleted{par}}','revised','One word-sized group; dark horizontal may be the written remainder or a cancellation.',16)
cd('C_context notation check: primes, double primes, family F and plain M',r"\mathcal F',M',\mathcal F'',M''",r"\mathcal F',M',\mathcal F'',M''",'resolved','The top pair has one raised tick each; the lower pair has two. M is plain and family F is hooked. Both halves and crops 01 and 08 were read independently.',8)
cd('C_context notation check: all cosup/cosupp, supp and def occurrences',r'\operatorname{cosup},\operatorname{cosupp},\operatorname{supp},\overset{\text{def}}{=}',r'\operatorname{cosup},\operatorname{cosupp},\operatorname{supp},\overset{\text{def}}{=}','resolved','Top three operators, first cancelled operator, lower-left and lower-right cancelled operators, M-double-prime operator and all three lower operators have one p; the repeated cancelled family definition and live family-double-prime definition have two p stems. Both supp forms have two p stems; neither def label has a distinct accent. Crops 01, 03, 04, 08 and 13 were inspected.',8)
cd('C_context notation check: barred F and two-way double arrow',r'\overline F,\Longleftrightarrow',r'\overline F,\Longleftrightarrow','resolved','Separate bar above F and two full arrowheads joined by two horizontal strokes.',6)
cd('C_context notation check: H_i, union bars and zero indices',r'H_i,\overline H_i,\mathcal F_0,M_0',r'H_i,\overline H_i,\mathcal F_0,M_0','resolved','Both union H labels have short dotted i indices; the upper bar lies over H, not i. The bottom zeros are low ovals. Crops 02, 12, 15, 16 and the lower half supply the local evidence.',12)
cd('C_context explicit check: second saturated definition support',r'cosupport de son support',r'cosupport de son support','resolved','The final word starts with s directly, with no preceding co strokes.',16)

remaining=[]
def rd(location,reading,alternatives,reason,confidence='low'):
    remaining.append(dict(location=location,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason))
rd('First disjoint clause','des',['de'],'Final reduced return does not determine s.')
rd('Second disjoint clause','de',['des'],'Small ending remains compressed.')
rd('Second set final phi',r'\varphi',[r'\Phi'],'Small loop and hooked descender do not settle capitalization/form.')
rd('Second set closing strokes',r'\rbrace',[r')\rbrace'],'Connected irregular brace versus an additional round closing stroke.')
rd('Cancelled first Donc','on aura',['on a'],'Two strike lines hide the middle letters.')
rd('Isolated cancelled phi',r'\phi',[r'\Phi'],'Long descender and obliterated loop.')
rd('Cancelled lower-left operator residual subscript',',',[r'\mathcal F'],'Only a small curled stroke survives.')
rd('Cancelled lower-right operator overwritten subscript',r'\mathcal F',['unrecoverable earlier hooked capital'],'Final M and cancellation hide most of the earlier form.')
rd('Left note accent','déterminent',['determinent'],'Accent-like stroke may join an adjacent letter.')
rd('Left note final word','mutuellement',['unresolved reduced medial letters'],'Some linking letters cannot be separated.','medium')
rd('Left note arrow',r'\longrightarrow',['terminal t and word-ending flourish'],'No fully separate start to the arrow shaft.')
rd('On a following word','vu',['bien','la','là'],'Initial rise and flat run support no unique word.')
rd('Body Sup/Supp','Sup',['Supp'],'Nearby descending strokes may be retraced p or two letters.')
rd('After passage','à',[':'],'Two detached small marks, without a full a loop.')
rd('Before union barred Phi',r'\deleted{M}',['unrecoverable crossed capital'],'Repeated cancellation through the two rising strokes.')
rd('Live lower operator overwritten subscript',r'\deleted{\mathcal F}',['unrecoverable earlier hooked capital'],'Overwriting by M.')
rd('Points after lower operator subscript',r'\ldotp\ldotp',[':','incidental pen points'],'Two diagonal detached points have no certain mathematical function.')
rd('Cancelled group before X',r'\varnothing',['x'],'Small crossed loop touches the opening brace.')
rd('After disjoint de in lower set',r'\forall',[r'\mathrm{tt}'],'Two uprights and shared crossbar admit both forms.')
rd('First heading earlier letter',r'\deleted{M}',['unrecoverable earlier capital'],'Peaked strokes mostly covered by family F.')
rd('Second saturée accent','saturee',['saturée'],'No securely separate acute in this occurrence.')
rd('Final par state','par',[r'\deleted{par}'],'A heavy horizontal may either form the flattened ending or cancel it.')

inventory=[]
def inv(element,kind,position,first):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=first,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('I01','text','Top centre','66')
inv('I02','display','Top first line',r"\mathcal F'=\operatorname{cosup}_{\mathcal F}(\Phi)")
inv('I03','insertion','Above right end of first line',r'\subset\mathcal F')
inv('I04','drawing','Under and right of top inclusion','Curved enclosure and short descending leader')
inv('I05','display','Top second line',r"M'=\operatorname{cosup}_{M}(\Phi)")
inv('I06','insertion','Third top line, indented right',r'=M\cap\operatorname{cosup}_{\mathcal F}(\Phi)\subset M')
inv('I07','drawing','Spanning above third top line','Long curled connecting arm')
inv('I08','deletion','First cancelled prose line','Donc on aura/on a, pour')
inv('I09','deletion','Left of cancelled second row',r'\phi/\Phi')
inv('I10','deletion','Middle of cancelled second row',r"\mathcal F'=\operatorname{cosupp}_{\mathcal F}(\Phi)")
inv('I11','deletion','Right of cancelled second row',r"M'=\mathcal F'\cap M,")
inv('I12','deletion','Below-left of cancelled block',r'F\in\operatorname{cosup}')
inv('I13','deletion','Below-right of cancelled block',r'=\operatorname{cosup}_{M}(\mathcal F)')
inv('I14','deletion','Under M subscript in cancelled lower-right formula',r'\unsure{\mathcal F}')
inv('I15','text','Below cancelled block','Donc pour')
inv('I16','margin note','Slanted left of braced display','Ainsi, M′ et ℱ′ se déterminent mutuellement')
inv('I17','drawing','From end of left note towards brace','Uncertain rightward arrow / terminal hook')
inv('I18','display','Centre, two lines under left brace',r"F\in\mathcal F'\Longleftrightarrow\overline F\subset M'")
inv('I19','margin note','Right of braced display','NB ℱ′, M′ sont des parties fermées de ℱ, M.')
inv('I20','margin note','Below-left of NB block','ℱ′ / Stable par Sup.')
inv('I21','drawing','Around separate ℱ′ and Stable note','Angular arm, underline enclosure and long lower continuation')
inv('I22','text','Below braced display','Soit d’autre part')
inv('I23','display','First double-prime definition',r"\mathcal F''=\operatorname{cosupp}_{\mathcal F}(\mathcal F')\overset{\text{def}}{=}\operatorname{supp}_{\mathcal F}(\Phi)")
inv('I24','display','Second double-prime definition',r"M''=\operatorname{cosup}_{M}(\mathcal F')\overset{\text{def}}{=}\operatorname{supp}_{M}(\Phi)")
inv('I25','text','Middle paragraph over three lines','On a vu/bien/la/là … et par passage à/: une sous-figure. Soit … alors')
inv('I26','deletion','Second line of middle paragraph','contient Φ')
inv('I27','deletion','Immediately before barred Phi in union',r'\unsure{M}')
inv('I28','display','Inline union in middle paragraph',r'\overline\Phi=\bigcup_{H_i\in\Phi}\overline H_i')
inv('I29','display','Lower first equation',r'\operatorname{cosup}_{\mathcal F}(\Phi)=\operatorname{cosup}_{\mathcal F}(M_{\overline\Phi})')
inv('I30','display','Lower second equation',r'\operatorname{cosup}_{M}(\Phi)=\{X\in M\mid\cdots\}')
inv('I31','deletion','Under M subscript in lower second equation',r'\unsure{\mathcal F}')
inv('I32','deletion','After opening brace, before lower X',r'\unsure{\varnothing|x}')
inv('I33','text','Below lower equations, two lines','donc on est ramené à des constructions dans M.')
inv('I34','text','After dans M. at mid-page width',r'\S')
inv('I35','text','First saturated definition, underlined beginning','Partie saturée … de ℱ : égale au cosupport de son cosupport (p. r. à ℱ).')
inv('I36','insertion','Above saturée/de in first saturated definition',r'\mathcal F_0')
inv('I37','deletion','Under final family letter of first heading',r'\unsure{M}')
inv('I38','text','Second saturated definition','Partie saturee/saturée … de M : égale au cosupport de son support (dans M).')
inv('I39','insertion','Above de M in second saturated definition',r'M_0')
inv('I40','text','Bottom prose continuing over line break','Elles se correspondent mutuellement par')
inv('I41','deletion','Final par, cancellation only as an in-place alternative',r'\unsure{par|\deleted{par}}')
inv('I42','display','First final equation',r'M_0=\mathcal F_0\cap M')
inv('I43','display','Second final equation',r'\mathcal F_0=\{F\in\mathcal F\mid\overline F\subset M_0\}')

notation=[
 dict(sign='Family F',latex=r'\mathcal F',appearance='Curved or looped top and hooked lower stroke; some occurrences heavily retraced.',location='Top definitions; cancelled block; braced display; NB; double-prime definitions; lower equations; saturated definitions and final display',alternatives=[]),
 dict(sign='Member F',latex='F',appearance='Plain upright with straight upper and middle arms.',location='All F membership clauses and both barred-member expressions',alternatives=[]),
 dict(sign='Ambient M',latex='M',appearance='Two plain rising peaks; no separate calligraphic construction.',location='Throughout this page',alternatives=[]),
 dict(sign='Single and double primes',latex=r"{}',{}''",appearance='One or two separate short raised ticks.',location='First and double-prime definitions, margins and braced display',alternatives=[]),
 dict(sign='First H_i relation',latex=r'\vdash',appearance='Straight upright with one rightward tick.',location='First top set builder',alternatives=[]),
 dict(sign='Tiny second-set phi',latex=r'\unsure{\varphi|\Phi}',appearance='Small oval above descending stem and hooked foot.',location='End of second top set builder',alternatives=[r'\Phi']),
 dict(sign='Bar and equivalence',latex=r'\overline F,\Longleftrightarrow',appearance='Detached bar; two horizontal arrow shafts and two arrowheads.',location='Braced display',alternatives=[]),
 dict(sign='Low point',latex='.',appearance='Separate point at baseline height, lower than the equals strokes.',location='Second braced line',alternatives=[]),
 dict(sign='Union H and i',latex=r'\overline H_i, H_i',appearance='H with two joined stems; short dotted low i; bar above H only.',location='Union and its subscript',alternatives=[]),
 dict(sign='Crossed two-upright sign',latex=r'\unsure{\forall|\mathrm{tt}}',appearance='V-like pair of tall strokes sharing a crossbar.',location='After disjoint de in lower set builder',alternatives=[r'\mathrm{tt}']),
 dict(sign='Subscript barred Phi',latex=r'M_{\overline\Phi}',appearance='Barred Phi wholly below M as its index.',location='Lower two equations',alternatives=[]),
 dict(sign='Zero indices',latex=r'\mathcal F_0,M_0',appearance='Low oval zeros, including both raised insertions.',location='Saturated definitions and final display',alternatives=[]),
 dict(sign='Section sign',latex=r'\S',appearance='Narrow joined double loop without a detached point.',location='After dans M.',alternatives=[]),
 dict(sign='Small detached points',latex=r'\unsure{\ldotp\ldotp|:}',appearance='Two small diagonally placed points after the corrected M subscript.',location='Lower second operator',alternatives=[':','incidental pen points']),
]
abbreviations=[
 dict(form='cosup',expansion='cosupport'),dict(form='cosupp',expansion='cosupport'),
 dict(form='supp',expansion='support'),dict(form='def',expansion='définition'),
 dict(form='NB',expansion='nota bene'),dict(form='Sup',expansion='supremum; exact abbreviation only transcribed'),
 dict(form='p. r. à',expansion='par rapport à'),dict(form='tt (if this is the lower sign)',expansion='tout'),
]

observations={
1:'One terminal p in each of the first two cosup forms; plain M and family F; separate single primes.',
2:'Retained both des/de endings; first relation resolved to upright-and-tick vd; second phi and closure retained as uncertain; traced raised inclusion enclosure.',
3:'One p in third cosup; read full added equality and its long overlying connector.',
4:'Read every cancelled row. Retained on aura/on a, isolated phi and two obscured subscripts; distinguished one-p and two-p operators and the repeated family definition.',
5:'Read the left note in the rotated image. Retained reduced mutuellement and an accent doubt; terminal arrow versus final-letter hook remains open.',
6:'Confirmed barred F, two arrowheads and two shafts. Resolved the extra point as low baseline dot.',
7:'Read NB and its separate family-prime/Stable continuation. Resolved Stable without a distinct final s; traced underlining and angular/curved enclosure strokes.',
8:'Confirmed two primes, two-p cosupp in first equation, one-p cosup in second, two-p supp twice, and def without a distinct accent twice.',
9:'Read the short word after On a; flattened ink supports vu first but does not settle the alternatives.',
10:'Retained Sup/Supp; observed separate comma; retained a/colon after passage and read une as a separate word.',
11:'Read struck contient Phi; live sous-figure ends singular with a separate stop.',
12:'Retained cancelled M before barred Phi; checked both dotted i labels, H bar and comma before alors.',
13:'Read all three one-p lower cosup forms, corrected subscript, two small detached points, pre-X crossed loop, both X forms, forall/tt sign and barred-Phi M subscripts.',
14:'Resolved ramené by medial humps and final accent; resolved continuous double-loop section sign.',
15:'Checked underline extent, raised family-zero, overwritten heading capital and parenthesis position; p. r. à is legible.',
16:'Checked second saturated definition, live raised M-zero, support without co, final mutuellement and ambiguous cancellation of par; second saturée accent remains uncertain.',
}

def macro_groups(text, command):
    out=[]
    p=0
    token='\\'+command+'{'
    while True:
        start=text.find(token,p)
        if start<0:
            return out
        depth=1
        i=start+len(token)
        while depth:
            c=text[i]
            bs=0
            j=i-1
            while j>=0 and text[j]=='\\':
                bs+=1
                j-=1
            if not bs%2:
                if c=='{': depth+=1
                elif c=='}': depth-=1
            i+=1
        out.append(text[start:i])
        p=i

figure_groups=macro_groups((OUT/'reading.tex').read_text(),'figure')
for d in diffs:
    if d['location'] in ['Enclosure and leader around raised top inclusion','Long connector over third top equality','Raised inclusion in first definition']:
        d['reading']=figure_groups[0]
    elif d['location']=='Right note enclosure and connecting arms':
        d['reading']=figure_groups[1]
    if d['location']=='Top first definition: family initial, operator subscript, family after membership, and raised inclusion':
        d['bbox']=[430,20,1668,205]
        d['scan_shows']+=' The first half and crops 01–02 cover the separately named occurrences.'
    elif d['location']=='Top second definition: M prime, operator subscript and ambient M':
        d['bbox']=[430,200,1150,303]
        d['scan_shows']+=' The ambient M after X was read in the first half.'
    if d['location'] in ['After passage','Number of sous-figure']:
        d['marked_in_h']='yes'

report=dict(reader='R3',cote='156-4',scan='067',brief_version='v03',
 started_utc='2026-11-20T09:53:26Z',finished_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
 image_views=meta['images'],reading_file=str(OUT/'reading.tex'),differences=diffs,c_doubts=doubts,
 inventory=inventory,remaining_doubts=remaining,notation=notation,abbreviations=abbreviations,
 notes=dict(
  summary='Handwritten page 66 defines cosupport and support, gives a braced relation with two marginal notes, then defines saturated parts. A heavily cancelled draft lies between the first definitions and the live Donc. All connected graphic enclosures are represented in TikZ.',
  math_reading_decisions='No mathematical proof or computation was used. Direct ink comparison distinguished one-p cosup from two-p cosupp/supp and member F from family F. Formula structure drew attention to the first upright-and-tick relation, the low dot, the bottom F bar and the surprising final support; none was normalized to an expected mathematical statement.',
  author_checks='No authorial proof check or explicit correction of a theorem is asserted. The bottom phrase is copied as “cosupport de son support”, despite the preceding family definition using cosupport twice. Cancelled and overwritten groups are retained, with uncertainty where their letters or state remain obscured.',
  title_dates_pagination='Manuscript page number 66 at top centre; scan 67 retained. No date or separate title. “Partie saturée … de” is underlined in the first lower definition. No cote marker has been added.'),
 check_events=[],crops=crops,
 workflow_feedback=['The prescribed crop width is useful, but cancellation blocks containing several tightly adjacent uncertain groups need a single wider crop; independently recropping each glyph would overlap the same evidence. This run used 16 locus-cluster crops and never recropped a decided place.','The report schema should specify whether change_c and change_h are booleans; this report uses booleans. All bbox values explicitly name the source with bbox_image.'])
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

lines=['# R3 inspection log — 156-4 scan 067','',
'Started reading packet at 2026-11-20T09:53:26Z. The assignment, v03 brief, packet metadata, C.tex, H.tex, conventions, preamble, C_context and the supplied notation snapshot were read before inspection. No other reader or page was consulted.',
'','## Actual view order','',
f'1. `{whole}` — whole page viewed once for layout. Identified page number, two top definitions, raised inclusion, added equality, connecting lines, cancelled block, braced display, both marginal notes, support definitions, middle prose and union, lower equations, section mark, saturated definitions, raised labels, overwritten letters and final two-line display.',
f'2. `{a}` — upper half viewed once at supplied resolution. Read all lines and symbols against both witnesses.',
f'3. `{b}` — lower half viewed once at supplied resolution. Read all lines and symbols against both witnesses.',
'','The open loci were then listed in `create_crops.py`; all 16 crops were generated once from the original whole-page image. Each was displayed once, in the following order. Tool results contained at most three crop images, and no displayed crop was truncated.','']
for i,cr in enumerate(crops,1):
    lines.extend([f"{i+3}. `{cr['path']}`",f"   Source: `{cr['source']}`. Original bbox: {cr['bbox']}. Rotation: {cr['rotation']}° (PIL positive is counterclockwise). LANCZOS scale after rotation: {cr['scale']:.9f}; final width 2600 px. Autocontrast, then UnsharpMask radius 1.3 / percent 120 / threshold 3; JPEG quality 94, no chroma subsampling.",f'   Visible evidence: {observations[i]}',''])
lines.extend(['## Completion and limits','','All three supplied images and every listed crop were actually viewed. No whole page or full half was shown a second time. No OCR, text recognition, web research or LaTeX compiler was invoked. The final two equations were decided from the lower half; their report bboxes are on that half, not on the whole image. All crop bboxes are on the original whole-page image.','',f'Completed {report["finished_utc"]}. Differences: {len(diffs)}. C-doubt dispositions: {len(doubts)}. Remaining doubts: {len(remaining)}. Inventory elements: {len(inventory)}. Crops: {len(crops)}.'])
(OUT/'inspection_log.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({k:len(report[k]) for k in ['differences','c_doubts','remaining_doubts','inventory','crops']},indent=2))
