"""Per-item context searches for the post-freeze research notes."""
from pathlib import Path
from datetime import datetime, timezone
import json
import subprocess

base = Path(__file__).resolve().parents[1]
context = base.parent / 'context'
assert (base / 'research/frozen_sha256.json').exists()
rows = [
('P01','002–044','Scope and planning disposition','K_G|Greenberg|Néron|Hom functors|rank 20'),
('P02','002,026','Chronology and the two covers','1966|1967|couverture|XVII|XIII'),
('N01','003','Integral alternating tensor line','symétrie|anti-invariants|n!|déterminant'),
('N02','003–005','Canonical norm section','polynôme|Can_|section canonique'),
('N03','005,013','Nonreduced finite flat fibres','multiplicité|localement libre|fini et plat'),
('N04','005','Trace from the norm','trace|Deligne|norme'),
('N05','005,007','Symmetric target and functoriality','morphisme symétrique|factorise|fonctorialité'),
('N06','007,012','Disjoint sums and multiplicativity','Additivité|additivité|sommes|amalg'),
('N07','005,007,009,012','Norm transitivity left unproved','transitivité|Je dis que|ii ter'),
('N08','011','Axioms and quotient closure','quotient|v bis|98-axiomatic-norms-can-section'),
('N09','011–013','Orbit-sum degree computation','permutation|orbites|card|quotPow'),
('N10','011–013','Empty-target degree convention','deg|hasDeg|identités|vide'),
('N11','012–013','Finite G-set multiset model','multi-ensemble|G-ensembles|can_comp'),
('N12','013','Finite flat versus finite locally free','présentation finie|fini et plat|localement libre'),
('N13','014','Contracted product and covering hypotheses','proprement|contracté|non ramifié|développer'),
('N14','002–009,026–044','Hilbert–Chow link','Hilbert--Chow|Hilbert.Chow|puissance divisée'),
('G01','016,018','Finite-orbit site and missing fibre products','nombre fini|produits fibrés|comparaison'),
('G02','016','Recovering the group action','translations|contravariant|Hom_G'),
('G03','018,020','Cohomology presheaf versus sheaf','préfaisceau|hyper-faisceau|Shapiro'),
('G04','018','Čech spectral sequence and coinduced contraction','coïnduit|injectif|acyclique|suite spectrale'),
('G05','018,020','Shapiro and orbit conventions','Shapiro|F \\backslash G|G/F'),
('G06','020','Relative sequence and Hochschild–Serre','Hochschild|F/F|pas essentiellement'),
('G07','020','Requested generalisation to arbitrary sheaves','généraliser|hyperrecouvrement|Verdier'),
('G08','022','Picard row and Brauer edge sequence','Pic|ligne|d_3|Brauer'),
('G09','024','Local coefficient systems','système local|coefficients locaux|Serre'),
('G10','024','Group–subgroup and quotient fibrations','Quatre fibrations|sous-groupe|distingué'),
('G11','016–024','No finite-homotopy or section result follows','FINMON|LM7 E.23|FLAGGED_149 B9|LM4 D.12'),
('B01','027–028','Fixed quotient and Hilbert polynomial boundedness','quotients|Hilbert|Theorem 2|Chow'),
('B02','027–028','Top-dimensional cycle data need lower support control','cycles|dimension|pure|longueur'),
('B03','028','Induction requires bounded kernels','noyaux|L\x27\x27|récurrence|extension de faisceaux'),
('B04','028,034','Properness for variable morphisms and extensions','morphismes|monomorphismes|extensions|propre'),
('B05','029','Field amalgamation over the middle field','amalgamation|K_2|dominées'),
('B06','029–030','Finite-type descent of sheaves and isomorphisms','type fini|Proposition 1|Chap. V'),
('B07','030,033','Arbitrary compositum counterexample','Question|universelle|composées|positions'),
('B08','030','Withdrawn base-field invariance','barré|contravariant|corps de base'),
('B09','031','Universal algebraically closed field and automorphism orbits','transcendance|Aut|Corollaire 5'),
('B10','030–031','Set size and finite-presentation qualification','univers|type fini|plongements'),
('B11','032–033','Multivalued operations and relative positions','toutes|extensions composées|T(F'),
('B12','034','Reduced support and inseparability','réduit|irréductible|inséparable|primaire'),
('B13','034','Primary components and noncanonical choices','filtration primaire|composantes primaires|quotients successifs'),
('B14','035','Tensor boundedness through product of parameter spaces','produit fibré|S\x27\x27\x27|tensoriel'),
('B15','035–036','Hom base change and generic flattening','Hom|conoyau|platitude générique'),
('B16','036–037','Finite stratification of complex cohomology','récurrence noethérienne|cocycles|cobords'),
('B17','036–037,044','One finite degree range at a time','borné|N + 1|degrés|complexes'),
('B18','039–040','Wrong-ring free resolution in Tor proof','résolution libre|B_i|bigotimes|Künneth'),
('B19','039–040','Missing module flatness refuted','F_i plats|M_i|plat|Lemme'),
('B20','040–041','Corrected Tor base-change mechanism','Künneth|Tor|différentielle|plat'),
('B21','039,041','Dense open and noetherian stratification','ouvert dense|ouvert non vide|ensembliste'),
('B22','042','Finite free truncation versus no finiteness','sans conditions de finitude|résolution|N + 1'),
('B23','042–043','Terminal cokernel flatness is essential','conoyau|C^{N+1}|Ext'),
('B24','043','All degrees of K versus the Ext range','tt|dimension|en particulier|C^{p}'),
('B25','042','Canonical comparison maps must glue','recollent|lecteur|locale'),
('B26','037,044','Tor in fixed degree versus all degrees','Tor_i|Tor|borné|limité'),
('B27','034,044','Proper direct images and coherence','propres|directes|R^{p}|cohérent'),
('B28','044','Relative Ext and the qualification quand ça marche','quand ça marche|en tout cas|Altman|7.7'),
('B29','044','Base-change detection needs a finiteness scope','réciproque|image|base|noethérien'),
('B30','044','Finite union and chapter programme','réunion finie|plan d.un chapitre|Prop. 1'),
('T01','004,006,008,010','Reused topology sheets are distinct evidence','tapuscrit|329|topologie|skipped'),
('T02','006','Subspace quotient criterion and literal trace typo','quotient|topologie|329'),
('T03','004,008,010','Products and gluing','produits|recollement|topologie|329'),
('T04','015','Theorem of the square and additive Picard pullback','abelian|abélienne|Picard|LM7 C.1|LM7 C.5'),
('T05','017','Kernel of the Picard homomorphism','Picard|Néron|WG H9|268'),
('T06','019,021,023','Jet flags and the last nonzero linear subsystem','linéaire|268|tapuscrit'),
('T07','019','Full-rank homogeneous equations do not give a divisor','rang|268|tapuscrit|90'),
('T08','023','Power-series lower limit is a reading issue','268|tapuscrit|série'),
('T09','025','Projectivity and historical ampleness terminology','abelian|abélienne|projectif|ample|268'),
('T10','019','Pencil marks and attribution limit','Prouver|crayon|page 18|Nouveau'),
('R01','002','XVII versus XVIII on the cover','XVII|XVIII|couverture'),
('R02','007,011–013','Cor/Cn versus Hua Can','Can|Cm|canonique'),
('R03','030–033','Phi/Cl versus Hua gothic F','gothic|mathfrak|classes géométriques'),
('R04','030–031','Compositum question and corollary numbering','Corollaire 5|universelle|Question'),
('R05','014,016','Unfinished assertion and Hom argument','on suppose|Hom_G|E pour A|s.interrompt'),
('R06','034','Example labels and the deleted final item','rebaptisé|ligne (i)|omise|Exemples'),
('R07','041–043','Coefficient alphabets and A-flat wording','A-libres|Hom_A|O_{S|A-plats'),
('R08','044','The adjective after familles','universelles|plan d.un chapitre'),
]

# Escape accidental unbalanced literal parentheses in selected mathematical search strings.
fixes={'B11':r'toutes|extensions composées|positions relatives',
       'B23':r'conoyau|terminal|Ext',
       'B24':r'tt|dimension|en particulier|conoyaux',
       'B27':r'propres|directes|cohérent',
       'R06':r'rebaptisé|ligne|omise|Exemples',
       'R07':r'A-libres|Hom_A|A-plats|coefficient'}
ledger=[]
for ident,scans,title,query in rows:
    query=fixes.get(ident,query)
    p=subprocess.run(['rg','--line-number','--ignore-case','--max-count','12',query,str(context)],capture_output=True,text=True)
    if p.returncode not in (0,1):
        raise RuntimeError(ident+': '+p.stderr)
    loc=[]
    for line in p.stdout.splitlines():
        parts=line.split(':',2)
        if len(parts)==3:
            loc.append({'file':str(Path(parts[0]).relative_to(context)), 'line':int(parts[1])})
    ledger.append({'id':'MPL98.'+ident,'scans':scans,'title':title,'query':query,
                   'searched_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
                   'exit_status':p.returncode,'matches':loc})
(base/'research/context_searches.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in ledger))
(base/'research/note_plan.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
print(f'Ran and recorded {len(ledger)} separate note-specific context searches.')
