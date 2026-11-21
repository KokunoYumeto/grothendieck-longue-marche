"""Exact delta projection: only two already-read codec comment spans are references."""
from pathlib import Path
import hashlib,json
B=Path('/workspace/scratch/94548b74fbe0');O=B/'out/checks'
sha=lambda x:hashlib.sha256(x).hexdigest()
def save(name,raw):
 p=O/name
 if p.exists():assert p.read_bytes()==raw
 else:p.write_bytes(raw)
 return {'path':str(p.relative_to(B)),'bytes':len(raw),'sha256':sha(raw)}
original_path=O/'scan026_source_sections13_19_delta_v01.diff'
original=original_path.read_bytes();projection=original;refs=[]
for kind in ['diagram96','pair16']:
 p=O/f'scan026_source_{kind}_comments_v01.txt';raw=p.read_bytes()
 block=b''.join(b'+'+line for line in raw.splitlines(keepends=True))
 assert projection.count(block)==1
 marker=('@@EXACT-PLUS-COMMENT-BLOCK '+kind+' SHA256='+sha(raw)+'@@\n').encode()
 assert marker not in projection
 at=projection.index(block)
 refs.append({'marker_utf8':marker.decode(),'source_path':str(p.relative_to(B)),
  'source_sha256':sha(raw),'source_bytes':len(raw),
  'exact_forward_map':'Prefix one ASCII + to each source line, preserving every source byte and line ending.',
  'prefixed_block_sha256':sha(block),'prefixed_block_bytes':len(block),
  'projected_replacement_char_start_at_step':len(projection[:at].decode())})
 projection=projection[:at]+marker+projection[at+len(block):]
replayed=projection
for ref in refs:
 raw=(B/ref['source_path']).read_bytes();assert sha(raw)==ref['source_sha256']
 block=b''.join(b'+'+line for line in raw.splitlines(keepends=True))
 assert sha(block)==ref['prefixed_block_sha256']
 marker=ref['marker_utf8'].encode();assert replayed.count(marker)==1
 replayed=replayed.replace(marker,block,1)
assert replayed==original
forward=replayed
for ref in refs:
 raw=(B/ref['source_path']).read_bytes();block=b''.join(b'+'+line for line in raw.splitlines(keepends=True))
 assert forward.count(block)==1;forward=forward.replace(block,ref['marker_utf8'].encode(),1)
assert forward==projection
projection_artifact=save('scan026_source_sections13_19_delta_review_v01.diff',projection)
chunks=[];current=[];size=0;line_start=1;line_number=0
def flush(lines,start,end):
 raw=b''.join(lines);record=save(f'scan026_source_sections13_19_delta_review_v01_{len(chunks)+1:02d}.txt',raw)
 record.update({'projection_line_start':start,'projection_line_end_inclusive':end});chunks.append(record)
for line in projection.splitlines(keepends=True):
 if current and size+len(line)>8500:
  flush(current,line_start,line_number);current=[];size=0;line_start=line_number+1
 current.append(line);size+=len(line);line_number+=1
if current:flush(current,line_start,line_number)
assert b''.join((B/r['path']).read_bytes() for r in chunks)==projection
manifest={'scope':'Full unaltered source delta with only the two exact previously read comment files replaced by references. Every other delta byte is displayed unchanged.',
 'source_delta_path':str(original_path.relative_to(B)),'source_delta_sha256':sha(original),
 'projection':projection_artifact,'references':refs,'read_chunks_in_order':chunks,
 'projection_concat_exact':True,'forward_exact':True,'inverse_reinsertion_exact':True,
 'whole_line_preservation':True,'maximum_chunk_bytes':max(r['bytes'] for r in chunks),
 'all_unreferenced_delta_bytes_preserved':True,'root_or_reader_files_changed':0}
save('scan026_source_sections13_19_review_manifest_v01.json',(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode())
print(json.dumps(manifest,ensure_ascii=False,indent=2))
