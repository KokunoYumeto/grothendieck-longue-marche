import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[
(r'finite \unsure{:|{}}\unsure{dimension-|dimension}',r'\unsure{finit.|finite} :\unsure{dimens-|dimension-|dimension}'),
(r'\unsure{an|a}',r'an'),
(r'\unsure{\mathrm{Id}|\mathrm{id}}',r'\mathrm{Id}'),
(r'\unsure{non}',r'non'),
(r'\unsure{\gamma|\mathscr{T}}',r'\unsure{\mathscr{J}|\mathcal{J}|\gamma}'),
(r'types of $\gamma$, $\gamma/\Gamma$',r'types of $\mathscr{J}$, $\mathscr{J}/\Gamma$'),
(r'\unsure{i.e|i.e.}',r'i.e'),
(r'values \unsure{.|{}}',r'values .')]
L=[]
def a(p,c,h,f,s,k='other',v='high',C=False,H=True,m='no',q=None):
 d=dict(place=p,c=c,h=h,final=f,ink=s,kind=k,confidence=v,against_c=C,against_h=H,marked_in_H=m)
 if q:d['consequential']=q
 L.append(d)
a('opening insertion','moduli for','modular (','moduli for','top: moduli followed by separate for, above an insertion bracket ending before motives; no text parenthesis.','misread word')
a('finite dimension',r'finite \unsure{:|{}}\unsure{dimension-|dimension}','finite dimension',r'\unsure{finit.|finite} :\unsure{dimens-|dimension-|dimension}','dimension crop: two separated low marks between words; compact final letters and terminal dash do not support silent expansion.','abbreviation expanded or spelling modernised','low',True)
a('before fundamental',r'\unsure{an|a}',r'\struck{\ill{}} a','an','top: a loop and short n hump, without cancellation; H invents deletion.','deletion state (struck given live or live given struck)',C=True,m='yes')
a('bilinear-form glyph',r'\unsure{\varphi|\phi}',r'\varphi',r'\unsure{\varphi|\phi}','form/positivity: small upper oval and long descending stroke; variant retained because upper crossing is compressed.','misread symbol or index','medium',False,True)
a('torus morphism',r'U_R\to G_R',r'\mathbb U_R\longrightarrow G_R',r'U_R\to G_R','form: U is one open bowl with no interior doubled upright; arrow has both wings.','misread symbol or index')
a('negative identity',r'-\unsure{Id|id}',r'-id',r'-Id','positivity: initial upright is undotted and as tall as d, unlike the dotted i in preceding id.','misread symbol or index',C=True)
a('after if phi',r'\deleted{\unsure{a|o}}','omitted',r'\deleted{\unsure{a|o}}','positivity: a small rounded blackened letter remains before skew-symmetric, interior occluded.','omission','low')
a('cancelled square-root condition',r'\deleted{\unsure{i_0|id}(\sqrt{-1})\unsure{=|\ne}\unsure{1|{-1}}}',r'\struck{\ill{}}',r'\deleted{\unsure{i_0|id}(\sqrt{-1})\unsure{=|\ne}\unsure{1|{-1}}}','positivity: dense diagonal strikes leave radical roof and parenthesis; starting character, relation and terminal sign remain ambiguous.','readable ink left as \\ill{}','low',m='yes')
a('cancelled non-triviality',r'\deleted{i_0(i) \unsure{non} trivial.}',r'\struck{\ill{}}',r'\deleted{i_0(i) non trivial.}','positivity: long horizontal strike crosses readable i_0(i), low non humps, tall t and terminal l plus dot.','readable ink left as \\ill{}',C=True,m='yes')
a('positivity insertion extent','and a positivity condition ... which I will not write down.','only and a positivity inserted; I will struck','entire clause inserted, I will live','positivity: small writing occupies interlinear space across two lines; I will is unstruck below condition.','deletion state (struck given live or live given struck)',q='The explicit statement that the positivity condition is not written down is live.')
a('period-domain glyph',r'\unsure{\gamma|\mathscr T}; \gamma',r'\mathcal J',r'\unsure{\mathscr J|\mathcal J|\gamma}; \mathscr J','positivity/bottom: two upper branches and narrow lower loop match preceding pages.','misread symbol or index','medium',True,False)
a('classifies all','all','the','all','classifies: two tall connected l strokes after initial a.','misread word')
a('cancelled under',r'\deleted{\unsure{under}}',r'\struck{\ill{}}',r'\deleted{\unsure{under}}','classifies: dark strike across short under-like word; internal letters partly merged.','readable ink left as \\ill{}','medium',m='yes')
a('before Q-vector',r'\deleted{\unsure{V|Q}}Q','Q',r'\deleted{\unsure{V|Q}}Q','classifies: large overwritten initial field letter retains an earlier oblique stroke; original V/Q uncertain.','omission','low')
a('before i.e.',r'\deleted{\unsure{(|a}}','omitted',r'\deleted{\unsure{(|a}}','classifies: narrow vertical curved mark crossed by repeated short horizontal strokes.','omission','low')
a('i.e. all bigradings','i.e. all',r'\add{i.e.}\add{M}','i.e. all','classifies: i.e. and tall two-l all are on the running line, with no insertion mark.','misread word')
a('cancelled having',r'\deleted{\unsure{having}}',r'\struck{\ill{}}',r'\deleted{\unsure{having}}','deleted_having: lower h-like initial and g descender survive very heavy horizontal cancellation; central letters insecure.','readable ink left as \\ill{}','medium',m='yes')
a('polarization parenthesis abbreviation',r'\unsure{i.e|i.e.}','i.e.','i.e','bottom: dot between i and e; no terminal dot before phi.','other',C=True)
a('polarization parenthesis','a polarization',r'a \add{polarized} polarization','a polarization','bottom: no inserted word; uninterrupted running polarization.','text not on the page')
a('bigrading exponents','pq','p,q','pq','bottom: two raised letters with no comma between.','misread symbol or index')
a('after given values',r'\unsure{.|{}}','no period','.','bottom: isolated dark round dot below-right of values, before the following parenthesis.','other',C=True)
a('weights sentence',r'U_{\deleted{R}C} operating on V_C ...',r'\ill{} question on V_C \ill{}',r'U_{\deleted{R}C} operating on V_C ...','bottom: open U, overwritten subscript R to C, operating with distinct initial o and descending p, three dots after V_C.','readable ink left as \\ill{}','high',m='yes',q='H loses the torus, its overwritten base field, and the word operating.')
a('trouble','The trouble is that','The thought is that','The trouble is that','bottom: tr followed by ou, tall b and final le; not thought.','misread word')
a('cancelled if/of',r'\deleted{\unsure{if|of}}',r'\struck{\ill{}}',r'\deleted{\unsure{if|of}}','bottom: long f descender beneath horizontal retracing; first character occluded.','readable ink left as \\ill{}','low',m='yes')
a('as these','as these','of these','as these','bottom: initial a bowl then s; next line continues these.','misread word')
a('universal quotation','``universal\'\'','guillemets','``universal\'\'','bottom: paired raised strokes enclose universal; no angular guillemets.','other')
I=[]
def i(k,p,t):I.append(dict(kind=k,position=p,text=t))
i('text','opening','an algebro-geometric interpretation ... following:')
i('insertion','opening','moduli for')
i('text','upper','start with a vector space ... skew-symmetric')
i('display','upper-middle','G=SO(phi), i_0:U_R to G_R, i_0(-1)=id / -Id')
i('deletion','before skew-symmetric','a/o')
i('deletion','middle above line','square-root condition')
i('deletion','middle on line','i_0(i) non trivial.')
i('insertion','middle, two interlines','and a positivity condition ... I will not write down.')
i('text','lower two thirds','Then J is ... for all others')
i('deletion','Hodge-structures','under')
i('deletion','Q-vector','overwritten V/Q')
i('deletion','before i.e.','parenthesis/a')
i('deletion','before the usual','having')
i('insertion','above deleted having','satisfying')
i('deletion','torus subscript','R overwritten C')
i('deletion','after that','if/of')
commit(13,18,dict(replace=R,changes=L,inventory=I,sheet_kind='letter',observations='Whole and supplied halves inspected, followed by five overlapping enlarged bands and targeted dimension and cancellation crops. No diagrams or marginal text omitted.'))
