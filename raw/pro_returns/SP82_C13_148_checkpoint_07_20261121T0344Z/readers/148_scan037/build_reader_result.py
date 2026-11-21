from pathlib import Path
import json,re,csv
P=Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan037')
O=Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148/readers/148_scan037')
C=(P/'C.tex').read_text();H=(P/'H.tex').read_text()
B=json.loads((O/'crop_boxes.json').read_text())
S=C[:C.index(r'\unsure{\texttt{TRACE}}')].rstrip()+'\n'
ineq=r"""\tikz[baseline=(ineq.base)]{
\node[inner sep=1pt] (ineq) {$\mu^2-4\ne0\quad\text{i.e.}\quad\unsure{\mu^2|\mu}\ne\pm2$};
\draw ([xshift=-2pt,yshift=4pt]ineq.south west)
 .. controls ([xshift=-2pt,yshift=-2pt]ineq.south west) and
 ([xshift=-1pt,yshift=-3pt]ineq.south west) .. ([xshift=2pt,yshift=-3pt]ineq.south west)
 -- ([xshift=-2pt,yshift=-3pt]ineq.south east)
 .. controls ([xshift=1pt,yshift=-3pt]ineq.south east) and
 ([xshift=2pt,yshift=-1pt]ineq.south east) .. ([xshift=2pt,yshift=1pt]ineq.south east);
\draw ([xshift=5pt,yshift=2pt]ineq.south east) -- ([xshift=5pt,yshift=2pt]ineq.north east);
}"""
margin=r"""\margin{\begin{tikzpicture}[baseline=(eq.base)]
\node[inner sep=1pt] (eq) {où $\mu'=\tfrac12\mu$};
\node[anchor=west,inner sep=1pt] (ie) at (eq.east) {i.e.};
\draw ([xshift=-2pt]eq.west)
 .. controls ([xshift=2pt,yshift=3pt]eq.north west) and
 ([xshift=-4pt,yshift=4pt]eq.north east) .. ([xshift=0pt,yshift=2pt]eq.north east)
 .. controls ([xshift=2pt]eq.north east) and
 ([xshift=-2pt,yshift=-2pt]ie.south west) .. ([xshift=2pt,yshift=-2pt]ie.south west)
 -- ([yshift=-2pt]ie.south east);
\end{tikzpicture}}"""
S=S.replace(r'\mspage{36}',r'\margin{36}')
S=S.replace(r'\deleted{\unsure{près}}',r'\uline{\unsure{un|aux}} ')
S=S.replace(r"\unsure{\lambda''|\lambda'}\underset{\unsure{\mathrm{df}}}{=}",r"\lambda'\overset{\unsure{\mathrm{df}}}{=}")
S=S.replace(r'\unsure{2}=','2=')
S=S.replace(r'\frac{\xi}{\eta}+\frac{\eta}{\xi}\ne2.',r'\frac{\xi}{\eta}+\frac{\eta}{\xi}\ne2')
S=S.replace(r'$\mu=\xi_0+\eta_0\in\mathbb C$ satisfaisant',r'$\mu=\xi_0+\eta_0\inserted{\in\mathbb C}$, satisfaisant')
S=S.replace(r"$\uline{\mu^2-4\ne0\quad\text{i.e.}\quad\unsure{\mu^2|\mu}\ne\pm2}$",ineq)
S=S.replace('néct non nulles',r'néc\textsuperscript{t} non nulles')
S=S.replace(r'\tfrac12\left(\mu\pm\sqrt{\mu^2-4}\right)',r'\tfrac12\left(\mu\pm\sqrt{\mu^2-4}\right.')
S=S.replace(r"\left\{\pm\sqrt{\mu'\pm\sqrt{\mu'^2-1}}\right\}.",r"\left\{\pm\sqrt{\mu'\pm\sqrt{\mu'^2-1}}\right\}")
S=S.replace(r"\margin{où $\mu'=\tfrac12\mu$ i.e.}",margin)
(O/'candidate.tex').write_text(S)
(O/'reading_components.json').write_text(json.dumps({'ineq':ineq,'margin':margin},ensure_ascii=False,indent=2)+'\n')

def ref(k):return f'crops/148_scan037_{k}.png'
changes=[]
def ch(place,c,h,final,ink,k,kind,ac=False,ah=False,math=False,confidence='high',**kw):
    assert c is None or c in C,('C',place,c)
    assert h is None or h in H,('H',place,h)
    d=dict(place=place,c=c,h=h,final=final,ink=ink,crop=ref(k),box=B[k],confidence=confidence,kind=kind,against_c=ac,against_h=ah,math=math)
    d.update(kw);changes.append(d)
ch('top-left foliation',r'\mspage{36}',None,r'\margin{36}','The first digit has two open rounded lobes; the second has an ascending upper stroke returning into a closed lower loop. The lighter 36 is in an unassigned hand.','foliation','omission',ah=True)
ch('opening words','le carré est',r'\uncertain{le} \ill{} est','le carré est','The looped l and low e, followed by the c opening and joined arr/e strokes, are readable; the final raised terminal stroke belongs to the accented ending.','opening',r'readable ink left as \ill{}',ah=True)
ch('first display, cancelled fraction',r'\deleted{\unsure{\frac{\xi}{\eta}}}',None,r'\deleted{\unsure{\frac{\xi}{\eta}}}','A crossed stacked group precedes the live xi/eta fraction. The upper angular and lower descending shapes support the tentative fraction, but their crossings obscure parts; no certainty is supplied. H only comments on overtracing and omits this cancelled group.','top_formula','omission',ah=True,math=True,confidence='low')
a=H.index('départ :')+len('départ ');z=H.index(r'\emph',a)
ch('isomorphism phrase','à iso.',H[a:z],'à iso.','After the compact a-like mark, the abbreviation has a dotted i, low s, rounded o, and point; there is no second e of i.e.','iso_condition','misread word',ah=True)
ch('short underlined word after iso.',r'\deleted{\unsure{près}}',r'\uncertain{aux}',r'\uline{\unsure{un|aux}}','The word begins with low undulating strokes, unlike the long p descender in the following près. Its horizontal stroke is below all the letter bodies, like the underline under unique; it is not a secure through-letter cancellation. An unfinished un-like beginning or aux remains possible.','iso_condition','deletion state',ac=True,ah=True,confidence='low')
ch('unique près',r'\uline{unique}',r'\uncertain{isomorphismes}',r'\uline{unique}','The low u/n/i strokes lead to a looped q with a long descender and the final u/e. A separate line runs below the word. There is no long isomorphismes sequence.','iso_condition','misread word',ah=True)
ch('condition wording','à mettre',r'\uncertain{imposée}','à mettre','A compact à precedes the low m/e and tall crossed t strokes of mettre; the initial i/m/p sequence of imposée is absent.','iso_condition','misread word',ah=True)
ch('definition display, prime',r"\unsure{\lambda''|\lambda'}",r"\lambda'",r"\lambda'",'One detached upright follows lambda. The next thin upright is attached to the small annotation cluster over the equals sign, not a second independent prime.','lambda_prime','misread symbol or index',ac=True,math=True,certainty_resolution=True,mark_ids=['M0467'])
ch('definition display, annotation above equals',r'\underset{\unsure{\mathrm{df}}}{=}',r"\lambda' = \lambda - 2",r'\overset{\unsure{\mathrm{df}}}{=}','The small looped d/f-like cluster lies above the two short horizontal equality strokes. A descending stroke from the preceding text crosses the area, so the exact df reading remains doubtful. C puts the annotation below the sign and H omits it.','lambda_prime','insertion or placement',ac=True,ah=True,math=True,confidence='medium')
ch('definition display, retouched 2',r'\unsure{2}',r'\lambda - 2','2','Despite retouching, the curved upper entry, descending diagonal and broad returning lower foot give 2. The crossing remains an overtrace; no earlier numeral is invented.','lambda_prime','misread symbol or index',ac=True,math=True,certainty_resolution=True,mark_ids=['M0469'])
ch('definition display, final punctuation',r'\frac{\xi}{\eta}+\frac{\eta}{\xi}\ne2.',r'\frac{\eta}{\xi} \neq 2',r'\frac{\xi}{\eta}+\frac{\eta}{\xi}\ne2','The final 2 has a returning foot and blank space to its right; no separate final point appears.','lambda_prime','text not on the page',ac=True,math=True)
ch('basis paragraph, En termes','En termes',r'En \uncertain{prenant}','En termes','A tall crossed t is followed by the low ermes sequence. There is no initial descending p or the later -nant sequence of prenant.','basis','misread word',ah=True)
ch('basis paragraph, tentative cancelled de',r'\deleted{\unsure{de}}',r'\struck{\ill{}}',r'\deleted{\unsure{de}}','A small ascending stroke and low body survive before e1 under a heavy horizontal strike. They support de only tentatively; the strike prevents complete letter recovery.','basis','misread word',ah=True,confidence='low')
ch('basis formula, fourth power',r'e_1^4',r'e_1^{\otimes 4}',r'e_1^4','The superscript consists of the angled upper part, cross stroke and descending limb of 4. There is no separate circled cross before it.','basis','text not on the page',ah=True,math=True)
ch('basis sentence, donnant','donnant une base','donc aussi une base','donnant une base','After the looped initial d, a long low connected onnan sequence ends in a short t. Une is separate; no extra aussi word is present.','basis','misread word',ah=True)
a=H.index(r'\add{par}');z=H.index(r'\note{en interligne',a)
ch('pair insertion and baseline par',r"par \inserted{la paire d'éléments distincts}",H[a:z],r"par \inserted{la paire d'éléments distincts}",'Par sits at the start of the main formula baseline. Above xi0, eta0 a leader joins the interlinear la paire d’éléments distincts: the p descender and the short aire ending distinguish paire from couple. No original parenthesis precedes that leader.','pair','insertion or placement',ah=True,math=True)
ch('parameter transition','ou encore par',r'i.e.\ aussi par','ou encore par','The low initial ou and the separate encore have the rounded c and linked ending; there is no dotted i.e. followed by aussi.','parameter','misread word',ah=True)
ch('parameter, raised membership insertion',r'\mu=\xi_0+\eta_0\in\mathbb C',r'\mu = \xi_0\n+ \eta_0 \in \mathbf{C}'.replace(r'\n','\n'),r'\mu=\xi_0+\eta_0\inserted{\in\mathbb C}','The membership sign and C stand above the mu/xi0/eta0 baseline. A long curved leader returns from their right to the insertion place after eta0. Both witnesses flatten this raised addition.','parameter','insertion or placement',ac=True,ah=True,math=True)
ch('parameter, comma before satisfaisant',r'\mathbb C$ satisfaisant',r'\mathbf{C}$, satisfaisant',r'$\mu=\xi_0+\eta_0\inserted{\in\mathbb C}$, satisfaisant','A short detached curved stroke descends at the baseline after eta0, to the right of the returning insertion leader. Its separation from the long leader supports a comma before satisfaisant.','parameter','omission',ac=True,math=True,confidence='medium')
ch('recovery of xi0 and eta0','se récupérant',r'se \uncertain{récupérant}','se récupérant','The word has an accented e, the c opening, a descending p, and the joined -érant ending. The surrounding se and comme are distinct.','parameter','misread word',ah=True)
ch('distinctness formula, bent underline',r'$\uline{\mu^2-4\ne0\quad\text{i.e.}\quad\unsure{\mu^2|\mu}\ne\pm2}$',r'$\mu^{2} - 4 \neq 0$ i.e.\ $\mu \neq \pm 2$',ineq,'A long line lies below the complete comparison, with an extended upward left end and a small upward right end. A separate tall vertical stroke stands just to the right, before s’exprime. Both line strokes are reproduced without assigning a punctuation role. The raised black cluster after the second mu remains doubtful, possibly a cancelled 2; the drawing does not resolve it.','distinctness','drawing or diagram',ac=True,ah=True,math=True)
ch('distinctness sentence',"s'exprime par",'signifiant que',"s'exprime par",'The initial s/apostrophe is followed by the x crossing and long p descender of exprime, then the separate par. No signifiant que sequence is written.','distinctness','misread word',ah=True)
ch('nonzero-root parenthesis','néct non nulles car',r'\uncertain{vu} \uncertain{que}',r'néc\textsuperscript{t} non nulles car','The short form starts néc with an accent and ends in a raised t. The following two words are non nulles; car begins the next baseline before leur produit est 1. H omits the nonzero wording.','distinctness','abbreviation expanded or spelling modernised',ac=True,ah=True,additional_evidence=[dict(crop=ref('recover'),box=B['recover'])])
ch('On récupère','On récupère',r'On \uncertain{récupère}','On récupère','After the round O/n, the word shows the low récu sequence, a descending p and the final ère. It is live after the cancelled word.','recover','misread word',ah=True)
ch('baseline l’ens des',"l'ens des",r"\add{l'ens.\ des}","l'ens des",'The words follow comme on the same ascending baseline as solutions de. There is no insertion leader or separate higher line, and no point after ens.','recover','insertion or placement',ah=True)
ch('first radical, closing parenthesis at page edge',r'\tfrac12\left(\mu\pm\sqrt{\mu^2-4}\right)',"\\tfrac{1}{2}\\bigl(\\mu \\pm \\sqrt{\\mu^{2} -\n4}\\bigr)",r'\tfrac12\left(\mu\pm\sqrt{\mu^2-4}\right.','The opening parenthesis before mu is visible. After the inner radicand 4, the surviving paper shows a small spot and the separate set brace, but no closing parenthesis can be read above the clipped edge. An invisible TeX delimiter prevents an unobserved parenthesis from being supplied.','roots','text not on the page',ac=True,ah=True,math=True,confidence='medium')
ch('radical display, final point',r"\left\{\pm\sqrt{\mu'\pm\sqrt{\mu'^2-1}}\right\}.",r"\sqrt{\mu'^{2} - 1}} \Bigr\rbrace",r"\left\{\pm\sqrt{\mu'\pm\sqrt{\mu'^2-1}}\right\}",'The rightmost set brace meets the paper edge; no separate final point is visible. The source edge, rather than expected sentence punctuation, is retained.','roots','text not on the page',ac=True,math=True)
ch('mu-prime margin, curved enclosing stroke',r"\margin{où $\mu'=\tfrac12\mu$ i.e.}",r"\marginal{où $\mu' = \frac{1}{2}\mu$ i.e.}",margin,'The text has one prime, a stacked 1/2, and the final i.e. A long curved stroke starts at the left, runs above où and the equation, turns down after mu, and continues beneath i.e. H describes this stroke in its note; C omits it.','muprime_margin','drawing or diagram',ac=True,math=True)
start=C.index(r'\unsure{\texttt{TRACE}}');star=C.index(r'\texttt{********')
ch('pale reversed listing, first witness block',C[start:star].strip(),None,'','The mechanically uniform characters are pale blue with laterally reversed asymmetric letter shapes, behind the dark upright handwriting. They are reverse-side show-through, not additional front text. This excludes C’s attempted TRACE/JCL blocks and their associated unreadable tokens.','bleed_upper','text not on the page',ac=True,mark_ids=[f'M{i:04d}' for i in range(471,480)],additional_evidence=[dict(crop=ref('bleed_lower'),box=B['bleed_lower'])])
ch('pale reversed listing, remaining witness block',C[star:].strip(),None,'','The pale blue asterisk band and machine rows share the reversed orientation and background colour of the upper listing. Their regular strokes pass beneath the darker manuscript. C’s remaining listing block is therefore omitted rather than guessed or marked illegible.','bleed_lower','text not on the page',ac=True,mark_ids=[f'M{i:04d}' for i in range(480,499)],additional_evidence=[dict(crop=ref('bleed_upper'),box=B['bleed_upper'])])

decisions=[]
def de(i,d,reading,ink,k,confidence='high'):
    decisions.append(dict(id=i,decision=d,reading=reading,ink=ink,crop=ref(k),box=B[k],confidence=confidence))
de('M0467','alternative',r"\lambda'",'One detached upright follows lambda; the adjacent upright belongs to the annotation cluster.','lambda_prime')
de('M0468','undecided',r'\overset{\unsure{\mathrm{df}}}{=}','The d/f-like loops lie above the equals sign, but overlapping descending ink prevents secure identification of both letters.','lambda_prime','medium')
de('M0469','first','2','The retouched sign retains a curved upper entry, diagonal descent and broad lower foot characteristic of 2.','lambda_prime')
de('M0470','undecided',r'\unsure{\mu^2|\mu}\ne\pm2','A raised black cluster follows mu. It may retain a 2, or be a cancelled superscript; no separate surviving numeral is plain enough to settle the choice.','distinctness','low')
for i in range(471,499):
    de(f'M{i:04d}','other','','Pale blue mechanically repeated strokes have reversed asymmetric letters and lie behind the upright dark handwriting. The mark belongs to reverse-side printing and is omitted from the front-side transcription.','bleed_upper' if i<480 else 'bleed_lower')

inventory=[]
def iv(e,k,pos,words,hand='main manuscript hand'):
    inventory.append(dict(element=e,kind=k,position=pos,first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes'))
iv('foliation','margin note','top left',r'\margin{36}','unassigned lighter foliation hand')
iv('opening','text','above first display','le carré est')
iv('lambda_display','display','upper page',r'\lambda=(\xi+\eta)^2/(\xi\wedge\eta)')
iv('cancelled_fraction','deletion','after first display equality',r'\deleted{\unsure{\frac{\xi}{\eta}}}')
iv('recover_situation','text','four lines below first display','et dont la connaissance nous permet')
iv('short_underlined_word','text','end of iso. line',r'\uline{\unsure{un|aux}}')
iv('unique_underline','text','start of following line',r'\uline{unique} près')
iv('lambda_prime_display','display','above basis paragraph',r"\lambda'\overset{\unsure{\mathrm{df}}}{=}\lambda-2")
iv('basis','text','middle three baselines',"En termes d'une base")
iv('cancelled_de','deletion','between base and e1',r'\deleted{\unsure{de}}')
iv('pair','insertion','above xi0 and eta0',r"\inserted{la paire d'éléments distincts}")
iv('parameter','text','from pair coordinates through quadratic introduction',r'\(\xi_0,\eta_0\in\mathbb C\)')
iv('parameter_membership','insertion','above the parameter sum, linked after eta0',r'\inserted{\(\in\mathbb C\)}')
iv('quadratic','display','lower middle',r'z^2-\mu z+1=0,')
iv('distinctness_sentence','text','below quadratic',"l'équation")
iv('distinctness_underline','drawing','beneath and at right of complete distinctness comparison','bent underline with upward ends and separate vertical at right')
iv('inserted_two','insertion','above gap between les and solutions',r'\inserted{2}')
iv('nonzero_parenthesis','text','next two baselines',r'néc\textsuperscript{t} non nulles car leur produit est \(1\)')
iv('cancelled_Les','deletion','before On récupère',r'\deleted{\unsure{Les}}')
iv('recover_I','text','above quartic',"On récupère I comme l'ens des solutions de")
iv('quartic','display','near bottom',r'z^4-\mu z^2+1=0')
iv('radicals','display','at lower paper edge',r'I=\left\{\pm\sqrt{\tfrac12\left(\mu\pm\sqrt{\mu^2-4}\right.}\right\}')
iv('muprime_note','margin note','bottom left',r"où \(\mu'=\tfrac12\mu\) i.e.")
iv('muprime_enclosure','drawing','around the bottom-left note','curve over the equation and under i.e.')

unresolved=[
dict(place='first display, cancelled fraction',reading=r'\deleted{\unsure{\frac{\xi}{\eta}}}',issue='Heavy crossing obscures parts of both stacked signs.',alternatives=[r'\frac{\xi}{\eta}'],confidence='low'),
dict(place='word after iso.',reading=r'\uline{\unsure{un|aux}}',issue='Low beginning and linked terminal strokes do not certify a complete word; the un-like form may be unfinished. The visible line is below the letters; a cancellation cannot be securely asserted.',alternatives=['un','aux'],confidence='low'),
dict(place='definition annotation',reading=r'\overset{\unsure{\mathrm{df}}}{=}',issue='The annotation is above the equals sign but is crossed by descending ink; both letters are not independently secure.',alternatives=[r'\mathrm{df}'],confidence='medium'),
dict(place='basis paragraph, cancelled de',reading=r'\deleted{\unsure{de}}',issue='The strike obscures most of the low letters.',alternatives=['de'],confidence='low'),
dict(place='distinctness, raised cluster after mu',reading=r'\unsure{\mu^2|\mu}\ne\pm2',issue='The raised black cluster may be a 2 or a cancelled exponent. Mathematical equivalence is not used to force its state.',alternatives=[r'\mu^2',r'\mu',r'\mu^{\deleted{2}}'],confidence='low'),
dict(place='cancelled Les',reading=r'\deleted{\unsure{Les}}',issue='The L is visible but e/s are entangled with the strike.',alternatives=['Les'],confidence='low'),
dict(place='first radical, closing parenthesis',reading=r'\sqrt{\tfrac12\left(\mu\pm\sqrt{\mu^2-4}\right.}',issue='The formula touches the lower paper edge; no closing parenthesis is readable in the surviving area. It is not supplied.',alternatives=[],confidence='medium'),
]
notes=[
dict(id='148037_N01',text='This portrait handwritten page is on the reverse of listing paper. The pale blue mechanically printed matter is laterally reversed and is excluded as show-through; C mistakenly treated it as additional front text. The lighter top-left 36 is retained as unassigned foliation. No authorial number or date is inferred from H’s editorial notes.'),
dict(id='148037_C01',text='The opening continues a preceding discussion. It writes lambda as a ratio involving xi wedge eta and as xi/eta+eta/xi+2, then shifts to lambda-prime=lambda−2. The geometric identification, the wedge/product convention and the claimed recovery up to unique isomorphism were not independently proved from this isolated leaf.'),
dict(id='148037_C02',text='The page writes e1^4=e=xi wedge eta, uses e1^2 as a base of L2, and introduces distinct scalar coordinates xi0,eta0 with product1 and sum mu. These conventions are transcribed; no tensor symbol is added before the fourth-power exponent.'),
dict(id='148037_C03',text='For the scalar quadratic z^2−mu z+1, the computed discriminant is mu^2−4. Over C, nonzero discriminant gives two distinct roots; their product1 makes both nonzero. Thus the condition is mu≠±2. If the raised dark mark in the manuscript’s second comparison is a live2, that written comparison would be a slip: mu=2 would satisfy mu^2≠±2 while giving the repeated root1. The ink remains unresolved.'),
dict(id='148037_C04',text='Expanding (z^2−xi0)(z^2−eta0) and substituting xi0+eta0=mu and xi0 eta0=1 gives z^4−mu z^2+1. Each nonzero scalar root has two opposite square roots over C, and distinct scalar roots give disjoint pairs, yielding four distinct roots under the stated discriminant condition.'),
dict(id='148037_C05',text='The radical expression follows by solving the quadratic in z^2. The rescaling mu-prime=mu/2 converts (mu^2−4)/4 to mu-prime^2−1; the two inner sign choices give the same set after this rescaling. A closing parenthesis and final punctuation not readable at the clipped paper edge are not silently supplied.'),
dict(id='148037_N02',text='The short word following iso. is underlined but remains unclear, tentatively un|aux. Its strokes differ from the clear later près. The cancelled fraction, de and Les retain their doubts; the superscript after mu is not forced by the discriminant calculation.'),
]
who='GPT-6 Astra Pro; effort not exposed; run SP82_C13_148; reader B'
checks=[
dict(statement_id='148037_C03',date='2026-11-20',who=who,type='computation or formal certificate',outcome='SymPy returned discriminant(z^2−mu z+1,z)=mu^2−4 and, at mu=2, factorisation (z−1)^2. This verifies the discriminant and the stated counterexample if the disputed exponent is live.'),
dict(statement_id='148037_C03',date='2026-11-20',who=who,type='targeted proof check',outcome='Factoring mu^2−4=(mu−2)(mu+2) proves nonzero discriminant iff mu≠±2 over C. The constant term1 gives product1, so neither quadratic root is zero.'),
dict(statement_id='148037_C04',date='2026-11-20',who=who,type='computation or formal certificate',outcome='SymPy expanded (z^2−a)(z^2−b) as z^4−a z^2−b z^2+a b. Substituting a+b=mu and ab=1 gives the manuscript quartic.'),
dict(statement_id='148037_C04',date='2026-11-20',who=who,type='targeted proof check',outcome='Each nonzero a in C has exactly two distinct roots of z^2=a. If a and b are distinct, a root cannot satisfy both equations. Therefore the two distinct nonzero quadratic roots produce four distinct quartic roots.'),
dict(statement_id='148037_C05',date='2026-11-20',who=who,type='computation or formal certificate',outcome='SymPy simplified ((mu^2−4)/4) with mu=2u to u^2−1. With both inner square-root signs included, this verifies the set-valued rescaling used in the second radical expression.'),
]
hand_log=[
dict(habit='A clear detached prime is a short upright; nearby connected annotation stems may imitate additional primes.',pages=[37],holds_at_every_observed_occurrence=True,scope='holds_at_every_observed_occurrence',observed_scope='Unobscured lambda-prime and mu-prime occurrences on this leaf; the black superscript cluster after mu is excluded.',witness_effect='C’s lambda-double-prime alternative is rejected because only one stroke is detached; df-like annotation strokes belong above the equality.'),
dict(habit='The exponent4 has an angled upper stroke, a cross stroke and a descending limb, without an enclosing circle.',pages=[37],holds_at_every_observed_occurrence=True,scope='holds_at_every_observed_occurrence',observed_scope='The clear fourth-power marks in the basis relation and quartic on this page.',witness_effect='H adds a tensor sign before the basis exponent; none is visible.'),
]
notation=[
dict(form=r"\lambda'",observation='A single prime names the shifted parameter lambda−2; a df-like annotation sits above the equality.',place='second display'),
dict(form=r'e_1^4',observation='Ordinary fourth-power notation is written without a separate tensor sign.',place='basis relation'),
dict(form=r"\mu'=\tfrac12\mu",observation='The bottom-left note defines the primed parameter used in the second radical expression.',place='bottom-left margin'),
]
abbreviations=[dict(form='iso.',expansion='isomorphisme'),dict(form='i.e.',expansion='id est'),dict(form=r'néc\textsuperscript{t}',expansion='nécessairement'),dict(form='ens',expansion='ensemble'),dict(form=r'\unsure{\mathrm{df}}',expansion='définition (tentative)')]

second=[]
def sb(key,kind,xy,reading):
    second.append(dict(box='148037_'+key,kind=kind,x0=xy[0],y0=xy[1],x1=xy[2],y1=xy[3],reading=reading))
sb('folio','handwritten number',[130,51,198,111],r'\margin{36}')
sb('opening','C/H different word',[199,163,550,221],'le carré est')
sb('lambda_whole','doubtful formula',[280,234,976,390],r'\(\lambda=\frac{(\xi+\eta)^2}{\xi\wedge\eta}=\deleted{\unsure{\frac{\xi}{\eta}}}\frac{\xi}{\eta}+\frac{\eta}{\xi}+2\)')
sb('iso','C/H different word',[1158,491,1321,556],'à iso.')
sb('underlined_word','C departure below high confidence',[1335,514,1445,568],r'\uline{\unsure{un|aux}}')
sb('unique','C/H different word',[230,588,605,700],r'\uline{unique} près.')
sb('condition','C/H different word',[672,588,1405,661],r'La condition à mettre sur \(\lambda\)')
sb('lambda_minus4','handwritten number',[540,675,896,749],r'\(\lambda-4\ne0\) i.e.')
sb('lambda_prime_whole','doubtful formula',B['lambda_prime'],r"\(\lambda'\overset{\unsure{\mathrm{df}}}{=}\lambda-2=\frac{\xi}{\eta}+\frac{\eta}{\xi}\ne2\)")
sb('basis_line','deletion',[301,891,1412,996],r"En termes d'une base \deleted{\unsure{de}} \(e_1\) de \(L_1\),")
sb('basis_fourth_power','handwritten number',[672,978,1028,1110],r'\(e_1^4=e=\xi\wedge\eta\)')
sb('donnant','C/H different word',[1052,994,1412,1061],'donnant une')
sb('basis_square','handwritten number',[234,1094,714,1189],r'base \(e_1^2\) de \(L_2\)')
sb('pair_inserted','insertion',[330,1153,886,1239],r"\inserted{la paire d'éléments distincts}")
sb('pair_coordinates','handwritten number',[242,1193,1352,1292],r'par \(\xi_0,\eta_0\in\mathbb C\) \((\xi=\xi_0e_1^2,\ \eta=\eta_0e_1^2)\),')
sb('product_transition','handwritten number',[630,1295,1230,1380],r'\(\xi_0\eta_0=1\), ou encore')
sb('mu_parameter','handwritten number',[237,1355,1094,1479],r'par \(\mu=\xi_0+\eta_0\inserted{\in\mathbb C}\), satisfaisant')
sb('mu_membership','insertion',[731,1358,836,1462],r'\inserted{\(\in\mathbb C\)},')
sb('mu_nondegeneracy','handwritten number',[242,1482,1475,1573],r'\(\mu^2-4\ne0\), \(\xi_0\) et \(\eta_0\) se récupérant comme')
sb('quadratic','handwritten number',[595,1658,1053,1735],r'\(z^2-\mu z+1=0\),')
sb('distinctness_formula','doubtful formula',[516,1744,1158,1863],ineq)
sb('sexprime','C/H different word',[1146,1745,1505,1834],"s'exprime par")
sb('inserted2','insertion',[322,1836,361,1885],r'\inserted{2}')
sb('nonzero','C/H different word',[1065,1846,1489,1910],r'(néc\textsuperscript{t} non nulles')
sb('product1','handwritten number',[242,1915,1026,2012],r'car leur produit est \(1\)).')
sb('cancelled_Les','deletion',[1058,1928,1167,1981],r'\deleted{\unsure{Les}}')
sb('On_recupere','C/H different word',[1172,1926,1507,2014],'On récupère')
sb('lens_des','C/H different word',[578,2026,854,2085],"l'ens des")
sb('quartic','handwritten number',[593,2080,1006,2144],r'\(z^4-\mu z^2+1=0\)')
sb('radicals','doubtful formula',[590,2130,1514,2233],r"\(I=\left\{\pm\sqrt{\tfrac12\left(\mu\pm\sqrt{\mu^2-4}\right.}\right\}=\left\{\pm\sqrt{\mu'\pm\sqrt{\mu'^2-1}}\right\}\)")
sb('muprime_margin','margin note',B['muprime_margin'],margin)

diffrows=list(csv.DictReader((P/'differences.tsv').open(),delimiter='\t'))
rev={}
def dr(ns,status,reading,ks,note):
    for n in ns:rev[n]=dict(source_row=n,status=status,reading=reading,crops=[ref(k) for k in ks],note=note)
dr([709,710,711],'editorial_only','',['foliation'],'H’s statements about page order and the other face are editorial; no other page was read. The actual foliation36 is separately retained.')
dr([712],'C_confirmed','le carré est',['opening'],'Opening words are readable.')
dr([713,714],'C_retained_uncertainty',r'\deleted{\unsure{\frac{\xi}{\eta}}}',['top_formula'],'The crossed stacked group is included tentatively; H’s comment does not transcribe it.')
dr([715],'C_confirmed','à iso.',['iso_condition'],'Visible dotted i, s, o and point.')
dr([716],'other_reading',r'\uline{\unsure{un|aux}} \uline{unique} près.',['iso_condition'],'Short preceding word remains doubtful and underlined; unique is clear, not isomorphismes.')
dr([717],'C_confirmed','à mettre',['iso_condition'],'The wording is not imposée.')
dr([718],'C_alternative_resolved',r"\lambda'",['lambda_prime'],'One detached prime.')
dr([719],'partly_resolved',r'\overset{\unsure{\mathrm{df}}}{=}', ['lambda_prime'],'Annotation lies above equality; exact letters remain doubtful.')
dr([720],'H_confirmed',r'\ne2',['lambda_prime'],'No final point appears.')
dr([721],'editorial_only','',['lambda_prime'],'H’s retouching note is not primary text; the underlying ink is separately recorded.')
dr([722],'C_confirmed','En termes',['basis'],'No descending p of prenant.')
dr([723],'C_retained_uncertainty',r'\deleted{\unsure{de}}',['basis'],'Tentative cancelled word retained.')
dr([724],'C_confirmed',r'e_1^4',['basis'],'No separate tensor sign.')
dr([725],'C_confirmed','donnant une base',['basis'],'No extra aussi.')
dr([726,727],'C_confirmed',r"par \inserted{la paire d'éléments distincts}",['pair'],'Par is baseline; la paire is interlinear with leader.')
dr([728,729],'macro_only',r'\xi_0e_1^2,\ \eta_0e_1^2',['pair'],'TeX spacing only.')
dr([730],'C_confirmed','ou encore par',['parameter'],'No dotted i.e. or aussi word.')
dr([731],'other_reading',r'\inserted{\(\in\mathbb C\)},',['parameter'],'Membership is a raised addition with a curved leader; a separate small curved comma remains on the baseline.')
dr([732],'undecided',r'\unsure{\mu^2|\mu}\ne\pm2',['distinctness'],'Raised dark cluster may be a live or cancelled2; not decided by algebra.')
dr([733],'C_confirmed',"s'exprime par",['distinctness'],'Visible x and p strokes support exprime.')
dr([734],'other_reading',r'néc\textsuperscript{t} non nulles car',['distinctness','recover'],'Preserve raised t and the nonzero-root wording omitted by H.')
dr([735,736],'C_confirmed',"l'ens des",['recover'],'Same ascending baseline, no insertion leader and no point after ens.')
dr([737,739],'macro_only',r'\tfrac12',['roots','muprime_margin'],'Stacked1/2, no numerical difference.')
dr([738],'H_confirmed','',['roots'],'No final point visible at the edge.')
dr([740],'other_reading',margin,['muprime_margin','bleed_upper','bleed_lower'],'Retain actual marginal note and curved stroke; exclude reversed blue listing.')
reviews=[]
for row in diffrows:
    n=int(row['source_row']);d=rev[n];d['c']=row['witness C'];d['h']=row['witness H'];reviews.append(d)
result=dict(scan=37,reader='B',model='GPT-6 Astra Pro',reasoning_effort='not exposed',run='SP82_C13_148',lines_read=27,
lines_read_breakdown=dict(main_prose_baselines=17,display_baselines=5,interlinear_baselines=3,margin_baselines=1,foliation=1,method='Primary manuscript baselines only; pale reversed machine rows were inspected and excluded as show-through.'),
changes=changes,decisions=decisions,inventory=inventory,unresolved=unresolved,notes=notes,checks=checks,hand_log=hand_log,notation=notation,abbreviations=abbreviations,second_boxes=second,differences_review=reviews,
reading_procedure=dict(whole_page_views=1,native_half_views=[1,1],evidence_crop_count=14,crops=[dict(label=k,crop=ref(k),box=v,rotation=0) for k,v in B.items()],all_C_deletions_and_insertions_audited=True,all_supplied_marks_decided=True,all_supplied_difference_rows_reviewed=True,no_ocr=True,no_web=True,no_tex_compilation=True,crop_provenance='Each of14 evidence crops was made once and actually viewed. Same-pixel JPEG encodings served only for image transport; original enhanced PNGs are preserved.'))
(O/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(changes=len(changes),marks=len(decisions),inventory=len(inventory),unresolved=len(unresolved),second_boxes=len(second),differences=len(reviews),checks=len(checks))))
