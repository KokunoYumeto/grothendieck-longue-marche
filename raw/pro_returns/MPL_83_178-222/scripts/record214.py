import sys,re
sys.path.insert(0,'MPL_83_178-222/scripts')
from record_page import record
tex=r'''\scanpage{214}
\mspage{451}
résiste pas à la tentation de la reproduire ici\inserted{(traduite)} in extenso\inserted{.}\deleted{\unsure{--}} \deleted{i}\inserted{I}l m'a fallu un moment, d'ailleurs, pour saisir que c'\deleted{\unsure{e}}était bel et bien une réponse à ma belle lettre \deleted{\unsure{d'il y avait}} du mois dernier\deleted{\unsure{;}}\inserted{. Voici donc la réponse.}

\begin{flushright}Heidelberg 15.3.1985\end{flushright}
\deleted{``}Cher Professeur Grothendieck,

Il me faut encore vous remercier pour votre lettre du 9 février. La lettre de Mme Dr. Byrne du 15 février aura sans doute répondu à vos questions.

\unsure{Recevez} etc
\begin{flushright}K.F. Springer\deleted{''}\end{flushright}

Là au moins je suis fixé ! Les gens ``bien informés'' (dont il a été déjà question) ont dû lui expliquer que c'était pas la peine qu'il se fatigue pour le Monsieur un peu excité qui lui écrivait là -- qu'il\deleted{\unsure{b}} ne faisait décidément pas partie du beau monde. Et c'est vrai, en plus ...

En attendant de recevoir cette réponse édifiante de la direction de l'entreprise de Pompes Funèbres Springer Verlag GmbH (c'était gentil encore de m'honorer d'une réponse \deleted{personelle}\inserted{signée} du directeur en personne), j'ai eu le temps de me sonder sur mes propres intentions. Le rôle joué par l'estimable entreprise me paraît vraiment très gros, et j'ai songé à l'éventualité d'un procès à grand spectacle, où je demanderais des dommages-intérêts astronomiques, à titre de ``monsieur bien''\inserted{ }outragé, \deleted{et} victime d'inqualifiables passes\deleted{\unsure{x}}-droits. Mais je me suis dit aussi \deleted{\unsure{que de tels pro}} qu'un procès comme ça, ça doit bouffer une énergie\inserted{ }dingue. A supposer même que j'aie gain de cause et que je touche des dommages-intérêts vertigineux (soyons optimistes!)\inserted{,} au bout de X années\deleted{,}\inserted{civils,} -- à quoi serais-je avancé ? Je ne suis pas dans le besoin et n'ai nul besoin de plus que ce que j'ai -- et une escroquerie n'est pas plus ni moins une escroquerie, parce qu'un certain procès a été gagné, ou perdu. Je ne vais pas améliorer le monde, ni moi-même, ni les manières de Monsieur K.F. Springer et de certains employés de l'entreprise qu'il dirige, et en tous cas pas leur\deleted{s} façon de concevoir leur métier\inserted{,} en mobilisant des avocats et en \deleted{le}\inserted{leur} faisant mobiliser les leurs\inserted{(*)}. \deleted{\unsure{Par contre, dans les années qui m}} Et je n'améliorerai pas non plus un certain esprit dans un certain beau monde que j'ai quitté, \deleted{un}\inserted{l'} esprit qui rend possible le genre d'opération dont le Dr. Springer et son estimable \deleted{entre} maison se sont\inserted{faits (depuis \unsure{treize|douze} ans) \deleted{\unsure{déjà}}} les serviteurs. Il me reste (je l'espère bien) quelques
\margin{213}
'''
e=[]
for m in re.finditer(r'\\(deleted|inserted|margin)\{',tex):
 d=1;i=m.end()
 while d and i<len(tex):
  if tex[i]=='{' and tex[i-1]!='\\':d+=1
  if tex[i]=='}' and tex[i-1]!='\\':d-=1
  i+=1
 e.append((m.start(),({'deleted':'deletion','inserted':'insertion','margin':'margin note'}[m.group(1)],'line '+str(tex[:m.start()].count('\n')+1),tex[m.end():i-1][:120] or 'space')))
for start in ['résiste','Heidelberg','Cher Professeur','Il me faut','Recevez','K.F. Springer','Là au moins','En attendant']:
 p=tex.index(start);e.append((p,('text','text block',tex[p:p+90])))
e.append((0,('text','top centre','451')))
record(214,tex,[v for _,v in sorted(e)],
[('first paragraph deletion','d il y avait','x-overstrike; letters d il y avai visible','low'),('letter salutation close','Recevez','v/g overprint','medium'),('after X annees','civils','handwritten word could be civils or civles; first reading from strokes','low'),('last insertion','faits (depuis treize ans) deja','number word and final heavily cancelled word uncertain','low'),('deleted clause before Et je','Par contre, dans les annees qui m','partial clause cut by right margin and x-overstrike','low')],
['Typescript451 contains author-translated letter attributed to K.F.Springer, Heidelberg15.3.1985, and reflection on legal action. This is primary text on the supplied sheet, not verification of correspondence history.'],sheet_kind='reused_typed')
