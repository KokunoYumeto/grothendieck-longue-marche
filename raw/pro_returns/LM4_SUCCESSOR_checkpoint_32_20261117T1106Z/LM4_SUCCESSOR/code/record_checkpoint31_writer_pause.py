"""Bind the three actual writer acknowledgments after all root producers ended."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
sha = lambda rel: hashlib.sha256((root/rel).read_bytes()).hexdigest()
specs = [
 ('/root/involutions','2026-11-17T07:46:06.148737+00:00','work_A/checkpoint31_status.json','e03c3f05b657c2cf9d139bcdc5dec5a44cbcc096a616a10b9c0bccd694019f27','work_A/checkpoint31_owned_manifest.json','627e7fca1a54956e99c794708ece9711d142bce384cde097011eaf4a2c5075b4'),
 ('/root/torus_real','2026-11-17T07:45:55.269949+00:00','work_CE/status_checkpoint31.txt','b3fb41bf734597333fc3a4192422bc6136f7ae05e84d9d63d335a62fadf46c3c','work_CE/checkpoint31_owned_manifest.json','5cbbbe20b44d4852ed73a87666db4fdca8ff64149bffb546587aa04ef3870359'),
 ('/root/topology_census','2026-11-17T07:46:19.888913+00:00','work_DE/checkpoint31_status.json','d7cd4e005f7d0507a6b89ef9652f92d969eb697760b413d81e135be4cd13f897','work_DE/checkpoint31_owned_manifest.json','1ee5303fbfdddb91c8d4ef7b61de69eca237b55374ab3104106b399b3e27e900'),
]
agents=[]
for name,at,status,digest,manifest,mdigest in specs:
    assert sha(status)==digest and sha(manifest)==mdigest
    assert at in (root/status).read_text()
    agents.append(dict(agent=name,paused_at=at,status=status,status_sha256=digest,
                       manifest=manifest,manifest_sha256=mdigest,
                       acknowledged_no_live_or_interrupted_producer=True))
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),
            all_writers_paused=True,agents=agents,live_producers=[],
            root_completed_sessions={'initial_combined_build':{'session_id':1071,'actual_exit_code':1},
                                     'corrected_combined_build':{'session_id':29246,'actual_exit_code':0},
                                     'final_renderer':{'session_id':73164,'actual_exit_code':0},
                                     'actual_size_estimate':{'session_id':24779,'actual_exit_code':0}},
            scope='All three explicit writer acknowledgments and status files were read. All root build/render/estimate sessions ended with their actual exit responses observed. No broad mathematical producer was started. Only the scheduled root capture driver may now update its review, inventory, retention and packaging records.',
            release='Root must release all three immediately after actual immutable capture closes, before verification or saving.')
out=root/'records/checkpoint31_writer_pause.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print('PASS:three actual writer pauses bound;root build/render/estimate sessions completed;no live producer.')
