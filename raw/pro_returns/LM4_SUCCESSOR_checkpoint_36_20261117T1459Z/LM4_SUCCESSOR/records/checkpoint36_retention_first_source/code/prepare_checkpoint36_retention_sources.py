"""Author separate36 retention helpers from exact reviewed35 source bytes.

This creates source and diffs only. It opens no archive, runs no generated
helper, and does not publish or change the live retention table.
"""
from pathlib import Path
import ast,hashlib,json,re,difflib

ROOT=Path(__file__).resolve().parents[1]
SOURCES={
 'preserve_checkpoint35_versions_inductive.py':'5f2203fe56aedf3237b3671f1cfb498ce724574f2819d9e4ff0a9b2c4d2a3f33',
 'verify_checkpoint35_inductive_retention.py':'b6ae3f0d76d78c33454c171a1d1b006b2e3b4b3155ce3e9110307455bf9273cb',
 'build_checkpoint35_parent_anchor.py':'63755c5b2bdab1bc9527c9c2b31b3f7ac36773785d5e4716c9a288c422d6442b',
 'verify_checkpoint35_system_tars.py':'6fb98bfd7824e0145d2186d37fafb942b3294c6d23600e94cbf7fb2e91f366cd',
}
NUMBERS={'33':'34','34':'35','35':'36','10387':'10746',
 '152653':'163040','163040':'173786','529409669':'530938760',
 '10053':'10387','83033':'19472','88075':'60334','81129':'29713'}
PARENT_OLD='28dbe8b35a6f9e1c6b7e606aa59ceed041f2ab217959e0cc243ab7e83761d8fb'
PARENT_NEW='33b0925ca3ba12d8944fc47243807a3c61ebb2a4f03ec47f7bb2ce1a5a83f121'

def adapt(source):
    # Protect every digest from any numeric substitution, then restore it.
    digests=[]
    def protect(m):
        digests.append(m[0]);return '@DIGEST_'+str(len(digests)-1)+'@'
    text=re.sub(r'[0-9a-f]{64}',protect,source)
    pattern=r'(?<![0-9])(?:'+ '|'.join(sorted(NUMBERS,key=len,reverse=True))+r')(?![0-9])'
    text=re.sub(pattern,lambda m:NUMBERS[m[0]],text)
    text=re.sub(r'@DIGEST_([0-9]+)@',lambda m:digests[int(m[1])],text)
    return text.replace(PARENT_OLD,PARENT_NEW)

records=[]
for basename,expected in SOURCES.items():
    oldpath=ROOT/'code'/basename;old=oldpath.read_bytes()
    assert hashlib.sha256(old).hexdigest()==expected
    source=old.decode();new=adapt(source)
    if basename=='build_checkpoint35_parent_anchor.py':
        new=new.replace('"a92f0e"','"3e985f"').replace('"0c93d3"','"1a39d7"').replace('"25e218"','"43e040"')
        marker='    pinned = {}\n'
        assert new.count(marker)==1
        observation='''    observed_path = ROOT / "records/checkpoint35_verification_observed.json"
    observed_raw = observed_path.read_bytes()
    observed = json.loads(observed_raw)
    assert observed["all_actual_exit_codes_observed"] is True
    assert observed["archive_sha256"] == EXPECTED_SHA
    for role, evidence in verifications.items():
        for key, value in evidence.items():
            assert observed["verifications"][role][key] == value
    pinned = {}
'''
        new=new.replace(marker,observation)
        marker='            "verification_records": verifications,\n'
        assert new.count(marker)==1
        new=new.replace(marker,marker+'''            "verification_observation": {"path": str(observed_path.relative_to(ROOT)),
                "bytes": len(observed_raw), "sha256": digest(observed_raw)},
''')
        start=new.index('    observed = {"recorded_at": datetime.now(timezone.utc).isoformat(),')
        end=new.index('    print(json.dumps(anchor, indent=2, sort_keys=True))',start)
        new=new[:start]+new[end:]
    if basename=='verify_checkpoint35_system_tars.py':
        oldline="    assert image_dictionary_bytes == 67108864 == packaging['image_lzma_dictionary_bytes']"
        assert new.count(oldline)==1
        new=new.replace(oldline,"    assert image_dictionary_bytes == 134217728 == packaging['image_lzma_dictionary_bytes']")
    ast.parse(new)
    target=ROOT/'code'/basename.replace('checkpoint35','checkpoint36')
    assert not target.exists()
    target.write_text(new)
    diffpath=ROOT/'records'/('checkpoint36_'+target.stem+'_source.diff')
    with diffpath.open('x') as stream:
        stream.writelines(difflib.unified_diff(source.splitlines(True),new.splitlines(True),
            fromfile=str(oldpath.relative_to(ROOT)),tofile=str(target.relative_to(ROOT))))
    raw=target.read_bytes()
    records.append(dict(source=str(oldpath.relative_to(ROOT)),source_sha256=expected,
        target=str(target.relative_to(ROOT)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
        diff=str(diffpath.relative_to(ROOT)),diff_sha256=hashlib.sha256(diffpath.read_bytes()).hexdigest()))
with (ROOT/'records/checkpoint36_retention_source_generation.json').open('x') as stream:
    json.dump(dict(sources=records,scope='Source-only creation; no helper run, archive creation or retention publication.'),stream,indent=2);stream.write('\n')
print(json.dumps(records,indent=2))
