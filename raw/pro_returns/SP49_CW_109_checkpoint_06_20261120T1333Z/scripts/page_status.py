from pathlib import Path
import json,sys
W=Path(__file__).resolve().parents[1];n=int(sys.argv[1])
for r in 'ABC':
    p=W/'readers'/f'{n:03}'/r
    count=sum(x.suffix.lower() in ['.jpg','.jpeg','.png'] for x in (p/'crops').glob('*'))
    print(r, 'report', (p/'report.json').exists(), 'reading', (p/'reading.tex').exists(), 'crops', count)
