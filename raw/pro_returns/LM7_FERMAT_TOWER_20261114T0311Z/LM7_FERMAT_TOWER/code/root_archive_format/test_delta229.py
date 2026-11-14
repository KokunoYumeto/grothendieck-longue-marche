"""Restore every selected original binary string and exercise rejection guards."""
from pathlib import Path
import copy,hashlib,importlib.util,json,os,shutil,subprocess,sys,time

HERE=Path(__file__).resolve().parent
TREE=HERE.parent/'LM7_FERMAT_TOWER'
sha=lambda b:hashlib.sha256(b).hexdigest()
spec=importlib.util.spec_from_file_location('restorer',TREE/'code/materialize_archive_files.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def main():
    started=time.monotonic();fresh=HERE/'fresh229_delta';assert not fresh.exists();fresh.mkdir()
    plans={}
    for name in ['archive_binary_deltas.json','archive_binary_aliases.json','archive_image_aliases.json']:
        source=TREE/'ledger'/name;target=fresh/'ledger'/name
        target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(source.read_bytes())
        plans[name]=json.loads(source.read_bytes())
    deltas=plans['archive_binary_deltas.json']['deltas']
    aliases=plans['archive_binary_aliases.json']['aliases']+plans['archive_image_aliases.json']['aliases']
    targets={r['path'] for r in deltas+aliases}
    physical={r['base_path'] for r in deltas}|{r['delta_path'] for r in deltas}
    physical|={r['storage_path'] for r in aliases if r['storage_path'] not in targets}
    assert all(r['base_path'] not in targets for r in deltas)
    for name in sorted(physical):
        source=TREE/name;target=fresh/name;target.parent.mkdir(parents=True,exist_ok=True)
        os.link(source,target)
    cli=fresh/'code/materialize_archive_files.py';cli.write_bytes((TREE/'code/materialize_archive_files.py').read_bytes())
    executions=[]
    for phase,args in [('restore',[]),('verify',['--verify-only'])]:
        run=subprocess.run([sys.executable,str(cli),*args],capture_output=True)
        (HERE/('delta229_'+phase+'.out')).write_bytes(run.stdout)
        (HERE/('delta229_'+phase+'.err')).write_bytes(run.stderr)
        assert run.returncode==0 and run.stderr==b'',run.stderr.decode()
        result=json.loads(run.stdout);assert result['status']=='PASS'
        executions.append({'phase':phase,'exit_code':run.returncode,
                           'stdout_sha256':sha(run.stdout),'stderr_sha256':sha(run.stderr),
                           'result':result})
    records=[]
    for name in sorted(targets|physical):
        actual=(fresh/name).read_bytes();original=(TREE/name).read_bytes()
        assert actual==original,name
        records.append({'path':name,'bytes':len(actual),'sha256':sha(actual)})

    # Each negative fixture has a separately created tiny byte-level example.
    # Its independent XOR encoder uses individual bytes, not the integer decoder.
    negative=HERE/'negative_delta229';assert not negative.exists();negative.mkdir()
    base=b'base\x00\xfforiginal';target=b'complete target\x00\x01\x02\xffbytes'
    delta=bytes(v^base[i%len(base)] for i,v in enumerate(target))
    valid={'path':'code/result.bin','base_path':'code/base.bin',
           'bytes':len(target),'sha256':sha(target),'base_bytes':len(base),
           'base_sha256':sha(base),'delta_bytes':len(delta),'delta_sha256':sha(delta),
           'delta_path':'archive_data/binary_deltas/'+sha(delta)+'.xor',
           'encoding':'xor-repeated-base-v1'}
    checked=[]
    cases=['bad_base_hash','bad_delta_hash','bad_target_hash','bad_target_size',
           'absolute_base','absolute_target','absolute_delta','parent_escape',
           'base_symlink','target_symlink','delta_symlink','parent_symlink',
           'delta_chain','nonmatching_target','verify_missing','delta_filename_mismatch']
    for case in cases:
        root=negative/case;root.mkdir();(root/'code').mkdir();(root/'ledger').mkdir()
        row=copy.deepcopy(valid);(root/'code/base.bin').write_bytes(base)
        dp=root/row['delta_path'];dp.parent.mkdir(parents=True);dp.write_bytes(delta)
        if case=='bad_base_hash':row['base_sha256']='0'*64
        elif case=='bad_delta_hash':dp.write_bytes(bytes([delta[0]^1])+delta[1:])
        elif case=='bad_target_hash':row['sha256']='0'*64
        elif case=='bad_target_size':row['bytes']+=1
        elif case=='absolute_base':row['base_path']=str(root/'code/base.bin')
        elif case=='absolute_target':row['path']=str(root/'code/result.bin')
        elif case=='absolute_delta':row['delta_path']=str(dp)
        elif case=='parent_escape':row['path']='code/../escaped.bin'
        elif case=='base_symlink':
            (root/'code/source.bin').write_bytes(base);(root/'code/base.bin').unlink()
            (root/'code/base.bin').symlink_to('source.bin')
        elif case=='target_symlink':(root/'code/result.bin').symlink_to('base.bin')
        elif case=='delta_symlink':
            (root/'delta.bin').write_bytes(delta);dp.unlink();dp.symlink_to(root/'delta.bin')
        elif case=='parent_symlink':
            (root/'code/link').symlink_to(root/'code',target_is_directory=True)
            row['path']='code/link/result.bin'
        elif case=='delta_chain':row['base_path']=row['path']
        elif case=='nonmatching_target':(root/'code/result.bin').write_bytes(b'preserve existing bytes')
        elif case=='delta_filename_mismatch':
            new=dp.with_name('0'*64+'.xor');dp.rename(new);row['delta_path']=str(new.relative_to(root))
        plan={'format_version':1,'encoding':'xor-repeated-base-v1','deltas':[row]}
        (root/'ledger/archive_binary_deltas.json').write_text(json.dumps(plan))
        try:m.materialize(root,case=='verify_missing')
        except AssertionError as exc:
            checked.append({'case':case,'rejected':True,'exception':str(exc)})
        else:raise AssertionError('Negative fixture accepted: '+case)
        if case=='nonmatching_target':assert (root/'code/result.bin').read_bytes()==b'preserve existing bytes'
        assert (root/'code/base.bin').read_bytes()==base
    result={'status':'PASS','delta_count':len(deltas),'alias_count':len(aliases),
            'whole_original_files_compared':len(records),
            'complete_original_bytes_compared':sum(r['bytes'] for r in records),
            'all_whole_byte_equal':True,'executions':executions,
            'negative_fixture_count':len(checked),'negative_fixtures':checked,
            'source_sha256':sha((TREE/'code/materialize_archive_files.py').read_bytes()),
            'manifest_sha256':{name:sha((TREE/'ledger'/name).read_bytes()) for name in plans},
            'files':records,'elapsed_seconds':time.monotonic()-started}
    (HERE/'delta229_roundtrip.json').write_text(json.dumps(result,indent=2)+'\n')
    # All restored bytes are retained in TREE and were compared in full above.
    shutil.rmtree(fresh)
    print(json.dumps({k:v for k,v in result.items() if k not in {'files','negative_fixtures','manifest_sha256'}},indent=2))

if __name__=='__main__':main()
