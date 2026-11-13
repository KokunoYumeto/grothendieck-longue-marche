#!/usr/bin/env python3
"""Assemble the self-contained LM4 paper and merge checked source metadata."""
from pathlib import Path
import re, json, csv, hashlib

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'deliverable'
PREFIX = 'LM4_FINITE_GROUP_ACTIONS'
FRAGMENTS = [
 'work/part_a/a.tex', 'work/part_b/b.tex', 'work/part_b/b25.tex', 'work/part_b/b26.tex',
 'work/part_b/b27.tex', 'work/part_b/b28.tex', 'work/part_b/b29.tex',
 'work/part_c/b_extra.tex', 'work/root/b_higher.tex', 'work/part_c/b34.tex',
 'work/part_b/b36.tex', 'work/part_c/b37.tex', 'work/part_b/b38.tex', 'work/part_c/b39.tex',
 'work/part_c/b40.tex', 'work/part_b/b41.tex',
 'work/part_c/c.tex', 'work/part_b/c26.tex', 'work/part_b/c27.tex', 'work/part_b/c28.tex', 'work/part_b/c29.tex', 'work/part_b/c30.tex', 'work/part_b/c31.tex', 'work/part_b/c32.tex', 'work/part_b/c33.tex', 'work/part_b/c34.tex', 'work/part_b/c35.tex', 'work/part_b/c36.tex', 'work/part_b/c37.tex', 'work/part_b/c38.tex', 'work/part_b/c39.tex', 'work/part_b/c40.tex', 'work/part_b/c41.tex', 'work/part_b/c42.tex', 'work/part_b/c43.tex', 'work/part_b/c44.tex', 'work/part_b/c45.tex', 'work/root/c46.tex', 'work/part_b/c47.tex', 'work/root/c48.tex', 'work/part_b/c49.tex', 'work/part_b/c50.tex', 'work/root/c51.tex', 'work/part_b/c52.tex', 'work/root/c53.tex', 'work/part_b/c54.tex', 'work/root/c55.tex', 'work/root/c56.tex', 'work/part_b/c57.tex', 'work/root/d.tex', 'work/part_a/gt_shadow.tex',
 'work/part_a/gt_shadow_all_prime.tex', 'work/part_a/haran_rank3.tex',
 'work/root/d_rank2.tex', 'work/part_a/gt_torsion_sections.tex', 'work/root/d_marked_counterexample.tex', 'work/part_c/d30.tex', 'work/part_a/sphere_completion_restriction.tex', 'work/part_c/d32.tex', 'work/part_c/ls2_lemma9_audit.tex', 'work/part_c/d33.tex', 'work/part_c/d34.tex',
 'work/part_a/pure_involution_conjugacy.tex', 'work/part_c/d36.tex', 'work/part_c/d37.tex', 'work/part_a/a5_involution_obstruction.tex', 'work/part_a/haran_torus_test.tex', 'work/root/d40.tex', 'work/part_c/d41.tex', 'work/part_a/pants_order_three.tex', 'work/part_c/d43.tex', 'work/part_a/pure_involution_first_symmetry.tex',
 'work/part_a/a5_schur_refinement.tex', 'work/part_c/d46.tex',
 'work/part_a/pure_involution_binary_conjugacy.tex', 'work/part_c/d48.tex', 'work/part_a/standard_involution_centralizer.tex', 'work/part_c/d50.tex', 'work/part_c/d51_note.tex', 'work/part_c/d52.tex', 'work/part_c/d53.tex', 'work/part_c/d54.tex', 'work/part_c/d55.tex', 'work/part_a/d56.tex', 'work/part_a/d57.tex', 'work/part_c/d58.tex', 'work/part_c/d59.tex',
 'work/part_c/ea.tex', 'work/root/eb.tex', 'work/root/f.tex', 'work/root/f_arithmetic.tex', 'work/part_a/f_centralizer_audit.tex', 'work/part_a/f_seven_point_continuation.tex', 'work/part_a/f_seven_point_kernel.tex', 'work/part_a/f_procyclic_exclusion.tex']
METADATA = ['work/part_a/results.json', 'work/part_b/results.json',
 'work/part_b/b25_result.json', 'work/part_b/b26_result.json', 'work/part_b/b27_result.json',
 'work/part_b/b28_result.json', 'work/part_b/b29_result.json',
 'work/part_c/b_extra_results.json', 'work/root/b_higher_result.json', 'work/part_c/b34_result.json',
 'work/part_b/b36_result.json', 'work/part_c/b37_result.json', 'work/part_b/b38_result.json', 'work/part_c/b39_result.json',
 'work/part_c/b40_result.json', 'work/part_b/b41_result.json',
 'work/part_a/gt_shadow_results.json', 'work/part_a/gt_shadow_all_prime_results.json',
 'work/part_a/haran_rank3_results.json', 'work/root/d_rank2_results.json', 'work/part_a/gt_torsion_sections_results.json', 'work/root/d_marked_counterexample_results.json', 'work/part_c/d30_result.json', 'work/part_a/sphere_completion_restriction_results.json', 'work/root/f_arithmetic_results.json', 'work/part_a/f_centralizer_audit_results.json', 'work/part_c/results.json',
 'work/root/results.json', 'work/part_c/d32_result.json', 'work/part_c/d33_result.json', 'work/part_c/d34_result.json', 'work/part_a/pure_involution_conjugacy_results.json', 'work/part_c/d36_result.json', 'work/part_c/d37_result.json', 'work/part_a/a5_involution_obstruction_results.json', 'work/part_a/haran_torus_test_results.json', 'work/root/d40_result.json', 'work/part_c/d41_result.json', 'work/part_a/pants_order_three_results.json', 'work/part_c/d43_result.json', 'work/part_a/pure_involution_first_symmetry_results.json', 'work/part_b/c26_result.json', 'work/part_b/c27_result.json', 'work/part_b/c28_result.json', 'work/part_b/c29_result.json', 'work/part_b/c30_result.json', 'work/part_b/c31_result.json', 'work/part_b/c32_result.json', 'work/part_b/c33_result.json', 'work/part_b/c34_result.json', 'work/part_b/c35_result.json', 'work/part_b/c36_result.json', 'work/part_b/c37_result.json', 'work/part_b/c38_result.json', 'work/part_a/a5_schur_refinement_results.json', 'work/part_c/d46_result.json', 'work/part_b/c39_result.json', 'work/part_b/c40_result.json', 'work/part_b/c41_result.json', 'work/part_a/f_seven_point_continuation_results.json', 'work/part_a/pure_involution_binary_conjugacy_results.json', 'work/part_c/d48_result.json', 'work/part_a/standard_involution_centralizer_results.json', 'work/part_c/d50_result.json', 'work/part_c/d51_result.json', 'work/part_b/c42_result.json', 'work/part_c/d52_result.json', 'work/part_b/c43_result.json', 'work/part_b/c44_result.json', 'work/part_b/c45_result.json', 'work/root/c46_result.json', 'work/part_c/d53_result.json', 'work/part_c/d54_result.json', 'work/part_c/d55_result.json', 'work/part_b/c47_result.json', 'work/root/c48_result.json', 'work/part_a/d56_result.json', 'work/part_a/d57_result.json', 'work/part_b/c49_result.json', 'work/part_c/d58_result.json', 'work/part_b/c50_result.json', 'work/root/c51_result.json', 'work/part_b/c52_result.json', 'work/root/c53_result.json', 'work/part_a/f_seven_point_kernel_results.json', 'work/part_b/c54_result.json', 'work/root/c55_result.json', 'work/root/c56_result.json', 'work/part_b/c57_result.json', 'work/part_c/d59_result.json', 'work/part_a/f_procyclic_exclusion_results.json']
BIBS = ['work/part_a/references.bib', 'work/part_b/references.bib',
 'work/part_b/b25_references.bib', 'work/part_b/d_mu_references.bib', 'work/part_b/c26_references.bib', 'work/part_b/c33_references.bib', 'work/part_b/c37_references.bib', 'work/part_b/c40_references.bib', 'work/part_b/c42_references.bib', 'work/part_b/c43_references.bib', 'work/root/c48_references.bib', 'work/part_b/c49_references.bib',
 'work/part_c/references.bib', 'work/part_a/gt_shadow_references.bib',
 'work/part_a/haran_rank3_references.bib', 'work/part_a/gt_torsion_sections_references.bib', 'work/part_c/d30_references.bib', 'work/part_a/sphere_completion_restriction_references.bib', 'work/part_a/pure_involution_conjugacy_references.bib', 'work/part_a/pants_order_three_references.bib', 'work/root/references.bib', 'work/part_a/f_seven_point_kernel_references.bib']
ALIASES = {'R-FarbMargalit':'A_FarbMargalit2012',
 'bFarbMargalit2012':'A_FarbMargalit2012',
 'C_FarbMargalit2012':'A_FarbMargalit2012',
 'C_Yagasaki2000':'A_Yagasaki2000',
 'C_Kolev2006':'bKolev2006', 'bKerckhoff1983':'C_Kerckhoff1983'}

def read(p): return (ROOT/p).read_text(encoding='utf-8')
def latex_text(s):
 if isinstance(s,list): s='; '.join(str(x) for x in s)
 if isinstance(s,bool): s='yes' if s else ''
 return s.replace('\\',r'\textbackslash{}').replace('&',r'\&').replace('%',r'\%').replace('_',r'\_').replace('#',r'\#')

rows = {}
for path in METADATA:
 if not (ROOT/path).exists(): continue
 data=json.loads(read(path))
 if isinstance(data,dict): data=[data]
 for row in data: rows[row['id']]=row

pieces = [read('work/root/prelude.tex')]
claim_ids=[]
actual_claims={}
for path in FRAGMENTS:
 text=read(path)
 for cm in re.finditer(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}\{([^\n]*)\}\n(.*?)\\end\{claim\}',text,re.S):
  cid,status,title,body=cm.groups()
  actual_claims[cid]={'status':status,'statement':title+' — '+' '.join(re.sub(r'\\label\{[^}]+\}','',body).split())}
 if path.endswith('ea.tex'): pieces.append(r'\section{E. Special groups and two operator groups}'+'\n')
 def decorate(m):
  cid=m.group(1); claim_ids.append(cid)
  row=rows.get(cid)
  if row and row.get('manuscript_passages'):
   return m.group(0)+'\n'+r'\passage{'+latex_text(row['manuscript_passages'])+'}\n'
  return m.group(0)
 text=re.sub(r'\\begin\{claim\}\{([^}]+)\}.*?\\end\{claim\}',decorate,text,flags=re.S)
 pieces.append(text)
pieces.append(r'\clearpage\bibliographystyle{plain}\bibliography{'+PREFIX+'_references}'+ '\n'+r'\end{document}'+'\n')
paper='\n'.join(pieces)
for old,new in ALIASES.items(): paper=paper.replace(old,new)
for old,new in {'–':'--','—':'---','‘':'`','’':"'",'“':'``','”':"''",'…':r'\ldots{}','§':r'\S{}'}.items():paper=paper.replace(old,new)
OUT.mkdir(exist_ok=True)
(OUT/(PREFIX+'_paper.tex')).write_text(paper)

entries={}
for path in BIBS:
 for entry in re.split(r'(?=^@)',read(path),flags=re.M):
  match=re.match(r'@\w+\{([^,]+),',entry)
  if not match: continue
  key=match.group(1)
  if key in ALIASES: continue
  if key in entries: raise RuntimeError('duplicate bibliography key '+key)
  entries[key]=entry.strip()
(OUT/(PREFIX+'_references.bib')).write_text('\n\n'.join(entries.values())+'\n')
fields=['id','statement','status','where_proved','depends_on',
 'manuscript_passages (section; folio; scan)',
 'depends_on_doubtful_reading (scan, alternatives)','notes']
with (OUT/(PREFIX+'_results.csv')).open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader()
 for cid in claim_ids:
  if cid not in rows: continue
  row=dict(rows[cid]);row['manuscript_passages (section; folio; scan)']=row.pop('manuscript_passages','')
  row.update(actual_claims[cid])
  row['where_proved']='Paper, Part '+cid[0]+', statement '+cid+'; computation locations are specified in that proof.'
  row['depends_on_doubtful_reading (scan, alternatives)']=row.pop('depends_on_doubtful_reading','')
  row={k:('; '.join(map(str,v)) if isinstance(v,list) else ('' if v is False else str(v))) for k,v in row.items()}
  writer.writerow({k:row.get(k,'') for k in fields})
readings=[]
for part in ['part_a','part_b','part_c','root']:
 p=ROOT/'work'/part/'readings.json'
 if p.exists(): readings.extend(json.loads(p.read_text()))
p=ROOT/'work/part_c/b_extra_readings.json'
if p.exists(): readings.extend(json.loads(p.read_text()))
fields=['package','scan',r'the \unsure or \illegible place','what the mathematics supports','how strongly']
with (OUT/(PREFIX+'_readings.csv')).open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader()
 for row in readings: writer.writerow({k:row.get(k,'') for k in fields})

cited={k for m in re.finditer(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',paper) for k in m.group(1).split(',')}
summary={'claims':len(claim_ids),'registered':sum(x in rows for x in claim_ids),
 'missing_result_rows':[x for x in claim_ids if x not in rows],
 'duplicate_claim_ids':sorted({x for x in claim_ids if claim_ids.count(x)>1}),
 'bibliography_entries':len(entries),'missing_bibliography_keys':sorted(cited-set(entries)),
 'readings':len(readings),'tex_bytes':len(paper.encode())}
source_inputs=set(FRAGMENTS+METADATA+BIBS+['work/root/prelude.tex','work/root/assemble.py','work/part_c/b_extra_readings.json'])
source_inputs.update('work/'+part+'/readings.json' for part in ['part_a','part_b','part_c','root'] if (ROOT/'work'/part/'readings.json').exists())
summary['source_input_sha256']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(source_inputs)}
(OUT/'assembly_check.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='source_input_sha256'},indent=2))
