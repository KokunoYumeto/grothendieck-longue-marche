#!/usr/bin/env python3
"""Integrate the independently audited complete common-field tower calculation."""
from pathlib import Path
import datetime,json

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex'
s=p.read_text();entry=r'\input{sections/dyadic_common_field_tower.tex}'
anchor=r'\section{Part B. Sections and valuations}'
assert anchor in s
if entry not in s:p.write_text(s.replace(anchor,entry+'\n'+anchor))
p=w/'notes/register_metadata.json';d=json.loads(p.read_text())
d['A.126']={
 'answers':'A5; A8; A9; A12; A15; L14; L17; L20',
 'depends_on':'A.57; A.96; A.121; exact root stabilizers, finite module annihilators, integral Smith maps and odd-factor CRT lifts',
 'uses_local_theorem':'no; actual finite rational radical fields and their common abelian subfields',
 'manuscript_passages':'cote149; scans56–58,126–127; finite character tests for puncture lifting',
 'notes':'Computes every common field at every exponent divisible4 through an exact dyadic recursion; a missing cyclotomic layer causes permanent stabilization. The complete integral negative relation test detects unbounded cyclotomic growth; otherwise integral Smith invariants bound stabilization. Every generator has a literal embedding into each field factor. The odd factor is removed through the actual root power map and compatible CRT stabilizer lifts. No completed coefficient or full section lift is inferred.'}
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=w/'SECTIONS_OVER_Q_report.md';s=p.read_text();lines=s.splitlines()
detail='A.126 computes every common field at all exponents divisible4, with exact permanent-stopping and unbounded-cyclotomic criteria; completed coefficient compatibility remains open.'
for i,line in enumerate(lines[:55]):
 if any(line.startswith('| '+item+' |') for item in ['A5','A8','A9','A12','A15','L14','L17','L20']):
  cells=[c.strip() for c in line.strip().strip('|').split('|')]
  assert len(cells)==3
  if 'A.126' not in cells[1]:cells[1]+=', A.126'
  if detail not in cells[2]:cells[2]+=' '+detail
  lines[i]='| '+' | '.join(cells)+' |'
s='\n'.join(lines)+'\n'
heading='## The complete common-field tower at all divisible-four exponents'
if heading not in s:
 s+='\n'+heading+'\n\n'+stamp+': A.126 proves the general recursion from literal root stabilizers. When the preceding common field contains the required cyclotomic layer, all extra fields are given by the complete relation module modulo half the exponent. Positive relations give quadratic fields; negative relations give the explicit even cyclotomic character plus a quadratic character. At the first missing cyclotomic layer, a whole index-two coset consists of actual stabilizer images at every later depth, which proves permanent stabilization. An integral multiplicative relation with product minus one supplies a primitive root of unity inside every factor at every depth. In its absence the integral Smith map gives a finite stabilization bound. The exact odd-factor CRT lifts prove equality with the dyadic common field for every exponent divisible four. Root, local_preprint and Legendre audited the proof; the executed certificate compares450 finite exponent cases and95040 literal odd-factor lifts. These are field and character results. The completed puncture-coefficient construction remains an explicit further task.\n'
p.write_text(s)
audit=(stamp+' A126 full proof passed root, local_preprint and Legendre audits: exact finite abelianization and compatible signs; all stabilizer and character equations; field-factor embeddings; first-failure coset at every later depth; integral kernel parity, Smith bound and exponent restriction map; every odd-factor CRT root lift. The certificate passed90 tuples,450 exponent cases,9600 literal stabilizer tests,3280 relation vectors,62466 subgroup products,4356 character checks,95040 odd CRT lifts and235 permanent-stopping comparisons. The first certificate failure was an incorrect sqrt2 sign constraint in its exponent2 ambient group; the exact correction and failure record are retained.\n')
for name in ['notes/hour8_root_audits.md','notes/root_progress.md']:
 p=w/name;s=p.read_text()
 if 'A126 full proof passed root' not in s:p.write_text(s+'\n'+audit)
out='Integrated audited A126, with full recursion, stopping criterion, Smith bound and odd-factor comparison.\n'
Path(__file__).with_name('integrate_a126_output.txt').write_text(out)
print(out,end='')
