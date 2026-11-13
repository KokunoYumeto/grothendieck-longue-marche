"""Explicit, source-local mathematical layout repairs for La Longue Marche.

No runtime fitting, scaling callback, font substitution, or hidden overflow.
Each change is keyed to a package and scan and is returned with its exact before
and after strings. Run before editorial annotation; forms share these patches.
"""
from pathlib import Path
import re,json,difflib
ROOT=Path(__file__).resolve().parents[2]
B='\\'
COVERAGE={p['package']:p for p in json.loads((ROOT/'sources/en/MANIFEST.json').read_text())['packages']}

def _scan_ranges(text):
    ms=list(re.finditer(r'\\scanpage\{(\d+)[^}]*\}',text))
    return [(int(m[1]),m.start(),ms[i+1].start() if i+1<len(ms) else len(text)) for i,m in enumerate(ms)]

def _option_end(t,start):
    if start>=len(t) or t[start]!='[': return start
    depth=0;brace=0
    for i in range(start,len(t)):
        if t[i]=='{' and (i==0 or t[i-1]!='\\'):brace+=1
        elif t[i]=='}' and (i==0 or t[i-1]!='\\'):brace-=1
        if brace==0:
            if t[i]=='[':depth+=1
            elif t[i]==']':
                depth-=1
                if not depth:return i+1
    raise ValueError('Unclosed tikz-cd options')

def _compact(diagram, fontsize=10, colsep=9, rowsep=14):
    a=len(r'\begin{tikzcd}')
    e=_option_end(diagram,a)
    opts=diagram[a+1:e-1] if e>a else ''
    extra=f'column sep={colsep}pt,row sep={rowsep}pt,execute at begin picture={{\\fontsize{{{fontsize}}}{{{fontsize+2}}}\\selectfont}}'
    return diagram[:a]+'['+opts+(',' if opts else '')+extra+']'+diagram[e:]

def _replace_scan(text,scan,fun,records,package,language):
    for n,a,b in _scan_ranges(text):
        if n!=scan:continue
        old=text[a:b];new,local=fun(old)
        for r in local:
            r.update(package=package,language=language,cote=COVERAGE[package]['cote'],scan=scan,
                     source_line=text[:a].count('\n')+old[:r.pop('offset')].count('\n')+1)
            records.append(r)
        return text[:a]+new+text[b:]
    return text

def _edit(t,old,new,why,kind='display line break',n=1):
    count=t.count(old)
    if count!=n:return t,[]
    records=[];start=0
    for _ in range(n):
        i=t.find(old,start);records.append(dict(offset=i,old=old,new=new,kind=kind,reason=why));start=i+len(old)
    return t.replace(old,new),records

def _chain(t,edits):
    records=[]
    for old,new,why,*kind in edits:
        t,r=_edit(t,old,new,why,kind[0] if kind else 'display line break');records+=r
    return t,records

def _boundary_map(old,new,boundaries):
    """Map the boundaries of new text to the checked source, preserving equals."""
    out=[0]*(len(new)+1)
    for tag,a,b,c,d in difflib.SequenceMatcher(None,old,new,autojunk=False).get_opcodes():
        if tag=='equal':
            out[c:d+1]=boundaries[a:b+1]
        elif d>c:
            for j in range(c,d+1):
                out[j]=boundaries[a+(b-a)*(j-c)//(d-c)]
        else:
            out[c]=boundaries[b]
    return out

def _audit_records(initial,final,records,package,language,check_width_counts=True):
    """Replay every exact replacement and locate it in the immutable source.

    Some repairs deliberately refine an earlier local edit. Their ``old`` is
    therefore the exact intermediate text, while ``source_old`` and the source
    offsets identify its original checked-source span. Offsets are zero-based;
    the end is exclusive. A separate exact scan-patch manifest records the net
    before/after text without these intermediate stages.
    """
    source_path=Path('fr/texts' if language=='fr' else 'en/packages')/(package+('_en' if language=='en' else '')+'.tex')
    # Preserve checked-source CRLF bytes here even though the TeX assembly
    # deliberately uses Python's normalized newline view.
    raw=(ROOT/'sources'/source_path).read_bytes().decode('utf-8')
    raw_scans={scan:(a,b,raw[a:b]) for scan,a,b in _scan_ranges(raw)}
    initial_scans={scan:(a,b,initial[a:b]) for scan,a,b in _scan_ranges(initial)}
    final_scans={scan:final[a:b] for scan,a,b in _scan_ranges(final)}
    byscan={}
    for record in records:byscan.setdefault(record['scan'],[]).append(record)
    for scan,local in byscan.items():
        ra,rb,original=raw_scans[scan]
        ia,ib,current=initial_scans[scan]
        mapping=_boundary_map(original,current,list(range(ra,rb+1)))
        for record in local:
            old,new=record['old'],record['new']
            count=current.count(old)
            if count!=1:raise ValueError(f'Layout replay expected one match: {package} {language} scan {scan} {record["id"]}: {count}')
            start=current.index(old);end=start+len(old)
            a,b=mapping[start],mapping[end]
            record.update(source_path=source_path.as_posix(),source_offset_start=a,source_offset_end=b,
                          source_byte_start=len(raw[:a].encode('utf-8')),source_byte_end=len(raw[:b].encode('utf-8')),
                          source_line=raw[:a].count('\n')+1,source_old=raw[a:b],expected_match_count=1)
            replacement_map=_boundary_map(old,new,mapping[start:end+1])
            mapping=mapping[:start]+replacement_map+mapping[end+1:]
            current=current[:start]+new+current[end:]
        if current!=final_scans[scan]:raise ValueError(f'Layout replay does not reproduce output: {package} {language} scan {scan}')
    expected_file=ROOT/'work/data/layout_expected_matches.json'
    if check_width_counts and expected_file.exists():
        for expected in json.loads(expected_file.read_text()):
            if (expected['package']==package and expected['language']==language
                    and expected['scan'] in initial_scans):
                count=sum(r['kind'] not in ('empty diagram cell','manuscript-page placement','paired marginal notes') for r in byscan.get(expected['scan'],[]))
                if count!=expected['expected_changes']:
                    raise ValueError(f'Expected {expected["expected_changes"]} local layout changes in {package} {language} scan {expected["scan"]}, found {count}')

def repair_empty_cells(text,package,language):
    """Retain invisible nodes at explicitly inventoried cancelled cell sites.

    This structural correction is independent of width repairs and may also be
    applied to a baseline build. It introduces no text, scaling, or font change.
    """
    initial=text;records=[]
    targets=json.loads((ROOT/'work/data/layout_cancelled_cells.json').read_text())
    present={n for n,a,b in _scan_ranges(text)}
    for target in targets:
        if target['package']!=package or target['language']!=language or target['scan'] not in present:continue
        def fix(t):
            ms=list(re.finditer(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',t,re.S))
            ordinal=target['ordinal']
            if ordinal>len(ms):raise ValueError(f'Missing cancelled-cell diagram: {package} {language} scan {target["scan"]} diagram {ordinal}')
            m=ms[ordinal-1];old=m[0]
            a=len(r'\begin{tikzcd}');e=_option_end(old,a)
            options=old[a+1:e-1] if e>a else ''
            if 'nodes in empty cells' in options:return t,[]
            new=old[:a]+'['+options+(',' if options else '')+'nodes in empty cells]'+old[e:]
            coordinates=', '.join(f'({c["row"]},{c["column"]})' for c in target['cancelled_cells'])
            record=dict(offset=m.start(),old=old,new=new,kind='empty diagram cell',
                reason=f'Retain invisible nodes in the explicitly cancelled diagram cells {coordinates}; this preserves arrow endpoints when corrected forms omit the cancelled labels.',
                id=f'{target["cote"]}-{target["scan"]}-E{ordinal}')
            return t[:m.start()]+new+t[m.end():],[record]
        text=_replace_scan(text,target['scan'],fix,records,package,language)
    if records:_audit_records(initial,text,records,package,language,check_width_counts=False)
    return text,records

def repair_pagefigures(text,package,language):
    """Keep the one circled manuscript page number intact in reading forms."""
    if package!='LM_C1-020-037' or 20 not in {n for n,a,b in _scan_ranges(text)}:return text,[]
    initial=text;records=[]
    old=r'''\figure{\begin{tikzpicture}
\node[draw,circle,inner sep=3pt] {\mspage{7}};
\end{tikzpicture}}'''
    new=r'\LMpagefigure{'+old+r'}{7}'
    def fix(t):
        if new in t:return t,[]
        if t.count(old)!=1:raise ValueError(f'Expected one circled manuscript-page figure: {package} {language} scan 20')
        result,local=_edit(t,old,new,'Keep the circled manuscript page number 7 as a complete figure; the reading form places that complete marker in the margin.',kind='manuscript-page placement')
        for r in local:r['id']='140-1-20-PF1'
        return result,local
    text=_replace_scan(text,20,fix,records,package,language)
    if records:_audit_records(initial,text,records,package,language,check_width_counts=False)
    return text,records

def repair_paired_margins(text,package,language):
    """Place the one adjacent-note pair in a single box with two baselines."""
    if package!='LM_P035' or 344 not in {n for n,a,b in _scan_ranges(text)}:return text,[]
    initial=text;records=[]
    wording='pas séparé' if language=='fr' else 'not separated'
    item=r'\margin{\unsure{'+wording+'}}'
    old=item+'\n'+item;new=r'\LMpairedmargins{'+old+'}'
    def fix(t):
        if new in t:return t,[]
        if t.count(old)!=1:raise ValueError(f'Expected one adjacent marginal-note pair: {package} {language} scan 344')
        result,local=_edit(t,old,new,'Put the two unchanged adjacent marginal notes in one margin box with two separate baselines, retaining both note references and both linked doubtful readings.',kind='paired marginal notes')
        for r in local:r['id']='140-2-344-NP1'
        return result,local
    text=_replace_scan(text,344,fix,records,package,language)
    if records:_audit_records(initial,text,records,package,language,check_width_counts=False)
    return text,records

# Per-place display line breaks. The mathematical tokens remain in their order;
# only alignment structure, spacing and explicit line breaks are inserted.
def _special(package,scan,t,language):
    edits=[]
    # Visually verified arrow-label clearances are literal source-local patches.
    # Where mechanical TikZ repair changes &, the data carries both exact forms.
    label_edits=[]
    for target in json.loads((ROOT/'work/data/layout_label_clearances.json').read_text()):
        if target.get('stage','before_geometry')!='before_geometry':continue
        if (target['package'],target['scan'],target['language'])!=(package,scan,language):continue
        candidates=target.get('variants',[target])
        matches=[p for p in candidates if t.count(p['old'])==1]
        if len(matches)!=1:raise ValueError(f'Expected one exact label-clearance patch: {package} {language} scan {scan}; found {len(matches)}')
        patch=matches[0]
        t,local=_edit(t,patch['old'],patch['new'],target['reason'],kind=target.get('kind','diagram label clearance'))
        for r in local:r['id']=target['id']
        label_edits.extend(local)
    if label_edits:return t,label_edits
    if package=='LM_P062' and scan==33:
        old=r'''\arrow[r,"{u\mapsto(\dot{u},\det(u))}"]
\&
\mathrm{GP}(1,\widehat{\mathbb{Z}})'''
        new=old.replace('\\&\n',r'\&[45pt]'+'\n')
        if t.count(old)!=1:raise ValueError(f'Expected one equation28 determinant-map label: {language}')
        result,local=_edit(t,old,new,'Equation (28): add45pt only between the first two columns so the determinant-map arrow label fits between the adjacent object labels, without changing the diagram height.',kind='diagram label clearance')
        for r in local:r['id']='140-3-33-L1'
        return result,local
    if package=='LM_P052' and scan==520:
        wording='rev. galoisien de groupe ' if language=='fr' else 'Galois covering with group '
        label=r'{\text{'+wording+r'}\mathrm{Sl}(2,\mathbb{F}_2)\simeq\unsure{\mathfrak{S}_3}}'
        old=r'\arrow[r,"'+label+'"'+"']"
        new=r'\arrow[r,"'+label+'"'+"'"+r'{yshift=-8pt}]'
        if t.count(old)!=1:raise ValueError(f'Expected one equation30 Galois-covering label: {language}')
        result,local=_edit(t,old,new,'Equation (30): lower the Galois-covering arrow label by8pt so it clears both adjacent object subscripts; retain its wording, size, arrow and endpoints.',kind='diagram label clearance')
        for r in local:r['id']='140-2-520-L1'
        return result,local
    if package=='LM_C3-530-548' and scan==546:
        edits.append((r'\unsure{\textcircled{1}}',r'\unsure{\text{\textcircled{1}}}',
                      'Give the doubtful circled 1 explicit text mode inside the exponent, preserving the circled glyph and its uncertainty.',
                      'math text-mode correction'))
    if package=='LM_P034' and scan==331:
        # This note is a full phrase embedded in the diagram's last cell.
        # The unchanged \margin call remains inside an explicitly measured
        # narrow prose block, rather than an unbreakable one-line \text box.
        marker=r'\text{\margin{'
        a=t.find(marker)
        if a>=0:
            start=a+len(r'\text{');depth=1;j=a+len(marker)
            while j<len(t) and depth:
                if t[j]=='{' and (j==0 or t[j-1]!='\\'):depth+=1
                elif t[j]=='}' and (j==0 or t[j-1]!='\\'):depth-=1
                j+=1
            old=t[a:j+1]
            note=t[start:j]
            new=r'\text{\parbox[t]{105pt}{\footnotesize\noindent '+note+'}}'
            return _edit(t,old,new,'The unchanged marginal note is placed in a 105pt prose cell; its runtime renderer supplies a single rule, marginal-note label and reference, without a redundant manual heading.',kind='marginal note in diagram')
    if package=='LM_P035' and scan==348:
        a=t.find(r'$\unsure{\text{')
        if a>=0:
            e=t.find('$',a+1)
            old=t[a:e+1]
            if r'\longrightarrow' in old:
                content=old[1:-1].replace(r'\longrightarrow',r'\\\longrightarrow',1)
                new=(r'\LMmathnotice{140-2-348-M1}'+'\n'
                     +r'\begin{multline*}'+content+r'\end{multline*}')
                nt,rs=_edit(t,old,new,'The map with long alternative labels is displayed on two lines, broken before its arrow; marker M1 identifies the original running-text position.', 'inline formula moved to display')
                for r in rs:r['id']='140-2-348-M1'
                return nt,rs
    if package=='LM_P042' and scan==419:
        a=t.find(r'(30)\qquad');e=t.find(r'\]',a)
        if a>=0:
            blk=t[a:e]
            nb=blk.replace(r'(30)\qquad',r'\begin{gathered}(30)\\[3pt]')
            nb=nb.replace(r'{c@{\quad}c@{\quad}c}',r'{c@{\,}c@{\,}c}')
            nb=nb.replace('0.45\\linewidth','0.44\\linewidth').replace('0.36\\linewidth','0.44\\linewidth')
            # These two tuples are the only non-breaking material in the prose
            # columns. A breakpoint after a comma changes no mathematical token.
            nb=nb.replace(r"I',\Gamma,\theta:",r"I',\allowbreak\Gamma,\allowbreak\theta:")
            nb=nb.replace(r"I',\unsure{\Gamma^{*}|\Gamma},\theta':",r"I',\allowbreak\unsure{\Gamma^{*}|\Gamma},\allowbreak\theta':")
            nb+=r'\end{gathered}'
            return _edit(t,blk,nb,'Equation (30): put the number above two balanced prose columns, reduce the intercolumn space, and permit tuple breaks after commas.')
    if package=='LM_C3-302-320' and scan==320:
        a=t.find(r'\tag{37}');e=t.find(r'\]',a)
        if a>=0:
            blk=t[a:e]
            nb=blk.replace('}&\n\\left\\{',r'}&\\[3pt]'+'\n'+r'&\left\{')
            # The parameter definition is a second relation, placed below its
            # verbal description instead of beside it.
            nb=nb.replace('}\n\\rho=\\begin{pmatrix}',r'}\\&\rho=\begin{pmatrix}')
            return _edit(t,blk,nb,'Equation (37): stack the verbal qualification and the nested parameter definition at their clause boundaries.')
    if package=='LM_C3-416-434' and scan==425:
        edits.append((r'\unsure{\mu}\in\Gamma \mathbb G_m,\qquad',r'\unsure{\mu}\in\Gamma \mathbb G_m,\\[-2pt]','Equation (71): place the scalar constraint and determinant constraint on separate rows inside the set builder.'))
    if package=='LM_C3-644-662' and scan==653:
        edits.append((r'(4)\qquad',r'\arraycolsep=3pt (4)\qquad','Equation (4): reduce array-column padding locally from 5pt to 3pt.'))
    if package=='LM_C4-058-076' and scan==66:
        a=t.find(r'(117)\qquad');e=t.find(r'\]',a)
        if a>=0:
            blk=t[a:e]
            nb=blk.replace(r'\mathfrak{sl}(2,\mathbb F_2)\simeq',r'\mathfrak{sl}(2,\mathbb F_2)\simeq\\[-1pt]&')
            nb=nb.replace(r',\quad\begin{array}{l}',r',\\[-1pt]&\begin{array}{l}')
            nb=nb.replace(r',\quad'+'\n'+r'\begin{array}{l}',r',\\[-1pt]&'+'\n'+r'\begin{array}{l}')
            t,records=_edit(t,blk,nb,'Equation (117): place the kernel expression and subgroup explanations on continuation rows of the same brace.')
            a=t.find(r'(114)\qquad');e=t.find(r'\]',a)
            if a>=0:
                blk=t[a:e];nb=blk.replace(r'(114)\qquad',r'\begin{gathered}(114)\\[3pt]')+r'\end{gathered}'
                t,rs=_edit(t,blk,nb,'Equation (114): set the number above the diagram to release the full line width.');records+=rs
            return t,records
    if package=='LM_C4-267-280' and scan==271:
        a=t.find(r'(122)\quad');e=t.find(r'\]',a)
        if a>=0:
            blk=t[a:e]
            nb=blk.replace(r'(122)\quad',r'\begin{gathered}(122)\\[3pt]')
            nb=nb.replace(r'{\operatorname{Isom}((',r'{\begin{gathered}\operatorname{Isom}((')
            nb=nb.replace("h_x),\n(","h_x),\\\\[-1pt]\n(")
            nb=nb.replace("h'_x))}","h'_x))\\end{gathered}}")
            nb=nb.replace(r'{F(u)=\operatorname{Isom}',r'{\begin{gathered}F(u)=\\[-1pt]\operatorname{Isom}')
            nb=nb.replace(r'\unsure{]|)}}',r'\unsure{]|)}\end{gathered}}')
            nb=nb.replace(r'{G(u)=\unsure{\operatorname{Isom}}',r'{\begin{gathered}G(u)=\\[-1pt]\unsure{\operatorname{Isom}}')
            nb=nb.replace(r'\mathcal{S}}_x^{*\prime\sim})}',r'\mathcal{S}}_x^{*\prime\sim})\end{gathered}}')
            nb=nb.replace(r'\mathbb{D}|D}_x^{*\prime\sim})}',r'\mathbb{D}|D}_x^{*\prime\sim})\end{gathered}}')
            nb+=r'\end{gathered}'
            return _edit(t,blk,nb,'Equation (122): stack the equation number above the triangle, and split long object labels at argument and equality boundaries.')
    if package=='LM_P067' and scan==85:
        # Equation (8): stack the two adjacent arrays and put fixed loci on
        # separate rows. No relation or delimiter reading is changed.
        old=r'''(8)\qquad
\left\{\begin{array}{l}'''
        new=r'''\begin{gathered}
(8)\qquad
\left\{\begin{array}{l}'''
        edits.append((old,new,'Equation (8): stack the fixed-locus array and the root explanations vertically.'))
        edits += [(r'\dot\sigma_0}=\{0,2\},\quad',r'\dot\sigma_0}=\{0,2\},\\[3pt]','Equation (8): separate the three fixed-point statements.'),
                  (r'\dot\sigma_1}=\{1,-1\},\quad',r'\dot\sigma_1}=\{1,-1\},\\[3pt]','Equation (8): separate the three fixed-point statements.'),
                  (r'''\end{array}\right.
\qquad
\begin{array}{l}''',r'''\end{array}\right.\\[6pt]
\begin{array}{l}''','Equation (8): stack the explanatory array after the fixed loci.'),]
        # identify the last array of (8), before its closing display
        mat=re.search(r'(\(8\).*?)(\\end\{array\}\s*\\\])',t,re.S)
        if mat:
            oldend=mat[2]; edits.append((oldend,oldend.replace(r'\end{array}',r'\end{array}\end{gathered}',1),'Equation (8): close the stacked display.'))
        edits.append((r'''\inserted{\unsure{=\frac12-\mathbb U}},\quad''',r'''\inserted{\unsure{=\frac12-\mathbb U}},\\[3pt]''','Equation (9): give each fixed locus its own row.'))
        # Split the long second row into a continuation inside the brace.
        edits.append((r'''\mathbb P_{\mathbb C}^{1\,\dot\tau'_0}=\{x+iy\mid(x-1)^2+y^2=1\}
\inserted''',r'''\mathbb P_{\mathbb C}^{1\,\dot\tau'_0}=\{x+iy\mid(x-1)^2+y^2=1\}\\[-1pt]
\quad\inserted''','Equation (9): continue the inserted alternative description on a new row.'))
    if package=='LM_P067' and scan==88:
        edits.append((r'\quad(\mathrm{NB}\ \sigma_\infty=\rho\sigma_1\rho^{-1})',r'\\[-1pt]&&&\quad(\mathrm{NB}\ \sigma_\infty=\rho\sigma_1\rho^{-1})','Equation (22): move the NB identity to an aligned continuation row.'))
    if package=='LM_P068-069' and scan==107:
        edits.append((r'\quad d=-\frac\delta b-c',r'\\[-1pt]&\quad d=-\frac\delta b-c','Equation (84): move the solved value of d to a continuation row.'))
        # Full alignment has 4 columns; continue the long S term.
        edits.append((r'S&=\unsure{ad}\ \illegible{1}\ {-c(c+d)+ad=1-c(\unsure{c+d-b})}',r'S&=\unsure{ad}\ \illegible{1}\\[-1pt]&&&{-c(c+d)+ad=1-c(\unsure{c+d-b})}','Equation (84): continue the S relation below its initial terms.'))
        edits.append((r'P&=0,&Q&=',r'P&=0,\\ Q&=','Equation (84): give each coefficient its own aligned row.'))
        edits.append((r'R&=(c+d)^2=\frac{\delta^2}{b^2},&S&=',r'R&=(c+d)^2=\frac{\delta^2}{b^2},\\ S&=','Equation (84): give each coefficient its own aligned row.'))
        # Subsequent continuation rows belong to the same two-column alignment.
        t,records=_chain(t,edits)
        a=t.find(r'(84)\quad\left\{');e=t.find(r'\]',a)
        if a>=0:
            blk=t[a:e];nb=blk.replace('&&&','&')
            t,rs=_edit(t,blk,nb,'Equation (84): use two-column continuation rows after separating P, Q, R and S.');records+=rs
        return t,records
    if package=='LM_C3-321-339' and scan==328:
        old=r'''\[\deleted{\rho^2\sigma=}\rho^2\sigma='''
        new=r'''\[\begin{gathered}\deleted{\rho^2\sigma=}\rho^2\sigma='''
        edits.append((old,new,'Separate the two matrix equations into vertically stacked rows.'))
        # Restrict change to wide matrix display, not earlier equations.
        a=t.find(old)
        if a>=0:
            e=t.find(r'\]',a)
            blk=t[a:e+2]
            nb=blk.replace(old,new).replace(r'''\end{pmatrix},
\qquad''',r'''\end{pmatrix},\\[5pt]''').replace(r'\]',r'\end{gathered}\]')
            # The ambiguous bottom-right entry is itself overlong. Break at
            # the alternative bar; the | remains printed at continuation start.
            target=r'\unsure{-\unsure{w|\omega}(\unsure{w|\omega}^2+2\unsure{v|\nu})+\unsure{v|\nu}-\unsure{w|\omega}^2|-\unsure{w|\omega}(\unsure{w|\omega}^2+2\unsure{v|\nu})+\unsure{v|\nu}+\unsure{w|\omega}^2}'
            replacement=r'\unsure{\begin{gathered}-\unsure{w|\omega}(\unsure{w|\omega}^2+2\unsure{v|\nu})+\unsure{v|\nu}-\unsure{w|\omega}^2\\[-1pt]|-\unsure{w|\omega}(\unsure{w|\omega}^2+2\unsure{v|\nu})+\unsure{v|\nu}+\unsure{w|\omega}^2\end{gathered}}'
            nb=nb.replace(target,replacement)
            return _edit(t,blk,nb,'The ambiguous matrix entry is set on two lines at its alternative separator; the second matrix equation follows on another row.')
    if package=='LM_C3-321-339' and scan==329:
        a=t.find(r'(27\mathrm{bis})')
        if a>=0:
            e=t.find(r'\]',a);blk=t[a:e]
            nb=r'\begin{gathered}'+blk
            nb=nb.replace(r'''\quad
\left(\Rightarrow''',r'''\\[4pt]
\left(\Rightarrow''')+r'\end{gathered}'
            return _edit(t,blk,nb,'Equation (27bis): place the parenthetical consequence on a separate line.')
    if package=='LM_C3-549-567' and scan==555:
        edits.append((r'\Longleftrightarrow\mathcal G^+\text{ is }',r'\\&\Longleftrightarrow\mathcal G^+\text{ is }','Equation (39): break the equivalence chain before its group-theoretic characterization.'))
        edits.append((r'\Longleftrightarrow\mathcal G^+\text{ est }',r'\\&\Longleftrightarrow\mathcal G^+\text{ est }','Équation (39) : poursuivre la chaîne d’équivalences sur une nouvelle ligne.'))
    if package=='LM_C3-606-624' and scan==606:
        a=t.find(r'\tag{103}');e=t.find(r'\]',a)
        if a>=0:
            blk=t[a:e];nb=blk.replace(r'\tag{103}',r'\tag{103}\begin{gathered}').replace(r'''\qquad
\left(-d''',r'''\\[3pt]
\left(-d''')+r'\end{gathered}'
            return _edit(t,blk,nb,'Equation (103): place the parenthetical congruence on a separate line.')
    if package=='LM_C3-606-624' and scan==621:
        # Keep long added explanatory text in a separate row of the same display.
        edits.append((r'''(1)\qquad Z_{\rho,\sigma}\simeq\mathcal M(0).L_0^{\mathcal G}''',r'''\begin{gathered}(1)\qquad Z_{\rho,\sigma}\simeq\mathcal M(0).L_0^{\mathcal G}''','Equation (1): set the added explanatory parenthesis below the identity.'))
        edits.append((r'''\inserted{=\mathcal M[0]}\ \deleted{\illegible{1}}\ \inserted{''',r'''\inserted{=\mathcal M[0]}\ \deleted{\illegible{1}}\\[3pt]\inserted{''','Equation (1): break before the long explanatory insertion.'))
        mat=re.search(r'(\(1\).*?)(\\\])',t,re.S)
        if mat:
            full=mat[0]
            for old,new,_,*x in edits:full=full.replace(old,new)
            if r'\begin{gathered}' in full:
                full=full[:-2]+r'\end{gathered}\]'
                return _edit(t,mat[0],full,'Equation (1): set the added explanatory parenthesis below the identity.')
    if package=='LM_C3-644-662' and scan==658:
        a=t.find(r'(18)\qquad');e=t.find(r'\]',a)
        if a>=0:
            blk=t[a:e];nb=r'\begin{gathered}'+blk.replace(r'''\qquad
\left(''',r'''\\[3pt]
\left(''')+r'\end{gathered}'
            t,r=_edit(t,blk,nb,'Equation (18): set the explanatory parenthesis on a separate line.')
            a=t.find(r'(24)\qquad');e=t.find(r'\]',a)
            if a>=0:
                blk=t[a:e];nb=r'\begin{gathered}'+blk.replace(r'\right.'+'\n'+r'\qquad',r'\right.\\[3pt]')+r'\end{gathered}'
                t,rs=_edit(t,blk,nb,'Equation (24): place the parenthetical description of inverse images below the three-column array.');r+=rs
            return t,r
    if package=='LM_C3-644-662' and scan==659:
        edits.append((r'''\gamma'_{\rho,\sigma}=\operatorname{Ker}\varepsilon_{3\gamma},\
\gamma''',r'''\gamma'_{\rho,\sigma}=\operatorname{Ker}\varepsilon_{3\gamma},\\[2pt]
\gamma''','Equation (24): set the definitions on separate rows.'))
        edits.append((r'''\gamma''_{\rho,\sigma}=\operatorname{Ker}\varepsilon_{2\gamma},\
\gamma''',r'''\gamma''_{\rho,\sigma}=\operatorname{Ker}\varepsilon_{2\gamma},\\[2pt]
\gamma''','Equation (24): set the definitions on separate rows.'))
        edits.append((r'''\gamma'''+'\x27'+r'''_{\rho,\sigma}=\operatorname{Ker}\varepsilon_{2\gamma}\varepsilon_{3\gamma},\
\gamma''',r'''\gamma'''+'\x27'+r'''_{\rho,\sigma}=\operatorname{Ker}\varepsilon_{2\gamma}\varepsilon_{3\gamma},\\[2pt]
\gamma''','Equation (24): set the definitions on separate rows.'))
    return _chain(t,edits)


def repair_after_geometry(text,package,language):
    """Replay the explicitly accepted literal refinements after local geometry.

    Targets are fixed source spans, shared by all three forms; no runtime
    fitting, generic label movement or suppression of overflow is involved.
    """
    records=[];present={n for n,a,b in _scan_ranges(text)}
    for target in json.loads((ROOT/'work/data/layout_label_clearances.json').read_text()):
        if target.get('stage')!='after_geometry':continue
        if target['package']!=package or target['language']!=language or target['scan'] not in present:continue
        def fix(t):
            matches=[p for p in target['variants'] if t.count(p['old'])==1]
            if len(matches)!=1:raise ValueError(f'Expected one exact post-geometry patch: {package} {language} {target["id"]}; found {len(matches)}')
            patch=matches[0]
            result,local=_edit(t,patch['old'],patch['new'],target['reason'],kind=target['kind'])
            for r in local:r['id']=target['id']
            return result,local
        text=_replace_scan(text,target['scan'],fix,records,package,language)
    return text,records


def repair_tag_bindings(text,package,language):
    """Replay only the explicitly inventoried source-local pagination pairs."""
    path=ROOT/'work/data/layout_tag_bindings.json'
    if not path.exists():return text,[]
    records=[];present={n for n,a,b in _scan_ranges(text)}
    for target in json.loads(path.read_text()):
        if target['package']!=package or target['language']!=language or target['scan'] not in present:continue
        def fix(t):
            matches=[p for p in target['variants'] if t.count(p['old'])==1]
            if len(matches)!=1:raise ValueError(f'Expected one exact pagination binding: {package} {language} {target["id"]}; found {len(matches)}')
            p=matches[0]
            result,local=_edit(t,p['old'],p['new'],target['reason'],kind=target['kind'])
            for r in local:r['id']=target['id']
            return result,local
        text=_replace_scan(text,target['scan'],fix,records,package,language)
    return text,records


def repair(text,package,language,*,include_pagination=True):
    """Return (repaired_text, exact_change_records). Does not write sources.

    The offline exact-inventory builder may request the geometry-only view;
    normal assembly always applies every recorded pagination binding too.
    """
    initial=text;records=[]
    for scan,_,_ in list(_scan_ranges(text)):
        text=_replace_scan(text,scan,lambda t:_special(package,scan,t,language),records,package,language)
    datafile=ROOT/'work/data/layout_diagram_targets.json'
    if datafile.exists():
        targets=json.loads(datafile.read_text())
        for target in targets:
            if target['package']!=package:continue
            scan=target['scan'];typ=target['environment'];ordinal=target['ordinal']
            def fix(t):
                pattern=r'\\begin\{'+typ+r'\}.*?\\end\{'+typ+r'\}'
                ms=list(re.finditer(pattern,t,re.S))
                if ordinal>len(ms):return t,[]
                m=ms[ordinal-1];old=m[0]
                if typ=='tikzcd':
                    fontsize=target.get('font_size',10);colsep=target.get('column_sep',9);rowsep=target.get('row_sep',14)
                    new=_compact(old,fontsize=fontsize,colsep=colsep,rowsep=rowsep)
                    why=f'Explicit local diagram spacing ({colsep}pt columns, {rowsep}pt rows) and {fontsize}pt type; original 11pt type is retained elsewhere.'
                    if package=='LM_C3-435-453' and scan==446 and ordinal==1:
                        before=r'\& \&' if r'\& \&' in new else '& &'
                        after=r'\&[18pt] \&' if before.startswith('\\') else '&[18pt] &'
                        if new.count(before)!=1:raise ValueError(f'Missing scan446 central-gap anchor: {language}')
                        new=new.replace(before,after)
                        labels=re.findall(r'(\\arrow\[rr,hook,"[^\n]+"\x27)(\])',new)
                        if len(labels)!=2:raise ValueError(f'Missing scan446 quotient labels: {language}')
                        for start,end in labels:new=new.replace(start+end,start+r'{yshift=-3pt}'+end)
                        why+=' Equation (133): add 18pt only to the central column gap and lower both unchanged quotient labels by 3pt so they clear the isomorphism signs and lower arrowhead barbs; preserve the diagram height.'
                    if package=='LM_C3-606-624' and scan==619 and ordinal==2:
                        before=r'\&N^*_{\rho}/\{\pm1\}' if r'\&N^*_{\rho}/\{\pm1\}' in new else r'&N^*_{\rho}/\{\pm1\}'
                        after=before.replace('&N','&[60pt]N')
                        if new.count(before)!=1:raise ValueError(f'Missing scan619 final-column anchor: {language}')
                        new=new.replace(before,after)
                        why+=' Equation (144): add 60pt only before the final column, giving the unchanged homomorphism (130) label clear horizontal space between the quotient objects without increasing the matrix height.'
                    if package=='LM_C3-549-567' and scan==561 and ordinal==1:
                        if new.count(r'\mathrm{II}')!=1:raise ValueError(f'Missing scan561 region-II label: {language}')
                        new=new.replace(r'\mathrm{II}',r'|[yshift=-3pt]| \mathrm{II}')
                        labels=[(r'"{\varepsilon_{\gamma,\rho}=\varepsilon'+"'"+r'_\gamma}"',r'{pos=.75}'),
                                (r'"{\varepsilon_{\gamma,\sigma}=\varepsilon_\gamma}"'+"'",r'{pos=.75}'),
                                (r'"\unsure{\mathrm{pr}}"',r'{pos=.25}')]
                        for before,option in labels:
                            if new.count(before)!=1:raise ValueError(f'Missing scan561 crossing label: {language}: {before}')
                            new=new.replace(before,before+option)
                        why+=' Lower the region label II by 3pt inside the same triangular region to clear the dashed and dotted boundaries.'
                    if package=='LM_C3-549-567' and scan==557 and ordinal==1:
                        local=[
                            (r'\arrow[dddrr,dashed,"\delta_Z"]',r'\arrow[dddrr,dashed,"\delta_Z"{pos=.17,xshift=2pt}]'),
                            (r'\arrow[ddr,dashed,"\delta_\rho"]',r'\arrow[ddr,dashed,"\delta_\rho"{pos=.34,xshift=3pt}]'),
                            (r'\arrow[dr,dashed,"\delta_\sigma"]',r'\arrow[dr,dashed,"\delta_\sigma"{pos=.55,xshift=5pt}]'),
                            (r'\arrow[uur,"{(\chi_\gamma,\varepsilon_{\gamma,\rho},\varepsilon_{\gamma,\sigma})}"]',r'\arrow[uur,"{(\chi_\gamma,\varepsilon_{\gamma,\rho},\varepsilon_{\gamma,\sigma})}"'+"'"+r'{pos=.6,xshift=8pt}]'),
                        ]
                        for before,after in local:
                            if new.count(before)!=1:raise ValueError(f'Missing scan557 map-label anchor: {language}: {before}')
                            new=new.replace(before,after)
                        why+=' Equation (45): separate the three convergent dashed-map labels at distinct positions and put the unchanged character-tuple label outside its ascending arrow; matrix dimensions, arrow styles and endpoints remain unchanged.'
                    if package=='LM_C3-625-643' and scan==637 and ordinal==1:
                        before='start anchor=north west,end anchor=south west'
                        if new.count(before)!=1:raise ValueError(f'Missing scan637 long diagonal: {language}')
                        new=new.replace(before,before+',bend left=25')
                        for before in [r'\mathcal{M}'+"'''"+r'(-\bar j)\times\mu\arrow[rr,hook,"2"]',r'\mathcal{N}_{\rho}^{?}\arrow[rr,hook,"3"]']:
                            if new.count(before)!=1:raise ValueError(f'Missing scan637 crossing degree label: {language}: {before}')
                            new=new.replace(before,before[:-1]+r'{pos=.75}]')
                        why+=' Equation (37): bend the long diagonal from 1 to the upper-left object by 25 degrees so it passes through the gap below the middle-left object, and put both middle-row horizontal degree labels at position 0.75 to clear the crossing verticals; retain every endpoint and the diagram height.'
                    if package=='LM_C1-001-019' and scan==10 and ordinal==1:
                        word='sous-groupe' if language=='fr' else 'subgroup'
                        local=[
                            (r'\& \begin{gathered}\text{'+word+'}',r'\& |[yshift=100pt]| \begin{gathered}\text{'+word+'}'),
                            (r'\Pi_{0,3}^{D} \arrow[r] \arrow[ddrr]',r'\Pi_{0,3}^{D} \arrow[r] \arrow[ddrr,bend right=25]'),
                            (r'\arrow[ddrrr]',r'\arrow[ddrrr,bend left=15]'),
                            (r'\widetilde{\mathrm S\ell}(2,\mathbb Z) \arrow[ul] \arrow[rrrr]',r'\widetilde{\mathrm S\ell}(2,\mathbb Z) \arrow[ul] \arrow[rrrr,bend left=12]'),
                            (r'\arrow[from=2-4,to=3-3,phantom,"\mathrm{Cart}"{description}]',r'\arrow[from=2-4,to=3-3,phantom,"\mathrm{Cart}"{description,xshift=20pt}]'),
                        ]
                        for before,after in local:
                            if new.count(before)!=1:raise ValueError(f'Missing scan10 diagram routing anchor: {language}: {before}')
                            new=new.replace(before,after)
                        why+=' The five-line subgroup annotation is raised locally by 100pt, three arrows are curved with their original endpoints, and one Cart label is shifted 20pt to keep annotation and object labels clear of strokes.'
                    if package=='LM_C1-020-037' and scan==20 and ordinal==1:
                        lower='cart' if language=='fr' else 'cartesian'
                        capital='Cart' if language=='fr' else 'Cartesian'
                        canonical='can' if language=='fr' else 'canonical'
                        local=[
                            (r'\arrow[d,phantom,"\text{\uline{'+capital+r'}}"'+"'"+r'{pos=.25,xshift=-3em}]',r'\arrow[d,phantom,"\text{\uline{'+capital+r'}}"'+"'"+r'{pos=.25,xshift=-3.5em,yshift=4pt}]'),
                            (r'\arrow[dr,phantom,"\text{\uline{'+lower+r'}}"{description,xshift=-1.5em,yshift=.5em}]',r'\arrow[dr,phantom,"\text{\uline{'+lower+r'}}"{description,xshift=-1.5em,yshift=-.5em}]'),
                            (r'\mathbb Z/4\mathbb Z\arrow[r,leftrightarrow,"\text{'+canonical+r'}"]',r'\mathbb Z/4\mathbb Z\arrow[r,leftrightarrow,"\text{'+canonical+r'}"'+"']"),
                        ]
                        for before,after in local:
                            if new.count(before)!=1:raise ValueError(f'Missing scan20 diagram label anchor: {language}: {before}')
                            new=new.replace(before,after)
                        why+=' In the lower-right triangle, Cartesian labels are separated from the diagonal labels and the bottom canonical label is placed below its arrow; endpoints and wording stay unchanged.'
                else:
                    # A physical sketch is scaled only here, by a recorded fixed
                    # factor, without automatic fitting; never below 70%.
                    new=r'\scalebox{0.90}{'+old+'}'
                    why='This physical drawing is reduced locally to 90% of its original dimensions.'
                if new==old:return t,[]
                if target.get('landscape'):
                    # Both exceptional diagrams stand directly inside a
                    # \diagram wrapper. Preserve a visible anchor at the
                    # preceding line before landscape's forced page break.
                    before=t[:m.start()]
                    prefix=re.search(r'\\diagram\{([^{}]*)$',before)
                    after=re.match(r'\s*\}',t[m.end():])
                    if not prefix or not after:
                        raise ValueError('Landscape target is not a direct diagram wrapper')
                    start=prefix.start();end=m.end()+after.end()
                    old=t[start:end]
                    ident=f"{target['cote']}-{scan}-D{ordinal}"
                    new=(r'\LMlayoutnotice{'+ident+'}\n'+r'\begin{landscape}'+'\n'
                         +r'\begin{center}'+prefix[1]+new+r'\end{center}'+'\n'+r'\end{landscape}')
                    why=f'Diagram exceeds the portrait measure after local spacing repair; a landscape page preserves the diagram at {fontsize}pt with a marked reference at its original position.'
                    if package=='LM_C3-549-567' and scan==561:
                        why+=' The region label II is lowered by 3pt inside the same triangular region; both right-hand epsilon labels are placed at position 0.75 and the uncertain projection label at position 0.25 along their own arrows to clear crossing verticals. Matrix dimensions, routes and endpoints remain unchanged.'
                    return t[:start]+new+t[end:],[dict(offset=start,old=old,new=new,kind='landscape diagram',reason=why,id=ident)]
                return t[:m.start()]+new+t[m.end():],[dict(offset=m.start(),old=old,new=new,kind='diagram spacing',reason=why)]
            text=_replace_scan(text,scan,fix,records,package,language)
    counts={}
    for r in records:
        key=r['scan'];counts[key]=counts.get(key,0)+1
        r.setdefault('id',f"{r['cote']}-{key}-T{counts[key]}")
    if package=='LM_C1-001-019':
        def projection_label(t):
            old=r'\arrow[rr,"\mathrm{pr}_1"]'
            new=r'\arrow[rr,"\mathrm{pr}_1"{pos=.8}]'
            if t.count(old)!=1:raise ValueError(f'Missing scan10 branching projection label: {language}')
            result,local=_edit(t,old,new,'In the second large branching diagram, move the first-projection label to position 0.8 along its horizontal arrow so the diagonal to E passes clear of it; retain all endpoints, matrix dimensions and type size.',kind='diagram label clearance')
            for r in local:r['id']='140-1-10-L1'
            return result,local
        text=_replace_scan(text,10,projection_label,records,package,language)
    text,empty_records=repair_empty_cells(text,package,language)
    records+=empty_records
    text,page_records=repair_pagefigures(text,package,language)
    records+=page_records
    text,pair_records=repair_paired_margins(text,package,language)
    records+=pair_records
    text,post_records=repair_after_geometry(text,package,language)
    records+=post_records
    if include_pagination:
        text,tag_records=repair_tag_bindings(text,package,language)
        records+=tag_records
    if records or any(x['package']==package and x['language']==language for x in json.loads((ROOT/'work/data/layout_expected_matches.json').read_text())):
        _audit_records(initial,text,records,package,language,check_width_counts=include_pagination)
    return text,records

if __name__=='__main__':
    import csv
    output=ROOT/'work/layout_repaired';allrecords=[]
    for lang,folder,suf in [('fr','fr/texts',''),('en','en/packages','_en')]:
        (output/lang).mkdir(parents=True,exist_ok=True)
        for package in COVERAGE:
            t=(ROOT/'sources'/folder/(package+suf+'.tex')).read_text()
            new,rs=repair(t,package,lang);allrecords+=rs
            (output/lang/(package+'.tex')).write_text(new)
    (ROOT/'work/data/layout_repairs_applied.json').write_text(json.dumps(allrecords,ensure_ascii=False,indent=2))
    keys=['id','language','package','cote','scan','source_path','source_line','source_offset_start','source_offset_end','source_byte_start','source_byte_end','expected_match_count','kind','reason','source_old','old','new']
    with (ROOT/'work/records/LAYOUT_REPAIR_DETAILS.tsv').open('w') as f:
        w=csv.DictWriter(f,keys,delimiter='\t');w.writeheader();w.writerows(allrecords)
    print('Local changes',len(allrecords))
