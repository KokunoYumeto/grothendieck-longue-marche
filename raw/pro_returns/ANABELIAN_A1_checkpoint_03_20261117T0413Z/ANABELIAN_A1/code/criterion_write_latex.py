#!/usr/bin/env python3
"""Build the criterion inclusion from the retained independent proof notes."""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
notes = (ROOT/'notes/criterion_audit.md').read_text()


def between(start, end):
    return notes.split(start, 1)[1].split(end, 1)[0].strip()


def section(n):
    match = re.search(r'^## '+str(n)+r'\. .*\n', notes, re.M)
    rest = notes[match.end():]
    return re.split(r'^## \d+\.', rest, maxsplit=1, flags=re.M)[0].strip()


REPL = {
    'Section 10.1': r'the difference-map argument in \statementref{A.CR8}',
    'Section 5.1': r'the Kummer step of \statementref{A.CR6}',
    'Section 7.3': r'Statement \statementref{A.CR13}',
    'Section 9': r'Statement \statementref{A.CR7}',
    'Section 4': r'Statement \statementref{A.CR4}',
    'Section 3': r'Statement \statementref{A.CR5}',
    'Section 2': r'Statement \statementref{A.CR2}',
    'Section 1': r'Statement \statementref{A.CR3}',
    'AG.40': 'AS-AG.40',
    'β': r'\ensuremath{\beta}', 'Σ': r'\ensuremath{\Sigma}',
    'Δ': r'\ensuremath{\Delta}', 'Π': r'\ensuremath{\Pi}',
    'Γ': r'\ensuremath{\Gamma}', 'χ': r'\ensuremath{\chi}',
    'δ': r'\ensuremath{\delta}', 'σ': r'\ensuremath{\sigma}',
    'μ': r'\ensuremath{\mu}', 'ζ': r'\ensuremath{\zeta}',
    'ℓ': r'\ensuremath{\ell}', 'κ': r'\ensuremath{\kappa}',
    '→': r'\ensuremath{\to}', '⊂': r'\ensuremath{\subset}',
    '≤': r'\ensuremath{\le}', '≥': r'\ensuremath{\ge}',
    '≠': r'\ensuremath{\ne}', '∈': r'\ensuremath{\in}',
    '∩': r'\ensuremath{\cap}', '∞': r'\ensuremath{\infty}',
    '×': r'\ensuremath{\times}', '⊴': r'\ensuremath{\trianglelefteq}',
    '≅': r'\ensuremath{\simeq}', '⊊': r'\ensuremath{\subsetneq}',
    '⋊': r'\ensuremath{\rtimes}', '∪': r'\ensuremath{\cup}',
    'Φ': r'\ensuremath{\Phi}', '∏': r'\ensuremath{\prod}',
    'ϕ': r'\ensuremath{\varphi}', 'ℤ': r'\ensuremath{\mathbf Z}',
    '−': '-', '–': '--', '—': '---', '′': "'",
    '⁷': r'\ensuremath{^7}', '¹': r'\ensuremath{^1}', '₂': r'\ensuremath{_2}',
}


def mark_math(text):
    """Turn the compact mathematical tokens in the working notes into math.

    The notes deliberately use human-readable G_k etc. outside explicit
    equations.  Protect existing equations/code and brace-balanced tokens.
    """
    text=text.replace(r'\bar k',r'\bar{k}').replace(r'\hat Z',r'\widehat{\mathbf Z}').replace(r'\tilde x',r'\tilde{x}')
    text=text.replace("\\'{e}tale", "étale")
    text=text.replace('*almost Σ-separated*','almost Σ-separated').replace('*Σ-separated*','Σ-separated')
    protected = re.compile(r'(\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$\$[\s\S]*?\$\$|\$[^$\n]*\$|`[^`]*`)')
    pieces = protected.split(text)
    markers = set('_^βΣΔΠΓχδσμζℓκ→⊂≤≥≠∈∩∞×⊴≅⊊⋊∪Φ∏ϕℤ−∅∤')
    for j in range(0,len(pieces),2):
        src=pieces[j]
        tokens=[]
        cur=[]
        depth=0
        for ch in src:
            if ch.isspace() and depth==0:
                if cur:
                    tokens.append(''.join(cur)); cur=[]
                tokens.append(ch)
            else:
                cur.append(ch)
                if ch=='{': depth+=1
                elif ch=='}': depth-=1
        if cur: tokens.append(''.join(cur))
        result=[]
        for tok in tokens:
            if not any(c in markers for c in tok) and not re.search(r'\\(?:bar|tilde|widehat|hat)',tok):
                result.append(tok); continue
            body,tail=re.match(r'^(.*?)([.,;:?!]*)$',tok,re.S).groups()
            prefix=''
            suffix=''
            for pref in ['geometric-pro-','prime-to-','pro-']:
                if body.startswith(pref):
                    prefix=pref;body=body[len(pref):];break
            adj=re.search(r'(-(?:primary|stable|coverings?|covers?|groups?|large|adic|rational|points?|module|extension|separated|largeness|torsion|Frobenius))$',body)
            if adj:
                suffix=adj.group();body=body[:-len(suffix)]
            body=body.replace('#',r'\#').replace('∤',r'\nmid ')
            body=re.sub(r'(?<![A-Za-z\\])ell(?![A-Za-z])',r'\\ell',body)
            body=body.replace('Primes-{p}',r'\mathrm{Primes}-\{p\}')
            body=body.replace('{P,Q}',r'\{P,Q\}')
            body=re.sub(r'(?<![A-Za-z\\])GL_',r'\\operatorname{GL}_',body)
            body=re.sub(r'(?<![A-Za-z\\])UT_',r'\\operatorname{UT}_',body)
            body=re.sub(r'(?<![A-Za-z\\])([FZQP])_',lambda m:r'\mathbf{'+m.group(1)+'}_',body)
            body=re.sub(r'\^\(([^)]*)\)',r'^{(\1)}',body)
            body=body.replace('^circ',r'^{\circ}')
            body=body.replace('_ell',r'_{\ell}')
            body=re.sub(r'(?<![A-Za-z\\])(ker|core|Aut|Out|Gal|Hom|Pic|pr|div|ord|id)(?=[(_])',lambda m:r'\operatorname{'+m.group(1)+'}',body)
            result.append(prefix+r'\('+body+r'\)'+suffix+tail)
        pieces[j]=''.join(result)
    return ''.join(pieces)


def latex(text):
    text=mark_math(text)
    for a,b in REPL.items():
        text = text.replace(a,b)
    text=text.replace('∅',r'\varnothing')
    text = re.sub(r'^###\s+(.*)$', r'\n**\1.**\n', text, flags=re.M)
    tex = subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex',
                          '-t','latex','--wrap=preserve'], input=text,
                         text=True, check=True, capture_output=True).stdout
    tex=tex.replace(r'\textquotesingle\{e\}tale','étale')
    tex=tex.replace(r'\(H^1(G_k,T_{\ell}\) \(J_C)\)',r'\(H^1(G_k,T_{\ell}J_C)\)')
    tex=tex.replace(r'\bar{k}',r'\bar k')
    tex=tex.replace(r'\#C(L)=129',r'\(\#C(L)=129\)')
    tex=tex.replace(r'The following strengthening was suggested independently during the parallel audit and checked here. It is useful both for an independent proof of the main theorem and for the \(J_C\)-large prime sets in ST2017.', r'This strengthening also applies to the \(J_C\)-large prime sets of \cite{ST2017}.')
    def mathfix(match):
        part=match.group()
        while r'\ensuremath{' in part:
            nxt=re.sub(r'\\ensuremath\{([^{}]*)\}',lambda m:'{'+m.group(1)+'}',part)
            if nxt==part: break
            part=nxt
        part=part.replace('Primes-{p}',r'\mathrm{Primes}-\{p\}')
        part=part.replace('C-{P,Q}',r'C-\{P,Q\}')
        part=part.replace(r'\cup}{P,Q}',r'\cup}\{P,Q\}')
        part=part.replace(r'\mathbf{F}_0','F_0').replace(r'\mathbf{Q}_m','Q_m')
        part=part.replace(r'\operatorname{GL}_rank(T_s)(\mathbf{F}_s)',r'\operatorname{GL}_{\operatorname{rank}T_s}(\mathbf F_s)')
        return part
    tex=re.sub(r'\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]',mathfix,tex)
    tex=tex.replace(r'\(degree-\ell^m\)',r'degree-\(\ell^m\)')
    tex=tex.replace(r'r\textbar n',r'\(r\mid n\)')
    tex=re.sub(r'\\textbf\{\d+\.\d+\. ',r'\\textbf{',tex)
    tex=tex.replace('seventh-adic','7-adic')
    tex=tex.replace("The inverse-limit Kummer map from a finite field's multiplicative group to", "The finite-field Kummer map to")
    return tex


items = []


def add(id, title, statement, proof, answers, deps=(), source=(), status='Proved'):
    items.append(dict(id=id,title=title,statement=statement,proof=proof,
                      answers=answers,dependencies=list(deps),source=list(source),status=status))


sec2 = section(2)
main2, comp2 = sec2.split('### Compactification and arithmetic compatibility')
add('A.CR1','The same-prime quotient lemma',r'''
Let $F$ be profinite, $K\triangleleft F$ closed, $r$ prime, and
$N=\ker(K\to K^{(r)})$. For every open $I\le F$ containing $N$, the
continuous quotient map induces a natural isomorphism
$I^{(r)}\simeq(I/N)^{(r)}$. No restriction on $[F:I]$ is imposed.
''',main2,['A3','K2'])

add('A.CR2','Compactification and Frobenius are retained at the cusp prime',r'''
Let $C/k$ be smooth proper geometrically connected of genus at least two,
$k$ finite of characteristic $p$, $P\in C(k)$, and $r\ne p$.
Every open geometric subgroup of the maximal cuspidally pro-$r$
quotient of $\pi_1(C-P)^{(p')}$, after its cusp inertia is killed and
its maximal pro-$r$ quotient is taken, gives the full geometric
pro-$r$ fundamental group of its actual smooth compactification.
The comparison is compatible with every arithmetic action preserving
the cover. Thus a cusp-preserving isomorphism over $G_k$ preserves
the point counts of every corresponding open cover over every
finite constant extension.
''',comp2+r'''

The point-count comparison uses the trace formula and the integral
Frobenius polynomial for a smooth proper curve over a finite field:
these are \cite[formula (1.5.1) and Theorem (1.6)]{WeilCurves}.
Their hypotheses apply to both smooth compactifications and to every
finite extension of their common constant field. Equality of their
$r$-adic characteristic polynomials is equality of integer polynomials,
since $\mathbf Z[T]\hookrightarrow\mathbf Z_r[T]$.
''',['A3','K2','A6'],['A.CR1'],['WeilCurves (1.5.1),(1.6)'])

add('A.CR3','The exact uniform exceptional-set input',r'''
For a proper hyperbolic curve $C/k$ over a finite field of
characteristic $p$, and $\Sigma=\mathrm{Primes}-\{p\}$, there is a
finite set $E_C\subset C^{\cl}$ such that outside its inverse image
a decomposition subgroup has a unique geometric point label, even
up to commensurability, over every finite constant extension at once.
The numbering of Definitions~1.3 and 1.5, Remark~1.2, and
Proposition~1.8(vi) is the same in the attached arXiv text and the
journal version of \cite{ST2009}.
''',section(1),['A2','K1'],source=['ST2009 Definition1.3,1.5; Remark1.2; Proposition1.8(iii)-(vi)'],status='Known, with derivation')

add('A.CR4','A rational point section is self-normalizing',r'''
Let $C/L$ be smooth proper geometrically connected of genus at least
two over a finite field, and let $\varnothing\ne\Sigma\subset
\mathrm{Primes}-\{\operatorname{char}L\}$. If $D\subset\Pi_C^\Sigma$
is a continuous section subgroup mapping isomorphically onto $G_L$,
then $N_{\Pi_C^\Sigma}(D)=D$.
''',section(4)+r'''

The opened source used in the first argument is
\cite[Lemma 1.7]{ST2009}; it has no cofiniteness assumption on $\Sigma$.
''',['A6','A12'],source=['ST2009 Lemma1.7'])

add('A.CR5','Point recognition in the whole cuspidal quotient',r'''
Under the hypotheses of AS-AG.40, a cusp-preserving isomorphism
$\beta:G_P\simeq G_Q$ over $\mathrm{id}_{\Pi_C}$ carries every
noncuspidal point section, after its finite residue-field extension,
to an actual noncuspidal point section. Outside $E_C\cup\{P,Q\}$ the
target point is the same point of $C$. This conclusion holds in the
whole quotient, and not merely at a finite level.
''',section(3),['A6'],['A.CR2','A.CR3'])

source_cohomology = r'''
For clarity about the orientation-class input, the precise finite-coefficient
facts are as follows. For a smooth proper connected curve over an
algebraically closed field and $r$ invertible in that field,
$H^2_{\et}(C,\mu_{r^a})\simeq\mathbf Z/r^a$ via degree, with a point
class sent to one; see \cite[Proposition 14.2 and Theorem 24.1(a)]{MilneEtale}.
The pro-$\Sigma$ group comparison when $r\in\Sigma$ can be verified
directly from \cite[Theorem 14.9 and Remark 14.10]{MilneEtale}.
In the tower of all connected geometric finite $\Sigma$-covers,
every $H^1(-,\mathbf Z/r^a)$ class is killed by its corresponding
cyclic torsor, and every $H^2(-,\mu_{r^a})$ class is killed by an
\'{e}tale cover of degree divisible by $r^a$. Such covers exist since
the Jacobian has nonzero $r$-adic Tate module. The Galois closures of
the composite covers remain $\Sigma$-covers, by the normal-core
argument. Cohomology above degree two vanishes. The spectral sequence
therefore identifies group cohomology with curve cohomology for these
coefficients. The same comparison over the finite ground field follows
by comparing the two Hochschild--Serre spectral sequences.
Inverse limits give the required $\mathbf Z_r(1)$ statement.
The tame surface presentation, including its canonical inertia words,
is \cite[Expos\'{e} XIII, Corollary 2.12]{SGA1}; its hypotheses are a
smooth proper connected curve over a separably closed field and a
finite set of distinct punctures, with the full prime-to-characteristic
quotient taken. Passing to any $\Sigma$ containing $r$ preserves the
pro-$r$ test used here.
'''
add('A.CR6','The complete conditional cuspidal criterion',r'''
Let $k$ be finite of characteristic $p$, $C/k$ smooth proper
geometrically connected of genus at least two, $P,Q\in C(k)$, and
$r\ne p$. Let $G_P,G_Q$ be the maximal cuspidally pro-$r$ quotients
of the arithmetic geometrically prime-to-$p$ groups of $C-P,C-Q$,
relative to their maps to the full proper group $\Pi_C$. If a
continuous isomorphism $\beta:G_P\to G_Q$ over
$\mathrm{id}_{\Pi_C}$ carries the cusp decomposition subgroup to
a conjugate of the cusp decomposition subgroup, then $P=Q$.
''',source_cohomology+'\n\n'+section(5),['A6','A1'],['A.CR1','A.CR2','A.CR3','A.CR4','A.CR5'],['SGA1 XIII2.12','MilneEtale 14.2,14.9,14.10,24.1','WeilCurves 1.6'])

add('A.CR7','Proper-field support suffices for the criterion',r'''
Let $\varnothing\ne\Sigma\subset\mathrm{Primes}-\{p\}$ and $r\in\Sigma$.
Use the full proper geometric pro-$\Sigma$ group in the preceding
criterion. It suffices that the noncuspidal point transport induced
by $\beta$ have unchanged labels outside $C(F)$, for one proper
algebraic subfield $k\subset F\subsetneq\bar k$. In particular,
an exceptional image supported over such an $F$ suffices, even if it
is infinite. The annihilating integer for $[P-Q]$ need not be
coprime to $r$.
''',section(9),['A6','A12','C1'],['A.CR1','A.CR2','A.CR4','A.CR5','A.CR6'],['WeilCurves 1.5.1,1.6'])

add('A.CR8','An independent elementary support-field proof',r'''
For a proper hyperbolic curve $C/k$ over a finite field of
characteristic $p$, put
\[
B_C=\{R\in C(\bar k):\exists S\ne R,
       [R-S]\in J_C(\bar k)[p^\infty]\}.
\]
There is a proper algebraic subfield $F\subsetneq\bar k$ containing
$k$ for which $B_C\subset C(F)$. Hence the conditional criterion
\statementref{A.CR6} admits a proof using
\statementref{A.CR7} and this support field in place of the
exceptional-set finiteness theorem.
''',section(10),['A1','A6','A12'],['A.CR1','A.CR2','A.CR4','A.CR5','A.CR7'])

add('A.CR9','Exceptional emptiness and all-extension point separation',r'''
For a proper hyperbolic $C/k$ over a finite field of characteristic
$p$ and every nonempty $\Sigma\subset\mathrm{Primes}-\{p\}$,
$E_C^\Sigma=\varnothing$ is equivalent to injectivity of the
geometric pro-$\Sigma$ point-section map after every finite
constant extension of $k$.
''',section(6),['A12','K6','C1','C5'],['A.CR4'],['ST2009 Proposition1.8(iii)','ST2017 Proposition2.11,2.12'])

add('A.CR10','Large prime sets and the finite-or-infinite dichotomy',r'''
Assume the cuspidal transport construction from equal point sections
has been established for nonempty
$\Sigma\subset\mathrm{Primes}-\{p\}$. Then
$E_C^\Sigma=\varnothing$ whenever $\Sigma$ is $J_C$-large in the
sense of \cite{ST2017}; this includes every cofinite $\Sigma$.
More generally, almost $\Sigma$-separation implies
$E_C^\Sigma=\varnothing$, and a finite $E_C^\Sigma$ is necessarily
empty. Thus the exceptional image is either empty or infinite.
This dichotomy alone does not classify every prime set.
''',section(11),['A12','C1','C5'],['A.CR7','A.CR8','A.CR9','configuration_transport'],['ST2017 Definition2.6,Proposition2.12'])

neg=section(7)
parts=re.split(r'^### 7\.\d+\. .*\n',neg,flags=re.M)[1:]
add('A.CR11','Genus-one negative control',r'''
The elliptic curve $E/\mathbf F_2:y^2+xy=x^3+1$ has distinct
rational points $O$ and $T=(0,1)$ whose sections collide in the
entire geometrically prime-to-two arithmetic group. Its exceptional
image is all of $E^{\cl}$. The finite-exception hypothesis used for
proper hyperbolic curves fails here.
''',parts[0],['A8','C3'],source=['criterion_negative_controls.py'])

add('A.CR12','The abelianized negative control in genus two',r'''
The smooth proper genus-two curve
$C/\mathbf F_2:y^2+x(x+1)y=x^5+1$ has distinct rational points
$P=(0,1)$ and $Q=(1,0)$ with $[P-Q]$ of exact order two. They
collide in the entire arithmetic extension by the geometric
abelian prime-to-two quotient. Both the cusp-residue and the
compactified-cover cohomology arguments cease to apply to that
abelianized replacement.
''',parts[1],['A8'],source=['criterion_negative_controls.py'])

add('A.CR13','A singleton prime set always has infinitely many exceptions',r'''
For every proper hyperbolic curve $C/k$ over a finite field and every
prime $r\ne\operatorname{char}k$, the exceptional image
$E_C^{\{r\}}$ is infinite. In particular, retaining only one
geometric prime does not separate rational points over every
finite constant extension.
''',parts[2],['A8','A12'],['A.CR9'],['criterion_negative_controls.py'])

add('A.CR14','A completely specified pro-three collision',r'''
Let $L=\mathbf F_2[t]/(t^7+t+1)$ and $C/L:y^2+y=x^5$.
The distinct $L$-points
$P=(t,t^6)$ and $Q=(t^2,t^6+t^5)$ have conjugate sections in
the entire arithmetic extension by the geometric pro-three group.
The assertion is not merely a finite-quotient collision.
''',parts[3],['A8','A12'],['A.CR13'],['criterion_negative_controls.py'])

add('A.CR15','The remaining arbitrary-prime-set classification',r'''
The assertions above prove emptiness for $J_C$-large sets (once
the stated transport theorem is inserted), infiniteness for
singletons, and a finite-or-infinite dichotomy. They do not decide
the alternative for every arbitrary nonempty prime set that is
neither a singleton nor $J_C$-large. That additional classification
asked in A12 remains unproved in this audit.
''',r'''
The remaining obstruction is exact: the Kummer comparison confines a
possible exceptional pair to a fibre over complementary-prime torsion,
but when the complementary Tate representation is faithful its kernel
gives no proper field supporting those pairs. The single-prime central
arithmetic subgroup proof cannot be applied to a multi-prime completion:
its automorphism group need not have a pro-$\Sigma$ kernel on a finite
Frattini quotient. Neither assertion is silently assumed. The next
approach would be to classify the kernel of the full outer Frobenius
action for these prime sets, or to establish sparse support of the
possible point-pair differences along a constant-field tower.
''',['A12'],['A.CR10','A.CR13'],status='Open')

out=[r'\subsection{The cuspidal criterion and its arithmetic inputs}',
     r'We retain the whole arithmetic Galois quotient throughout this subsection.',
     r'The manuscript question addressed is cote~149, scan~36: can the covering condition force the equality of the two points?']
for item in items:
    out.append(r'\begin{claim}{'+item['id']+'}{'+item['status']+'}{'+item['title']+'}')
    out.append(item['statement'].strip())
    out.append(r'\end{claim}')
    if item['status'] != 'Open':
        out.append(r'\begin{proof}')
    else:
        out.append(r'\paragraph{State of the unresolved assertion.}')
    out.append(latex(item['proof']))
    if item['status'] != 'Open':
        out.append(r'\end{proof}')

(ROOT/'sections/A_criterion.tex').write_text('\n\n'.join(out)+'\n')
metadata=[{k:v for k,v in item.items() if k!='proof'} for item in items]
(ROOT/'notes/criterion_statements.json').write_text(json.dumps(metadata,indent=2)+'\n')
print('Wrote sections/A_criterion.tex with',len(items),'numbered statements.')
print('Wrote notes/criterion_statements.json.')
