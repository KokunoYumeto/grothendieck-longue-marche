from pathlib import Path
import re
from record_page import commit, change
t=Path('/workspace/scratch/c6b7a14fa47f/source/SP32_CW_156-3_witnesses/codex/J156-3-05/pages/J156-3-05_156-3_scan038.tex').read_text()
t=t.replace(r'\unsure{mor\textsuperscript{t}|moral\textsuperscript{t}|ess\textsuperscript{t}}',r'mor\textsuperscript{t}').replace(r'\unsure{L|\mathcal L}','L').replace(r'\unsure{\varphi|\Phi}',r'\Phi').replace(r'\varphi\in',r'\Phi\in')
t=t.replace(r'\unsure{\mathrm{Drop}|\mathrm{Drp}}',r'\unsure{\mathrm{Drop}|\mathrm{Drap}|\mathrm{Drp}}').replace(r'\unsure{\mathrm{Tro}|\mathrm{Tr}_0}',r'\unsure{\mathrm{Tro}|\mathrm{Tr}_0|\mathrm{Tr}}').replace(r'\unsure{sur|sûr}','sur').replace(r'\unsure{soit|soient}','soit')
t=re.sub(r'\bM\b',lambda m:r'\mathcal M',t)
c=[]
def a(p,C,H,F,e,k='other',cd=False,hd=True,q='high',marked=False):c.append(change(p,C,H,F,e,k,cd,hd,marked,q))
for p,crop in [('non réduit qualification','top'),('example three occurrences','example'),('join decomposition display','proof')]:
 a(p+' M alphabet','M',r'\mathcal M',r'\mathcal M','scan038_'+crop+': same swept-entry double-bowl M as preceding scans.','misread symbol or index',True,False)
a('finie emphasis','plain','bold','plain','scan038_top: no underline, doubling or separate emphasis on finie.','text not on the page')
a('before X nonempty',r'\deleted{\unsure{Y|X}}','omitted',r'\deleted{\unsure{Y|X}}','scan038_top: small crossed fork and descender before the live X; original glyph not safely separable.','omission',False,True,'low')
a('minimaux emphasis','underlined','bold','underlined','scan038_top: continuous rule under minimaux.','other')
a('qui soient','soient','sont','soient','scan038_top: separated short i/e strokes between initial s and final nt.','misread word')
a('bracket opening','en supposant','On suppose','en supposant','scan038_top: lower-case en after bracket, then long supp...ant ending.','misread word')
a('point abbreviation',r'p\textsuperscript{t}','pt',r'p\textsuperscript{t}','scan038_top: t is distinctly raised above p stem.','abbreviation expanded or spelling modernised')
a('morally abbreviation',r'\unsure{mor^t|moral^t|ess^t}','aussi',r'mor\textsuperscript{t}','scan038_top: initial m humps, small rounded o, hooked r and isolated raised t; no full aussi.','misread word',True,True,'medium')
a('vide quotation','double high quotation marks','guillemets','double high quotation marks','scan038_top: two short slant strokes at each end, not angled guillemets.','other')
a('Ex emphasis','underlined','bold','underlined','scan038_example: clear separate rule below Ex.','other')
a('first L alphabet',r'\unsure{L|\mathcal L}','L','L','scan038_example: same simple looped L in both consecutive Mod arguments; no different alphabet indicated.','misread symbol or index',True,False)
a('On aura','On aura','On a','On aura','scan038_example: au-r-a occupies several connected strokes before donc.','misread word')
a('X index Phi',r'\unsure{varphi|Phi}',r'\Phi',r'\Phi','scan038_example: full-height upright through two-sided loop and a base stroke, capital Phi.','misread symbol or index',True,False)
a('family Phi membership',r'\varphi',r'\Phi',r'\Phi','scan038_example: same capital loop with central upright and bottom foot as the preceding index.','misread symbol or index',True,False)
a('family operator spelling',r'\unsure{Drop|Drp}','Drap',r'\unsure{Drop|Drap|Drp}','scan038_example: small closed round stroke between r and p; a versus o is not settled by its tiny tail.','misread word',True,True,'low')
a('family superscript',r'\unsure{*|K}','*',r'\unsure{*|K}','scan038_example: short upright with two right-hand obliques can be a compact star or K; retained doubt.','misread symbol or index',False,True,'low')
a('H order subscript','no subscript','ll subscript','no subscript','scan038_example: blank space below the family operator and before the parenthesis; no ll under it.','text not on the page')
a('Tro notation',r'\unsure{Tro|Tr_0}','Tr',r'\unsure{Tro|Tr_0|Tr}','scan038_example: small closed loop immediately after r near baseline; uncertain separate o/0 versus final r flourish.','misread symbol or index',True,True,'low')
a('union index and placement',r'\inserted{=\bigcup_i T_i}',r'=\bigcup T_i',r'\inserted{=\bigcup_i T_i}','scan038_example: equality and union added below the Phi index, with a tiny i underneath union.','insertion or placement')
a('pseudo-tronçon spelling',r'\unsure{ps.tronçons|pr.tronçons}','ps.-tronçons',r'\unsure{ps.tronçons|pr.tronçons}','scan038_proof: dot then tall t without an intervening hyphen; second compressed letter remains s/r.','abbreviation expanded or spelling modernised',False,True,'medium')
a('composant ending','composant','composants','composant','scan038_proof: final tall t followed directly by the capital T_i; no s.','misread word')
a('bien sur',r'\unsure{sur|sûr}','sûr','sur','scan038_proof: no circumflex above the short u strokes.','abbreviation expanded or spelling modernised',True)
a('cancelled conjunction sign',r'\deleted{\unsure{\&}}','cancelled et',r'\deleted{\unsure{\&}}','scan038_proof: one compact self-crossing angular glyph; cannot safely read two letters et.','misread symbol or index',False,True,'low')
a('decomposition phrase','se décomposer en deux parties',r'\uncertain{s’écrire} comme réunion \uncertain{disjointe} de deux parties','se décomposer en deux parties','scan038_bottom: décomposer is one long word with d ascender and p descender; no comme réunion clause.','misread word',False,True,'high',True)
a('cancelled soit',r'\unsure{soit|soient}',r'\struck{\ill{}}','soit','scan038_bottom: short soi with final tall t under the strike, without room for ent.','readable ink left as \\ill{}',True,True,'medium',True)
a('relative closed insertion',r'\inserted{rel^t} fermées',r'\add{fermées}',r'\inserted{rel\textsuperscript{t}} fermées','scan038_bottom: rel and raised t lie above the line, while fermées remains on the baseline.','insertion or placement')
inv=[('text','L1–4','de Boole... comp. connexes...'),('deletion','L3 before X','Y or X'),('text','L4–7 bracket','en supposant zero ne one...'),('deletion','L6','une'),('text','L8–10 example','Ex Reprenons M=Mod(L)...'),('text','L11','On aura donc'),('display','L11–12','A=X_Phi; Phi in Drop star(Tro(L))'),('insertion','below X_Phi','equals union_i T_i'),('text','L13–14','Je dis que les comp. connexes...'),('text','L15','En effet on a bien sur'),('display','L16–17','A=join_i T_i; Ti wedge Tj=empty'),('deletion','between display clauses','ampersand, tentative'),('text','L18–22','si i ne j... prouver que a)... b)...'),('deletion','bottom','soit'),('insertion','bottom above fermées','rel superscript t')]
d=[('before X nonempty','Y','X','low','Crossed fork.'),('family operator','Drop','Drap; Drp','low','Small closed round letter and tiny tail.'),('family superscript','star','K','low','Compact upright and right obliques.'),('Tro notation','Tro','Tr_0; Tr','low','Small baseline loop and right-edge crowding.'),('pseudo-tronçon abbreviation','ps.tronçons','pr.tronçons','medium','Compressed second letter.'),('cancelled conjunction sign','ampersand','unresolved','low','One angular crossed glyph.')]
commit(38,t,c,inv,d,consequential=['The claim concerns ps.tronçons as components of the relative moderate structure; its proof obligations a) and b) are preserved.','The bottom insertion is rel^t before fermées; H loses the relative qualification and relocates the insertion.','The family symbol is capital Phi; H’s ll subscript has no ink counterpart in this occurrence.'])
