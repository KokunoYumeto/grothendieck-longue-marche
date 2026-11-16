#!/usr/bin/env python3
"""Prepare/render CP16 QA from live PDF anchors, never historical page numbers.

Run only after the parent confirms the final PDF. --plan-only resolves anchors
and writes the manifest without rendering. The script does not certify review.
"""
from pathlib import Path
import argparse, hashlib, json, re
import fitz
from PIL import Image, ImageDraw

W = Path(__file__).resolve().parents[1]
PDF = W / 'SECTIONS_OVER_Q_paper.pdf'
QA = W / 'qa/hour16'

def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)

def repairs():
    # Hour 7 records the amounts but lacks equation-level structured fields.
    result = [
        dict(hour=7, points=27.17383, anchor='A.103.1', source='sections/norm_permitted_unit_obstruction.tex'),
        dict(hour=7, points=48.88760, anchor='A.108.7', source='sections/harmonic_jacobian_descent.tex'),
        dict(hour=7, points=4.97246, anchor='A.109.11', source='sections/norm_torus_selmer_agent.tex'),
    ]
    for hour in range(8, 17):
        path = W / f'notes/hour{hour}_typesetting_corrections.json'
        for row in walk(json.loads(path.read_text())):
            amount = row.get('before_hbox_pt', row.get('points', row.get('maximum_pt', 0)))
            special = hour == 16 and 'ninth_root_subfield_unit_certificate.py' in row.get('anchor', '')
            if not isinstance(amount, (int, float)) or not (amount > 2 or special):
                continue
            anchor = row.get('anchor') or row.get('equation') or row.get('source', '')
            source = row.get('source', row.get('file', ''))
            found = re.search(r'A\.\d+\.(?:S)?\d+', anchor)
            if found:
                anchor = found.group()
            if 'A.150 certificate' in anchor:
                anchor = 'harmonic_prym_quotient_certificate.py'
                source = 'sections/harmonic_prym_selmer.tex'
            result.append(dict(hour=hour, points=amount, anchor=anchor, source=source,
                               minor_exception=special))
    unique = {(r['hour'], r['anchor']): r for r in result}
    return list(unique.values())

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--plan-only', action='store_true')
    args = ap.parse_args()
    doc = fitz.open(PDF)
    raw_texts = [page.get_text() for page in doc]
    texts = [' '.join(text.split()) for text in raw_texts]
    raw_lines = [[line.strip() for line in text.splitlines()] for text in raw_texts]
    compact = [re.sub(r'\s+', '', text) for text in texts]
    starts = {}
    for page, text in enumerate(texts, 1):
        for m in re.finditer(r'A\.(\d+)\.\s*\[(?:Proved|Refuted|Open|Known)\]', text):
            starts.setdefault(int(m.group(1)), page)
    missing = [n for n in range(193, 205) if n not in starts]
    if missing:
        raise RuntimeError(f'Final PDF lacks new statements {missing}; do not render an intermediate build.')
    def locate(anchor, number=None):
        # Restrict equation and prose anchors to their actual proof section.
        if number is None:
            match = re.search(r'A\.(\d+)', anchor)
            number = int(match.group(1)) if match else None
        lo = starts.get(number, 1)
        hi = starts.get(number + 1, len(doc)) if number else len(doc)
        key = re.sub(r'\s+', '', anchor)
        if re.fullmatch(r'A\.\d+\.(?:S)?\d+', anchor):
            # Match the standalone printed equation label, never a citation or
            # a prefix such as A.103.1 inside A.103.10.
            label = re.compile(r'^\(' + re.escape(anchor) + r'\)$')
            found = [i+1 for i, lines in enumerate(raw_lines)
                     if lo <= i+1 <= hi and any(label.fullmatch(line) for line in lines)]
        else:
            found = [i+1 for i, text in enumerate(compact)
                     if lo <= i+1 <= hi and key in text]
        if not found:
            raise RuntimeError(f'Unresolved live PDF anchor: {anchor!r}, section {number}')
        return found

    mapping = []
    for row in repairs():
        number = 150 if 'harmonic_prym_quotient_certificate' in row['anchor'] else (
                 194 if 'ninth_root_subfield_unit_certificate' in row['anchor'] else None)
        pages = locate(row['anchor'], number)
        if number == 150:
            # All three repaired path lines, even if the paragraph straddles pages.
            pages = sorted(set(pages + locate('harmonic_prym_dyadic_filter.py', 150)
                                      + locate('harmonic_prym_odd_filter.py', 150)))
        mapping.append(dict(row, pages=pages,
                            correction_record=f'notes/hour{row["hour"]}_typesetting_corrections.json'))
    assert sum(r['points'] > 2 for r in mapping) >= 16
    assert any(r.get('minor_exception') for r in mapping)

    start = starts[193]
    part_b = next(i+1 for i, text in enumerate(texts)
                  if i+1 >= starts[204] and 'Part B. Sections and valuations' in text)
    refs = next(i+1 for i, text in enumerate(texts)
                if i+1 > part_b and re.search(r'\bReferences\b', text))
    # Cover the complete current TOC, with adjoining front matter.
    toc = list(range(1, min(12, start-1)+1))
    new_pages = list(range(start, part_b+1))
    historical = sorted({p for row in mapping for p in row['pages']})
    # Earlier samples are supplementary; repaired locations are anchor-derived.
    samples = [20,38,54,69,82,104,128,145,161,178,195,212,229,246,
               263,283,299,305,317,325,347,351,365,377,395,410,422,
               437,447,465,470,488,504,525,540,555]
    samples += [max(1, round((start-1)*j/18)) for j in range(1,18)]
    new_full_tags = ['A.193.3','A.193.13','A.194.3','A.195.8','A.195.15',
                     'A.196.1','A.196.18','A.197.4','A.198.10','A.198.18',
                     'A.199.7','A.200.2','A.201.11','A.202.11','A.203.8',
                     'A.203.12','A.204.11','A.204.13']
    # Optional detailed anchors supplement every new statement's first page.
    equation_locations = {}
    for tag in new_full_tags:
        try:
            equation_locations[tag] = locate(tag)
        except RuntimeError:
            # Source equation numbering may evolve; all new proof pages remain included.
            equation_locations[tag] = []
    required_full = sorted(set(toc + historical + [starts[n] for n in range(193,205)]
                               + [p for ps in equation_locations.values() for p in ps]))
    pages = sorted(set(p for p in samples + required_full + new_pages
                       + [part_b+3,part_b+10,part_b+19,part_b+26]
                       + list(range(refs,len(doc)+1)) if 1 <= p <= len(doc)))
    QA.mkdir(parents=True, exist_ok=True)
    record = dict(pdf_pages=len(doc), pdf_sha256=hashlib.sha256(PDF.read_bytes()).hexdigest(),
                  rendered_pages=pages, new_result_pages=new_pages,
                  new_statement_pages={str(n):starts[n] for n in range(193,205)},
                  toc_pages=toc, equation_locations=equation_locations,
                  historical_repair_anchor_map=mapping, prior_overflow_pages=historical,
                  required_full_resolution_pages=required_full,
                  reference_pages=list(range(refs,len(doc)+1)), render_scale=1.35,
                  full_resolution_scale=2.0, contact_parts=[],
                  status='Anchor plan resolved; rendering and actual visual review pending.')
    lines = ['# CP16 live PDF repair anchor map', '',
             'All pages below are resolved from the current PDF text and actual statement bounds. No historical page number selects a repaired location.', '',
             '| Hour | Previous overflow (pt) | Source anchor | Current PDF page(s) |',
             '|---|---:|---|---|']
    for row in mapping:
        lines.append(f'| {row["hour"]} | {row["points"]} | {row["anchor"]} | '+', '.join(map(str,row['pages']))+' |')
    lines += ['', 'The A194 certificate paragraph is included despite its smaller recorded overflow. All listed repair pages and the complete front matter/TOC are required full-resolution review targets.',
              '', f'New proof pages: {start}–{part_b}; references: {refs}–{len(doc)}.',
              'This mapping does not certify visual review.']
    (W/'notes/hour16_render_anchor_map.md').write_text('\n'.join(lines)+'\n')
    if not args.plan_only:
        previous = W/'qa/visual_review.json'
        saved = W/'qa/visual_review_hour15.json'
        if previous.exists() and not saved.exists():
            saved.write_bytes(previous.read_bytes())
        paths = []
        for page in pages:
            path = QA/f'page_{page:03d}.png'
            doc[page-1].get_pixmap(matrix=fitz.Matrix(1.35,1.35),alpha=False).save(path)
            paths.append(path)
        full_dir = QA/'full'
        full_dir.mkdir(exist_ok=True)
        for page in required_full:
            doc[page-1].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(full_dir/f'page_{page:03d}.png')
        for number, offset in enumerate(range(0,len(pages),16),1):
            block = list(zip(pages[offset:offset+16], paths[offset:offset+16]))
            sheet = Image.new('RGB',(1720,640*((len(block)+3)//4)),'#e8e8e8')
            draw = ImageDraw.Draw(sheet)
            for j,(page,path) in enumerate(block):
                im = Image.open(path).convert('RGB'); im.thumbnail((414,604))
                left=(j%4)*430+(430-im.width)//2; top=(j//4)*640+26
                sheet.paste(im,(left,top))
                draw.text(((j%4)*430+10,(j//4)*640+8),f'Page {page}',fill='black')
            path=QA/f'contact_part_{number}.png'; sheet.save(path)
            record['contact_parts'].append(str(path.relative_to(W)))
        record['status']='Rendered; actual visual review pending.'
    out=json.dumps(record,indent=2)+'\n'
    for path in [QA/'render_record.json', W/'code/render_hour16_qa_output.txt']:
        path.write_text(out)
    if not args.plan_only:
        (W/'qa/render_record.json').write_text(out)
    print(out,end='')

if __name__ == '__main__':
    main()
