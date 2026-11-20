from records import *
p=page('162-1',9)
tex=r'''\scanpage{9}
\deleted{\unsure{Brieskorn|Briskorn}}

\deleted{2 lettres Deligne sur connexions intégr.bles (sur $\mathbb C$)}

\deleted{Notes Serre formes quadratiques}

\deleted{Rapport Griffiths sur périodes}

\deleted{Séminaire Chevalley gr. \unsure{semi|ses} alg.}

\deleted{Schlessinger, \unsure{thèse|Thèse}}

\deleted{Trois tirages \unsure{à} \unsure{part} de Bott}

\deleted{Borel : Springer Lecture Notes}

\deleted{Rim : SGA 7 $\overline{\underline{\unsure{\mathrm{XVI}|\mathrm{VI}}}}$}

Demazure\qquad \deleted{notes sur Kostant, sur résolution d'un morphisme ....}

Saavedra\quad \(\left\{\vcenter{\hbox{\begin{minipage}{.87\linewidth}
\deleted{Griffiths, Schmid}

\deleted{Bourbaki Groupes de Lie}

\deleted{Notes sur polarisations dans catégories tannakiennes}

\deleted{Notes sur structure de Hodge, lettre : Mumford, deriv. transc. des motifs en car. 0}

\deleted{Tate : \uline{cohomologie} tores}
\end{minipage}}}\right.\)

Bitzakis\qquad Bourbaki Algèbre

\deleted{Van de Ven}

\deleted{Mes notes sur}

\deleted{SGA 7 XX (Katz : le th. de Griffiths \unsure{)|\S}}

\deleted{\uline{Griffiths : Report on Variation of Hodge structure}}

Saint Donat 2\qquad \(\left\vert\begin{array}{@{}p{.68\linewidth}@{}}SGA 5 $\overline{\underline{\mathrm{XVIII}}}$\\Notes Mumford sur variétés définies par \unsure{équs.|éqs.} quadratiques\\Livre Mumford V.A.\end{array}\right.\)

Hubbard\qquad \unsure{tir.g.|tir.g} à part sur rigidité des structures complexes (\unsure{Man.|Ann.} Math.)

Nakis\qquad Produits tens. top. (Groth.)

% archive sheet number: 8
\clearpage
'''
def c(place,C,H,F,S,K='misread word',conf='high',a='CH',m='no'):change(p,place,C,H,F,S,K,conf,a,m)
c('top recipient',r'\unsure{Brieskorn|Briskorn}',r'\ill',r'\unsure{Brieskorn|Briskorn}','Crop 162-1/009 (140,51,325,127): B-r-i, obscured medial strokes, then k-o-r-n. A word can be read, although the internal e/s remains partly covered.','readable ink left as \\ill{}','medium','H','yes')
c('Deligne / abbreviated adjective',r'\unsure{intégr.bles|intégrables}','intégrables','intégr.bles','Crop 162-1/009 (1174,69,1405,139): a distinct point follows the g/r group before the tall b and l; the omitted a is not supplied.','abbreviation expanded or spelling modernised','high','H')
c('Chevalley subject',r'\unsure{gr.|gr} \unsure{semi|ses} \unsure{alg.|sg.}','groupes par algèbres',r'gr. \unsure{semi|ses} alg.','Crop 162-1/009 (490,248,1213,374): three short groups; the first has g/r and a point, the last a-l-g and a point. The middle remains obscured by cancellation.','abbreviation expanded or spelling modernised','medium','H')
c('Bott quantity','Trois','Tous','Trois','Crop 162-1/009 (485,377,1151,449): after T there is a separate r turn before the o/i/s group.','misread word','high','H')
c('Rim chapter',r'capped XVI|VI','VI',r'capped \unsure{XVI|VI}','Crop 162-1/009 (645,487,900,556): a heavily retraced sign precedes VI within the cap and foot. It may be X; it is not safe to omit it as H does.','misread symbol or index','medium','H')
c('Demazure / end of title','....',r'\ill','....','Half a: a short series of low dots follows morphisme; no word is visible there.','text not on the page','high','H','yes')
c('Saavedra / collaborator',r'\unsure{Schmid|Schmidt}',r'\uncertain{Columbia}','Schmid','Crop 162-1/009 (525,762,900,828): S followed by ch, low m/i and a final d ascender; no terminal t after d.','misread word','high','H','yes')
c('Hodge note / cancellation','struck','live','struck','Crop 162-1/009 (525,869,1650,1000): pale oblique cancelling strokes run across the two-line entry, including the continuation des motifs en car. 0. This records the visible cancellation, without claiming an order of ink layers.','deletion state (struck given live or live given struck)','medium','H')
c('Hodge note / technical abbreviation',r'\unsure{deriv.|dériv.} \unsure{transc.|transc}','description transcendante','deriv. transc.','Same crop (525,869,1650,1000): short d-e-r-i-v group, point, then t-r-a-n-s-c and point. The source does not spell description or transcendante.','abbreviation expanded or spelling modernised','medium','H')
c('Hodge note / characteristic','car. 0','caractéristique 0','car. 0','Same crop: three-letter c-a-r group and point before zero.','abbreviation expanded or spelling modernised','high','H')
c('Tate / inserted word absent','cohomologie tores',r'cohomologie \add{des} tores','cohomologie tores','Half b: there is a gap after cohomologie and then tores; no written des is present above or in that gap.','text not on the page','high','H')
c('Bitzakis / ownership of Bourbaki title','Bitzakis; Bourbaki Algèbre live','Bourbaki Algèbre under Saavedra, struck; Bitzakis followed by ill','Bitzakis; Bourbaki Algèbre live','Crop 162-1/009 (172,1000,1128,1121), read with half b: the Saavedra brace ends above this line, which aligns with Bitzakis. The sloping separator runs above Bourbaki Algèbre; it does not cross its letters.','insertion or placement','high','H','yes')
c('Van de Ven / two-line entry','Mes notes sur; SGA 7 XX ... struck','Mes notes sur SGA 7 XX ... live','both lines struck','Half b: independent cancellation strokes traverse Mes notes sur and the SGA line, not just the recipient.','deletion state (struck given live or live given struck)','high','H')
c('Saint Donat / chapter state','XVIII capped, live','XVIII struck','XVIII capped, live','Half b: cap and foot lie outside the body of XVIII; no crossing line through its centre.','deletion state (struck given live or live given struck)','high','H')
c('Mumford / equations abbreviation',r'\unsure{éqs.|équ.}','équations',r'\unsure{équs.|éqs.}','Crop 162-1/009 (1250,1340,1655,1433): q has a long descender and is followed by a low u-like return and terminal s-like curve before a point. The middle return is weak, so éqs. remains possible.','abbreviation expanded or spelling modernised','medium','CH')
c('Hubbard / abbreviated opening',r'\unsure{tirage|tir.g.}','tirage',r'\unsure{tir.g.|tir.g}','Crop 162-1/009 (521,1740,1101,1870): t-i-r and a separate internal point precede a descending g. No full a/e sequence is visible; a terminal stop is uncertain.','abbreviation expanded or spelling modernised','medium','CH')
c('Hubbard / journal abbreviation','Ann. Math.','Man. Math.',r'\unsure{Man.|Ann.} Math.','Same crop: the first tall letter has a looped entrance and two high strokes, closer to M than A; the small following group reads an. Ann. remains a graphic alternative, not a bibliographic correction.','misread word','medium','C')
c('Nakis / abbreviated title and name','Produits tens. top. (Groth.)','Produits tensoriels topologiques (Grothendieck)','Produits tens. top. (Groth.)','Crop 162-1/009 (520,1871,1262,1940): three abbreviated groups end in visible stops; no full expansions are written.','abbreviation expanded or spelling modernised','high','H')
c('source punctuation and underline scope','no comma after Serre, Chevalley, Bourbaki; Tate colon; cohomologie and whole Griffiths reference underlined','commas added after those names; Tate comma; missing cohomologie underline and author part of Griffiths underline','source punctuation and underline scope retained','Halves a/b: separation after Serre/Chevalley/Bourbaki is blank; Tate has two vertically separated points. The rule under cohomologie and the Griffiths rule beginning beneath the author are visible.','other','high','H')
for a in [('top name','Brieskorn|Briskorn','retained','Multiple cancellation strokes cross the middle letters.'),('Deligne','intégr.bles|intégrables','intégr.bles','Internal point before b.'),('Chevalley','gr.|gr; semi|ses; alg.|sg.','gr.; semi|ses retained; alg.','Points and tall l/g clear; medial abbreviation still crossed.'),('Schlessinger','thèse|Thèse','retained','Initial t/T and h share a tall stroke under a strike.'),('Bott','à|:; part|prod.|p.d.','à and part, each still marked unsure','Faint acute/grave-like mark and p descender favor à part, but cancellation obscures the small letters.'),('Rim','XVI|VI','retained','First sign too heavily retraced.'),('Griffiths collaborator','Schmid|Schmidt','Schmid','No terminal t beyond d.'),('polarisations','tannakiennes|Tannakiennes','tannakiennes','Initial low t rather than separate capital T.'),('Hodge','lettre|lettres; deriv.|dériv.; transc.|transc','lettre; deriv.; transc.','One final e and written stops; no separate accent over deriv.'),('Bitzakis and title','Bitzakis|Bitzahis; Algèbre|Algébre','Bitzakis; Algèbre','Branch of k and grave-like accent visible.'),('Griffiths parenthesis',')|section sign','retained','Crossing meets the closing mark.'),('Mumford adjective','quadratiques|quadritiques','quadratiques','a between r and t visible.'),('Nakis','Nakis; Groth.|Groth','Nakis; Groth.','Half b settles name; crop shows stop after h.')]:certainty(p,*a)
for a in [('top recipient','Brieskorn','Briskorn','medium','Crossing covers medial letters.'),('Chevalley middle abbreviation','semi','ses','low','Most of the letter bodies overlap the cancelling line.'),('Schlessinger initial','thèse','Thèse','medium','Shared tall initial strokes.'),('Bott short words','à part','uncertain small letters under strike','medium','Preference is graphic; no expected title used.'),('Rim numeral','XVI','VI','medium','First mark retouched.'),('Griffiths closing mark',')','section sign','low','Crossing and terminal mark merge.'),('Mumford short form','équs.','éqs.','medium','Low intermediate return can be u or continuation.'),('Hubbard short form','tir.g.','tir.g','medium','Internal abbreviation secure; final point uncertain.'),('Hubbard journal','Man.','Ann.','medium','First capital not completely decisive; no journal identification attempted.')]:doubt(p,*a)
for k,pos,t in [('deletion','top left','Brieskorn'),('deletion','top right line 1','2 lettres Deligne sur connexions intégr.bles'),('deletion','line 2','Notes Serre formes quadratiques'),('deletion','line 3','Rapport Griffiths sur périodes'),('deletion','line 4','Séminaire Chevalley gr. semi alg.'),('deletion','line 5','Schlessinger, thèse'),('deletion','line 6','Trois tirages à part de Bott'),('deletion','line 7','Borel : Springer Lecture Notes'),('deletion','line 8','Rim : SGA 7 XVI'),('text','upper middle left','Demazure'),('deletion','Demazure title','notes sur Kostant, sur résolution d’un morphisme ....'),('text','middle left','Saavedra'),('display','middle right','brace grouping five Saavedra titles'),('deletion','Saavedra 1','Griffiths, Schmid'),('deletion','Saavedra 2','Bourbaki Groupes de Lie'),('deletion','Saavedra 3','Notes sur polarisations dans catégories tannakiennes'),('deletion','Saavedra 4, two lines','Notes sur structure de Hodge ... des motifs en car. 0'),('deletion','Saavedra 5','Tate : cohomologie tores'),('text','below Saavedra brace','Bitzakis; Bourbaki Algèbre'),('deletion','middle lower recipient','Van de Ven'),('deletion','next line','Mes notes sur'),('deletion','next line','SGA 7 XX (Katz : le th. de Griffiths)'),('deletion','next line','underlined Griffiths : Report on Variation of Hodge structure'),('text','lower left','Saint Donat 2'),('display','lower right','vertical grouping of three Saint Donat titles'),('text','Saint Donat 1','SGA 5 XVIII'),('text','Saint Donat 2','Notes Mumford sur variétés définies par équs. quadratiques'),('text','Saint Donat 3','Livre Mumford V.A.'),('text','foot, two lines','Hubbard; tir.g. à part ... (Man. Math.)'),('text','last line','Nakis; Produits tens. top. (Groth.)')]:inventory(p,k,pos,t)
p['notation']=[['Complex field','Doubled vertical/curved C in Deligne parenthesis, set as mathbb C.'],['Roman caps and feet','Rim XVI|VI lies in a cancelled line; Saint Donat XVIII itself is live with cap and foot.'],['Grouping','Saavedra brace ends above Bitzakis/Bourbaki; Saint Donat has a vertical rule.']]
p['hand']=[['Abbreviation with internal dot','intégr.bles and tir.g. omit internal letters; both dots are visible.','H expands both; C preferred full tirage in the latter.'],['Pale cancellation and separator','Pale strokes cross Hodge’s two lines, while the sloping line above Bourbaki Algèbre leaves the letters below intact. Scope limited to these two places.','H reverses these states and attaches Bourbaki to Saavedra.'],['Capital A/M ambiguity','First capital of Man.|Ann. has two tall strokes and a low looped entrance. Does not settle all A/M forms.','C and H disagree; retained as uncertainty.']]
p['abbreviations']=[['intégr.bles','intégrables'],['gr. semi alg.','groupes semi-algébriques, tentative and not a reading of the unclear middle letters'],['deriv. transc.','dérivation transcendante, tentative only'],['car.','caractéristique'],['équs. / éqs.','équations'],['tir.g.','tirage'],['Man. / Ann. Math.','journal abbreviation unresolved; no publication identification attempted'],['tens. top.','tensoriels topologiques'],['Groth.','Grothendieck']]
p['notes']=['Loan-list entries for a cancelled Brieskorn/Briskorn name, Demazure, Saavedra, Bitzakis, Van de Ven, Saint Donat, Hubbard and Nakis. The Bourbaki Algèbre entry is below Saavedra’s brace and aligned with Bitzakis; the text is live.', 'The Hodge entry contains deriv. transc. des motifs en car. 0. This is a reference label, not an argument, and does not establish the expansion of deriv. The pale cancellation marks are recorded without assigning a chronology to the differently dark ink.', 'The Roman numeral at Rim remains XVI|VI; XVIII under Saint Donat has cap and foot but is not cancelled. No mathematical theorem is proved or checked on this list. Archive number 8; no date, title-sheet heading, or page count.']
save(p,tex)
print('Saved',p['filename'],len(p['changes']),'changes;',p['done'])
