from pathlib import Path
import json,csv,re
out=Path(__file__).parent
packet=Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan031')
C=(packet/'C.tex').read_text();H=(packet/'H.tex').read_text();T=(out/'candidate.tex').read_text()
boxes=json.loads((out/'crop_boxes.json').read_text())
F=json.loads((out/'figure_readings.json').read_text())
J=json.loads((out/'reading_journal.json').read_text())
margin=(out/'margin_reading.txt').read_text()
# All source quotations are exact strings of the supplied witnesses.
def between(s,a,b):
 i=s.index(a);j=s.index(b,i)+len(b);return s[i:j]
def hbetween(a,b):return between(H,a,b)
def cbetween(a,b):return between(C,a,b)
def evidence(key):return J['observations'][key]
def crop(key):return 'crops/148_scan031_'+key+'.png'
R=dict(scan=31,reader='C',lines_read=0,changes=[],decisions=[],inventory=[],unresolved=[],notes=[],checks=[],hand_log=[],notation=[],abbreviations=[],second_boxes=[],differences_review=[])
def exact_quote(q,src,place):
 if not q or q in src:return q
 idx=[i for i,ch in enumerate(src) if not ch.isspace()]
 norm=''.join(src[i] for i in idx);nq=''.join(q.split())
 at=norm.find(nq)
 assert at>=0,('witness quotation',place,q)
 return src[idx[at]:idx[at+len(nq)-1]+1]
def change(place,c,h,final,key,ink=None,confidence='high',kind='misread symbol or index',ac=True,ah=False,math=True):
 c=exact_quote(c,C,place);h=exact_quote(h,H,place)
 R['changes'].append(dict(place=place,c=c,h=h,final=final,ink=ink or evidence(key),crop=crop(key),box=boxes[key],confidence=confidence,kind=kind,against_c=ac,against_h=ah,math=math))
def unresolved(place,reading,issue,alts,confidence='low'):
 R['unresolved'].append(dict(place=place,reading=reading,issue=issue,alternatives=alts,confidence=confidence))
S={
'i10_text':r'''\mathrm I_{10}\ (\text{pentagonale})\\12\ \text{structures pentagonales sur }K\\\{\sigma,\sigma^{-1}\}\in P_2(\mathrm{Circ}(K)\\G\simeq\mathbb D_5\\\widetilde G\simeq\mathbb D_5\times\{1,\sigma\}''',
'i6_text':r'''20\ \text{structures }K=J\amalg\omega\\\text{avec }\omega\xrightarrow{\sim}\underline\omega(J)\\G\simeq\unsure{\mathfrak S|G}_J\simeq\unsure{\mathfrak S|G}_3\\\widetilde G\simeq\unsure{\mathfrak S|G}_3\times\{1,\sigma\}''',
'i4_text':r'''30\ \text{structures carrés orientés}\\K\simeq\{P\}\amalg I\\I\ \text{structure carrée \uline{orientée}}\ (Q,\omega)=\vec Q\\I=\coprod_{\alpha\in\delta}\alpha\qquad\delta=\text{ens. des diagonales }\alpha\\\omega\in\delta\wedge\bigwedge_{\alpha\in\delta}\alpha\\G=\widetilde G=\mathbb Z/4\mathbb Z''',
'ii2_text':r'''60\ \text{structures ``pentagone avec sommet'' sur }K\\\text{i.e. }K\simeq B\amalg\omega,\ \text{avec }\omega\hookrightarrow J\\\text{i.e. }P\in J\text{ et }\omega\simeq\omega'=B\setminus\{P\}\\G\simeq\mathbb Z/2\mathbb Z\\\widetilde G\simeq\mathbb Z/2\mathbb Z\times\{1,\sigma\}''',
'ii2prime_text':r'''\text{même paramétrage que }\mathrm{II}_2\\G\simeq\mathbb Z/2\mathbb Z,\ \widetilde G\simeq\mathbb Z/2\mathbb Z\times\{1,\sigma\}''',
'ii1_text':r'''120\ \text{structures entièrement épinglées,}\\G=\deleted{\unsure{1}}=\{1\},\quad\widetilde G=\{1,\sigma\}''',
'ii1_parameters':r'''\left[\begin{gathered}K=J\amalg\varepsilon\quad\operatorname{card}J=3,\operatorname{card}\varepsilon=2\\\omega\in\underline\omega(J),\ r\in J\times\varepsilon\\\tau_r^0:\mathrm{II}_1(J,\varepsilon)\longrightarrow\mathrm{II}_1(u_\omega(r))\\\text{où }u_\omega=\omega\times(-1)\text{ sur }J\times\varepsilon\end{gathered}\right]''',
'iii2_text':r'''60\ \text{structures ``pentagone avec sommet'' sur }K,\\G=\mathbb Z/2\mathbb Z,\widetilde G=\mathbb Z/2\mathbb Z\times\{1,\sigma\}''',
'iii1_heading':r'\mathrm{III}_1\ (\text{triple triangle sem.-gauche})',
'iii1_text':r'''120\ \text{structures épinglées}\\G=1,\widetilde G=\{1,\sigma\}''',
'iii2prime_heading':r"\mathrm{III}'_2\ (\text{triple triangle gauche})",
'iii2prime_text':r'''60\ \text{structures de carré orienté à codiagonales, }K=\{P\}\amalg I,\\I\ \text{muni d’une \inserted{str.} carré en codiagonales }\delta=\{\{\alpha,\beta\},\{\alpha',\beta'\}\}\\\text{i.e. d’un repère de }\unsure{\mathfrak X|\mathbb J}\unsure{(}I)\\G=\mathbb Z/2\mathbb Z\unsure{\deleted{*}},\quad\widetilde G\simeq\mathbb Z/2\mathbb Z\times\mathbb Z/2\mathbb Z\simeq\mathbb Z/2\mathbb Z\times\{1,\sigma\}''',
'levels_totals':r'''\begin{array}{lll}\uline{\text{niveau }2}&\mathrm I_{10},\mathrm I_6,\mathrm I_4&12+20+30=62\\\uline{\text{niveau }}1&\mathrm{II}_2,\mathrm{II}'_2,\mathrm{II}_1&60+60+120=240\\\uline{\text{niveau }}0&\mathrm{III}_2,\mathrm{III}_{\unsure{1|4}},\mathrm{III}'_2&60+120+60=240\\&&\overline{542}\end{array}''',
'indice_nb':r'''(l’``indice'' indique l’ordre de \(G=\operatorname{Aut}^{+}\)\unsure{;|,} donc le nb de structures est \(120/i\))\\\uline{NB} Sauf \(\mathrm I_4\), toutes ces structures sont ``réelles''. ''',
'parameter_key':r'''\begin{array}{ll}\pi\in\mathrm{Pent}(K),&B\in\mathrm{Bit\acute et}(K)\\s\in K,&\vec Q\in\overrightarrow{\mathrm{Carr}}(K)\\\rho\in\mathrm{Rep}(\pi);&r\in\mathrm{Rep}(K)\end{array}\\(\uline{NB}\ \{(\pi,\rho)\}\unsure{\simeq}\mathrm{Rep}(K)).''',
'folio':r'\margin{30}',
'arrow_fbs':r'''\arrow[r,"{3\quad f_{B,s}\quad2}","{(B\in\unsure{\mathrm{Bit\acute et}|\mathrm{Bitet}}(K),\ s\in T(B)=J)}"']''',
'arrow_fq':r'''\arrow[dl,bend right=10,"{4\quad f_{\vec Q,\omega,a}\quad2}","{(Q=\overrightarrow{\mathrm{Carr}}(K),\ a\in\Lambda(Q))}"']''',
'arrow_gamma_pi_s':r'''\arrow[u,"{1\quad\gamma_{\pi,s}\quad5}","{(\pi\in\mathrm{Pent}(K),\ s\in K)}"']''',
'arrow_tau_pi_s':r'''\text{2 sommets-repères}\quad\deleted{\text{\unsure{repères}}}\\\arrow[r,"{1\quad\tau_{\pi,s}=\mathrm{tw}_{1/4}\quad1}"]''',
'arrows_upper_middle':r'''\arrow[u,"{\gamma'_{\pi,s}\quad3}","{\text{comp. avec }\unsure{\vec Q|\vec G};\ (\pi\in\mathrm{Pent}(K),\ s\in K)}"']\\\arrow[ul,"{1\quad\gamma_r^0\quad6}","{\text{compat. avec }\unsure{\vec Q|\vec G}}"']''',
'arrow_gamma_pi_rho':r'''\arrow[u,"{2\quad\gamma_{\pi,\rho}\quad2}","{(\pi\in\mathrm{Pent}(K),\rho\in\mathrm{Rep}\,\pi)}"']\quad\begin{tikzpicture}\draw (0,.15)..controls(-.12,.23)and(-.16,.3)..(-.14,.37);\end{tikzpicture}''',
'arrow_tau_pi_rho':r'''\arrow[r,"{\unsure{\tau_{\pi,\omega}}}","{2\quad\tau_{\pi,\rho}=\mathrm{tw}_{1/4}\quad1}"']''',
'arrows_gamma_r1':r'''\arrow[u,"{1\quad\gamma_r^1\quad2}"]\quad\arrow[ur,"{3\qquad3}","{(r\in\mathrm{Rep}(K))}"',"{\begin{tikzpicture}\draw (0,0) ellipse (.55 and .32);\node at(-.04,.07){$\gamma_r^{1'}$};\node at(.3,-.13){$!$};\end{tikzpicture}}"{description}]''',
'loop_tau_r0':r'\arrow[loop right,"{\tau_r^0=\mathrm{tw}_{1/6}}"]',
'arrow_tau_rprime':r'''\arrow[r,"{1\quad\tau'_r\quad2}"]''',
'arc_gamma_r2':r'''\arrow[ull,bend left=65,"{2\quad\gamma_r^2\quad2}"']''',
'arc_gamma_r2prime':r'''\arrow[uu,bend right=70,"{1\quad\gamma_r^{2'}\quad2}"]''',
'top_isolated_mark':r'\begin{tikzpicture}\draw (.12,.32)--(.1,.08)..controls(.09,.01)and(.02,.01)..(0,.05);\end{tikzpicture}',
'iii2_count':r'2+2\ \text{sommets-repère}',
'iii1_count':r'2+4\ \text{sommets-repère}',
'iii2prime_count':r'4+4\ \text{sommets-repère}',
'ii1_count':r'6\ \text{sommets-repères}',
'ii2prime_count':r'4\ \text{sommets}\ \deleted{\text{\unsure{repères}}}',
'margin_graph1':r'\begin{tikzpicture}\fill(0,0)circle(2pt);\draw(0,0)--(-.5,.85);\draw(0,0)--(-.22,.98);\draw(0,0)--(.04,1.01);\draw(0,0)--(.26,1.05);\draw(0,0)--(.47,1.08);\end{tikzpicture}',
'margin_graph2':r'\begin{tikzpicture}\draw(0,0)--(.85,0);\fill(0,0)circle(2pt);\fill(.85,0)circle(2pt);\draw(0,0)--(-.17,.7);\draw(0,0)--(.1,.75);\draw(0,0)--(.32,.74);\draw(.85,0)--(.72,.78);\draw(.85,0)--(1.03,.86);\end{tikzpicture}',
'margin_graph3':r'\begin{tikzpicture}\draw(0,0)--(.55,.03)--(1,.06);\foreach\x/\y in{0/0,.55/.03,1/.06}{\fill(\x,\y)circle(2pt);}\draw(0,0)--(-.06,.9);\draw(0,0)--(.1,.9);\draw(.55,.03)--(.5,.85);\draw(1,.06)--(.86,.89);\draw(1,.06)--(1.15,.87);\end{tikzpicture}',
'margin_arrow1':r'\begin{tikzpicture}\draw[thick](.52,5.35)--(1.04,5.38)..controls(1.4,5.42)..(1.68,5.42);\draw[thick](1.68,5.42)..controls(1.34,5.29)..(1.04,5.38);\end{tikzpicture}',
'margin_arrow2':r'\begin{tikzpicture}\draw[thick](.52,2.32)..controls(1.15,2.37)..(1.65,2.4);\draw[thick](.52,2.32)..controls(1.15,2.3)..(1.65,2.28);\draw[thick](.52,2.32)..controls(1.15,2.2)..(1.7,2.17);\end{tikzpicture}',
'margin_bracket_base':r'\begin{tikzpicture}\draw[gray](.52,7.3)..controls(.44,4.7)and(.55,1.5)..(.57,-.32);\draw[gray](.6,-.47)..controls(1.12,-.45)and(1.52,-.52)..(1.72,-.51)--(1.73,-.55);\end{tikzpicture}',
'listing_bleed':''
}
fig_keys=['figure_i10','figure_i6','figure_i4','figure_ii2','figure_ii2prime_canceled','figure_ii2prime_live','figure_ii1','figure_iii2','figure_iii1_a','figure_iii1_b','figure_iii2prime_a','figure_iii2prime_b']
for n,k in enumerate(fig_keys,180):S[k]=F[str(n)]
# Text readings, including every resolved C mark.
change('I10 P2',r'\unsure{\mathbb P}',r'\ill{}',r'P','i10_text',ink='The capital has a straight stem and a closed angular upper bowl; no second stem establishes a blackboard-bold P.',kind=r'readable ink left as \ill{}',ah=True)
change('I10 Circ',r'\unsure{\mathrm{Circ}}',r'\mathrm{Circ}',r'\mathrm{Circ}','i10_text',ink='C, i, r, c are separately legible in the notation following the first opening parenthesis.',ac=True)
change('I10 unmatched parenthesis',r'\{\sigma,\sigma^{-1}\}\in\unsure{\mathbb P}_2(\unsure{\mathrm{Circ}}(K))',r'$(\mathrm{Circ}(K))$',r'\{\sigma,\sigma^{-1}\}\in P_2(\mathrm{Circ}(K)','i10_text',ink='Two opening curved strokes occur before Circ and K, but only one closing curved stroke follows K.',kind='text not on the page',ah=True)
change('I4 top masculine plural',r'\text{30 structures carrés orientés}',r'30 structures carrées orientées',r'30\ \text{structures carrés orientés}','i4_text',ink='The upper line ends each adjective in accented e followed directly by s, without an intervening e.',kind='misread word',ac=False,ah=True,math=False)
change('I4 lower feminine singular',r'I\ \text{structure carré \uline{orienté}}',r'$I$ structure carrée \emph{orientée}',r'I\ \text{structure carrée \uline{orientée}}','i4_text',ink='A small terminal e follows each accented e in the lower line. Only orientée has the underline.',kind='misread word',math=False)
change('I4 omega delta',r'\unsure{\delta|J}',r'\omega \in J \wedge',r'\omega\in\delta\wedge\bigwedge_{\alpha\in\delta}\alpha','i4_text',ink='The disputed letter has the same closed lower loop and rising stem as the delta written immediately above.',ah=True)
change('I4 group equality',r'G=\widetilde G=\mathbb Z/4\mathbb Z',hbetween(r'G = \widetilde{G} \simeq',r'\mathbf{Z}/4\mathbf{Z}'),r'G=\widetilde G=\mathbb Z/4\mathbb Z','i4_text',ink='The relation before the quotient consists of two straight horizontal strokes, without a tilde.',ac=False,ah=True)
change('II2 first B',r'K\simeq \unsure{J|B}\amalg\omega',r'K \simeq B \amalg \omega',r'K\simeq B\amalg\omega','ii2_text',ink='A straight upright and two right-facing bowls identify B, unlike the hooked J to its right.')
change('II2 second B',r"\omega'=\unsure{J|B}\setminus\{P\}",hbetween(r"\omega' = B",r'\setminus \lbrace P \rbrace'),r"\omega'=B\setminus\{P\}",'ii2_text',ink='The second B again has two closed or nearly closed right-facing bowls.')
change('II2 omega relation',r'\omega\xrightarrow{\sim}\omega',r"\omega \simeq \omega'",r"\omega\simeq\omega'",'ii2_text',ink='Only a horizontal stroke with a tilde is present between the omegas; the right end has no arrowhead.')
change('II2 pentagone phrase and quotation marks',r"\text{60 structures ``pentagone}\\\text{avec sommet'' sur }K",r'60 structures « \uncertain{pentagone avec sommet} » sur $K$',r"60\ \text{structures ``pentagone avec sommet'' sur }K",'ii2_text',ink='Pentagone avec sommet is legible, including the final t; the quotation marks are paired short strokes, not guillemets.',kind='misread word',ac=False,ah=True,math=False)
change('II2 count and live repères',r'\text{2 sommets-repères}\quad\deleted{\text{\unsure{repères}}}',hbetween(r'\note{au-dessus : « 2 sommets-repère »',r'biffé}'),r'\text{2 sommets-repères}\quad\deleted{\text{\unsure{repères}}}','arrow_tau_pi_s',ink='The live word on the line under sommets ends in s; the crossing strokes belong to a separate lower word, not to that live repères.',kind='deletion state',ac=False,ah=True,math=False)
change('II2prime paramétrage',r'\text{mêmes paramètres que }\mathrm{II}_2',r"même paramétrage que $\mathrm{II}_2$",r'\text{même paramétrage que }\mathrm{II}_2','ii2prime_text',ink='Même has no final s; the following word has the descending loop of g before its final e.',kind='misread word',math=False)
change('II1 entièrement',r'\unsure{entièrement|anticanoniques}',r'\uncertain{anticanoniques}',r'entièrement','ii1_text',ink='The sequence e-n-t-i-è-r-e-m-e-n-t is visible, including the acute/sloping accent and the final t.',kind='misread word',ah=True,math=False)
for idx,(c,h,f) in enumerate([
 (r'K=J\amalg\varepsilon',r'K = J \amalg E',r'K=J\amalg\varepsilon'),
 (r'\operatorname{card}\varepsilon=2',r'\mathrm{card}\, E = 2',r'\operatorname{card}\varepsilon=2'),
 (r'r\in J\times\varepsilon',r'r \in J \times E',r'r\in J\times\varepsilon'),
 (r'\mathrm{II}_1(J,\varepsilon)',r'\mathrm{II}_1(J, E)',r'\mathrm{II}_1(J,\varepsilon)'),
 (r'\text{ sur }J\times\varepsilon',r'\text{ sur } J \times E',r'\text{ sur }J\times\varepsilon')],1):
 change('II1 epsilon '+str(idx),c,h,f,'ii1_parameters',ink='The letter is a curly epsilon with rounded lobes, matching the same five occurrences in this parameter block; it is not an upright three-bar E.',ac=False,ah=True)
change('II1 omega closing parenthesis',r'\omega\in\underline\omega(J))',r'\omega \in \underline{\omega}(J)',r'\omega\in\underline\omega(J)','ii1_parameters',ink='There is one curved closing stroke after J, followed by the comma; C duplicates that parenthesis.',kind='text not on the page')
change('II1 minus before one',r'\omega\times(-1)',hbetween(r'\omega'+'\n'+r'\times (1)',r'\times (1)'),r'\omega\times(-1)','ii1_parameters',ink='A short straight horizontal minus stands inside the parentheses immediately before the upright 1.',ac=False,ah=True)
change('III2 group equality',r'\widetilde G\simeq\mathbb Z/2\mathbb Z\times\{1,\sigma\}',hbetween(r'\widetilde{G} = \mathbf{Z}/2\mathbf{Z}',r'\times \lbrace 1, \sigma \rbrace'),r'\widetilde G=\mathbb Z/2\mathbb Z\times\{1,\sigma\}','iii2_text',ink='The two horizontal strokes before the quotient are straight; there is no wavy upper stroke.')
change('III2 quotation marks',r"\text{60 structures ``pentagone avec}\\\text{sommet'' sur }K,",r'structures « \uncertain{pentagone avec sommet} » sur $K$',r"60\ \text{structures ``pentagone avec sommet'' sur }K,",'iii2_text',ink='The phrase is legible and enclosed by paired short straight quotation strokes.',kind='misread word',ac=False,ah=True,math=False)
change('III1 heading index',r'\mathrm{III}_1\ (\text{triple triangle sem.-gauche})',r"$\mathrm{III}'_{1}$ (triple triangle semi-gauche)",r'\mathrm{III}_1\ (\text{triple triangle sem.-gauche})','iii1_heading',ink='There is no detached prime beside the three vertical I strokes; the lower digit is 1.',ac=False,ah=True)
change('III1 sem abbreviation',r'sem.-gauche',r'semi-gauche',r'sem.-gauche','iii1_heading',ink='The handwritten sem is followed by a dot and a short hyphen; no i follows m.',kind='abbreviation expanded or spelling modernised',ac=False,ah=True,math=False)
change('III2prime codiagonales plural',r'\text{codiagonales, }K=',r'codiagonale, $K =',r'\text{codiagonales, }K=','iii2prime_text',ink='A terminal s follows the final e before the comma.',kind='misread word',ac=False,ah=True,math=False)
change('III2prime lower carré en codiagonales',r'\inserted{str.} carré en codiagonales',r'\add{str.}\ \uncertain{carrée} à codiagonale',r'\inserted{str.} carré en codiagonales','iii2prime_text',ink='Carré ends at the accented e; en has two distinct letters; codiagonales has a terminal s. Str. is above the line.',kind='misread word',ac=False,ah=True,math=False)
change('III2prime right parenthesis scope',r'\unsure{\mathfrak X}(I)',r'$\mathbb{J}(I)$) ;',r'\unsure{\mathfrak X|\mathbb J}\unsure{(}I)','iii2prime_text',ink='One closing parenthesis is visible after I. A second closing parenthesis supplied by H is not present; the opening parenthesis remains inseparable from the X-like glyph.',confidence='medium',kind='text not on the page',ac=False,ah=True)
change('level1 underline scope',r'\uline{\text{niveau }1}',r'\text{niveau 1}',r'\uline{\text{niveau }}1','levels_totals',ink='The underline ends below the word niveau before the separate final digit 1.',kind='insertion or placement',ah=True,math=False)
change('level0 underline scope',r'\uline{\text{niveau }0}',r'\text{niveau 0}',r'\uline{\text{niveau }}0','levels_totals',ink='The underline is beneath niveau; the digit 0 is to its right beyond the underline.',kind='insertion or placement',ah=True,math=False)
change('total 542 overbar',r'\underline{542}',r'\overline{542}',r'\overline{542}','levels_totals',ink='The long horizontal stroke is above the digits 542, separating them from the preceding line.')
change('total word absent','',r'\text{total }',r'','levels_totals',ink='There are no letters before 542 on its line; only the bar and the three digits occur.',kind='text not on the page',ac=False,ah=True,math=False)
change('indice quotation marks',r"l’``indice''",r"l'« indice »",r"l’``indice''",'indice_nb',ink='The word indice is enclosed by paired short quotation strokes, not angle-shaped guillemets.',kind='other',ac=False,ah=True,math=False)
change('réelles quotation marks',r"``réelles''",r'« réelles »',r"``réelles''",'indice_nb',ink='Paired short marks open and close réelles; no guillemet chevrons are drawn.',kind='other',ac=False,ah=True,math=False)
change('parameter key Pent',r'\unsure{\mathrm{Pent}|\mathrm{Pand}}',r'\pi \in \mathrm{Pand}(K)',r'\pi\in\mathrm{Pent}(K)','parameter_key',ink='The middle letters have the loop of e then the two-stroke n, ending in t; there is no a-d sequence.',ah=True)
# Arrows and their labels.
change('fQ omega and a',r'f_{\vec Q,\unsure{\omega},a}',r'f_{\vec{Q},\alpha}',r'f_{\vec Q,\omega,a}','arrow_fq',ink='A two-lobed omega occurs between commas after Q; the final a is Latin a, not alpha.',ah=True)
change('fQ Lambda condition',r'a\in\unsure{\Lambda}(Q)',hbetween(r'$\alpha \in',r'\Lambda(Q)$'),r'a\in\Lambda(Q)','arrow_fq',ink='The capital Lambda has two sloping legs without a crossbar; the preceding letter is the same Latin a as the subscript.',ah=True)
change('fQ direction',cbetween(r'\arrow[dl,bend right=10',r'\ a\in\unsure{\Lambda}(Q))}"\']') if False else re.search(r'\\arrow\[dl,bend right=10.*?\]',C).group(0),hbetween(r'\item $f_{\vec{Q},\alpha}',r'(degré 4) ;'),S['arrow_fq'],'arrow_fq',ink='The upper endpoint near I4 has 4 and no head; the lower-left endpoint near II2prime has a left/down arrowhead and 2.',kind='drawing or diagram',ac=False,ah=True)
change('gamma pi s Pent',r'(\pi\in\mathrm{Pent}(K),\ s\in K)',r'\pi \in \mathrm{Pand}(K)',r'(\pi\in\mathrm{Pent}(K),\ s\in K)','arrow_gamma_pi_s',ink='The parameter name has e-n-t, agreeing with the lower key.',ac=False,ah=True)
change('upper gamma pi s prime',r"\unsure{\gamma^1_{\pi,s}|\gamma'_{\pi,s}}",r"\gamma'_{\pi,s}",r"\gamma'_{\pi,s}",'arrows_upper_middle',ink='The raised detached stroke has no hooked top or basal foot, unlike the nearby written numerical 1. Root confirmed this comparison on the saved crop and with an independently read notation occurrence; reader C initially left it open.',confidence='medium')
change('upper gamma degree placement',r"\unsure{\gamma^1_{\pi,s}|\gamma'_{\pi,s}}\quad3",r"\gamma'_{\pi,s}$ : $3 \to 6$",r"\gamma'_{\pi,s}\quad3",'arrows_upper_middle',ink='The 3 sits at the head of the vertical arrow. The nearby 6 belongs to the crossing diagonal gamma_r^0, and is not a degree on this vertical arrow.',kind='insertion or placement',ac=False,ah=True)
change('upper gamma comp abbreviation',r'\text{comp. avec }',r'compat.\ avec',r'\text{comp. avec }','arrows_upper_middle',ink='The upper annotation is comp. with the dot immediately after p; the longer compat. is written only on the lower diagonal.',kind='abbreviation expanded or spelling modernised',ac=False,ah=True,math=False)
change('upper gamma Pent',r'(\pi\in\mathrm{Pent}(K),\ s\in K)',r'\pi \in \mathrm{Pand}(K)',r'(\pi\in\mathrm{Pent}(K),\ s\in K)','arrows_upper_middle',ink='The upper condition also spells Pent with e and terminal t.',ac=False,ah=True)
change('gamma r0 target and exponent',re.search(r'\\arrow\[ul,pos=\.73.*?\]',C).group(0),hbetween(r'\item $\gamma^{0}_{r}',r"vers $\mathrm{II}'_2$ ;"),r'''\mathrm{II}_1\xrightarrow{1\quad\gamma_r^0\quad6}\mathrm I_6''','arrows_upper_middle',ink='The diagonal runs upward-left from II1 into I6, ending beside 6. Its raised 0 is a closed loop, unlike the detached prime stroke.',kind='drawing or diagram',ac=False,ah=True)
change('gamma pi rho Pent',r'\pi\in\mathrm{Pent}(K),\rho\in\mathrm{Rep}\,\pi',r'\pi \in \mathrm{Pand}(K)',r'\pi\in\mathrm{Pent}(K),\rho\in\mathrm{Rep}\,\pi','arrow_gamma_pi_rho',ink='Pent has the same e-n-t sequence as the upper condition and lower key.',ac=False,ah=True)
change('gamma pi rho lower hook',re.search(r'\\arrow\[u,"\{2\\quad\\gamma_\{\\pi,\\rho\}.*?\]',C).group(0),hbetween(r'\item $\gamma_{\pi,\rho}',r'\pi$) ;'),S['arrow_gamma_pi_rho'],'arrow_gamma_pi_rho',ink='The top has a complete upward arrowhead. The bottom has a curved left hook rising from the tail, without a second complete head; that visible hook is retained as a stroke.',kind='drawing or diagram',ah=True)
change('tau pi rho quarter',r'\unsure{1/4|1/3}',r'\tau_{\pi,\rho} = \mathrm{tw}_{1/4}',r'\tau_{\pi,\rho}=\mathrm{tw}_{1/4}','arrow_tau_pi_rho',ink='The denominator has an angled upper limb, a crossing horizontal stroke and right upright: 4, not 3.')
change('tau pi rho target degree',r'\unsure{1|2}',r'\tau_{\pi,\rho} = \mathrm{tw}_{1/4}$ : $2 \to 2$',r'2\quad\tau_{\pi,\rho}=\mathrm{tw}_{1/4}\quad1','arrow_tau_pi_rho',ink='The head degree is one upright with a foot, without the curved head and diagonal foot of 2.',ah=True)
change('gamma r1 source',r'\arrow[u,"{1\quad\gamma_r^1\quad2}"]',hbetween(r'\item $\gamma^{1}_{r}',r"vers $\mathrm{II}'_2$ ;"),r"\mathrm{III}_1\xrightarrow{1\quad\gamma_r^1\quad2}\mathrm{II}'_2",'arrows_gamma_r1',ink='The vertical shaft starts at the unprimed III1 block and ends in II2prime. The labels 1 and 2 are visible at its ends.',kind='drawing or diagram',ac=False,ah=True)
change('gamma r1prime oval and exclamation',re.search(r'\\arrow\[ur,.*?\]',C).group(0),hbetween(r'$\gamma^{1\,\prime}_{r}$ :',r'vers $\mathrm{II}_1$ ;'),S['arrows_gamma_r1'],'arrows_gamma_r1',ink='A pencil oval encloses the diagonal gamma label. Inside it, below and to the right, a separate upright and dot form an exclamation mark; the shaft crosses the oval.',kind='drawing or diagram',ah=True)
change('gamma r2 broad arc target',re.search(r'\\arrow\[ul,bend left=40.*?\]',C).group(0),hbetween(r'$\gamma^{2}_{r}$ (grand arc',r'$\mathrm{I}_4$)'),S['arc_gamma_r2'],'arc_gamma_r2',ink='The large U-shaped curve leaves III2prime beside 2, dips below III1, then rises to an up-left head beside 2 near x1030,y945, outside and left of II2prime: its target is II2.',kind='drawing or diagram',ah=True)
change('gamma r2prime exponent and target',re.search(r'\\arrow\[uu,bend right=70.*?\]',C).group(0),hbetween(r'$\gamma^{2\,\prime}_{r}$ (de',r'$\mathrm{II}_1$).'),S['arc_gamma_r2prime'],'arc_gamma_r2prime',ink='The superscript is 2 followed by a short detached stroke without the hooked head or foot of a written 1. Root confirmed the prime by stroke comparison. The long outer arc runs from III2prime beside 1 to I4 beside 2.',confidence='medium',kind='drawing or diagram',ah=True)
# Full witness drawing quotations, not placeholder descriptions.
hdrawing=H[H.index(r'\drawing{'):H.index('\n\n',H.index(r'\drawing{'))]
for n,key in enumerate(fig_keys,180):
 c=re.search(r'^\\sbox\{'+str(n)+r'\}.*$',C,re.M).group(0)
 h=hdrawing
 ah=False
 if n==183:h=hbetween(r'\note{sur la sphère',r"\beta'$}")
 if n in (184,185):
  h=hbetween(r'\note{deux sphères ; la première',r"\alpha_1, P$}");ah=n==185
 if n==186:
  h=hbetween(r'\note{le $\lbrace 1 \rbrace$',r'$u_0, \ldots, u_5$}');ah=True
 if n in (188,189):h=r'\note{deux sphères égalées, portant $P, \bar{P}, 0, 1, \infty$}'
 change(key,c,h,F[str(n)],key,kind='drawing or diagram',ah=ah)
change('margin arrow1 course',r'\draw[->] (1.5,3.3)--(.5,3.3);','',S['margin_arrow1'],'margin_arrow1',kind='drawing or diagram',ah=True)
change('margin arrow2 course',r'\draw[->] (1.5,1.1)--(.5,1.1);','',S['margin_arrow2'],'margin_arrow2',kind='drawing or diagram',ah=True)
change('margin bracket and detached base','','',S['margin_bracket_base'],'margin_bracket_base',kind='omission',ah=True,math=False)
change('isolated upper hooked stroke','','',S['top_isolated_mark'],'top_isolated_mark',kind='omission',ah=True,math=False)
change('reverse-side listing excluded',r'\unsure{\texttt{GUTS OUTPUT FOR PREDONT DELIVER AT 0000 - PREDONT.MODULEF5}}','','','listing_bleed',ink='All 28 identical C entries refer to pale blue, laterally reversed machine print showing through the leaf. It is not front-side source text; no reading of that print is supplied.',kind='text not on the page',math=False)
# Mark decisions: one for each of all 48 supplied IDs.
dec={
'M0299':('other','P','i10_text','high'),
'M0300':('first',r'\mathrm{Circ}','i10_text','high'),
'M0301':('undecided',r'\unsure{\mathfrak S|G}_J','i6_text','low'),
'M0302':('undecided',r'\unsure{\mathfrak S|G}_3','i6_text','low'),
'M0303':('undecided',r'\unsure{\mathfrak S|G}_3','i6_text','low'),
'M0304':('first',r'\delta','i4_text','high'),
'M0305':('first',r'\omega','arrow_fq','high'),
'M0306':('first',r'\Lambda','arrow_fq','high'),
'M0307':('alternative','B','ii2_text','high'),
'M0308':('alternative','B','ii2_text','high'),
'M0309':('alternative',r"\gamma'_{\pi,s}",'arrows_upper_middle','medium'),
'M0310':('undecided',r'\unsure{\vec Q|\vec G}','arrows_upper_middle','low'),
'M0311':('first','entièrement','ii1_text','high'),
'M0312':('undecided',r'\unsure{\vec Q|\vec G}','arrows_upper_middle','low'),
'M0313':('undecided',r'\unsure{\tau_{\pi,\omega}}','arrow_tau_pi_rho','low'),
'M0314':('first','1/4','arrow_tau_pi_rho','high'),
'M0315':('first','1','arrow_tau_pi_rho','high'),
'M0316':('undecided',r'\unsure{\mathfrak X|\mathbb J}','iii2prime_text','low'),
'M0317':('alternative',r"\gamma_r^{2'}",'arc_gamma_r2prime','medium'),
'M0318':('first',r'\mathrm{Pent}','parameter_key','high')}
for i in range(319,347):dec['M'+str(i).zfill(4)]=('other','','listing_bleed','high')
with (packet/'marks.tsv').open(newline='') as f:marks=list(csv.DictReader(f,delimiter='\t',quoting=csv.QUOTE_NONE))
for m in marks:
 d,r,k,q=dec[m['id']];ink=evidence(k)
 if m['id'] in ('M0309','M0317'):ink='Reader C initially retained the ambiguity. Root adjudicated the short detached stroke as a prime: it lacks the hooked top and basal foot of numerical 1 in the same saved crop, with a separately read notation occurrence confirming the same stroke. No new reader-C crop was made.'
 R['decisions'].append(dict(id=m['id'],decision=d,reading=r,ink=ink,crop=crop(k),box=boxes[k],confidence=q))
# Unresolved readings include doubts added outside the original mark inventory.
for place,read,issue,alts in [
 ('I6 three group symbols',r'\unsure{\mathfrak S|G}_J,\ \unsure{\mathfrak S|G}_3,\ \unsure{\mathfrak S|G}_3','All three have a wavy upper stroke and broad lower loop; the alphabet is not settled by the ink.',['\\mathfrak S','G']),
 ('upper compatibility symbol',r'\unsure{\vec Q|\vec G}','The lower loop and right continuation do not securely separate Q from G.',['\\vec Q','\\vec G']),
 ('lower compatibility symbol',r'\unsure{\vec Q|\vec G}','The retraced loop remains open to Q or G.',['\\vec Q','\\vec G']),
 ('fBs accent',r'\unsure{\mathrm{Bit\acute et}|\mathrm{Bitet}}','The short upper stroke is faint in this occurrence; the lower key accent was adjudicated separately.',['Bitét','Bitet']),
 ('II2 struck word',r'\deleted{\text{\unsure{repères}}}','The separate lower word is struck; not every letter can be distinguished from its crossing strokes.',['repères','unread canceled word']),
 ('II2prime struck word',r'\deleted{\text{\unsure{repères}}}','The entire word after 4 sommets is crossed; its internal letters remain partly obscured.',['repères','unread canceled word']),
 ('II1 canceled group material',r'\deleted{\unsure{1}}','The overwritten dark group entry cannot be read letter by letter.',['1','unread canceled symbol']),
 ('II1 figure P labels',r'\unsure{P},\ \unsure{\bar P}','The live P-like labels are heavily retraced; separate earlier letter forms cannot be securely recovered.',['P and bar P with unread overwritten strokes']),
 ('tau pi omega faint label',r'\unsure{\tau_{\pi,\omega}}','The upper pencil label is faint and partly overwritten by the main annotation.',['\\tau_{\\pi,\\omega}','unread tau subscript']),
 ('III2prime repère formula',r'\unsure{\mathfrak X|\mathbb J}\unsure{(}I)','The X-like letter and a possible left parenthesis cannot be separated confidently; one closing parenthesis is visible.',['\\mathfrak X(I)','\\mathfrak X I)','\\mathbb J(I)']),
 ('III2prime group blob',r'\unsure{\deleted{*}}','The dark material after the quotient does not establish its original glyph or conclusively distinguish cancellation from retracing.',['canceled star-like mark','unread live or canceled strokes']),
 ('III2prime first figure overwritten labels',r'\unsure{\alpha\'},\ \unsure{\beta},\ \unsure{\beta\'}','The top rear and lower two labels contain distinct overlapping dark strokes; the prior forms are not secure.',['alpha-prime, beta, beta-prime with unread underforms']),
 ('level0 middle index',r'\mathrm{III}_{\unsure{1|4}}','The index has a 4-like crossing/angled form; it is not silently regularized to the index expected from the heading.',['1','4']),
 ('punctuation after Aut+',r'\unsure{;|,}','A dot and a long curved descending stroke do not securely distinguish semicolon from comma.',['; ',',']),
 ('parameter NB overwritten relation',r'\unsure{\simeq}','The visible relation is tilde over a horizontal stroke, but separately crossed underlying strokes are unreadable.',['simeq with unread prior relation'])]:unresolved(place,read,issue,alts)
# Inventory. Line totals count separately read text/formula lines and individual written figure labels.
def inv(element,kind,position,words,hand='his hand',lines=0):
 R['inventory'].append(dict(element=element,kind=kind,position=position,first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes'))
 R['lines_read']+=lines
text_blocks=[
 ('I10 block','upper left','I10 (pentagonale)',5),('I6 block','upper middle','I6 (bitétraédrale)',5),('I4 block','upper right','I4 (pyramidale)',8),
 ('II2 block','middle left','II2 (carré-triangle droit)',7),('II2prime block','middle middle','II2prime=Tw1/4 II2',4),('II1 block','middle right','II1 (tétraèdre-triangle)',5),
 ('II1 parameters','middle right below group line','K=J amalg epsilon',4),('III2 block','lower left','III2 (triple triangle droit)',4),('III1 block','lower middle','III1 (triple triangle sem.-gauche)',3),('III2prime block','lower right','III2prime (triple triangle gauche)',7)]
for e,pos,w,l in text_blocks:inv(e,'text',pos,w,lines=l)
for key,w,l in [('arrow_tau_pi_s','2 sommets-repères',2),('ii2prime_count','4 sommets',1),('ii1_count','6 sommets-repères',2),('iii2_count','2+2 sommets-repère',2),('iii1_count','2+4 sommets-repère',2),('iii2prime_count','4+4 sommets-repère',2)]:inv(key,'text',key,w,lines=l)
for key,labels,l in zip(fig_keys,['five unlabeled coloured points','five unlabeled coloured points','five unlabeled coloured points','alpha alpha-prime P beta beta-prime','canceled sphere, no secure labels','alpha P beta beta-prime alpha-prime','1 infinity 0 P barP u0 u1 u2 u3 u4 u5','P','P barP 0 1 infinity','P barP 0 1 infinity','P alpha alpha-prime beta beta-prime','P alpha alpha-prime beta beta-prime'],[0,0,0,5,0,5,11,1,5,5,5,5]):inv(key,'drawing',key,labels,lines=l)
arrow_inventory=[('arrow_fbs','I6 to I4',2),('arrow_fq','I4 to II2prime',2),('arrow_gamma_pi_s','II2 to I10',2),('arrow_tau_pi_s','II2 to II2prime',1),('arrows_upper_middle','II2prime to I6; II1 to I6',4),('arrow_gamma_pi_rho','III2 to II2',2),('arrow_tau_pi_rho','III2 to III1',2),('arrows_gamma_r1','III1 to II2prime and II1',3),('loop_tau_r0','II1 loop',1),('arrow_tau_rprime','III1 to III2prime',1),('arc_gamma_r2','III2prime to II2',1),('arc_gamma_r2prime','III2prime to I4',1)]
for k,w,l in arrow_inventory:inv(k,'diagram',k,w,lines=l)
for k in ['margin_graph1','margin_graph2','margin_graph3','margin_arrow1','margin_arrow2','margin_bracket_base','top_isolated_mark']:inv(k,'drawing','left margin' if k.startswith('margin') else 'upper right margin',S[k])
inv('level table','text','bottom left','niveau 2; niveau 1; niveau 0; overline542',lines=4)
inv('indice note','margin note','bottom left under level table','l’indice indique l’ordre de G=Aut+',lines=1)
inv('NB real structures','margin note','bottom left last line','NB Sauf I4 toutes ces structures sont réelles',lines=1)
inv('parameter key','text','bottom middle','pi in Pent(K), B in Bitét(K)',lines=3)
inv('parameter NB','margin note','below parameter key','NB {(pi,rho)} simeq Rep(K)',lines=1)
inv('folio30','margin note','bottom right','30',hand='another unnamed hand',lines=1)
for e,pos,w in [('II2 separate canceled word','under live 2 sommets-repères','repères?'),('II2prime canceled word','after 4 sommets','repères?'),('II2prime canceled sphere','left of live sphere','seven oblique cancellation strokes'),('II1 canceled group entry','between G= and ={1}','1?'),('III2prime doubtful canceled blob','after Z/2Z','star-like mark?')]:inv(e,'deletion',pos,w)
inv('str insertion','in III2prime descriptive line above carré','str.') if False else None
inv('str insertion','insertion','above carré in lower right block','str.')
inv('circled gamma annotation','drawing','between III1 and II1','gamma_r^{1prime} and separate exclamation mark',lines=1)
for e,pos,w in [('III2prime index retracing','lower right heading','2'),('III2prime count retracing','lower right text','60'),('III2prime K retracing','lower right text','K'),('III2 second count retracing','beside lower left sphere','second2'),('niveau2 retracing','bottom left level table','2'),('III2prime figure label overtracing','upper rear and lower two labels','alpha-prime beta beta-prime'),('II1 P-label overtracing','bottom of II1 sphere','P and barP'),('parameter relation overtracing','NB below parameter key','simeq')]:inv(e,'text',pos,w)
# All potentially difficult places nominated with original rectangles, one rectangle per place.
for i,(key,b) in enumerate(boxes.items(),1):
 kind='drawing' if key.startswith(('figure','margin','top_')) else 'formula or text'
 if key in ['ii2prime_count','arrow_tau_pi_s','ii1_text','iii2prime_text']:kind='deletion or insertion and surrounding text'
 if key=='folio':kind='handwritten number'
 if key=='listing_bleed':kind='excluded reverse-side material'
 R['second_boxes'].append(dict(box='031_c_'+str(i).zfill(3),kind=kind,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=S[key]))
R['notes']=[
 dict(id='148-031-N01',type='page',text='This landscape manuscript contains nine related structure blocks, twelve sphere drawings including one canceled drawing, three marginal graphs, two retraced marginal arrows and two long outer arcs. The main ink and pencil are treated as his hand; the light folio30 is attributed only to another unnamed hand.'),
 dict(id='148-031-N02',type='excluded material',text='Pale blue laterally reversed computer listing shows through from the reverse. It is excluded entirely, including all 28 identical GUTS lines supplied by C. It is not treated as illegible front-side text.'),
 dict(id='148-031-N03',type='literal formula',text='The I10 expression visibly opens two parentheses and closes one after K. The unmatched formula is preserved without completing it.'),
 dict(id='148-031-N04',type='literal notation',text='The II2 block visibly combines B in two formulas with J in P in J and omega hooked into J. All letters are retained as written; no mathematical consistency correction was made.'),
 dict(id='148-031-N05',type='uncertainty',text='The three I6 group symbols remain S/G ambiguities. Neither the expected symmetry group nor the wording of either witness was used to resolve them.'),
 dict(id='148-031-N06',type='root adjudication',text='Reader C initially retained 1/prime ambiguity in the upper gamma_pi,s and 21/2prime in the outer gamma_r superscript. Root subsequently adjudicated both detached strokes as primes at medium confidence, using their lack of a numerical1 hook or foot on the saved031 crops and an independent notation comparison reported from033. Reader C did not inspect another page.'),
 dict(id='148-031-N07',type='root adjudication',text='Reader C did not securely isolate the accent in the lower Bitét key. Root identified a visible accent in that saved crop; the final reading retains Bitét. The upper fBs occurrence remains uncertain separately.'),
 dict(id='148-031-N08',type='retracing',text='The current digits 2 in the III2prime heading,60 in its text,2 in niveau2 and the second2 in III2 count are readable. They are retraced but no earlier digit is supplied. The current K is also legible without a secure prior form. Distinctly overlapping figure-label strokes remain flagged where they prevent a clean reading.'),
 dict(id='148-031-N09',type='diagram',text='The broad lower gamma_r2 arc runs from III2prime to II2, with degree2 at each end. This differs from both witnesses. The narrow outer-right gamma_r2prime arc runs from III2prime to I4, with1 at the tail and2 at the head.'),
 dict(id='148-031-N10',type='diagram',text='The lower end of gamma_pi,rho has a curved hook but not a second complete arrowhead. The trace preserves that hook without assigning a second semantic direction. The upper marginal arrow likewise retains its mid-shaft meeting strokes.'),
 dict(id='148-031-N11',type='drawing',text='Five large coloured points are distinguished from smaller black junctions. The canceled II2prime drawing has no securely surviving written point labels; C duplicated labels from its neighbouring drawing. The two lower right figures have eight black junctions each and visible black crosslinks absent from C.'),
 dict(id='148-031-N12',type='workflow',text='Whole page and two native overlapping halves were each visually read once. Fifty-three distinct original crop rectangles were viewed once per place. One interrupted, invalid iii1_text PNG was preserved and recreated at the identical rectangle as documented in crop_recovery.json; no valid crop was replaced. No OCR, web research, other-page reader source, or TeX compilation was used.'),
 dict(id='148-031-N13',type='accounting',text='Run SP82_C13_148; reader C, model GPT-6 Astra Pro, effort not exposed, date2026-11-20. The line count records separately read text/formula lines, arrow-label/condition lines and individual figure labels, excluding reverse-side print. No independent mathematical computation or proof was performed, so checks is empty.'),
 dict(id='148-031-N14',type='layout limitation',text='The complex spatial relation of nine large blocks, crossing arrows and twelve irregular sphere drawings is approximated in TikZ/TikZ-cd; the candidate retains crop-candidate for the full plate. Exact counts, labels, solid/dashed paths, gaps and cancellation marks were transcribed from the saved crops.'),
]
R['hand_log']=[
 dict(pages=[31],hand='his hand',observation='Curly epsilon has rounded joined lobes in all five occurrences in the II1 parameter block.',holds_at_every_observed_occurrence=True,witness_effect='H reads E at all five places; C epsilon is retained.'),
 dict(pages=[31],hand='his hand',observation='The two B letters in II2 have two right-facing bowls, contrasting with nearby long hooked J.',holds_at_every_observed_occurrence=True,witness_effect='C marks J|B twice; both read B.'),
 dict(pages=[31],hand='his hand',observation='The delta before the wedge has a lower loop and rising stem like the defined delta on the preceding line.',holds_at_every_observed_occurrence=True,witness_effect='C delta|J resolved as delta; H J rejected.'),
 dict(pages=[31],hand='his hand',observation='The short detached primes have no hooked top or basal foot, unlike adjacent numerical1 strokes; root made the final comparison for two ambiguous instances.',holds_at_every_observed_occurrence=False,witness_effect='C gamma^1_pi,s and gamma_r^21 alternatives are replaced by the primes after root adjudication.'),
 dict(pages=[31],hand='his hand',observation='Three I6 group symbols have broad lower loops and wavering tops, which do not securely distinguish S from G.',holds_at_every_observed_occurrence=True,witness_effect='C gives doubtful S, H gives G_J then S3; all three remain explicitly uncertain.'),
 dict(pages=[31],hand='another unnamed hand',observation='Folio30 is lighter and pencilled; attribution is not secure.',holds_at_every_observed_occurrence=True,witness_effect='Foliation retained without assigning the hand.')
]
R['notation']=[
 dict(form=r'\mathrm{Pent}(K)',observed_use=r'\pi\in\mathrm{Pent}(K)',pages=[31],caution='The e-n-t sequence is visible in all three arrow conditions and the lower key; do not substitute Pand.'),
 dict(form=r'\mathrm{Bit\acute et}(K)',observed_use=r'B\in\mathrm{Bit\acute et}(K)',pages=[31],caution='Root confirms the lower-key accent; the upper occurrence remains locally uncertain.'),
 dict(form=r'\vec Q=(Q,\omega)',observed_use='Written oriented square datum in I4.',pages=[31],caution='The comparison annotations remain locally Q/G uncertain.'),
 dict(form=r"\gamma'_{\pi,s},\ \gamma_r^{2'}",observed_use='Prime-bearing arrow labels.',pages=[31],caution='Resolved by root comparison of detached prime strokes, with reader first-pass uncertainty recorded.'),
 dict(form='coloured point / black junction / dashed path',observed_use='Sphere drawings distinguish five large reddish points from smaller black junctions and rear dashed courses.',pages=[31],caution='Do not replace these with a uniform grid of identical dots.'),
 dict(form=r'\mathrm{tw}_{1/4},\ \mathrm{Tw}_{1/4},\ \mathrm{tw}_{1/6}',observed_use='Lowercase tw on arrows and uppercase Tw in the II2prime heading.',pages=[31],caution='Case is retained locally; no expansion is inserted.')
]
R['abbreviations']=[dict(form=a,expansion=b) for a,b in [('ens.','ensemble'),('str.','structure'),('comp.','compatible'),('compat.','compatible'),('sem.','semi'),('nb','nombre'),('i.e.','id est'),('NB','nota bene'),('card','cardinal')]]
# Differences TSV uses literal quote tokens: QUOTE_NONE is essential.
with (packet/'differences.tsv').open(newline='') as f:diffs=list(csv.DictReader(f,delimiter='\t',quoting=csv.QUOTE_NONE))
reading={
168:'twelve sphere drawings; actual paths and labels',171:'I10 P2',172:'I10 unmatched parenthesis',177:'I6 group-symbol uncertainty',179:'fBs arrow and accent',182:'I4 top masculine plural',184:'I4 lower feminine singular',188:'I4 omega delta',190:'I4 group equality',192:'fQ label, condition and direction',194:'II2 count, live repères and separate deletion',195:'II2 quotation marks',196:'II2 pentagone phrase and quotation marks',198:'II2 first B',200:'II2 omega relation',201:'II2 second B',203:'II2 to I10 and II2prime arrows; II2prime text',205:'upper gamma pi s prime; II2 figure labels',206:'upper gamma pi s prime; II2 figure labels',207:'II2prime heading and upper gamma alignment',208:'upper gamma compatibility uncertainty and degree3',209:'upper gamma Pent condition',210:'II2prime même paramétrage and canceled drawing',211:'II2prime live sphere labels',212:'II2prime alpha-prime label',215:'II1 entièrement',217:'II1 canceled group material',218:'II1 figure P and barP labels; canceled group material',220:'II1 epsilon1',222:'II1 epsilon2',224:'II1 omega closing parenthesis',225:'II1 epsilon3',228:'II1 epsilon4',229:'II1 minus before1',230:'II1 epsilon5',232:'gamma r0 and tau r0 separate arrows',233:'gamma r0 target, exponent and compatibility uncertainty',234:'outer gamma r2prime separate from tau r0 loop',237:'III2 quotation marks',238:'III2 pentagone phrase and quotation marks',240:'III2 group equality',241:'gamma pi rho arrow and Pent',242:'tau pi rho quarter, degree1 and faint upper label',243:'III1 sem abbreviation and unprimed heading',244:'III1 paired figures',248:'III1 figure point labels',249:'gamma r1 source and target',250:'gamma r1prime circle, exclamation and tau rprime',251:'III2prime paired sphere drawings',253:'III2prime codiagonales plural',255:'III2prime lower carré en codiagonales',258:'III2prime repère formula uncertainty',259:'III2prime right parenthesis scope',260:'III2prime doubtful canceled blob',261:'III2prime readable current digits and unread underforms',262:'fBs arrow degrees and parameters',263:'fQ direction and condition',264:'fQ omega, Latin a and direction',265:'upper gamma arrows, prime and Pent conditions',266:'gamma pi rho and tau pi rho labels',267:'gamma r1 source',268:'gamma r1prime and tau rprime',269:'gamma r2 broad arc target',270:'gamma r2prime exponent and outer arc',271:'gamma r2prime target I4',273:'level0 middle index uncertainty; no prime',274:'total word absent',275:'readable level counts and retracing',276:'indice quotation marks',279:'punctuation after Aut+ remains uncertain',284:'réelles quotation marks',286:'parameter key Pent',288:'parameter key Bitét accent adjudication',293:'parameter NB overwritten relation; reverse-side listing excluded'}
macro_places={
155:'scan marker and H editorial overview',156:'drawing style versus H editorial overview',157:'drawing style versus H editorial overview',158:'drawing style versus H editorial overview',159:'margin graph representation',160:'margin graph and H drawing synopsis',161:'drawing layout',162:'drawing layout',163:'drawing layout',164:'drawing layout',165:'drawing layout',166:'margin graph representation',167:'margin graph representation',169:'inline figure number and heading layout',170:'display-to-prose punctuation',173:'group-display punctuation',174:'display wrapper',175:'inline figure number and heading layout',176:'display-to-prose punctuation',178:'group-display punctuation',180:'gathered wrapper',181:'inline figure number and heading layout',183:'display-to-prose punctuation',185:'display wrapper and punctuation',186:'H parenthetical grouping of delta definition',187:'H parenthetical grouping of delta definition',189:'display-to-prose punctuation',191:'TikZ arrow options',193:'gathered wrapper',197:'display-to-prose punctuation',199:'display-to-prose punctuation',202:'group displays reordered by alignment',204:'gathered wrapper versus editorial note',213:'inline figure number and heading layout',214:'display-to-prose punctuation',216:'display wrapper',219:'gathered wrapper',221:'formula spacing punctuation',223:'display-to-prose punctuation',226:'superscript-before-subscript syntax',227:'superscript-before-subscript syntax',231:'gathered wrapper versus editorial description',235:'inline figure number and heading layout',236:'display-to-prose punctuation',239:'display wrapper',245:'display-to-prose punctuation',246:'display wrapper',247:'display wrapper and figure synopsis',252:'display-to-prose punctuation',254:'typographic apostrophe',256:'display-to-prose punctuation',257:'typographic apostrophe',272:'array column specification',277:'typographic apostrophe',278:'inline math delimiter token',280:'inline math delimiter token',281:'inline math delimiter token',282:'inline math delimiter token',283:'inline math delimiter token',285:'array wrapper',287:'parameter-key column ordering',289:'parameter-key column ordering',290:'parameter-key column ordering and punctuation',291:'array wrapper',292:'inline math delimiter token'}
for d in diffs:
 n=int(d['source_row'])
 if n in reading:R['differences_review'].append(dict(source_row=n,classification='reading decision',place=reading[n]))
 elif n in macro_places:R['differences_review'].append(dict(source_row=n,classification='macro-only',place=macro_places[n]))
 else:raise ValueError('Unmapped difference '+str(n))
assert len(R['decisions'])==48 and len({x['id'] for x in R['decisions']})==48
assert len(R['differences_review'])==139 and {x['source_row'] for x in R['differences_review']}==set(range(155,294))
assert len(R['second_boxes'])==53
for x in R['changes']:
 key=x['crop'].removeprefix('crops/148_scan031_').removesuffix('.png');assert x['box']==boxes[key]
(out/'result.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print('Saved result:',len(R['changes']),'changes,',len(R['decisions']),'marks,',len(R['inventory']),'inventory elements,',len(R['second_boxes']),'second boxes,',len(R['differences_review']),'diff rows; lines',R['lines_read'])
