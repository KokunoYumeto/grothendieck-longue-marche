#!/usr/bin/env python3
"""Build the exact ORIGINAL-source Hopf-torsion test modulo |G|.

The source presentation, all collector words, and all source-identity rows
are unchanged. Only the linear reduction is in Z/|G|. Power-word correction
rows are omitted; the target and every allowed correction lie in Hopf torsion.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

BASE = Path(__file__).parent


def write_routine():
    text = (BASE / 'pbc_hermite_precollected_witness.g').read_text()
    text = text.replace('PBC_HermitePrecollectedWitness', 'PBC_HermiteModularWitness')
    text = text.replace('baseCommute,zz,hh;', 'baseCommute,zz,hh,modulus;')
    text = text.replace('orders:=data.orders;n:=Length(orders);m:=n*(n+1)/2;',
                        'orders:=data.orders;n:=Length(orders);m:=n*(n+1)/2;modulus:=data.modulus;')
    text = text.replace('n,\",\",m,\"]\\n\");', 'n,\",\",m,\",\",modulus,\"]\\n\");')
    # Do not reduce the input's leading N to zero: that representative is
    # needed by the Euclidean step which computes gcd(c,N). All subsequent
    # nonleading coefficients are reduced modulo N, preventing coefficient
    # growth. The entire proof DAG is an identity modulo N.
    old = 'acc[idx]:=acc[idx]-q*row[ii+1];if acc[idx]<>0'
    new = 'acc[idx]:=(acc[idx]-q*row[ii+1]) mod modulus;if acc[idx]<>0'
    assert old in text
    text = text.replace(old, new)
    old = 'for i in [1..Length(extras)] do insert(extras[i],[i,1],newLeaf("extra",[i],extras[i]));od;'
    new = '''# N times each ORIGINAL tail is zero in K/NK. Hopf torsion embeds
 # in that quotient. Only genuine centralizer commutators are inserted;
 # the two power words are deliberately excluded.
 for i in [1..m] do
  basis[i]:=[i,modulus];basisweights[i]:=[];
  basisproof[i]:=newLeaf("modulus",[i],[i,modulus]);
 od;
 for i in [3..Length(extras)] do insert(extras[i],[i,1],newLeaf("extra",[i],extras[i]));od;'''
    assert old in text
    text = text.replace(old, new)
    text = text.replace('Assert(0,v[2]<basis[idx][2]);old:=',
                        'Assert(0,v[2]<basis[idx][2]);if basis[idx][2]=modulus then pivots:=pivots+1;fi;old:=')
    text = text.replace('result:=rec(success:=true,coefficients:=coeffs,',
                        'Assert(0,coeffs[1]=0 and coeffs[2]=0);result:=rec(success:=true,coefficients:=coeffs,')
    text = '# Original-presentation modular Hopf-torsion witness.\n' + text
    (BASE / 'pbc_hermite_modular_witness.g').write_text(text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=Path)
    parser.add_argument('--precollected', type=Path)
    parser.add_argument('--trace', type=Path)
    parser.add_argument('--stem', type=Path, required=True)
    args = parser.parse_args()
    assert bool(args.precollected) != bool(args.trace)
    source = json.loads(args.source.read_text())
    orders = source['relative_orders']
    modulus = math.prod(orders)
    assert modulus % 6 == 0
    if 'order' in source:
        assert int(source['order']) == modulus
    n = len(orders)
    if 'conjugates_nested' in source:
        conjugates = source['conjugates_nested']
    else:
        conjugates = [[] for _ in orders]
        for i, j, word in source['conjugates']:
            assert len(conjugates[i-1]) == j-1
            conjugates[i-1].append(word)
    if args.precollected:
        raw = json.loads(args.precollected.read_text())
        target, extras = raw['target'], raw['extras']
    else:
        target = None
        extra_map = {}
        for line in args.trace.read_text().splitlines():
            row = json.loads(line)
            if row[0] != 'leaf':
                continue
            if row[2] == 'target':
                assert target is None
                target = row[4]
            elif row[2] == 'extra':
                extra_map[row[3][0]] = row[4]
        assert target is not None
        extras = [extra_map[i] for i in range(1, len(extra_map)+1)]
    assert len(extras) == 2 + len(source['s_centralizers']) + len(source['r_centralizers'])
    data = dict(orders=orders, powers=source['powers'], conjugates=conjugates,
                s=source['s'], r=source['r'], bs=source['left_s_frame'],
                br=source['left_r_frame'], cs=source['s_centralizers'],
                cr=source['r_centralizers'], s_image=source['s_image'],
                r_image=source['r_image'], initial_target=target,
                initial_extras=extras, modulus=modulus,
                source_sha256=hashlib.sha256(args.source.read_bytes()).hexdigest(),
                trace_stem=str(args.stem)+'_trace')
    write_routine()
    gap = 'LoadPackage("polycyclic");;\nRead("LM8_PUSH/code/pbc_hermite_modular_witness.g");;\n'
    gap += 'PBC_data:=rec('+','.join(k+':='+json.dumps(v,separators=(',',':')) for k,v in data.items())+');;\n'
    gap += 'PBC_witness:=PBC_HermiteModularWitness(PBC_data);;\n'
    gap += 'Print("modular_witness_success ",PBC_witness.success,"\\n");\n'
    gap += 'if PBC_witness.success then\n'
    gap += 'PrintTo('+json.dumps(str(args.stem)+'_certificate.json')+',"{\\n\\\"success\\\":true,\\n\\\"coefficients\\\":",PBC_witness.coefficients,",\\n\\\"relations\\\":",PBC_witness.relations,",\\n\\\"pivots\\\":",PBC_witness.pivots,",\\n\\\"s_count\\\":",PBC_witness.s_count,",\\n\\\"r_count\\\":",PBC_witness.r_count,",\\n\\\"proof_node\\\":",PBC_witness.proof_node,"\\n}\\n");\nfi;\nQUIT;\n'
    args.stem.with_suffix('.g').write_text(gap)
    files = [args.source, BASE/'pbc_hermite_precollected_witness.g',
             BASE/'pbc_hermite_modular_witness.g', Path(__file__), args.stem.with_suffix('.g')]
    files.append(args.precollected or args.trace)
    report = dict(source_sha256=data['source_sha256'], modulus=modulus,
                  base_generators=n, formal_central_tails=n*(n+1)//2,
                  target_support=len(target)//2, s_count=len(data['cs']), r_count=len(data['cr']),
                  forbidden_power_word_rows=[1,2],
                  source_identity_collection='Original formal source; no processed relation lattice.',
                  hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
                  scope='A modular result is valid integrally only with the proved Hopf-torsion embedding, original-word replay, and exclusion of power-word corrections.')
    args.stem.with_suffix('.inputs.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
