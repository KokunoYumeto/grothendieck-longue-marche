from pathlib import Path
import hashlib, json, shutil

R = Path(__file__).resolve().parents[1]
A = R / 'audit' / 'pre_primary_projection'
A.mkdir(parents=True, exist_ok=True)
paths = [R/'sections/E_fiftythree_positional_stable.tex']
paths += list((R/'qa').glob('*'))
paths += [R/'code'/('e53_positional_layout'+s) for s in ('.py','.out','.err','.json')]
for p in paths:
    if p.is_file():
        q=A/p.relative_to(R); q.parent.mkdir(parents=True,exist_ok=True)
        if q.exists(): assert q.read_bytes()==p.read_bytes()
        else: shutil.copy2(p,q)
p=R/'sections/E_fiftythree_positional_stable.tex'
old=p.read_text()
start=old.index('For any other prime in $\\mathcal P$')
end=old.index('\\emph{Surviving branches, completion and coherent lifts.}',start)
before=old[start:end].rstrip()
after='''For any other prime in $\\mathcal P$, its three-primary coordinate
$c_p$ can therefore be evaluated by exact ideal relations in this
certified finite presentation. One unconditional terminating
procedure enumerates positive integers $m\\equiv1\\pmod9$, the $81$
prime-basis classes, integral powers of the two $S$-primes, and
nonzero field elements, until the full ideal equality for
$\\mathfrak p_2^{\\,m}$ is found. Some such $m$ annihilates the
prime-to-three component of $[\\mathfrak p_2]$, by the Chinese
remainder theorem. On $C_2=C_9^2$ multiplication by $m$ is the
identity, so the recovered coordinate is exactly $c_p$ and is
unique. This is the explicit projection to the three-primary
subgroup; it does not require a value for the remaining class-group
part. A principal-ideal routine may propose the equality directly;
it is accepted only after full ideal verification. No missing
coordinate is assigned from the genus projection.'''
assert before in old
new=old.replace(before,after)
p.write_text(new)
record={'status':'PASS','scope':'Exact terminating three-primary projection algorithm only; no mathematical program or numerical certificate changed.',
        'old_section_sha256':hashlib.sha256(old.encode()).hexdigest(),
        'new_section_sha256':hashlib.sha256(new.encode()).hexdigest(),
        'map':'For m=1 mod9 killing the prime-to-three part, [p^m] in C9^2 equals pr_3[p]; the full ideal relation is checked.',
        'preserved_directory':str(A.relative_to(R))}
(A/'amendment.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
