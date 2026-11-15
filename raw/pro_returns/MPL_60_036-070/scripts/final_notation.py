#!/usr/bin/env python3
"""Record the pre-context visual notation comparison; never run after freezing."""
from pathlib import Path
import json, re
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
assert 'transcription frozen ' not in (root/'progress.log').read_text()
for p in sorted((root/'pages').glob('*.tex')):
    s = p.read_text()
    n = int(p.stem[-3:])
    if n % 2 == 0:
        s = re.sub(r'([46]) -- (\d+) --', r'\1 - \2 -', s)
        s = s.replace('.--', '.-').replace('n°', r'n\textsuperscript{o}')
        s = re.sub(r'^-- si ', '- si ', s, flags=re.M)
    if n == 38:
        s = s.replace(r'\unsure{\theta|\vartheta}',r'\unsure{\vartheta|\theta}')
    if n == 41:
        s = s.replace(r'\unsure{mêmes}',r'\unsure{$=$s|mêmes}')
    if n == 47:
        s = s.replace(r'\unsure{même|$=$}',r'\unsure{$=$|même}')
    if n == 49:
        s = s.replace(r'\unsure{E_U(\varphi+1)}',r'\unsure{E_U(\varphi+1)|E_U(\rho+1)}')
        s = s.replace(r'\unsure{\varphi}',r'\unsure{\varphi|\rho}')
    if n == 53:
        s = s.replace(r'\unsure{\beta|\chi}',r'\unsure{\chi|\beta}')
    if n == 55:
        s = s.replace(r'\unsure{Chafarevitch} -- Ogg',r'\unsure{Chafarevitch} - Ogg')
    if n == 59:
        s = s.replace(r'\unsure{----|....}',r'\unsure{-{}-{}-{}-|....}')
    p.write_text(s)

revisions = {
37: {2: ['lines 6–7, L argument','t','Earlier s/U readings rejected after visual comparison of this writer’s t; stroke remains uncertain.','medium']},
38: {0: ['16, elements with subscript i','vartheta','theta; compared with the same typewritten form on scans054 and060.','medium']},
39: {4: ['middle insertion','E opère; triviale / trivialem. sur les','Ending and insertion attachment remain uncertain.','low']},
41: {0: ['opening paragraph','du pt de; essentiellement; =s','The equals sign followed by s is visible; an expanded mêmes would conceal the shorthand.','medium']},
47: {3: ['middle paragraph','Il revient / Il vient au =','Opening verb remains doubtful; two short parallel strokes replace the word même.','low']},
49: {2: ['erasure after D(EU)','[2] EU(φ+1)','EU(ρ+1); shift clearer than the crossed expression.','low'],3:['twists in long equality','deleted φ before 1','ρ; loop and entry stroke remain obscured by cancellation.','low']},
51: {2: ['last box scalar','φ','ρ; the enlarged loop extends to both sides of the stem here, unlike the cleaner right-hand loop on scan053; both alternatives are retained.','low']},
52: {0: ['opening formulas','χA, χB','γ; compared across scans052–060 and066, with chi favoured by the crossed diagonal.','low']},
53: {3: ['local exponent and final definition','χx','βx; cleaner unlooped forms on055 and057 favour chi, but the overwritten strokes here remain doubtful.','low']},
55: {4: ['local characteristic symbol','χx','βx; visual comparison with053 and057 completed; cleaner unlooped form favours chi.','medium']},
67: {3: ['reciprocal powers','n−rho; n−rho−1','n+rho; n+rho−1; enlargement favours a short horizontal stroke with no decisive vertical crossing.','low']}
}
additions = {
49: [['derived-functor R throughout','double-stem R (mathbb)','bold R; separate from the ordinary representation-ring R on043.','medium']],
61: [['derived-functor R throughout','double-stem R (mathbb)','bold R; paired visual reading with049.','medium']],
63: [['group in lower paragraph','bold Z / 2 bold Z','plain Z / 2 plain Z; heavy strokes do not decisively identify the alphabet.','low']],
65: [['cancelled paragraph and final line','= in la = propriété and de = pour','The written sign is preserved; expansion même is listed only here.','medium']],
67: [['paragraph beginning Mais supposons','lui-=','The short parallel strokes stand in place of même.','medium']]
}
for n in sorted(set(revisions)|set(additions)):
    p = root/'records'/f'scan{n:03}.json'
    d = json.loads(p.read_text())
    for k,v in revisions.get(n,{}).items(): d['doubts'][k] = v
    d['doubts'].extend(additions.get(n,[]))
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:
    f.write(f'notation consistency audit completed {now}: recurring alphabets, natural/xi, eta/y, local chi/beta, weight phi/rho, theta variants, derived R, primes/exclamation marks, quotation marks, equals shorthand, and typed dashes compared against the scans; unresolved visual differences explicitly retained.\n')
