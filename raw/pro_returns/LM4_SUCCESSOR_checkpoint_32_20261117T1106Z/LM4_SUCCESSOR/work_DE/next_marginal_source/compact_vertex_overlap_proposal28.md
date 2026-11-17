# Provisional compact vertex-overlap upgrade

Status: ROOT PROPOSAL, UNDER INDEPENDENT AUDIT as of 2026-11-17 04:20 UTC. This file records a proposed argument, not an accepted theorem. It does not alter the frozen ordinary B137 source.

For each n>=2 take the actual B117 map L=H*_<k>P -> L_n=C2(C)*P_n, where H=<h,k|[h^2,k]>, P=<k>xF(a,d,e,V4), P_n=C_n(k)x(C2)^4(a,d,e,V4), and h maps to C. Then H_n=C2*C_n and f_n=Ck^-1. The proposed claim is that the exact B137 tree immersion/fork survives: U_n=<k_n,q_n> is C_n*Z, with kernel on U the normal closure of k^n, and U_n intersects zeta_n H_n zeta_n^-1 trivially. All internal leaf blocks remain nonzero in P_n/<k>: a,V4,a^-1=a,D=d e d^-1=e,d^-1=d; the fork directions 1,e,V4 remain distinct. Every nonzero f_n power is outside <k>; f_n^-1 k^j f_n is outside <k> for j nonzero modulo n. Repeated involutive leaf labels and whole reduced paths require explicit audit.

Each L_n is virtually free. The needed topological input is: finitely generated subgroups have full induced profinite topology, and products of finitely generated subgroups are closed. A primary source must be opened/read at use, including the finite-index-free extension.

Proposed intersection lemma: if A,B are finitely generated subgroups of such a G, then cl(A) intersection cl(B)=cl(A intersection B). Given a finite quotient q and a common completed element t, choose a in A,b in B with q(a)=q(b)=q(t). Put A0=A intersection ker(q),B0=B intersection ker(q). Then t lies in a cl(A0) intersection b cl(B0), so b^-1a lies in cl(B0 A0). Closedness supplies b^-1a=b0 a0 and b b0=a a0^-1 lies in A intersection B with the prescribed q-image. This proves the equality if the topological input holds.

Cofinality proposal: every finite U target factors through some U_n by taking n divisible by the order of k. Full topology of U_n in L_n permits a finite L_n quotient refining that target. Thus the maps Uhat -> L_nhat jointly separate Uhat and establish full U topology in L. A common element of actual closures of U and zeta H zeta^-1 maps to one in every L_nhat and is therefore one. Conjugating gives Bjhat intersection Hhat=1; continuous color retraction gives E1hat intersection Bjhat=1.

The continuous actual retraction then gives Bjhat intersection (E1hat Khat)=Bjhat intersection Khat=closure<eta(f)>; theta gives the other vertex. The products here are compact and hence closed. This does NOT yet give a whole compact Hi/Hj invariant-tree embedding or compact intersection: their nontrivial cyclic-edge subamalgam/full-topology issue remains separate.

Audit, primary-source retrieval and exact proof will be recorded in a separate note. No numerical or word-depth census is proposed.
