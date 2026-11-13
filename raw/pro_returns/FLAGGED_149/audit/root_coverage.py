import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]
rows=[
('F8','149 §2; p22; scan45','centralisateur de Gamma′° ... réduit à(1); à vérifier','True as written','F8a','Attached CYCLOTOMIC_KERNEL B1 (proof re-read); arithmetic application in A6'),
('F10','149 §3; pp26–27; scans54–56','Proposition sauf pour(0,3); centralisateur Z(L_i)','False in the allowed type(0,2); hyperbolic statement true including(0,3), with normalizer correction','F10a–F10c','Stix0809.0017 Proposition11,Corollary12,Theorem14'),
('G1','142 pp1–3; scans5–7 (6 before5)','Periodic homological rigidity; isolated fixed points; invariant complex structure; translation','True with stated orientation/homology conventions; n=2 false; doubtful proper-homology readings tested','G1–G3,G11; B4','Constantin–Kolev2.5,3.1,3.3; SGA1XII5.1; explicit proof'),
('G2','142 p3 continuation; scan8','Composantes connexes contractiles; tout sous-groupe fini; orbites fini','Contractibility and finite orbit count true; all-finite-subgroups margin false, free-realization criterion exact','G4–G5','Yagasaki1.1(ii),2.1(i); KerckhoffTheorem1; Farb–Margalit8.8'),
('G3','142 pp4–6; scans9–12','Composition par continuité; mérite d’être faite avec plus de soin; enveloppe','True after Hausdorff closure correction; continuity, associativity and universal property proved','G6–G7,G10','Direct construction and two counterexample categories'),
('G4','142 pp5–6; scans11,14','(*) finite-index lifting; injectif; unique factorization; conservativity','True for surfaces with markings retained; general injectivity hypothesis alone insufficient','G6,G8–G9','Paris1.4; Farb–Margalit8.8; explicit finite-cover lifting'),
('Z142a','142 pp3–6; scans8–9,13','Sign orbits; compact metrizable Hom; no isolated points','First two true; no-isolated-points claim false in type(0,3)','Z142a','Farb–Margalit4.9,4.11; direct quotient proof'),
('Z142b','142 pp6–7; scans13–16','Purely algebraic description; moduli paths; base-change equivalence','True in characteristic zero with Hurwitz-stack transport and marked factorization','Z142b','Bertin–Romagny6.8,6.9,6.14,6.20; Noohi20.4; BrescianiA.22,A.23'),
('Z142c','142 p7; scans15–16','Pas besoin car0; fundamental group unchanged after algebraically closed extension','Full-curve base-invariance premise false in characteristic p; exact replacements proved','Z142c','SGA1X1.8,XIII2.9,2.12; Artin–Schreier counterexample'),
('Z142d','142 pp7–8; scans16–17','Aut(k) acts; classes classified by types; completed Teichmüller groups','True in the characteristic-zero construction, with explicit outer ambiguity','Z142b,Z142d','Noohi20.4; base-change proof'),
('Z142e','142 pp8–9; scans18–19','Reasonable isotopy equals two-sided identity-component orbit','Ordinary-path reading false even for composites of the allowed generators; fixed Hurwitz-incidence local statement proved; adjective remains unspecified','Z142e','Explicit degree-six composite; exact discriminants and critical values in G_checks.py'),
('Z142f','142 pp8–10; scans18,20–21','Filling holes; source containment; forgetful functor and transitivity','True with remaining hyperbolic-type restriction and exact ramification containment','Z142f','Direct map and moduli-stack construction'),
('Z142g','142 pp7–10; scans15–21','Wild category; intrinsic arithmetic image; completion with hole fillings','UNRESOLVED objectives: constructions and failed transfer steps recorded precisely','Z142g','Z142b–Z142f; no theorem asserted for the remaining programmes')]
keys=['row','scan','words','verdict','statements','source_opened']
(p/'ROOT_coverage.json').write_text(json.dumps([dict(zip(keys,r)) for r in rows],ensure_ascii=False,indent=2)+'\n')
