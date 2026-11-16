#!/usr/bin/env python3
"""Integrate the audited finite-support persistence and exact norm criterion."""
from pathlib import Path
import datetime,json,subprocess
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
records={
 'A.153':{
  'file':'two_prime_finite_support_persistence_agent.tex',
  'answers':'A5; A9; A15; L10; L14; L20',
  'depends_on':'A.151 literal cubic class quotient; exact cyclotomic residue orders; unique local unramified extensions; norm-Artin identity and compact finite fibres',
  'uses_local_theorem':'no',
  'manuscript_passages':'cote149; scans56–58 and126–127; finite support in the actual norm tower',
  'notes':'For every fixed finite enlargement T of the support, the explicit cubic extension F L_n/L_n is split at T above a displayed depth n_T. Its nonzero Artin quotient persists at every later level and in the ideal-norm inverse limit. The cyclotomic local field inclusion is explicit. This does not evaluate the particular target class. Root independently read the whole proof and reran all finite residue-order checks.',
  'detail':'A.153 proves that the nonzero compatible cubic class quotient persists after every fixed finite enlargement of the allowed support.'},
 'A.155':{
  'file':'balanced_class_norm_criterion_agent.tex',
  'answers':'A5; A9; A15; L10; L14; L20',
  'depends_on':'A.140 actual local norm surjectivity; A.149 full local holomorph; A.151 literal root branches; finite Poitou–Tate duality; continuous Shapiro and Kummer maps; actual ideal norms',
  'uses_local_theorem':'no',
  'manuscript_passages':'cote149; scans56–58 and126–127; precise fixed-support coherent norm obstruction',
  'notes':'The dual localization kernel is exactly the character group of the displayed quotient of the ordinary three-primary ideal class group by balanced residue-degree relations. The pairing with the actual norm target -2 is h(e_n)/3^r, with positive sign fixed by the retained cochain calculation and arithmetic Frobenius. The target is a completed S-unit norm exactly when e_n vanishes; a single coherent norm family exists exactly when every e_n vanishes. The element is killed by3^n, but no precision bound based only on its order is claimed. The erroneous draft r=n claim was removed before integration; C9 with e=3 is a retained regression counterexample. Root reopened Milne ADT I4.10(a), I4.15, printed65, and CFT III3.6/section4 Steps2–3, audited every map, and independently reran the finite certificate.',
  'detail':'A.155 identifies the exact balanced ideal class e_n paired with the norm target -2 and proves its all-precision equivalence with one compatible completed S-unit norm family.'}
}
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
anchor=r'\input{sections/harmonic_prym_dyadic_injection.tex}'
assert anchor in s
entries='\n'.join(r'\input{sections/'+r['file']+'}' for r in records.values())
if all(r['file'] not in s for r in records.values()):s=s.replace(anchor,anchor+'\n'+entries,1)
else:assert all(r['file'] in s for r in records.values())
p.write_text(s)
p=w/'notes/register_metadata.json';metadata=json.loads(p.read_text())
for ident,rec in records.items():metadata[ident]={k:v for k,v in rec.items() if k not in {'file','detail'}}
p.write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines()
for i,line in enumerate(lines[:55]):
 if not line.startswith('| '):continue
 cells=[x.strip() for x in line.strip().strip('|').split('|')]
 if len(cells)!=3:continue
 for ident,rec in records.items():
  if cells[0] in {x.strip() for x in rec['answers'].split(';')}:
   if ident not in cells[1]:cells[1]+=', '+ident
   if rec['detail'] not in cells[2]:cells[2]+=' '+rec['detail']
 lines[i]='| '+' | '.join(cells)+' |'
heading='## Continued work: persistent class quotients and the exact target class'
if heading not in lines:lines.extend(['',heading,'',stamp+': '+records['A.153']['detail']+' '+records['A.155']['detail'],'',
 'For an added prime p, the cyclotomic residue degree over Q(mu3) is divisible by three once n>v3(p²-1). The unique unramified local cubic extension is then contained in the actual cyclotomic completion. This proves splitting at every newly allowed place, while the literal common field F keeps the global Artin quotient nonzero. Ideal norms preserve its value, and finite-fibre compactness gives the inverse-limit surjection.',
 'The target calculation uses the dual of the literal augmentation kernel, not an unspecified class-group surrogate. A locally trivial dual class lifts by Shapiro to a class character on K_n. Subtracting its unique global cyclotomic character at three makes it unramified. At2,11,59 its local values are exactly the displayed residue-degree multiples, giving the balanced quotient. The retained cochain calculation and arithmetic Frobenius identify the pairing as h(e_n)/3^r. Finite duality, continuous coefficient limits, and compact norm fibres prove the fixed-level and whole-tower equivalences.',
 'Pre-integration correction: the draft asserted that3^n e_n=0 made coefficient precision r=n sufficient. This is false for an element inside a larger finite group: e=3 in Z/9 is killed by3 but every character to Z/3 kills it. The claim was removed from source and certificate. All coefficient precisions are retained; no value of e_n is inferred by A.155.',''])
p.write_text('\n'.join(lines)+'\n')
p=w/'SECTIONS_OVER_Q_references.bib';s=p.read_text()
old='perfect duality of the finite localization kernels and finiteness for a finite ramification set with3 inverted.'
extra=' For A.155 the root reopened the same results and the explicit pairing on printed p.65 following Remark4.19, checking the local-minus-global cochain convention against the actual augmentation sequence.'
if 'For A.155 the root reopened' not in s:assert old in s;s=s.replace(old,old+extra,1)
p.write_text(s)
audit=stamp+' A153/A155 root audits PASS after the A155 precision correction. The exact cyclotomic local inclusions, norm-Artin maps, fixed-support dual coefficient sequences, unramified character normalization, cochain sign, finite duality, continuous coefficient limits, and compatible compact norm fibres were checked. All finite certificates rerun. A155 makes no claim that the target classes vanish.\n'
for name in ['notes/hour11_root_audits.md','notes/root_progress.md']:
 with(w/name).open('a')as f:f.write('\n'+audit)
r=subprocess.run(['python',str(w/'code/build_register.py')],check=True,capture_output=True,text=True)
out='Integrated audited A153 and corrected A155.\n'+r.stdout
Path(__file__).with_name('integrate_a153_a155_output.txt').write_text(out);print(out,end='')
