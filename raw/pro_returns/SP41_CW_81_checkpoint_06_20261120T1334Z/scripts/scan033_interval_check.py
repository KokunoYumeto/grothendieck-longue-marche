"""Exact finite-cell certificate for the concrete interval example in S, SA01-R81-07.

Let the seven nonempty disjoint cells be {0}, (0,1), {1}, (1,2), {2},
(2,3), {3}. Their union is X=[0,3]. Each of the four closed sets below
is the indicated union of whole cells. The map from a union of cells to
its cell-index set has inverse J -> union of cells indexed by J.
Disjointness and nonemptiness of the cells give both inverse identities.
Membership in each cell gives exact preservation of union, intersection,
set difference and inclusion. Thus the following finite operations are
an exact representation of these specified sets, not point sampling.
"""
from pathlib import Path
import json,datetime
w=Path(__file__).resolve().parents[1]
cells=['{0}','(0,1)','{1}','(1,2)','{2}','(2,3)','{3}']
X=frozenset(range(7))
sets={'Sigma1+':frozenset([2,3,4]), 'Sigma1-':frozenset([0,1,2,4,5,6]),'Sigma2+':frozenset([4,5,6]),'Sigma2-':frozenset([0,1,2,3,4])}
intervals={'Sigma1+':'[1,2]','Sigma1-':'[0,1] union [2,3]','Sigma2+':'[2,3]','Sigma2-':'[0,2]'}
checks={
 'all_four_sets_nonempty':all(sets.values()),
 'first_pair_covers_X':sets['Sigma1+']|sets['Sigma1-']==X,
 'second_pair_covers_X':sets['Sigma2+']|sets['Sigma2-']==X,
 'first_pair_members_distinct':sets['Sigma1+']!=sets['Sigma1-'],
 'second_pair_members_distinct':sets['Sigma2+']!=sets['Sigma2-'],
 'two_unordered_pairs_distinct':frozenset([sets['Sigma1+'],sets['Sigma1-']])!=frozenset([sets['Sigma2+'],sets['Sigma2-']]),
 'display_11_inclusion':sets['Sigma1+']<=sets['Sigma2-'],
 'display_11bis_inclusion':sets['Sigma2+']<=sets['Sigma1-'],
 'positive_intersection_exactly_point_2':sets['Sigma1+']&sets['Sigma2+']==frozenset([4]),
 'display_10_empty_intersection':not (sets['Sigma1+']&sets['Sigma2+'])
}
assert all(v for k,v in checks.items() if k!='display_10_empty_intersection')
assert checks['display_10_empty_intersection'] is False
result={'source':'Supplied sweep cote81.md, SA01-R81-07; correction SA01-K81-01','UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'X':'[0,3] with the ordinary subspace topology','cells':cells,'interval_sets':intervals,'cell_index_sets':{k:sorted(v) for k,v in sets.items()},'closedness':'Each indicated closed interval is closed in X; the indicated finite union is closed in X.','exact_representation':__doc__,'checks':checks,'all_cross_intersections':{a+' intersect '+b:[cells[i] for i in sorted(sets[a]&sets[b])] for a in ['Sigma1+','Sigma1-'] for b in ['Sigma2+','Sigma2-']},'scope':'Concrete supplied example verified by exact finite-cell operations. The manuscript wording is decided separately from image crops; this computation never changes its transcription.'}
(w/'validation/scan033_interval_certificate.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False,indent=2))
