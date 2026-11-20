from records import *
p=page('162-1',5)
tex=r'''\scanpage{5}
\deleted{Husemöller\qquad Schlessinger, \unsure{functors|functor} of Artin rings.}

\deleted{Mes notes sur cat. de Picard comm.}

\deleted{Saavedra\qquad \unsure{Classes} de Chern des représentations de groupes discrets}

\deleted{Note sur cat. de Picard}

\inserted{\deleted{Notes sur \unsure{gr.|polygr.} de Picard enveloppant d'une cat. triangulée}}

\deleted{\unsure{Rédaction|Réduction} \unsure{prégroupes|polygr. groupes} \illegible{1} en catégorie.}

\noindent$\left\{\begin{array}{l}\text{\deleted{Notes Catégories de Picard}}\\[-1pt]
\text{\deleted{Notes pré-groupes et $\unsure{0^{\mathrm{ième}}|\mathrm O^{\mathrm{ième}}}$ catégorie}}\end{array}\right.$
\margin{\deleted{Notes filtrations et groupes paraboliques}}

Mme Raynaud \quad 1\qquad Papiers de Horrocks

Papier de Popps (?) sur \uline{th.} de Lefschetz\inserted{Zariski} etc pour $\unsure{\pi_1|\pi_r}$

Deligne App. SGA 7 $\overline{\underline{\mathrm{XXI}}}$

Mme Hakim 1\qquad mes notes sur tapis Quillen $\overline{\underline{\mathrm{I}}}\quad\overline{\underline{\mathrm{II}}}$

\deleted{Katz \unsure{'}\qquad notes sur connexions et équations de Picard-Fuchs.}

\deleted{notes sur torsion dans coh. cristalline, et \unsure{sol.} par \unsure{passage|pass.} de \unsure{fnd.|fond.} sur cohomologie évanescente}

\deleted{notes EGA $\overline{\underline{\mathrm{V}}}$}

Verdier 1\qquad \unsure{Prenote|Prenotes} Séminaire Hartshorne

\deleted{\unsure{Singer}\qquad papier Karoubi}

Bardach\qquad \deleted{Thèse Verdier}

Mumford, sur équivalence rationnelle des $0$-cycles

Harder\qquad Sém Bourbaki, avec exposé Deligne

\deleted{Artin : Algebraization of formal moduli $\overline{\underline{\mathrm{I}}},\overline{\underline{\mathrm{II}}}$}

% archive sheet number: 4
\clearpage
'''
c=lambda place,C,H,F,S,K='misread word',conf='high',a='CH',m='no':change(p,place,C,H,F,S,K,conf,a,m)
c('top recipient',r'\unsure{Husemöller|Huremöller|Murre-Möller}',r'\ill','Husemöller (struck)','Crop 162-1/005 (205,50,555,132): H, use, the two dots over ö, and two tall l strokes survive.','readable ink left as \\ill{}','high','H','yes')
c('Schlessinger title, whole entry',r'\deleted{Schlessinger, \unsure{functor|functors} of Artin rings.}','Schlessinger, Functors of Artin rings (live)',r'\deleted{Schlessinger, \unsure{functors|functor} of Artin rings.}','Crop 162-1/005 (615,54,1465,190): a continuous heavy cancellation crosses the title; the initial f has a descender. Final s remains partly merged with the line.','deletion state (struck given live or live given struck)','high','H')
c('Mes notes, ending',r'Picard \unsure{comm.}','Picard','Picard comm.','Same top-titles crop (615,54,1465,190): a further connected c/omm group and terminal point follow Picard.','omission','high','H')
c('Saavedra / Chern first word and ending',r'\unsure{Classes|Relèv.} de Chern des représentations des groupes discrets',r'\ill de Chern des représentations de groupes \ill',r'\unsure{Classes} de Chern des représentations de groupes discrets','Crop 162-1/005 (590,355,1610,430): large looped initial and following l/strokes favor Classes; de before groupes has no final s; discrets has a tall final t and terminal s.','misread word','medium','CH','yes')
c('crowded added Picard line',r'Notes sur \unsure{polygr.|polygr} de Picard \unsure{enveloppante|enveloppant} d’une cat. triangulée',r'Rédaction \ill Picard enveloppant d’une catégorie triangulée',r'\inserted{\deleted{Notes sur \unsure{gr.|polygr.} de Picard enveloppant d’une cat. triangulée}}','Crop 162-1/005 (570,425,1640,505): an upper line begins Notes sur, with a descending abbreviated group before de Picard; enveloppant ends in a t without a distinct e. cat. has a point and is not expanded. The lower Rédaction line is separate.','insertion or placement','low','CH','yes')
c('lower overwritten line',r'\unsure{Réduction|Restriction} \unsure{polygr.} \unsure{groupes} \illegible{1} en \unsure{catégorie}',r'Rédaction \ill (merged with upper line)',r'\deleted{\unsure{Rédaction|Réduction} \unsure{prégroupes|polygr. groupes} \illegible{1} en catégorie.}','Crop 162-1/005 (570,425,1640,505): lower R-initial word, separate descenders, and en catégorie. survive. Middle ink is overstruck; no secure full reconstruction is possible.','misread word','low','CH','yes')
c('brace second line',r'Notes pré-groupes et \unsure{0^{ième}|O^{ième}|n^{ième}} catégorie',r'Notes \ill catégories',r'Notes pré-groupes et \unsure{0^{ième}|O^{ième}} catégorie','Crop 162-1/005 (595,493,1230,585): p descender, gr loop, et, a closed oval and small raised ième precede singular catégorie.','readable ink left as \\ill{}','medium','H','yes')
c('filtrations note, position','separate normal paragraph','separate normal paragraph',r'\margin{\deleted{Notes filtrations et groupes paraboliques}}','Half a: the two-line note sits to the right of the braced Picard entries at their height, above Mme Raynaud.','insertion or placement','high','CH')
c('filtrations note, deletion','struck','Note filtrations et groupes paraboliques (live)','Notes filtrations et groupes paraboliques (struck)','Half a: diagonal and horizontal cancellation cross the note; terminal s after Notes is visible.','deletion state (struck given live or live given struck)','high','H')
c('Raynaud / Zariski attachment',r'Lefschetz\inserted{-Zariski}','Papiers de Horrocks (Zariski)',r'Lefschetz\inserted{Zariski}','Half a: circled Zariski sits over the Lefschetz ending with a descending connector to that line; it is not next to Horrocks and no hyphen is written.','insertion or placement','high','CH')
c('Raynaud / second author',r'\unsure{Popps|Popp}',r'\uncertain{Popp}',r'Popps (?)','Crop 162-1/005 (790,632,1010,708): two p descenders and a separate final s before the parenthesized question mark.','misread word','high','H','yes')
c('Raynaud / th. underline','th.','th.',r'\uline{th.}','Half a: short independent horizontal below th.; it does not cross the letters.','other','high','CH')
c('Raynaud / etc punctuation','etc','etc.','etc','Half a: no point separates etc from pour.','other','high','H')
c('Deligne / XXI','XXI barred above and below','XXI struck','XXI barred above and below, live','Half a: cap and foot frame the numeral; no cancellation passes through its centre.','deletion state (struck given live or live given struck)','high','H')
c('Katz / small mark',r'\unsure{,|’}','absent',r'\unsure{’}','Half b: small isolated high oblique mark after Katz, partly intersected by the crossing.','omission','medium','H')
c('Katz / cristalline abbreviation','coh.','cohomologie','coh.','Half b and crop 162-1/005 (470,1122,1515,1240): three-letter abbreviated group followed by a point.','abbreviation expanded or spelling modernised','high','H')
c('Katz / continuation',r'et \unsure{sol.|obs.} par \unsure{passage|pap.} \unsure{de|du} \unsure{fnd.|fond.}',r'et sol. \ill de fond \ill',r'et \unsure{sol.} par \unsure{passage|pass.} de \unsure{fnd.|fond.}','Crop 162-1/005 (470,1122,1515,1240), read with half b: par is a separate group; the following word and abbreviated f-initial group remain crossed. No extra legible word follows that abbreviation before sur.','readable ink left as \\ill{}','low','H','yes')
c('Verdier entry',r'Verdier 1 \unsure{Prenotes|Prénotes|Prechter} Séminaire Hartshorne','absent',r'Verdier 1 \unsure{Prenote|Prenotes} Séminaire Hartshorne','Half b and crop 162-1/005 (500,1405,775,1518): P-r-e-n-o-t-e outline, no separate accent; final small curve may be e or es. Entire line is uncancelled.','omission','medium','CH')
c('Karoubi recipient and entry',r'\deleted{\unsure{Swan|Singer|Switzer} papier Karoubi}','absent',r'\deleted{\unsure{Singer} papier Karoubi}','Half b and crop 162-1/005 (210,1585,400,1670): initial S and a descending g favor Singer; crossing obscures the central i/n strokes. Both name and title are cancelled.','omission','medium','H')
c('Bardach / Verdier entry',r'\unsure{Bardach|Bredach|Bredoch}; \deleted{Thèse Verdier}','absent',r'Bardach; \deleted{Thèse Verdier}','Crop 162-1/005 (210,1735,425,1810) and half b: Bardach has a clear B, a-r, d, a-c-h. The name is live; only Thèse Verdier has a horizontal strike.','omission','high','H')
c('Mumford entry','Mumford, sur équivalence rationnelle des 0-cycles','absent','Mumford, sur équivalence rationnelle des 0-cycles','Half b: entire uncancelled line beneath Thèse Verdier, including zero and hyphen.','omission','high','H')
c('Harder entry','Harder; Sém Bourbaki, avec exposé Deligne','absent','Harder; Sém Bourbaki, avec exposé Deligne','Half b: recipient and line sit immediately above the final crossed Artin title.','omission','high','H')
c('final Artin title','Artin : Algebraization of formal moduli I, II (struck)','absent','Artin : Algebraization of formal moduli I, II (struck)','Half b: full title, colon, of, comma and capped I/II visible beneath the cancellation.','omission','high','H')
for args in [
 ('top recipient','Husemöller','Husemöller without doubt','Name crop resolves the two l strokes and umlaut.'),
 ('top title','functor|functors','functors|functor retained doubtful','Final s lies in the cancellation; plural is favored but not certain.'),
 ('top second line','Picard|Picart; comm.','Picard comm. resolved','The d ascender and final abbreviated group survive in top-title crop.'),
 ('Saavedra recipient','Saavedra','resolved','Half a shows full surname despite the rule.'),
 ('Saavedra second line','Note|Notes','Note resolved','Half a has final e then spacing before sur; no separate s.'),
 ('brace ordinal','0ième|Oième|nième','0ième|Oième retained','Closed oval; no n humps; mathematical identification not forced.'),
 ('Raynaud / name','Popps|Popp','Popps resolved','Final s is separate in crop.'),
 ('Raynaud / index','pi_1|pi_r|pi_ell','pi_1|pi_r retained','Crop (1420,628,1605,703): sloping single hooked index, no closed ell loop.'),
 ('Hakim / tapis','tapis|topis|topos','tapis resolved','Crop (910,735,1245,805): dot over i and long p descender; no second o.'),
 ('Katz mark',',|apostrophe','apostrophe retained doubtful','High mark; its function remains unclear.'),
 ('Katz continuation','sol.|obs.; passage|pap.; de|du; fnd.|fond.','sol.; passage|pass.; de; fnd.|fond.','Crossing permits sol., obscures the end of passage; de has an e loop.'),
 ('Karoubi name','Swan|Singer|Switzer','Singer retained doubtful','Descending g favors Singer, but central strokes remain concealed.'),
 ('Bardach','Bardach|Bredach|Bredoch','Bardach resolved','Crop shows a-r and a-c, with final h.')]: certainty(p,*args)
for args in [
 ('top title','functors','functor','medium','Final s is merged with the cancellation.'),
 ('Chern first word','Classes','no secure full alternative','medium','Initial letters overlap the cancellation and adjacent loop.'),
 ('upper Picard abbreviation','gr.','polygr.','low','Descenders visible, but intervening letters are obscured.'),
 ('lower overwritten line','Rédaction; prégroupes; illegible 1','Réduction; polygr. groupes','low','Two writing layers and strikes merge; one word remains physically unreadable.'),
 ('brace ordinal','0^{ième}','O^{ième}','low','A closed oval with raised ième; no mathematical statement on this page decides its identity.'),
 ('Raynaud index','pi_1','pi_r','medium','Lower hooked stroke could be angular 1 or r.'),
 ('Katz mark','apostrophe','unidentified short stroke','low','Small high stroke partly crossed.'),
 ('Katz continuation','sol.; passage; fnd.','pass.; fond.','low','Crossing conceals endings and the f-initial abbreviation.'),
 ('Verdier title','Prenote','Prenotes','medium','No accent visible; the final stroke does not settle singular/plural.'),
 ('Karoubi recipient','Singer','no secure full alternative','medium','Only S and g are fully distinct through the crossing.')]:doubt(p,*args)
for kind,pos,txt in [
 ('deletion','top left','Husemöller'),('deletion','top right, line 1','Schlessinger, functors of Artin rings.'),('deletion','top right, line 2','Mes notes sur cat. de Picard comm.'),
 ('deletion','upper left','Saavedra'),('deletion','upper right, first line','Classes de Chern des représentations de groupes discrets'),('deletion','upper right, second line','Note sur cat. de Picard'),('insertion','above crowded third line','Notes sur gr. de Picard enveloppant d’une cat. triangulée'),('deletion','crowded upper line','Notes sur gr. de Picard enveloppant'),('deletion','under inserted line','Rédaction prégroupes [unreadable] en catégorie.'),('display','upper middle, brace','Notes Catégories de Picard / Notes pré-groupes et 0ième catégorie'),('deletion','brace, first line','Notes Catégories de Picard'),('deletion','brace, second line','Notes pré-groupes et 0ième catégorie'),('margin note','right of brace','Notes filtrations et groupes paraboliques'),('deletion','right of brace','Notes filtrations et groupes paraboliques'),
 ('text','middle upper, left and right','Mme Raynaud 1; Papiers de Horrocks'),('text','Raynaud second line','Papier de Popps (?) sur th. de Lefschetz etc pour pi_1'),('insertion','above Lefschetz','Zariski (circled, connector)'),('text','Raynaud third line','Deligne App. SGA 7 XXI'),('text','next entry','Mme Hakim 1; mes notes sur tapis Quillen I II'),
 ('deletion','centre lower, recipient','Katz and small mark'),('deletion','Katz first line','notes sur connexions et équations de Picard-Fuchs.'),('deletion','Katz second and third lines','notes sur torsion dans coh. cristalline, et sol. par passage de fnd. sur cohomologie évanescente'),('deletion','Katz final line','notes EGA V'),
 ('text','lower third','Verdier 1; Prenote Séminaire Hartshorne'),('deletion','below Verdier','Singer; papier Karoubi'),('text','below Karoubi, left','Bardach'),('deletion','beside Bardach','Thèse Verdier'),('text','Bardach second line','Mumford, sur équivalence rationnelle des 0-cycles'),('text','near foot','Harder; Sém Bourbaki, avec exposé Deligne'),('deletion','foot','Artin : Algebraization of formal moduli I, II')]: inventory(p,kind,pos,txt)
p['notation']=[['Roman bibliographic numerals','XXI, I, II and V have long cap/foot strokes; transcribed as overline/underline, not cancellation.'],['pi with low index','Raynaud line: pi_1 favored, pi_r retained; the index is not silently regularized.'],['Raised ordinal','Braced cancelled line: 0^{ième}|O^{ième}; not n^{ième}.'],['Source question mark','Popps (?) is an authorial question mark, distinct from editorial unsure marks.'],['Margin brace and connector','Brace groups the two Picard entries. Circled Zariski attaches at Lefschetz; its outline is an insertion cue, not a separate mathematical drawing.']]
p['hand']=[['Capped Roman numerals','All four numeral groups on this page are capped and footed; cancellation is an additional crossing line.','H mistakes XXI for struck text.'],['Looped p and dotted i in tapis','One occurrence here, before Quillen; clear long p descender and separate i dot.','C offered topis/topos; those alternatives are not supported here.'],['Highly compressed word middles under cancellation','Especially upper Picard block and Katz continuation; does not justify filling omitted letters.','C and H differ markedly; one lower word remains unreadable.'],['Names with a-r and a-c compressed','Bardach here shows a-r-d-a-c-h; comparison on later pages still required.','C offered Bredach/Bredoch; H omitted the entry.']]
p['abbreviations']=[['cat.','catégorie'],['comm.','commutative(s), probably'],['gr. / polygr.','groupe(s); longer alternative unresolved'],['th.','théorème'],['App.','appendice'],['SGA','Séminaire de géométrie algébrique'],['Mme','Madame'],['coh.','cohomologie'],['sol.','solution, probably'],['fnd. / fond.','fondamental, possibly; unresolved'],['EGA','Éléments de géométrie algébrique'],['Sém','séminaire'],['etc','et cetera']]
p['notes']=['Loan-register sheet: names at left and papers or notes at right. The entries range from Husemöller/Schlessinger through Harder/Artin; many are cancelled. Cancellation is recorded without asserting that a loan was returned.', 'The Raynaud entry carries the authorial (?) after Popps. The Picard ordinal and the index following pi do not occur in an argument that could settle their form; no theorem was used to replace their ink.', 'No title sheet, date, page count, or mathematical proof occurs here. The lower-left 4 is archive numbering, retained only as a TeX comment.']
save(p,tex)
print('Saved',p['filename'],len(p['changes']),'changes;',p['done'])
