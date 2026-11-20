"""Prepare neutral box descriptions after all first readings; never expose readings."""
from pathlib import Path
import csv,json,re

W=Path(__file__).resolve().parents[1]
SCANS=[24,26,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,50,52,53]

def neutral(s):
    s=s.lower(); kinds=[]
    for pattern,label in [
        (r'insert|replacement','insertion'),
        (r'margin','margin note'),
        (r'struck|cancel|delet','cancelled passage'),
        (r'number|digit|numeric|numeral|footer|pagination|heading','number or heading'),
        (r'formula|diagram|index|indices|hat|prime|symbol|quotient|relation|tuple|mathematic','mathematical expression'),
        (r'difference|c/h|disputed|word|abbreviation|spelling|quotation','textual comparison'),
        (r'doubt|uncertain|confidence','uncertain passage')]:
        if re.search(pattern,s):kinds.append(label)
    return '; '.join(kinds) or 'passage for independent reading'

def main():
    for n in SCANS:
        assert (W/'pages'/f'147_scan{n:03d}.tex').exists(),f'First reading missing: {n}'
    for n in SCANS:
        p=W/'second'/f'147_scan{n:03d}_boxes.tsv'
        with p.open() as f:rows=list(csv.DictReader(f,delimiter='\t'))
        for r in rows:r['kind']=neutral(r['kind'])
        with p.open('w',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=['box','kind','x0','y0','x1','y1'],delimiter='\t')
            writer.writeheader();writer.writerows(rows)
    print('Prepared neutral blind box descriptions for all 24 pages.')

if __name__=='__main__':main()
