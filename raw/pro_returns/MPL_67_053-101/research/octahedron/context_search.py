"""Record targeted closed-context searches for each octahedron research note."""
from pathlib import Path
import re,json,subprocess
from datetime import datetime,timezone
root=Path('context')
queries={
'O01':[r'bitranspositions',r'partitions de type',r'V\(I\)',r'549',r'554'],
'O02':[r'normalisateur',r'normaliser',r'Toutes les actions fidèles',r'octaédral'],
'O03':[r'caractéristique différente de',r'characteristic 5',r'char. 5',r'GP.*F_5'],
'O04':[r'catégorie.*octaèdres',r'octaédrales',r'antipodisme',r'equivalence.*octa'],
'O05':[r'scindages',r'stabilisateur.*face',r'face seule',r'paires de faces'],
'O06':[r'H.*mathfrak',r'supplémentaires',r'quatre.*scind',r'quatre sous-groupes'],
'O07':[r'racine carrée de',r'mu_4',r'orientation combinatoire',r'S.*Gamma'],
'O08':[r'milieux d.arêtes',r'centres de faces',r'ramification',r'caractéristique.*3'],
'O09':[r'involution sans point fixe',r'S.*sigma',r'orientations',r'octa-quart'],
'O10':[r'I\(V\)',r'orbite.*torseur',r'face.*torseur'],
'O11':[r'produit contracté',r'tordu',r'X\(T',r'torsor',r'à expliciter'],
'O12':[r'z\^2',r'q\(z\)',r'trois points de ramification',r'Sigma\(J\)'],
'O13':[r'groupoïde des couples',r'automorphismes se correspondent',r'grossier',r'M_\{0,4\}\^'],
'O14':[r'droite projective.*réelle',r'lettre.*Sigma',r'X barré',r'construction.*raturée'],
'O15':[r'revêtement octaédral',r'courbe de Fermat',r'568',r'571'],
'O16':[r'PUSH_ORDER5_FRAME',r'C.12',r'M_\{0,5\}',r'niveaux',r'deux niveaux']
}
# Exact queries are retained, including zero-hit queries. Lines are bounded only
# in the saved excerpts; full hit counts and paths remain available.
results=[]
cache={}
for path in root.rglob('*'):
 if not path.is_file():continue
 lines=path.read_text().split('\n');scan=None;heading='';locations=[]
 for line in lines:
  m=re.search(r'\\scanpage\{([^}]+)\}',line)
  if m:scan=m[1]
  if line.startswith('#') or re.match(r'\\(?:sub)?section',line):heading=line
  locations.append((scan,heading))
 cache[str(path)]=locations
for note,patterns in queries.items():
 qres=[]
 for pattern in patterns:
  cp=subprocess.run(['rg','-n','-i','--no-heading','-e',pattern,str(root)],text=True,capture_output=True)
  assert cp.returncode in (0,1),(pattern,cp.stderr)
  hits=[]
  for line in cp.stdout.split('\n'):
   if not line:continue
   path,num,text=line.split(':',2)
   number=int(num)
   scan,heading=cache[path][number-1]
   hits.append({'path':path,'line':number,'nearest_scan':scan,'nearest_heading':heading,'excerpt':text[:450]})
  qres.append({'query':pattern,'total_hits':len(hits),'hits':hits[:100],'saved_excerpt_limit':100})
 results.append({'note_id':note,'searched_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'queries':qres})
Path('MPL_67_053-101/research/octahedron/search_ledger.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print('Saved per-note searches:',len(results))
for item in results:print(item['note_id'],[(q['query'],q['total_hits']) for q in item['queries']])
