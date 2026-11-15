#!/usr/bin/env python3
"""Generate two read-only-input audit tables from frozen cote 15 TeX."""
from pathlib import Path
from collections import Counter
import csv,hashlib,json,re
R=Path(__file__).resolve().parent.parent
T={n:(R/"pages"/f"{R.name}_15_scan{n:03d}.tex").read_text() for n in range(195,229)}
S={n:t.splitlines() for n,t in T.items()}
rows=[]
def add(n,a,b,q,status,action,notes,coverage="Covered"):
    if isinstance(q,str):q=[q]
    s=" ".join("\n".join(S[n][a-1:b]).split())
    for x in q:
        if " ".join(x.split()) not in s:raise ValueError(f"Quote mismatch {n}:{a}-{b}: {x}")
    rows.append((n,a,b,q,status,action,notes,coverage))
def precise_quotes(n,a,b,quotes):
    fragment="\n".join(S[n][a-1:b])
    anchors=[]
    for q in quotes:
        pattern=r"\s+".join(re.escape(part) for part in q.split())
        matches=list(re.finditer(pattern,fragment))
        if len(matches)!=1:raise RuntimeError(f"Nonunique exact quotation {n}:{a}-{b}: {q}")
        m=matches[0]
        line=a+fragment.count("\n",0,m.start())
        endline=a+fragment.count("\n",0,m.end()-1)
        column=m.start()-fragment.rfind("\n",0,m.start())
        anchors.append((q,line,endline,column))
    return anchors
E="Editorial; no extra mathematical note required"
N="Substantive omission; proposed extra note"
add(195,15,17,"sans doute","Expectation","Non-isomorphism in the mixed-characteristic comparison; the following finite-field assertion is also qualified/uncertain.","A01")
add(195,19,19,r"\deleted{\unsure{Vérifier}}","Deleted check","The marginal request for verification is itself deleted.","A01")
add(195,23,23,r"\unsure{bien faire attention}","Caution","Distinguish the realization's Hodge–de Rham filtration from a filtration of the motive.","A02")
add(196,6,6,"mettre l'exer. 1","Editorial move","Move exercise 1 into Proposition 11(c) and exercise 2 into the text.","—",E)
add(196,8,8,"Ajouter un utile rablot","Requested generalization","Generalize Propositions 5 and 6 to the algebras whose form is written with (commutative) and x sl₂; do not reconstruct the missing source propositions.","R12",N)
add(196,12,12,"Définir","Definition/clarification","Define deployment/deployability, explain diagonalizability, and restore semisimplicity in the indicated line.","R13",N)
add(196,14,14,"Remplacer","Terminological edits","Replace canonique by diagonale and abélienne by commutative where required.","—",E)
add(196,16,16,r"Y expliciter l'isom. $\varphi_{\alpha}$","Requested precision","Correct the primary-space wording; move the semisimplicity explanation; specify the one-dimensional subspace and isomorphism; add et si in (iv).","R14",N)
add(196,18,18,"démontrer le th. 3, c)","Deferred proof/editorial changes","Supply Theorem 3(c), use φα, amend the opening and W(2) wording, recognize the parenthesis already treated in §2, and specify the ambient Cartan for R.","R14",N)
add(196,20,20,"Le haut de la p. 44 remonte p. 41.","Editorial move","Move the specified source passage.","—",E)
add(196,22,22,"Titre : terminologie et inventaire.","Requested title","Replace the n°4 title.","—",E)
add(196,24,24,r"choisissons arbitrairement une racine $\alpha$","Choice convention","State choices of representatives of opposite roots and their corresponding Xα explicitly.","R14",N)
add(197,2,2,"penser que pour les pts différents","Expectation/continuation","The qualified comparison continues from scan 195; retain its incomplete opening and the effect of field automorphisms.","A03")
add(197,4,4,"à priori du moins","Qualified expectation","Two rational trivializations need not be isomorphic.","A04; A05")
add(197,4,6,r"pas d'isom \uline{canonique} prévisible","Qualified comparison","No canonical comparison is predicted; integral origin is questioned, and the margin asserts non-isomorphism already at weight/level zero.","A04; A05")
add(198,6,6,"Un cor. à la prop. 1 dira","Proposed corollary","State the e_n alternative, replace part of Proposition 2, and add stability under the binomial operators.","R15",N)
add(198,8,8,"arranger (4)","Normalization task","Specify boundary vectors, the divided-power generator and canonical basis, then adjust formula (4).","R15",N)
add(198,10,10,"Remplacer l'exer. 2","Editorial moves","Use Gabriel's replacement, move exercise 3 into the text, and move Lemma 4 from later pages.","—",E)
add(198,12,12,"Il semble qu'on n'a pas besoin","Hypothesis correction/tentative editing","Add finite dimensionality and decide whether Proposition 6(ii),(iii) can become exercises while (i) is combined with Proposition 5.","R02")
add(198,14,14,"donner une référence","Proof support","Reference complete reducibility, expand Remark 1, and replace the insufficiently easy Remark 2 with the Casimir calculation.","R02")
add(198,16,16,["seront définies en Alg. IV","Expliciter la fin de la démonstration"],"Deferred definition/proof","Add x²=0 and finite dimensionality, prefer the second proof, defer exponentials, and expand Proposition 9's argument.","R02; R16",N)
add(198,16,16,r"$\unsure{\theta|\varphi}^4=1$","Requested representation assertions","Add the claim about all irreducible holomorphic representations, correct E=S^m(V), and impose the fourth-power formula with its unresolved symbol.","R16",N)
add(200,6,6,r"raisonner sur $\underline{g}/\underline{h}$","Proof/editorial revision","Specify finite product, Autel invariance, and the quotient argument in place of Fitting.","R17",N)
add(200,8,8,"une seule valeur","Local edits","Add t∈k, specify a unique value, use inclusion, and identify the image under F.","—",E)
add(200,10,10,"opère transitivement","Action precision","State the acting group and transitivity in Theorem 2, and reference the conclusion of (iii).","R17",N)
add(200,12,12,"Ajouter le cor. suivant","Proposed corollary","Add the Cartan-subalgebra equivalence under equal-rank and regular-element conditions.","R18",N)
add(200,14,14,"Utiliser la prop. ajoutée au n° 3","Proof/editorial revision","Replace abélienne, add the nilpotence reason, and use the new proposition in Proposition 14.","R18",N)
add(200,16,16,r"Ajouter que, si $\underline{g}$ est une alg. Lie sur $K$","Proposed scalar-restriction assertion","Amend action/component wording and assert that restriction from K to a subfield preserves the Cartan subalgebras.","R19",N)
add(200,20,20,"Eviter les points","Editorial task","Remove the indicated points and use sous-algèbre diagonale.","—",E)
add(200,22,22,"Un exer. montrera les séries génératrices","Deferred exercise/definition","Explain that X is a bracket, extend weights to all H-eigenvectors, give generating-series exercises, and specify division by n!.","R15",N)
add(201,2,2,"On ne la confondra pas","Caution","Distinguish the integral-fibre involution from semilinear descent.","A07")
add(201,16,16,"n'opère pas à priori","Qualified action claim","Separate the absence of a general π₁-action from real conjugation and semilinear field automorphisms.","A03; A07")
add(202,6,6,"On donnera le principe de Lefschetz comme lemme.","Deferred lemma","Add the stated Lefschetz principle and connected-group corollary.","R20",N)
add(202,8,8,"Dire que toute sous-algèbre qui contient une Cartan","Proposed assertion","Correct terminology/references and add the self-normalizer assertion for subalgebras containing a Cartan.","R18",N)
add(202,10,10,"c'est au chap. I, p. 53 qu'il faut référer","Reference correction","Correct Proposition 8's reference.","—",E)
add(202,12,12,[r"Vérifier la formule du bas de la p. 9.",r"ne sont vraies qu'en caract. $\neq 2$"],"Explicit check/error qualification","Check the rank formula, define zero-root multiplicity, add the nilpotent example, restrict characteristic, and expand the terse example.","R03; R04")
add(202,14,14,"fausse en caract. p","Retraction/proof revision","Use the quotient argument, specify Cartan in the corollary, and remove the false positive-characteristic remark.","R04")
add(202,16,16,"Ajouter la prop. suivante","Proposed proposition","Add the Cartan inheritance, regular-element and nilespace assertions in (a),(b).","R18",N)
add(202,18,18,"est fausse en caract. p","Error correction","Replace the assertion by the indicated zero-eigenvalue multiplicity calculation.","R04")
add(203,2,7,r"il faut \uline{ajouter} la \uline{décomposition en types}","Required additional datum","Add the transcendental type decomposition to the integral Hodge–de Rham realization; the following involution comparison remains subject to its explicit check.","A07; A09")
add(203,13,17,r"\margin{à vérifier}","Explicit check","Verify the product and commutation relation between the two semilinear involutions.","A07")
add(203,19,24,r"\margin{à vérifier}","Explicit check","Verify the identification of the resulting action with real-place Frobenius.","A08")
add(204,8,8,r"Ce n° \unsure{absorde|absorbe}","Editorial consolidation","Record the announced absorption of source material.","—",E)
add(204,10,10,["c'est faux","vont au dépotoir"],"Retractions/reorganization","Delete the specified false passage and propositions/lemma; retain Proposition 2(b) and make Proposition 3(b) a corollary.","R05")
add(204,12,12,"un erratum à Alg. VII permettra","Deferred erratum/proof revision","Provide the eigenvalue erratum, remove unnecessary nilpotence, avoid a nonexistent characteristic-p simple quotient, and revise the proof.","R05; R21",N)
add(204,14,14,"sera faite en Alg. VII","Deferred descent proof","Leave descent to Algèbre VII, recall it here, and use an arbitrary Galois extension.","R21",N)
add(204,16,16,"la sommation est incorrecte","Correction","Correct invariance/module/zero-image wording, sum over half the roots, and delete the final remark.","R05")
add(204,18,18,"Une remarque donnera la nilpotence","Deferred replacement claim","Replace Proposition 5 by the nilpotence assertion for the literally written Ad(x), under missing Proposition 4 hypotheses.","R22",N)
add(204,20,20,"Remonter ici le résultat suivant","Relocated theorem","Move the analytic open-subgroup/eigenvalue result; the typed (4) leaf on scan 202 continues this statement.","R20",N)
add(205,4,4,r"\uline{conjecture de Hodge}","Conjectural interpretation","Interpret the motivic level filtration using Hodge data and real Frobenius.","A09")
add(205,8,13,"provient d'un sous-motif","Conjectural consequence","The displayed rational intersection is claimed to be motivic; retain the uncertain level index.","A09; A10")
add(206,12,12,"Le nouveau titre sera","Editorial programme","Rename the chapter and non-split algebras; direct the next redactor to add the following items.","—",E)
add(206,14,14,r"Les modules infinis $W(\lambda)$","Requested additions","Add infinite modules, Harish-Chandra formulas and invariant-differential-operator results.","R23",N)
add(206,16,16,"Jacobson-Mort aux Off","Programme label","Retain this literal named item; no theorem statement is supplied to identify or test.","—","Label only; no standalone mathematical assertion recoverable")
add(206,18,18,r"montrer les autom. de trialité de $D_4$","Requested constructions/proof","Treat classical split algebras and fundamental representations, demonstrate triality, and put exceptional algebras in exercises.","R24",N)
add(206,20,20,"Cartier rédigera un tapis arithmétique","Assigned future work","Cartier is assigned the Z-structure supplement; other complements are said to be discarded or incorporated.","R25",N)
add(206,24,24,"l'annexe II est traitée avec la rédaction des racines","Editorial disposition","Appendix II is assigned to the root-system redaction.","—",E)
add(206,26,26,"prendre la démonstration par références","Requested statement/proof support","Add density of every nonempty open to Proposition 1, remove its corollary, and use references for proof.","R26",N)
add(206,28,28,"intervertir définition et critère","Editorial clarification","Specify Zariski topologies, interchange the dominance definition and criterion, and replace W by A_W.","R26",N)
add(207,2,4,["Je pense que","faux, cf"],"Rejected expectation","Distinct places were proposed to give non-isomorphic bare integral/real fibres; the marginal figure calls this false.","A11")
add(207,8,8,r"je pense que $T_\alpha(\mathbf R)=\varnothing$","Expectation","Real-valued motivic points are expected to be absent in characteristic p for sufficiently large α.","A12")
add(207,10,10,r"Vérifier s'il ne peut y avoir des pt à val. dans une \unsure{ext. tot.} réelle ???","Explicit check","Test the totally real extension possibility.","A12")
add(207,12,14,"Si","Abandoned branch","A solitary conditional opening is followed by separator strokes, without a condition or conclusion.","—","Fragment only; no identifiable substantive claim")
add(209,9,12,r"\text{Il semble que ces pts correspondent}","Expectation","Propose a bijection of enriched transcendental motivic points with complex points modulo conjugation.","A15")
add(211,3,4,[r"\uline{Questions}",r"\margin{À revoir}"],"Whole-sheet review flag","The ensuing correspondence scheme is explicitly headed Questions and marked for revision.","A15; A16; A17")
add(211,8,8,r"avec \uline{structure supplémentaire}","Question under review heading","Match positive-characteristic points with Witt-valued motivic points carrying F,V/formal-group data.","A16")
add(211,9,9,"avec structure filtrée !","Question under review heading","Specify generalized categorical motivic points in h with filtered structure.","A16")
add(211,10,10,r"avec \uline{structure filtrée}","Question under review heading","Match characteristic-zero points with filtered motivic points over h.","A17")
add(211,18,20,"mod conj. complexe (= place)","Question under review heading","Compare archimedean places with real, conjugated complex, or integral fibres.","A15")
add(211,26,30,r"\uline{Pts banaux}","Classification under review heading","List Z_l/Q_l cases and the residue-characteristic restriction.","A15; A17")
add(211,33,36,r"\uline{Cas particulier important}","Question under review heading","Compare finite-field points with W(F_q)-valued motivic points carrying F,V.","A16")
add(213,10,14,r"En vertu de Borel\inserted{-\unsure{Harish}}","Unproved application","Apply arithmetic finiteness to integral fibre-functor forms and resulting groups.","A19")
add(213,13,14,r"Sont-ils tous \unsure{isom's}","Explicit question","Are the resulting discrete groups all isomorphic in the unspecified qualified sense?","A19")
add(213,29,30,"Comparaison avec","Comparison programme","Compare the discrete motivic group with the indicated topological fundamental group.","A18")
add(213,32,37,r"est \unsure{plt} fidèle","Conjecturally justified claim","The enriched functor's full-faithfulness assertion continues on scan 215 under Hodge/Tate input.","A20; M08")
add(214,15,17,"Nous laisserons au lecteur le soin d'étendre","Deferred verification","Extend Propositions 3 and 3 bis to group germs.","R08")
add(214,24,26,"les autres notations et résultats des n°s 12 à 16","Deferred verification","Extend earlier notation/results, including the induced enveloping-object representation.","R08")
add(214,28,32,"on vérifie aisément","Unexpanded verification","Check the tangent group-germ structure and projection morphism.","R08")
add(214,33,34,"les propositions 11 et 12 ainsi que leurs corollaires","Deferred verification","Extend Propositions 11–12 and their corollaries.","R08")
add(215,3,9,"Résulte de la conjonction des conj.","Conditional justification","Invoke Hodge and finite-field Tate, at least for normal X, also for the stated algebraically closed h⊂C.","A20; M08")
add(215,5,5,r"\unsure{Caractériser} \deleted{de} l'image","Explicit question","Characterize the essential image; retain the double question mark.","A21")
add(215,11,12,"Analyser l'exemple de Serre","Requested analysis","Analyze Serre's non-isomorphic fundamental-group example.","A22")
add(215,14,26,["irred (pas néc. géom irred)","est pleinement fidèle."],"Revised hypothesis/unproved real case","Retain the changed irreducibility hypothesis and the Frobenius-generation/full-faithfulness assertions.","A23; M06; M08")
add(215,35,37,r"\uline{Pb} étudier comment varie la structure","Explicit problem","Recover Hodge variation from the data at one fixed point.","A24")
add(217,3,8,r"est déterminé quand on connaît sa valeur \uline{en un point}","Proposed rigidity","Determine a moduli map from one value and the induced π₁-map.","A25")
add(217,10,16,r"Peut-être peuvent elles \unsure{ttes} être","Expectation/programme","Study the intrinsic rigidity property and characterize all such varieties by modular interpretations.","A26")
add(217,20,27,r"Introduire la notion de schéma \inserted{\unsure{motiviquement}} pointé","Definition programme","Introduce motivically pointed schemes/morphisms over h and their group maps.","A27")
add(219,5,7,r"Question : a) \inserted{Quand} sont-ils","Explicit question","When are the entire integral fibre functors isomorphic?","A28")
add(219,7,10,"Quand est-il vrai que pour tte sous-catégorie","Explicit question","When are restrictions isomorphic on every finite-type tensor subcategory?","A28")
add(219,12,17,r"[utilise le fait $X$ \uline{normal} !]","Marked dependency","The base-field reduction explicitly invokes normality.","A29")
add(219,50,53,[r"\unsure{mais rien ne prouve qu'on ait}",r"\unsure{je pense que}"],"Acknowledged gap/deleted expectation","The special comparison does not supply the proposed broader non-isomorphism claim, which is deleted.","A28; A31; A32")
add(220,18,18,"On a des propriétés analogues pour l'intégrale essentielle.","Unexpanded analogue","The essential-integral analogue is asserted without a separate derivation here.","—","Routine parallel verification; index only")
add(220,35,37,"on précisera toujours explicitement","Future convention","For finite groups, specify which incompatible Haar normalization is intended.","—",E)
add(220,42,43,"Nous verrons plus tard","Deferred theorem","Unimodularity of connected semisimple/nilpotent Lie groups is deferred.","R09")
add(221,19,19,r"Si $k$ pas dénombrable,","Unfinished case","The uncountable-field branch has no conclusion.","A31")
add(221,21,29,r"Alors je \deleted{\unsure{crois}}\inserted{pense}","Expectation/revised reduction","Different restrictions to E should be separated on a finite tensor subcategory; the extra base-change reduction is deleted.","A32")
add(223,2,2,r"Il suffirait de construire $X$ projectif lisse","Construction programme","Construct non-isomorphic integral cohomology rings of the two archimedean realizations.","A33; M05")
add(223,2,2,"On devrait mettre Serre à contribution.","Requested contribution","Seek Serre's contribution to the construction.","A22; A33")
add(223,3,3,r"Peut-on \unsure{remplacer} $\mathbf Z$ par $\mathbf R$??","Explicit question","Can the cohomology-ring witness use real coefficients?","A33")
add(223,6,9,r"si on admet ce qui a été \deleted{dit}\inserted{conjecturé}","Conjectural implication","For a sufficiently large motive, infer injectivity of the place-to-torsor map.","A34")
add(223,10,11,["se demander si",r"risque d'être une \unsure{condit\textsuperscript{n}} \unsure{vraimt} décisive"],"Question with restriction","Ask whether every torsor comes from a place; the margin warns that complex/Hodge compatibility may restrict the target.","A35")
add(223,16,16,r"à priori ne sont pas \unsure{isomorphes}","Expectation","Non-isomorphism of the resulting groups is qualified rather than proved.","A36")
add(225,2,2,r"\deleted{\unsure{L'énoncé implique} $X$ de type fini, \unsure{qui} \unsure{intervient}}","Deleted qualification","Retain the withdrawn finite-type qualification.","A37")
add(225,3,3,"Mais que se passe-t-il si on le regarde comme foncteur dans les structures de Hodge ?","Explicit question","Does Hodge enrichment recover the place?","A37")
add(225,4,8,r"\unsure{ceci devrait}","Cancelled attempted reduction","The proposed k₀/finite-type/quasi-projective/projective-line reduction is cancelled.","A37")
add(225,5,5,r"Vrai pour un schéma \unsure{$k$ local}","Inserted restricted assertion","The uncertain restricted case is asserted without completing the general argument.","A41",N)
add(225,9,9,"Attention, il faut parler des pl. complexes","Caution","Specify/restrict complex places sufficiently to define Hodge structures.","A37")
add(225,16,16,"Il semble qu'on le verrait facilement","Expectation/test case","Try the punctured projective line and the tentative appeal to classical theory.","A38")
add(225,16,16,"prendre comme motif celui défini par un schéma en courbes elliptiques","Proposed test construction","Use the elliptic family with invariant the indeterminate j.","A38; X01")
add(227,2,2,"en vertu de la conjecture de Hodge","Conjectural input","The margin invokes Hodge without proving the ensuing reconstruction questions.","A39; M08")
add(227,3,3,[r"\uline{quels} sont les foncteurs multiplicatifs",r"\unsure{inclure} les motifs sur $\mathbf C$!"],"Question/scope instruction","Characterize Hodge-valued tensor functors arising from archimedean places, including complex motives.","A37; A39")
add(227,3,3,"dans quelle mesure un morphisme de préschémas","Explicit question","Recover a prescheme map from its functor on motives.","A39")
add(227,3,3,"peut-il être pris arbitrairement ?!?","Explicit question","Characterize which multiplicative functors arise.","A39")
add(227,5,5,r"Pb de \uline{construire des schémas de modules}","Construction problem","Construct moduli schemes of polarized motives.","A40")
add(227,5,5,["est une immersion",r"\unsure{anabélien}"],"Proposed implication","Use a global polarized motive with an immersive classifying map to obtain the uncertain anabelian conclusion.","A40")
add(227,5,5,r"\unsure{Marche} en particulier si $Y$ est le spectre d'un corps","Expected special case","The spectra-of-fields case is asserted tentatively, without proof here.","A40")

heads=[]
def h(n,a,b,q,kind):
    if " ".join(q.split()) not in " ".join("\n".join(S[n][a-1:b]).split()):raise ValueError(f"Heading mismatch {n}:{a}: {q}")
    heads.append((n,a,b,q,kind))
for n,l,q,k in [
 (195,3,"2°)","Case label"),(195,9,"(i)","Case label"),(195,13,"(ii)","Case label"),(195,15,"Connexion : relation","Problem lead"),(195,21,"(iii)","Case label"),
 (196,4,"ALGÈBRES de LIE SEMI-SIMPLES (7)","Typed running title"),
 (196,10,r"§3 -- \uuline{Le système de racines}...","Section heading"),
 (196,22,"Titre : terminologie et inventaire.","Requested title"),
 (198,4,"ALGÈBRES de LIE SEMI-SIMPLES (6)","Typed running title"),
 (198,8,r"\uline{n° 2} -- Titre : les modules simples $W(m)$","Requested subsection title"),
 (198,12,r"\uline{n° 3} -- Titre : décomposition des $\underline{s}$-modules.","Requested subsection title"),
 (198,16,r"\uline{n° 4}","Editorial subsection"),
 (199,4,"(iv)","Case label"),(199,25,"a)","Case label"),(199,25,"b)","Case label continuing on 201"),
 (200,4,"ALGÈBRES de LIE SEMI-SIMPLES (5)","Typed running title"),
 (200,6,r"\uline{n° actuellement 4}","Editorial subsection"),(200,14,r"\uline{n° 6}","Editorial subsection"),(200,16,r"\uline{n° 7}","Editorial subsection"),
 (200,18,r"§2 -- \uuline{Les représentations de} $\mathrm{sl}_2$.","Section heading"),(200,22,r"\uline{n° 1}","Editorial subsection"),
 (202,4,"ALGÈBRES de LIE SEMI-SIMPLES (4)","Typed running title"),(202,8,r"\uline{n° 2}","Editorial subsection"),(202,12,r"\uline{n° 3}","Editorial subsection"),(202,18,r"\uline{n° actuellement 5}","Editorial subsection"),
 (204,4,"ALGÈBRES de LIE SEMI-SIMPLES (3)","Typed running title"),(204,10,r"\uline{n° 1}","Editorial subsection"),
 (205,4,r"\uline{N.B.}","Paragraph marker"),
 (206,6,"DÉCISIONS sur les ALGÈBRES de LIE SEMI-SIMPLES","Typed title"),
 (206,12,"algèbres de Lie semi-simples déployées","Requested replacement title"),
 (206,22,r"\uline{Annexe} I \uline{des applications polynomiales}.","Appendix heading"),
 (206,26,r"\uline{n° 1}","Editorial subsection"),(206,28,r"\uline{n° 2}","Editorial subsection"),
 (207,2,r"\uline{Faisons varier}","Programme lead"),(207,8,r"\uline{NB}","Paragraph marker"),
 (207,16,r"Pt motivique de $X$ à valeurs dans un corps (ou un anneau) $h$","Definition lead"),
 (208,2,"SYSTÈMES de RACINES (3)","Typed running title"),(208,6,"III.","Example-section label"),(208,10,"IV.","Example-section label"),
 (209,6,r"\text{Pts }l\text{-adiques}","Table label"),(209,7,r"\text{Pts transcendants}","Table label"),(209,16,r"\text{Pts Hodge-de Rham}","Table label"),(209,17,r"\text{pts de Witt}","Table label"),
 (210,3,"SYSTÈMES de RACINES (2)","Typed running title"),(210,9,"I.","Example-section label"),(210,29,"II.","Example-section label"),
 (211,3,r"\uline{Questions}","Manuscript heading"),(211,24,r"\uline{\deleted{\unsure{de X}} \unsure{car $p$}}","Uncertain/revised heading"),
 (211,26,r"\uline{Pts banaux}","Internal heading"),(211,33,r"\uline{Cas particulier important}","Internal heading"),
 (212,5,"SYSTÈMES de RACINES","Typed title without leaf label"),(212,7,r"\uline{Introduction}, (Rédaction Borel).","Internal heading and attribution"),
 (213,3,r"\uline{Groupe fondamental motivique discret}","Manuscript title"),(213,10,r"\uline{N.B.}","Paragraph marker"),(213,32,r"\uline{Ex}.","Example marker"),
 (215,5,r"\uline{\uuline{\unsure{Caractériser} \deleted{de} l'image}} ??","Programme/question lead"),
 (215,14,r"\uline{Cas corps de base} $\mathbb R$","Case heading"),(215,35,r"\uline{Pb}","Problem marker"),
 (216,5,r"17. \uline{Noyaux de groupe}.","Numbered section"),(216,7,"DÉFINITION 5.","Definition heading"),
 (216,37,r"\uline{Exemple} 1.","Example heading"),(216,39,r"\uline{Exemple} 2.","Example heading"),
 (217,20,r"Introduire la notion de schéma \inserted{\unsure{motiviquement}} pointé","Programme lead"),
 (218,5,r"16. \uline{Mesure de Haar d'une variété de groupe}.","Numbered section"),
 (219,6,"Question : a)","Question/case marker"),(219,7,"b)","Question/case marker"),(219,24,"1°)","Case marker"),(219,50,"b)","Case marker"),
 (220,5,"4)","Case marker"),(220,20,"PROPOSITION 2.","Proposition heading"),(220,28,"COROLLAIRE.","Corollary heading"),
 (221,19,r"Si $k$ pas dénombrable,","Unfinished case lead"),(221,21,"2)","Case marker"),
 (222,15,"COROLLAIRE.","Corollary heading"),(222,18,r"\uline{Exemple} 1.","Example heading"),(222,21,r"\uline{Exemple} 2.","Example heading"),(222,31,r"\uline{Exemple} 3.","Example heading"),(222,40,"PROPOSITION 1.","Heading; statement cut off"),
 (223,17,r"\unsure{Nom}: groupes \uline{fondamentaux \inserted{(arithmétiques)} discrets}.","Proposed name"),
 (226,5,r"2. \uline{Le théorème d'existence et d'unicité}.","Numbered section"),(226,7,"DÉFINITION 2.","Definition heading"),(226,9,"THÉORÈME 1.","Theorem heading"),(226,11,r"A) \uline{Existence}","Proof-part heading")]:
    h(n,l,l,q,k)
for line,label in [(12,"1"),(16,"2"),(18,"3"),(22,"4"),(24,"5")]:
    h(196,line,line,rf"\uline{{n° {label}}}","Editorial subsection")
h(211,33,34,r"\uline{Pts à valeurs dans corps} fini $\mathbb F_q$","Case lead")
h(215,11,12,r"\uline{Analyser l'exemple de Serre de} $\pi_1$ \uline{non isomorphes}","Programme heading")
h(217,3,4,"Lien avec la variété des modules pour des motifs polarisés rigidifiés","Programme lead")
heads.sort(key=lambda x:(x[0],x[1]))

def c(x):return chr(96)+x.replace("|",r"\|")+chr(96)
def ls(a,b):return f"L{a}" if a==b else f"L{a}–{b}"
def frozen():
    d=json.loads((R/"records/frozen_manifest.json").read_text())["sha256"]
    for p,v in d.items():
        if hashlib.sha256((R/p).read_bytes()).hexdigest()!=v:raise RuntimeError("Frozen mismatch: "+p)
    return len(d)
nf=frozen()
pk={}
with (R/(R.name+"_inventory.csv")).open() as f:
    for x in csv.DictReader(f):
        if x["cote"]=="15":pk[int(x["scan"])]=x["sheet_kind"]
ct=Counter(n for n,*_ in rows)
marker_re=re.compile(r"vérif|verif|check|question|\?|je pense|peut-être|il semble|nous laisserons|plus tard|il faut|reste|conject|à revoir|on devrait|il suffirait",re.I)
marker_hits=[]
marker_excluded=[]
for n,lines in S.items():
    for line,s in enumerate(lines,1):
        if not marker_re.search(s):continue
        if not marker_re.search(s.replace(r"\check","")):
            marker_excluded.append((n,line,"Mathematical check accent, not an instruction"))
            continue
        if (n,line)==(222,41):
            marker_excluded.append((n,line,"Ordinary theorem iff wording, cut off by the excerpt boundary"))
            continue
        cover=[i for i,(p,a,b,*_) in enumerate(rows,1) if p==n and a<=line<=b]
        if not cover:raise RuntimeError(f"Unexplained marker hit {n}:{line}: {s}")
        marker_hits.append((n,line,cover))
out=["# Cote 15: author-marked questions, checks and standing steps","",
 "All 34 frozen cote 15 page fragments (195–228) were read as TeX only. No source image was opened. References are to individual page-TeX lines; every quoted marker was matched to that source with only whitespace collapsed. Uncertain readings and quoted alteration macros remain literal.","",
 "The register includes explicit questions, expectations, checks, retractions, unfinished branches, proof/exercise deferrals, and the reused typescripts' editorial requests. Routine proof moves followed by an argument, emphasis alone and mere page breaks are not promoted to open problems. An unexpanded easy/analogous verification is labelled accordingly. Editorial work and mathematical conjecture remain distinct.","",
 "Coverage means coverage by an existing A/R/M observation at review time. The proposed extra notes R12–R26 and A41 are separately flagged; they are not yet assumed adopted. Routine typography, source rearrangement, heading/pagination instructions and programme labels without an identifiable mathematical claim require no extra research note.","",
 "## Register","",
 "| Item | Scan and page TeX lines | Exact short marker(s) | Status | Step or issue | Note IDs | Coverage |",
 "| --- | --- | --- | --- | --- | --- | --- |"]
for i,(n,a,b,q,status,action,notes,cov) in enumerate(rows,1):
    exact=precise_quotes(n,a,b,q)
    quoted="; ".join(c(x)+f" [{ls(line,endline)}:C{column}]" for x,line,endline,column in exact)
    out.append(f"| S15-{i:03d} | 15/{n}:{ls(a,b)} | {quoted} | {status} | {action} | {notes} | {cov} |")
out+=["","## Page coverage","",
 "| Scan | Retained sheet kind | Items | Qualification |","| --- | --- | --- | --- |"]
for n in range(195,229):
    m="See register." if ct[n] else "No standing marker under the stated inclusion rule."
    if n==199:m+=" The case continues on 201 rather than being abandoned."
    if n==216:m+=" R07 is a reader-side domain check, not an author-marked doubt."
    if n==222:m+=" The last proposition is cut off by the excerpt boundary."
    if n in (224,226,228):m+=" Ordinary proof/definition continuations are not author doubts."
    out.append(f"| 15/{n} | {pk[n]} | {ct[n]} | {m} |")
out+=["","## Independent marker sweep","",
 "A separate rg sweep of all 34 frozen TeX files used vérif/verif/check/question/question-mark, expectation, conjecture, revision and deferred-proof terms; the helper also verifies that every resulting substantive line is included in a registered source range. This caught and repaired the two independent à vérifier margins on 15/203 (L17 and L24), and added the required Hodge-type datum at L2.","",
 f"Substantive matching lines covered: {len(marker_hits)}. Unexplained matching lines: **0**. Every quoted marker also has a unique exact-text match, whose actual starting source line and column are printed beside it; thus a broad witness range cannot conceal a wrong quote-line attribution. The excluded hits are listed explicitly below; editorial tasks without these words remain covered by the full-page reading and the main register.","",
 "| Scan/line | Exclusion reason |","| --- | --- |"]
out += [f"| 15/{n}:L{line} | {why} |" for n,line,why in marker_excluded]
out+=["",f"Total: {len(rows)} registered items. All {nf} frozen manifest hashes checked before and after writing. The separate titles register records pagination without inferring a total.",""]
(R/"records/standing_steps_cote15.md").write_text("\n".join(out))
typed={
196:(4,"ALGÈBRES de LIE SEMI-SIMPLES (7)","Tribu n° 59","parenthetical leaf label (7)"),
198:(4,"ALGÈBRES de LIE SEMI-SIMPLES (6)","Tribu n° 59","parenthetical leaf label (6)"),
200:(4,"ALGÈBRES de LIE SEMI-SIMPLES (5)",r"Tribu n° \unsure{57|59}","parenthetical leaf label (5)"),
202:(4,"ALGÈBRES de LIE SEMI-SIMPLES (4)","Tribu n° 59","parenthetical leaf label (4)"),
204:(4,"ALGÈBRES de LIE SEMI-SIMPLES (3)","Tribu n° 59","parenthetical leaf label (3)"),
206:(4,"Tribu n° 59","(n° 400)","Tribu L4; document/redaction identifier L8; no typed leaf number stated"),
208:(2,"SYSTÈMES de RACINES (3)","Tribu n° 59","parenthetical leaf label (3)"),
210:(3,"SYSTÈMES de RACINES (2)","Tribu n° 59","parenthetical leaf label (2)"),
212:(3,"Tribu n° 59","(Rédaction Borel).","Tribu L3; attribution L7; no parenthetical leaf number"),
214:(3,"1 -- 49 --","n° 413","typed locator 1 -- 49 --"),
216:(3,"1 -- 48 --","n° 413","typed locator 1 -- 48 --"),
218:(3,"1 -- 47 --","n° 413","typed locator 1 -- 47 --"),
220:(3,"-- 12 --","n° 370","typed page 12"),222:(3,"-- 9 --","n° 370","typed page 9"),
224:(3,"-- 7 --",r"n\textsuperscript{o}370","typed page 7"),
226:(3,"-- 6 --",r"n\textsuperscript{o}370","typed page 6"),
228:(3,"-- 5 --",r"n\textsuperscript{o}370","typed page 5")}
out=["# Cote 15: titles, headings and separate pagination layers","",
 "Scope: all 34 supplied frozen fragments, scans 195–228, read as TeX only. The primary reader's "+c(r"\mspage")+" layer is reported separately from the reused typescript's own locators and editorial identifiers. A requested new title is not treated as already adopted. No missing leaf, total or chronology is reconstructed.","",
 "## Pagination and typed headers","",
 "| Scan | Recorded manuscript pagination | Typed title/locator and source line | Editorial identifier | Limited interpretation |",
 "| --- | --- | --- | --- | --- |"]
for n in range(195,229):
    mm=list(re.finditer(r"\\mspage\{([^{}]+)\}",T[n]))
    ms="; ".join(c(m.group(0))+f" (L{T[n].count(chr(10),0,m.start())+1})" for m in mm)
    title=ident="—";desc="No typed running header/page locator recorded."
    if n in typed:
        line,title,ident,desc=typed[n]
        if title not in S[n][line-1] or ident not in T[n]:raise ValueError(f"Header mismatch {n}")
        title=c(title)+f" (L{line})";ident=c(ident)
    out.append(f"| 15/{n} | {ms} | {title} | {ident} | {desc} |")
out+=["","## Titles and internal headings","",
 "Included: named/numbered sections, theorem/definition/proposition/example headings, explicit case labels, table-category labels and programmatic paragraph leads. Formula numbers, internal algebraic condition labels, ordinary emphasized assertions and headings merely cited as external references are excluded.","",
 "| Scan and page TeX lines | Exact heading or lead | Function/status |","| --- | --- | --- |"]
for n,a,b,q,k in heads:out.append(f"| 15/{n}:{ls(a,b)} | {c(q)} | {k} |")
noheads=[n for n in range(195,229) if not any(x[0]==n for x in heads)]
out+=["","No local heading under this rule on scans: "+", ".join(map(str,noheads))+". Their typed locators, if present, remain in the first table.","",
 "## Counts and limits","",
 f"- This supplied selection contains **34** fragments, classified by the retained inventory as **{sum(v=='text' for v in pk.values())} text** and **{sum(v=='reused_typed' for v in pk.values())} reused typescript**. These are package counts, not totals stated by the author.",
 "- The recorded manuscript numbers run from 194 through 227, one per scan. Their endpoints do not establish the length of an original document.",
 "- The Lie running headers have leaf labels (7), (6), (5), (4), (3); the root-system headers have (3), (2), then a title leaf without that label. No absent label is supplied, and none is an explicit total.",
 "- Other typed locators are 1 -- 49 --, 1 -- 48 --, 1 -- 47 --, and -- 12 --, -- 9 --, -- 7 --, -- 6 --, -- 5 --. No completeness of the intervening sequence is presumed.",
 "- Tribu n°59 (with the frozen 57|59 alternative on scan 200), n°400, n°413 and n°370 are editorial/document identifiers, not page totals. Rédaction Borel is an attribution.",
 "- **No explicit total number of pages or leaves is stated in these selected frozen texts.** No total is inferred from running titles, leaf labels, document identifiers, referenced page ranges or the supplied scan interval.","",
 f"All {nf} frozen manifest hashes checked before and after writing; all heading quotations mechanically matched to the cited individual-page text.",""]
(R/"records/titles_cote15.md").write_text("\n".join(out))
frozen()
print(json.dumps({"standing_items":len(rows),"headings":len(heads),"pages":34,"frozen_checked":nf},indent=2))
