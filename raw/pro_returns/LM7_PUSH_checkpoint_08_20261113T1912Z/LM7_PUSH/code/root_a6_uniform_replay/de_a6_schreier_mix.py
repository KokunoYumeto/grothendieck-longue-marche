#!/usr/bin/env python3
"""Supply exact product words inside an already certified subgroup.

The deterministic mixtures are only a search aid.  The later certificate
proves its own exact generated derived image, and every supplied word is
retained.  Equality with a containing certified subgroup is used only
after an explicit order and source-word comparison.
"""
from pathlib import Path
import argparse,json
import numpy as np
from de_a6_schreier_certificate import read_certificate,verify_words

def main():
    parser=argparse.ArgumentParser();parser.add_argument('certificate')
    parser.add_argument('output_prefix');parser.add_argument('--count',type=int,default=10)
    args=parser.parse_args();d=read_certificate(args.certificate);verify_words(d)
    rng=np.random.default_rng(20261113);strong=d['strong'];inverse=np.argsort(strong,axis=1).astype(np.uint16)
    images=[];words=[]
    for _ in range(args.count):
        indices=rng.permutation(len(strong));signs=rng.integers(0,2,len(strong));word=[]
        p=np.arange(d['degree'],dtype=np.uint16)
        for i,sign in zip(indices,signs):
            p=(strong[i] if sign else inverse[i])[p];word.append((int(i)+1)*(1 if sign else -1))
        images.append(p);words.append(word)
    prefix=Path(args.output_prefix);images=np.array(images,dtype=np.uint16)
    with Path(str(prefix)+'.input').open('w') as out:
        out.write(f'{d["degree"]} {len(images)}\n')
        for row in images:out.write(' '.join(map(str,row))+'\n')
    np.savez_compressed(str(prefix)+'_input.npz',generators=images)
    metadata={'status':'PASS_WORD_INPUTS','source_certificate':str(Path(args.certificate)),
              'source_certificate_is_derived':d['derived'],
              'one_based_signed_strong_generator_words':words,
              'source_word_nodes':d['words'].tolist(),'degree':d['degree'],
              'all_source_word_DAG_values_independently_replayed':True,
              'no_generation_or_perfectness_claim_from_mixtures':True}
    Path(str(prefix)+'_input.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps({k:v for k,v in metadata.items() if k not in
        ('one_based_signed_strong_generator_words','source_word_nodes')},indent=2))

if __name__=='__main__':main()
