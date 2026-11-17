"""Install only completed, improving, reviewed lossless compression policies."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json
root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--image-observation',required=True)
parser.add_argument('--document-observation',required=True)
parser.add_argument('--review',required=True)
args=parser.parse_args()
def bound(rel):
    p=root/rel
    return dict(path=rel,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
def read(rel):return json.loads((root/rel).read_text())
measurements={}
for kind,path in [('images',args.image_observation),('documents',args.document_observation)]:
    obs=read(path)
    assert obs['actual_tool_result_observed'] is True and obs['actual_exit_code']==0
    assert obs['actual_completion_tool_chunk'] and obs['session_id']>0
    for key in ('source','report','stdout','stderr'):
        assert bound(obs[key]['path'])=={k:obs[key][k] for k in ('path','bytes','sha256')}
    assert obs['stderr']['bytes']==0
    measurement=read(obs['report']['path'])
    assert measurement['result']=='PASS_EXACT_PROSPECTIVE_STREAM_AND_FULL_ROUNDTRIP'
    assert measurement['input_preflight']==measurement['input_second_pass']==measurement['candidate']['roundtrip']
    assert measurement['candidate']['decoder_eof'] and measurement['candidate']['decoder_unused_bytes']==0
    measurements[kind]=measurement
base=read('records/checkpoint36_first_size_estimate/checkpoint36_size_estimate.json')
saving=sum(base['prospective_bundles'][k]['compressed_bytes']-measurements[k]['candidate']['compressed_bytes'] for k in measurements)
assert all(base['prospective_bundles'][k]['compressed_bytes']>measurements[k]['candidate']['compressed_bytes'] for k in measurements)
assert base['estimated_total_with_allowance']-saving<536870912
assert base['header_manifest_retention_late_text_allowance_bytes']==5000000
review=read(args.review);assert review['result'].startswith('PASS')
specs=[
 ('work_CE/checkpoint_image_tar_256_proposed36.py','code/checkpoint_image_tar.py','e6019666bfc8486f3de4355c4f78dd297532e3c764114a450be1fcd4d43fb885','c3de17157c5d6fa5ac66bfc64717df096c3dbcc195965be1a7d91c878df352f6'),
 ('work_DE/checkpoint_document_tar_proposed36.py','code/checkpoint_document_tar.py','c5b791f3906be7bd74d471076560c75d52833eb6d76a02ec171e5e5eb9dc4025',None),
 ('work_DE/package_checkpoint_image256_document128_proposed36.py','code/package_checkpoint.py','7c753ea7355dcb2dc511ee31f6e3814121784835fe987fb0cd2df37cf3abb447','cf0a5219cf66ec07e7f8509634888392929fb1eced6f05748e35d462052938dc'),
 ('work_DE/check_checkpoint36_preconditions_image256_document128_proposed.py','code/check_checkpoint36_preconditions.py','56aab1c260f7949dd94a98a8862d8411210d1b77666ae8b7fbd1605ae8bd1374','94a98c480176128d68e64a3db9f530d1e567b0b4eba30e1d38bc99c87b315d08'),
 ('work_DE/publish_checkpoint36_readiness_image256_document128_proposed.py','code/publish_checkpoint36_readiness.py','ca619b01dec20ca6ff56d364466818df443a354cb6c1638faa54f1c84ee739c3','c790a3d96fd5eeac2c945f7491a7d91a14b2a0331c2a9f4e0707663ca2e1fe21'),
 ('work_DE/verify_checkpoint36_system_tars_image256_document128_proposed.py','code/verify_checkpoint36_system_tars.py','7f88c4a0c2c02f3eff1de787aae63bbd93ae3879cf47ab2d0ec7aa2bdcbf9a37','339bd9668f05b199af15270a1ea39b8b312132ef774ea70136aa6c8f8d031bfb')]
assert not (root.parent/'LM4_SUCCESSOR_checkpoint_36.zip').exists()
for source,target,digest,old in specs:
    assert bound(source)['sha256']==digest
    if old is None:assert not (root/target).exists()
    else:assert bound(target)['sha256']==old
assert bound('code/checkpoint_data_tar.py')['sha256']=='9e149cc79ca9790fc55a3147a4664c0886cbe1dc0b981727459a26bac35badbb'
preserve=root/'records/checkpoint36_before_dual_dictionary_install';preserve.mkdir(exist_ok=False)
before=[]
for source,target,digest,old in specs:
    if old is not None:
        previous=preserve/Path(target).name
        with previous.open('xb') as stream:stream.write((root/target).read_bytes())
        before.append(bound(str(previous.relative_to(root))))
for source,target,digest,old in specs:
    (root/target).write_bytes((root/source).read_bytes())
    assert bound(target)['sha256']==digest
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),
 result='PASS_REVIEWED_MEASURED_DICTIONARIES_INSTALLED',installed_sources=[bound(t) for _,t,_,_ in specs],
 preserved_sources=before,independent_review=bound(args.review),
 component_measurement_observations={k:bound(p) for k,p in [('images',args.image_observation),('documents',args.document_observation)]},
 unchanged_data_helper=bound('code/checkpoint_data_tar.py'),
 measured_saving_bytes=saving,estimated_total_with_unchanged_allowance=base['estimated_total_with_allowance']-saving,
 scope='Both actual candidate producers completed before mutation. Only exact reviewed source bytes installed. Previous canonical files, all source-only proposals and original measurements remain retained. Checkpoint35 document policy remains64MiB; current36 image/document/data policies are256/128/64MiB. No compressor or archive is run by this installer.')
with (root/'records/checkpoint36_dual_dictionary_install.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print(json.dumps(record,indent=2))
