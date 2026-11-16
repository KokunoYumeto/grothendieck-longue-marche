"""Extract visually verified printed pages from the retained GDZ volume.

Original source:
https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0217/PPN243919689_0217.pdf
The volume was downloaded on 2026-11-16. Printed page p has zero-based
PDF index p+4. The printed187 header and full adjointness proof were
checked visually after extraction; no OCR is needed for this extraction.
"""
from pathlib import Path
from pypdf import PdfReader, PdfWriter

base = Path(__file__).resolve().parents[1] / 'sources'
reader = PdfReader(base / 'cassels1965_volume217.pdf')
lines = []
for name, pages in [
    ('cassels1965_isogenies.pdf', range(180, 200)),
    ('cassels1965_isogeny_adjointness_extract.pdf', [181, 182, 183, 187, 188]),
]:
    writer = PdfWriter()
    for p in pages:
        writer.add_page(reader.pages[p+4])
    path = base / name
    with path.open('wb') as output:
        writer.write(output)
    lines.append(f'{name}: printed pages {list(pages)}, {path.stat().st_size} bytes')
text = '\n'.join(lines) + '\n'
(base.parent / 'code/extract_cassels1965_source_output.txt').write_text(text)
print(text, end='')
