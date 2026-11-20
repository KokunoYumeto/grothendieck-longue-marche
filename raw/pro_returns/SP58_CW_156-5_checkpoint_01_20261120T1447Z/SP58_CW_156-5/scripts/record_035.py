from records import commit, OUT
from pathlib import Path
p=OUT.parents[1]/'source/SP58_CW_156-5_witnesses/codex/J156-5-05/pages/J156-5-05_156-5_scan035.tex'
tex=p.read_text()
repls={r'\unsure{Interprétons}':'Interprétons',r"$F'\leq F$":r"$F'\preccurlyeq F$",r"$G'\leq G$":r"$G'\preccurlyeq G$",r'\unsure{-|\to}':'-',r"et $J\subset I$, \deleted{\unsure{, factorise}}":r"et \deleted{factorise} \inserted{$J\subset I$},",r"\unsure{\chi'|y'}":r"\chi'",r"\unsure{\psi'|{+}'}":r"\psi'",r'\unsure{surjective|surjection}':'surjection',r'\unsure{Dire}':'Dire',r'\unsure{sous-d.}':'sous-d.',r'\unsure{donnée}':'donnée',r'\deleted{\unsure{k}}':r'\deleted{\unsure{\chi|k}}'}
for a,b in repls.items():
    assert a in tex,a
    tex=tex.replace(a,b)
# The overwrites remain doubtful only where the old ink is crowded.
for a,b in [(r'\deleted{\unsure{\varphi}}',r'\deleted{\varphi}'),(r'\deleted{\unsure{\chi}}',r'\deleted{\chi}'),(r'\deleted{\unsure{\psi\prime}}',r'\deleted{\psi\prime}')]:tex=tex.replace(a,b)
ch=[]
def add(place,c,h,f,e,k='misread symbol or index',conf='high',ac=False,ah=True,hm=False,con=''):ch.append((place,c,h,f,e,k,conf,ac,ah,hm,con))
add('opening, relation of F′ to F','≤','≼','≼','Upper half, y110–175: two curved comparison strokes, matching the relation on the following line.',ac=True,ah=False,con='Subdivision ≼, not the subfigure relation ≤, is the datum being interpreted.')
add('opening, relation of G′ to G','≤','≼','≼','Upper half, y195–245: curved upper wedge and lower arc.',ac=True,ah=False)
add('opening article','d’une F′','d’un F′','d’une F′','Upper half, first line: the final small e in une is visible before F′.','misread word')
add('diagram (*), top horizontal and bottom horizontal','headless hooked lines','hooked arrows','headless hooked lines','Upper half: a hook by T/J and a bare shaft at S/I; no arrowheads at the right.','drawing or diagram')
add('diagram (*), f⁻¹(J)','cancelled φ before f','only f','cancelled φ before f','035 crop top_labels (385,630,745,1020): the closed loop of the older φ survives through the f.','omission','medium')
add('diagram (*), T→J′ label','cancelled ψ/φ; g_J* or g_J','g_J','cancelled ψ/φ; g_J* or g_J','Same top_labels crop: an older loop at g and a detached raised dark mark; cannot safely exclude a cancelled prime.','omission','medium')
add('diagram (*), curved restriction label','cancelled φ; f_J* or f_J = cancelled φ f|T','f_J=f|T','cancelled φ; f_J* or f_J = cancelled φ f|T','Same top_labels crop: two overwritten loops; raised blot remains at the first f.','omission','medium')
add('diagram (*), J′→J label','cancelled χ before h_J','h_J','cancelled χ before h_J','Same top_labels crop: older crossed diagonals under h.','omission','medium')
add('diagram (*), S→I label','cancelled φ before f','f','cancelled φ before f','Upper half, y860–945: looped remnant at base of the live f.','omission','medium')
add('NB, S to I and final two links','bare strokes','three arrows','bare strokes','Upper half NB: S–I and T–J′–J each have straight blunt shafts; the intervening T→J does have a point.','drawing or diagram')
add('NB, replacement after et','J⊂I, cancelled , factorise','cancelled fermé, J⊂I','cancelled factorise, inserted J⊂I','035 crop NB_strike (1245,740,1655,885): long f descender, factorise under a straight cancellation; J⊂I sits above that word.','insertion or placement','high',True,True)
add('middle factorisation, T→J′','cancelled ψ′, g_J or g_J*','g_J','cancelled ψ′, g_J or g_J*','035 crop middle_labels (1010,1220,1370,1340): forked ψ-form crossed under the replacement g and J.','omission','medium')
add('middle factorisation, J′→J','cancelled χ′, h_J* or h_J','h_J','cancelled χ′, h_J* or h_J','Same middle_labels crop: cross-form under h and a high residual mark; its state is unresolved.','omission','medium')
add('prose after où','χ′ or y′','g_J','χ′','Lower half: long descending diagonal crossed near its top, followed by a detached prime; no J subscript.',con='The increasing ordered-set map is called χ′ in the prose; H transfers the label to g_J.')
add('prose before une application ensembliste','ψ′ or +′','h_J d’une','ψ′ une','Lower half: forked short Greek form with prime, followed directly by une; no d apostrophe.',con='The set-surjection map is ψ′ in the prose; keep the unrevised Greek notation.')
add('prose, after ensembliste','surjective (alternative surjection)','surjective','surjection','035 crop ending (275,1450,740,1600): the final detached oval and n-shape are -on, not -ve.','misread word','high',True,True)
add('second occurrence of F′ datum','d’une F′','d’un F′','d’une F′','Lower half, y1500–1555: final e after un.','misread word')
add('before S→I′→I','pour φ en','pour φ','pour φ en','Lower half, y1590–1645: en is at the right edge after φ.','omission')
add('S→I′→I, first old label','cancelled ψ before g','g','cancelled ψ before g','Lower half, y1650–1730: old wide forked/looped form behind g.','omission','medium')
add('S→I′→I, second old label','cancelled χ before h','h','cancelled χ before h','Lower half, same display: crossed old form to the left of h.','omission','medium')
add('revised paragraph, opening','Dire que ça induit','cancelled Dire; Dire que ça se déduit','Dire que ça induit','035 crop rewritten (285,1710,1555,1930): one retraced initial D, followed by que ça induit; there is no separate first Dire or se déduit.','text not on the page')
add('revised paragraph, first cancellation','cancelled un diag','ill.','cancelled un diag, doubtful','Same rewritten crop: two short words below induit, with diag-like ending; keep C’s doubt.','readable ink left as \\ill{}','low',False,True,True)
add('revised paragraph, replacement of situation','la cancelled situation; inserted sous-d. donnée G′ de G; donnée','inserted induit sur G la donnée G′; ill.','la cancelled situation; inserted sous-d. donnée G′ de G; donnée','Same rewritten crop: the insert begins sous-d., with a hyphen, then donnée G′ de G. The original donnée survives at right.','insertion or placement','medium')
add('revised paragraph, qu’ and cancelled continuation','qu’ cancelled elle; cancelled a des d’applications; inserted existe i′','qu’il; ill.; existe i′','qu’ cancelled elle; cancelled a des d’applications (doubtful); inserted existe i′','Same rewritten crop: elle under black cancellation; a long crossed d’applications sequence lies below the insertion.','misread word','low',False,True,True)
add('revised paragraph, commutation','les deux carrés commutent','les [ill.] diagrammes [ill.] suivants commutent','les deux carrés commutent','Lower half and rewritten crop: deux and carrés are directly visible on the last baseline. No diagrammes or suivants.','misread word')
add('with J′=h⁻¹(J), cancelled initial','cancelled ξ','only J′ in surcharge','cancelled ξ, doubtful, then J′','035 crop inverse (1230,1970,1640,2090): separate old curved sign with strikes before the live J′.','omission','low')
add('with J′=h⁻¹(J), old letter','cancelled k','omitted','cancelled χ or k','Same inverse crop: old diagonal cross at the bottom of h; χ is now the first reading in view of the repeated χ→h change, but k remains possible.','misread symbol or index','low',True,True)
inv=[('text','top centre','34'),('text','opening','Interprétons la donnée d’une F′≼F'),('insertion','opening, above ens','ord'),('diagram','upper half','(*) T, S, J′, J, I'),('deletion','diagram labels','φ; ψ/φ; φ; φ; χ; φ overwritten'),('text','below J','partie fermée de I'),('margin note','right of diagram','NB On part de f'),('deletion','NB','factorise'),('insertion','NB','J⊂I'),('text','middle','La donnée de G′ équivaut'),('deletion','middle factorisation labels','ψ′; χ′'),('deletion','before appl.','un'),('text','lower middle','La donnée d’une F′'),('diagram','lower middle','S → I′ → I'),('deletion','labels in preceding diagram','ψ; χ'),('text','revised paragraph','Dire que ça induit la ... signifie'),('deletion','revised paragraph','un diag; situation; elle; a des d’applications'),('insertion','above revised paragraph','sous-d. donnée G′ de G'),('insertion','inside revised paragraph','existe i′:J′↪I′'),('diagram','foot','T, S; J′, I′; J, I'),('deletion','right of foot diagram','ξ; χ/k beneath h')]
notes='''### 035-N1 — Statement and notation

Recasts a subdivision F′≼F inducing G′≼G as a factorisation of the map to the ordered set of strata. The first diagram has T=f⁻¹(J), with J closed in I; the final diagram imposes commutativity and J′=h⁻¹(J). It is a translation of the data, not a new verification request. Manuscript pagination 34; no date or title sheet.

### 035-N2 — Readings directed by the mathematics

The curved opening signs are subdivision signs; replacing them by ≤ changes the data. The ordered surjection and set-surjection in the explanatory sentence retain the old names χ′ and ψ′, respectively, while diagrams have been overwritten with h_J and g_J. The roles explain the old χ→h and ψ→g overwrites, but do not authorize replacing the prose labels. Raised blots on some overwritten labels may be stars or struck old primes and remain marked. “application ensembliste surjection” is retained as written, despite the unusual ending. No independent proof of the figure/factorisation dictionary was performed on this page.'''
doubts=r'''| Place | Reading | Alternatives | Confidence |
|---|---|---|---|
| (*) old T→J′ label | ψ | φ | low |
| (*) live labels | g_J*, f_J* | g_J, f_J; possible cancelled old primes | medium |
| middle live labels | g_J; h_J* | g_J*; h_J | medium |
| cancelled un before appl. | un | no secure alternate | low |
| overwritten middle ψ′ and χ′; display ψ | first readings retained | obscured underlying strokes | low |
| revised paragraph cancellations | un diag; situation; elle; a des d’applications | uncertain remnants, no secure alternatives | low |
| before final J′ | ξ | unidentifiable crossed start | low |
| under final h | χ | k | low |

C certainty-only decisions: Interprétons, the repeated overwritten φ forms, χ under h in the upper diagram, the bare NB stroke, χ′ and ψ′ in prose, Dire, sous-d., and donnée are resolved. The endings, opening signs, NB attachment and old letter at h have substantive rows. Every one of C’s 30 listed doubt places was examined; repeated overwrite loci are grouped in this table.'''
hand='''The subdivision sign has a curved wedge and lower curve, distinct from the ordinary ≤ used later; C flattened both opening occurrences. Latin f, g, h overwrite φ, ψ, χ in several diagrams, but old Greek names remain live in the prose. Raised residual blots are not reliably distinguishable from live stars at all occurrences: the ambiguity is explicitly retained rather than propagated as certain notation. H omits most old letters and reverses the roles in the explanatory sentence. The reduced final -on in surjection is visible as a detached oval and n; both witnesses preferred the grammatical surjective.'''
commit(35,tex,ch,inv,notes,doubts,hand,notation='Subdivision ≼ distinguished from ≤; diagram f,g,h with restriction indices J coexist with live φ,ψ,χ in prose. The consistent map roles support χ′ and ψ′ rather than Latin y′ or a plus.',abbr='ens = ensembles; ord = ordonnés; NB = nota bene; appl. = application; croiss. = croissante; sous-d. = sous-donnée (probable); surj = surjectif; diag = diagramme.')
