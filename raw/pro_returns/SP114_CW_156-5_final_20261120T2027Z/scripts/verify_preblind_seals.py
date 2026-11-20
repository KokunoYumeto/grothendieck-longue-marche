"""Verify immutable blind inputs and preserved pre-audit page hashes.

No page or sealed file is written. Checkpoint ZIPs are read in memory, never
extracted. Current page changes after blind adjudication are expected; their
original hashes are verified against checkpoint02 or exact reverse edits.
"""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--utc',required=True)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--report',type=Path,required=True)
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[1]
    report={'verified_utc':args.utc,'immutable_files':[],
            'pre_audit_pages':[],'checkpoint_paths':{},'errors':[]}
    seals=json.loads((root/'review/second_seal_026_031.json').read_text())
    first_pages={row['path']:row['sha256'] for row in seals['files']
                 if row['path'].startswith('pages/')}
    immutable=[row for row in seals['files']
               if not row['path'].startswith('pages/')]
    later=json.loads((root/'review/second_seal_032_033.json').read_text())
    for row in later:
        first_pages[f'pages/J156-5-04_156-5_scan{row["scan"]:03}.tex']=row['edition_sha256']
        immutable += [{'path':'second/'+name,'sha256':value}
                      for name,value in row['files'].items()]
    for row in immutable:
        actual=sha((root/row['path']).read_bytes())
        result={'path':row['path'],'sealed_sha256':row['sha256'],
                'current_sha256':actual,'unchanged':actual==row['sha256']}
        report['immutable_files'].append(result)
        if not result['unchanged']:report['errors'].append('Immutable input changed: '+row['path'])
    with zipfile.ZipFile(args.checkpoint) as archive:
        archived_paths={r.filename for r in archive.infolist() if not r.is_dir()}
        current_paths={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
        manifest_name='review/archive_manifests/'+args.checkpoint.stem+'.json'
        manifest=json.loads(archive.read(manifest_name))
        manifest_paths={r['path'] for r in manifest['files_before_manifest']}|{manifest_name}
        missing=sorted(archived_paths-current_paths)
        disagreement=sorted(archived_paths^manifest_paths)
        report['checkpoint_paths']={
            'archive':str(args.checkpoint.resolve()),
            'archive_files':len(archived_paths),
            'manifest_files_including_manifest':len(manifest_paths),
            'manifest_and_archive_agree':not disagreement,
            'manifest_path_disagreement':disagreement,
            'missing_current_paths':missing,
            'all_checkpoint_files_remain':not missing,
            'scope':'Path continuity only; updated contents and losslessly recompressed PNG encodings are expected.'}
        if missing:report['errors'].append('Checkpoint paths missing from deliverable')
        if disagreement:report['errors'].append('Checkpoint ZIP/manifest filename mismatch')
        for path,expected in sorted(first_pages.items()):
            current=(root/path).read_bytes()
            scan=int(Path(path).stem[-3:])
            record=json.loads((root/f'review/scan{scan:03}_adjudicated.json').read_text())
            if scan<=31:
                original=archive.read(path)
                method='Actual pre-audit page bytes retained in checkpoint02, read in memory without extraction'
            else:
                data=json.loads((root/f'second/scan{scan:03}_adjudication_input.json').read_text())
                text=current.decode('utf-8')
                for edit in reversed(data['edits']):
                    count=edit.get('count',1)
                    if not edit['new'] or text.count(edit['new'])!=count:
                        raise ValueError(f'Nonunique reverse edit for scan{scan:03}; no page was written')
                    text=text.replace(edit['new'],edit['old'],count)
                original=text.encode('utf-8')
                method='Original page reconstructed in memory by reversing the exact recorded blind-adjudication edits'
            actual=sha(original)
            before=record.get('second_page_hashes',{}).get('before')
            if before is None:
                candidate=root/f'second/scan{scan:03}_adjudication_input.json'
                if candidate.exists():before=json.loads(candidate.read_text()).get('page_before_sha256')
            row={'path':path,'sealed_sha256':expected,'verified_original_sha256':actual,
                 'original_matches_seal':actual==expected,'method':method,
                 'current_sha256':sha(current),'current_is_original':sha(current)==expected,
                 'audit_complete_at_read':bool(record.get('second_audit_complete')),
                 'declared_pre_audit_sha256':before,
                 'declared_pre_audit_matches_seal':before==expected if before else None}
            report['pre_audit_pages'].append(row)
            if not row['original_matches_seal']:report['errors'].append('Original page does not match seal: '+path)
            if before and before!=expected:report['errors'].append('Declared pre-audit hash does not match seal: '+path)
    report['immutable_count']=len(report['immutable_files'])
    report['pre_audit_page_count']=len(report['pre_audit_pages'])
    report['sealed_entries_verified']=report['immutable_count']+report['pre_audit_page_count']
    report['passed']=not report['errors'] and report['sealed_entries_verified']==24
    args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['verified_utc','immutable_count','pre_audit_page_count','sealed_entries_verified','checkpoint_paths','errors','passed']},ensure_ascii=False))
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
