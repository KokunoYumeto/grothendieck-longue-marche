"""Read-only research-note and bibliography structure checks."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
text = (root/'MPL_33_050-097_notes.md').read_text()
heads = list(re.finditer(r'^### (N\d{2}) — (.+)$', text, re.M))
assert [m[1] for m in heads] == [f'N{i:02}' for i in range(1,73)]
queries = (root/'records/context_queries.md').read_text()
assert re.findall(r'^## (N\d{2})$', queries, re.M) == [m[1] for m in heads]
allowed = ['conjecture', 'unproved claim', 'unpursued implication', 'own idea',
           'reading question', 'self-flagged', 'withdrawn in the same text']
counts = {}
for i, m in enumerate(heads):
    end = heads[i+1].start() if i+1 < len(heads) else text.index('## VIII.')
    section = text[m.end():end]
    assert '**Locator:** Cote 33,' in section, m[1]
    assert '**Context:**' in section and f'search {m[1]}' in section, m[1]
    kind = re.search(r'\*\*Kind:\*\* ([^\n]+)', section)[1]
    key = next((k for k in allowed if kind.startswith(k)), None)
    assert key, (m[1],kind)
    counts[key] = counts.get(key,0)+1
    if key == 'own idea': assert '**Confidence:**' in section, m[1]
    if key == 'withdrawn in the same text': assert '→' in kind, m[1]
    # The final paragraph before the next section is the 1-4-sentence note body;
    # punctuation inside quotations and references requires human review.
    body = [p for p in section.split('\n\n') if p and not p.startswith('**') and not p.startswith('##')]
    assert len(body) == 1, (m[1],len(body))
    assert '“' in body[0], (m[1],'brief source quote missing')
    assert body[0].count('$') % 2 == 0, (m[1],'unbalanced math delimiter')

for url in re.findall(r'\]\((https?://[^)]+)\)',text):
    assert not re.search(r'\s',url), ('Whitespace in URL',url)
    assert not url.endswith('.'), ('Trailing period in URL',url)
for line in text.splitlines():
    assert line.count('`') % 2 == 0, ('Unpaired code span',line[:160])
for section in ['## VIII.', '## IX.', '## X.', '## XI.']:
    assert section in text
print(f'PASS: {len(heads)} ordered notes, per-note context searches, locators, kinds, quotes, confidence fields, standing sections, balanced inline delimiters and URL checks.')
print('Classifications:', counts)
print('Word count including tables and references:', len(text.split()))

