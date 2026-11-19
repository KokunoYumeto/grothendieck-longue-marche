from work import *
from record_helpers import *
n=6;s=ctext(n)
for a,b in [(r'\unsure{A|X}_J',r'A_J'),(r'\unsure{sûr|non}','sûr'),(r'\unsure{\ensuremath{=}|m}',r'\ensuremath{=}'),(r'A_{\unsure{i}}',r'A_i'),(r'\unsure{fibres}','fibres'),(r'\unsure{forme|formule}','forme')]:
 assert a in s,a
 s=s.replace(a,b)
r={'changes':[
D('first display A_J','unsure A|X with deleted unsure X','A_J','A_J with deleted unsure X','006_top.jpg: live triangular A and crossbar over older crossing strokes; old X remains uncertain.',True,True,'omission','medium'),
D('first display function glyph','unsure varphi|phi','varphi','unsure varphi|phi','006_top.jpg: loop with descending stem; precise conventional glyph remains a notation choice.',False,True,'misread symbol or index','medium'),
D('where J overwrite','deleted unsure A before J','J','deleted unsure A before J','006_top.jpg: crossed triangular stroke inside J.',False,True,'omission','medium'),
D('parenthetical family','unsure Phi|Psi|L','L','unsure Phi|Psi|L','006_top.jpg: upper loop on tall stem, unlike the clearly footed family glyph in NB; do not force it to L.',False,True,'misread symbol or index','medium'),
D('parenthetical opening','deleted unsure bien; unsure sûr|non','unsure Cette fois-ci','deleted unsure bien; sûr','006_top.jpg: crossed bien then short sûr; no fois-ci at this position.',True,True,'misread word','high',marked_h='yes'),
D('prose shorthand','de unsure =|m','de même','de =','006_top.jpg: two parallel bars, not letters même.',True,True,'abbreviation expanded or spelling modernised'),
D('second display old glyph','deleted unsure X before A_J','A_J','deleted unsure X before A_J','006_top.jpg: diagonal old glyph crossed beneath A.',False,True,'omission','medium'),
D('second display index','unsure i','i','i','006_top.jpg: dot and short stem below A.',True),
D('local condition abbreviation','loc fermée','loc. fermée','loc fermée','006_middle.jpg: no stop between loc and fermée.',False,True,'abbreviation expanded or spelling modernised'),
D('I_ge_i overwritten character','deleted unsure J|I','I_ge_i','deleted unsure J|I before I_ge_i','006_middle.jpg: heavy bars obscure older form.',False,True,'omission','medium'),
D('cover adjective','des ouvert','des ouverts','des ouvert','006_middle.jpg: final t terminates word, no separate s.',False,True,'abbreviation expanded or spelling modernised'),
D('local proof replacement','deleted unsure dans cet; inserted pour un tel ouvert','inserted pour chacun; deleted dans; de ces ouverts','deleted unsure dans cet; inserted pour un tel ouvert','006_middle.jpg: replacement pour un tel above crossed phrase; ouvert singular on line.',False,True,'misread word',consequential='Restores the actual local-closedness proof wording and its correction.'),
D('local proof subject insertion','deleted J; inserted J cap I_ge_i','J cap I_ge_i','deleted J; inserted J cap I_ge_i','006_middle.jpg: old J crossed on baseline; longer expression above.',False,True,'insertion or placement'),
D('local proof ambient insertion','inserted dans I_ge_i','baseline dans I_ge_i','inserted dans I_ge_i','006_middle.jpg: phrase raised with attachment curve.',False,True,'insertion or placement'),
D('local proof conclusion','si on a (*)','d’après (*)','si on a (*)','006_middle.jpg: distinct si on and isolated a before star.',False,True,'misread word'),
D('local proof inverse','l’inv. étant encore plus évident','l’inverse étant évident','l’inv. étant encore plus évident','006_middle.jpg: abbreviated inv.; encore plus present.',False,True,'omission'),
D('NB qualifier','inserted si L fini','inserted si L finie','inserted si L fini','006_boolean.jpg: terminal i and dot; no e before punctuation.',False,True,'abbreviation expanded or spelling modernised'),
D('NB cancelled word','deleted unsure at','deleted ill','deleted unsure at','006_boolean.jpg: a/t-like remains in heavy cancellation; not enough ink for a full word.',False,True,'readable ink left as \\ill{}','medium',marked_h='yes'),
D('NB fibres','unsure fibres','fibres','fibres','006_boolean.jpg: f tall stem, i dot and b/r/e/s sequence.',True),
D('NB power-set glyph','unsure cal P|scr P','cal P','unsure cal P|scr P','006_boolean.jpg: doubled vertical P stem; script/font mapping still uncertain.',False,True,'misread symbol or index','medium'),
D('NB ens abbreviation','ens','ens.','ens','006_boolean.jpg: no stop after ens.',False,True,'abbreviation expanded or spelling modernised'),
D('Boolean operation','unsure complémentaires|complémentations','complémentations','unsure complémentaires|complémentations','006_boolean.jpg: terminal run compressed; neither ending securely distinguished from shape alone.',False,True,'misread word','medium'),
D('second support delimiters','unsure |L) or |L|','|L|','unsure |L) or |L|','006_boolean.jpg: right delimiter curls inward at foot, unlike upper occurrence.',False,True,'misread symbol or index','medium'),
D('saturation preposition','par la rel','pour la rel.','par la rel','006_boolean.jpg: short par and no visible stop after rel.',False,True,'misread word'),
D('stratum glyph','unsure A°|X°','A°','unsure A°|X°','006_boolean.jpg: doubled triangular/diagonal strokes before superscript circle.',False,True,'misread symbol or index','medium'),
D('equivalence abbreviation','unsure i.e.|id.','i.e.','unsure i.e.|id.','006_boolean.jpg: compact strokes over a descending flourish; last letter uncertain.',False,True,'misread word','medium'),
D('bijection abbreviation','biuniv.','biunivoquement','biuniv.','006_bottom.jpg: abbreviated terminal v and point.',False,True,'abbreviation expanded or spelling modernised'),
D('display introduction','unsure forme|formule','formule','forme','006_bottom.jpg: f then low connected orme; no second tall l.',True,True,'misread word'),
D('last union index','unsure J|supset','J','unsure J|supset','006_bottom.jpg: short round rightward-curving sign; compare angular J in same display but retain doubt.',False,True,'misread symbol or index','medium'),
D('definition wording','unsure appelera|appellera; ses|ces|les; ainsi|aussi','appellera les ens. ainsi unsure obtenus','unsure appelera|appellera; ses|ces|les; ainsi|aussi; no obtenus','006_bottom.jpg: compressed spelling/short words; no word between ainsi/aussi and les parties.',False,True,'text not on the page','medium',marked_h='yes')],
'doubt_decisions':['Resolved from enlarged ink: live A_J in (1); sûr after crossed bien; prose =; second-display index i; fibres; forme. Retained all other C doubts: old X/A/J/I corrections, Phi/Psi/family sign, function and power-set glyph styles, old bien/dans cet/at, complementary-operation ending, support right delimiter, A°/X°, i.e./id., final J/supset, appelera/appellera, ses/ces/les and ainsi/aussi.'],
'unresolved':['Several overwritten letters, the Boolean-operation ending and the compressed wording of the final definition remain uncertain.'],
'doubts':[Q('top overwrites','X; A; bien'),Q('family in parenthesis','Phi','Psi; L'),Q('function','varphi','phi'),Q('local proof old text','J','I; dans cet'),Q('NB family and power set','scr L; cal P','cal L; scr P'),Q('NB old noun','at'),Q('Boolean operation','complémentaires','complémentations'),Q('support ending','|L)','|L|'),Q('stratum abbreviation','A°; i.e.','X°; id.'),Q('last union','J','supset'),Q('last sentence','appelera; ses; ainsi','appellera; ces; les; aussi')],
'inventory':[E('text','header','manuscript page 5; la forme'),E('display','top (1)','A_J=union A_i°=phi inverse(J)'),E('deletion','top display','old X'),E('text','first paragraph','où J … ne pas remplacer A_i° par A_i'),E('deletion','first paragraph','old A beneath J; bien'),E('text','before second display','Les parties loc. fermées sont de = les'),E('display','upper middle','A_J=phi inverse(J)=union A_i°'),E('deletion','second display','old X'),E('text','condition introduction','où cette fois J … telles que'),E('display','middle (*)','i≤j≤k; i,k in J implies j in J'),E('text','local proof','les I_ge_i … plus évident'),E('deletion','local proof','old J/I; dans cet; J'),E('insertion','local proof','pour un tel; J cap I_ge_i; dans I_ge_i'),E('text','NB','On peut aussi dire … algèbre de Boole'),E('insertion','NB opening','si L fini'),E('deletion','before fibres','at'),E('text','Boolean algebra paragraph','Les ens obtenus … parties quelc. de I'),E('display','bottom','J maps A_J=phi inverse(J)=union A_i°'),E('text','foot definition','parties L-modérées ou L-constructibles de L')]
}
save(n,s,r)
