"""Measure exact reversible XOR storage for related binary transcripts.

For target bytes t of length n and nonempty reference bytes b, let r be
the length-n prefix of the repeated byte string bbb... . Store d=t XOR r.
The inverse is t=d XOR r, with n retained explicitly. Every candidate is
reconstructed and compared with the entire original byte string here.
"""
from pathlib import Path
from collections import defaultdict
import hashlib,io,json,time,zipfile

BASE=Path(__file__).resolve().parent;ROOT=BASE.parent;TREE=ROOT/'LM7_FERMAT_TOWER'
ZIP=ROOT/'LM7_FERMAT_TOWER.zip';OUT=BASE/'delta229_candidates'
sha=lambda b:hashlib.sha256(b).hexdigest()

def xor(data,reference):
    assert reference
    n=len(data);r=(reference*((n+len(reference)-1)//len(reference)))[:n]
    return (int.from_bytes(data,'little')^int.from_bytes(r,'little')).to_bytes(n,'little')

def zipped(data):
    stream=io.BytesIO()
    with zipfile.ZipFile(stream,'w') as z:z.writestr('delta',data,compress_type=zipfile.ZIP_LZMA)
    with zipfile.ZipFile(io.BytesIO(stream.getvalue())) as z:
        assert z.read('delta')==data
        return z.getinfo('delta').compress_size

def main():
    assert not OUT.exists();OUT.mkdir()
    start=time.monotonic();groups=defaultdict(list);rows=[]
    with zipfile.ZipFile(ZIP) as z:
        infos={i.filename.split('/',1)[1]:i for i in z.infolist()}
        for path,info in infos.items():
            if Path(path).suffix=='.bin' and info.file_size>=100000 and info.compress_size>=10000:
                groups[(Path(path).name,info.file_size)].append(path)
        pairs=[]
        for key,paths in sorted(groups.items()):
            paths.sort(key=lambda s:(len(Path(s).parts),len(s),s))
            if len(paths)>1:pairs.extend((p,paths[0]) for p in paths[1:])
        # The retained two-record PARI stream is compared as literal bytes
        # with the named single-record stream, without parsing any GEN.
        special='code/e123_bundle/audit/binary_reference_amendment/e53_positional_presentation_two_records.bin'
        base='code/e123_bundle/code/e53_positional_presentation.bin'
        assert special in infos and base in infos
        pairs.append((special,base))
        for target,base in pairs:
            data=(TREE/target).read_bytes();reference=(TREE/base).read_bytes()
            assert data==z.read(TREE.name+'/'+target)
            assert reference==z.read(TREE.name+'/'+base)
            delta=xor(data,reference)
            assert xor(delta,reference)==data
            size=zipped(delta);old=infos[target].compress_size
            row={'path':target,'base_path':base,'bytes':len(data),'sha256':sha(data),
                 'base_bytes':len(reference),'base_sha256':sha(reference),
                 'delta_sha256':sha(delta),'delta_bytes':len(delta),
                 'old_compressed_bytes':old,'delta_compressed_bytes':size,
                 'savings':old-size,'whole_target_roundtrip_equal':True,
                 'delta_codec_roundtrip_equal':True}
            if old-size>1024:
                p=OUT/(sha(delta)+'.xor');p.write_bytes(delta)
                row['delta_path']=str(p.relative_to(BASE))
            rows.append(row)
            print(json.dumps({k:row[k] for k in ['path','bytes','savings','whole_target_roundtrip_equal']}),flush=True)
    chosen=[r for r in rows if 'delta_path' in r]
    targets={r['path'] for r in chosen}
    assert not any(r['base_path'] in targets for r in chosen),'Delta chains are deliberately excluded'
    result={'status':'PASS','source_archive_sha256':sha(ZIP.read_bytes()),
            'source_archive_bytes':ZIP.stat().st_size,'candidates':len(rows),
            'selected_count':len(chosen),'selected_savings':sum(r['savings'] for r in chosen),
            'projected_archive_bytes':ZIP.stat().st_size-sum(r['savings'] for r in chosen),
            'all_whole_byte_roundtrips_passed':True,'delta_chains':False,
            'elapsed_seconds':time.monotonic()-start,'records':rows}
    (BASE/'delta229_benchmark.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
