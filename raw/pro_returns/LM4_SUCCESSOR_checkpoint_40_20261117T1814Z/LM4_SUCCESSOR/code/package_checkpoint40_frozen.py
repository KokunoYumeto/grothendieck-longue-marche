"""Separate checkpoint40 authorization and sole exact sealed ZIP assembly.

No39 source or input is modified. Preparation explicitly applies only the
approved59 derivative omissions and proves zero historical-target omissions.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse
import json
import os
import zipfile
from checkpoint39_frozen_spools import (CAP, DEPENDENCIES, PREFIX, identity,
    relative_path, runtime_contract, exact_layout, json_exclusive, replay_entry,
    utc_now, verify_archived_spans)
ROOT=Path(__file__).resolve().parents[1]
NUMBER=40
CONTENTS='records/checkpoint_40_contents_sha256.tsv'
PACKAGING='records/checkpoint_40_packaging.json'
PREFLIGHT='records/checkpoint40_spool_preflight.json'
GENERATED={CONTENTS,PACKAGING,PREFLIGHT}
SOURCES=['code/package_checkpoint40_frozen.py','code/checkpoint40_filtered_prepare.py',
         'code/package_checkpoint39_frozen.py','code/reseal_checkpoint39_data512.py',
         'code/checkpoint39_frozen_spools.py']+list(DEPENDENCIES)
PAUSED_AGENTS={'/root/involutions','/root/torus_real','/root/topology_census'}
OPEN_NOT_BEFORE=datetime(2026,11,17,19,49,30,tzinfo=timezone.utc)
OPEN_BEFORE=datetime(2026,11,17,20,49,30,tzinfo=timezone.utc)

def validate_binding(binding):
    relative_path(binding['path'])
    actual = identity(ROOT/binding['path'])
    assert actual['bytes'] == binding['bytes'] and actual['sha256'] == binding['sha256'], binding['path']
    if 'crc32' in binding:
        assert actual['crc32'] == binding['crc32']
    return actual


def authorization(relative):
    relative_path(relative)
    value = json.loads((ROOT/relative).read_text())
    assert value['checkpoint'] == NUMBER and value['result'] == 'PASS_FROZEN_INPUTS_AUTHORIZED'
    bindings = value['bindings'] + [value['final_pdf'], value['retention_ledger']] + value['pause_receipts']
    assert value['final_pdf']['path'] == 'LM4_SUCCESSOR_paper.pdf'
    seen = {}
    for binding in bindings:
        assert binding['path'] not in GENERATED
        actual = validate_binding(binding)
        if binding['path'] in seen:
            assert seen[binding['path']] == actual
        seen[binding['path']] = actual
    assert set(SOURCES) <= set(seen), 'Authorization must pin the new pair and three unchanged codecs'
    agents = set()
    assert len(value['pause_receipts']) == 3
    for binding in value['pause_receipts']:
        receipt = json.loads((ROOT/binding['path']).read_text())
        assert receipt['paused'] is True and receipt['owned_live_producers'] == []
        paused = datetime.fromisoformat(receipt['paused_at'])
        assert paused.tzinfo is not None and paused <= datetime.now(timezone.utc)
        assert receipt['agent'] not in agents
        agents.add(receipt['agent'])
    assert agents == PAUSED_AGENTS
    runtime = runtime_contract(ROOT)
    return {'path': relative, 'identity': identity(ROOT/relative), 'record': value,
            'checked_bindings': seen, 'runtime': runtime}


def exclusion_reason(f):
    """Unchanged authored-file exclusions from the reviewed checkpoint38 policy."""
    r = f.relative_to(ROOT).as_posix()
    if r in {'verification_images.tar', 'historical_documents.tar', 'historical_data.tar'}:
        return 'Storage-only container from a restored checkpoint; all original logical files are retained and repackaged individually by path.'
    if r.startswith('tex_cache/'):
        return 'Regenerable TeX/font infrastructure; build recipe, sources, output PDF and logs retained.'
    if r.startswith('work_CE/') and f.parent == ROOT/'work_CE' and (f.name.startswith('D_') or f.name.startswith('LM6_')):
        return 'Verbatim excerpt of user-provided attachment; independent audit retained.'
    if r.startswith('work_DE/') and f.name.endswith('_source.txt'):
        return 'Verbatim excerpt of user-provided attachment; independent audit retained.'
    if 'work_CE/sources/' in r and f.suffix.lower() in {'.pdf', '.txt'}:
        return 'Third-party full source copy; authoritative links, bibliography and reading records retained.'
    if (r.startswith('work_DE/') and f.name not in {'B118_initial_spacing.pdf', 'B122_initial_layout.pdf', 'B128_initial_comma.pdf'}
            and not f.with_suffix('.tex').exists()
            and (f.suffix.lower() == '.pdf' or (f.suffix.lower() == '.txt' and f.with_suffix('.pdf').exists()
                 and f.stem not in {'DE_review', 'B_separability_review'}))):
        return 'Third-party full source copy; authoritative links, bibliography and reading records retained.'
    if '__pycache__' in f.parts or f.suffix in {'.aux', '.toc', '.blg', '.bbl'}:
        return 'Regenerable TeX/Python auxiliary; source, output PDF, build logs and recipes retained.'
    return None


def checked_stage(stage):
    stage = Path(stage).resolve()
    assert stage.parent == ROOT.parent.resolve() and stage.name.startswith('.checkpoint40_stage_')
    assert stage.is_dir() and not stage.is_symlink()
    return stage


def validate_seal(stage, expected_sha):
    stage = checked_stage(stage)
    assert identity(stage/'sealed-plan.json')['sha256'] == expected_sha
    plan = json.loads((stage/'sealed-plan.json').read_text())
    assert plan['result'] == 'PASS_SEALED_EXACT_SIZE' and plan['checkpoint'] == NUMBER
    assert plan['stage'] == str(stage) and plan['output'] == str(ROOT.parent/'LM4_SUCCESSOR_checkpoint_40.zip')
    assert identity(stage/'snapshot.json') == plan['snapshot_identity']
    assert authorization(plan['authorization']['path']) == plan['authorization']
    assert runtime_contract(ROOT) == plan['runtime']
    for relative, expected in plan['source_bindings'].items():
        assert identity(ROOT/relative) == expected
    assert exact_layout(plan['entries']) == plan['layout'] and plan['layout']['exact_zip_bytes'] <= CAP
    assert plan['open_not_before'] == OPEN_NOT_BEFORE.isoformat() and plan['open_before'] == OPEN_BEFORE.isoformat()
    assert plan['zip_metadata']['entry_extra_hex'] == plan['zip_metadata']['entry_comment_hex'] == plan['zip_metadata']['archive_comment_hex'] == ''
    for row in plan['entries']:
        for key in ['raw_path', 'payload_path', 'encoder_report_path', 'decoder_report_path']:
            relative_path(row[key])
        assert identity(stage/row['raw_path']) == row['raw_identity']
        assert identity(stage/row['payload_path']) == row['payload_identity']
        assert identity(stage/row['encoder_report_path']) == row['encoder_report_identity']
        assert identity(stage/row['decoder_report_path']) == row['decoder_report_identity']
        encoded = json.loads((stage/row['encoder_report_path']).read_text())
        decoded = json.loads((stage/row['decoder_report_path']).read_text())
        assert encoded['input'] == decoded['roundtrip'] == row['raw_identity']
        assert encoded['payload'] == decoded['payload'] == row['payload_identity']
        assert encoded['zip_method'] == decoded['zip_method'] == row['zip_method']
        assert decoded['decoder_eof'] is True and decoded['unused_bytes'] == 0
        for key in ['encoder_observed', 'decoder_observed']:
            observed = row[key]
            assert observed['returncode'] == 0
            for stream in ['stdout', 'stderr']:
                relative_path(observed[stream+'_path'])
                path = stage/observed[stream+'_path']
                assert identity(path) == observed[stream+'_identity']
                assert path.read_bytes() == observed[stream+'_utf8'].encode()
    return plan


def assemble(stage, expected_sha):
    stage = checked_stage(stage)
    plan = validate_seal(stage, expected_sha)
    out = Path(plan['output'])
    assert not out.exists(), 'Never overwrite or append to a checkpoint'
    assert not (stage/'assembly-open-attempt.json').exists(), 'No second assembly attempt'
    class ExclusiveDeadlineZipFile(zipfile.ZipFile):
        def __init__(self, file, mode, **kwargs):
            assert mode == 'x' and Path(file).resolve() == out.resolve()
            now = datetime.now(timezone.utc)
            assert OPEN_NOT_BEFORE <= now < OPEN_BEFORE, 'Actual exclusive constructor outside authorized slot'
            json_exclusive(stage/'assembly-open-attempt.json', {
                'checked_at': now.isoformat(), 'path': str(out), 'mode': mode,
                'plan_sha256': expected_sha, 'exact_bytes': plan['layout']['exact_zip_bytes'],
                'scope': 'Constructor attempt only; completion is not yet observed.'})
            # The time is checked again immediately before the inherited open.
            assert OPEN_NOT_BEFORE <= datetime.now(timezone.utc) < OPEN_BEFORE
            super().__init__(file, mode=mode, **kwargs)
    print('All sealed identities validated; entering sole exclusive40 constructor.', utc_now(), flush=True)
    try:
        with ExclusiveDeadlineZipFile(out, 'x', allowZip64=False) as z:
            assert z._seekable and z.start_dir == 0 and z.comment == b''
            for row, location in zip(plan['entries'], plan['layout']['entries'], strict=True):
                info = replay_entry(z, stage, row, plan['zip_metadata']['date_time'])
                assert info.header_offset == location['header_offset']
            assert z.start_dir == plan['layout']['central_directory_offset']
            assert len(z.filelist) == len(plan['entries'])
        with out.open('rb') as archived:
            os.fsync(archived.fileno())
        assert out.stat().st_size == plan['layout']['exact_zip_bytes'] <= CAP
        with zipfile.ZipFile(out, 'r') as z:
            assert z.comment == b'' and len(z.infolist()) == len(plan['entries'])
            for info, row, location in zip(z.infolist(), plan['entries'], plan['layout']['entries'], strict=True):
                assert info.filename == row['archive_name'] and info.compress_type == row['zip_method']
                assert info.file_size == row['raw_identity']['bytes'] and info.CRC == row['raw_identity']['crc32']
                assert info.compress_size == row['payload_identity']['bytes']
                assert info.header_offset == location['header_offset'] and info.extra == info.comment == b''
                assert info.flag_bits == (2 if info.compress_type == zipfile.ZIP_LZMA else 0)
                date_time = list(plan['zip_metadata']['date_time'])
                date_time[-1] = date_time[-1]//2*2
                assert info.date_time == tuple(date_time)
        physical = verify_archived_spans(out, plan['entries'], plan['layout'], plan['zip_metadata']['date_time'])
        actual = identity(out)
        assert actual['bytes'] == plan['layout']['exact_zip_bytes'] <= CAP
        for relative, expected in plan['source_bindings'].items():
            assert identity(ROOT/relative) == expected
        report = {'result': 'PASS_EXACT_SEALED_ZIP_ASSEMBLED', 'closed_at': utc_now(),
                  'archive': str(out), 'archive_identity': actual, 'plan_sha256': expected_sha,
                  'exact_zip_bytes': plan['layout']['exact_zip_bytes'], 'logical_file_count': plan['logical_file_count'],
                  'all_payloads_replayed_without_recompression': True,
                  'archived_compressed_spans_and_local_headers': physical,
                  'scope': 'Ordinary ZIP structure and exact sealed size checked. Separate generic, native TAR and retention verification remain required. No parent38 archive is asserted.'}
        json_exclusive(stage/'assembly-result.json', report)
        print(json.dumps(report, indent=2), flush=True)
    except BaseException as error:
        json_exclusive(stage/'assembly-failure.json', {'recorded_at': utc_now(),
                       'error_type': type(error).__name__, 'error': str(error),
                       'archive_path': str(out), 'archive_exists': out.exists(),
                       'scope': 'Failure observed; any partial archive is preserved and no retry is performed.'})
        raise


def main():
    parser=argparse.ArgumentParser()
    sub=parser.add_subparsers(dest='command',required=True)
    p=sub.add_parser('prepare');p.add_argument('--authorization',required=True)
    p=sub.add_parser('assemble');p.add_argument('--stage',required=True);p.add_argument('--plan-sha256',required=True)
    args=parser.parse_args()
    if args.command=='prepare':
        from checkpoint40_filtered_prepare import prepare
        prepare(args.authorization)
    else:
        assemble(args.stage,args.plan_sha256)

if __name__=='__main__':
    main()
