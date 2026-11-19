import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\unsure{necessary|necesary|neccessary|neccesary}',r'necessary'),(r'\unsure{\gamma|\mathscr{T}}',r'\unsure{\mathscr{J}|\mathcal{J}|\gamma}'),(r'\gamma',r'\mathscr{J}'),(r'\unsure{\mathscr{J}|\mathcal{J}|\mathscr{J}}',r'\unsure{\mathscr{J}|\mathcal{J}|\gamma}'),(r'\unsure{Hodge-structures|Hodge-structure}',r'Hodge-structures'),(r'\unsure{\mathscr{V}|V}',r'\mathscr{V}'),(r'\unsure{conjectures|conjecture}',r'conjectures'),(r'\unsure{not}',r'\unsure{not|\deleted{not}}'),(r'wrong\unsure{.|{}}',r'wrong')]
L=[]
def a(p,c,h,f,s,k='other',v='high',C=False,H=True,m='no',q=None):
 d=dict(place=p,c=c,h=h,final=f,ink=s,kind=k,confidence=v,against_c=C,against_h=H,marked_in_H=m)
 if q:d['consequential']=q
 L.append(d)
a('necessary spelling',r'\unsure{necessary|necesary|neccessary|neccesary}','necessary','necessary','necessary: n, looped e, open c, next looped e, joined double-s stroke, ary; separate underline.','other',C=True,H=False)
a('period-domain glyph',r'\unsure{gamma|mathscr T}; gamma',r'\mathcal J',r'\unsure{\mathscr J|\mathcal J|\gamma}; \mathscr J','top, cancel_bottom and end: same upper branches and long lower loop as previous pages.','misread symbol or index','medium',True,False)
a('Hodge-structures ending',r'\unsure{Hodge-structures|Hodge-structure}','Hodge-structure','Hodge-structures','top: terminal s after e visible at far right.','misread word',C=True)
a('family glyph',r'\unsure{\mathscr V|V}, then \mathscr V','V',r'\mathscr V','top/cancel_bottom: open curved left stroke and high right hook, distinct from pointed plain V.','misread symbol or index',C=True)
a('conjectures ending',r'\unsure{conjectures|conjecture}','conjectures','conjectures','top: low final s before closing parenthesis.','other',C=True,H=False)
a('real-group component exponent',r'\unsure{0|\circ}',r'\circ',r'\unsure{0|\circ}','formula: small closed oval at upper right outside parenthesis; zero/circle not distinguishable from its ink alone.','misread symbol or index','medium')
a('conjugate expression',r'g[i_0(U_R)]g^{-1}',r'g i_0(\mathbb U_R)g^{-1}',r'g[i_0(U_R)]g^{-1}','formula: square opening bracket immediately after g, corresponding closing square stroke; U has a single bowl, no doubled vertical.','omission')
a('last subgroup symbol',r'\unsure{\Gamma|T}_0',r'\Gamma_0',r'\unsure{\Gamma|T}_0','formula: long horizontal bar with downstroke slightly inset from left end; unlike clear Gamma_0 above, Gamma/T remains uncertain.','misread symbol or index','medium')
a('not within cancelled block',r'\unsure{not}','not; editorial note says separately crossed out',r'\unsure{not|\deleted{not}}','cancel_top: letters not readable; thick retracing overlaps n/o and grid crosses nearby. Separate cancellation cannot be securely distinguished from retracing.','deletion state (struck given live or live given struck)','low',True,True)
a('usual within cancelled block',r'\uline{usual}','usual',r'\uline{usual}','cancel_top: separate short horizontal underline below usual survives larger cancellation grid.','omission')
a('as we know','as we know',r'\ill{} we know','as we know','cancel_bottom: low a and s remain left of we, crossed only by the general cancellation.','readable ink left as \\ill{}',m='yes')
a('is within cancelled block',r'\uline{is}','is',r'\uline{is}','cancel_bottom: short underline immediately beneath is, distinct from oblique cancellation strokes.','omission')
a('cancelled ending punctuation',r'wrong\unsure{.|{}}','wrong.','wrong','cancel_bottom: g descender reaches box edge; no separate period after word.','other',C=True)
a('Question location',r'\margin{Question ...}','running paragraph',r'\margin{Question ...}','question: smaller text occupies cut-out lower-right corner beside cancelled passage, above next running paragraph.','insertion or placement')
a('Question punctuation',r'\unsure{?!|??}','??',r'\unsure{?!|??}','question: first curved mark and second more vertical hooked stroke, each with dot; second may be emphatic exclamation or question mark.','other','medium')
a('brace at final question','left brace beside four final lines','no brace','left brace beside four final lines','end: tall left curly mark groups Boulder talk through constructible?; no right partner.','drawing or diagram')
I=[]
def i(k,p,t):I.append(dict(kind=k,position=p,text=t))
i('text','top','To come back ... G itself.')
i('insertion','above subgroup','alg.')
i('display','upper condition','g in G(R)^0, Gamma_0, H_R contains g[i_0(U_R)]g^-1 and Gamma_0')
i('deletion','central large crosshatched block','I did not try ... conjecture is wrong')
i('deletion','inside cancelled block','not: possible independent cancellation')
i('marginnote','lower-right of cancelled block','Question: If G_R ... Zariski-dense in G?!')
i('text','bottom','By the way ... constructible?')
i('display','final four lines','left brace beside Boulder talk ... constructible?')
commit(13,20,dict(replace=R,changes=L,inventory=I,sheet_kind='letter',observations='Whole and halves inspected; top, formula, cancelled block in two overlapping bands, question, ending brace, and necessary crops inspected. Full cancelled block preserved. Context still unopened.'))
