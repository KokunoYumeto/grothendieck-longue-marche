"""Index every supplied question to completed decisions, including grouped early reviews.

This is a textual cross-reference, not a new ink inspection or mathematical check.
"""
from pathlib import Path
import json,csv
root=Path(__file__).resolve().parents[1]
base=root.parent
maps={
 170:[[1],[2],[3],[4],[5],[6],[7],[8],[],[1],[],[4,5],[],[8]],
 171:[[1,2],[3],[4],[5],[6],[7],[4],[7],[1,2,3],[6],[]],
 172:[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[],[10],[11],[],[5],[6],[7,9],[8,9,10,13]],
 173:[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[2],[6],[9],[1],[3,4,5],[8,10],[12,13,14]],
 174:[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12,13],[11],[14],[14],[14],[14],[14],[14]],
 175:[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[15],[4,5,6],[15],[15],[13,15]],
 176:[[1],[2],[3],[4],[5],[6],[7],[8],[9],[3],[5],[10],[11],[12],[13],[14]]
}
supp={
 (170,9):'The written local-system rank is n, without (n−1); the earlier (n−1)-champs phrase remains distinct. The English comparison is not ink evidence.',
 (170,11):'Retain written parentheses and high C in the first (n-Cat), later low c in (n-cat), and the single physical rule under Hom with low n. These were read by all three readers and recorded in notation.',
 (170,13):'Repeat of the local-system-rank question: preserve n-systèmes, with no supplied minus sign, 1 or parentheses.',
 (170,14):'First limit remains arrow/underlined-lim uncertain; the second is a clear direct-limit arrow. Preserve the parenthetic singly underlined NB and uninterrupted paragraph. No English wording supplies signs or stops.',
 (171,10):'Retain n-groupoïde, two rules under pro only, low 1 on pi, the recurring uncertain calligraphic E family, and parentheses around ind. The apparent line under n belongs to the returning g descender.',
 (171,11):'Reproduce the three unequal horizontal separator strokes and the ensuing Je comprends paragraph. No star or external section heading is inserted.',
 (172,14):'Preserve loc constant without a final e; the following cancelled et is separately recorded. Grammar does not supply an ending.',
 (172,17):'Keep the first parenthesis after faisceaux and the separate et plaçons-nous… addition at its own guide. Both are insertion layers; the join within plaçons-nous remains doubtful.',
 (172,18):'Preserve the complete modulo qualification and singular modèle. Its accent is resolved to grave by the recorded crop; the earlier question does not compel retained uncertainty.',
 (172,20):'Keep the finie and ou strates additions, the union with i∈I below it and X_i, and both cancelled words. The extra physical point near the union index is drawn without mathematical interpretation.',
 (172,21):'The repeated combined question confirms constant without e, the separate literal point after X, and barred m after elle-. No agreement or sentence-boundary repair is made.',
 (173,19):'Both insertion guides are retained: partition P after fixée, and de la cat before the relevant sheaf phrase. P uses the preferred calligraphic family with first-occurrence doubt.',
 (173,20):'Keep the below-baseline Pour…di cancellation, a single rule under Hom, the opposite star heights in Rj_*j^*, the doubtful connector, and inserted etc. No expected arrow is supplied.',
 (173,21):'Keep the guided de torsion addition, both shorter cancellations, and paired raised quotation ticks around d’équisingularité. The manuscript layers remain explicit.',
 (173,22):'Keep the stated X_i regular/connected wording and the damaged foot: pour and présent remain uncertain; notre and propos are readable. No English supplementation is used.'
}
rows=[]
for p in sorted((root/'records').glob('scan*/decision.json')):
 d=json.loads(p.read_text());n=d['scan']
 source=(base/f'packets/{n}/C_questions.md').read_text().split('# Earlier notes')[0]
 qs=[line for line in source.splitlines() if line.startswith(f'| {n} |')]
 mapping=maps.get(n,[[i] for i in range(1,len(qs)+1)])
 if len(mapping)!=len(qs):raise ValueError(f'Question map length mismatch: {n}')
 for i,(question,inds) in enumerate(zip(qs,mapping),1):
  if not inds and (n,i) not in supp:raise ValueError(f'Unmapped question {n} Q{i}')
  disposition='; '.join(d['doubt_review'][j-1]['decision'] for j in inds)
  extra=supp.get((n,i),'')
  if extra:disposition=(disposition+'; ' if disposition else '')+extra
  refs=', '.join(f'doubt_review[{j-1}]' for j in inds)
  if extra:refs+=(', ' if refs else '')+'completed differences / inventory / notes / notation'
  rows.append({'scan':n,'question_id':f'C{n}-Q{i:02}','supplied_question_row':question,'completed_disposition':disposition,'decision_record':f'records/scan{n}/decision.json','record_fields':refs,'scope':'Textual cross-reference to the completed independent readings and root decisions; no new image inspection or proof.'})
out=root/'records/C_question_coverage.tsv'
with out.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'completed_pages_indexed':len(set(x['scan'] for x in rows)),'supplied_question_rows_indexed':len(rows),'unmapped_questions':0}))
