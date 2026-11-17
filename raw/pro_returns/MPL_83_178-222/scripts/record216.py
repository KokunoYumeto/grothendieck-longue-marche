import sys,re
sys.path.insert(0,'MPL_83_178-222/scripts')
from record_page import record
tex=r'''\scanpage{216}
\mspage{450}
(Ce n'est pas\inserted{certes,} la première fois\inserted{(ni la dernière que je suis ``\unsure{soufflé}'' )} dans cette brillante opération ``au service de la science''\inserted{...)}\deleted{\unsure{rôle}\illegible{5}}. J'apprends par sa lettre (datée du 15 février 85) que conformément \deleted{aux} ``à la façon habituelle d'agir quand un ouvrage contient des contributions de plusieurs auteurs'' (sic), il n'y avait pas lieu de s'adresser plus spécialement à moi, qui n'étais que \uline{directeur} du Séminaire ... \deleted{(}Les cinq ``auteurs'' de SGA 5 sont Bucur, Houzel, Illusie, Jouanolou, Serre, à l'exclusion de ma modeste personne, qui \deleted{ne} ne figure que comme ``directeur'' -- sans doute purement honorifique, en \deleted{ais}\inserted{avais}-je trop dit (*) -- pour ce brillant séminaire.

Dès avant de recevoir cette lettre instructive et trouvant le temps long (n'ayant rien reçu pendant un mois), j'ai pris ma plus belle plume (en allemand) pour écrire au Dr. K.F Springer en personne, \deleted{faisant}\inserted{lequel fait} partie des directeurs responsables de la maison Springer. Ça a été une belle \deleted{\unsure{lett}} lettre de deux pages machine, lui expliquant que j'étais bien peiné d'une longue série de désagréments dans ma relation à la maison Springer, et au delà de celles-ci, d'un certain nombre d'irrégularités grossières à mon égard, dont je me contentais pour le moment de lui soumettre deux, qui me paraissaient particulièrement flagrant\deleted{s}\inserted{es}: la publication de deux volumes des Lecture Notes (n\textsuperscript{o}s 288,589) parus sous mon nom et sans \deleted{aucun} juger nécessaire de me consulter. Que dans ces deux \deleted{cas}\inserted{textes}, les idées, méthodes et résultats que j'avais développés dans les séminaires oraux, étaient raccourcis ou mutilés parfois au point d'être méconnaissables. Que la coïncidence de ce dernier fait, \inserted{avec} \deleted{d}\inserted{l}es circonstances inhabituelles qui ont entouré la publication de ces deux volumes, ne pouvait être pour moi l'effet d'un pur hasard. Et que je m'attendais à des excuses publiques\deleted{, de la part} et sans réserve de la part de la maison\inserted{ }Springer, sous une forme qui serait à fixer d'un commun accord, une fois \deleted{que la question}\inserted{qu'un accord} de principe \deleted{était}\inserted{\unsure{serait}} acquis. Que j'espérais qu'il aurait à coeur comme moi de mettre fin à une situation déplaisante et inadmissible et de trouver une solution\unsure{n}qui soit à la hauteur des circonstances (``eine dem Fall geziemende Lösung zu finden'', ce qui \deleted{est} est même plus distingué encore), ``ho\deleted{\unsure{a}}chachtungsvoll'' (comme il se doit) signé de ma plus belle main.

Pour jouer cartes sur table, il me semble que j'ai joué cartes sur table ! Là il ne pourra pas dire, Monsieur K.F. Springer, qu'il \unsure{n'a} pas été informé personnellement de la situation, et de première main encore\deleted{\unsure{k}}\inserted{,} par nul autre que le principal intéressé lui-même!

Le hasard fait bien les choses: j'ai \deleted{\unsure{réçu|reçu}} fini par recevoir une réponse (un bon mois après\inserted{encore}) pas\inserted{\unsure{,}}plus tard que hier. C'est si court que je ne
\margin{215}
'''
e=[]
for m in re.finditer(r'\\(deleted|inserted|margin)\{',tex):
 d=1;i=m.end()
 while d and i<len(tex):
  if tex[i]=='{' and tex[i-1]!='\\':d+=1
  if tex[i]=='}' and tex[i-1]!='\\':d-=1
  i+=1
 e.append((m.start(),({'deleted':'deletion','inserted':'insertion','margin':'margin note'}[m.group(1)],'line '+str(tex[:m.start()].count('\n')+1),tex[m.end():i-1][:120] or 'space')))
for start in ['(Ce','Dès avant','Pour jouer','Le hasard']:
 p=tex.index(start);e.append((p,('text','paragraph',tex[p:p+90])))
e.append((0,('text','top centre','450')))
record(216,tex,[v for _,v in sorted(e)],
[('first paragraph heavy blackout','role plus about five unreadable words','original typed line examined enlarged at4x; dense black ink physically covers characters','low'),('blue top insertion','ni la derniere que je suis souffle','quotation word and parenthesis boundaries uncertain','medium'),('de principe correction','serait','blue s before typed etait; ending appears retained','medium'),('solutionnqui','n','extra type between solution and qui retained as uncertain','medium'),('German closing','ho[a]chachtungsvoll','overstruck extra character after ho','medium')],
['Typescript450 refers to a two-page typed letter in German; this is an internal page-count statement to record separately from supplied sheet count.','The translated response in scan214 follows this page in authorial order.','One heavily blacked-out typed passage cannot be recovered at enlarged inspection; retained partial doubtful reading plus estimated five-word illegibility.'],sheet_kind='reused_typed')
