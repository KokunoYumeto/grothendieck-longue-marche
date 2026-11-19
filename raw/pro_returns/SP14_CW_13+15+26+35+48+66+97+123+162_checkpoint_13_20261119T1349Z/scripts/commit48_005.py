import sys
sys.path.insert(0,'out/scripts')
from work import commit
R=[
(r'\unsure{schémas}',r'schémas'),
(r'\unsure{parabeliens|parabéliens|paraabeliens|paraabéliens}',r'\unsure{parabeliens|parabéliens}'),
(r'\unsure{gpes|groupes}',r'gpes'),
(r'\unsure{Chevalley}',r'Chevalley'),
(r'\deleted{\unsure{F|D}}\unsure{D|F}',r'\deleted{\unsure{F|D}}D'),
(r'\uline{torseurs sous gpes classiques}',r'\uline{torseurs} \uline{sous gpes classiques}'),
(r'\unsure{où|ou}',r'où'),
(r'\unsure{isotrivialité}',r'isotrivialité'),
(r'\unsure{(?)|(!)|(P.)}',r'\unsure{(P.)|(?)}'),
(r'\unsure{Néron|Neron}',r'Néron'),
(r'\unsure{paragraphe}',r'paragraphe'),
(r'\unsure{variations}',r'variations'),
(r'\noindent Réf\quad',r'\noindent \unsure{Ref|Réf}\quad'),
(r'\draw (n.center) ellipse (1.08em and 1.13em);',r'\draw (n.center) ellipse (1.08em and 1.13em);\draw ([xshift=-1em,yshift=-.35em]n.center) .. controls ([xshift=-1.04em,yshift=.75em]n.center) and ([xshift=-.30em,yshift=1em]n.center) .. ([xshift=.35em,yshift=.96em]n.center);')]
L=[]
def a(p,c,h,f,ink,conf='high',ac=False,ah=True,k='other',mh='no',cons=None):
 d=dict(place=p,c=c,h=h,final=f,ink=ink,confidence=conf,against_c=ac,against_h=ah,kind=k,marked_in_H=mh)
 if cons:d['consequential']=cons
 L.append(d)
a('first D enclosure','two ovals','(D)','two ovals and extra upper-left arc','dlabel 8x: two enclosing loops, with another rising left stroke returning across the upper part.','high',True,True,'drawing or diagram')
a('first heading, schémas',r'\unsure{schémas}','schémas','schémas','title6x: initial s/c, tall h, accented e and m/a/s are traceable.','medium',True,False)
a('first heading, abéliens',r'\unsure{abéliens|abeliens}','abéliens',r'\unsure{abéliens|abeliens}','abel1 12x: a/b and compressed e join the tall l; i dot is clear, but an independent acute cannot be securely separated from the retraced b/e.','low',False,True,'misread word')
a('first heading, last word',r'\unsure{parabeliens|parabéliens|paraabeliens|paraabéliens}','polarisations',r'\unsure{parabeliens|parabéliens}','titlefinal 12x: p descender, a/r/a, b ascender, e/l/i/e/n/s; one a before b, with uncertain accent. No polarisation sequence.','medium',True,True,'misread word',cons='The first rubric ends with parabeliens/parabéliens, not polarisations.')
a('first heading rules','three underlined stretches','no rules','three underlined stretches','title6x: separate rules below Propriétés générales des, schémas abéliens, and et parabeliens.','high',False,True,'drawing or diagram')
a('below first heading','five vertical dots','omitted','five vertical dots','firstdots12x: five distinct small points form a short vertical run.','high',False,True,'omission')
a('first E enclosure','double oval','(E)','double oval','elabel9x: two elongated enclosing loops around the letter, with retracing.','high',False,True,'drawing or diagram')
a('Extensions heading, abéliens',r'\unsure{abéliens|abeliens}','abéliens',r'\unsure{abéliens|abeliens}','abel2 12x: b/e are compressed and partly retraced; clear l and i dot do not decide a separate acute.','low',False,True,'misread word')
a('Extensions heading, abbreviation',r'\unsure{gpes|groupes}','groupes','gpes','extension6x: g loop and p descender followed directly by e/s; r/o/u are not written.','medium',True,True,'abbreviation expanded or spelling modernised')
a('Extensions heading, adjective','affines','finis','affines','extension6x: a precedes two long f stems, then dotted i/n/e/s.','high',False,True,'misread word',cons='Extensions are by gpes affines, not groupes finis.')
a('Extensions heading, rule','underline','no rule','underline','extension6x: one long line runs below the complete heading.','high',False,True,'drawing or diagram')
a('parenthetical theorem name',r'\unsure{Chevalley}',r'\uncertain{\ill}','Chevalley','chevalley9x: C/h/e/v/a, two tall l stems, e and descending y remain readable.','medium',True,True,r'readable ink left as \ill{}','yes')
a('parenthetical theorem punctuation','four dots, then close parenthesis and period','ellipsis, close parenthesis; no final period','four dots, then close parenthesis and period','chevalley9x: four separate points follow y; another point follows the closing parenthesis.','high',False,True,'omission')
a('below second heading','five vertical dashes','omitted','five vertical dashes','seconddashes12x: five short vertical strokes with intervening blank intervals.','high',False,True,'omission')
a('third rubric, former letter',r'\deleted{\unsure{F|D}}','omitted',r'\deleted{\unsure{F|D}}','thirdlabel10x: a medial horizontal arm remains within the round D; the earlier letter is obscured by the thick common stem and lower stroke.','low',False,True,'omission')
a('third rubric, live letter',r'\unsure{D|F}','D','D','thirdlabel10x: large dark closed right bowl meets the stem at top and bottom.','medium',True,False)
a('third rubric enclosure','double oval','described in note','drawn double oval','thirdlabel10x: two complete ovals around the overlaid letters.','high',False,True,'drawing or diagram')
a('boxed insertion wording','Groupes classiques et',r'Groupes de \ill','Groupes classiques et','torseurs7x: Groupes followed by c/l/a/s/s/i/q/u/e/s and e/t; all are legible.','high',False,True,r'readable ink left as \ill{}','yes')
a('boxed insertion state and anchor','live insertion before torseurs','struck phrase before Torseurs','live insertion before torseurs','torseurs7x: surrounding line follows the outside of the words and leads down to the left of torseurs; no cancellation crosses the letter bodies.','high',False,True,'deletion state (struck given live or live given struck)',cons='Groupes classiques et is a live boxed insertion, not withdrawn text.')
a('insertion box and leader','box and leader drawn','omitted drawing','box and leader drawn','torseurs7x: rounded upper enclosure and long lower rule; left end bends down beside torseurs.','high',False,True,'drawing or diagram')
a('torseurs, initial case','torseurs','Torseurs','torseurs','torseurs7x: long crossed t stem turns into a low foot before o, unlike capital T.','high',False,True,'misread word')
a('torseurs heading abbreviation',r'\unsure{gpes|groupes}','gr.','gpes','torseurs7x: g loop, long p and compact e/s are visible without terminal point.','medium',True,True,'misread word')
a('torseurs heading underline','one continuous underline','no rule','two underline stretches','torseurs7x: first rule below torseurs reaches near sous, then a short interruption precedes the longer rising rule beneath sous gpes classiques.','high',True,True,'drawing or diagram')
a('right marginal note, initial case',"N'importe","n'importe","N'importe",'nimporte10x: tall capital N starts the parenthesized note at right.','high',False,True,'misread word')
a('right marginal note, accent',r'\unsure{où|ou}','où','où','nimporte10x: short dark accent stroke stands over the final compressed vowel.','medium',True,False)
a('theorem continuation','de l’isotrivialité with doubt','d’irréductibilité',"de l'isotrivialité",'isotriv8x: de then separate l/apostrophe; i/s/o/t/r/i/v/i/a/l/i/t/é follow, with the tall t/l stems and final acute visible.','medium',True,True,'misread word',cons='The continuation names the theorem of isotriviality, not irreducibility.')
a('theorem continuation, condition','sur un corps',r'\ill','sur un corps','isotriv8x: s/u/r, u/n, then c/o/r/p/s are visible, including the descending p.','high',False,True,r'readable ink left as \ill{}','yes')
a('end after corps',r'\unsure{(?)|(!)|(P.)}','(P.)',r'\unsure{(P.)|(?)}','isotrivend15x: left parenthesis joins a tall looped stem with right bowl, followed by a point. P. is favoured; a looped question mark remains possible. No separate exclamation stem.','low',True,True,'misread symbol or index')
a('end of theorem continuation','period','no period','period','isotrivend15x: a detached dark dot follows the closing parenthesis.','high',False,True,'omission')
a('fourth rubric, overlaid letters',r'\deleted{\unsure{E|F}}\unsure{F|E}','E',r'\deleted{\unsure{E|F}}\unsure{F|E}','lastlabel10x: top arm, doubled lower arm and projecting vertical stem show overlaid E/F strokes; sequence remains indeterminate. Both layers retained with doubt.','low',False,True,'omission')
a('fourth rubric enclosure','two ovals','described in note','two drawn ovals','lastlabel10x: thin outer oval and heavily retraced inner oval enclose the letter layers.','high',False,True,'drawing or diagram')
a('Modèles de name',r'\unsure{Néron|Neron}','Néron','Néron','neron10x and neronaccent16x: large N, open e with a separate raised accent stroke to its right, then r/o/n.','medium',True,False)
a('lower paragraph noun',r'\unsure{paragraphe}','paragraphe','paragraphe','paragraph7x/paragraphe14x: initial p, low a/r/a, g descender, r/a/p and tall h with e exit can be followed.','medium',True,False)
a('lower paragraph, variations',r'\unsure{variations}','variantes,','variations','variations12x: low v/a/r, dotted i, a, crossed t, second i and o/n/s; no detached comma after s.','medium',True,True,'misread word')
a('lower paragraph, connective','sur le','avec le','sur le','paragraph7x: s/u/r followed by a separate tall looped l and low e.','high',False,True,'misread word')
a('theorem article',r'\unsure{du|des}','des',r'\unsure{du|des}','carre12x: d loop enters a heavy low joined stroke with two humps and final hook; u favoured, e/s not securely excluded.','low',False,True,'misread word')
a('theorem noun','carré','carrés','carré','carre12x: c/a/r/r/é with short acute; no s between final e and closing quotes.','high',False,True,'misread word')
a('theorem quotation marks','paired raised quotes','guillemets','paired raised quotes','carre12x: two curved strokes above-left of th. and two above-right of carré, not angle-shaped guillemets.','high',False,True,'misread symbol or index')
a('lower paragraph end','question mark',r'\ill','question mark','carre12x: descending curved hook and separate lower dot at far right after closing quotation marks.','high',False,True,r'readable ink left as \ill{}','yes')
a('references heading','Réf','Réf.',r'\unsure{Ref|Réf}','refaccent13x: e has a tall returning curl but no securely detached accent; no period appears beyond the long f. Accent newly marked uncertain.','low',True,True,'misread word')
a('Boulder quotes','paired raised quotes','guillemets','paired raised quotes','refs7x: paired high curved marks on each side of Boulder; no angular guillemets.','high',False,True,'misread symbol or index')
I=[]
def i(k,p,t):I.append(dict(kind=k,position=p,text=t))
i('text','first rubric','D; Propriétés générales des schémas abéliens/abeliens et parabeliens/parabéliens')
i('drawing','first D','two enclosing ovals and additional upper-left arc')
i('drawing','first rubric','three stretches of underline')
i('drawing','below first rubric','five vertically aligned dots')
i('text','second rubric','E; Extensions des schémas abéliens/abeliens par gpes affines')
i('drawing','first E','two ovals')
i('drawing','second rubric','long underline')
i('text','below second rubric','(th. de Chevalley....).')
i('drawing','below second rubric','five vertical dashes')
i('deletion','third rubric label','former F/D')
i('insertion','third rubric label','replacement D')
i('drawing','third rubric label','two ovals')
i('insertion','above torseurs','Groupes classiques et')
i('drawing','above/beside torseurs','rounded box and leader ending before torseurs')
i('text','third rubric','torseurs sous gpes classiques')
i('drawing','third rubric','underline with short interruption near sous')
i('marginnote','right of third rubric',"(N’importe où)")
i('text','third rubric continuation',"et théorème de l’isotrivialité sur un corps (P.)/(?).")
i('deletion','fourth rubric label','former E/F')
i('insertion','fourth rubric label','replacement F/E')
i('drawing','fourth rubric label','two ovals, inner heavily retraced')
i('text','fourth rubric','Modèles de Néron (?)')
i('text','lower question','Un paragraphe de variations sur le “th. du/des carré”?')
i('text','references heading','Ref/Réf')
for n,t in enumerate(['SGAD','BIBLE','``Boulder\'\'','Livre(s) Mumford'],1):i('text','reference'+str(n),t)
commit(48,5,dict(replace=R,changes=L,inventory=I,sheet_kind='text',hand='his hand',observations='Whole scan and both supplied halves personally viewed before witnesses. All 18 base crops and six further crops inspected. Faint reversed typescript is show-through, not an additional text on this face. No watermark visible on this page. Pencil archive number 4 retained only in comment. Uncertain letter layers and accents are not harmonised to the headings or bibliography.'))
