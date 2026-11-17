#!/usr/bin/env python3
"""Record actual note-specific searches of the supplied, post-freeze context."""
import json, subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[2]
queries={
 'R01':r'Q_0|Q_\{0\}|Aut\^\+|rotations|carré combinatoire',
 'R02':r'natural|flat|épinglage de Legendre sur une base|tensor',
 'R03':r'épinglages de Legendre|torseur|alpha',
 'R04':r'hexagonal|rigide|automorphismes|1728',
 'R05':r'Legendre.pinning.moduli|schéma de modules|Jacobi|niveau.?2',
 'R06':r'D._3|D.?.?.?3|produit fibré|extension centrale',
 'R07':r'abélianisé|abelianization|chi_4|caractère canonique',
 'R08':r'action à droite|action à gauche|tautologique|caractère',
 'R09':r'1728|invariant.?j|équianharmonique|hexagonal|LM4 D.12',
 'R10':r'caractéristique.?3|characteristic.?3|hexagonal|points fixes',
 'R11':r'courbe standard|universelle|Kummer|T_0',
 'R12':r'Explicitation calculatoire|forme linéaire|coefficients|73',
 'R13':r'naïf|naif|Legendre|sqrt\{-1\}',
 'R14':r'LM7_PUSH E.3|LM6 A.22|CM|1728',
 'R15':r'Descriptions explicites|Weierstrass|pages 100|page 100',
 'R16':r'base canonique|k\^J|V_J|Explicitation calculatoire'
}
out=root/'MPL_64_078-115'/'records'
(out/'root_context_queries.json').write_text(json.dumps(queries,ensure_ascii=False,indent=2)+'\n')
blocks=[]; summary=[]
for key,pattern in queries.items():
    p=subprocess.run(['rg','-n','-i','--',pattern,str(root/'context')],text=True,capture_output=True)
    if p.returncode not in (0,1):raise RuntimeError(p.stderr)
    hits=p.stdout.splitlines()
    blocks.append(f'## {key}\nQuery: {pattern}\nMatches: {len(hits)}\n'+p.stdout+'\n')
    summary.append({'note':key,'query':pattern,'matches':len(hits),'first_hits':hits[:3]})
(out/'root_context_searches.txt').write_text('\n'.join(blocks))
(out/'root_context_search_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'note':x['note'],'matches':x['matches']} for x in summary],indent=2))
