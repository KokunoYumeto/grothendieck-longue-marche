r"""Mechanical compile repairs authorized by en/COMPILE.tsv, with exact diffs.

Replicates the three supplied repair scripts in their recorded order. The
missing build_fixes.math_mask dependency is supplied here as a lexical TeX
mode scanner. Only packages marked as needing mechanical repairs are changed.
No source file is edited; repair(text, package, language) returns new text and
per-place records. A complete standard TeX Live remains the compile target.
"""
from __future__ import annotations
import csv, difflib, re
from pathlib import Path

B='\\'
TIKZ=re.compile(re.escape(B+'begin{tikzcd}')+r'(\[[^\]]*\])?(.*?)'+re.escape(B+'end{tikzcd}'),re.S)
LENGTH=re.compile(r'\s*-?[\d.]+\s*(pt|em|ex|mm|cm|bp|in|sp|pc|mu)\s*\]')
UNWRAP=re.compile(re.escape(B+'begin{gathered}')+r'\s*('+re.escape(B+'diagram{')+r'(?:(?!'+re.escape(B+'begin{gathered}')+r').)*?'+re.escape(B+'end{tikzcd}')+r'\})\s*'+re.escape(B+'end{gathered}'),re.S)
COMMAND=re.compile(r'\\([A-Za-z@]+|.)',re.S)
MATH_ENVS={'equation','equation*','displaymath','math','align','align*','alignat','alignat*','flalign','flalign*','aligned','alignedat','gather','gather*','gathered','multline','multline*','split','array','matrix','pmatrix','bmatrix','Bmatrix','vmatrix','Vmatrix','smallmatrix','cases','tikzcd'}
TEXT_MACROS={'text','textrm','textnormal','textsf','texttt','textit','textbf','textsc','mbox','hbox','operatorname'}


def eligibility():
    if not hasattr(eligibility,'cache'):
        with Path('sources/en/COMPILE.tsv').open() as f:
            rows=list(csv.DictReader(f,delimiter='\t'))
        eligibility.cache={r['package'] for r in rows if 'mechanical' in r['english']}
    return eligibility.cache


def _brace_end(s,start):
    depth=1;i=start+1
    while i<len(s):
        if s[i]=='\\':
            m=COMMAND.match(s,i);i=m.end() if m else i+2
        elif s[i]=='%':
            j=s.find('\n',i);i=len(s) if j<0 else j+1
        elif s[i]=='{':depth+=1;i+=1
        elif s[i]=='}':
            depth-=1;i+=1
            if not depth:return i
        else:i+=1
    raise ValueError('Unclosed TeX argument')


def math_mask(s):
    """Use the shared scanner, including parbox and other text-box arguments."""
    from editorial import math_mode_map
    return math_mode_map(s)


def brace_labels(body):
    """Exact logic of build/fix_tikzcd_in_macros.py."""
    out=[];i=0
    for m in re.finditer(r'\\arrow\[',body):
        out.append(body[i:m.end()]);j=m.end();depth=1;k=j
        while k<len(body) and depth:
            depth+={'[':1,']':-1}.get(body[k],0);k+=1
        opts=body[j:k-1]
        def fix(mm):
            lab=mm.group(1);d=0;top_comma=False
            for ch in lab:
                d+={'{':1,'}':-1}.get(ch,0)
                if ch==',' and d==0:top_comma=True
            return '"{'+lab+'}"' if top_comma and not(lab.startswith('{') and lab.endswith('}')) else mm.group(0)
        out.append(re.sub(r'"([^"]*)"',fix,opts)+']');i=k
    out.append(body[i:]);return ''.join(out)


def env_pairs(s,name):
    tok=re.compile(re.escape(B+'begin{'+name+'}')+'|'+re.escape(B+'end{'+name+'}'))
    pairs=[];depth=0;start=None
    for m in tok.finditer(s):
        if m.group(0).startswith(B+'begin'):
            if depth==0:start=m.start()
            depth+=1
        elif depth:
            depth-=1
            if depth==0:pairs.append((start,m.end()))
    return pairs


def brace_gathered_cells(body):
    out=[];i=0
    for a,e in env_pairs(body,'gathered'):
        before=body[max(0,a-300):a];cell_start=max(before.rfind(B+'&'),before.rfind(B+B))
        cell=before[cell_start+1:] if cell_start!=-1 else before
        unmatched_left=cell.count(B+'left')>cell.count(B+'right');already=body[max(0,a-1):a]=='{'
        out.append(body[i:a]);out.append(body[a:e] if(unmatched_left or already) else '{'+body[a:e]+'}');i=e
    out.append(body[i:]);return ''.join(out)


def _gathered_array(t):
    parts=[];i=0
    for a,e in env_pairs(t,'gathered'):
        block=t[a:e]
        if B+'begin{tikzcd}' in block:
            inner=block[len(B+'begin{gathered}'):-len(B+'end{gathered}')]
            block=B+'begin{array}{c}'+inner+B+'end{array}'
        parts.append(t[i:a]+block);i=e
    parts.append(t[i:]);return ''.join(parts)


def _tikz(t):
    out=[];i=0
    for m in TIKZ.finditer(t):
        opts=m.group(1) or '';body=m.group(2)
        if 'ampersand replacement' not in opts:
            opts='[ampersand replacement='+B+'&'+(','+opts[1:-1] if opts[1:-1].strip() else '')+']'
            body=re.sub(r'(?<!\\)&',lambda _:B+'&',body)
        body=brace_gathered_cells(brace_labels(body))
        out.append(t[i:m.start()]+B+'begin{tikzcd}'+opts+body+B+'end{tikzcd}');i=m.end()
    out.append(t[i:]);return ''.join(out)


def _operators(t):
    mask=math_mask(t);out=[];i=0
    for m in re.finditer(re.escape(B+'operatorname{'),t):
        if mask[m.start()]:continue
        end=_brace_end(t,m.end()-1)
        out.append(t[i:m.start()]+'$'+t[m.start():end]+'$');i=end
    out.append(t[i:]);return ''.join(out)


def _brackets(t):
    def br(mm):
        if LENGTH.match(t[mm.end():mm.end()+30]):return mm.group(0)
        return mm.group(1)+'{}'+mm.group(2)+'['
    return re.sub(r'(\\\\)(\s*)\[',br,t)


def _diagram_array(t):
    return re.sub(r'\\diagram\{\s*\\begin\{array\}(.*?)\\end\{array\}\s*\}',lambda m:B+'diagram{$'+B+'begin{array}'+m.group(1)+B+'end{array}$}',t,flags=re.S)

STAGES=[
 ('gathered-array',_gathered_array,'A gathered environment collecting TikZ-CD as an argument prevents matrix parsing. Replaced only the outer gathering wrapper by array{c}, preserving every entry.'),
 ('tikz-macro-syntax',_tikz,'Explicit ampersand replacement makes TikZ-CD safe inside macro arguments; comma-bearing arrow labels and gathered cells are braced. Diagram entries and arrow content are unchanged.'),
 ('unwrap-gathered',lambda s:UNWRAP.sub(lambda m:m.group(1),s),'Removed a redundant gathered wrapper around one already centered TikZ-CD diagram.'),
 ('operator-math-mode',_operators,'Wrapped an operatorname used outside mathematics in math delimiters; the operator name is unchanged.'),
 ('row-bracket',_brackets,'Inserted an empty group after a row break so a following literal opening bracket is not parsed as optional vertical spacing.'),
 ('array-math-mode',_diagram_array,'Placed an array supplied as a diagram into math mode; array content is unchanged.')]


def _opcodes(before,after):
    """Line anchors keep exact character diffs fast in repetitive TeX."""
    a=before.splitlines(keepends=True);b=after.splitlines(keepends=True)
    ao=[0];bo=[0]
    for line in a:ao.append(ao[-1]+len(line))
    for line in b:bo.append(bo[-1]+len(line))
    outer=difflib.SequenceMatcher(None,a,b,autojunk=False)
    for tag,i,j,k,l in outer.get_opcodes():
        if tag=='equal':continue
        aa=before[ao[i]:ao[j]];bb=after[bo[k]:bo[l]]
        inner=difflib.SequenceMatcher(None,aa,bb,autojunk=max(len(aa),len(bb))>6000)
        for kind,x,y,u,v in inner.get_opcodes():
            if kind!='equal':yield kind,ao[i]+x,ao[i]+y,bo[k]+u,bo[k]+v


def repair(text,package,language):
    language=language.lower()
    if package not in eligibility():return text,[]
    records=[];current=text
    for stage,fn,reason in STAGES:
        new=fn(current)
        if new!=current:
            for n,(tag,a,b,c,d) in enumerate(_opcodes(current,new)):
                if tag=='equal':continue
                scans=list(re.finditer(r'\\scanpage\{(\d+)\}',current[:a]));scan=int(scans[-1][1]) if scans else 0
                records.append(dict(id=f'MECH-{language}-{package}-{stage}-{n}',language=language,package=package,scan=scan,
                    source_path=('fr/texts/'+package+'.tex' if language=='fr' else 'en/packages/'+package+'_en.tex'),
                    source_line=current.count('\n',0,a)+1,stage=stage,kind='mechanical LaTeX repair',reason=reason,
                    before=current[a:b],after=new[c:d],offset_before=a,offset_after=c,
                    context_before=current[max(0,a-60):min(len(current),b+60)]))
        current=new
    return current,records


def verify_reversal(original,repaired,records):
    """Reverse stages and their nonoverlapping source diffs exactly."""
    s=repaired
    for stage,_,_ in reversed(STAGES):
        for r in sorted((r for r in records if r['stage']==stage),key=lambda r:r['offset_after'],reverse=True):
            a=r['offset_after'];b=a+len(r['after'])
            if s[a:b]!=r['after']:return False
            s=s[:a]+r['before']+s[b:]
    return s==original

if __name__=='__main__':
    import json
    rows=[];counts={};verified=0
    for language in ('fr','en'):
        for package in sorted(eligibility()):
            path=Path('sources/fr/texts')/(package+'.tex') if language=='fr' else Path('sources/en/packages')/(package+'_en.tex')
            s=path.read_text();new,rs=repair(s,package,language)
            assert verify_reversal(s,new,rs),(language,package)
            rows.extend(rs);counts[language+'/'+package]=len(rs);verified+=1
            print(language,package,len(rs),flush=True)
    output=Path('work/data/mechanical_repairs.json');output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps({'records':rows,'counts':counts,'reversal_checks':verified},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'guarded_packages':len(eligibility()),'language_package_checks':verified,'diff_records':len(rows),'stages':{stage:sum(r['stage']==stage for r in rows) for stage,_,_ in STAGES}},indent=2))
