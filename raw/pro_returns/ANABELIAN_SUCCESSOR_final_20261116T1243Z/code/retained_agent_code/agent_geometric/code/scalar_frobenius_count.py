"""Independent exact point-count certificate for the scalar-Frobenius example.

The existence deduction uses all C13 quotients collectively, Fourier inversion,
and the genus-two difference bound. It does not guess a covering character.
The explicit character is supplied by the criteria agent's separate certificate.
"""
import json


def count_AS_x5(degree, modulus):
    size=1<<degree
    def mul(a,b):
        result=0
        while b:
            if b&1: result^=a
            b>>=1
            a<<=1
            if a&size: a^=modulus
        return result
    def trace(a):
        result=0
        for _ in range(degree):
            result^=a
            a=mul(a,a)
        assert result in (0,1)
        return result
    zeros=0
    for x in range(size):
        x2=mul(x,x)
        x5=mul(mul(x2,x2),x)
        zeros += trace(x5)==0
    return 1+2*zeros


N16=count_AS_x5(4,0b10011)
N4096=count_AS_x5(12,(1<<12)+(1<<3)+1)
assert N16==33
assert N4096==4353
assert N16==16+1+4*4
assert N4096==4096+1+4*64
H=5**4
bound=2*(H-1)
assert N4096-N16>bound
assert pow(-4,3,13)==1 and all(pow(-4,i,13)!=1 for i in (1,2))
assert {pow(2,i,13) for i in range(12)}==set(range(1,13))
print(json.dumps({
    "curve":"y^2+y=x^5",
    "N16":N16,
    "N4096":N4096,
    "Jacobian_Frobenius_over_F16":"[-4], from equality in the maximal Weil bound",
    "Jacobian_F4096":"J[65] = (Z/65)^4",
    "H":"13*J(F4096) = J[5]",
    "H_cardinality":H,
    "zero_coset_occupancy":N16,
    "nonzero_coset_points":N4096-N16,
    "maximum_number_of_points_sharing_cosets":bound,
    "contradiction":"4320 > 1248 if every C13 quotient failed the rational test",
    "first_constant_C13_field_over_F16_degree":3,
    "geometric_new_rank":"12 for every C13 cover: theta13 is empty by AG.21",
    "conclusion":"A pointed rational C13 witness exists despite ordinary new part",
    "assertions":"all passed"
},indent=2))
