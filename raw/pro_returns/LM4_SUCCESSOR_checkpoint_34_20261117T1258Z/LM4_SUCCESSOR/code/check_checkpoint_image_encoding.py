"""Exercise actual PNG hard links through the reader and standard tar restore."""
from pathlib import Path
import tarfile,zipfile,io,tempfile,subprocess,json
from checkpoint_archive_io import CheckpointReader,IMAGE_BUNDLE
root=Path(__file__).resolve().parents[1]
images=sorted(root.glob('records/pdf_qa/checkpoint19_final/page-*.png'))[:2]
assert len(images)==2
expected={'LM4_SUCCESSOR/a.png':images[0].read_bytes(),
          'LM4_SUCCESSOR/sub/b.png':images[0].read_bytes(),
          'LM4_SUCCESSOR/c.png':images[1].read_bytes(),
          'LM4_SUCCESSOR/test.txt':b'actual fixture\n'}
with tempfile.TemporaryDirectory(prefix='lm4-image-encoding-') as temp:
 p=Path(temp);stream=io.BytesIO()
 with tarfile.open(fileobj=stream,mode='w') as tf:
  for name in ['LM4_SUCCESSOR/a.png','LM4_SUCCESSOR/sub/b.png','LM4_SUCCESSOR/c.png']:
   item=tarfile.TarInfo(name)
   if name.endswith('/b.png'):
    item.type=tarfile.LNKTYPE;item.linkname='LM4_SUCCESSOR/a.png';tf.addfile(item)
   else:
    item.size=len(expected[name]);tf.addfile(item,io.BytesIO(expected[name]))
 with zipfile.ZipFile(p/'fixture.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
  z.writestr(IMAGE_BUNDLE,stream.getvalue())
  z.writestr('LM4_SUCCESSOR/test.txt',expected['LM4_SUCCESSOR/test.txt'])
 with CheckpointReader(p/'fixture.zip') as z:
  assert set(z.names())==set(expected)
  assert all(z.read(n)==d for n,d in expected.items())
  assert z.testzip() is None
 # The system TAR extraction is independent of the helper's member reader.
 with zipfile.ZipFile(p/'fixture.zip') as z:z.extractall(p/'restore')
 subprocess.run(['tar','-xf',str(p/'restore'/IMAGE_BUNDLE)],cwd=p/'restore',check=True)
 assert all((p/'restore'/n).read_bytes()==d for n,d in expected.items())
 report={'helper_logical_file_check':'PASS','standard_system_tar_restore':'PASS',
         'fixture_paths':list(expected),'identical_png_hardlink':'PASS',
         'scope':'Reader/standard extraction fixture; complete checkpoint20 manifest and retention audit will run against the captured actual archive.'}
 (root/'records/checkpoint20_packaging_fixture.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps(report,indent=2))
