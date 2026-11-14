#!/usr/bin/env python3
"""One isolated E63 replay, with complete or literal-certificate mode.

Complete mode repeats every new full presentation.  Literal mode checks
all saved independent words/matrices against the frozen complete outputs.
Both keep all original files immutable and compare exact arrays.
"""
from pathlib import Path
from hashlib import sha256
import argparse,json,re,shutil,subprocess,time
import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent


def mathematical(value):
    if isinstance(value,dict):
        return {k:mathematical(v) for k,v in value.items()
                if k not in {'seconds','total_seconds','input_sha256'}}
    if isinstance(value,list):return [mathematical(v) for v in value]
    return value


def verify_provenance(value,tree_root,context):
    """Validate every input hash before its containing map is disregarded.

    A bare filename routes to code/.  An explicit code/ or research/
    path retains that exact path.  An absolute original-workspace path
    is transported by its exact relative suffix.  No basename fallback
    is used for a missing explicitly routed path.
    """
    records=[]
    def walk(obj,pointer):
        if isinstance(obj,dict):
            for key,entry in obj.items():
                if key=='input_sha256':
                    assert isinstance(entry,dict),('untyped input provenance',context,pointer)
                    for name,expected in entry.items():
                        assert isinstance(expected,str) and re.fullmatch('[0-9a-f]{64}',expected),('invalid hash',context,name)
                        supplied=Path(name)
                        if supplied.is_absolute():relative=supplied.relative_to(ROOT)
                        elif len(supplied.parts)==1:relative=Path('code')/supplied
                        else:
                            assert supplied.parts[0] in {'code','research'},('unregistered provenance route',context,name)
                            relative=supplied
                        assert '..' not in relative.parts,('parent route forbidden',context,name)
                        actual=tree_root/relative
                        assert actual.is_file(),('missing routed hash input',context,name,str(actual))
                        observed=sha256(actual.read_bytes()).hexdigest()
                        assert observed==expected,('input hash mismatch',context,pointer,name,expected,observed)
                        records.append({'record':context,'json_pointer':pointer+'/input_sha256',
                                        'input':name,'actual_relative_path':str(relative),'sha256':observed})
                else:walk(entry,pointer+'/'+str(key))
        elif isinstance(obj,list):
            for i,entry in enumerate(obj):walk(entry,pointer+'/'+str(i))
    walk(value,'');return records


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--mode',choices=('complete','literal'),default='complete')
    parser.add_argument('--destination',required=True)
    args=parser.parse_args();started=time.monotonic()
    dest=Path(args.destination)
    if not dest.is_absolute():dest=ROOT/dest
    assert not dest.exists(),('fresh isolated destination required',str(dest))
    manifest_path=HERE/'de_a6_double_source_manifest.json'
    manifest=json.loads(manifest_path.read_text())
    files={**manifest['records'],**manifest['documents']}
    for name,record in files.items():
        assert sha256((ROOT/name).read_bytes()).hexdigest()==record['sha256'],('frozen input mismatch',name)
        target=dest/name;target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(ROOT/name,target)
    code=dest/'code';rows=[]
    report={'status':'RUNNING','mode':args.mode,
            'manifest_sha256':sha256(manifest_path.read_bytes()).hexdigest(),
            'protected_original_count':len(files),'steps':rows,
            'verified_input_provenance':[]}
    def save():
        (dest/'replay.json').write_text(json.dumps(report,indent=2)+'\n')
    def compare(name):
        original=HERE/name;actual=code/name
        assert actual.exists() and original.exists(),('missing comparison output',name)
        if actual.suffix=='.npz':
            a,b=np.load(actual),np.load(original)
            assert set(a.files)==set(b.files),('NPZ keys',name)
            for key in a.files:
                assert a[key].shape==b[key].shape and a[key].dtype==b[key].dtype,('NPZ type',name,key)
                assert np.array_equal(a[key],b[key]),('NPZ value',name,key)
        elif actual.suffix=='.json':
            new,old=json.loads(actual.read_text()),json.loads(original.read_text())
            # Validation uses the exact actual bytes in each separate
            # tree before these verified provenance maps are omitted.
            report['verified_input_provenance'].extend(verify_provenance(old,ROOT,'original:'+name))
            report['verified_input_provenance'].extend(verify_provenance(new,dest,'regenerated:'+name))
            assert mathematical(new)==mathematical(old),('JSON mathematics',name)
        else:assert actual.read_bytes()==original.read_bytes(),('byte output',name)
    def run(label,command,outputs=()):
        begin=time.monotonic();row={'label':label,'command':command,'status':'RUNNING'}
        rows.append(row);save();print(json.dumps(row),flush=True)
        with (dest/(label+'.out')).open('w') as out,(dest/(label+'.err')).open('w') as err:
            completed=subprocess.run(command,cwd=code,stdout=out,stderr=err)
        row['exit_code']=completed.returncode
        assert completed.returncode==0,('program failure',label)
        for name in outputs:compare(name)
        row.update(status='PASS',exact_outputs=list(outputs),seconds=round(time.monotonic()-begin,3))
        save();print(json.dumps(row),flush=True)
    try:
        run('compile_engine',['g++','-O3','-std=c++17','de_a6_schreier.cpp','-o','de_a6_schreier_fast'])
        run('candidate_small',['python','a_cm_signed_common_candidate.py'],
            ['a_cm_signed_common_candidate.json','a_cm_signed_common_candidate.npz'])
        for stem in ('B','F','Fprime','Fsecond','three_factors','F_typed_product'):
            compare('a_cm_signed_common_'+stem+'.bin')
        if args.mode=='complete':
            run('candidate_GL',['python','a_cm_signed_common_GL.py'],
                ['a_cm_signed_common_GL.json','a_cm_signed_common_GL.npz'])
        run('bridge_build',['python','de_a6_double_bridge_build.py'],
            ['de_a6_double_bridge_build.json','de_a6_double_bridge.cpp'])
        if args.mode=='complete':
            run('compile_bridge',['g++','-O3','-std=c++17','de_a6_double_bridge.cpp','-o','e63_bridge'])
            run('bridge_complete',['./e63_bridge','e_a6_double_kernel_model_root.bin',
                'e_a6_double_central_model_root.bin','de_a6_gl_central_model.bin',
                'de_a6_schreier_residual_derived.bin','de_a6_double_bridge.json'],['de_a6_double_bridge.json'])
        run('bridge_independent',['python','de_a6_double_bridge_replay.py'],
            ['de_a6_double_bridge_replay.json','de_a6_double_bridge_replay.npz'])
        run('signed_prepare',['python','de_a6_double_signed_prepare.py'],
            ['de_a6_double_signed_prepare.json','de_a6_double_signed_prepare.npz',
             'de_a6_double_signed_upper.bin','de_a6_double_signed_gl_core.hpp','de_a6_double_signed_lifted.hpp'])
        if args.mode=='complete':
            run('compile_signed',['g++','-O3','-std=c++17','de_a6_double_signed.cpp','-o','e63_signed'])
            run('signed_complete',['./e63_signed','e_a6_double_kernel_model_root.bin','de_a6_gl_model.bin',
                'de_a6_double_signed_upper.bin','de_a6_a5_common_source.bin','de_a6_double_signed.json'],
                ['de_a6_double_signed.json'])
        run('signed_independent',['python','de_a6_double_signed_replay.py'],
            ['de_a6_double_signed_replay.json','de_a6_double_signed_replay.npz'])
        run('candidate_prepare',['python','de_a6_double_candidate_prepare.py'],
            ['de_a6_double_candidate_prepare.json','de_a6_double_candidate_model.bin',
             'de_a6_double_candidate_lifted.hpp'])
        if args.mode=='complete':
            run('compile_candidate',['g++','-O3','-std=c++17','de_a6_double_candidate.cpp','-o','e63_candidate'])
            run('candidate_complete',['./e63_candidate','e_a6_double_kernel_model_root.bin',
                'de_a6_double_candidate_model.bin','de_a6_schreier_full_ordered.bin',
                'de_a6_double_candidate.json'],['de_a6_double_candidate.json'])
        run('candidate_independent',['python','de_a6_double_candidate_replay.py'],
            ['de_a6_double_candidate_replay.json','de_a6_double_candidate_replay.npz'])
        run('deep_words',['python','de_a6_double_deep_words.py'],
            ['de_a6_double_deep_words.json','de_a6_double_deep_words.npz'])
        run('target_old_maps',['python','e_a6_double_target_old_maps_root.py'],
            ['e_a6_double_target_old_maps_root.json'])
        run('target_independent',['python','e_a6_double_target_certificate_root.py'],
            ['e_a6_double_target_certificate_root.json','e_a6_double_target_certificate_root.npz'])
        run('target_both_covers',['python','e_a6_double_triple_target_root.py'],
            ['e_a6_double_triple_target_root.json'])
        assert all(sha256((ROOT/name).read_bytes()).hexdigest()==record['sha256'] for name,record in files.items())
        report.update(status='PASS_COMPLETE_ISOLATED_E63_REPLAY' if args.mode=='complete' else 'PASS_ISOLATED_E63_LITERAL_REPLAY',
                      all_originals_unchanged=True,seconds=round(time.monotonic()-started,3),
                      complete_new_relations_repeated=args.mode=='complete',
                      every_omitted_input_hash_independently_verified=True,
                      verified_input_hash_count=len(report['verified_input_provenance']),
                      root_previously_replayed_target_chains_used_unchanged=True)
        save();print(json.dumps({k:v for k,v in report.items() if k not in {'steps','verified_input_provenance'}},indent=2),flush=True)
    except BaseException as error:
        report.update(status='FAILED_PRESERVED_ISOLATED_REPLAY',failure=repr(error),
                      seconds=round(time.monotonic()-started,3))
        save();raise


if __name__=='__main__':main()
