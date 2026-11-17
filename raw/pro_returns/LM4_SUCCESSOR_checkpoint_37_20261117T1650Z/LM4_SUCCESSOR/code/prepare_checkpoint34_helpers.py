"""Create separate 33-to-34 source candidates; never create an archive."""
from pathlib import Path
from hashlib import sha256
import difflib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    pairs = [
        ('preserve_checkpoint33_versions_inductive.py', 'preserve_checkpoint34_versions_inductive.py'),
        ('verify_checkpoint33_inductive_retention.py', 'verify_checkpoint34_inductive_retention.py'),
        ('estimate_checkpoint33_size.py', 'estimate_checkpoint34_size.py'),
        ('verify_checkpoint33_system_tars.py', 'verify_checkpoint34_system_tars.py'),
        ('build_checkpoint33_parent_anchor.py', 'build_checkpoint34_parent_anchor.py'),
    ]
    common = {'32':'33', '33':'34'}
    counts = {'9680':'10053', '132920':'142600', '142600':'152653'}
    rows = []
    diffs = []
    for old_name, new_name in pairs:
        old_path, new_path = ROOT/'code'/old_name, ROOT/'code'/new_name
        assert not new_path.exists()
        before = old_path.read_text()
        changes = dict(common)
        if 'inductive' in new_name or 'anchor' in new_name:
            changes.update(counts)
            changes['31'] = '32'
        if 'anchor' in new_name:
            changes.update({'30':'31', '9388':'9680', '494718836':'508499680',
                            '33853':'5195', '94597':'28023', '7370':'66162'})
        pattern = r'(?<!\d)('+'|'.join(sorted(changes,key=len,reverse=True))+r')(?!\d)'
        after = re.sub(pattern, lambda m: changes[m.group(0)], before)
        if 'anchor' in new_name:
            after = after.replace(
                '67ad6a36bef8bc98dbf3a6db7426065765022ca95d18434e6bde60d56c24f2c0',
                '5c68edb5a023c97cb400b506f7e1b7303f19e3cac9212947491e47793d77ef96')
        compile(after, str(new_path), 'exec')
        with new_path.open('x') as stream:
            stream.write(after)
        rows.append({'source':str(old_path.relative_to(ROOT)),
                     'source_sha256':sha256(before.encode()).hexdigest(),
                     'target':str(new_path.relative_to(ROOT)),
                     'target_sha256':sha256(after.encode()).hexdigest(),
                     'target_bytes':len(after.encode())})
        diffs.extend(difflib.unified_diff(before.splitlines(True),after.splitlines(True),
                                         fromfile=old_name,tofile=new_name))
    with (ROOT/'records/checkpoint34_helper_source_adaptation.json').open('x') as stream:
        json.dump({'archive_created':False,'retention_published':False,'copies':rows,
                   'parent_logical_entries':10053,'inherited_rows':142600,
                   'expected_child_retention_rows':152653},stream,indent=2)
        stream.write('\n')
    with (ROOT/'records/checkpoint34_helper_source_adaptation.diff').open('x') as stream:
        stream.writelines(diffs)
    print(json.dumps(rows,indent=2))


if __name__ == '__main__':
    main()
