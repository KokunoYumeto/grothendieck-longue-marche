"""Verify retained certificates without running the producer's xgcd."""
from pathlib import Path
from functools import lru_cache
import hashlib, json, struct
from flint import fq_default_ctx, fq_default_poly_ctx, fmpz_mod_poly_ctx, nmod_poly

root=Path(__file__).resolve().parent
base=root/"primitive_certificates"
manifest=json.loads((base/"manifest.json").read_text())
exp=manifest["field_modulus_exponents"]
k=fq_default_ctx(modulus=fmpz_mod_poly_ctx(2)([int(i in exp) for i in range(39)]),
                 var="t",fq_type="FQ_NMOD")
t=k.gen(); R=fq_default_poly_ctx(k); U=R.gen(); den=t**3+1
A=(U*U+t*t*U+t)/den
B=(t*U*U+U+t*t)/den
X=nmod_poly([0,1],2)
@lru_cache(None)
def division(n):
    if n in (1,2,4): return nmod_poly([1],2)
    if n==3: return X**4+X
    if not n%2:return division(n//2)**4
    j=n//2
    return division(j+2)*division(j)**3+division(j-1)*division(j+1)**3

def decode(data):
    integers=struct.unpack("<"+"Q"*(len(data)//8),data)
    assert all(x<2**38 for x in integers)
    return R([k([(x>>j)&1 for j in range(38)]) for x in integers])

results=[]
for cert in manifest["certificates"]:
    polys=[]
    for item in cert["polynomials"]:
        data=(base/item["file"]).read_bytes()
        assert len(data)==item["bytes"]
        assert hashlib.sha256(data).hexdigest()==item["sha256"]
        poly=decode(data); assert poly.degree()==item["degree"]
        polys.append(poly)
    pa,pb,va,vb=polys
    psi=division(cert["n"])
    q=R([int(x) for x in psi])
    assert q.compose(A)==pa and q.compose(B)==pb
    assert va*pa+vb*pb==R.one()
    record={"n":cert["n"],"hashes":"PASS","encodings":"PASS",
            "independent_compositions":"PASS","full_bezout_identity":"PASS"}
    print(record,flush=True);results.append(record)
(root/"primitive_verify.json").write_text(json.dumps(results,indent=2)+"\n")
print("All retained conductor certificates verified.",flush=True)

