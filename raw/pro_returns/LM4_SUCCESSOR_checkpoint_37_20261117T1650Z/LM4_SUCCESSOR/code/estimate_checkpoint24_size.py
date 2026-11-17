"""Conservative current-workspace size estimate; no ZIP is created."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
import zipfile
import zlib
from checkpoint_standard_tar import build_standard_tar

root = Path(__file__).resolve().parents[1]
archive = root.parent/'LM4_SUCCESSOR_checkpoint_23.zip'
prefix = 'LM4_SUCCESSOR/'
digest = lambda data: hashlib.sha256(data).hexdigest()

def included(f):
    r = str(f.relative_to(root))
    if r in {'verification_images.tar', 'historical_documents.tar'}: return False
    if r.startswith('tex_cache/'): return False
    if r.startswith('work_CE/') and f.parent == root/'work_CE' and (f.name.startswith('D_') or f.name.startswith('LM6_')): return False
    if r.startswith('work_DE/') and f.name.endswith('_source.txt'): return False
    if f.name.endswith('_check.pdf') or f.name in ['DE_review.pdf', 'B_separability_review.pdf', 'B81_review.pdf', 'B82_review.pdf']: return False
    if 'work_CE/sources/' in r and f.suffix.lower() in ['.pdf', '.txt']: return False
    if r.startswith('work_DE/') and not f.with_suffix('.tex').exists() and (f.suffix.lower() == '.pdf' or (f.suffix.lower() == '.txt' and f.with_suffix('.pdf').exists() and f.stem not in ['DE_review', 'B_separability_review'])): return False
    if '__pycache__' in f.parts or f.suffix in ['.aux', '.toc', '.blg', '.bbl']: return False
    return True

def compressed_size(data, method):
    if method == 'deflate':
        c = zlib.compressobj(6, zlib.DEFLATED, -15)
    else:
        c = zipfile.LZMACompressor()
    return len(c.compress(data)+c.flush())

with zipfile.ZipFile(archive) as z:
    rows = list(csv.DictReader(io.StringIO(z.read(prefix+'records/checkpoint_23_contents_sha256.tsv').decode()), delimiter='\t'))
    old = {r['path']: r for r in rows}
    old_png = {(int(r['bytes']), r['sha256']) for r in rows if r['path'].lower().endswith('.png')}
    prior_pdfs = {i.filename[len(prefix):]: z.read(i) for i in z.infolist() if i.filename.lower().endswith('.pdf')}
    previous_pdf_compressed = sum(i.compress_size for i in z.infolist() if i.filename.lower().endswith('.pdf') and i.filename != prefix+'LM4_SUCCESSOR_paper.pdf')

documents = {}
new_files = []
png_seen = set(old_png)
new_png_count = 0
for f in sorted(root.rglob('*')):
    if not f.is_file() or not included(f): continue
    rel = str(f.relative_to(root))
    data = f.read_bytes()
    sha = digest(data)
    if f.suffix.lower() == '.pdf' and rel != 'LM4_SUCCESSOR_paper.pdf':
        documents[rel] = data
        continue
    previous = old.get(rel)
    if previous and sha == previous['sha256'] and len(data) == int(previous['bytes']): continue
    if f.suffix.lower() == '.png':
        key = (len(data), sha)
        if key in png_seen: continue
        png_seen.add(key)
        new_png_count += 1
        method = 'deflate'
    else:
        method = 'deflate' if f.suffix.lower() in {'.pdf','.jpg','.jpeg','.gif','.zip','.gz','.xz','.tar'} else 'lzma'
    new_files.append((compressed_size(data, method), rel))

# Preserve each checkpoint23 PDF even if its active path has since changed.
# All earlier retained histories already appear in that archive or workspace.
for rel, data in prior_pdfs.items():
    active = root/rel
    if active.is_file() and active.read_bytes() == data and rel != 'LM4_SUCCESSOR_paper.pdf':
        documents[rel] = data
    else:
        history = 'checkpoint_history/checkpoint_23/'+rel
        if history in documents: assert documents[history] == data
        documents[history] = data

bundle, metrics = build_standard_tar(list(documents.items()))
bundle_compressed = compressed_size(bundle, 'lzma')
added = sum(n for n, _ in new_files)
estimate = archive.stat().st_size - previous_pdf_compressed + bundle_compressed + added
allowance = 5_000_000
report = {
    'recorded_at': datetime.now(timezone.utc).isoformat(),
    'baseline_archive': archive.name, 'baseline_bytes': archive.stat().st_size,
    'previous_historical_pdf_compressed_bytes_removed': previous_pdf_compressed,
    'prospective_document_bundle': metrics,
    'prospective_document_bundle_compressed_bytes': bundle_compressed,
    'new_unique_pngs': new_png_count,
    'new_or_changed_nonbundled_files': len(new_files),
    'additional_compressed_payload_bytes': added,
    'estimated_before_allowance': estimate,
    'header_manifest_retention_and_late_text_allowance_bytes': allowance,
    'estimated_total_with_allowance': estimate+allowance,
    'delivery_cap_bytes': 536870912,
    'estimated_headroom_bytes': 536870912-estimate-allowance,
    'largest_new_compressed_payloads': sorted(new_files, reverse=True)[:15],
    'creates_zip': False,
    'scope': 'Conservative non-capture estimate from actual checkpoint23 and current included files. Changed non-PDF originals remain in the baseline while their new versions are added. Previous main PDF remains conservatively counted in the baseline as well as its prospective document history. Five MB covers headers, enlarged retention records and subsequent text. Actual size is verified after scheduled immutable capture.'
}
(root/'records/checkpoint24_size_estimate.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
assert estimate+allowance < 536870912
