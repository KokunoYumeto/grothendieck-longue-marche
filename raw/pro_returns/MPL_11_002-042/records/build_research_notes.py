#!/usr/bin/env python3
"""Assemble research notes without writing any frozen transcription artifact."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / 'records'

def read(name):
    return (R / name).read_text(encoding='utf-8')

def shift_headings(text, by=1):
    return re.sub(r'^(#{1,5}) ', lambda m: '#' * (len(m.group(1)) + by) + ' ', text, flags=re.M)

def entry_values(name):
    return json.loads(read(name))

def text_value(v):
    if v is None:
        return ''
    if isinstance(v, str):
        return v
    if isinstance(v, list):
        parts = []
        for x in v:
            if isinstance(x, dict):
                if 'id' in x:
                    parts.append('`' + x['id'] + '` — ' + x.get('status', '') + ('; ' + x['detail'] if x.get('detail') else ''))
                elif 'file' in x:
                    s = '`' + x['file'] + '`'
                    if x.get('cote'): s += ', cote ' + str(x['cote'])
                    if x.get('scan'): s += ', scan ' + str(x['scan'])
                    if x.get('lines'): s += ', lines ' + str(x['lines'])
                    if x.get('detail'): s += ' — ' + x['detail']
                    parts.append(s)
                else:
                    parts.append(json.dumps(x, ensure_ascii=False))
            else:
                parts.append(str(x))
        return '; '.join(parts)
    return str(v)

KINDS = {
    'RT01': 'unproved claim; external proof reference',
    'RT02': 'unproved claim; announced later construction',
    'RT03': 'self-flagged: a verification left as an exercise',
    'RT04': 'conjecture attributed to Tits; abbreviated proofs',
    'RT05': 'reading question; own idea',
    'RT06': 'unproved claim in an incomplete selected proof sequence',
    'RT07': 'unproved claim; external attribution',
    'RT08': 'unproved claim',
    'RT09': 'reading question: unfinished reference',
    'RT10': 'reading question: local cancellation and continuation',
    'RT11': 'unproved claim taken up in the same selected text',
    'RT12': 'unpursued implication; external proof reference',
    'RT13': 'unproved claim; announced section goal',
    'RT14': 'unproved claim with a visible proof, followed by a further programme',
    'RT15': 'unproved claim in an unfinished selected excerpt',
    'MB13': 'reading question; cross-source scope comparison',
}

SHORT_QUOTES = {
    'RT01': r'(cf. Chapter 1, §2)',
    'RT02': 'so-called arithmetic schemes of moduli of abelian varieties',
    'RT03': 'it is an exercise in elementary calculus to check',
    'RT04': 'according to a conjecture of Tits',
    'RT05': r'for every subset $S\unsure{\subset}X_k$',
    'RT06': 'we must show that the lines joining them',
    'RT07': 'Tits has shown',
    'RT08': 'it can be shown',
    'RT09': r'(cf.\ \hspace{2cm})',
    'RT10': r'\deleted{$\unsure{\Rightarrow}$}\inserted{with}',
    'RT11': r'then I claim $\mathcal U=X$.',
    'RT12': r'SGA 8, \S1',
    'RT13': 'The purpose of this section is to show',
    'RT14': r'Thirdly, we will prove that $2)\Rightarrow3)$.',
    'RT15': 'Then it is easy to see that:',
}

def render_entry(e):
    eid = e['id']
    scans = ', '.join(e['scans']) if isinstance(e['scans'], list) else e['scans']
    title = (' — ' + e['title']) if e.get('title') else ''
    out = [f'### {eid}{title}', '', f"**Source:** `11.pdf`, cote 11, scan(s) {scans}; frozen text in `MPL_11_002-042_transcription.tex` and the matching `pages/` fragments. **Kind:** {KINDS.get(eid, e['kind'])}."]
    if e.get('witness'):
        out += ['', '**Exact locator:** ' + e['witness']]
    quote = SHORT_QUOTES.get(eid, e['quote'])
    # These are brief anchors from the frozen witness, not normalized readings.
    out += ['', '**Witness anchor:** `' + quote.replace('`', '').replace('\n', ' ') + '`', '', e['body'], '']
    if e.get('confidence'):
        out += ['**Confidence and reason:** ' + text_value(e['confidence']), '']
    out += ['**Context search:** `' + e['query'].replace('`','') + '`. **Located context:** ' + text_value(e['context']) + '.', '', '**Relation:** ' + text_value(e['relation']) + '. **Results-state:** ' + text_value(e['ledger']) + '.', '']
    return '\n'.join(out)

def extract_tables():
    src = read('typed_standing_tables.md')
    blocks = []
    current = []
    for line in src.splitlines():
        if line.startswith('|'):
            current.append(line)
        elif current:
            blocks.append('\n'.join(current))
            current = []
    if current: blocks.append('\n'.join(current))
    assert len(blocks) == 2, f'Unexpected typed-table count: {len(blocks)}'
    titles = next(x for x in blocks if 'Exact internal header' in x)
    flags = next(x for x in blocks if x != titles)
    flags = flags.replace(r'4.6:13|4.6.13', r'4.6:13\|4.6.13')
    return titles, flags

def main():
    h = entry_values('root_research_entries.json')
    m = entry_values('motivic_research_entries.json')
    c = entry_values('lettering_research_entries.json')
    t = entry_values('typed_research_entries.json')
    all_entries = h+m+c+t
    ids = [e['id'] for e in all_entries]
    assert len(ids) == len(set(ids)) == 64
    parts = [read('notes_frontmatter.md')]
    parts += ['## Question 1 — the draft and printed conjecture letters\n', shift_headings(read('lettering_answer.md'), 1)]
    parts += ['## Question 2 — the correspondence category and cote 16\n',
              'The source writes the kernel category and its realization, while cote 16 specifies the additional map `Φ→E` with chosen Lefschetz and projector images. The comparison is therefore made by the following explicit maps and by the source locators in MB01–MB12; the selected cote-11 pages supply no written completion of that construction to a category of motives. O01 supplies a complete two-dimensional calculation of the realization and of the n=1 image of `Φ`, and MB09 gives the exact inclusion into the cited Chow-motive construction.\n',
              shift_headings(read('motivic_maps_appendix.md'), 1)]
    groups = [
        ('Handwritten questions, claims and retractions', [e for e in h if e['id'].startswith('H')]),
        ('Connections to cote 16 and the motivic programme', m),
        ('Lettering comparison: itemized evidence', c),
        ('Reading questions arising after the freeze', [e for e in h if e['id'].startswith('RQ')]),
        ('Explicit editorial calculations and further comparisons', [e for e in h if e['id'].startswith('O')]),
        ('Reused typed sheets: claims, gaps and continuations', t),
    ]
    for heading, entries in groups:
        parts += ['## ' + heading + '\n', '\n'.join(render_entry(e) for e in entries)]
    titles, flags = extract_tables()
    standing = read('handwritten_standing_sections.md').replace('<!-- TYPED_FLAGS -->', flags).replace('<!-- TYPED_TITLES -->', titles)
    parts += [standing, read('notes_sources_and_status.md')]
    result = '\n\n'.join(parts).rstrip() + '\n'
    result = result.replace('## Operational comparison of the A–D letters\n\n','').replace('## Supplement: explicit correspondence maps and completion data\n\n','')
    target = ROOT / 'MPL_11_002-042_notes.md'
    target.write_text(result, encoding='utf-8')
    (R/'assembled_research_entry_manifest.json').write_text(json.dumps({'count':len(ids),'ordered_ids':[e['id'] for _,es in groups for e in es],'source_files':['root_research_entries.json','motivic_research_entries.json','lettering_research_entries.json','typed_research_entries.json']},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'notes':str(target),'bytes':target.stat().st_size,'words':len(result.split()),'entries':len(ids)},ensure_ascii=False))

if __name__ == '__main__':
    main()
