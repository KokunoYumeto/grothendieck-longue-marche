import json,re
from pathlib import Path
base=Path(__file__).resolve().parents[1]
meta={
'F8a':('149; section2; manuscript22; scan45','PriorCyclotomic B1','None','The attached return is cited under explicit prompt authorization; its unramified-prime supplement is retained.'),
'F10a':('149; section3; manuscript26 continuation; scans53–54','A4; RootStix Proposition11,Corollary12','scan54: centralisateur in the writing versus normalizer required mathematically','Exact centralizer formula retained; a uniformizer supplies the splitting.'),
'F10b':('149; section3; manuscript26–27; scans54–56','B2; RootStix Theorem14','None','All hyperbolic types including (0,3).'),
'F10c':('149; section3; manuscript26–27; scans54–55','F10a; F10b','None','Type (0,2) is an explicit failure of disjointness of point and cusp packets.'),
'G1':('142; opening; manuscript1 continuation and3; scans6–7','G_ConstantinKolev Lemma2.5,Theorem3.1,Proposition3.3; SGA1 XII5.1','scan5: sans doute versus loin d’être; scan6 periodic map orientation','Orientation-preserving hypothesis is exact; reflection supplies the other case.'),
'G2':('142; opening; manuscript2–3; scans5,7','G1','scan5: H1/propre; alternatives treated separately in G11','Integral and mod-n n≥3 rigidity; explicit n=2 failure.'),
'G3':('142; opening; manuscript3; scan7','G2; B4','scan7: 2g−nu≥2 versus 2g+nu≥2','Full stability Y+u=Y; does not assert the false open-subset lemma.'),
'G4':('142; opening; manuscript1–3; scans3,4,6–8','G2; G_Yagasaki Theorem1.1(ii),Lemma2.1(i); G_FarbMargalit Theorem8.8','scan4 isotopes/homotopes; unique factorization requires marking','Compact-open connected components identified with identity homeomorphism group, including openness proof.'),
'G5':('142; opening; manuscript3 continuation; scan8','G2; G4; G_Kerckhoff Theorem1','None','Free realization is the exact criterion; genus-two involution refutes all-finite-subgroups margin.'),
'G6':('142; opening; manuscript4–6; scans9–12,14','None','scan9 composition domains; scan12 devrait suffire; scan14 completed stabilizer','General separated profinite envelope, actions, continuous associative composition and conservativity proved.'),
'G7':('142; opening; manuscript5–6; scans12,14','G6','scan12 raw contracted product versus closure; scan14 hatG_u versus closureG_u','Two explicit categories prove both corrections.'),
'G8':('142; opening; manuscript5–6; scans11,14','G2; G4; G6; G_Paris Theorem1.4; G_FarbMargalit Theorem8.8','scan14 unique Y-isomorphism retains marking','Finite deck group is closed and separated; full residual finiteness is proved.'),
'G9':('142; opening; manuscript6 continuation; scan14','G6; G7; G8','scan14 injective alone versus closed embedding','Dense stabilizer Z in hatZ gives failure of the stated general hypothesis.'),
'G10':('142; opening; manuscript4–5; scans10–11','None','scan10–11 closed stabilizer and finite-index image','Actual composition in an already profinite-automorphism category is continuous under the stated conditions.'),
'G11':('142; opening; manuscript2; scan5','G2','scan5: H1, propre; ordinary, Borel–Moore and compactified homology interpretations','Explicit intersection pairing and two counterexamples test the alternatives without settling paleography.'),
'Z142a':('142; opening; manuscript3–6; scans8–9,13','G2; G4; G6; G8; G_FarbMargalit Theorems4.9,4.11','scan13 no isolated points; mathematical correction','Compact metrizable proved; absence of isolated points has exact infinite-group condition and type(0,3) counterexample.'),
'Z142b':('142; opening; manuscript6–7; scans13–16','G6; G8; G_BertinRomagny2007 Theorems6.9,6.20,Proposition6.14; G_Noohi2005 Theorem20.4; G_Bresciani2021 LemmaA.22,PropositionA.23','scan16 équivalences but not surjectifs; objectwise versus essential surjectivity','Characteristic-zero category defined through actual covers and étale paths; every comparison map specified.'),
'Z142c':('142; opening; manuscript7; scans15–16','SGA1 X1.8,XIII2.9,2.12','None','Artin–Schreier torsor y^p−y=tx refutes full base-invariance premise; no claim that an unspecified wild category has been classified.'),
'Z142d':('142; opening; manuscript7–8; scans16–17','Z142b','None','Explicit base-change functors and inner ambiguity of their action on a skeleton.'),
'Z142e':('142; opening; manuscript8–9; scans18–19','None','scan19 isotopie raisonnable lacks definition','Degree-six composite of finite covers and puncture fillings refutes ordinary-path reading; fixed Hurwitz incidence gives a proved local replacement.'),
'Z142f':('142; opening; manuscript8–10; scans18,20–21','Z142b','scan18 T=Yhat−T versus Yhat−Y; S versus C; scan19 Xhat versus Yhat','Source containment and ramification condition proved; functorial filling requires remaining type hyperbolic.'),
'Z142g':('142; opening; manuscript7–10; scans15–21','Z142b–Z142f','scan19 reasonable isotopy; unspecified relations in scan21','Exact unfinished objectives, failed transfer steps, and next mathematical obligations recorded.')}
rows=[]
for file in ['F_root.tex','G_root.tex','Z_root.tex']:
 text=(base/'sections'/file).read_text()
 for m in re.finditer(r'\\begin\{result\}\{([^}]+)\}\{([^}]+)\}\{',text):
  ident,status=m.group(1,2)
  end=text.index('\\end{result}',m.end())
  statement=text[m.end():end].strip()
  # Retain mathematical TeX, including full hypotheses, in the machine ledger.
  passage,dependencies,doubt,notes=meta[ident]
  rows.append(dict(id=ident,statement=statement,status=status,where_proved=f'sections/{file}; Result {ident}',depends_on=dependencies,manuscript_passages=passage,depends_on_doubtful_reading=doubt,notes=notes))
(base/'ROOT_results.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
readings=[]
def rd(file,scan,place,support,strength):
 readings.append({'file':file,'scan':scan,'the_unsure_or_illegible_place':place,'what_the_mathematics_supports':support,'how_strongly':strength})
f='MPL_142_001-093_transcription.tex'
rd(f,'4,6','isotopes | homotopes; factorization unique à isomorphisme unique près','For finite covers, a lifted homotopy gives an isotopy; uniqueness concerns the cover together with its marking. Unmarked covers can have deck automorphisms.','Exact proof G4,G8; selected images inspected; no final reading.')
rd(f,'5','sans doute | loin d’être tjs vrai; isolated fixed points continued from scan6','A nonidentity orientation-preserving periodic map has isolated fixed points. Orientation reversal may fix a circle.','Exact alternatives G1; scan6 read before5; image evidence does not settle words.')
rd(f,'5','H_1, propre (doubtful qualification)','Ordinary H1 gives G2. Borel–Moore H1 gives the same result for orientation-preserving maps, by the explicit perfect pairing G11; complex conjugation on U03 refutes it without that hypothesis. Homology of the compactification alone fails even for an oriented involution.','Exact comparison/counterexamples G11; paleographic uncertainty retained.')
rd(f,'7','2g−nu≥2 | 2g+nu≥2','The Abel–Jacobi immersion range excludes exactly (0,0),(0,1), equivalent to 2g+nu≥2. The displayed minus reading excludes valid examples. The image appears compatible with a minus glyph, so correction is mathematical rather than claimed transcription certainty.','Strong mathematical evidence B4,G3; image inspected, not settled.')
rd(f,'8','NB tout sous-groupe fini peut s’obtenir comme stabilisateur','Exact criterion is existence of a free orientation-preserving realization. The genus2 hyperelliptic subgroup cannot act freely: its quotient genus would be3/2.','Refutation G5; statement itself legible, mathematical correction.')
rd(f,'9','Hom(X,Y|Z) × Hom(X|Y,Z)','Composition is Hom(X,Y) × Hom(Y,Z) → Hom(X,Z), with (u,v)↦v∘u.','Forced by typed domains; scan inspected.')
rd(f,'10–11','Aut(Y|Z) and closed projection H_u','The four endpoint factors are Aut(Y),Aut(X),Aut(Z),Aut(Y) in the manuscript’s order; compactness makes the projected closed stabilizer H_u closed, and finite index makes it open.','Typed proof G10; images inspected.')
rd(f,'12','contracted product and devrait suffire','A Hausdorff quotient uses the closure of the original stabilizer; the raw quotient can be non-Hausdorff. This is additional mathematical content, not a proposed glyph resolution.','Explicit counterexamples G7; scan inspected.')
rd(f,'13','sans points isolés','False without an exception: the type(0,3) self-Hom space is S3, or one point with puncture labels.','Exact computation Z142a; scan inspected.')
rd(f,'14','Y-isom unique; injectif; (hatpsi,hatphi) in hatG_u','Uniqueness retains the marking and requires the original stabilizer to be closed in the completed automorphism group. For surfaces finite deck groups meet this condition and hatG_u embeds; arbitrary categories need closureG_u.','G6–G9; image inspected; no final paleographic assertion.')
rd(f,'16','équiv. de cat. [mais pas ... surjectifs]','In characteristic zero, essential surjectivity follows through paths between points of the same moduli component; individual curves need not descend up to scheme isomorphism. The full fundamental-group premise fails in characteristic p.','Z142b,Z142c; first-pass transcription, later scan image not attached.')
rd(f,'18','T=Yhat−T | Yhat−Y; S | C','The definition is T=Yhat−Y, and the extra ramification lies in S; the actual map restriction requires f^{-1}(T)⊂S.','Exact domain calculation Z142f; first-pass only.')
rd(f,'19','Aut(Y)=Aut(Xhat|Yhat,T); isotopie raisonnable','The target compactification is Yhat. For isotopy, ordinary continuous paths do not have the asserted orbit classification; the degree-six composite Z142e tests the reading inside the category generated by finite covers and puncture fillings.','Domain forced; isotopy adjective remains undefined, no final reading.')
rd(f,'20','nu′≤nu; forgotten labelled packet I','The forgetting morphism exists on hyperbolic moduli when 2g−2+nu−nu′>0. Successive forgettings have canonical composition.','Exact type correction Z142f; first-pass only.')
f='MPL_149_001-090_transcription.tex'
rd(f,'45','Gamma′°; starred centralizer fact','All open Gamma′ are included; the auxiliary prime must also be unramified in its number field.','F8a and attached return B1 proof rechecked; lower image inspected.')
rd(f,'54','centralisateur Z(L_i)','The surjective group in (2) is the normalizer. The centralizer is its inverse image of ker(chi); the written centralisateur cannot have the asserted surjectivity over a finitely generated characteristic-zero field.','Exact formula F10a; both scan halves inspected; correction of mathematics, not a settled alternative glyph.')
rd(f,'54','splittings of (1) | (2)','The H1 torsor is the splitting torsor of the cusp extension (2), with conjugation by its inertia T.','F10a; image evidence supports (2), final reading not claimed.')
(base/'ROOT_readings.json').write_text(json.dumps(readings,indent=2,ensure_ascii=False)+'\n')
print('root results',len(rows),'readings',len(readings))
