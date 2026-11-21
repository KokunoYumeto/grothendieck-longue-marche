"""Align doubt-table quotations with already adjudicated TeX, without changing pages.

This is bookkeeping, not a fresh image reading. Original reader returns and
frozen first readings remain untouched. Each mapping below names its existing
metadata entry. The page's literal unsure expression is copied into that entry.
"""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
fixes={
28:{
'opening replacement before un':r'\unsure{a|-}',
'last-line map connector':r'\unsure{\longrightarrow|-}',
'asterisk note, noun before d’ordre fini':r"\unsure{d'éléments|d'élts}",
'asterisk note, before cas':r'\unsure{au|aux}',
'asterisk note, before fibres':r'\unsure{de|des}'},
29:{
'cancelled opening, line 4 after et':r'\unsure{\overline m|=}',
'cancelled opening, line 4':r'\unsure{localisations|localisés}',
'cancelled symbol after clôture algébrique':r'\unsure{\overline K|\overline Q}',
'cancelled phrase after dans k':r"\unsure{des $k$ l'|des $f_k\,\ell$}",
'end of inserted subject':r'\deleted{\unsure{sur|se}}',
'cancelled opening before car.':r'\unsure{En}',
'cancelled opening after qu’il':r'\unsure{suffit}',
'cancelled opening after de':r'\unsure{travailler}',
'cancelled opening before les groupes':r'\unsure{avec}',
'cancelled opening first occurrence':r'\unsure{fondamentaux}',
'cancelled opening before à p':r'\unsure{premiers}',
'cancelled opening last line':r'\unsure{groupes}',
'cancelled opening last word':r'\unsure{fondamentaux}',
'cancelled replacement opening':r'\unsure{Choisissons}',
'second paragraph after ces':r'\unsure{hypothèses|hyp. mises}'},
31:{
'first homology map connector':r'\unsure{-|\longrightarrow}',
'first homology kernel index':r'\unsure{1|n}',
'second homology kernel index':r'\unsure{1|n}',
'proof opening, after pour':r'\unsure{$\forall$|tt}',
'cancelled extension phrase quantifier':r'\unsure{$\forall$|tt}',
'cancelled old verb':r'\unsure{étendre}',
'cancelled upper word above corps':r'\unsure{base}',
'lower replacement after crossed base':r'\unsure{corps|corps de}',
'after conjugaison de':r'\unsure{Scindages|scindages}'},
33:{
'cancelled second handwritten number':r'\unsure{16|46}',
'line before the canonical comparison, article':r'\unsure{Le|La}',
'line before the canonical comparison, noun':r'\unsure{composé|composée}'},
37:{
'opening theorem abbreviation, initial case':r'\unsure{th.|Th.}',
'cancelled word after Cela':r'\unsure{signifie}'}
}
for n,mapping in fixes.items():
 path=R/'records'/f'149_scan{n:03}.json';r=json.loads(path.read_text());tex=(R/'pages'/f'149_scan{n:03}.tex').read_text()
 for d in r['doubts']:
  if d['place'] in mapping:
   quoted=mapping[d['place']];assert quoted in tex,(n,d['place'],quoted);d['reading']=quoted
 if n==29:
  # First main visual review: "Only one crossed de appears before Q."
  # Blind B04 independently agrees; this old reader question is stale.
  r['doubts']=[d for d in r['doubts'] if d['place']!='de before Q']
  for row in r['rows']:
   if row['place']=='main paragraph, beginning of line 9 before Q':
    row['scan_shows']=row['scan_shows'].replace('Proposed state: one cancelled de, with no supplied replacement.','The main visual review confirms one crossed de, with no supplied replacement. The earlier unresolved-state question is therefore removed from the current doubt table.')
 path.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
path=R/'records/149_scan039.json';r=json.loads(path.read_text());extra=[x for x in r['inventory'] if x['element'] in ['E_extra_et','E06a']]
if extra:
 r['inventory']=[x for x in r['inventory'] if x['element'] not in ['E_extra_et','E06a']]
 e=extra[0];e['element']='E06a';i=next(i for i,x in enumerate(r['inventory']) if x['element']=='E06');r['inventory'].insert(i+1,e)
path.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print('Doubt quotations reconciled; stale 029 question removed; 039 insertion inventory ordered. No page file changed.')
