from work import *
from record_helpers import *
n=7;s=ctext(n)
for a,b in [(r'\unsure{\ensuremath{=}|m}',r'\ensuremath{=}'),(r'\unsure{donc}','donc'),(r'\unsure{\Psi|(\Psi)}',r'\Psi'),(r'\unsure{.}','')]:
 assert a in s,a;s=s.replace(a,b)
r={'changes':[
D('opening quotation mark','unsure opening quote','omitted','unsure opening quote','007_heading.jpg: two small ink ticks at far left, possibly a quotation mark.',False,True,'omission','medium'),
D('heading number','Sous-famille admissible','Sous-familles admissibles','Sous-famille admissible','007_heading.jpg: terminal low stroke after double l/e; no distinct s after either word.',False,True,'misread word'),
D('heading insertion','(ou sous-ens)','(ill)','(ou sous-ens)','007_heading.jpg: ou and sous-ens clearly readable above title.',False,True,'readable ink left as \\ill{}','high',marked_h='yes'),
D('ens abbreviation','ens','ens.','ens','007_heading.jpg: no point before admissible.',False,True,'abbreviation expanded or spelling modernised'),
D('opening gender','un; fermé','une; fermée','un; fermé','007_heading.jpg: no final e at either locus.',False,True,'abbreviation expanded or spelling modernised'),
D('cancelled boundary expression','deleted unsure partial_L A','deleted ill','deleted unsure partial_L A','007_heading.jpg: boundary-like curl, looped family subscript and A under crossed strokes; exact old expression remains doubtful.',False,True,'readable ink left as \\ill{}','medium',marked_h='yes'),
D('first superscript correction','deleted L beneath Psi','Psi only','deleted L beneath Psi','007_equalities.jpg: footed loop visible beneath forked Psi in exponent.',False,True,'omission'),
D('relation correction','deleted unsure L before R_L','R_L only','deleted unsure L before R_L','007_equalities.jpg: looped old character beneath capital R.',False,True,'omission','medium'),
D('relation following word/sign','unsure s=|sur|S=','de','unsure s=|sur|S=','007_equalities.jpg: short raised curve then two horizontal strokes; not securely de.',False,True,'misread word','medium'),
D('cancelled proof opening','De unsure =|m','Donc','De =','007_proof.jpg: De followed by parallel bars under cancellation.',True,True,'misread word'),
D('cancelled proof ending','unsure ce|x','ill','unsure ce|x','007_proof.jpg: heavy last strokes, retain two candidates.',False,True,'readable ink left as \\ill{}','medium',marked_h='yes'),
D('existence overwrite','deleted unsure A before exists','exists','deleted unsure A before exists','007_proof.jpg: triangular old strokes beneath exists sign.',False,True,'omission','medium'),
D('point variable','unsure a|x in A','x in A','unsure a|x in A','007_proof.jpg: small loop-shaped letter, unlike the clearly crossed x earlier; do not normalize.',False,True,'misread symbol or index','medium'),
D('proof connective','unsure donc','donc','donc','007_proof.jpg: d loop followed by joined onc under initial rewrite.',True),
D('proof colon','contains x :','contains x.','contains x :','007_proof.jpg: two vertically separated ink dots after x.',False,True,'other'),
D('before Ainsi','deleted unsure Ain','omitted','deleted unsure Ain','007_proof.jpg: short struck beginning at left of Ainsi.',False,True,'omission','medium'),
D('proof grammar','que il est','qu’il est','que il est','007_proof.jpg: separate que and il groups on line.',False,True,'abbreviation expanded or spelling modernised'),
D('nonempty-stratum superscript','unsure Psi|(Psi)','(Psi)','Psi','007_proof.jpg: bare Psi after circle; no distinct parentheses around it.',True,True,'misread symbol or index'),
D('proposition introduction','ens de parties','un ens. de parties','ens de parties','007_prop.jpg: begins ens immediately after formula; no un or stop.',False,True,'text not on the page'),
D('equivalent conditions punctuation','no colon','colon','no colon','007_prop.jpg: empty space after équivalentes.',False,True,'text not on the page'),
D('saturation insertion anchor','b after admissible','a after closedness','b after admissible','007_prop.jpg: long curved attachment descends immediately after b’s admissible, before et la relation.',False,True,'insertion or placement',consequential='The saturation condition belongs to b, not a.'),
D('saturation relation subscript','unsure R_Psi|R_varphi|R_L','R_L','unsure R_Psi|R_varphi|R_L','007_prop.jpg: tiny loop/fork form at far right lacks a secure family foot.',False,True,'misread symbol or index','medium'),
D('equivalence relation label placement','inserted R_Psi','baseline R_Psi','inserted R_Psi','007_prop.jpg: symbol lies above d’équivalence and before the following preposition.',False,True,'insertion or placement'),
D('equivalence preposition','unsure sur|de','dans','unsure sur|de','007_prop.jpg: compressed short group after inserted label; no clearly written ans.',False,True,'misread word','medium'),
D('final punctuation','unsure period','none','none','007_prop.jpg: no ink point after final R_L; remove editorially supplied doubtful stop.',True)
],
'doubt_decisions':['Resolved: cancelled De =; donc; bare Psi exponent in nonemptiness clause; no final period. Retained: opening quote, family/power-set styling, overwritten boundary expression and L, compressed s=/sur/S=, cancelled ce/x and A, a/x, cancelled Ain, inserted relation subscript and sur/de.'],
'unresolved':['Tiny overwritten symbols and the subscript in the saturation insertion; the a/x variable may be a manuscript slip.'],
'doubts':[Q('opening','quote; scr L; cal P','cal L; scr P'),Q('cancelled expression','partial_L A'),Q('relation overwrite','L'),Q('relation wording','s=','sur; S='),Q('cancelled proof tail','ce','x'),Q('existence old glyph','A'),Q('point variable','a','x'),Q('crossed start','Ain'),Q('insertion subscript','R_Psi','R_varphi; R_L'),Q('preposition','sur','de')],
'inventory':[E('text','top','manuscript page 6; Sous-famille admissible'),E('insertion','title','ou sous-ens'),E('text','opening','definition of closed Psi subset L'),E('deletion','opening','old boundary expression'),E('display','upper','partial_Psi A=partial_L A; stratum equality'),E('deletion','first stratum superscript','L replaced by Psi'),E('text','upper middle','support saturation for equivalence relation'),E('deletion','relation label','old L'),E('deletion','middle','La top. de Psi est induite'),E('text','middle','En fait … notations précédentes'),E('display','middle','|Psi|=A_Psi'),E('deletion','middle proof opening','De = il est évident que pour ce/x'),E('text','proof','Soit x … least member containing x'),E('deletion','proof','old A beneath exists; x in |Psi| implies'),E('deletion','before conclusion','Ain'),E('text','conclusion','Ainsi Psi est préadmissible … admissible'),E('text','lower proposition','Prop. … Conditions équivalentes'),E('text','a)','Psi subset L and closedness'),E('text','b)','Psi admissible and induced relation'),E('insertion','b interline','support saturation condition'),E('insertion','b final lines','R_Psi')]
}
save(n,s,r)
