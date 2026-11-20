from pathlib import Path
import csv,json,hashlib
ROOT=Path('/workspace/scratch/ddf8babdc42e')
REL=r'\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);}}'
R={}
R['B001']=r'\mspage{5}'
R['B002']=r'\uline{At 3}'
R['B003']=r'\uline{At} 4'
R['B004']=r'\uline{At} \unsure{\deleted{5}\inserted{6}|\deleted{6}\inserted{5}}'
R['B005']=r'\uline{At} \unsure{\deleted{6}\inserted{5}|\deleted{5}\inserted{6}}'
R['B006']=r'\uline{At} \deleted{\unsure{6}}\inserted{7}'
R['B007']=r'\uline{At}$_M$ 0'
R['B008']=r'\uline{A}t$_M$ 1'
R['B009']=r'\uline{At}$_M$ 2'
R['B010']=r'\uline{At}$_M$ 3'
R['B011']=r'\(1\)'
VIEWED=[f'B{i:03}' for i in range(1,12)]
OBS=[{'boxes':['B004','B005'],'observation':'Numerals 5 and 6 are superposed. Both forms are retained; the physical sequence of overwriting is not completely secure.'},{'boxes':['B006'],'observation':'The final 7 is dark and extended; its underlying heavily obliterated numeral is provisionally 6 and retained as doubtful. The open curve at the left belongs to the surrounding paragraph, outside the central numerical inscription.'},{'boxes':['B008'],'observation':'The underline is short and physically spans A, stopping before the t.'}]
R['B012']=r'\((\mathscr F,\leq)\)'
R['B013']=r'équivalent :'
R['B014']=r'\((M,\leq\,\deleted{\illegible{1}}\ (\mathrm{ordre}),\ '+REL+r'\ (\text{\unsure{rel b.|rel.}, reflex et sym}))\)'
R['B015']=r'a) \deleted{\(\forall x\in M,\) \inserted{\unsure{posant,}} \(\unsure{F_x}=\{\unsure{y}\in M\mid\unsure{y}\leq x\}\)}'
R['B016']=r'\unsure{\deleted{\inserted{posant,}}|\inserted{posant,}}'
R['B017']=r'\deleted{\(\forall x\in M,\ \unsure{F_x}=\{\unsure{y}\in M\mid\unsure{y}\leq x\}\)} Toute partie fermée \unsure{basique} \(\Phi\) de \(M\) est de type fini (i.e. \deleted{\unsure{\(\exists\)}}\unsure{\(\Phi\)} union finie \unsure{d’imm.|d’irr.} \(\widetilde{\unsure{x|X}}=M_{\leq x}\))'
R['B018']=r'\deleted{\unsure{\(\exists\)}}\unsure{\(\Phi\)}'
R['B019']=r'\margin{On aura alors \(\widetilde{\mathscr F}=\) ens des parties fermées de \(M\), de type fini, formées d’éléments deux à deux compatibles (p. r. \('+REL+r'\))}'
R['B020']=r'b) \(x'+REL+r'y,\ x^{\prime}\leq x,\ y^{\prime}\leq y\ \Longrightarrow\ x^{\prime}'+REL+r'y^{\prime}.\)'
VIEWED += [f'B{i:03}' for i in range(12,21)]
OBS += [{'boxes':['B014'],'observation':'The heavily struck group after the order sign has no fully secure word. The abbreviation after the compatibility relation appears to be rel b.; its exact superscript and stops remain doubtful.'},{'boxes':['B015','B016','B017'],'observation':'The high word is provisionally posant. A deletion stroke rises into its s; whether the insertion survives the cancellation is not securely separable. Cancelled formula letters not fully exposed remain doubtful.'},{'boxes':['B017','B018'],'observation':'The overwritten group before union finie has clear horizontal components of an existential sign, with another curled form superposed; Phi is provisional. The epithet basique and abbreviated word d’imm./d’irr. remain physically uncertain.'}]
R['B013']=r'\unsure{équivaut|équivalent} :'
R['B021']=r'\uline{At 3} Soient \(F,G\in\mathscr F\) tels que \(\forall\,\deleted{\unsure{de}}\,x\in\widetilde F,\ y\in\widetilde G\), on ait \(x'+REL+r'y\), alors \(F'+REL+r'G\) (i.e. \(F\vee G\) existe)'
R['B022']=r'\deleted{\unsure{de}}'
R['B023']=r'\margin{Critère de \uline{compatibilité} \uline{par \unsure{Atomes}}}'
R['B024']=r'\deleted{\unsure{At}}'
R['B025']=r'entre \(\leq\) et \(\ll\). \(1\)'
R['B026']=r'\uline{At} 4 \(\forall F,G\in\mathscr F,\quad F\ll G\ \Longleftrightarrow\ \forall x\in\widetilde F,\exists y\in\widetilde G,\ \text{t.q. }x\ll y\)'
R['B027']=r'\margin{Critère de \uline{raffinement} \uline{par Atomes} \([\text{\uline{Corollaire}}\ F\leq G\ \Longrightarrow\ F\ll G]\)}'
R['B028']=r'Ramène la connaissance de \(\ll\) dans \(\mathscr F\) à celle de \(\ll_M\)'
VIEWED += [f'B{i:03}' for i in range(21,29)]
OBS += [{'boxes':['B013'],'observation':'The low, compressed middle of the word before the colon does not securely distinguish équivaut from équivalent.'},{'boxes':['B022'],'observation':'A small overwritten group stands above x; de is a provisional reading, not a reconstructed word.'},{'boxes':['B023'],'observation':'The final margin word under par is compressed and crossed by the long descender of the preceding line; Atomes is retained as doubtful.'},{'boxes':['B027'],'observation':'The complete central margin inscription ends at the closing bracket after F<<G. The lower le plus petit fragment and right-edge axiom-label fragments belong to neighboring inscriptions and are not merged into this reading.'}]
R['B029']=r'\margin{\begin{tikzpicture}[baseline=(m.base),x=1em,y=1em]\node[align=left,inner sep=0,anchor=west] (m) at (0,0) {Axiome de le plus \unsure{petit|petite}\\Atome, ou du\\\uline{raffinement interne}};\draw (2,2) .. controls (2.8,2.6) and (4.2,2.7) .. (4.8,2.5);\draw (4.9,2.7)--(5.3,2.7);\draw[->] (10.2,0.9) .. controls (11.3,0.4) and (12.5,-.2) .. (13.5,-.6);\end{tikzpicture}}'
R['B030']=r'\deleted{\illegible{1}}\inserted{\(\forall\)}\(\unsure{x|X},F\in\mathscr F,\ x\triangleleft F\) (i.e. \(x\in\widetilde F\)), soit \(F^{\unsure{x|X}}=\{y\in\widetilde F\mid x\unsure{\lll|\deleted{\leq}\inserted{\ll}}y\}\). Alors \(F^{\unsure{x|X}}\) a un plus petit élément.'
R['B031']=r'\deleted{\illegible{1}}\inserted{\(\forall\)}'
R['B032']=r'\(x\unsure{\lll|\deleted{\leq}\inserted{\ll}}y\)'
R['B033']=r'Notation \(x\overset{\circ}{\ll}y\ \overset{\mathrm{df}}{\Longleftrightarrow}\ x\) est plus petit élément de \(\widetilde Y^{x}\) i.e. \(x\ll y,\ \text{et }x\ll y^{\prime}\triangleleft y\ \Longrightarrow\ y^{\prime}=y\)'
R['B034']=r'(ou \(x\in\operatorname{Omb}(y)^{\circ}\)) \(x\) \uline{raffinement interne} de \(y\)'
VIEWED += [f'B{i:03}' for i in range(29,35)]
OBS += [{'boxes':['B029'],'observation':'The central note is followed by a long arrow towards the neighboring axiom label. A separate short curved stroke and dash above the note are preserved graphically. The partial earlier Corollaire above is not merged into the central inscription.'},{'boxes':['B030','B031'],'observation':'A universal quantifier is clearly present over an older, irrecoverably crossed group. The x/X case is not securely settled by the size contrast in the first group and superscripts.'},{'boxes':['B030','B032'],'observation':'The relation contains three visible left-pointing sets of arms, with thick overlapping ink at the vertices. A literal triple-chevron and a possible overwritten <= to << remain alternatives; no mathematical repair was made.'},{'boxes':['B033'],'observation':'The visible subject before est is read x, and the superscript on the tilde-bearing Y is x. The wording is retained despite any mathematical implications.'}]
R['B035']=r'\margin{\begin{tikzpicture}[x=1em,y=1em]\node[anchor=north west,align=left,inner sep=0] at (0,0) {équivaut à :\\\inserted{\unsure{Si} \(G,H\) \illegible{1}}\\\deleted{\unsure{Axiome}} :\\\unsure{sont|deux} \unsure{égaux} d’un\\\illegible{1} \(F,G\)\\\(F\ll G\Longleftrightarrow F\leq G\)\\(Critère du \uuline{raffinement} \uline{\unsure{extrins.|extrinsèque.}} cf. \uline{figure}};\draw (-.2,.5) .. controls (3,1.2) and (8,1.3) .. (11,.7) .. controls (11.8,.5) and (12,.2) .. (12,-.4);\draw[->] (6.2,3) .. controls (5.8,2.3) and (5.8,1.5) .. (6,1);\draw (4,-3.2)--(4.5,-1.3)--(10.5,-.8);\draw (10.5,-.8)--(10.9,-.5)--(11,-.9)--(10.6,-1.1)--cycle;\end{tikzpicture}}'
R['B036']=r'\deleted{\unsure{Axiome}}\inserted{\unsure{Si} \(G,H\) \illegible{1}} :'
R['B037']=r'\deleted{\unsure{Axiome}} \unsure{sont|deux} \unsure{égaux} \inserted{\(F,G\)}'
R['B038']=r'. \uline{figure}'
VIEWED += [f'B{i:03}' for i in range(35,39)]
OBS += [{'boxes':['B035','B036','B037'],'observation':'The marginal correction is heavily superposed. The cancelled word is provisionally Axiome; Si and the lower words sont/deux and égaux are uncertain, and the unreadable groups are not reconstructed. The F,G group is legible, but its insertion scope is less secure. The terminal adjective after raffinement may be abbreviated; no expansion is asserted. The shallow over-arc, descending arrow, bent leader and terminal open rhomboid are preserved graphically. Neighboring At labels and lower Transitivité note are not merged into the central inscription.'},{'boxes':['B038'],'observation':'The central word figure is underlined, with a dot preceding it. The (ou) fragment at the upper right belongs to the neighboring main line.'}]
R['B039']=r'Si \(\unsure{x|X}'+REL+r'\unsure{y|Y}\ (\unsure{x|X},\unsure{y|Y}\in M)\) alors \(\unsure{x|X}\ll\unsure{y|Y}\ \Longrightarrow\ \unsure{x|X}\leq\unsure{y|Y}\)'
R['B040']=r'ou encore, dans un \(\widetilde F\), \(\leq\) et \(\ll\) coïncident, ou encore, si \(F,G\in M\) et \(F'+REL+r'G\), alors \(F\ll G\Longleftrightarrow F\leq G\).'
R['B041']=r'\margin{\begin{tikzpicture}[x=1em,y=1em]\node[anchor=north west,align=left,inner sep=0] at (0,0) {\uline{Transitivité}\\du raffinement\\interne};\draw[<-] (-.3,.45)--(8,.45);\draw (8,-.2) .. controls (6.6,-1) and (5.7,-2.1) .. (5.8,-3.4);\end{tikzpicture}}'
R['B042']=r'\unsure{Soient} \(x,y,z\in M\), alors \(\unsure{x|X}\overset{\circ}{\ll}\unsure{y|Y}\overset{\circ}{\ll}\unsure{z|Z}\ \Longrightarrow\ \unsure{x|X}\overset{\circ}{\ll}\unsure{z|Z}\)'
VIEWED += [f'B{i:03}' for i in range(39,43)]
OBS += [{'boxes':['B039','B042'],'observation':'The x/y/z forms in the displayed relation are larger and more angular than the nearby text. Case is not securely separable from handwriting size; uncertainty is retained without normalising the formula.'},{'boxes':['B041'],'observation':'The central note reads Transitivité du raffinement interne; only Transitivité is underlined. The long stroke with left-pointing termination above it and curved stroke at its right are retained. The partial Critère note above belongs to the previous inscription.'},{'boxes':['B042'],'observation':'The initial word is compressed and ink-heavy and remains doubtful. All three refinement relations have raised circular marks; the middle mark is filled more darkly.'}]
R['B043']=r'Traduction en termes de \((M,\leq,\ll,\widetilde{\mathscr F})\)'
R['B044']=r'\uline{At}$_M$ 0 \(\leq\ \Longrightarrow\ \ll\) \quad \uline{A}t$_M$ 1 Les \(\Phi\in\widetilde{\mathscr F}\) fermés pour \(\leq\)'
R['B045']=r'\uline{At}$_M$ 2 Si \(\Phi\in\widetilde{\mathscr F}\), \(\unsure{\Psi|\deleted{\illegible{1}}\inserted{\Psi}}\) partie fermée de \(\Phi\) pour \(\leq\), alors \(\Psi\in\widetilde{\mathscr F}\) et \(\widetilde{\mathscr F}\ne\varphi\) (i.e. \(\varphi\in\widetilde{\mathscr F}\))'
R['B046']=r'\(\unsure{\Psi|\deleted{\illegible{1}}\inserted{\Psi}}\) partie'
VIEWED += [f'B{i:03}' for i in range(43,47)]
OBS += [{'boxes':['B043'],'observation':'The central heading is complete; the At_M 0 material at its lower edge belongs to the next inscription.'},{'boxes':['B044'],'observation':'The box contains both the At_M 0 relation and At_M 1 sentence. The underline below the latter label spans A only, leaving t outside it.'},{'boxes':['B045','B046'],'observation':'The Psi before partie has an additional diagonal lower stroke and thick superposition. Psi is visible, but whether an older symbol was cancelled beneath it is uncertain. The word partie is retained; its connected horizontal pen-strokes are not confidently isolated as a separate deletion. The phi-shaped empty inscription is transcribed by its physical form, varphi.'}]
R['B047']=r'\uline{At}$_M$ 3 Si \(\Phi,\Psi\in\widetilde{\mathscr F}\), tels que \(\forall\unsure{X|x}\in\Phi,\forall\unsure{Y|y}\in\Psi,\ \deleted{\{\unsure{x|X},\unsure{y|Y}\}}\ \unsure{X|x}'+REL+r'\unsure{Y|y}\) (i.e. \(\exists\Phi\in\widetilde{\mathscr F},\ x,y\in\Phi\)), alors \(\Phi'+REL+r'\Psi\) (i.e. \(\Phi\overset{M}{\cup}\Psi\in\widetilde{\mathscr F}\)).'
R['B048']=r'\deleted{\(\{\unsure{x|X},\unsure{y|Y}\}\)}'
R['B049']=r'\(\exists\Phi\in\widetilde{\mathscr F},\ x,y\in\Phi\))'
R['B050']=r'(i.e. \(\Phi\overset{M}{\cup}\Psi\in\widetilde{\mathscr F}\)).'
R['B051']=r'\uline{At} \unsure{\deleted{5}\inserted{6}|\deleted{6}\inserted{5}}'
VIEWED += [f'B{i:03}' for i in range(47,52)]
OBS += [{'boxes':['B047','B048'],'observation':'The deleted group has visible outer curly braces and a comma. Its crossed internal forms are provisionally x,y; their exact case and letter identity remain uncertain. Large X/Y forms in the upper line are left doubtful against lowercase forms rather than regularised.'},{'boxes':['B049'],'observation':'The small high stroke above the first lower-line Phi aligns with the comma in the neighboring upper line; it is not assigned as a prime on the lower Phi.'},{'boxes':['B050'],'observation':'The union sign bears a raised M. The final closing parenthesis and full stop are visible.'},{'boxes':['B051'],'observation':'Both 5- and 6-shaped strokes remain visible in the overwritten numeral. The final stroke order is not securely separable, so both deletion/insertion directions remain open. This separately generated crop was directly viewed despite repeating another box coordinate.'}]
