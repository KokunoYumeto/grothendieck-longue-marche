from pathlib import Path
from PIL import Image
import csv, json, shutil, sys

BASE = Path('/workspace/scratch/27306e6fcc57')
SRC = BASE / 'source'
WORK = BASE / 'SP94_C13_151_work'

def prepare(page):
    packet = BASE / 'reading_packets' / page
    packet.mkdir(parents=True, exist_ok=True)
    scan = int(page.rsplit('scan', 1)[1])
    image = SRC / 'SP94_C13_151_scans' / (page + '.jpg')
    shutil.copyfile(image, packet / 'page.jpg')
    im = Image.open(image)
    w, h = im.size
    if w <= h:
        halves = [('top', (0, 0, w, round(h*.55))), ('bottom', (0, round(h*.45), w, h))]
    else:
        halves = [('left', (0, 0, round(w*.55), h)), ('right', (round(w*.45), 0, w, h))]
    for name, box in halves:
        dest = packet / (name + '.png')
        if not dest.exists(): im.crop(box).save(dest)
    shutil.copyfile(SRC/'SP94_C13_151_texts/pages'/(page+'.tex'), packet/'C.tex')
    shutil.copyfile(SRC/'SP94_C13_151_texts/hua'/('hua_'+page+'.tex'), packet/'H.tex')
    shutil.copyfile(SRC/'SP94_C13_151_texts/PREAMBLE.tex', packet/'PREAMBLE.tex')
    shutil.copyfile(WORK/'notation.md', packet/'notation.md')
    for src, dest, key, value in [
        (SRC/'SP94_C13_151_C_H_differences.tsv', 'differences.tsv', 'page', page),
        (SRC/'SP94_C13_151_texts/MARKS.tsv', 'marks.tsv', 'scan', str(scan))]:
        with src.open() as f:
            # The supplied TSV is raw tab-separated text; TikZ quote characters
            # are literal data, not CSV field delimiters.
            reader=csv.DictReader(f,delimiter='\t',quoting=csv.QUOTE_NONE); fields=reader.fieldnames
            rows=[r for r in reader if r[key]==value]
        with (packet/dest).open('w') as f:
            writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(rows)
    prompt=(BASE/'upload/PROMPT(20261121-193705).md').read_text()
    relevant=prompt[prompt.index('## The errors that recur'):prompt.index('## Method')]
    (packet/'reading_rules.md').write_text(relevant)
    print(json.dumps({'page':page,'packet':str(packet),'dimensions':[w,h],'halves':halves}))

if __name__=='__main__':
    for page in sys.argv[1:]: prepare(page)
