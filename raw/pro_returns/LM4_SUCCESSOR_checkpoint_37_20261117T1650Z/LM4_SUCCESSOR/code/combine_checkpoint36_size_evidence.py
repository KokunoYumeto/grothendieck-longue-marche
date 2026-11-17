"""Combine completed same-input256 images with actual completed doc/data sizes.

No compressor and no ZIP is created. The complete preceding128 estimate,
its real stdout/stderr and observed exit must already have been preserved.
The actual current image stream is rehashed to prove it is still identical.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, copy, hashlib, json
from measure_checkpoint36_prospective_image256 import png_paths, stream_images, CountingSink

ROOT=Path(__file__).resolve().parents[1]
PARENT=ROOT.parent/'LM4_SUCCESSOR_checkpoint_35.zip'
PARENT_SHA='33b0925ca3ba12d8944fc47243807a3c61ebb2a4f03ec47f7bb2ce1a5a83f121'
PARENT_BYTES=530938760
CAP=536870912
ALLOWANCE=5000000
IMAGE_BYTES=606720000
IMAGE_SHA='936dfe5a59bff2c3c93380d033c0c9b70160d20163c502b319423da1267f8b7d'
FINAL_IMAGE_HELPER='e6019666bfc8486f3de4355c4f78dd297532e3c764114a450be1fcd4d43fb885'
OLD_IMAGE_HELPER='c3de17157c5d6fa5ac66bfc64717df096c3dbcc195965be1a7d91c878df352f6'

def hash_path(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
    return h.hexdigest()

def read(rel):return json.loads((ROOT/rel).read_text())

def bound(rel):
    p=ROOT/rel
    return dict(path=rel,bytes=p.stat().st_size,sha256=hash_path(p))

def check_binding(item):
    assert bound(item['path'])=={k:item[k] for k in ('path','bytes','sha256')},item['path']

def check_observation(rel,report_path):
    obs=read(rel)
    assert obs['actual_tool_result_observed'] is True
    assert isinstance(obs['session_id'],int) and obs['session_id']>0
    assert obs['actual_completion_tool_chunk'] and obs['initial_tool_chunk']
    assert obs['report']['path']==report_path
    for key in ('report','stdout','stderr','source'):check_binding(obs[key])
    return obs

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-observation',required=True)
    parser.add_argument('--candidate-observation',required=True)
    args=parser.parse_args()
    first='records/checkpoint36_first_size_estimate/'
    base_path=first+'checkpoint36_size_estimate.json'
    candidate_path='records/checkpoint36_prospective_image256_measurement.json'
    base_obs=check_observation(args.base_observation,base_path)
    candidate_obs=check_observation(args.candidate_observation,candidate_path)
    assert base_obs['actual_exit_code'] in (0,1)
    assert candidate_obs['actual_exit_code']==0
    assert base_obs['source']['path']=='code/estimate_checkpoint36_size.py'
    assert base_obs['source']['sha256']=='293e093f5d0cdc7ed8d841182b2c33e09f0c38bde414724891ea7a3d50bc0e47'
    assert candidate_obs['source']['path']=='code/measure_checkpoint36_prospective_image256.py'
    assert candidate_obs['source']['sha256']=='33fe2d1d463b774ff65032c5cd2924af8e036592ec76c44aaa5aa77107949197'
    base=read(base_path);candidate=read(candidate_path)
    if base_obs['actual_exit_code']==1:
        assert base['estimated_total_with_allowance']>=CAP
        err=(ROOT/base_obs['stderr']['path']).read_text()
        assert err.rstrip().endswith('AssertionError: Conservative estimate exceeds the delivery cap; report retained')
    else:
        assert not (ROOT/base_obs['stderr']['path']).read_bytes()
    assert not (ROOT/candidate_obs['stderr']['path']).read_bytes()
    assert candidate['result']=='PASS_EXACT_PROSPECTIVE_STREAM_AND_FULL_ROUNDTRIP'
    assert candidate['encoder_count']==1 and not candidate['creates_zip'] and not candidate['creates_tar_file']
    assert not candidate['installs_packaging_change']
    assert candidate['predicted_parent_png_versions_added']==0
    assert base['baseline_archive']==PARENT.name and base['baseline_bytes']==PARENT_BYTES
    assert base['baseline_sha256']==PARENT_SHA and base['baseline_identity_verified_before_and_after']
    assert base['parent_logical_paths']==10746 and base['parent_retention_rows']==163040
    assert candidate['archive']==PARENT.name and candidate['archive_bytes']==PARENT_BYTES
    assert candidate['archive_sha256']==PARENT_SHA and candidate['archive_unchanged']
    assert base['header_manifest_retention_late_text_allowance_bytes']==ALLOWANCE
    assert base['delivery_cap_bytes']==CAP and not base['creates_zip'] and not base['writes_authored_input_files']
    assert set(base['prospective_bundles'])=={'images','documents','data'}
    old_image=base['prospective_bundles']['images']
    assert old_image['dictionary_bytes']==134217728 and old_image['zip_method']=='ZIP_LZMA'
    assert old_image['metrics']==candidate['actual_estimator_image_metrics']
    assert old_image['metrics']['bundle_bytes']==IMAGE_BYTES and old_image['metrics']['bundle_sha256']==IMAGE_SHA
    for kind in ('documents','data'):
        row=base['prospective_bundles'][kind]
        assert row['dictionary_bytes']==67108864 and row['zip_method']=='ZIP_LZMA'
        assert row['compressed_bytes']>0 and row['metrics']['paths']>0
    cand=candidate['candidate']
    assert cand['dictionary_bytes']==268435456 and cand['zip_method']=='ZIP_LZMA' and cand['method_number']==14
    assert cand['method14_header_hex']=='090405005d00000010'
    assert cand['decoder_eof'] and cand['decoder_unused_bytes']==0
    assert candidate['input_preflight']==candidate['input_second_pass']==cand['roundtrip']
    assert cand['roundtrip']['bytes']==IMAGE_BYTES and cand['roundtrip']['sha256']==IMAGE_SHA
    saving=old_image['compressed_bytes']-cand['compressed_bytes']
    assert saving>0,'Do not install an unmeasured or nonimproving alternative'

    # Pin the actual final policy. The packager reads its image constant;
    # its source body is unchanged by the reviewed128-to256 module change.
    expected_sources={
      'code/package_checkpoint.py':'cf0a5219cf66ec07e7f8509634888392929fb1eced6f05748e35d462052938dc',
      'code/checkpoint_image_tar.py':FINAL_IMAGE_HELPER,
      'code/checkpoint_data_tar.py':'9e149cc79ca9790fc55a3147a4664c0886cbe1dc0b981727459a26bac35badbb',
      'code/checkpoint_standard_tar.py':'8d3253e1fcdb406c94f7aa1ca3a2a2ffeb4ab59bd9c44ed54958b9d13de2e2df',
      'code/checkpoint_archive_io.py':'e508fa3bae0cb845b5d02a0623aea6643a9981a7ade822fe87e7c539140e21e4',
      'records/checkpoint36_before_image256_install/checkpoint_image_tar.py':OLD_IMAGE_HELPER,
    }
    for rel,digest in expected_sources.items():assert hash_path(ROOT/rel)==digest,rel
    assert PARENT.stat().st_size==PARENT_BYTES and hash_path(PARENT)==PARENT_SHA
    m=read('records/checkpoint36_metrics.json')
    assert hash_path(ROOT/'LM4_SUCCESSOR_paper.pdf')==m['pdf_sha256']==base['current_main_pdf_sha256']
    assert (ROOT/'LM4_SUCCESSOR_paper.pdf').stat().st_size==m['pdf_bytes']

    # A full fresh deterministic hash, with no encoder, guards against any
    # image addition/change after the two actual compression measurements.
    sources=png_paths()
    identities={rel:(p.stat().st_size,hash_path(p)) for rel,p in sources.items()}
    sink=CountingSink()
    actual_metrics=stream_images(sources,identities,sink)
    assert actual_metrics==old_image['metrics']
    assert sink.result()==candidate['input_preflight']

    removed_main=base['previous_direct_main_pdf_compressed_payload_removed']
    migrated=base['previous_direct_main_pdf_migrated']
    assert base['previous_direct_main_pdf_headers_removed']==0
    assert removed_main==(0 if migrated is None else migrated['compressed_payload_bytes'])
    old_total=(PARENT_BYTES-sum(base['previous_container_compressed_bytes_removed'].values())
      -base['previous_direct_data_compressed_bytes_removed']-removed_main
      +sum(row['compressed_bytes'] for row in base['prospective_bundles'].values())
      +base['additional_direct_compressed_payload_bytes'])
    assert old_total==base['estimated_before_allowance']
    assert old_total+ALLOWANCE==base['estimated_total_with_allowance']
    report=copy.deepcopy(base)
    report['prospective_bundles']['images'].update(
      compressed_bytes=cand['compressed_bytes'],dictionary_bytes=268435456,
      elapsed_seconds=cand['compression_seconds'],actual_candidate_report=bound(candidate_path))
    total=old_total-saving
    assert total+ALLOWANCE<CAP,'The stronger measured candidate still exceeds the unchanged cap/allowance'
    report.update(recorded_at=datetime.now(timezone.utc).isoformat(),
      estimated_before_allowance=total,estimated_total_with_allowance=total+ALLOWANCE,
      estimated_headroom_bytes=CAP-total-ALLOWANCE,
      baseline_estimate_128=bound(base_path),baseline_estimate_observation=bound(args.base_observation),
      candidate_observation=bound(args.candidate_observation),same_image_stream_rehashed_at_combination=sink.result(),
      measured_image_saving_bytes_256_vs_128=saving,
      original_component_source_bindings=base['source_bindings'],
      source_bindings={rel:{'bytes':(ROOT/rel).stat().st_size,'sha256':hash_path(ROOT/rel)} for rel in expected_sources},
      accounting_source=bound('code/combine_checkpoint36_size_evidence.py'),
      measurement_method='Combine three completed actual component measurements with identical image input; no compressor executed by this accounting step.',
      scope='The preserved complete128MiB prospective estimate supplies actual document/data compression and conservative direct/header/retention accounting. Its image component is replaced only by the independently fully decoded256MiB measurement of exactly the same606720000-byte image TAR, whose complete current stream was rehashed here. No image/document/evidence is omitted. The old PDF payload is still removed exactly once; old headers and the unchanged5MB allowance remain. Small late textual records lie within that allowance. All failed/initial measurements and source versions remain retained. Actual immutable archive size remains authoritative.')
    target=ROOT/'records/checkpoint36_size_estimate.json'
    assert hash_path(target)==hash_path(ROOT/base_path),'Preserve the initial report before replacing its path'
    assert not (ROOT.parent/'LM4_SUCCESSOR_checkpoint_36.zip').exists()
    target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='predicted_history'},indent=2),flush=True)

if __name__=='__main__':main()
