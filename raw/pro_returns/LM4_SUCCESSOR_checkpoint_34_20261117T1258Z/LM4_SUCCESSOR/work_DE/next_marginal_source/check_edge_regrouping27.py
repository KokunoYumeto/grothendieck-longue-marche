#!/usr/bin/env python3
"""Exact free-basis input to the actual edge-regrouping obstruction.

No quotient enumeration or finite-orbit search. Reads the already certified
literal five-generator common-neck reflection, then checks the indicated
quotient and both inverse basis substitutions independently.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'work_DE/next_marginal_source/annular_neck_reflection23.json'
OUT = Path(__file__).with_suffix('.json')

def red(w):
    a=[]
    for x in w:
        if a and a[-1] == -x:
            a.pop()
        else:
            a.append(x)
    return a

def inv(w):
    return [-x for x in reversed(w)]

def mul(*ws):
    return red([x for w in ws for x in w])

def sub(w, images):
    return mul(*(images[abs(x)] if x>0 else inv(images[abs(x)]) for x in w))

def comm(a,b):
    return mul(a,b,inv(a),inv(b))

raw=json.loads(SRC.read_text())
eta={int(i):w for i,w in raw['eta_adapted_K_basis_a_barb_d_e_f'].items()}
checks=[]
def check(name, actual, expected):
    assert actual == expected, (name,actual,expected)
    checks.append(name)

for i in range(1,6):
    check(f'eta_square_{i}',sub(eta[i],eta),[i])
kill_f={i:[i] for i in range(1,5)}|{5:[]}
e={i:sub(eta[i],kill_f) for i in range(1,5)}
check('normal_f_is_invariant',sub(eta[5],kill_f),[])
for i in range(1,5):
    check(f'quotient_eta_square_{i}',sub(e[i],e),[i])

# y=Inn(a^-1) after e. Its inverse is e after Inn(a).
y={i:mul([-1],e[i],[1]) for i in range(1,5)}
yinv={i:sub(mul([1],[i],[-1]),e) for i in range(1,5)}
for i in range(1,5):
    check(f'y_then_inverse_{i}',sub(y[i],yinv),[i])
    check(f'inverse_then_y_{i}',sub(yinv[i],y),[i])
check('Y_a_literal',y[1],[2,-1,-2])

# Abstract target generators: a,B,d,e,k = 1,2,3,4,5.
k=[5]
v0=[-1]
s=mul(inv(v0),k,v0)
for i in range(1,5):
    image=comm(s,e[i])
    wanted=mul([1],comm(k,y[i]),[-1])
    check(f'leaf_relation_{i}',image,wanted)
check('known_U_image',mul(v0,e[1],inv(v0)),y[1])
check('h_square_relation_image',comm(mul(s,s),s),[])

data={
    'status':'PASS',
    'input':str(SRC.relative_to(ROOT)),
    'input_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
    'basis':['a','B','d','e'],
    'eta_mod_f':e,
    'Y_basis':y,
    'Y_inverse':yinv,
    'V_i_order':['a','d','e','f^-1 B f'],
    'Y_leaf_order':[y[i] for i in (1,3,4,2)],
    'v0_image':v0,
    's_image':s,
    'known_U_image':y[1],
    'checks':checks,
    'scope':('All other claims are the exact actual-retraction and free-product '
             'normal-form proof in edge_regrouping_obstruction27.md. This does '
             'not identify the additional leaves with actual corrected source '
             'contacts and does not infer any new final-group relation among '
             'those source contacts.')
}
OUT.write_text(json.dumps(data,indent=2)+'\n')
print(f'PASS: {len(checks)} exact identities; complete four-generator Y basis and inverse.')
print('Y_a = B a^-1 B^-1; the remaining three Y letters are independent free-basis entries.')
print('Known source relation only yields Z^2(k,Y_a)*F(Y_d,Y_e,Y_B) in this detector.')
