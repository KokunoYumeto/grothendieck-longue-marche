from record_api import Page
p=Page(25)
p.r("\\begin{flushright}\\fbox{Algèbres de Hodge d'ordre 2}\\end{flushright}",r'''\begin{flushright}\begin{tikzpicture}
\node[anchor=west] at (0,0) {Algèbres de Hodge d'ordre 2};
\draw (-.15,.45)--(-.15,-.35)--(7,-.35);
\end{tikzpicture}\end{flushright}''')
p.r(r'\unsure{appl.}',r'appl.')
p.r(r'\unsure{Q|\bar Q}',r'\bar Q')
p.r(r'\unsure{isom.}',r'isom.')
p.r("\\unsure{\\rho'|\\rho^1|\\rho}",r'\rho')
p.r("\\unsure{\\langle x,y'\\rangle|+\\langle x,y'\\rangle|\\deleted{+}\\langle x,y'\\rangle|\\deleted{-}\\langle x,y'\\rangle}","\\deleted{\\unsure{+|-}}\\langle x,y'\\rangle")
p.r(r'\deleted{\unsure{i=4}}',r'\deleted{i=4}')
p.r(r'\deleted{\unsure{x\xi^2=0}}',r'\deleted{x\xi^2=0}')
p.r(r'H^2\times H^i\longrightarrow H^{i+2}',r'H^2\times H^i\longrightarrow H^{j+2}')
p.r(r'\left|\quad i=2:',r'\left|\quad j=2:')
p.r(r'\unsure{Quels que soient les choix|Quelle que soit la donnée}',r'Quels que soient les choix')
p.r(r'\unsure{sss|ssi}',r'sss')
p.r(r'\unsure{itou|idem}',r'itou')
p.ch('Title enclosure','complete frame','no frame','left and bottom strokes','page: the left vertical turns into a bottom rule; no closing top or right stroke in the scan.','CH',kind='drawing or diagram',error=4)
p.ch('Below graded table','V,W','omitted','V,W','page: isolated V,W written below the table.',kind='omission',error=3)
p.ch('Definitions before φ','no avec','avec','no avec','page: the marginal definitions start directly with φ.',kind='text not on the page',error=9)
p.ch('Q definition','forme bil. sym.','forme bilinéaire symétrique','forme bil. sym.','page: both words stop after their abbreviated stems.',kind='abbreviation expanded or spelling modernised',error=8)
p.ch('Cancelled opening',r'\deleted{\unsure{Point de vue}}',r'\struck{\ill{}}',r'\deleted{\unsure{Point de vue}}','scan 025 (160,515,910,705): Point de v... survives the long horizontal cancellation; the final letters remain damaged.',confidence='medium',kind=r'readable ink left as \ill{}',error=5,marked='yes')
p.ch('Reconstruction data',r'\unsure{Q|\bar Q}','Q',r'\bar Q','scan 025 (160,515,910,705): a short separate horizontal stroke stands directly above Q.','CH',kind='misread symbol or index',error=1)
p.ch('Before isom.','no à',r'\add{à}','no à','scan 025 (160,515,910,705): the next line begins isom.; no insertion à is visible.',kind='text not on the page',error=9)
p.ch('Degree-zero product','clair par',r'clair, \struck{pour}','clair par','page: the small linking word is live par, with no cancellation through it.',kind='deletion state (struck given live or live given struck)',error=7)
p.ch('Degree-zero rule end',r'\forall x','omitted',r'\forall x','page: quantifier and x stand after the final equality.',kind='omission',error=3)
p.ch('ρ notation',"\\unsure{\\rho'|\\rho^1|\\rho}",r'\rho',r'\rho','scan 025 (785,850,1540,1045): the tall stroke after ρ descends from the φ in the line above; no separate prime is established.','C',confidence='medium',kind='misread symbol or index',error=1)
p.ch('Cancelled callout before y maps to φ',r'\deleted{\unsure{(*)}}','omitted',r'\deleted{\unsure{(*)}}','scan 025 (785,850,1540,1045): a hatched parenthesized callout remains before the map.',confidence='low',kind='omission',error=3)
p.ch('Sign before pairing',r'\unsure{pairing|+pairing|deleted + pairing|deleted - pairing}',r'\struck{\ill{}} pairing',"\\deleted{\\unsure{+|-}}\\langle x,y'\\rangle",'scan 025 (785,850,1540,1045): the angle bracket is clear; immediately before it a small sign has been blacked out.','C',confidence='low',kind='deletion state (struck given live or live given struck)',error=7)
p.ch('Cancelled last product',r'\deleted{\unsure{x\xi^2=0}}',r'\struck{\ill{}}',r'\deleted{x\xi^2=0}','scan 025 (785,850,1540,1045): x, ξ with superscript 2, equality and terminal 0 remain through the diagonal strikes.',kind=r'readable ink left as \ill{}',error=5,marked='yes')
p.ch('Degree-two multiplication indices',r'H^2×H^i→H^{i+2}, i=2',r'H^2×H^j→H^{j+2}, j=2',r'H^2×H^i→H^{j+2}, j=2','scan 025 (145,1120,680,1230): first superscript is a short dotted i; output exponent and case label have the descending hook of j.','CH',confidence='medium',kind='misread symbol or index',error=1,consequence='Mixed i/j indices retained in the degree-two multiplication line.')
p.ch('Footnote enclosure','curved enclosing rule','omitted','curved enclosing rule','page: a long bent rule connects and encloses the (*) definition.',kind='drawing or diagram',error=4)
p.ch('Before composition law','de φ,ψ, on trouve',r'de φ,ψ,Q, \ill{} \struck{donnent}','de φ,ψ, on trouve','page: φ and ψ are the two named symbols; the following words on trouve are live.',kind='misread word',error=2,marked='yes')
p.ch('Associativity callout and box',r'\deleted{\unsure{(*)}} and box','omitted callout and box',r'\deleted{\unsure{(*)}} and box','scan 025 (455,1590,550,1695): dense hatching covers the small callout; page: an enclosing frame surrounds the equation.',confidence='low',kind='drawing or diagram',error=4)
p.ch('Associativity margin','alternée en y,z (donc en unsure toutes/tous les var.!)',r'alternée \ill{} y^2 \ill{} \struck{\ill{}}','alternée en y,z (donc en unsure toutes/tous les var.!)','scan 025 (20,1600,445,1885): comma between y,z; donc en begins the parenthesis; crowded final words remain doubtful.',confidence='medium',kind=r'readable ink left as \ill{}',error=5,marked='yes')
p.ch('Nondegeneracy conclusion frames','φ and Q conclusions boxed','no frames','φ and Q conclusions boxed','page: both conclusions have hand-drawn enclosing rules.',kind='drawing or diagram',error=4)
p.ch('Poincaré middle line',r'\unsure{itou|idem}','idem','itou','page: the tall crossed t and final rounded u read itou.',kind='misread word',error=2)
p.d('M0271','first','appl.','abbreviated a-p-p-l with terminal point')
p.d('M0272','alternative',r'\bar Q','separate overbar above Q','scan 025 (160,515,910,705)')
p.d('M0273','first','isom.','i-s-o-m abbreviation at line start','scan 025 (160,515,910,705)')
p.d('M0274','alternative',r'\rho','apparent high stroke belongs to φ above','scan 025 (785,850,1540,1045)','medium')
p.d('M0275','undecided',"\\deleted{\\unsure{+|-}}\\langle x,y'\\rangle",'small cancelled sign; angle bracket itself clear','scan 025 (785,850,1540,1045)','low')
p.d('M0276','first','Quels que soient les choix','plural quels, soient, choix are separately visible')
p.d('M0277','undecided',r'\unsure{toutes les var.!|tous les var.!}','final words crossed by the enclosure and crowded into the margin','scan 025 (20,1600,445,1885)','low')
p.d('M0278','first','sss','three similar s strokes; no dotted i')
p.d('M0279','first','itou','t with upright and crossstroke, final u')
p.d('M0280','first','sss','three s forms')
p.inv(('text','top right','Algèbres de Hodge d’ordre 2'),('drawing','title','left and bottom enclosing rule'),('diagram','top','H⁰ H¹ H² H³ H⁴ / k V kξ+W checkV kξ²'),('text','below table','V,W'),('display','upper left','wedge² V → kξ+W; α'),('display','upper left second','Sym²(W) → kξ²; β'),('margin note','upper right','φ forme alternée; ψ; Q'),('deletion','before reconstruction','Point de vue'),('text','upper middle','La connaissance de V,W,φ,ψ,Qbar'),('display','middle','H⁰×H^i; unit law'),('display','middle','H¹×H^i; four cases'),('deletion','first case','donc/dont'),('deletion','second case','(*)'),('deletion','third case','sign before pairing'),('deletion','fourth case','i=4; xξ²=0'),('display','middle lower','H²×H^i→H^{j+2}; j=2'),('text','enclosed note','(*) On pose tildeφ'),('drawing','enclosed note','curved connecting rule'),('text','below note','Quels que soient les choix'),('text','lower middle','Condition d’associativité'),('display','lower middle','boxed associativity identity'),('deletion','left of box','hatched callout'),('margin note','left of box','exprime aussi que la forme'),('text','lower','Condition de Lefschetz'),('display','lower','ξ²:H⁰≃H⁴'),('display','lower','ξ:H¹→H³; boxed φ non dégénérée'),('text','bottom','Condition de Poincaré'),('display','bottom','three conditions; boxed Q non dégénérée'),('text','bottom left','24','hand not attributed, pencil'))
p.p['notes']='The heading is “Algèbres de Hodge d’ordre 2”; pencil folio 24. The page gives H⁰=k, H¹=V, H²=kξ+W, H³=check V, H⁴=kξ², the products, an associativity identity and the stated Lefschetz/Poincaré conditions. The reconstruction sentence names Q with an overbar, although the bilinear-form notation elsewhere is Q. The degree-two multiplication line writes H^i at the source and j+2, j=2 afterward; these visible letters are retained. The high stroke beside ρ belongs to the φ above, so the crop supports plain ρ. The sign cancelled before the pairing remains unreadable as + versus −. Direct expansion of the displayed degree-two rules gives (aξ+w)(bξ+w′)=(ab+Q(w,w′))ξ²: the two mixed terms vanish by the displayed ξw=wξ=0. Substituting a=φ(x,y), b=φ(t,z), w=ψ(x,y), w′=ψ(t,z) produces the left side of the boxed formula. This checks that local expansion only; the page’s universal associativity and nondegeneracy assertions have not been independently proved in this run.'
p.p['checks']=[['025.degree_two_product','2026-11-20','GPT-6 Astra Pro, current run','computation or formal certificate','Expanded four terms using the displayed table; mixed terms zero, ξξ=ξ² and ww′=Q(w,w′)ξ².'],['025.associativity_expansion','2026-11-20','GPT-6 Astra Pro, current run','used and rechecked in this run','Substituted the α products into the checked degree-two product; recovered the boxed left-hand expression.']]
p.p['doubts']=[['cancelled opening',r'\deleted{\unsure{Point de vue}}','last letters under strike','medium'],['first product case',r'\deleted{\unsure{donc|dont}}','terminal letter covered','low'],['cancelled callouts',r'\deleted{\unsure{(*)}}','hatching prevents full recovery','low'],['sign before pairing',r'\deleted{\unsure{+|-}}','original sign obscured','low'],['margin end',r'\unsure{toutes les var.!|tous les var.!}','crowded ending and enclosure cross the text','low']]
p.p['certainty']=[['M0271, M0273, M0276, M0278–M0280','First readings confirmed; certainty only.'],['cancelled i=4 and xξ²=0','Readable through strikes; retained wording.']]
p.p['notation']=[['ξ','looped upper stroke and descending tail','025','all products on this page'],['ρ / tildeφ','ρ on second line overlaps descending stem of φ above','025','local crowded display'],['sss','three s strokes','025','both nondegeneracy equivalences']]
p.p['hand']=[['Long descenders can intrude into the next formula line; φ stem lies beside ρ','025','local overlap','C offered prime/1 on ρ'],['A short i and a hooked j occur in one index line','025','local retained letter change','C regularised j to i; H regularised first i to j']]
p.p['abbreviations']=[['appl.','application'],['bil. alt.','bilinéaire alternée'],['bil. sym.','bilinéaire symétrique'],['isom.','isomorphisme'],['tjrs','toujours'],['sss','si et seulement si'],['non dég.','non dégénérée'],['var.','variables']]
p.save()
