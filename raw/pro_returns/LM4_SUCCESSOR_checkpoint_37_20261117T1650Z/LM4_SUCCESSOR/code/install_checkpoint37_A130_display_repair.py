"""Install only the independently reviewed three-row A.130 display."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
source='work_A/A130_GT0_two_strand_fixed_group_proposed.tex'
target='sections/a_gt0_two_strand_fixed_group.tex'
proposal='work_A/A130_GT0_two_strand_fixed_group_layout37.tex'
OLD='b4ee884abb27c24f6f311901daa713c203b1aeb8c1c1b835d3d9740090b68de9'
NEW='4e9a245abd26dbfcc9cc20108382038d9bf8d4ffdb1e7712980ceb2b09b5d40c'
reviews=['work_CE/review_A130_final_layout37.txt', 'work_CE/review_A130_final_layout37.json']
def sha(rel): return hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
assert sha(source)==sha(target)==OLD and sha(proposal)==NEW
review=json.loads((ROOT/reviews[1]).read_text())
assert str(review.get('result',review.get('status',''))).startswith('PASS')
assert NEW in (ROOT/reviews[1]).read_text()
binding_paths=['records/checkpoint37_formal_source_copies.json',
               'records/checkpoint37_root_formal_reviews.json',
               'records/checkpoint37_independent_review_manifest.json']
dest=ROOT/'records/checkpoint37_before_A130_display_repair'
dest.mkdir(exist_ok=False)
for rel in [source,target]+binding_paths:
    saved=dest/rel
    saved.parent.mkdir(parents=True,exist_ok=True)
    saved.write_bytes((ROOT/rel).read_bytes())
new=(ROOT/proposal).read_bytes()
(ROOT/source).write_bytes(new)
(ROOT/target).write_bytes(new)
loaded={rel:json.loads((ROOT/rel).read_text()) for rel in binding_paths}
copies=loaded[binding_paths[0]]['copies']
row=next(item for item in copies if item['statement']=='A.130')
assert row['sha256']==OLD
row['sha256']=NEW
stamp=datetime.now(timezone.utc).isoformat()
for rel in binding_paths:
    loaded[rel]['A130_display_repair_at']=stamp
loaded[binding_paths[1]]['copies']=copies
loaded[binding_paths[1]]['independent_reviews'].update({p:sha(p) for p in reviews})
loaded[binding_paths[1]]['A130_display_root_review']={'complete_source_and_diff_read_chunk':'90e5c2', 'scope':'Only one display wrapped into three gathered rows; mathematical text unchanged.'}
loaded[binding_paths[2]]['source_hashes'][source]=NEW
loaded[binding_paths[2]]['reviews'].update({p:sha(p) for p in reviews})
for rel,data in loaded.items():
    (ROOT/rel).write_text(json.dumps(data,indent=2)+'\n')
record={'recorded_at':stamp,'result':'PASS_DISPLAY_ONLY_REPAIR_INSTALLED',
        'source':source,'target':target,'proposal':proposal,'old_sha256':OLD,'new_sha256':NEW,
        'root_complete_source_and_diff_read_chunk':'90e5c2',
        'independent_reviews':{p:sha(p) for p in reviews},
        'before_overfull_count':1,'before_maximum_overfull_pt':26.55002,
        'before_overflow_page_individually_viewed':246,
        'before_visual_observation':'The five-part canonical norm display extends beyond the right text margin. All symbols remain visible; the three-row repair addresses the actual excess.',
        'preserved_directory':str(dest.relative_to(ROOT)), 'build_run_by_installer':False}
with (ROOT/'records/checkpoint37_A130_display_repair_install.json').open('x') as stream:
    json.dump(record,stream,indent=2)
    stream.write('\n')
print(json.dumps(record,indent=2))
