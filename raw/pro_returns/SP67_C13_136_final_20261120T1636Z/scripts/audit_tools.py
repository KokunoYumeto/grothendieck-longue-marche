from workflow import *

def finish(n, *, replacements=(), changes=(), note, doubts=None, extra_hand=(), extra_notation=()):
    """Record the sole reader's second image reading; never infer readings."""
    assert not re.search(rf'^scan {n} audited ', (ROOT/'progress.log').read_text(), re.M)
    p=ROOT/f'records/scan{n}.py'
    r=ast.literal_eval(p.read_text())
    if doubts is not None:
        for d in doubts: _check_doubt(d)
        r['unresolved']=list(doubts)
    assert all(isinstance(x,dict) for x in r['unresolved']), 'Sole reader must assign confidence explicitly'
    r['hand']+=list(extra_hand)
    r['notation']+=list(extra_notation)
    p.write_text(pprint.pformat(r,sort_dicts=False,width=120)+'\n')
    t=(ROOT/f'pages/136_scan{n}.tex').read_text()
    for pair in replacements:
        t=repl(t,*pair)
    audit(n,text=t,changes=changes,note=note)
    print('AUDITED',n,'additional doubts',len(r['unresolved']),'changes',len(changes))

def _check_doubt(d):
    assert isinstance(d,dict) and d['confidence'] in ('low','medium','high')

