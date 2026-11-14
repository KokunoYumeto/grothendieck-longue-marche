#!/usr/bin/env python3
"""Frozen independent replay package for the exact cover and target model."""
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent


def main():
    names=[]
    for stem in ('de_a6_triple_cover','de_a6_triple_model'):
        names.extend(stem+suffix for suffix in ('.py','.json','.npz','.out','.err'))
    names+=['de_ferrari_a6_kernels.npz','de_ferrari_a6_model.py',
            'de_ferrari_a6_model.npz','de_ferrari_two_model.py','de_ferrari_mod9_lift.py',
            'de_a6_triple_models_manifest.py']
    records={name:{'sha256':sha256((HERE/name).read_bytes()).hexdigest(),
                   'bytes':(HERE/name).stat().st_size} for name in sorted(names)}
    info={'status':'FROZEN_EXACT_COVER_AND_TARGET_MODELS','files':len(records),
          'bytes':sum(v['bytes'] for v in records.values()),'records':records,
          'sequential_replay':['python de_a6_triple_cover.py','python de_a6_triple_model.py'],
          'comparison':'JSON exact except seconds; every NPZ key, shape, dtype and value exact',
          'all_imported_legacy_main_entrypoints_unexecuted':True,
          'no_source_or_CM_fibre_conclusion_in_this_package':True}
    (HERE/'de_a6_triple_models_manifest.json').write_text(json.dumps(info,indent=2)+'\n')
    print(json.dumps({k:v for k,v in info.items() if k!='records'},indent=2))


if __name__=='__main__':main()
