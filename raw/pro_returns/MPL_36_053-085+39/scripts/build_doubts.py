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
def deleted_ranges(t):
    out=[]
    for pos,arg in macro_args(t,'deleted'):
        out.append((pos,pos+len('\\deleted{')+len(arg)+1))
    return out
def cell(s): return s.replace('|','&#124;').replace('\n',' ').strip()
def rebuild():
    lines=[(ROOT/'notation.md').read_text(),'# Doubts\n\nLocations use the line in the individual LaTeX page file as a reproducible approximate locator; the adjoining words identify the manuscript passage. Doubts within heavily cancelled text are low confidence. Other marked readings are medium confidence unless specified otherwise.\n\n| Cote | Scan | Approximate location | Reading | Alternatives | Confidence |\n|---|---|---|---|---|---|']
    for p in sorted((ROOT/'pages').glob('*.tex')):
        m=re.search(r'_(36|39)_scan(\d+)\.tex',p.name); t=p.read_text()
        for pos,arg in macro_args(t,'unsure'):
            a=arg.split('|',1); ln=t[:pos].count('\n')+1
            prior=t[max(0,pos-70):pos]
            conf='low' if any(a <= pos < b for a,b in deleted_ranges(t)) or '\\unsure{' in arg else 'medium'
            lines.append(f'| {m[1]} | {m[2]} | TeX line {ln} | `{cell(a[0])}` | {"`"+cell(a[1])+"`" if len(a)>1 else "—"} | {conf} |')
        for pos,arg in macro_args(t,'illegible'):
            ln=t[:pos].count('\n')+1
            lines.append(f'| {m[1]} | {m[2]} | TeX line {ln} | physically unreadable, estimated {cell(arg)} words | — | low |')
    lines.extend(['\n'+(ROOT/'abbreviations.md').read_text(),'\n# Legibility\n\nAll 49 whole-page images and all 98 half-page images were read visually, followed by a second page-by-page comparison and a package-wide notation review before the transcription was frozen. No OCR was used. The reused typescripts are generally clearer than the handwriting, although their ornate mathematical fonts sometimes remain ambiguous. The handwritten pages have compressed endings, very small indices, faint blue ink, interlinear insertions and multiple layers of cancellation. The least secure passages are the cancelled divisibility proof on 36/067, the compressed marginal and draft arguments on 36/069–071, the marginal category/module notes on 39/011, the overwritten functor notation on 39/015, and the multiply cancelled preparation proof on 39/019–020. Several formulas and phrases remain surprising even where their strokes are clear; they were not corrected to make the mathematics work. Explicit doubt marks are a candid record of the remaining reading risk, not an excuse to omit a passage. Dense diagrams were transcribed object by object and arrow by arrow; very small heads, indices and decorations remain less secure than the main objects. Long descenders were compared against genuine underlining. Structural checks establish balanced LaTeX syntax and complete page/inventory coverage, but do not certify a reading or replace a real TeX compilation; the available TeX installation lacked its formats and required packages.\n'])
    (ROOT/(BASE+'_doubts.md')).write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__': rebuild()
