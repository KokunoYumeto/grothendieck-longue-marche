"""Item-by-item searches of the supplied context, after transcription freeze."""
from pathlib import Path
import json,subprocess
ROOT=Path(__file__).resolve().parents[1]
CONTEXT=ROOT.parent/'context'
PLAN=[
 ('S01',['cinq sujets','Réarrangements sur un groupe','162-1','162-6']),
 ('S02',['none of ours','None of ours','E.3','C2-CP2','Delta']),
 ('G01',['Gagnantes, perdantes, nulles','C \\smallsetminus (G \\cup P)','convention dite normale']),
 ('G02',['Caractérisation sans parties infinies','Pris à la lettre','positions non terminales']),
 ('G03',['construction récurrente','ordinal','cardinal au plus','bon ordre']),
 ('G04',['noyau du graphe','Sprague','parties infinies']),
 ('G05',['Jeux à $N$ joueurs','permutation circulaire','unique dès']),
 ('G06',['condition de gain','coalition','Jeux à $N$ joueurs']),
 ('E01',["L’exponentielle des éléments nilpotents","L'exponentielle des éléments nilpotents",'séries formelles','exp 1']),
 ('E02',['Exemple 2','mais avec','nilidéal','nilpotent']),
 ('E03',['M/JM','Hom','projectif de type fini','conditions de la remarque']),
 ('E04',['Groupes formels à un paramètre','Yoneda','polynôme']),
 ('E05',['Opérations sur un module','localement nilpotents','suite d\'endomorphismes','nuls à partir']),
 ('E06',['Morphismes, et le passage','c_{ij}','Hom}_K(M, N)','log$ est un polynôme']),
 ('E07',['Tenseurs, dérivations','non nécessairement associative','Leibniz']),
 ('E08',['toute rigueur','projectif de type fini','Foncteurs en modules']),
 ('E09',['Foncteurs en modules','On ne tranche pas','bijectives','réduit','nilradical']),
 ('E10',['localement nilpotents','log$ est un polynôme','Morphismes, et le passage']),
 ('E11',['Globalisation','chaque section','translation','nilradical']),
 ('E12',['Globalisation','avec un signe','composition','Theta +']),
 ('E13',['Automorphismes unipotents','commutateurs itérés','opérateur différentiel']),
 ('E14',['gr}_J','gr}_I','2e','unipotent']),
 ('E15',['est-il','Pour ceci','équivalentes','automorphismes unipotents']),
 ('E16',['opérateur différentiel','ordre','noethérien','nilradical']),
 ('E17',['K$-linéaire','K$-algèbre','log u']),
 ('E18',['Theta(I)','I^2','gr}_I','nilidéal','Exemple 2']),
 ('O01',['Deux lemmes','produit contracté','lemme 2','Lean']),
 ('O02',['Les axiomes','68-orientation-stokes-axioms','bijectivité','cardinal']),
 ('O03',['Hom.bijective','Hom.ext','exists_unique_hom','existence c)']),
 ('O04',['Réduction au signe du déterminant','transvection','epsilon_n','stabilisateur']),
 ('O05',['normale','rentrante','sortante','normalisation']),
 ('O06',["I(\\omega, \\omega')",'Produits, et composition','drapeau']),
 ('O07',['quadrant','Koszul','Stokes et produits','carré']),
 ('O08',['(-1)^?','signe','Produits, et composition']),
 ('O09',['composantes connexes','contrainte de Koszul','rapprochement']),
 ('D01',['Les déterminants gradués','groupoïde monoïdal','rang $1$','Picard']),
 ('D02',['varphi_{W_1','lambda','quatre flèches','mathbb{P}']),
 ('D03',['supplémentaires','Ce qui équivaut','transvections','V/W_1']),
 ('D04',['SK_1','anneau quelconque','transvections','déterminant']),
 ('D05',['pour $V$ de rang','naturels','foncteur monoïdal','degré $1$']),
 ('D06',['libres de rang','projectifs','Picard','Les déterminants gradués']),
 ('T01',['épousailles','trois exemplaires','tapuscrit','non transcrit']),
 ('T02',['collier','Récoltes','yin','yang','état']),
 ('T03',['82','attribuer','pagination de sa main']),
 ('U01',['réciproque','indéterminées','lambda, \\mu']),
 ('U02',['Foncteurs en modules','On ne tranche pas','bijectives']),
 ('U03',['est-il nécessaire','La réponse est non','Pour ceci']),
 ('U04',['Existence','existence','68-orientation-stokes-axioms']),
 ('U05',['(-1)^?','vérifier','illisible','53']),
 ('P01',['Exponentielles','Groupes formels','Globalisation','Jeux à $N$','déterminants gradués']),
 ('P02',['XVIII','82','épousailles','pages']),
 ('P03',['pagination','pages{1}{55}','blanches','rank 25']),
 ('X01',['La norme','sign','norme adélique','composantes connexes','epsilon_1']),
]
assert len({x[0] for x in PLAN})==len(PLAN)
records=[]
for ident,terms in PLAN:
    cmd=['rg','-n','-i','-F']
    for term in terms:cmd+=['-e',term]
    cmd+=[str(CONTEXT)]
    result=subprocess.run(cmd,capture_output=True,text=True)
    assert result.returncode in (0,1),(ident,result.stderr)
    hits=result.stdout.replace(str(CONTEXT)+'/', 'context/').splitlines()
    records.append({'id':ident,'terms':terms,'hit_count':len(hits),'hits':hits})
(ROOT/'records'/'context_searches.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
(ROOT/'records'/'research_outline.json').write_text(json.dumps([{'id':x[0],'queries':x[1]} for x in PLAN],ensure_ascii=False,indent=2)+'\n')
print('\n'.join(f"{r['id']}: {r['hit_count']} context hits" for r in records))
