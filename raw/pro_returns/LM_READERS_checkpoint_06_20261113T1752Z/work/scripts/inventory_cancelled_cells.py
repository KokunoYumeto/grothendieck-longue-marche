"""Identify exact tikz-cd diagrams whose cancelled labels leave empty cells."""
from pathlib import Path
import json,re
from layout_repairs import COVERAGE,_option_end

ROOT=Path(__file__).resolve().parents[2]

def balanced_end(text,start,left='{',right='}'):
    assert text[start]==left
    depth=1;i=start+1
    while i<len(text):
        if text[i]=='\\':
            if i+1<len(text) and not text[i+1].isalpha():i+=2;continue
        if text[i]==left:depth+=1
        elif text[i]==right:
            depth-=1
            if not depth:return i+1
        i+=1
    raise ValueError('Unbalanced cell argument')

def cells(diagram):
    start=_option_end(diagram,len(r'\begin{tikzcd}'))
    stop=diagram.rfind(r'\end{tikzcd}')
    replacement=r'ampersand replacement=\&' in diagram[:start]
    row=1;column=1;depth=0;env=[];i=start;begin=start
    while i<stop:
        if diagram[i]=='%' and (i==0 or diagram[i-1]!='\\'):
            e=diagram.find('\n',i);i=e if e>=0 else stop;continue
        m=re.match(r'\\(begin|end)\{([^}]+)\}',diagram[i:])
        if m:
            if m[1]=='begin':env.append(m[2])
            elif env:env.pop()
            i+=m.end();continue
        if not depth and not env:
            if diagram.startswith(r'\\',i):
                yield row,column,begin,diagram[begin:i]
                row+=1;column=1;i+=2
                if i<stop and diagram[i]=='[':i=_option_end(diagram,i)
                begin=i;continue
            sep=r'\&' if replacement else '&'
            if diagram.startswith(sep,i):
                yield row,column,begin,diagram[begin:i]
                column+=1;i+=len(sep);begin=i;continue
        if diagram[i]=='\\':
            m=re.match(r'\\(?:[A-Za-z@]+|.)',diagram[i:])
            i+=m.end() if m else 1;continue
        if diagram[i]=='{':depth+=1
        elif diagram[i]=='}':depth-=1
        i+=1
    yield row,column,begin,diagram[begin:stop]

def removed_label(cell):
    text=re.sub(r'%[^\n]*','',cell)
    # Remove arrow declarations, since they do not constitute cell contents.
    for m in list(re.finditer(r'\\(?:arrow|ar)\b',text))[::-1]:
        end=m.end()
        while end<len(text) and text[end].isspace():end+=1
        if end<len(text) and text[end]=='[':end=_option_end(text,end)
        elif end<len(text) and text[end]=='{':end=balanced_end(text,end)
        text=text[:m.start()]+text[end:]
    found=False
    while True:
        m=re.search(r'\\deleted\s*\{',text)
        if not m:break
        end=balanced_end(text,m.end()-1)
        text=text[:m.start()]+text[end:];found=True
    text=re.sub(r'\\(?:displaystyle|textstyle|scriptstyle|scriptscriptstyle|relax|mathord|text|mathrm|mathit|mathbf|mathsf|mathcal|mathbb|unsure)\b','',text)
    return found and not re.sub(r'[\s{}$]','',text)

def main():
    records=[]
    for language,folder,suffix in [('fr','fr/texts',''),('en','en/packages','_en')]:
        for package in COVERAGE:
            source=Path('sources')/folder/(package+suffix+'.tex');text=(ROOT/source).read_text()
            ordinals={}
            for match in re.finditer(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',text,re.S):
                previous=list(re.finditer(r'\\scanpage\{(\d+)',text[:match.start()]))
                scan=int(previous[-1][1]);ordinals[scan]=ordinals.get(scan,0)+1
                removed=[dict(row=row,column=col,cell=cell) for row,col,offset,cell in cells(match[0]) if removed_label(cell)]
                if removed:
                    records.append(dict(package=package,language=language,cote=COVERAGE[package]['cote'],scan=scan,
                        ordinal=ordinals[scan],source_line=text[:match.start()].count('\n')+1,
                        source_path=source.relative_to('sources').as_posix(),cancelled_cells=removed,diagram=match[0]))
    path=ROOT/'work/data/layout_cancelled_cells.json';path.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    print(f'{len(records)} language-specific diagrams, {sum(len(r["cancelled_cells"]) for r in records)} cancelled cells')
    for r in records:print(r['language'],r['package'],r['scan'],r['ordinal'],[(c['row'],c['column']) for c in r['cancelled_cells']])

if __name__=='__main__':main()
