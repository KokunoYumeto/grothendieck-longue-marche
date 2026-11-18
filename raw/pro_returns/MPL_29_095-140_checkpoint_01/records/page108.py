from save_page import save_page

save_page(108, r'''
\scanpage{108}
% archive foliation: 107
% Pale reversed typescript is mirror-image show-through from the other face.
\[
P=QQ'\qquad QR+Q'R'=1
\]
\margin{$(P)=(Q)(Q')=(Q)\cap(Q')$\par
car $s\in(Q)$, $s\in(Q')$\par
$\Longrightarrow s=Q'sR'+QsR\in(QQ')$}
\[
A[t]/(P)\longrightarrow A[t]/(Q)\times A[t]/(Q')
\]
injectif car $(\unsure{P})=(Q)\cap(Q')$

Surjectif car par Nakayama on est ramené au cas

$A[t]$

\uline{Lemme.} Soient $Q,Q'\subset A$ \uline{\unsure{id\textsuperscript{x}} étrangers}.

Alors $A/(QQ')\longrightarrow A/Q\times A/Q'$ est un \unsure{isom}.

En effet,\quad (i)\quad $(Q)\cap(Q')=QQ'$

car
\[
\underline Q\cap\underline {Q'}=(\underline Q\cap\underline {Q'})(\underline Q+\underline {Q'})
\subset\underline {Q'}\underline Q+QQ'=QQ'.
\]
(ii) $\underline Q+\underline {Q'}=A$, \unsure{par hypothèse}; \unsure{il s'ensuit} que
\[
x\in A,\ y\in A\quad\Longrightarrow\quad
\begin{gathered}
\exists\unsure{b}\in Q\quad\text{qui est }\equiv y\quad(Q')\\
\exists a\in Q'\quad\text{qui est }\equiv x\quad(Q).
\end{gathered}
\]
donc
\[
a+b\equiv\begin{cases}x&(Q)\\y&(Q')\end{cases}
\]
\figure{\begin{tikzpicture}\draw[very thick] (0,0) .. controls (1.8,-0.09) and (3.0,-0.04) .. (4.8,0.01);\draw (0.05,-0.07)--(4.68,-0.02);\end{tikzpicture}}

\diagram{\begin{tikzcd}[column sep=small,row sep=small]
A/(Q.Q')\longrightarrow A/Q\unsure{\times|+}A/Q' & \text{surjectif }\deleted{\unsure{ssi}} \arrow[d,Leftrightarrow] & \\
& \text{bijectif} \arrow[d,Leftrightarrow] & \\
& Q+Q'=A \arrow[r,Rightarrow] & QQ'=Q\cap Q'
\end{tikzcd}}
''', [
('display','top left and centre','P=QQ′; QR+Q′R′=1'),
('margin note','top right','(P)=(Q)(Q′)=(Q)∩(Q′); s∈(Q),s∈(Q′)'),
('display','upper left','A[t]/(P)→A[t]/(Q)×A[t]/(Q′)'),
('text','upper explanation','injectif car (P)=(Q)∩(Q′)'),
('text','upper middle','Surjectif car par Nakayama on est ramené au cas'),
('display','isolated below upper explanation','A[t]'),
('text','middle lemma','Lemme. Soient Q,Q′⊂A idˣ étrangers'),
('text','lemma conclusion','Alors A/(QQ′)→A/Q×A/Q′ est un isom'),
('text','proof (i)','En effet, (i) (Q)∩(Q′)=QQ′'),
('display','proof (i) expansion','Q∩Q′=(Q∩Q′)(Q+Q′)⊂Q′Q+QQ′=QQ′'),
('text','proof (ii)','Q+Q′=A, par hypothèse'),
('display','proof existence','x∈A,y∈A⇒∃b∈Q … ∃a∈Q′'),
('display','proof congruences','a+b≡{x (Q), y (Q′)}'),
('drawing','above final diagram','double horizontal separator'),
('diagram','bottom','surjectif ⇔ bijectif ⇔ Q+Q′=A ⇒ QQ′=Q∩Q′'),
('deletion','bottom after surjectif','ssi'),
], [
('lemma hypothesis','idˣ étrangers','abbreviation for ideals uncertain; not expanded in transcription','medium'),
('lemma conclusion','isom','end of word compressed, probably abbreviation','medium'),
('proof (ii) transition','par hypothèse; il s’ensuit','heavily compressed handwriting','low'),
('proof first existential element','b','overwritten with an earlier loop; b is best reading','medium'),
('final map product symbol','×','could be a plus; literal alternative retained','medium'),
('pale typescript beneath manuscript','mirror-image reverse-side show-through','orientation checked by rotation; not a second text written on this face','high'),
], [
'Chinese remainder calculation for P=QQ′ with QR+Q′R′=1; the short first surjectivity argument invokes Nakayama but breaks off at “ramené au cas” and isolated A[t]. A separate lemma supplies an elementary ideal-theoretic proof below.',
'Final diagram asserts equivalence of surjectivity, bijectivity, and Q+Q′=A for the displayed quotient map, and the implication to QQ′=Q∩Q′; check independently if this equivalence is used later.',
])
