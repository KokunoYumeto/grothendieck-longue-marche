import sys,re
sys.path.insert(0,'MPL_83_178-222/scripts')
from record_page import record
tex=r'''\scanpage{208}
\margin{447}
(*\deleted{*}) Les deux autres livres sont les thèses de Jean Giraud et de \deleted{Monique} Monique Hakim (sur le formalisme des champs et de la 1-cohomologie non commutative, et sur les schémas relatifs sur des topos annelés généraux).

\margin{448}
(*) Cette citation (traduite) est extraite de la courte lettre (adressée au Dr. Peters) du 18 février l'an dernier, où je l'informais de ma décision de me retirer de l'``editorial board'' des Grundlehren. Le Dr. Peters avait en fait quitté déjà le Springer Verlag (il travaille à présent dans le Birkhäuser Verlag), et la correspondance s'est continuée avec le \deleted{Dr.} Dr. J. Heinze, en charge des Grundlehren dans la maison Springer\deleted{ Verlag}. J'avais demandé\deleted{e} qu'une copie de ma lettre soit envoyée à chacun des co-éditeurs des Grundlehren (au nombre de dix-huit), et avais réitéré cette prière\deleted{,} au Dr Heinze\deleted{,} à deux reprises (en avril 84 et janvier 85) sans qu'il juge utile de me \deleted{dire} préciser si oui ou non elle avait été respectée (il \deleted{apparaît}\inserted{\unsure{est apparu}} que \uline{non}). J'ai pris la peine d'envoyer moi-même une copie de \unsure{ma|la} lettre \deleted{de démission, avec quelques mots d'explication,} à chacun des dix-huit éditeurs, avec quelques mots d'explication \deleted{\unsure{adressé}} au sujet de cet envoi. \deleted{\unsure{Parmi ces éditeurs j'en conn}}\inserted{Je} connais bien personnellement sept \unsure{parmi} \deleted{ces éditeurs,}\inserted{eux,} et \deleted{cinq entre eux} \deleted{je}\inserted{j'en} comptais\inserted{cinq} parmi mes amis. Un seul \deleted{\unsure{k}} (Artin) a pris la peine de me répondre, et aucun apparemment \unsure{n'a} rien trouvé d'anormal \deleted{\unsure{visà}} (ne serait-ce que vis-à-vis de \unsure{lui-même}) que la maison Springer n'ait pas\inserted{elle-même} pris la peine de lui faire parvenir \deleted{elle-même} \deleted{au mois} (et dès le mois de février 1984) la lettre en question.

(**\deleted{*}) Ce sont les volumes n\textsuperscript{os} 288,340, 569, 589, 900.

(***\deleted{*}) Comme je le précise dans l'avant-dernière note de b. de p., le Dr. Peters a depuis quitté\inserted{le} Springer Verlag pour Birkhäuser Verlag.

\margin{450}
(*) \deleted{Voir mes observations\inserted{\deleted{(p. \unsure{899})}} dans la sous-note ``Les double-sens -- ou l'art de l'arnaque'' (n° \unsure{169_7|169_2}), concernant} \inserted{Dans} le fameux ``Fil d'Ariane'' \deleted{\unsure{à travers SGA}}\inserted{(à travers SGA 4 etc)} dans le volume nommé `` SGA $4\frac12$ '', \deleted{\unsure{où}} rien ne pourrait laisser supposer au lecteur que j'aie eu l'honneur de faire des exposés dans SGA 4 et SGA 5 (par contre, j'ai\inserted{bien} eu celui de ``collaborer'' à ``SGA $4\frac12$ '' ...).
\inserted{Voir à ce sujet mes observations dans la note ``Les double-sens -- ou l'art de l'arnaque'' (n° \unsure{169_2|167_2}), p. 899.}

\margin{\unsure{452|451}}
(*) J'ai songé d'ailleurs aussi qu'il se pourrait bien que la situation se renverse, et que ce soit l'estimable entreprise qui m'intente un procès, pour atteinte à sa réputation. \deleted{J'imagine que} \deleted{c}\inserted{C}es gens ``au service de la \deleted{s}\inserted{S}cience'', ils doivent être pointilleux sur ce chapitre \deleted{\unsure{--}} \inserted{(}du moment que c'est de \uline{leur} \deleted{propre} réputation qu'il s'agit ...\inserted{)}.

\margin{452}
(*) Cette idée-force de bâtir des ``maisons'', et qui soient bonnes ``pour tous'', a joué un rôle considérable dans mon oeuvre mathématique, et ceci depuis le début des années cinquante déjà. Cela a été l'expression \unsure{concrète} \deleted{de \unsure{la pulsion de}}\inserted{dans mon travail de} ce que j'ai appelé la ``pulsion de service'' \deleted{en moi}, qui a fait partie (sans même que je la décèle avant la réflexion ``La clef du yin et du yang'') des \deleted{\unsure{motivations profon}} forces profondes donnant leur force \unsure{vive} à mon travail mathématique. L'archétype de la ``maison'' apparaît pour la première fois dans ma réflexion, \deleted{et avec} sans que je\inserted{ne} l'aie \deleted{\unsure{entrev}} \unsure{pressenti}, et avec une grande force, dans la note\inserted{(du 26 novembre)} ``Yin le serviteur, et les nouveaux maîtres'' (n° 135).
\margin{207}
'''
items=[]
for m in re.finditer(r'\\(deleted|inserted|margin)\{',tex):
 depth=1;i=m.end()
 while depth and i<len(tex):
  if tex[i]=='{' and tex[i-1]!='\\':depth+=1
  if tex[i]=='}' and tex[i-1]!='\\':depth-=1
  i+=1
 kind={'deleted':'deletion','inserted':'insertion','margin':'margin note'}[m.group(1)]
 items.append((m.start(),(kind,'text line '+str(tex[:m.start()].count('\n')+1),tex[m.end():i-1][:120])))
for m in re.finditer(r'(?m)^\(',tex):items.append((m.start(),('text','paragraph beginning line '+str(tex[:m.start()].count('\n')+1),tex[m.start():m.start()+105])))
record(208,tex,[v for _,v in sorted(items)],
[('448, parenthesis il apparait','est apparu','blue overtyping of word ending and marginal est; exact final verb uncertain','medium'),('448, deleted type under Je','Parmi ces editeurs j en conn','typewriter x-overstrike obscures terminal partial word','low'),('450, note number','169_7;169_2','last digit and lowered final digit uncertain; handwritten alternative167_2','low'),('452, right edge','concrete;vive;pressenti','rightmost letters cut by photocopy edge; readings marked in text','medium'),('452, x-overstruck words','la pulsion de;motivations profon;entrev','partial underlying type remains but terminal letters not secure','low')],
['Reused typescript with notes keyed447,448,450,451/452,452; these are reference numbers, not 43-page package counts.','Mentions theses of Jean Giraud and Monique Hakim, Grundlehren editorial resignation, five numbered volumes, SGA4 1/2 Fil d Ariane, house-building metaphor and Yin le serviteur n135. These are authorial historical assertions, not independently checked.'],sheet_kind='reused_typed')
