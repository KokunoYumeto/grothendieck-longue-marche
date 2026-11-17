"""Assemble post-freeze research drafts without touching transcription bytes."""
from pathlib import Path
import argparse, re
from datetime import datetime, timezone

p=argparse.ArgumentParser()
p.add_argument('--partial',action='store_true')
args=p.parse_args()
root=Path(__file__).resolve().parents[1]
research=root/'research'
assert 'context opened' in (root/'progress.log').read_text()

def items(name, first, stop=None):
    path=research/name
    if not path.exists():
        if args.partial:
            return '\nResearch section is still being drafted; completed work is preserved in the accompanying research files.\n'
        raise FileNotFoundError(path)
    s=path.read_text()
    assert first in s,(name,first)
    s=s[s.index(first):]
    if stop and stop in s:
        s=s[:s.index(stop)]
    return s.strip()+'\n'

sections=[(research/'report_opening.md').read_text()]
lecture=research/'lecture_notes_draft.md'
if lecture.exists():
    body=lecture.read_text()
    matches=list(re.finditer(r'^#{2,4} (?:L\d+|LR\d+)[^\n]*',body,re.M))
    if not matches:
        raise ValueError('Inspect lecture note headings before assembly.')
    body=body[matches[0].start():]
    # Supplementary summaries remain in the research work record, while the
    # final report has its own standing-question and pagination sections.
    for marker in ['\n## Standing-question', '\n## Standing question', '\n## Search record', '\n## Context-search', '\n## Coverage']:
        if marker in body: body=body.split(marker,1)[0]
    sections+=['\n## Lecture, construction, and open programme\n',body]
elif args.partial:
    sections+=['\n## Lecture, construction, and open programme\n\nThis section is being drafted.\n']
else:
    raise FileNotFoundError(lecture)

sections += ['\n## Shadows, binomial arithmetic, and categorical scope\n',
             items('shadow_notes_draft.md','### SH01','\n## Boundaries for merging'),
             '\n## Homogeneous maps, negative degrees, and divisibility\n',
             items('negative_hom_notes_draft.md','### NH01','\n## Standing-question contribution'),
             '\n## Documentary and reused-source questions\n',
             items('documentary_notes_draft.md','### D001'),
             (research/'report_closing.md').read_text()]
text='\n\n'.join(x.strip() for x in sections)+'\n'
# These changes affect editorial prose only, never source transcription.
text=re.sub(r'\bcote136\b','cote 136',text)
text=re.sub(r'\bscans(?=\d)','scans ',text)
text=re.sub(r'\bscan(?=\d)','scan ',text)
text=re.sub(r'\bpages(?=\d)','pages ',text)
text=re.sub(r'\blines(?=\d)','lines ',text)
text=re.sub(r'\bline(?=\d)','line ',text)
text=re.sub(r'\bgapg(?=\d)','gap g',text)
text=text.replace('$omega_0',r'$\omega_0')
text=re.sub(r'\bmanuscript pp(?=\d)', 'visible lower folios ', text)
text=re.sub(r'\bmanuscript p(?=\d)', 'visible lower folio ', text)
text=re.sub(r'\bLemme(?=\d)', 'Lemme ', text)
text=text.replace('equal to1', 'equal to 1').replace('are3 and2', 'are 3 and 2')
out=root/'MPL_136_002-046_notes.md'
out.write_text(text)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:
    f.write(f'research notes {"partial" if args.partial else "assembled"} {now}; post-freeze context analysis; transcription untouched\n')
print(f'{out.name}: {len(text.encode())} bytes; {len(text.split())} whitespace-delimited words; partial={args.partial}')
