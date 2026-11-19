"""Root-reviewed linkage of mechanical C edit candidates to the ink decisions."""
from work import *
links={2:[[31],[31],[3],[4],[4],[5],[15],[26],[30],[30]],3:[[16],[16],[18]],4:[[1],[9],[11],[13]],5:[[3],[7],[11],[16]],7:[[6],[7]],9:[[4]],10:[[],[8],[9],[10],[11]],11:[[1],[1],[3],[5],[6],[7],[11]],12:[[7],[9],[10],[12],[14]],13:[[5],[5],[5],[8],[8],[8],[9],[10]],14:[[10]],15:[[1],[4],[5],[5],[6],[8],[10]],16:[[2],[2],[5],[6],[7]],17:[[4],[4],[4],[5],[6,7],[8]],18:[[],[9],[11],[17],[17]],19:[[1],[3],[4],[8],[11]],20:[[6],[9],[10]],21:[[1],[2],[3],[6],[9]],22:[[4],[5],[6],[7,8,10],[9]],23:[[3],[5],[6],[8]],24:[[3],[3],[5],[5],[6],[10]],25:[[2,3],[3,4],[7],[9],[9],[10]]}
cs=list(csv.DictReader((OUT/'audit/source_C_non_doubt_diff_candidates.tsv').open(),delimiter='\t'))
rows=[]
for c in cs:
 n=int(c['scan']);k=int(c['candidate_id'].rsplit('-',1)[1]);inds=links[n][k-1];r=json.loads((OUT/'records'/f'{n:03}.json').read_text())
 refs='; '.join(f'{n:03}-{j:02}' for j in inds)
 crops='; '.join(dict.fromkeys(r['rows'][j-1]['crop'] for j in inds))
 reason='Root compared the candidate source/final fragments and their surrounding page text. The local reading/state/alphabet decision is covered by the linked change row(s) and their crop evidence; isolated TeX fragments are not additional readings.'
 status='covered by recorded ink decision'
 if not inds:status='assembly convention only';reason='Removed repeated cotefile marker at an original session boundary; no manuscript text removed and no witness-reading difference counted.'
 if (n,k) in [(2,1),(2,2),(2,9),(2,10),(3,3),(4,4),(5,4)]:reason='Comment or brace/wrapper fragment belongs to the linked drawing/watermark edit; not an extra word-level decision.'
 if (n,k)==(2,8):reason='Closing brace belongs to the cancelled-quantifier wrapper covered by row002-26; no independent text is lost.'
 if (n,k) in [(3,1),(4,1),(5,3),(7,1),(7,2)]:reason='Full-height f in Modf is the cross-page graphic decision recorded in the linked row and notation table; the raw diff splits the TeX wrapper.'
 rows.append([c['candidate_id'],n,status,refs,crops,reason])
with (OUT/'audit/source_C_diff_review.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['candidate_id','scan','root_disposition','changes_rows','crop_references','root_reason']);w.writerows(rows)
print('Root mapped all',len(rows),'mechanical non-doubt candidates; no uncategorized candidate remains.')
