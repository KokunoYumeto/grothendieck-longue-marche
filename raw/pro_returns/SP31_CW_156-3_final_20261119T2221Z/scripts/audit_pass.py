"""Root's image-audit ledger. Dispositions supplied explicitly, never inferred."""
from work import *

LEDGER=OUT/'audit/source_C_unsure.tsv'
def show(n):
    rs=list(csv.DictReader(LEDGER.open(),delimiter='\t'))
    for r in rs:
        if int(r['scan'])==n:
            print(r['occurrence_id'], 'L'+r['source_line'], r['source_argument'], '=>',r['final_aligned_text'].replace('\n',' '),'| doubts:',r['final_unsure_arguments'])
    print('CROPS:', ' '.join(p.name for p in sorted((OUT/'crops').glob(f'{n:03}*'))))

def review(n,groups,note):
    with LEDGER.open() as f:
        rd=csv.DictReader(f,delimiter='\t'); fields=rd.fieldnames;rs=list(rd)
    selected={int(r['source_occurrence']):r for r in rs if int(r['scan'])==n}
    seen=set();stamp=utc()
    for ids,disposition,crops,reason in groups:
        for i in ids:
            if i in seen:raise ValueError(('duplicate',n,i))
            if i not in selected:raise ValueError(('absent',n,i))
            seen.add(i);r=selected[i]
            for p in crops.split('; '):
                if not (OUT/'crops'/p).is_file():raise ValueError(('missing crop',p))
            r.update(ink_disposition=disposition,crop_links='; '.join('crops/'+p for p in crops.split('; ')),reviewed_by='GPT-6 Astra Pro / root; effort not exposed',reviewed_utc=stamp,review_note=reason,alignment_recheck_required='')
    if seen!=set(selected):raise ValueError(('incomplete review',n,sorted(set(selected)-seen)))
    with LEDGER.open('w') as f:
        wr=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');wr.writeheader();wr.writerows(rs)
    with (OUT/'progress.log').open('a') as f:f.write(f'scan {n:03} audited {stamp}\n')
    with (OUT/'audit/image_audit.md').open('a') as f:f.write(f'\n## Scan {n:03} — {stamp}\n\n{note}\n\nEvery source-C doubt occurrence on this page is separately dispositioned in source_C_unsure.tsv.\n')
    print('audited',n,len(seen),'source-C doubts',stamp)

if __name__=='__main__':
    import sys
    show(int(sys.argv[1]))
