import sys,re
sys.path.insert(0,'MPL_83_178-222/scripts')
from record_page import record
tex=r'''\scanpage{220}
\margin{\unsure{1}}
\mspage{L 20}
\deleted{par des épithètes} comme ``vaseux'', ``mou'', ``inconsistant'' -- ou au bout opposé\inserted{comme} ``trivialités'', ``enfantillage'', ``\unsure{bonbinage|bombinage}'' ...), mais où sera extirpé également ce travail même et ses fruits: celui où sont conçues, s'élaborent et naissent les notions et les visions nouvelles. Ce sera l'époque aussi où l'exercice de notre art sera réduit à d'arides et vaines voltiges de ``poids et haltères'' cérébraux, aux surenchères des prouesses pour ``craquer'' les problèmes au concours (``de difficulté proverbiale'') -- l'époque d'une hypertrophie ``supermacho'' fiévreuse et stérile, prenant la suite de plus de trois siècles de renouvellement créateur.

\inserted{7.} Mais à nouveau je digresse, en anticipant sur ce que la réflexion m'a enseigné. \deleted{Je}\inserted{J'étais} part\deleted{ais}\inserted{i} d'un double propos\inserted{,} clairement présent en moi dès avant même les débuts de celle-ci: le propos d'une ``déclaration d'intentions'', et (intimement lié à celui-ci, comme il vient d'apparaître) celui de m'exprimer au sujet de la nature du travail créateur. Il y avait pourtant un troisième propos encore, moins clairement présent sûrement au niveau conscient, mais répondant à un besoin \unsure{pbus|plus} profond et plus essentiel. Il était suscité par ces ``interpellations'' parfois déconcertantes, me \unsure{pervenant|parvenant} de mon passé de mathématicien par la voix de ceux qui avaient été mes élèves ou mes amis\unsure{(} (ou \deleted{les deux}\inserted{du moins}, de \deleted{certains}\inserted{bon nombre} d'entre eux). Au niveau épidermique, ce besoin se traduisait par une envie de ``vider mon sac'', de dire quelques ``vérités déplaisantes''. Mais plus profondément, sûrement, il y avait le besoin de \deleted{faire} f\enspace a\enspace i\enspace r\enspace e\quad c\enspace o\enspace n\enspace n\enspace a\enspace i\enspace s\enspace s\enspace a\enspace n\enspace c\enspace e enfin avec un certain passé, que j'avais choisi jusque là d'éluder. C'est de ce besoin-là, avant tout, qu'est \deleted{né}\inserted{issu} Récoltes et Semailles. Cette longue réflexion a été ma ``réponse'', au jour le jour, à cette pulsion de connaissance en moi, et à l'interpellation sans cesse renouvelée qui me venait du monde extérieur, du ``monde mathématique'' que j'avais quitté sans esprit de retour. Mais à part les toutes premières pages de ``Fatuité et Renouvellement''\deleted{,}\inserted{(}celles qui en forment les deux premiers chapitres ``Travail et découverte'' et ``Le rêve et le Rêveur''\inserted{)}, et dès le chapitre qui enchaîne ``Naissance de la crainte'' (p. 18), avec un ``témoignage'' qui n'était nullement prévu au programme, c'est ce besoin de faire connaissance de mon passé et de l'assumer pleinement, qui (je crois) a été la force principale en oeuvre dans l'écriture de Récoltes et Semailles.
\deleted{Récoltes et Semailles}

L'interpellation qui m'était venue du monde des mathématiciens, et qui revenait sur moi avec une force nouvelle tout au cours \deleted{de l'écriture} de Récoltes et Semailles (et surtout,\inserted{au cours} de l' ``enquête'' poursuivie dans les parties II et IV) avait pris d'emblée le masque de la suffisance,
\margin{219}
'''
e=[]
for m in re.finditer(r'\\(deleted|inserted|margin)\{',tex):
 d=1;i=m.end()
 while d and i<len(tex):
  if tex[i]=='{' and tex[i-1]!='\\':d+=1
  if tex[i]=='}' and tex[i-1]!='\\':d-=1
  i+=1
 e.append((m.start(),({'deleted':'deletion','inserted':'insertion','margin':'margin note'}[m.group(1)],'line '+str(tex[:m.start()].count('\n')+1),tex[m.end():i-1][:120])))
for start in ['comme ``vaseux','Mais à nouveau','L\'interpellation']:
 p=tex.index(start);e.append((p,('text','paragraph',tex[p:p+90])))
e.append((0,('text','top centre','L20')))
record(220,tex,[v for _,v in sorted(e)],
[('first paragraph quoted word','bonbinage','middle character resembles n, alternative m; no normalization','medium'),('second paragraph','pbus;pervenant','typed letterforms retained with possible alternatives plus;parvenant','medium'),('after amis','two opening parentheses','first weak parenthesis may be copy impression','low'),('top isolated mark','1','short rotated mark above typescript, identity uncertain','low')],
['Manuscript section7 is handwritten into reused typescript L20. Titles Fatuité et Renouvellement, Travail et découverte, Le rêve et le Rêveur, Naissance de la crainte and references to partsII/IV are explicit.','This L20 continues scan196 L19 and precedes scan218 L21 in authorial order, though scan order is preserved.'],sheet_kind='reused_typed')
