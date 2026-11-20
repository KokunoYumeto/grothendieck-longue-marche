"""Formal endpoint check only; no OCR, geometric identification or manuscript repair."""
import json
labels = ("0", "1", "infinity")
def pair(i,j): return (labels[i%3],labels[j%3])
def lam(i): return (pair(i,i+1),pair(i,i+2))
def a_live(i): return (pair(i,i+1),pair(i+1,i+2))
def inv(arrow): return (arrow[1],arrow[0])
rows=[]
for li,ai in ((0,1),(2,0),(1,2)):
    right=a_live(ai); left=inv(lam(li))
    rows.append({"factor":"lambda_"+labels[li]+"^-1 a_"+labels[ai],"a_target":right[1],"lambda_inverse_source":left[0],"composable_right_to_left":right[1]==left[0]})
assert all(not row["composable_right_to_left"] for row in rows)
print(json.dumps(rows,indent=2))
