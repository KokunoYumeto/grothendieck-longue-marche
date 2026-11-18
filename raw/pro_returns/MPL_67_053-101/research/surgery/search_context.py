"""Reproducible, note-by-note searches of the supplied context only."""
from pathlib import Path
import subprocess,json
from datetime import datetime,timezone
base=Path(__file__).resolve().parents[3]
ctx=base/'context'
queries={
'S01':r'torique|unitaire|dualité',
'S02':r'topologie|Théorème 1|restriction.*Int',
'S03':r'faisceau|germes|continues.*holomorph',
'S04':r'Schwarz|Schwartz|réflexion',
'S05':r'a_n|dérivée.*annule|n = 1',
'S06':r'Alling|Greenleaf|double.*complex|bord dans le bord',
'S07':r'Carath|rectifiabil|arc de Jordan',
'S08':r'f\(0\)|extrémité|Lemme 2',
'S09':r'régularité|rive|Scholie',
'S10':r'Théorème 4|recollement|welding',
'S11':r'lemme 3|demi-disque|repliement',
'S12':r'rectifiable|effaçable|Morera|Besicovitch',
'S13':r'compact maximal|disque pointé|structure torique',
'S14':r'ombre|shadow|Q1-07|homothét',
'S15':r'canonique.*bord|choix d.un point|disque fermé',
'S16':r'admissibl|coïncid|Q1-07',
'S17':r'Bergman|géodésique|géométrie intrinsèque',
'S18':r'fibration|fibre|C\.12|bouchage',
'S19':r'longueurs|ne dépend|quartiers d.orange',
'S20':r'Koebe|ombres|bijective|Q1-07',
'S21':r'fibré principal|surjectiv|ombre|Q1-07',
'S22':r'section canonique|métrique canonique|sphère.*marqu',
'S23':r'lemme 4|Lemme 4|uniformisation|soudure',
'S24':r'simplement transitive|triples|prime end',
'S25':r'absolument contin|rectifiable|homeomorph',
'S26':r'f\(0\)|f\(1\)|normalise|extrémité',
'S27':r'séries entières|convergence|coefficien',
'S28':r'stable|stabilisation|stabilization|A\.5',
'S29':r'propagation|plombage|tensor|F\.43|E\.35',
'S30':r'dimension|M_st|mdt|E\.35',
'S31':r'isomorphismes|inverse|conjecturale',
'S32':r'géodésique|homotop|coutures',
'S33':r'vaseux|faux|rayons|plombage',
'S34':r'étale|tangente|Fenchel|O\.20|E\.45',
}
rows=[]
for note,pattern in queries.items():
 p=subprocess.run(['rg','--json','-i','-e',pattern,str(ctx)],capture_output=True,text=True)
 if p.returncode not in [0,1]:raise RuntimeError(p.stderr)
 matches=[]
 for line in p.stdout.splitlines():
  e=json.loads(line)
  if e['type']=='match':
   d=e['data'];matches.append({'file':str(Path(d['path']['text']).relative_to(ctx)),'line':d['line_number'],'excerpt':d['lines']['text'].strip()[:220]})
 counts={};kept=[]
 for m in matches:
  counts[m['file']]=counts.get(m['file'],0)+1
  if counts[m['file']]<=4:kept.append(m)
 rows.append({'note_id':note,'utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'command':['rg','--json','-i','-e',pattern,'context/'],'total_matching_lines':len(matches),'counts_by_file':counts,'sample_hits':kept,'limit':'First four matching lines per file retained; counts include every matching line. Exact chosen section/scan is cited in the note.'})
 print(note,len(matches),'matching lines in',len(counts),'files')
Path(__file__).with_name('search_ledger.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
