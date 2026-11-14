import json
bc=11351380622391
n=2*3**49-bc
value=(n+575)//576
assert value==830900448697714719719
assert (value-1)*576<n<=value*576
print(json.dumps({"status":"PASS","Bc":bc,"numerator":n,"denominator":576,"ceiling":value,"integer_inequalities_verified":True},indent=2))
