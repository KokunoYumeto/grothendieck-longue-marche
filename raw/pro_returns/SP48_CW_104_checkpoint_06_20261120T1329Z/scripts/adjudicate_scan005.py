"""Apply the main reader's once-only scan 005 crop decisions to reader A's text.

No image reading or mathematical normalization is performed by this script.
The authoritative decision observations are records/scan005/main_observations.md.
"""
from pathlib import Path

O = Path(__file__).resolve().parents[1]
s = (O / 'records/scan005/reader_A/reading.tex').read_text()

def rep(old, new):
    global s
    if old not in s:
        raise ValueError('Absent patch anchor: ' + old[:140])
    s = s.replace(old, new, 1)

start = s.index('\\diagram{')
end = s.index('\n\\[', start)
s = s[:start] + r'''\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=.7em]
{\mathbb Z[\mathbb F_{\unsure{n-2|n\,2|n-1}}]}
\& {\begin{tikzpicture}[baseline=-.15em,x=.45em,y=.45em,line width=.45pt]
\draw (.7,.7)..controls(-.1,.45)and(-.15,-.1)..(.55,-.5);
\draw (.45,.05)--(1.65,.05);
\end{tikzpicture}}
\& {\mathbb Z[\mathbb F_{n-1}]}
\& {\mathbb Z[F_n]}\arrow[l,"{t_n-s_n}"]
\& {\mathbb Z[\mathbb F_{n+1}]}\arrow[l]
\& {\begin{tikzpicture}[baseline=-.3ex,x=.5em,y=.5em,line width=.8pt]
\draw (0,.15)--(.65,.15);
\draw (.43,.55)--(.43,-.3)--(.7,-.3);
\draw (0,0)--(0,.3);
\end{tikzpicture}}
\end{tikzcd}}
% The first connector has an open curved head separated from its shaft.
% The middle left-arrow label is below the shaft, as in C's equivalent syntax.
% The terminal cross-like trace has no securely assigned lexical/algebraic value.
\figure{\begin{tikzpicture}[x=1em,y=1em,line width=.4pt,line cap=round]
\draw (0,.35)..controls(.04,.08)and(.2,-.05)..(.3,-.12);
\draw (.35,-.16)--(.4,-.18);
\draw (.48,-.21)--(.6,-.23);
\draw (1.1,.06)--(1.2,.13);
\draw (1.28,.2)--(1.48,.32);
\end{tikzpicture}}
% Detached curved traces below the chain; uncertain function, no word assigned.
''' + s[end:]

rep(r'\unsure{E_3|\xi}', r'\unsure{E_7|E_3|\xi}')
rep(r'\node at ([xshift=5.5em,yshift=-2em]eq.west) {$0$};',
    r'''\node at ([xshift=5.5em,yshift=-2em]eq.west) {$0$};
\draw ([xshift=3.3em,yshift=-.75em]eq.west)
 --([xshift=3.46em,yshift=-.82em]eq.west);
\draw ([xshift=3.42em,yshift=-.83em]eq.west)
 --([xshift=3.58em,yshift=-.98em]eq.west);''')
rep(r'\underset{\smile}{F}_0 & \unsure{F|\mathbb F}_1',
    r'\underset{\smile}{F}_0 & F_1')
rep(r'\unsure{\prime|1}&', r'\unsure{1|\prime}&')

rep(r"\(\bigl(C_i\bigr)\quad\forall w'\in\mathbb F'_i,\)",
    r'''\(\bigl(\begin{tikzpicture}[baseline=-.55ex,x=1em,y=1em]
\node[inner sep=0pt] at (0,0) {$C_i$};
\fill (-.5,.65) circle (.025);
\fill (-.35,.57) circle (.025);
\end{tikzpicture}\bigr)\quad\forall w'\in\mathbb F'_i,\)''')
rep(r'u_{\unsure{i-1|i}}=s_i(w)', r'u_{\unsure{i|i-1}}=s_i(w)')
rep(r"\(f(u_{\unsure{i|1}})=u'_i\)",
    r"\(f(u_{\unsure{\cdot|i|1}})=u'_{\unsure{i|1}}\)")
rep(r"\(f(v_i)=v'_i\)", r"\(\unsure{g|f}(v_i)=v'_i\)")
rep(r'\(s(u)=s(v),\ t(u)=t(v)\)',
    r'\(s(u)=s(v),\ t(u)\unsure{\equiv|=}t(v)\)')
rep(r"(NB on n'exige pas que \(\unsure{f|g}(u)=u'\))",
    r"(NB on n'exige pas que \(g(u)=u'\))")
rep(r'\end{flushright}', r'''\end{flushright}
% The two points above-left of C are literal detached ink, not an assigned accent.
% The later v/v' subscripts retain the i/1 doubt first marked on u'.
% The NB function shares the g/f uncertainty of the preceding equality;
% its use of g is the first candidate, not a separate resolution of that form.''')
rep(r'\unsure{\mathrm a)|\mathrm b)}', r'\unsure{\mathrm b)|\mathrm a)}')
rep(r"\forall \text{\uline{\(s\)}}'\in F'_0", r"\forall s'\in F'_0")
rep(r'\deleted{\pi_0(f)\ \text{surj}}',
    r'\deleted{\pi_0(f)\ \unsure{\text{surj}}}')
if s.count(r'\rotatebox{90}') != 6:
    raise ValueError('Expected six vertical membership signs')
s = s.replace(r'\rotatebox{90}', r'\rotatebox{-90}')
rep(r"f(u)\xrightarrow[\sim]{\ell}u'", r'''f(u)\mathrel{\begin{tikzpicture}[baseline=-.4ex,x=.35em,y=.35em,line width=.45pt]
\draw[->] (0,0)--(4,0);
\draw (0,0)..controls(.7,1.0)and(1.6,1.0)..(2,.45)
 ..controls(2.5,-.25)and(3.4,.2)..(4,0);
\node at (2,1.8) {$\ell$};
\end{tikzpicture}}u' ''')
rep(r'\unsure{w|\exists\,w}\in F_2', r'\unsure{w|\exists\,w|u}\in F_2')
rep('% The wavy stroke in the preceding arrow is drawn across its shaft in the source.',
    '% The wavy stroke is traced across the shaft. Xi_1 follows the first candidate\n'
    '% of the Xi/E uncertainty marked at the preceding level; E_2 below has a clear stem.')
rep(r'\deleted{\forall s,t\in\unsure{\mathbb F_0|F_0},}',
    r'\deleted{\forall s,t\in\mathbb F_0,}')
rep(r'\begin{gathered}s_1(u)=s_1(v)\\[-.2em] t_1(u)=t_1(v)\end{gathered}',
    r'\begin{gathered}s_1(u)=s_1(v)\\[-.2em] t_1(u)\mathbin{-}t_1(v)\end{gathered}')
rep(r' \deleted{et}\ \text{tel que}', r''' \mathord{\begin{tikzpicture}[baseline=(oldet.base),line width=.4pt]
\node[inner sep=0pt] (oldet) {\(\deleted{\text{et}}\)};
\draw ([xshift=-.15em,yshift=-.2em]oldet.south west)
 --([xshift=.05em,yshift=-.2em]oldet.south east);
\draw ([xshift=-.2em,yshift=.1em]oldet.north east)
 --([xshift=-.2em,yshift=-.22em]oldet.south east);
\end{tikzpicture}}\ \text{tel que}''')
rep(r'\node at (10.4,-1.05) {surj};', r'\node at (6.3,-1.05) {surj};')
rep(r'\draw (.78,-.62)--(1,-.65)--(.83,-.85);',
    r'\draw (1,-.65)--(.83,-.85);')
rep(r'\node at (.1,1.35) {$f(u)$};',
    r'\node at (.1,1.35) {$\unsure{fu)|f(u)}$};')

(O / 'pages/H104-01_104_scan005.tex').write_text(s)
print('Wrote pages/H104-01_104_scan005.tex from the recorded main decisions.')
