from audit import *
k='120_scan008'
# The preceding audited leaf's doubtful letter is compared with the now-reread
# explicitly defined category letter; retain the uncertainty itself.
replace_text('120_scan007',[(r'\unsure{E|\Sigma}',r'\unsure{\mathcal E|\Sigma}')])
for name,fields_to_update in [('CHANGE_LEDGER.tsv',['final']),('DOUBTS.tsv',['reading'])]:
 rows=readtsv(name)
 for r in rows:
  if r['page']=='120_scan007':
   for f in fields_to_update:r[f]=r[f].replace(r'\unsure{E|\Sigma}',r'\unsure{\mathcal E|\Sigma}')
 rewrite_tsv(name,rows)
finish(k,'Reread every line, all nine category-letter occurrences, the insertions and the three marginal notes. The category letter is the same two-curved calligraphic E throughout. Compared it with the previous leaf’s isolated doubtful letter and rendered that candidate as calligraphic E while retaining Sigma as an alternative; the prior uncertainty is not declared resolved. The first ∀ objet has joined lower legs, whereas item c has the independent stems of tt. The written R in tt objet de R remains uncorrected. No change to this page’s text.',notation=[('cross-page category letter','The explicitly defined calligraphic E here supports calligraphic E as the first, still doubtful candidate at the isolated letter in 120_scan007.')])
