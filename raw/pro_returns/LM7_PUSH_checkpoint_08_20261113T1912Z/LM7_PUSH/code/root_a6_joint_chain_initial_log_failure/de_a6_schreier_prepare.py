#!/usr/bin/env python3
"""Prepare exact subgroup inputs from saved literal Schreier certificates.

Every input is linked to its earlier word DAG and verified before export.
Selecting generators skips discovery only: the later greedy certificate
still sifts every supplied generator and the derived run keeps every
pair commutator and the full normal closure.
"""
from pathlib import Path
import argparse,json,math
import numpy as np
from de_a6_schreier_certificate import read_certificate,verify_words

def permutation_order(p):
    seen=np.zeros(len(p),dtype=bool);order=1
    for i in range(len(p)):
        if seen[i]:continue
        j=i;length=0
        while not seen[j]:seen[j]=True;length+=1;j=int(p[j])
        order=math.lcm(order,length)
    return order

def main():
    parser=argparse.ArgumentParser();parser.add_argument('certificate')
    parser.add_argument('output_prefix');parser.add_argument('--selected-log')
    args=parser.parse_args();d=read_certificate(args.certificate);verify_words(d)
    if args.selected_log:
        log=json.loads(Path(args.selected_log).read_text().splitlines()[-1])
        indices=log['selected_original_indices'];assert indices
        arrays=d['original'][indices];kind='original';nodes=None
    else:
        orders=[permutation_order(p) for p in d['strong']]
        indices=sorted(range(len(orders)),key=lambda i:orders[i],reverse=True)
        arrays=d['strong'][indices];kind='strong';nodes=d['words'][indices].tolist()
    prefix=Path(args.output_prefix)
    with Path(str(prefix)+'.input').open('w') as out:
        out.write(f'{d["degree"]} {len(arrays)}\n')
        for row in arrays:out.write(' '.join(map(str,row))+'\n')
    np.savez_compressed(str(prefix)+'_input.npz',generators=arrays,
                        source_indices=np.array(indices,dtype=np.int64))
    metadata={'status':'PASS','source_certificate':str(Path(args.certificate)),
              'source_generator_kind':kind,'source_indices':indices,
              'source_word_nodes':nodes,'source_certificate_derived':d['derived'],
              'all_source_words_independently_replayed':True,
              'degree':d['degree'],'generator_count':len(arrays),
              'generator_orders':[permutation_order(p) for p in arrays]}
    Path(str(prefix)+'_input.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps(metadata,indent=2))

if __name__=='__main__':main()
