from pathlib import Path
import re
ROOT=Path('/workspace/scratch/b8e2c31cadf4/work')
BASE='MPL_36_053-085+39'
def macro_args(text,name):
    for match in re.finditer(r'\\'+name+r'\{',text):
        pos=match.end(); start=pos; depth=1
        while pos<len(text) and depth:
            if text[pos]=='{' and (pos==0 or text[pos-1]!='\\'): depth+=1
            elif text[pos]=='}' and (pos==0 or text[pos-1]!='\\'): depth-=1
            pos+=1
        yield match.start(),text[start:pos-1]
def cell(s): return s.replace('|','&#124;').replace('\n',' ').strip()
def rebuild():
    lines=[(ROOT/'notation.md').read_text(),'# Doubts\n\nLocations use the line in the individual LaTeX page file as a reproducible approximate locator; the adjoining words identify the manuscript passage. Doubts within heavily cancelled text are low confidence. Other marked readings are medium confidence unless specified otherwise.\n\n| Cote | Scan | Approximate location | Reading | Alternatives | Confidence |\n|---|---|---|---|---|---|']
    for p in sorted((ROOT/'pages').glob('*.tex')):
        m=re.search(r'_(36|39)_scan(\d+)\.tex',p.name); t=p.read_text()
        for pos,arg in macro_args(t,'unsure'):
            a=arg.split('|',1); ln=t[:pos].count('\n')+1
            prior=t[max(0,pos-70):pos]
            conf='low' if '\\deleted{' in prior or '\\unsure{' in arg else 'medium'
            lines.append(f'| {m[1]} | {m[2]} | TeX line {ln} | `{cell(a[0])}` | {"`"+cell(a[1])+"`" if len(a)>1 else "—"} | {conf} |')
        for pos,arg in macro_args(t,'illegible'):
            ln=t[:pos].count('\n')+1
            lines.append(f'| {m[1]} | {m[2]} | TeX line {ln} | physically unreadable, estimated {cell(arg)} words | — | low |')
    lines.extend(['\n'+(ROOT/'abbreviations.md').read_text(),'\n# Legibility\n\nThe typed sheets are generally clear; the handwritten pages contain rapidly compressed words, overwritten symbols, marginal additions, and very dense diagrams. Marks of doubt indicate unresolved readings rather than mathematical corrections. The cancelled passages, small subscripts, and terms at the outer edge of diagrams are the least secure. All supplied whole-page and half-page images are being read visually; no OCR is used.\n'])
    (ROOT/(BASE+'_doubts.md')).write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__': rebuild()
