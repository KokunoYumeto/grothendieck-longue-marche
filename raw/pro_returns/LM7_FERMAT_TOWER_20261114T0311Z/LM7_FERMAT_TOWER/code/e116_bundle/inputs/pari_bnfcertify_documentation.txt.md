\subsec{bnfcertify$(\var{bnf},\{\fl = 0\})$}\kbdsidx{bnfcertify}\label{se:bnfcertify}
$\var{bnf}$ being as output by
\kbd{bnfinit}, checks whether the result is correct, i.e.~whether it is
possible to remove the assumption of the Generalized Riemann
Hypothesis\sidx{GRH}. It is correct if and only if the answer is 1. If it is
incorrect, the program may output some error message, or loop indefinitely.
You can check its progress by increasing the debug level. The \var{bnf}
structure must contain the fundamental units:
\bprog
? K = bnfinit(x^3+2^2^3+1); bnfcertify(K)
  ***   at top-level: K=bnfinit(x^3+2^2^3+1);bnfcertify(K)
  ***                                        ^-------------
  *** bnfcertify: precision too low in makeunits [use bnfinit(,1)].
? K = bnfinit(x^3+2^2^3+1, 1); \\ include units
? bnfcertify(K)
%3 = 1
@eprog

If $\fl$ is present, only certify that the class group is a quotient of the
one computed in bnf (much simpler in general); likewise, the computed units
may form a subgroup of the full unit group. In this variant, the units are
no longer needed:
\bprog
? K = bnfinit(x^3+2^2^3+1); bnfcertify(K, 1)
%4 = 1
@eprog

The library syntax is \fun{long}{bnfcertify0}{GEN bnf, long flag }.
Also available is  \fun{GEN}{bnfcertify}{GEN bnf} ($\fl=0$).

\subsec{bnfdecodemodule$(\var{nf},m)$}\kbdsidx{bnfdecodemodule}\label{se:bnfdecodemodule}
If $m$ is a module as output in the
first component of an extension given by \kbd{bnrdisclist}, outputs the
