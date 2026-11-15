"""Assemble post-freeze research notes. Never writes any transcription file."""
from pathlib import Path
import re

work = Path(__file__).resolve().parents[1]
rec = work / 'records'

def read(name):
    return (rec/name).read_text()

def replace_once(text, old, new):
    assert old in text, old
    return text.replace(old, new, 1)

def between(text, start, end):
    return text.split(start,1)[1].split(end,1)[0].strip()

def root_math(text):
    # Repair research-note delimiters only. Balanced parentheses containing TeX,
    # or explicitly listed scalar expressions, are math; prose parentheses stay.
    text = text.replace(r'\)', ')')
    scalar = {'p','p=2','p=1,X=\\mathbf P^1','u','v','-u','K','f','G','V','sV',
              '4','5','R=R','i,j','p','bAa,baA,aAb,Aba','q=3','1|i','j',
              'y_1+y_q=0','y_2','-y_1=y_3','i+p','2i+2p','p_i'}
    out=[]; i=0
    while i<len(text):
        if text[i]!='(':
            out.append(text[i]); i+=1; continue
        j=i+1; depth=1
        while j<len(text) and depth:
            if text[j]=='(': depth+=1
            elif text[j]==')': depth-=1
            j+=1
        if depth:
            out.append(text[i]); i+=1; continue
        inner=text[i+1:j-1]
        is_math=('\\' in inner or '^' in inner or '_' in inner or inner in scalar)
        if is_math and '\n\n' not in inner:
            out.extend(['$',inner,'$'])
        else:
            out.append(text[i:j])
        i=j
    return ''.join(out)

root = root_math(read('research_root_observations.md'))
root = root.replace('That line may still have the immediately preceding example',
                    'The immediately preceding example is')
root = root.replace('in view, and the formula for the lattice',
                    '; the formula for the lattice')
root = root.replace('$ ;', '$;')
root = root.replace('un-oriented lattice', 'unoriented lattice')
cycle = between(root,'## Cycle classes, orientations and comparison maps',
                '## Reused typescripts, cancelled material and source questions')
reused = between(root,'## Reused typescripts, cancelled material and source questions',
                 '## Title sheets, headings and page counts')
titles = root.split('## Title sheets, headings and page counts',1)[1].strip()

rh = read('research_real_hodge.md')
rh_items = '### RH03 ' + between(rh,'### RH03','## Appendix A')
rh_items = re.sub(r'\bN (?=[A-Z]|§)', 'PN ', rh_items)
rh_items = rh_items.replace('with its real algebraic polarization',
                          'equipped with a specified polarization morphism over R')
rh_items = rh_items.replace(r'\(H^{\unsure{*|0}}(X(\mathbf R),\mathbf Q)=V^f\)',
                           r'`H^{\unsure{*|0}}(X(\mathbf R),\mathbf Q)=V^f`')
rh_items = replace_once(rh_items,
    'These two explicit realizations show why the abstract group at the bottom of the diagram cannot by itself characterize the assertion \\(f_\\infty=1\\).',
    'The exact quotient characters from \\(\\mu_2\\times\\mathbf G_m\\) are \\(\\rho_T(a,t)=t\\) and \\(\\rho_L(a,t)=at\\); they send the same specified involution \\((-1,-1)\\) to −1 and +1, proving that these two identifications with the abstract group \\(\\mathbf G_m\\) do not identify its distinguished real Frobenius.')
rh_items = rh_items.replace('this particular linear action retains the involution while forgetting the possible component distinction recorded by the section class.',
    'this conjugation action on the abelianization retains the involution while forgetting the possible component distinction recorded by the section class; this calculation does not discard the section cocycle from the entire abelianized extension.')

rh_appendix = '## Appendix A ' + between(rh,'## Appendix A','## Author-marked qualifications')
# The four-row comparison table already contains the real-section row.
rh_appendix = re.sub(r'\n\| Linear statement and map \|.*?\n\nThe positive-form',
                    '\nThe positive-form', rh_appendix, flags=re.S)
rh_appendix = rh_appendix.replace('## Appendix C — Exact polarization/real-section row',
                                  '## Appendix C — Polarization and the action of a real section')

p = between(read('research_period_cocycles.md'),'## Observation register',
            '## Selected primary sources actually checked')
p = re.sub(r'\bC(\d\d)\b', r'P\1', p)
p = re.sub(r'\bSC\b', 'PN', p)
p = replace_once(p,
    'The selected pages do contain an explicit period-conjecture witness: the comparison point of $P_{v,k}$ is declared generic in “conjecture de transcendance N° 1”.',
    'The selected pages contain an explicit period-conjecture witness: “conjecture de transcendance N° 1” declares the comparison point generic, with genericity interpreted over the definition field $k_0$; the same $k$-valued point is closed after base change to $k$.')
p = replace_once(p,
    'The morphism $D_g:x\\mapsto x^{-1}g$ is an algebraic isomorphism with inverse',
    'The morphism $D_g:x\\mapsto x^{-1}g$ is an algebraic isomorphism over $k$ with inverse')
p = replace_once(p,
    'This concrete example shows why a minimal-transcendence-degree choice and a separate assertion about the Tate period must both be tracked; it supplies no interpretation of the author\'s unfinished “π transcendant” margin or a refutation of a fully specified conjecture on these pages.',
    'This is a curve-level test of the base-field qualification: applying its minimum to the manuscript\'s motive $M$, including $h^1(E_t)$, still requires an isogeny/descent argument, which the $j$-calculation does not supply. The unfinished “π transcendant” margin and the scope of the author\'s conjecture remain reading questions.')
p = p.replace('For a complete complex place $v$, the fibre of the orbit map',
    'For a complete complex place $v$, the fibre onto the orbit of the map')
p = p.replace('by the coordinate inclusion, but its compact-open integral product is not open for the latter product topology.',
    'by the coordinate inclusion, which omits the full-product tuple $(1/\\ell)_\\ell$; its compact-open integral product is not open for the latter product topology.')
p += '\n\n' + read('research_period_extra.md').strip()

mb = between(read('research_motivic_bridges_formatted.md'),'## Observation register',
             '## Compact comparison tables')
mb = mb.replace('with zero endpoint values.',
    'with $E(v_m)=0$ and $\\Lambda(v_0)=F(v_0)=0$.')
mb = mb.replace('**Explicit rational image calculation:**',
    '### MB03b — The two rational operator images have explicit matrix units\n\n'
    '**Kind:** own idea, explicit calculation. **Witness:** CT16/013–018,033; current 18/027. '
    '**Quote:** “ξ(Z(−1))” on 18/027. **Context search:** the `Lambda | sl_2 | Lefschetz | projecteurs` search recorded for MB03, CT16/013–018,033 and PN M02/R01; separately repeated for MB03b in `context_searches.jsonl`. '
    '**RS:** WG2 §2.3 #2, §2.4 #3 [unchecked]; PN M02 [lead]. '
    '**Relation:** verifies the rational operator-image comparison through actual maps. '
    '**Confidence:** high, from the matrix units and Casimir eigenvalues displayed below.\n\n')
for ident, reason in [('MB03','direct commutator calculations on every string basis vector'),
                      ('MB04','the displayed matrices and their action on the unit vector'),
                      ('MB05','the exponents on each graded summand'),
                      ('MB06','the cohomological degrees and the explicit nonidentity matrix'),
                      ('MB14','the explicitly computed kernel of conjugation')]:
    pat = r'(### '+ident+r' —[^\n]*\n\n)([^\n]*)(\n\n)'
    def add(m):
        line=m[2]
        if 'own' not in line.split('**Witness:**')[0]:
            line=line.replace('**Kind:** ', '**Kind:** own calculation / ',1)
        return m[1]+line+' **Confidence:** high; reason: '+reason+'.'+m[3]
    mb,n=re.subn(pat,add,mb,count=1)
    assert n==1, ident
mb = replace_once(mb, 'For proper smooth curves a morphism',
    'For smooth proper geometrically connected curves $X,Y$ of genus at least two over the same number field $K$, a morphism')
mb = mb.replace('the actual arXiv v4 PDF and the published PDF both confirm locator 5.10, while the retrieved HTML numbering is inconsistent with those checked PDFs.',
    'the actual arXiv v4 PDF and the published PDF both confirm PN\'s locator 5.10.')
mb = mb.replace('printed D', 'printed D')
mb = mb.replace('matching the operator content of printed B in Grothendieck\'s 1969 §3;',
    'matching the operator content of printed B in Grothendieck\'s 1969 §3;')
mb = mb.replace('The new 18 pages add no decisive witness for those two letters.',
    'Kleiman [K94, §5, p.17] verifies the printed meaning of D as equality of homological and numerical equivalence; the new 18 pages add no decisive witness for the remaining manuscript letters.')
mb = mb.replace('**Kind:** own calculation', '**Kind:** own idea (explicit calculation)')
mb = mb.replace('**Kind:** explicit calculation', '**Kind:** own idea, explicit calculation')
mb = mb.replace('\n\n On the model', '\n\nOn the model')

parts = [
 read('research_front_matter.md').strip(),
 '## 1. Cycle classes, orientations and comparison maps\n\n'+cycle,
 '## 2. Real structures, Hodge theory and the Oda comparison\n\n'+rh_items,
 '## 3. Periods, archimedean lattices and cocycles\n\n'+p,
 '## 4. Correspondence rings, motivic groups and the requested bridges\n\n'+mb,
 '## 5. Reused typescripts, cancelled material and source questions\n\n'+reused,
 read('research_self_flagged.md').strip(),
 '## 7. Title sheets, headings and page counts\n\n'+titles,
 read('research_register_impact.md').strip(),
 rh_appendix.strip(),
 read('research_bibliography.md').strip(),
 '## Reading questions and verification boundary\n\n'
 'All proposed scope checks, index questions and alternative contextual interpretations above remain in these notes. '
 'The page files and combined transcription retain the bytes frozen before the context was opened. '
 'The doubts file indexes all 268 uncertainty macros and records the least legible regions; '
 'the inventory records 624 elements over all 45 scans. '
 'A rendered LaTeX harness checked syntax and the diagram/drawing pages before freezing, '
 'and the final SHA-256 comparison is recorded in `progress.log` and `records/quality_checks.md`. '
 'The source-reading records, individual research contributions and their search records are retained under `records/`; '
 'this assembled notes file incorporates the cross-review corrections and controls the wording of the research conclusions.'
]
result='\n\n'.join(parts)+'\n'
assert result.count('### P17 —')==1
assert result.count('### C01 —')==1
(work/'MPL_18_018-062_notes.md').write_text(result)
print({'notes_bytes':len(result.encode()),'words':len(result.split()),
       'observation_headings':len(re.findall(r'^### (?:C|RH|P|MB|R|T|SF)\d',result,re.M))})
