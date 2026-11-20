"""Record a page only after the primary reader has visually reread it."""
import sys
from workflow import *
def record(cote,scan,summary):
    assert all((WORK/'pages'/f'{c}_scan{s}.tex').exists() for c,s in ORDER)
    previous=readrows('visual_audit.tsv')
    assert (cote,scan)==ORDER[len(previous)], 'Second reading must follow page order'
    HEADERS['visual_audit.tsv']=['cote','scan','audited_UTC','reader','findings']
    stamp=now()
    add('visual_audit.tsv',[dict(cote=cote,scan=scan,audited_UTC=stamp,reader='GPT-6 Astra Pro; primary reader',findings=summary)])
    log(f'scan {scan} audited {stamp} cote {cote}')
    print('Audited '+cote+'/'+scan)
if __name__=='__main__':record(sys.argv[1],sys.argv[2],sys.argv[3])
