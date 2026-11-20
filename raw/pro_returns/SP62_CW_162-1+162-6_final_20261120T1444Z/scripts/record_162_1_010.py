from records import *
p=page('162-1',10)
tex=r'''\scanpage{10}
\uline{Lascou}\qquad Borel-\unsure{Hirzebruch|Hirzebroch} $\overline{\underline{\mathrm I}}\ \overline{\underline{\mathrm {II}}}$

Borel thèse

Serre \unsure{Gèbres|Gèbrs}

Mazur\qquad Lettre à Serre corps \unsure{classe|class} local etc

\deleted{Notes Katz connexions ``intégrables''}

Quillen : Complex cobordism $+$ formal groups

Lettre de Barsotti

Rim SGA 7 $\overline{\underline{\mathrm{VII}}}$

Teissier\qquad 2 articles \unsure{Brieskorin|Brieskorn} rés. d'un morphisme.

\unsure{Fígeroa|Figeroa}\qquad Article Serre 1957

Fouzat\qquad Article Mumford $0$-cycles

\uline{Saavedra}\qquad \(\left.\begin{array}{@{}p{.58\linewidth}@{}}Groupes ${}^{1}\!/\!{}_{2}$ simples et esp. riem. sym.\\\rule{2em}{.35pt} et Algèbres de Lie\end{array}\right\vert\ \text{Bourbaki}\)

SGA 4 $\overline{\underline{\mathrm{IV}}}$

% archive sheet number: 9
\clearpage
'''
def c(place,C,H,F,S,K='misread word',conf='high',a='CH',m='no'):change(p,place,C,H,F,S,K,conf,a,m)
c('top recipient',r'\unsure{Lascou|Lascoux}','Lascoux','Lascou','Crop 162-1/010 (191,57,390,137): the terminal u ends in a single shallow rightward flourish; no separate x or pair of crossing strokes.','misread word','high','H')
c('Serre title',r'\unsure{Gèbres|Gèbrs|Gèbre}','Algèbre',r'\unsure{Gèbres|Gèbrs}','Crop 162-1/010 (781,180,964,248): the word begins with a single large G-like curve and è; no A/l prefix. A final s-like downturn is present; an intervening e is compressed.','misread word','medium','H')
c('Mazur / short description',r'corps \unsure{classe|class} local etc','corps de classes local etc.',r'corps \unsure{classe|class} local etc','Crop 162-1/010 (850,350,1136,419): blank between corps and the short class(e) group, with no de; no distinct extra plural s. Half a shows no terminal stop after etc.','text not on the page','medium','H')
c('Katz / quotation marks','``intégrables’’','« intégrables »','``intégrables’’','Half a: two detached upper strokes at each side of the word; no guillemet angles.','other','high','H')
c('letter author',r'\unsure{Barsotti|Barsatti}',r'Bass \ill','Barsotti','Crop 162-1/010 (770,515,963,577): B-a-r-s, rounded small o, two tall t strokes with a shared crossbar, then dotted i. No second unreadable word follows.','misread word','high','H','yes')
c('Teissier / author spelling',r'\unsure{Brieskorn|Brieskorin}','Brieskorn',r'\unsure{Brieskorin|Brieskorn}','Crop 162-1/010 (831,625,1055,706): a distinct dot stands over the low stroke between r and the final n-like downturn. It favors an additional i, but a displaced dot remains possible.','misread word','medium','CH')
c('Teissier / subject abbreviation','rés. d’un morphisme.',r'\ill d’un morphisme','rés. d’un morphisme.','Half a: r, accented é, s and stop are visible; another source point follows morphisme.','readable ink left as \\ill{}','high','H','yes')
c('Serre-1957 recipient',r'\unsure{Fígeroa|Figeroa}','Figueroa',r'\unsure{Fígeroa|Figeroa}','Crop 162-1/010 (227,752,435,844): the g goes directly into e-r-o-a, without u. The high stroke over i is long and slanted, so an accent/dot distinction is left open.','misread word','high','H')
c('Mumford / cycle degree','0-cycles','cycles','0-cycles','Half a: a closed oval 0 and short connecting hyphen precede cycles.','omission','high','H')
c('Saavedra / first title',r'Groupes 1/2 simples et esp. \unsure{riem.|riém.} sym.',r'Groupes \ill, champs de vecteurs symétriques','Groupes 1/2 simples et esp. riem. sym.','Halves a/b: raised 1, descending diagonal and lower 2 before simples; then et esp. and two abbreviated adjectives. Crop (1163,1000,1320,1068) shows a single high mark associated with i in riem., not a separate accent on e.','readable ink left as \\ill{}','high','H','yes')
c('Saavedra / second title and right label','repetition stroke et Algèbres de Lie; right rule and Bourbaki',r'\add{et} Algèbres de Lie \add{Bourbaki}','repetition stroke et Algèbres de Lie; right rule and Bourbaki','Half b: et is written at the same level as Algèbres; a long dash starts the line. A right vertical rule groups the two titles with Bourbaki, written over two lines at the right. These are source text and grouping, not supplied words.','insertion or placement','high','H')
c('underlines and source punctuation','Lascou and Saavedra underlined; no extra commas; Lettre capitalized','no recipient underlines; added commas in Borel/Serre/Katz/Rim/Mumford entries; lettre lower-case','source underlines, spacing and Lettre retained','Halves a/b: separate rules beneath the two recipient names; no comma dots at the indicated name/title gaps; tall looped L in Lettre de Barsotti.','other','high','H')
for a in [('Lascou','Lascou|Lascoux','Lascou','No final x.'),('Hirzebruch','Hirzebruch|Hirzebroch','retained','Crop (766,40,1042,138): medial vowel is looped and can be u or o.'),('Gèbres','Gèbres|Gèbrs|Gèbre','Gèbres|Gèbrs','Final s visible; compressed e remains uncertain.'),('classe','classe|class','retained','Terminal horizontal turn can be reduced e or the end of s.'),('Quillen','Quillen|Quilleu','Quillen','Half a: final n has a low return and descending exit.'),('Barsotti','Barsotti|Barsatti','Barsotti','Small oval after rs has no extra a stem.'),('Fígeroa','Fígeroa|Figeroa','retained','Long high stroke may be a dot made with a flick.'),('Fouzat','Fouzat|Fauzat','Fouzat','Half a: closed o with no a stem.'),('riem.','riem.|riém.','riem.','Only the i’s high mark; no separate acute over e.')]:certainty(p,*a)
for a in [('Borel collaborator','Hirzebruch','Hirzebroch','medium','Small medial vowel can be u or o.'),('Serre short title','Gèbres','Gèbrs','medium','Compressed ending after br.'),('Mazur short description','classe','class','medium','Weak terminal turn.'),('Teissier author','Brieskorin','Brieskorn','medium','Extra dot may signify i or be displaced.'),('Serre-1957 recipient','Fígeroa','Figeroa','medium','Long high i mark may be accent or dot.')]:doubt(p,*a)
for k,pos,t in [('text','top left','underlined Lascou'),('text','top right line 1','Borel-Hirzebruch I II'),('text','line 2','Borel thèse'),('text','line 3','Serre Gèbres'),('text','upper middle left','Mazur'),('text','Mazur line 1','Lettre à Serre corps classe local etc'),('deletion','Mazur line 2','Notes Katz connexions intégrables, double quotes'),('text','Mazur line 3','Quillen : Complex cobordism + formal groups'),('text','Mazur line 4','Lettre de Barsotti'),('text','Mazur line 5','Rim SGA 7 VII'),('text','middle','Teissier; 2 articles Brieskorin rés. d’un morphisme.'),('text','next entry','Fígeroa; Article Serre 1957'),('text','next entry','Fouzat; Article Mumford 0-cycles'),('text','lower left','underlined Saavedra'),('display','lower right grouped block','Groupes 1/2 simples et esp. riem. sym.; repetition stroke et Algèbres de Lie; right bar Bourbaki'),('text','last line','SGA 4 IV')]:inventory(p,k,pos,t)
p['notation']=[['Title conjunction','Complex cobordism + formal groups has an actual plus sign.'],['Half used as word','Small raised 1, slash, lower 2 before simples; retained as 1/2 rather than expanded to semi.'],['Repetition dash','Long horizontal beginning second Bourbaki title; not an omitted illegible word.'],['Roman numerals','I II, VII and IV all have upper and lower pen bars; no cancellation.'],['Zero cycles','Written 0 and short hyphen retained.']]
p['hand']=[['Name endings are not regularized','Lascou ends in u, and the Teissier title has a separate dot favoring Brieskorin. The latter remains doubtful.','H supplies Lascoux and regular Brieskorn; C preferred Brieskorn.'],['Long i dot versus accent','Fígeroa/Figeroa has a long high stroke; riem. has one high mark corresponding to i.','H supplies u in Figueroa; C’s riém. alternative is removed.'],['Half as abbreviated prefix','1/2 before simples is fully drawn; this occurrence supports semi only as an expansion in the apparatus.','H left the group illegible and supplied a different title.']]
p['abbreviations']=[['Gèbres','possibly shortened Algèbres; no prefix supplied'],['rés.','résolution'],['1/2 simples','semi-simples, interpretation of the written fraction'],['esp. riem. sym.','espaces riemanniens symétriques']]
p['notes']=['Final loan-list sheet in this selected part of cote 162-1, for Lascou, Mazur, Teissier, Fígeroa/Figeroa, Fouzat and Saavedra. The Katz connexions entry is cancelled; the other entries are live.', 'The source uses 1/2 in Groupes 1/2 simples and 0 in 0-cycles. Reading these small numerals restores what H omitted, but no mathematical proposition is being checked. The two Bourbaki titles share a right-hand grouping line; the second starts with a repetition dash.', 'Article Serre 1957 carries a bibliographic year, not a date of this sheet. Gèbres and the possible extra i in Brieskorin are preserved without normalization. Archive number 9; no page count or mathematical doubt attached to a proof.']
save(p,tex)
print('Saved',p['filename'],len(p['changes']),'changes;',p['done'])
