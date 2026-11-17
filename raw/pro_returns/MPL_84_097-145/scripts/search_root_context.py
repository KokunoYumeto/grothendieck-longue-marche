#!/usr/bin/env python3
"""Record actual per-item context searches; does not read or alter scan images/TeX."""
from pathlib import Path
import json,re

ROOT=Path(__file__).resolve().parents[1]
CONTEXT=ROOT.parent/'context'
QUERIES={
 'C01':['B12','conic','Azumaya','ternary','SO(3)','P¹'],
 'C02':['rank-four','commutative','A₁⊗A₂','84-product-quadratic-algebras-formula'],
 'C03':['torsor','PGL','χ-trivial','line bundle'],
 'C04':['Clifford','Voight (2021','5.2','B12'],
 'C05':['B5','C.d5','B.f7','regular polyhedron','congruence'],
 'C06':['480','475 bis','pagination','8.2.'],
 'C07':['1984','July 1976','juillet 1976','eight-year','1979'],
 'C08':['Désir et méditation','Section 39','L’émerveillement','36'],
 'D01':['holocauste','nuclear','destructive imbalance','T179.1','T179.2'],
 'D02':['complementarity','balance','T187.1','T169.1'],
 'D03':['mechanisms','childhood','T171.3'],
 'D04':['three periods','juillet 1976','T167.2','T171.4'],
 'D05':['mother','hatred','mystère','T153.2'],
 'D06':['Weil','Deligne','standard conjectures','T151.1','T165.4'],
 'D07':['standard conjectures','cycles algébriques','motifs','T191.1','T191.2'],
 'D08':['résolution des singularités','resolution of singularities','fécondité','T169.5'],
 'D09':['identification à mon père','approval','T153.2','T165.2'],
 'D10':['eighth year','basculement','T153.1','1933–1942'],
 'D11':['mystère','accept','T169.1','T153.2'],
 'D12':['acceptance','approval','T157.4','T159.1','T171.2'],
 'D13':['dominante','dominant','T169.1','T169.4'],
 'D14':['yin','signes','creative','T191.3'],
 'D15':['doll','humiliation','acceptance','T159.1'],
 'D16':['1933','1979','1980','T153.4'],
 'D17':['474','475','473','T153.4'],
 'D18':['Blankenese','pastor','99','1939'],
 'D19':['17 octobre 1976','reunion','dream','T151.2','T155.1'],
 'D20':['superfather','super-mâle','resentment','T165.1','T165.4'],
 'D21':['nearly three','avoidance','T151.3','T155.4','T169.4'],
 'D22':['two repressive','l’une de ces deux','T153.1'],
 'D23':['unconscious','choice','T165.1','T171.3'],
 'D24':['quatre parmi','cinquième','five children','T153.1'],
 'P01':['title sheet','page count','8.1.','8.2.'],
 'P02':['Désir et méditation','Yang enterre yin','Eclosion','massacre'],
 'S01':['question','uncertain','compatib','7.1.','7.2.'],
 'RS01':['84-product-quadratic-algebras-formula','84-chi-trivialised-extension-product','MPL_84_146-193'],
 'RS02':['refereed','LM2','LM4','LM7','WG2 §1.1 #3'],
}

files=sorted(CONTEXT.rglob('*.md'))
results=[]
for note,terms in QUERIES.items():
 item={'item':note,'queries':[]}
 for term in terms:
  q={'literal_case_insensitive':term,'files':[]}
  for p in files:
   lines=p.read_text().splitlines()
   hits=[{'line':i,'excerpt':s[:220]} for i,s in enumerate(lines,1) if term.casefold() in s.casefold()]
   q['files'].append({'file':p.relative_to(CONTEXT).as_posix(),'hit_count':len(hits),'first_hits':hits[:6]})
  item['queries'].append(q)
 results.append(item)
(ROOT/'research/root_context_searches.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
md=['# Per-item context search record (root notes)','',
    'Literal, case-insensitive searches of all four supplied Markdown context files. Counts include incidental matches; relevance is judged in the notes. An earlier note is a lead, not a verified manuscript reading. Only a few short hit excerpts are stored per file, not copies of the source documents.','']
for item in results:
 md += ['## '+item['item'],'']
 for q in item['queries']:
  md += ['- Query `'+q['literal_case_insensitive']+'`: '+ '; '.join(f"{f['file']} — {f['hit_count']} hit(s)"+((' at lines '+','.join(str(h['line']) for h in f['first_hits'])) if f['first_hits'] else '') for f in q['files'])+'.']
 md.append('')
(ROOT/'research/root_context_searches.md').write_text('\n'.join(md)+'\n')
print(f'Recorded {len(results)} item search sets in {len(files)} supplied context files.')
