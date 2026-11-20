from record_api import Page
p=Page(29)
p.r(r'\unsure{au facteur scalaire|à un facteur scalaire}','au facteur scalaire')
p.r(r"\unsure{Q:Q_{\chi'}|Q=Q_{\chi'}}",r"Q:Q_{\chi'}")
p.r(r'\unsure{pourront être infinis|pourront être infinies}','pourront être infinis')
p.r(r'\unsure{$W$|$V$}','$W$')
p.r(r'\unsure{est|étant}','étant')
p.r(r'\unsure{quand}','quand')
p.r(r'\unsure{croissant}','croissant')
p.r(r'\unsure{non}}',r'non}')
start=p.text.index(r'\deleted{\uline{Exemple}')
end=p.text.index(r'\uline{Ex} Prenons')
p.text=p.text[:start]+r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=west] (a) at (0,3.8) {\deleted{\uline{Exemple} Prenons $\varphi$ non dég.}};
\node[anchor=west,align=left] at (.3,2) {$\begin{array}{l}
\varphi:\bigwedge^2V\longrightarrow k\qquad\text{non dégénérée}\\
\text{i.e. }\varphi\in\bigwedge^2\check V\\
\deleted{\unsure{\text{d'où }\check\varphi\in\bigwedge^2V}}\\
\chi=\varphi^2\in\bigwedge^4\check V\qquad\chi:\bigwedge^4V\longrightarrow k
\end{array}$};
\draw (0,3.4)--(0,.7);
\node[anchor=west] (b) at (0,0) {\deleted{Alors $\chi$ comme forme sur $\bigwedge^2V$ est non}};
\draw (a.east) .. controls +(0.4,0) and +(0,1) .. (8,1.2) .. controls (8,.8) and (10,.9) .. (10,.5)--(10.2,.15);
\end{tikzpicture}}

'''+p.text[end:]
p.ch('Cancelled opening','Exemple Prenons φ non dég.','Exemple Prenons pour ill dég. ill','Exemple Prenons φ non dég.','scan 029 (255,80,1240,425): φ has its characteristic descending stem; no pour or further word after dég.',kind=r'readable ink left as \ill{}',error=5,marked='yes')
p.ch('Cancelled d’où formula',r"unsure d'où checkφ∈wedge²V",r'checkφ∈wedge²checkV ill',r"unsure d'où checkφ∈wedge²V",'scan 029 (255,80,1240,425): d’ and the check over φ remain; the end is heavily struck. No secure check over terminal V.',confidence='low',kind='misread symbol or index',error=1,marked='yes')
p.ch('Cancelled Alors line','Alors χ comme forme sur wedge²V est unsure non','Alors χ ill forme ill sur wedge²V ill','Alors χ comme forme sur wedge²V est non','scan 029 (255,80,1240,425): comme, sur, est and final non remain above/below the thin strike.',confidence='medium',kind=r'readable ink left as \ill{}',error=5,marked='yes')
p.ch('Connector between cancelled lines','detached curved stroke','omitted','curved stroke beside opening display, joining vicinity of cancelled lines','scan 029 (255,80,1240,425): long bent line descends from the first strike and turns toward the last line.','CH',kind='drawing or diagram',error=4)
p.ch('Cancelled phrase after non dégénérée',r'\deleted{\unsure{comme isom.}}',r'\struck{\ill{}}',r'\deleted{\unsure{comme isom.}}','scan 029 (1050,430,1370,515): dotted i and isom. ending survive; first word partly covered.',confidence='medium',kind=r'readable ink left as \ill{}',error=5,marked='yes')
p.ch('Choice of ξ','Alors un choix convenable de ξ ... donne','Alors on choisit un ξ ... donné','Alors un choix convenable de ξ ... donne','page: un choix convenable de is written in full; the verb ends in e.')
for n in (1,2):p.ch(f'Scalar phrase {n}','unsure au facteur scalaire / à un facteur scalaire','à un facteur scalaire','au facteur scalaire','scan 029 (765,600,1330,735): short joined au before facteur; no separate un.',confidence='medium')
p.ch('Inserted membership of checkφ','checkφ inserted ∈wedge²V','checkφ∈wedge²checkV','checkφ inserted ∈wedge²V','page: the check belongs to φ; the V in the raised insertion is plain.',kind='misread symbol or index',error=1,marked='yes')
p.ch('First square in tensor-algebra discussion','checkφ²','checkφ','checkφ²','page: small 2 stands at upper right of the checked φ before comme élément.',kind='misread symbol or index',error=1)
p.ch('Cancelled tensor expression',r'\deleted{wedge²V unsure⊗}',r'\struck{wedge²checkV}',r'\deleted{wedge²V unsure⊗}','scan 029 (725,795,880,875): plain V followed by a crossed circular sign; no check on V.',confidence='medium',kind='misread symbol or index',error=1)
p.ch('Exterior-algebra tensor factors','wedge*V⊗wedge*V (twice)','checkΛV⊗checkΛV (twice)','wedge*V⊗wedge*V (twice)','page: raised star-like marks stand on the wedges, and each V is plain.',kind='misread symbol or index',error=1)
p.ch('Bidegree-two tensor','wedge²V⊗wedge²V','wedge²checkV⊗wedge²checkV','wedge²V⊗wedge²V','page: both superscript digits are on wedges; neither V has a check.',kind='misread symbol or index',error=1)
p.ch('Parenthetic insertion','(quand ∈wedge²V) after le carré ... dans wedge*V','(qui ∈wedge⁴checkV) before subset','(quand ∈wedge²V) after le carré ... dans wedge*V','page: quand ∈wedge²V is raised over est l’image, with a curved insertion leader.',kind='insertion or placement',error=6)
p.ch('Square and image sentence','le carré de checkφ dans wedge*V ... est l’image de checkφ^(2) précédent par','le carré ... de wedge²V (à l’image ... prise par)','le carré de checkφ dans wedge*V ... est l’image de checkφ^(2) précédent par','page: dans, est, précédent are live; star on the first wedge.')
p.ch('Map to wedge⁴V','wedge²V⊗wedge²V→wedge⁴V','wedge²V⊗checkΛV→wedge⁴V','wedge²V⊗wedge²V→wedge⁴V','page: the second factor carries a small raised 2, with plain V.',kind='misread symbol or index',error=1)
p.ch('Q punctuation',r"unsure Q:Q_{χ′}/Q=Q_{χ′}",r'Q=Q_{χ′}',r'Q:Q_{χ′}','scan 029 (440,1200,665,1305): two short vertically separated dots, not two horizontal equality bars.',kind='misread symbol or index',error=1)
p.ch('Orbit verb','unsure pourront être infinis/infinies','peuvent deleted jamais être infinis','pourront être infinis','scan 029 (290,1385,1690,1665): pourront is live, followed by être infinis; no cancelled jamais there.',kind='misread word',error=2,marked='yes')
p.ch('Even-dimension parenthesis','unsure W/V unsure est/étant de dim paire','W ill de dim paire','W étant de dim paire','scan 029 (290,1385,1690,1665): large double-valley W; compressed étant immediately afterward.',confidence='medium',kind=r'readable ink left as \ill{}',error=5,marked='yes')
p.ch('Final inserted description and dimension','deleted unsure de; inserted unsure linéairement engendrées et pleines; de dim non bornée (quand dim V croissant...)','deleted ill; plusieurs ill de dim non bornés (qui dès V ill)','deleted unsure de; inserted unsure linéairement engendrées et pleines; de dim non bornée (quand dim V croissant...)','scan 029 (290,1385,1690,1665): long insertion leader places words before de dim; final parenthesis reads quand dim V croissant; central insertion remains doubtful.',confidence='low',kind='insertion or placement',error=6,marked='yes')
p.ch('Last cancelled symbol',r'\deleted{unsure ξ}','omitted',r'\deleted{unsure ξ}','scan 029 (345,1640,435,1745): dense crossed symbol below the final insertion; its curved upper stroke permits ξ but does not settle it.',confidence='low',kind='omission',error=3)
p.d('M0288','first','au facteur scalaire','joined short au','scan 029 (765,600,1330,735)','medium')
p.d('M0289','first','au facteur scalaire','same small joined prefix as preceding occurrence','scan 029 (765,600,1330,735)','medium')
p.d('M0290','first',r"Q:Q_{\chi'}",'two vertically aligned dots','scan 029 (440,1200,665,1305)')
p.d('M0291','first','pourront être infinis','pourront and infinis visible across the last lines','scan 029 (290,1385,1690,1665)')
p.d('M0292','first','$W$','double valley of capital W','scan 029 (290,1385,1690,1665)')
p.d('M0293','alternative','étant','tall t and joined ending','scan 029 (290,1385,1690,1665)','medium')
p.d('M0294','undecided',r'\unsure{linéairement engendrées et pleines}','crowded inserted words with several letters merged into the leader','scan 029 (290,1385,1690,1665)','low')
p.d('M0295','first','quand','q with descender and joined ending','scan 029 (290,1385,1690,1665)','medium')
p.d('M0296','first','croissant','croiss- and terminal rising strokes','scan 029 (290,1385,1690,1665)','medium')
p.inv(('deletion','top','Exemple Prenons φ non dég.'),('display','upper left','φ:wedge²V→k; i.e. φ∈wedge²checkV; χ=φ²'),('deletion','inside display','d’où checkφ∈wedge²V'),('drawing','around upper display','left rule and bent right connector'),('deletion','below display','Alors χ comme forme ... est non'),('text','middle heading','Ex Prenons χ′ non dégénérée'),('deletion','same line','comme isom.'),('text','middle','Alors un choix convenable de ξ'),('insertion','after checkφ','∈wedge²V'),('text','middle','Considérons alors checkφ²'),('deletion','before l’algèbre','wedge²V tensor sign'),('text','middle bracket','[en écrivant wedge²V⊂V⊗V]'),('text','middle lower','et checkφ² comme élément...; le carré'),('insertion','above est l’image','(quand ∈wedge²V)'),('display','inline middle lower','wedge²V⊗wedge²V→wedge⁴V'),('text','lower','Utilisant la forme Q:Qχ′'),('text','lower','Je dis que l’orbite sous u'),('deletion','near final insertion','de'),('insertion','last lines','linéairement engendrées et pleines'),('deletion','below final line','ξ'),('text','bottom left','28','hand not attributed, pencil'))
p.p['notes']='Pencil folio 28. The opening example and concluding Alors sentence are cancelled, while the intervening definitions remain live; a bent connector accompanies the cancellation. The live example sets α=id and tilde W=wedge²V. It discusses choosing ξ, forming powers of checkφ in exterior tensor algebras, and obtaining an endomorphism u through the form Q attached to χ′. The ink writes “Q:Qχ′” with a colon. Stars on wedge algebras and checks on φ or V were distinguished occurrence by occurrence; H frequently moves these decorations to the wrong object. The final assertion about an orbit includes “dim V≥4 (ou 6?)” and “W étant de dim paire”; both the explicit question and W are preserved. The inserted phrase tentatively read “linéairement engendrées et pleines” remains the least secure part. No proof of the orbit assertion or normalization of the two square constructions was performed. The contraction underlying the tensor-to-endomorphism sentence can be written explicitly as a⊗b ↦ [v↦Q(b,v)a] on E=wedge²V; distributivity of Q makes that expression bilinear in a,b, so it defines the stated linear map E⊗E→End(E). This local construction supplies the map only, without certifying the later orbit claim.'
p.p['checks']=[['029.tensor_contraction','2026-11-20','GPT-6 Astra Pro, current run','targeted proof check','Wrote a⊗b↦(v↦Q(b,v)a); bilinearity in a,b and linearity in v establish the linear tensor-to-endomorphism map. No orbit claim checked.']]
p.p['doubts']=[['cancelled d’où formula',r"\deleted{\unsure{d'où checkφ∈wedge²V}}",'end under heavy strike','low'],['cancelled isom. phrase',r'\deleted{\unsure{comme isom.}}','first word partly covered','medium'],['cancelled tensor sign',r'\deleted{wedge²V\unsure{⊗}}','round sign crossed by strike','medium'],['final insertion',r'\unsure{linéairement engendrées et pleines}','several merged letters and uncertain endings','low'],['cancelled de',r'\deleted{\unsure{de}}','insertion leader crosses word','low'],['final symbol',r'\deleted{\unsure{ξ}}','multiple cancellation strokes','low']]
p.p['certainty']=[['M0288–M0292, M0295–M0296','First readings confirmed; uncertainty removed.'],['M0293','étant selected from the listed alternatives.'],['cancelled non','Word recovered under thin strike.']]
p.p['notation']=[['checkφ² / checkφ^(2)','small 2 versus parenthesized raised 2','029','both forms preserved'],['wedge*V','small raised star on wedge, plain V','029','exterior-algebra tensor discussion'],['Q:Qχ′','two dots, first above the second','029','local colon retained']]
p.p['hand']=[['Stars and checks belong to different letters in crowded exterior-algebra notation','029','each occurrence examined','H repeatedly attaches a check to V where the wedge has a star or 2'],['Long insertion leaders cross adjacent words','029','final inserted phrase','H loses placement and much of the phrase']]
p.p['abbreviations']=[['Ex','Exemple'],['non dég.','non dégénérée'],['endom','endomorphisme']]
p.save()
