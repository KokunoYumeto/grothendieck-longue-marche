import sys, json, csv, os
a_dir, b_dir = sys.argv[1], sys.argv[2]
names = sys.argv[3:]
for n in names:
    pa, pb = os.path.join(a_dir, n), os.path.join(b_dir, n)
    if n.endswith('.json'):
        ja = json.load(open(pa, encoding='utf-8')); jb = json.load(open(pb, encoding='utf-8'))
        if isinstance(ja, dict) and 'certificate_sha256' in ja:
            ja = dict(ja); jb = dict(jb)
        print(n, 'EQUAL' if ja == jb else 'DIFFERENT')
        if ja != jb and isinstance(ja, dict):
            for k in set(ja) | set(jb):
                if ja.get(k) != jb.get(k): print('   key differs:', k)
    elif n.endswith('.csv'):
        ra = list(csv.reader(open(pa, encoding='utf-8'))); rb = list(csv.reader(open(pb, encoding='utf-8')))
        print(n, 'EQUAL' if ra == rb else 'DIFFERENT', len(ra), len(rb))
    else:
        ta = open(pa, encoding='utf-8').read().split(); tb = open(pb, encoding='utf-8').read().split()
        print(n, 'EQUAL(tokens)' if ta == tb else 'DIFFERENT(tokens)')
