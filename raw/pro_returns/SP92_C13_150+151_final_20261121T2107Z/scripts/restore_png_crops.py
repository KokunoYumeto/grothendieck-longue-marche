"""Restore crop pixels from a portable archive without rereading or recropping."""
from pathlib import Path
from PIL import Image
import csv,hashlib,json,re,subprocess

# These are the two observed JSON keys whose bare filename values identify
# files in W/crops. Other bare names, particularly historical display names,
# must not be rewritten merely because their basename matches a crop.
_BARE_CROP_KEYS=frozenset({'viewed_crops','crops_viewed'})
_QUALIFIED_CROP_REF=re.compile(r'(?<![A-Za-z0-9_.-])crops/([A-Za-z0-9_.+-]+)(?![/A-Za-z0-9_.+-])')


def rewrite_crop_references(text,mapping,*,is_json=False):
    """Rewrite live crops/ paths and explicitly identified bare JSON values.

    Non-crops paths, prose containing a bare filename, hash fields and unknown
    bare-name fields retain their original values. Qualified replacements keep
    the surrounding text bytes; JSON is serialized only when a whitelisted
    bare-name field actually changes.
    """
    def qualified(match):
        name=match.group(1)
        return 'crops/'+mapping.get(name,name)
    updated=_QUALIFIED_CROP_REF.sub(qualified,text)
    if not is_json:return updated
    document=json.loads(updated)
    bare_changed=False
    def visit(value,key=None):
        nonlocal bare_changed
        if isinstance(value,dict):
            return {k:visit(v,k) for k,v in value.items()}
        if isinstance(value,list):
            return [visit(v,key) for v in value]
        if isinstance(value,str) and key in _BARE_CROP_KEYS and value in mapping:
            replacement=mapping[value]
            bare_changed=bare_changed or replacement!=value
            return replacement
        return value
    document=visit(document)
    if not bare_changed:return updated
    return json.dumps(document,ensure_ascii=False,indent=2)+('\n' if updated.endswith('\n') else '')


def verify_jxl_dimensions(path,expected_size):
    """Check encoded geometry independently of the flattened RGB buffer."""
    result=subprocess.run(
        ['ffprobe','-v','error','-select_streams','v:0',
         '-show_entries','stream=width,height','-of','json',str(path)],
        check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    streams=json.loads(result.stdout).get('streams',[])
    if len(streams)!=1:
        raise ValueError(f'Expected one image stream in {path}, found {len(streams)}')
    try:actual=(int(streams[0]['width']),int(streams[0]['height']))
    except (KeyError,TypeError,ValueError) as exc:
        raise ValueError(f'Missing or invalid image dimensions in {path}') from exc
    if actual!=tuple(expected_size):
        raise ValueError(f'JPEG XL dimensions differ for {path}: {actual} != {tuple(expected_size)}')
    return actual


def main():
    W=Path(__file__).resolve().parents[1]
    rows=list(csv.DictReader((W/'CROP_ENCODING.tsv').open(encoding='utf-8'),delimiter='\t'))
    mapping={}
    for r in rows:
        p=W/r['stored']
        assert hashlib.sha256(p.read_bytes()).hexdigest()==r['stored_file_sha256']
        expected_size=(int(r['width']),int(r['height']))
        if p.suffix=='.jxl':
            assert r['mode']=='RGB'
            verify_jxl_dimensions(p,expected_size)
            raw=subprocess.run(['ffmpeg','-v','error','-threads','2','-i',str(p),'-f','rawvideo','-pix_fmt','rgb24','pipe:1'],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout
            im=Image.frombytes('RGB',expected_size,raw)
        else:im=Image.open(p).convert(r['mode'])
        assert im.size==expected_size
        assert hashlib.sha256(im.tobytes()).hexdigest()==r['pixel_sha256']
        target=W/r['original']
        if not target.exists():im.save(target,format='PNG')
        test=Image.open(target).convert(r['mode'])
        assert test.size==expected_size
        assert hashlib.sha256(test.tobytes()).hexdigest()==r['pixel_sha256']
        mapping[Path(r['stored']).name]=Path(r['original']).name
    frozen={'first_reading_hashes.tsv','TRANSCRIPTION_SHA256.tsv','CROP_ENCODING.tsv','CROP_ENCODING.md'}
    for p in W.rglob('*'):
        if not p.is_file() or p.name in frozen or p.suffix not in {'.json','.md','.tsv','.csv','.log','.txt','.py','.tex'}:continue
        if p.relative_to(W).parts[0]=='pages' or p.name.endswith(('_transcription.tex','_first.tsv','_second.tsv','_boxes.tsv')):continue
        old=p.read_bytes().decode('utf-8')
        new=rewrite_crop_references(old,mapping,is_json=p.suffix=='.json')
        if old!=new:p.write_bytes(new.encode('utf-8'))
    print(f'Restored and verified {len(rows)} original crop pixel arrays; no readings changed.')


if __name__=='__main__':main()
