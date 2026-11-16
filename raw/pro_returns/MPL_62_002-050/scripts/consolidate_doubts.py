#!/usr/bin/env python3
"""Mechanically assemble primary-reader records; do not interpret scans or change pages."""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path
import re

PACKAGE='MPL_62_002-050'

def cell(value):
    return str(value if value is not None else '').replace('|',r'\|').replace('\r','').replace('\n','<br>')

def notation_rows(text):
    rows=[];scan='General';block=[]
    def flush():
        if block:
            rows.append((scan,'\n'.join(block).strip()))
            block.clear()
    for line in text.splitlines():
        m=re.match(r'^##\s+(.+)$',line)
        if m:
            flush();scan=m.group(1)
        elif line.startswith('# '):
            continue
        elif not line.strip():
            flush()
        elif line.startswith('- '):
            flush();block.append(line[2:])
        else:
            block.append(line)
    flush()
    return rows

def assemble(root):
    source=root/'records/doubts.jsonl'
    entries=[]
    for number,line in enumerate(source.read_text(encoding='utf-8').splitlines(),1):
        if line.strip():
            record=json.loads(line)
            required={'cote','scan','line','reading','alternatives','confidence'}
            if not required.issubset(record):
                raise ValueError(f'doubts.jsonl line {number}: missing fields {required-set(record)}')
            if record['confidence'] not in {'high','medium','low'}:
                raise ValueError(f'doubts.jsonl line {number}: unrecognized confidence')
            entries.append((number,record))
    # Stable sorting retains the primary reader's within-page order.
    entries.sort(key=lambda pair:(int(pair[1]['cote']),int(pair[1]['scan']),pair[0]))
    notation=(root/'records/notation.md').read_text(encoding='utf-8')
    generated=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    counts=Counter(r['confidence'] for _,r in entries)
    out=[f'# {PACKAGE}: Notation and doubts', '',
         '## Notation table', '',
         'The primary reader’s observations from `records/notation.md` are reproduced below without interpreting or normalizing their readings. Only the section-and-paragraph layout has been converted to table rows. Provisional language in that source is retained for the final cross-page audit.', '',
         '| Source section | Primary reader’s notation observation |',
         '|---|---|']
    out.extend('| '+cell(scan)+' | '+cell(content)+' |' for scan,content in notation_rows(notation))
    out += ['', '## Consolidated doubt register', '',
            f'Mechanically assembled at {generated} from {len(entries)} primary-reader records. Every JSONL record is included, with its original confidence and alternatives. Approximate line labels are retained as recorded; they are not newly inferred line numbers.', '',
            '| File | Scan page | Approximate line or location | Reading | Alternatives or qualification | Confidence |',
            '|---|---:|---|---|---|---|']
    for _,r in entries:
        values=[str(r['cote'])+'.pdf',f"{int(r['scan']):03d}",r['line'],r['reading'],r['alternatives'] or '—',r['confidence']]
        out.append('| '+' | '.join(cell(v) for v in values)+' |')
    out += ['', '## Abbreviations: review pending', '',
            'A mechanical candidate list with occurrence locations is available in `records/qa/abbreviation_candidates.md`. That list intentionally contains unclassified candidates and assigns no expansions. The primary reader must supply the reviewed abbreviation-and-expansion list here before delivery; expansions must not be inserted into the transcription.', '',
            '## Provisional legibility note — pending the primary reader’s final audit', '',
            f'This register currently contains {len(entries)} recorded doubts: {counts["high"]} high-confidence, {counts["medium"]} medium-confidence, and {counts["low"]} low-confidence entries. These counts summarize the recorded judgments; they do not measure the manuscript’s actual error rate or prove that every uncertain reading has been recorded.', '',
            'The notation observations retain unresolved differences in letter forms, accents, exponents, arrowheads, and typed versus handwritten material where the primary reader recorded them. The least secure passages must be identified by that reader from the images during the final audit. This note is explicitly provisional: the mechanical assembly did not inspect images and cannot independently assess handwriting legibility, physical damage, or completeness against the ink.', '']
    output=root/f'{PACKAGE}_doubts.md'
    output.write_text('\n'.join(out),encoding='utf-8')
    return {'output':str(output),'records':len(entries),'confidence_counts':dict(counts),'notation_rows':len(notation_rows(notation)),'generated_utc':generated}

def abbreviation_candidates(root):
    # Broad lexical patterns intentionally overgenerate. No candidate is asserted
    # to be an abbreviation and no expansion is inferred by this utility.
    patterns=[('period-form',re.compile(r"(?<![\w\\])(?:[^\W\d_]{1,12}\.){1,4}",re.UNICODE)),
              ('literal-short-form',re.compile(r"(?<![\w\\])(?:tt|tts|tte|ttes|tjs|tjrs|pt|pts|ssi|RR|NB|N°|n°|nº|cohomolgt|cohomologt|isomgt|nilpotts|élémts|resp|cqfd|i\.e\.|N\.B\.)(?!\w)",re.UNICODE)),
              ('capital-token',re.compile(r"(?<![\w\\])[A-Z]{2,6}(?!\w)",re.UNICODE))]
    found=defaultdict(list)
    for page in sorted((root/'pages').glob('*.tex')):
        scan=int(re.search(r'scan(\d+)',page.name).group(1))
        for number,line in enumerate(page.read_text(encoding='utf-8').splitlines(),1):
            # Control words themselves are not prose abbreviations.
            visible=re.sub(r'\\[A-Za-z]+',lambda m:' '*len(m.group(0)),line)
            seen=set()
            for kind,pattern in patterns:
                for m in pattern.finditer(visible):
                    token=m.group(0)
                    key=(token,m.start(),m.end())
                    if key in seen:continue
                    seen.add(key)
                    found[token].append({'scan':scan,'line':number,'pattern':kind,
                                         'source':page.name,
                                         'context':line[max(0,m.start()-45):min(len(line),m.end()+60)]})
    qa=root/'records/qa';qa.mkdir(exist_ok=True)
    output=qa/'abbreviation_candidates.md'
    lines=['# Mechanical abbreviation candidates — review required','',
           'This is a lexical extraction from the saved LaTeX, not a reading of the images. Full words at sentence ends, initials, mathematical operator names, figure labels, and TikZ dimension tokens can be false positives. No candidate is classified as an actual abbreviation, and no expansion is proposed. Review and transfer only confirmed abbreviations to the final doubts document.','',
           '| Candidate as encoded | Occurrences | Locations (scan:LaTeX line) | First literal source context |',
           '|---|---:|---|---|']
    for token,occ in sorted(found.items(),key=lambda p:p[0].casefold()):
        locations='; '.join(f"{o['scan']:03d}:{o['line']}" for o in occ)
        lines.append('| '+' | '.join([cell(token),str(len(occ)),cell(locations),cell(occ[0]['context'])])+' |')
    lines += ['', 'Locations refer to the saved LaTeX files, not estimated manuscript line numbers. All occurrences and their unabridged extracted context windows are retained in `abbreviation_candidates.json`.','']
    output.write_text('\n'.join(lines),encoding='utf-8')
    (qa/'abbreviation_candidates.json').write_text(json.dumps(found,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return {'output':str(output),'candidate_count':len(found),'occurrences':sum(map(len,found.values()))}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    args=p.parse_args()
    root=args.root.resolve()
    print(json.dumps({'doubts':assemble(root),'abbreviations':abbreviation_candidates(root)},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
