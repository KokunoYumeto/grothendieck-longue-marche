from records import commit,OUT
p=OUT.parents[1]/'source/SP58_CW_156-5_witnesses/codex/J156-5-05/pages/J156-5-05_156-5_scan036.tex'
tex=p.read_text()
repls={r'\unsure{ensembles|au même} \unsure{sc.}':r'\unsure{comme ça|ensembles sc.}',r"$F''\leq F'$":r"$F''\preccurlyeq F'$",r'\deleted{\unsure{Donc}}':r'\deleted{Donc}',r'\unsure{avant}':'avant',r'\deleted{\unsure{tant}}':r'\deleted{tant}',r'\unsure{induit}':'induit',r'\unsure{expliciter}':'expliciter',r'\deleted{\unsure{\alpha}}\;':r'\deleted{\unsure{\alpha,\beta|\alpha}}\;',r'\deleted{\unsure{\alpha\leq}}':r'\deleted{\alpha\leq}',r'\unsure{composé}':'composé',r'\unsure{i|j}':'i',r"l'\unsure{ident|idel|id.}":r"l'\unsure{idel|ident.}",r'\deleted{\unsure{et que de plus,}}':r'\deleted{et que de plus,}'}
for a,b in repls.items():
 assert a in tex,a
 tex=tex.replace(a,b)
ch=[]
def add(place,c,h,f,e,k='misread word',conf='high',ac=False,ah=True,hm=False,con=''):ch.append((place,c,h,f,e,k,conf,ac,ah,hm,con))
add('cancelled opening, after deux','ensembles / au même sc.','ill. ill.','comme ça / ensembles sc.','036 opening crop (300,105,1555,345): low linked m-like waves and a separate short ça-like group under the cancellation; reduced ink does not support certainty.',conf='low',ac=True,hm=True)
add('cancelled opening relation','F″≤F′','F″≼F′','F″≼F′','Opening crop: curved upper comparison stroke and a curved lower stroke, as on scan 035.','misread symbol or index','high',True,False)
add('cancelled opening before a','cancelled en','omitted','cancelled en, uncertain','Opening crop: short separate crossed group between on and a.','omission','low')
add('Mais ds une telle situation','ds','dans','ds','Upper half: only d and s; abbreviation is not expanded.','expansion or normalisation')
add('reference after situation (*)','cancelled N; avant I′','cancelled ill.; au-dessus de I; cancelled ill.','cancelled N, uncertain; “avant I′”','036 reference crop (1040,470,1630,660): avant has the v and terminal t, and the I carries a detached prime. No au-dessus de.','misread word','high',False,True,True,con='The quoted qualifier is “avant I′”; H substitutes a more conventional phrase.')
add('after K definition','en cancelled tant qu’ens.','comme ens. ill.','en cancelled tant qu’ens.','Reference region and upper half: en, then crossed tant, then qu’ens.; the initial q descends.','misread word','high',False,True,True)
add('relation d’ordre sur K','induit','induisant','induit','Upper half, y810–850: a short t ending, no -sant.','misread word')
add('first order criterion','sss','ssi','sss','Upper half, y980: three similarly rounded s forms, no dotted i.','misread word')
add('cancelled below first criterion','pour β, doubtful','ill.','pour β, doubtful','036 below_inequality crop (495,985,675,1125): p descender and looped beta remain, but the cancellation obscures parts.','readable ink left as \\ill{}','low',False,True,True)
add('second order criterion','sss','ssi','sss','Lower half, line before cases: final sign is a curved s like the preceding two.','misread word')
add('slanted marginal instruction','expliciter ds une proposition à part','explicitation pour partir : ill.','expliciter ds une proposition à part','036 margin crop (30,1190,305,1585), rotated −48°: full sequence legible, including the t in part.','misread word','high',False,True,True)
add('case 1 before pair','cancelled α','cancelled ill.','cancelled α,β / α','036 case_cancellations crop (605,1170,1080,1445): two crossing letter-shaped remnants; second may be β, not secure.','misread symbol or index','low',True,True,True)
add('case 1 before J′','cancelled I','omitted','cancelled I, doubtful','Same case_cancellations crop: a separate upright/crossbar under the J′.','omission','low')
add('case 2 before J','cancelled α','omitted','cancelled α, doubtful','Same crop: small crossed loop before live J.','omission','low')
add('case 3 before J′','cancelled I','omitted','cancelled I, doubtful','Same crop: upright canceled sign under the replacement J′.','omission','low')
add('case 3 before h_J','cancelled α≤','omitted','cancelled α≤','036 case3 crop (1375,1280,1655,1405): the alpha and two short inequality strokes survive the cancellation.','omission','medium')
add('square, below J→I','hooked headless line','hooked arrow','hooked headless line','Lower half: shaft has a left hook but ends bluntly at the right.','drawing or diagram')
add('square, above K','cancelled I″ / en','omitted','cancelled I″ / en','036 square crop (640,1630,1030,1775): horizontal cancellation through a short three-stroke group; no secure resolution.','omission','low')
add('side note, identity abbreviation','ident / idel / id.','ident.','idel / ident.','036 identity crop (1110,1640,1655,1785): final tall loop resembles l, with no separable n or t; abbreviation remains doubtful.','misread word','low',True,True)
add('On a fait ce qu’il fallait','no insertion','inserted sur la relation d’ordre de K','no insertion','Lower half: no such interlinear words above or below this clause.','text not on the page')
add('foot revision','cancelled et que de plus,; inserted cela implique que le; cancelled pour tout le G qui soit; inserted carré est cartésien','cancelled et; cela implique que la; ill.','C wording retained; obscure long deletion remains doubtful','036 foot crop (320,2050,1585,2335): the first deletion includes que de plus; le is visible above, and carré est cartésien is inserted below.','insertion or placement','medium',False,True,True)
add('foot parenthesis','J′=h_K⁻¹(J) avec rel./rels induite','J′=h_K⁻¹(J); cette condition and ill.','(J′=h_K⁻¹(J) avec rel./rels induite)','Foot crop: avec starts at the right and rel... induite continues below, enclosed by a final parenthesis.','misread word','medium',False,True,True)
inv=[('text','top centre','35'),('deletion','top, enclosed by cancellation','Si on ... a deux ... F′ et F″'),('deletion','opening of live text','Donc'),('text','upper middle','Mais ds une telle situation; Considérons'),('deletion','reference (*)','N'),('display','upper middle','K=J′ amalg I∖J'),('deletion','after definition','tant'),('text','middle','la relation d’ordre sur K'),('display','middle','α≤β sss h_J(α)≤β'),('deletion','below inequality','pour β'),('text','before cases','donc (α,β)∈K×K'),('margin note','left slanted','expliciter ds une proposition à part'),('display','cases','ou bien ... three cases'),('deletion','case 1','α,β/α; I'),('deletion','case 2','α'),('deletion','case 3','I; α≤'),('text','below cases','Ceci posé, on a'),('diagram','lower middle','J′ K / J I'),('deletion','above K','I″/en'),('margin note','right of square','h_K est h_J sur J′'),('text','foot','On a fait ce qu’il fallait'),('deletion','foot','et que de plus,; pour tout le G qui soit'),('insertion','foot interlinear','cela implique que le; carré est cartésien')]
notes='''### 036-N1 — Construction

Defines the ordered set K as J′ disjoint union I∖J, with the original orders on its two parts and mixed relation α≤β exactly when h_J(α)≤β in I. Displays the canonical square and describes h_K as h_J on J′ and the identity on the complement. The marginal instruction asks for an explicit separate proposition. Manuscript page 35, with a cancelled three-line opening; no date.

### 036-N2 — Ink and possible slips

The first two cases literally put the pair (α,β) in J′ and I∖J, with no square. Those omissions are preserved; they were not supplied from the mathematics. The top quoted phrase is “avant I′”. The final interlinear replacement says that the square is cartesian, with J′=h_K⁻¹(J) and the induced relation. The identity abbreviation is not expanded because its ending is uncertain.

### 036-N3 — Targeted check of the order construction

Under the preceding page’s hypothesis that h_J is increasing and J is a lower closed subset of I, transitivity holds within each part. For a chain starting in J′ and ending in the complement, the sole transition is J′→I∖J: if the first two terms lie in J′, apply monotonicity of h_J; if the last two lie in the complement, apply transitivity in I. There is no complement→J′ comparison. Reflexivity and antisymmetry follow from those on each part, since a mixed relation has no reverse relation. Thus the intended relation is an order, h_K is increasing and its inverse image of J is exactly J′. This checks the construction, not the literal type-inconsistent omitted squares.'''
doubts=r'''| Place | Reading | Alternatives | Confidence |
|---|---|---|---|
| cancelled opening, after on | en | no secure alternative | low |
| cancelled opening, after deux | comme ça | ensembles sc. | low |
| (*) cancellation | N | crossed old start | low |
| below first criterion | pour β | no secure alternatives | low |
| case 1 initial deletion | α,β | α | low |
| overwritten case letters | I; α; I | no secure alternatives | low |
| above K | I″ | en | low |
| identity abbreviation | idel | ident. | low |
| foot long deletion | pour tout le G qui soit | some interior strokes obscured | low |
| foot relation abbreviation | rel. | rels | medium |

C’s listed doubts were examined in the halves and nine non-overlapping locus crops. Certainty-only resolutions: Donc; avant; tant; induit; expliciter; deleted α≤; composé; square’s upper label i; deleted et que de plus. Remaining uncertainty is recorded above; no unreadable whole word has been invented to fill the deletions.'''
hand='''A small dotted curl labels the upper arrow i; it resembles a 2-shaped stroke but has no descending j. The final -t in induit and -ter in expliciter are abbreviated in height. The abbreviation for identity ends in a tall loop, hence idel/ident. remains open. The ordinary order signs inside the construction are ≤, while the cancelled opening still uses the curved subdivision sign ≼. The author uses sss consistently on this sheet.'''
commit(36,tex,ch,inv,notes,doubts,hand,notation='K=J′ amalg (I∖J); h_J maps J′ to J, h_K extends it to I. Ordinary ≤ is distinct from subdivision ≼.',abbr='ds = dans; ens = ensemble; can. = canonique; iso = isomorphisme; rel./rels = relation(s), ending uncertain; idel/ident. = identity abbreviation, ending uncertain.',checks=[('036-N3-order','targeted proof check','Verified reflexivity, antisymmetry and both mixed transitivity cases under h_J increasing; h_K increasing and inverse image of J equal J′. Literal missing pair-set squares remain unchanged.')])
