# Independent eight-equation certificate for arbitrary coarse sections

Root research and manual verification, checkpoint29. This is separate
from the frozen formal paper. We use the actual B.123 and B.127 groups,
all forty node seeds and every signed source/deck translate. The whole
node normal closure lies in [L,L]. Consequently the actual quotient
P=F/[L,L] has the exact split form M semidirect T, with
M=Z[T]^8 and T=F(f,g,x). Both source automorphisms preserve [L,L], giving
the actual quotient Gamma0 -> P semidirect S, S=F(m,v).

We independently derive the necessary equations for an arbitrary section
of Gamma0 -> Q0=T semidirect S. No selected-involution condition and no
restriction on any of its three retained lifts is imposed. Its image
in the module quotient sends t to eta(t) sigma(t), where sigma is the
old retained section and eta is a left T-derivation:

    eta(tu)=eta(t)+t eta(u).

It sends m,v to mu_m m,mu_v v in the module quotient. Let rho_s be the
actual action on M, phi_s the retained action, and d_s(t) the actual
old-section defect. The source relation forces, for s=m,v and t=f,g,x,

    rho_s eta(t) + d_s(t) - eta(phi_s(t)) = (phi_s(t)-1)mu_s.  (1)

This follows by multiplying in M semidirect T: conjugation by mu_s
adds mu_s-phi_s(t)mu_s. It is necessary for every original section,
irrespective of whether all module-level solutions lift to the original
group. The proof below shows that even these necessary equations are
inconsistent.

## The actual B-color data

Each actual signed source preserves the positive B core, so this single
color does not mix with any other family color. In the original F11
marking its two conjugator heads are

    h_m=f^{-1}g,                 h_v=xg^{-1}x^{-1}.

Both positive retained actions induce on the abelianization of T

    f -> g,  g -> f,  x -> x+f-g.

The exact positive heads needed below are

    phi_m(f)=f^{-1}gf,   phi_m(g)=f,   phi_m(x)=xg^{-1}f,
    phi_v(f)=xgx^{-1},               phi_v(x)=xg^{-1}f.

For a finite integral group-ring element z put epsilon(z)=sum z_t,
and chi_i(z)=sum z_t chi_i(t), for i=f,g,x. The B-color defects for m
are identically zero. The two v defects needed are exactly

    d_v(f)_B=1-xg^{-1}x^{-1},
    d_v(x)_B=xg^{-1}-xg^{-1}f.

Their four coordinates (epsilon,chi_f,chi_g,chi_x) are respectively
(0,0,1,0) and (0,-1,0,0). These are the entire relevant color classes,
not selected coefficients from a larger unexamined class. All data
come from the same fixed actual operator and Schreier inputs as B.140.

## All variables remain arbitrary

Write F_j,G_j,X_j for the four coordinates j=0,1,2,3 of eta(f)_B,
eta(g)_B,eta(x)_B, with index0 denoting augmentation and indices1,2,3
the f,g,x moments. Put M=epsilon(mu_m,B), V=epsilon(mu_v,B).
These are fourteen unrestricted integer variables. No relation between
the B and opposite-B colors is imposed.

The actual source actions on a B-coordinate with jet (z0,z1,z2,z3) are

    rho_m: (z0,z2+z3-z0,z1-z3+z0,z3),
    rho_v: (z0,z2+z3,   z1-z3-z0,z3).

The derivation rule evaluates eta on the exact retained words. For
example eta(f^{-1}gf)=(f^{-1}g-f^{-1})eta(f)+f^{-1}eta(g), while
eta(xg^{-1}f)=eta(x)+xg^{-1}(eta(f)-eta(g)). The eight necessary
coordinates of (1), in order, are:

| Equation | Left side | Right side |
|---|---|---:|
| E1: m,f,augmentation | F0-G0 | 0 |
| E2: m,f,f-moment | F2+F3-F0-G1+G0 | 0 |
| E3: m,f,x-moment | F3-G3 | 0 |
| E4: m,g,f-moment | G2+G3-G0-F1-M | 0 |
| E5: m,x,f-moment | X2+X3-X0-X1+G1-F1-M | 0 |
| E6: m,x,g-moment | X1-X3+X0-X2+G2-F2+F0-G0+M | 0 |
| E7: v,f,g-moment | F1-F3-F0-G2+X0-V | -1 |
| E8: v,x,f-moment | X2+X3-X1+G1-F1-V | 1 |

The exact integral combination

    -E1 -2E2 +E3 +E4 -3E5 -2E6 -E7 +E8

has left side zero: every one of the fourteen coefficients cancels.
Its right side is2. Thus (1) has no solution even over the rationals,
and in particular no integral solution. This establishes ordinary
nonsplitting of the specified actual coarse quotient. It uses only
positive m/v equations, so the delta and inverse-source equations from
the larger discovery computation are not needed for the obstruction.

## The full profinite obstruction is already finite

B.140's cofinal finite wreath-head proof gives the actual compact
quotient P-hat=Omega semidirect T-hat, with
Omega=Zhat[[T-hat]]^8. Characteristic finite-index refinements in the
finitely generated P extend its finite targets to P semidirect S.
Hence the map from the original full completion to this quotient is
actual, with no assertion that the closed family kernel's abelianization
is Omega.

Every continuous section of the actual completed coarse quotient would
induce the same derivation and source equations in Omega. Reduce to the
finite coefficient head F3[(C3)^3]. The augmentation and three moments
are continuous F3-valued functions there. Their multiplication and
source rules are precisely the reductions of the displayed integer
rules. The eight equations therefore have the same integral combination,
giving 0=2 in F3. This is impossible. If one wants a single whole-group
finite detector, refine the kernel of that actual P head to a
characteristic finite-index subgroup and retain the finite source action.
The initial head itself need not be source-stable.

Thus the completed quotient has no continuous section either. The
conclusion concerns this exact coarse extension. It neither disproves
the remaining fixed-source equality nor decides the geometric Main-B
kernel or the actual icosahedral K=1 problem.

## Independent verification scope

Root read the entire CE first-order producer, its genuine stdout/stderr,
and its complete output JSON. We then derived the eight equations above
directly from the displayed actual heads and the left derivation rule,
and canceled their coefficients by hand, without using Smith normal form
as the proof. The small root checker reads the actual immutable inputs,
checks their complete relevant color data and heads, and verifies the
fourteen-variable combination directly with integer arithmetic. It is
not a repeat of the underlying geometric extraction or an enumeration
of groups, sections, coefficients, or source words.

Input paths: records/root_coarse_corrections29.json and
work_CE/next_symmetric_nodes/family_kernel_schreier25.json.
Checker: code/check_root_arbitrary_section_certificate29.py, with genuine
stdout/stderr and records/root_arbitrary_section_certificate29.json.
The author's complete independent proof and reviews are retained
separately. All frozen formal sources remain unchanged.
