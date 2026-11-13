r"""Give each literal source mark a stable identity before TeX expansion.

Instrumentation is lossless: deinstrument(instrument(body)[0]) == body.
Nested marks are individually identified. A literal mark re-executed during
amsmath's measurement or mathchoice trials retains its identity instead of
creating fictitious unlinked source occurrences. No text or notation changes.
"""
from __future__ import annotations
import bisect, re
from editorial import blank_comments, brace_end

NAMES=('unsure','illegible','LMdoubtcopy','LMcancelledDoubts','LMuncertaindeletion','scanpage','margin','mspage')
PAT=re.compile(r'\\('+'|'.join(NAMES)+r')\b\s*\{')
WRAPPER=re.compile(r'\\LMsourceMark\b\s*\{')


def _contexts(body,mask):
    # Package boundaries are intentional build comments, never executed TeX.
    packages=[(m.start(),m[1]) for m in re.finditer(r'^% BEGIN PACKAGE ([A-Za-z0-9_-]+)\s*$',body,re.M)]
    cotes=[(m.start(),m[1]) for m in re.finditer(r'\\LMcote\{([^}]*)\}',mask)]
    scans=[(m.start(),m[1]) for m in re.finditer(r'\\scanpage\{([^}]*)\}',mask)]
    def before(rows,pos,default=''):
        i=bisect.bisect_right(rows,(pos,chr(0x10ffff)))-1
        return rows[i][1] if i>=0 else default
    return lambda pos:(before(packages,pos),before(cotes,pos),before(scans,pos))


def instrument(body):
    """Return (instrumented body, mark records) in literal source order."""
    mask=blank_comments(body)
    if WRAPPER.search(mask):raise ValueError('Body is already instrumented')
    ctx=_contexts(body,mask);marks=[];stack=[];newlines=[-1]+[i for i,c in enumerate(body) if c=='\n']
    for n,m in enumerate(PAT.finditer(mask),1):
        end=brace_end(body,m.end()-1)
        while stack and m.start()>=stack[-1]['end']:stack.pop()
        package,cote,scan=ctx(m.start());identifier=f'M{n:06d}'
        rec={'id':identifier,'kind':m[1],'package':package,'cote':cote,'scan':scan,
             'source_line':bisect.bisect_right(newlines,m.start()),
             'body_line':bisect.bisect_right(newlines,m.start()),
             'start':m.start(),'end':end,'parent_id':stack[-1]['id'] if stack else '',
             'argument':body[m.end():end-1]}
        marks.append(rec);stack.append(rec)
    # Nested interval events avoid re-scanning or duplicating the body.
    starts={};ends={}
    for r in marks:
        starts.setdefault(r['start'],[]).append(r)
        ends.setdefault(r['end'],[]).append(r)
    positions=sorted(set(starts)|set(ends));out=[];last=0
    for pos in positions:
        out.append(body[last:pos])
        # Close inner wrappers before opening a following, nonnested mark.
        for r in sorted(ends.get(pos,[]),key=lambda x:x['start'],reverse=True):out.append('}')
        for r in sorted(starts.get(pos,[]),key=lambda x:x['end'],reverse=True):out.append(r'\LMsourceMark{'+r['id']+'}{')
        last=pos
    out.append(body[last:]);result=''.join(out)
    if deinstrument(result)!=body:raise AssertionError('Mark instrumentation failed its exact round trip')
    return result,marks


def deinstrument(body):
    """Remove only LMsourceMark wrappers, preserving enclosed bytes exactly."""
    mask=blank_comments(body);events=[]
    for m in WRAPPER.finditer(mask):
        endid=brace_end(body,m.end()-1);pos=endid
        while pos<len(body) and body[pos].isspace():pos+=1
        if pos==len(body) or body[pos]!='{':raise ValueError('Malformed LMsourceMark wrapper')
        end=brace_end(body,pos)
        events.extend([(m.start(),pos+1),(end-1,end)])
    events.sort();out=[];last=0
    for a,b in events:
        if a<last:raise ValueError('Overlapping instrumentation delimiters')
        out.append(body[last:a]);last=b
    out.append(body[last:]);return ''.join(out)

inverse=deinstrument

if __name__=='__main__':
    sample=r'''% BEGIN PACKAGE LM_TEST
\LMcote{140-2}
\scanpage{1}
\unsure{A \illegible{2} \unsure{B}}\LMcancelledDoubts{\(\unsure{C}\)}
% \unsure{comment is not a mark}
\scanpage{2} \LMuncertaindeletion{140-2-s002-D001}
'''
    result,records=instrument(sample)
    assert deinstrument(result)==sample
    assert len(records)==8 and records[3]['parent_id']==records[1]['id']
    print('Nested/comment/scan instrumentation round trip PASS; 8 literal marks.')
