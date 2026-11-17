"""Combine actual image256/document128/data64 evidence; no encoder or ZIP."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,copy,hashlib,json,zipfile
from measure_checkpoint36_prospective_image256 import png_paths,stream_images,CountingSink
from measure_checkpoint36_prospective_document128 import document_paths,stream_documents
from checkpoint_image_tar import IMAGE_DICTIONARY_BYTES
from checkpoint_document_tar import DOCUMENT_DICTIONARY_BYTES
from checkpoint_data_tar import DATA_DICTIONARY_BYTES

ROOT=Path(__file__).resolve().parents[1]
PARENT=ROOT.parent/'LM4_SUCCESSOR_checkpoint_35.zip'
PARENT_SHA='33b0925ca3ba12d8944fc47243807a3c61ebb2a4f03ec47f7bb2ce1a5a83f121'
BASE_PATH='records/checkpoint36_first_size_estimate/checkpoint36_size_estimate.json'
BASE_SHA='005b64fab4b5cf9dfd302ca5c837b053b3b06045765012b187fb1d2ac2436d28'
CAP=536870912
ALLOWANCE=5000000

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
    return h.hexdigest()
def read(rel):return json.loads((ROOT/rel).read_text())
def bound(rel):
    p=ROOT/rel
    return dict(path=rel,bytes=p.stat().st_size,sha256=sha(p))
def check(item):
    assert bound(item['path'])=={k:item[k] for k in ('path','bytes','sha256')},item['path']
def observation(rel,report_path,source_path,source_sha,exit_code):
    o=read(rel)
    assert o['actual_tool_result_observed'] is True
    assert isinstance(o['session_id'],int) and o['session_id']>0
    assert o['initial_tool_chunk'] and o['actual_completion_tool_chunk']
    assert o['actual_exit_code']==exit_code
    assert o['report']['path']==report_path
    assert o['source']['path']==source_path and o['source']['sha256']==source_sha
    for k in ('source','report','stdout','stderr'):check(o[k])
    if exit_code==0:assert o['stderr']['bytes']==0
    return o

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-observation',required=True)
    parser.add_argument('--image-observation',required=True)
    parser.add_argument('--document-observation',required=True)
    parser.add_argument('--installation',required=True)
    args=parser.parse_args()
    assert not (ROOT.parent/'LM4_SUCCESSOR_checkpoint_36.zip').exists()
    assert sha(ROOT/BASE_PATH)==BASE_SHA
    assert sha(ROOT/'records/checkpoint36_size_estimate.json')==BASE_SHA
    base_obs=observation(args.base_observation,BASE_PATH,'code/estimate_checkpoint36_size.py',
      '293e093f5d0cdc7ed8d841182b2c33e09f0c38bde414724891ea7a3d50bc0e47',1)
    base=read(BASE_PATH)
    assert (ROOT/base_obs['stderr']['path']).read_text().rstrip().endswith(
      'AssertionError: Conservative estimate exceeds the delivery cap; report retained')
    assert base['estimated_total_with_allowance']==545183245>=CAP
    assert base['header_manifest_retention_late_text_allowance_bytes']==ALLOWANCE
    assert base['delivery_cap_bytes']==CAP and not base['creates_zip'] and not base['writes_authored_input_files']
    assert base['baseline_archive']==PARENT.name and base['baseline_bytes']==530938760
    assert base['baseline_sha256']==PARENT_SHA and base['baseline_identity_verified_before_and_after']
    assert base['parent_logical_paths']==10746 and base['parent_retention_rows']==163040
    assert PARENT.stat().st_size==530938760 and sha(PARENT)==PARENT_SHA
    specs={
      'images':(args.image_observation,'records/checkpoint36_prospective_image256_measurement.json',
        'code/measure_checkpoint36_prospective_image256.py','33fe2d1d463b774ff65032c5cd2924af8e036592ec76c44aaa5aa77107949197',
        'actual_estimator_image_metrics',134217728,268435456,'090405005d00000010'),
      'documents':(args.document_observation,'records/checkpoint36_prospective_document128_measurement.json',
        'code/measure_checkpoint36_prospective_document128.py','f063ce24764aa7e077757ecdffc81f784a5c4aa010b98e671dfbe32c6312c9f9',
        'actual_estimator_document_metrics',67108864,134217728,'090405005d00000008')}
    candidates={};observations={};savings={}
    for kind,(obs_path,report_path,source_path,source_sha,metrics_key,old_dictionary,new_dictionary,header) in specs.items():
        observations[kind]=observation(obs_path,report_path,source_path,source_sha,0)
        candidate=read(report_path);candidates[kind]=candidate
        assert candidate['result']=='PASS_EXACT_PROSPECTIVE_STREAM_AND_FULL_ROUNDTRIP'
        assert candidate['archive']==PARENT.name and candidate['archive_bytes']==530938760
        assert candidate['archive_sha256']==PARENT_SHA and candidate['archive_unchanged']
        assert candidate['encoder_count']==1 and not candidate['baseline_reencoded']
        assert not candidate['creates_zip'] and not candidate['creates_tar_file'] and not candidate['installs_packaging_change']
        old=base['prospective_bundles'][kind];new=candidate['candidate']
        assert old['metrics']==candidate[metrics_key]
        assert old['dictionary_bytes']==old_dictionary and new['dictionary_bytes']==new_dictionary
        assert old['zip_method']==new['zip_method']=='ZIP_LZMA'
        assert new['method_number']==14 and new['method14_header_hex']==header
        assert new['decoder_eof'] and new['decoder_unused_bytes']==0
        assert candidate['input_preflight']==candidate['input_second_pass']==new['roundtrip']
        assert new['roundtrip']['bytes']==old['metrics']['bundle_bytes']
        assert new['roundtrip']['sha256']==old['metrics']['bundle_sha256']
        savings[kind]=old['compressed_bytes']-new['compressed_bytes']
        assert savings[kind]>0
    assert candidates['images']['predicted_parent_png_versions_added']==0
    assert candidates['documents']['baseline_actual_document64_compressed_bytes']==base['prospective_bundles']['documents']['compressed_bytes']
    assert candidates['documents']['saving_from_actual_document64_bytes']==savings['documents']
    assert base['prospective_bundles']['data']['dictionary_bytes']==67108864
    assert base['prospective_bundles']['data']['zip_method']=='ZIP_LZMA'
    assert (IMAGE_DICTIONARY_BYTES,DOCUMENT_DICTIONARY_BYTES,DATA_DICTIONARY_BYTES)==(268435456,134217728,67108864)
    installation=read(args.installation)
    assert installation['result']=='PASS_REVIEWED_MEASURED_DICTIONARIES_INSTALLED'
    installed={item['path']:item for item in installation['installed_sources']}
    required={'code/package_checkpoint.py','code/checkpoint_image_tar.py','code/checkpoint_document_tar.py',
      'code/check_checkpoint36_preconditions.py','code/publish_checkpoint36_readiness.py','code/verify_checkpoint36_system_tars.py'}
    assert required<=set(installed)
    for item in installed.values():check(item)
    assert sha(ROOT/'code/checkpoint_data_tar.py')=='9e149cc79ca9790fc55a3147a4664c0886cbe1dc0b981727459a26bac35badbb'
    assert sha(ROOT/'records/checkpoint36_before_dual_dictionary_install/checkpoint_image_tar.py')=='c3de17157c5d6fa5ac66bfc64717df096c3dbcc195965be1a7d91c878df352f6'
    assert sha(ROOT/'records/checkpoint36_before_dual_dictionary_install/package_checkpoint.py')=='cf0a5219cf66ec07e7f8509634888392929fb1eced6f05748e35d462052938dc'

    # Rehash both exact current streams. No encoder is created here.
    image_sources=png_paths()
    image_ids={rel:(p.stat().st_size,sha(p)) for rel,p in image_sources.items()}
    image_sink=CountingSink()
    assert stream_images(image_sources,image_ids,image_sink)==base['prospective_bundles']['images']['metrics']
    assert image_sink.result()==candidates['images']['input_preflight']
    doc_sources=document_paths()
    doc_ids={rel:(p.stat().st_size,sha(p)) for rel,p in doc_sources.items()}
    old_pdf=base['previous_direct_main_pdf_migrated']
    assert old_pdf['path']=='LM4_SUCCESSOR_paper.pdf'
    pending=[r for r in base['predicted_history'] if r['path'].endswith('.pdf')]
    assert len(pending)==1 and pending[0]['path']==old_pdf['historical_path']
    if old_pdf['historical_path'] not in doc_sources:
        with zipfile.ZipFile(PARENT) as z:data=z.read('LM4_SUCCESSOR/'+old_pdf['path'])
        assert len(data)==old_pdf['bytes'] and hashlib.sha256(data).hexdigest()==old_pdf['sha256']
        doc_sources[old_pdf['historical_path']]=data
        doc_ids[old_pdf['historical_path']]=(len(data),old_pdf['sha256'])
    else:
        assert doc_ids[old_pdf['historical_path']]==(old_pdf['bytes'],old_pdf['sha256'])
    doc_sink=CountingSink()
    assert stream_documents(doc_sources,doc_ids,doc_sink)==base['prospective_bundles']['documents']['metrics']
    assert doc_sink.result()==candidates['documents']['input_preflight']
    metrics=read('records/checkpoint36_metrics.json')
    assert sha(ROOT/'LM4_SUCCESSOR_paper.pdf')==metrics['pdf_sha256']==base['current_main_pdf_sha256']
    assert (ROOT/'LM4_SUCCESSOR_paper.pdf').stat().st_size==metrics['pdf_bytes']
    assert base['previous_direct_main_pdf_headers_removed']==0
    assert base['previous_direct_main_pdf_compressed_payload_removed']==old_pdf['compressed_payload_bytes']
    old_total=(530938760-sum(base['previous_container_compressed_bytes_removed'].values())
      -base['previous_direct_data_compressed_bytes_removed']-old_pdf['compressed_payload_bytes']
      +sum(row['compressed_bytes'] for row in base['prospective_bundles'].values())
      +base['additional_direct_compressed_payload_bytes'])
    assert old_total==base['estimated_before_allowance']
    assert old_total+ALLOWANCE==base['estimated_total_with_allowance']
    total=old_total-sum(savings.values())
    assert total+ALLOWANCE<CAP,'Measured replacements still exceed unchanged cap and allowance'
    report=copy.deepcopy(base)
    for kind,(_,report_path,_,_,_,_,new_dictionary,_) in specs.items():
        candidate=candidates[kind]['candidate']
        report['prospective_bundles'][kind].update(compressed_bytes=candidate['compressed_bytes'],
          dictionary_bytes=new_dictionary,elapsed_seconds=candidate['compression_seconds'],
          actual_candidate_report=bound(report_path))
    source_paths=sorted(set(installed)|{'code/checkpoint_data_tar.py','code/checkpoint_standard_tar.py',
      'code/checkpoint_archive_io.py','code/combine_checkpoint36_dual_dictionary_size_evidence.py'})
    report.update(recorded_at=datetime.now(timezone.utc).isoformat(),estimated_before_allowance=total,
      estimated_total_with_allowance=total+ALLOWANCE,estimated_headroom_bytes=CAP-total-ALLOWANCE,
      baseline_estimate_128=bound(BASE_PATH),baseline_estimate_observation=bound(args.base_observation),
      component_measurement_observations={kind:bound(specs[kind][0]) for kind in specs},
      measured_component_savings=savings,same_streams_rehashed_at_combination={'images':image_sink.result(),'documents':doc_sink.result()},
      original_component_source_bindings=base['source_bindings'],
      source_bindings={rel:{'bytes':(ROOT/rel).stat().st_size,'sha256':sha(ROOT/rel)} for rel in source_paths},
      installation=bound(args.installation),accounting_source=bound('code/combine_checkpoint36_dual_dictionary_size_evidence.py'),
      measurement_method='Combine completed exact image256/document128 measurements with completed actual data64, after full fresh image/document stream hashes; no encoder in this step.',
      scope='Only two actual compressed components are replaced, each with a complete same-input independently decoded measurement. The completed original data64 and conservative direct/header/retention accounting are reused unchanged. No payload or image is omitted. The old main PDF compressed payload is removed exactly once, headers remain counted, and the5000000-byte late-text/manifest/retention allowance is unchanged. All original/failed reports, proposals and sources remain retained. Actual immutable archive size remains authoritative.')
    assert sha(ROOT/'records/checkpoint36_size_estimate.json')==BASE_SHA
    (ROOT/'records/checkpoint36_size_estimate.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='predicted_history'},indent=2),flush=True)

if __name__=='__main__':main()
