import sys,re
sys.path.insert(0,'MPL_83_178-222/scripts')
from record_page import record
tex=r'''\scanpage{218}
\mspage{L 21}
quand ce n'était celui du dédain (``délicatement dosé''), de la dérision ou du mépris, que ce soit vis-à-vis de moi (parfois) ou (surtout) vis-à-vis de ceux qui avaient osé s'inspirer de moi (sans se douter, certes, de ce qui les attendait) et qui étaient ``classés'' comme ayant partie liée à moi, par quelque décret tacite et implacable. Et à nouveau je vois apparaître ici le lien ``évident'' et profond, entre le r\enspace e\enspace s\enspace p\enspace e\enspace c\enspace t (ou l'absence de respect) pour la personne d'autrui, celui pour l'acte de création et pour certains de ses fruits \deleted{parmi} les plus délicats et les plus essentiels, et enfin le respect pour les règles les plus évidentes de l'éthique scientifique, celles qui s'enracinent dans un respect élémentaire de soi et d'autrui et que je serais tenté d'appeler les ``r\enspace è\enspace g\enspace l\enspace e\enspace s\quad d\enspace e\quad d\enspace é\enspace\unsure{c}\enspace e\enspace n\enspace c\enspace e'' dans l'exercice de notre art. \inserted{Ce sont là autant d'aspects, sûrement, d'un élémentaire et essentiel ``\uline{respect de soi}''.} Si j'essaie, en une seule formule lapidaire\inserted{,} de faire le bilan de ce que m'a enseigné Récoltes et Semailles au sujet d'un certain monde qui fut le mien, un monde auquel je m'étais identifié pendant plus de vingt ans de ma vie, je dirais: c'est un monde qui a p\enspace e\enspace r\enspace d\enspace u\quad l\enspace e\quad r\enspace e\enspace s\enspace p\enspace e\enspace c\enspace t (*).

C'était là une chose déjà fortement sentie, sinon formulée, dès les années qui avaient précédé. Elle n'a fait que se confirmer et se préciser\inserted{,} de façon \deleted{souvent} imprévue toujours et parfois stupéfiante, tout au cours de Récoltes et Semailles. Elle est clairement apparente dès le moment déjà où une réflexion de nature ``philosophique'' et générale devient soudain un témoignage personnel, dans la section ``L'étranger bienvenu'' (n° $9\deleted{\unsure{5}}$, p. 18) ouvrant le chapitre déjà cité ``Naissance de la crainte''\deleted{)}.

Cette perception n'apparaît pourtant pas sur le ton de la récrimination acerbe ou amère, mais (par la logique interne de l'écriture et par l'attitude différente que celle-ci suscite) sur celui d'une i\enspace n\enspace t\enspace e\enspace r\enspace r\enspace o\enspace g\enspace a\enspace t\enspace i\enspace o\enspace n : quelle a été ma propre part dans cette dégradation, dans cette perte du respect que je constate aujourd'hui ? C'est là l'interrogation principale qui traverse et porte cette première partie de\margin{\unsure{(!)}} Récoltes et Semailles, jusqu'au moment où elle se résoud finalement en une constatation claire et sans équivoque (**). Auparavant, cette dégradation m'était apparue comme ``tombée du ciel'' soudain, de façon inexplicable et d'autant plus outrageuse, intolérable. Au cours de la réflexion, je découvre qu\deleted{e}\inserted{'} \deleted{cette}\inserted{elle} \deleted{dégradation} s'était \deleted{déjà} poursuivie insidieusement, sans que personne sûrement ne la décèle autour de lui ni en lui-même, tout au \deleted{cours}\inserted{long} des années cinquante et soixante, y\quad c\enspace o\enspace m\enspace p\enspace r\enspace i\enspace s\quad d\enspace a\enspace n\enspace s\quad m\enspace a\quad p\enspace r\enspace o\enspace p\enspace r\enspace e\quad p\enspace e\enspace r\enspace s\enspace o\enspace n\enspace n\enspace e.

\deleted{\unsure{Cette constat}} La constatation de cet humble fait,\inserted{bien} évident sûrement
\margin{217}
'''
e=[]
for m in re.finditer(r'\\(deleted|inserted|margin)\{',tex):
 d=1;i=m.end()
 while d and i<len(tex):
  if tex[i]=='{' and tex[i-1]!='\\':d+=1
  if tex[i]=='}' and tex[i-1]!='\\':d-=1
  i+=1
 e.append((m.start(),({'deleted':'deletion','inserted':'insertion','margin':'margin note'}[m.group(1)],'line '+str(tex[:m.start()].count('\n')+1),tex[m.end():i-1][:120])))
for start in ['quand ce','C\'était là','Cette perception','La constatation']:
 p=tex.index(start);e.append((p,('text','paragraph',tex[p:p+90])))
e.append((0,('text','top centre','L21')))
record(218,tex,[v for _,v in sorted(e)],
[('decence','c','blue blot over first c; remaining letterform uncertain','medium'),('section reference','9 with deleted5','blue crossing could instead correct underlying digit to5','low'),('right margin next to premiere partie','(!)','small dark mark resembles parenthesized exclamation; possible copy blemish','low'),('last cancelled text','Cette constat','typewriter x-overstrike over unfinished clause','low')],
['L21 describes loss of respect and authorial self-implication; continues into supplied L22 scan212.','Titles L etranger bienvenu and Naissance de la crainte, section9/95 and p18, are internal references, not this package title or count.','Typed resoud retained without final t, as visible.'],sheet_kind='reused_typed')
