from record import save_page
save_page(114,5,r'''\scanpage{5}
\mspage{1}
% archive foliation: 4
\diagram{\begin{tikzcd}
\widehat A & M\arrow[l,"i^*"'] & M'\arrow[l,"f"']\\
& M_{\mathrm{as}} & M'_{\mathrm{as}}
\end{tikzcd}}
\figure{\begin{tikzpicture}\draw (0,0)--(5,0)--(5,1.5);\end{tikzpicture}}

\diagram{\begin{tikzcd}
A\arrow[r,"i"]\arrow[dr,dashed] & \underline M\\
& M_{\mathrm{as}}\arrow[u,hook]
\end{tikzcd}}
: $M_{\mathrm{as}}.$ asphériques $\overset{?}{\Longrightarrow}$
$i^*$ conservatif et fidèle

\uline{NB} Si $A\xrightarrow f B$ asphérique, alors
$f^*: \widehat B\longrightarrow\widehat A$ conservatif et fidèle
\inserted{i.e. $f$ dominant}
i.e. le cocrible engendré par $f(\unsure{\operatorname{Ob}A})$ est $B$.

\deleted{En effet}, les propriétés d'exactitude de $f^*$ impliquent que
\[
f^*\text{ conservatif}\Longleftrightarrow f^*\text{ fidèle}
\deleted{\unsure{\Longleftrightarrow}}\Longleftrightarrow
\deleted{\unsure{f^*}}\unsure{[}
\]
\deleted{Supposons $\unsure{b}\to b'$ tel que $f^*(b)\longrightarrow f^*(b')$ iso.}
\[
[f^*(x)=\varnothing_{\widehat A}\Longrightarrow x=\varnothing_{\widehat B}]
\]
\deleted{\unsure{donc} $A_{/f^*(b)}$.}
\[
\unsure{A_{/i^*(x)}}\ \longleftrightarrow
\]
\[
\operatorname{Hom}_A(a,f^*(x))
\]
\[
\overset{\unsure{''}}{\operatorname{Hom}}_B(f(a),x)
\]

Mais $f^*(x)=\varnothing_{\widehat A}\Longleftrightarrow
\operatorname{Hom}_{\widehat B}(\deleted{\unsure{b}}b,\unsure{x|a})
=\varnothing$ pour $\forall b\in f(\operatorname{Ob}(A))$,

\margin{i.e. pour $\forall b\in\operatorname{Ob}B$ $\exists a\in A$ et
$f(a)\longrightarrow b$ i.e. $A_{/b}\ne\varnothing$ OK}

\margin{Mais il faut \unsure{une} \unsure{petit.} hypothèse sur $\underline W$!}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,5.5) .. controls (1,5.4) and (3,5.2) .. (4,5.2);
\draw (3,5.2) .. controls (1.7,5.2) and (1,4.9) .. (1,3.7)
 .. controls (1,2.2) and (1.4,1.4) .. (0,0);
\end{tikzpicture}}

\deleted{Il faut en déduire que
$\operatorname{Hom}(b,x)=\varnothing\quad\forall b\in B$}

\deleted{Plus général on \unsure{remplace}}

Pour conclure que $i^*$ est fidèle, \inserted{ou conservatif,}
il faut savoir que $M\longrightarrow\widehat{M_{\mathrm{as}}}$ l'est,
i.e. que $M_{\mathrm{as}}$ est \uline{générateur}.

Peut-on avoir $M_{\mathrm{as}}=\varnothing$ \unsure{?}
il faudrait alors que $A=\varnothing$, donc $\widehat A=\{e\}$,
donc $\widehat A_{\mathrm{as}}=\varnothing$, \uline{OK}.

Contr'exemple! Peut-on avoir $M_{\mathrm{as}}=\{a\}$

\deleted{Alors} \unsure{DPS} $A=\{a\}$,
\deleted{$\widehat A\simeq(\operatorname{Ens}),\quad
\widehat A_{\mathrm{as}}=\text{un unique \unsure{terme}},$}
\deleted{$M_{\mathrm{as}}=\{x\in\operatorname{Ob}M\mid
\operatorname{Hom}(a,x)\text{ de cardinal }1\}$}
\unsure{donc}

\deleted{\unsure{Plus général}}
\margin{\unsure{(*)}}
''',[
('diagram','top boxed','Ahat <- M <- M prime; Mas, Mprime_as'),
('drawing','top box','bottom and right border'),
('diagram','upper left','A -> M, dashed A -> Mas, Mas inclusion M'),
('text','upper question','Mas. asphériques ?=> i* conservatif et fidèle'),
('text','NB','Si A -> B asphérique'),
('insertion','NB right','i.e. f dominant'),
('text','NB next line','i.e. le cocrible engendré par f(Ob A) est B'),
('deletion','lemma beginning','En effet'),
('text','lemma','les propriétés d’exactitude de f* impliquent que'),
('display','lemma equivalences','f* conservatif iff f* fidèle iff'),
('deletion','equivalence line','iff; f*'),
('deletion','middle','Supposons b -> b prime tel que f*(b) -> f*(b prime) iso'),
('display','bracket','f*(x)=empty_Ahat => x=empty_Bhat'),
('deletion','below bracket','donc A/f*(b)'),
('display','middle left','A/i*(x) leftrightarrow'),
('display','middle left Hom 1','Hom_A(a,f*(x))'),
('display','middle left Hom 2','Hom_B(f(a),x), ditto mark'),
('text','middle right','Mais f*(x)=empty iff Hom_Bhat(b,x)=empty'),
('deletion','right Hom argument','b overwritten'),
('margin note','left slanting upper','i.e. pour all b in Ob B exists a in A'),
('margin note','left slanting lower','Mais il faut une petit. hypothèse sur W!'),
('drawing','left boundary','curved separating strokes'),
('deletion','lower middle 1','Il faut en déduire que Hom(b,x)=empty all b in B'),
('deletion','lower middle 2','Plus général on remplace'),
('text','lower argument','Pour conclure que i* est fidèle'),
('insertion','lower argument above right','ou conservatif'),
('text','bottom case 1','Peut-on avoir Mas=empty?'),
('text','bottom case 2','Contr’exemple! Peut-on avoir Mas={a}'),
('deletion','bottom beginning','Alors'),
('text','bottom','DPS A={a}'),
('deletion','bottom displayed continuation','Ahat = Ens; Ahat_as = un unique terme'),
('deletion','bottom last formula','Mas={x in Ob M | Hom(a,x) de cardinal 1}'),
('text','bottom right','donc'),
('deletion','bottom last line','Plus général'),
('margin note','bottom left','(*)')],doubts=[
('upper question','Mas. asphériques','Final plural ending and punctuation are compressed.','medium'),
('NB last line','f(Ob A)','Ob A heavily overwritten.','low'),
('equivalence ending','deleted f*; [','Several overwritten strokes; continuation to bracket is not explicit.','low'),
('cancelled trial','Supposons b -> b prime; donc A/f*(b)','Letter b overwritten, terminal subscript dense.','low'),
('central loose formula','A/i*(x) leftrightarrow','Index and unfinished arrow both uncertain.','low'),
('central Hom comparison','ditto above Hom_B','Two short vertical strokes may be a comparison sign.','low'),
('right Mais formula','Hom_Bhat(b,x)','Second argument may read a; first is overwritten.','low'),
('left margin','une petit. hypothèse','First two words are compressed/abbreviated.','medium'),
('lower cancellation','Plus général on remplace','Last word uncertain.','low'),
('bottom','DPS; un unique terme; donc','Abbreviation and last overwritten lines are particularly uncertain.','low')],notes='Initial question: asphericity of i into Mas implies i* conservative and faithful? NB asserts aspherical functor gives conservative faithful inverse image, reduces via exactness to reflection of initial object, and sketches dominance/nonempty comma categories. Margin explicitly requires a small hypothesis on W. Lower argument says faithfulness/conservativity needs Mas generating; then tests empty and singleton Mas, announces Contr’exemple!, and cancels a proposed formula. Do not report this as a completed proof or a clean counterexample. Own author pagination 1. Need link question/corrections to following scan 006 without changing readings.')
