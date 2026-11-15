#!/usr/bin/env python3
"""Build a complete occurrence index of the root reader's marked doubts.

No image processing, OCR, outside text or contextual correction is performed.
Confidence and notation comments record the root reader's visual judgments.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent
PACKAGE = 'MPL_33_002-049'

NOTATION = r'''# Notation table and doubts

## Package notation table

This table was maintained during the single ordered reading and completed in the cross-page review before the transcription was frozen and before the context archive was opened. Differences listed below are deliberate distinctions in the visible writing; they are not harmonizations of the mathematics.

| Recurring visible form | LaTeX used | Scope and visual distinction |
|---|---|---|
| Site suffix ét | `X_{\mathrm{ét}}` | Roman, accented suffix; distinct from an analytic superscript. |
| Wavy stroke over the site letter | `\widetilde X_{\mathrm{ét}}` | Topos notation on scan002; the wavy stroke is retained. |
| Plain capital letters | `X`, `Y`, `S`, `A`, `F`, `G`, `R`, etc. | Plain capitals are not made script or doubled merely from their mathematical role. The typed ambient real-space letter is plain `R`, including scans025,031,049. |
| Doubled integer letter | `\mathbb Z` | Handwritten doubled diagonals, checked on scans012,014,026,028,030,032,034,036,044,048. The typed lattice pages retain their plain `Z`. |
| Doubled complex-field letter | `\mathbb C` | Live passages on scans006 and020 have a second left stroke. The two single-curve C's in scan006's cancelled analytic paragraph remain plain `C`. |
| Doubled projective letter | `\mathbb P` | Scan034, including the cancelled symbol. |
| Doubled hypercohomology H | `\mathbb H` | Scan040: both spectral-sequence H symbols have doubled left stems, confirmed in an enlarged crop; the first is heavily retraced. |
| Script sheaf letters | `\mathcal O`, `\mathcal H` | Structure-sheaf O on the handwritten pages; cohomology-sheaf H on scan042. No Gothic alphabet was confidently identified. |
| Underlined mathematical objects | `\underline{...}` | Underline is not converted into a script alphabet: e.g. local cohomology, local fundamental class, typed ideals and categories. |
| Upper and lower stars | `f^*`, `f_*` | Read at their actual vertical position; a dual lattice star is also retained as a star. |
| Compact-support exclamation | `R^q_!f_*`, `R_!f_*`, `f_!` | The exclamation belongs below R or f where drawn. Headers on scans014 and018 were specifically rechecked. Deleted exclamations remain inside `\deleted{...}`. |
| Prime and double prime | `'`, `''` | Distinct from exclamation marks in objects, maps, lattices, and spectral-sequence labels. |
| Plus sign as superscript | `g^+` | Scan044: retained as a visible plus, without changing it to the conventional inverse-image star. |
| Rank ell and handwritten l | `\ell`, `l` | Typed root-system ranks use ell, including the quotient n/ell on scan031. The handwritten l-adic program on scan002 retains its plain l. |
| Greek root-coordinate letter | `\varepsilon_i` | Repeated typed root-coordinate letter. The special generator on scan017 has `\unsure{\xi_i|\varepsilon_i}` because its strokes do not decide. |
| Other Greek letters | `\alpha`, `\beta`, `\delta`, `\lambda`, `\mu`, `\nu`, `\omega`, `\pi`, `\psi`, `\rho`, `\sigma`, `\upsilon`, `\varphi`, `\xi`; `\Delta`, `\Gamma`, `\Phi` | Distinct forms retained rather than inferred from a formula. Specific nu/upsilon and delta/epsilon ambiguities are indexed below. |
| Local/global fundamental-class letter | `\unsure{\gamma|\sigma}` | Consistent uncertainty on scans024,026,028,030; underlining and the order Y/X or X/Y are transcribed independently. The different typed superscript on scan009 remains sigma/gamma, in that order. |
| Rounded complex argument | `\unsure{G|C}` | Scan040 throughout: the repeated glyph remains unresolved. It is not settled by the expected derived-Hom formula. |
| Quantifier and abbreviated tout | `\forall` or `\unsure{\forall|\text{tt}}` | The uncertain small marks on scans016 and028 remain explicit; written words are not replaced by quantifiers. |
| Headed arrow | `\longrightarrow`, TikZ `\arrow[...]` | Direction and head are reproduced from the image. A mathematical expectation does not supply a missing head. |
| Unheaded connector | `\mathbin{-}` or TikZ `dash` | Plain shafts remain plain; uncertain shafts are indexed, particularly scans002,004,008. |
| Injection and double arrow | Hook decoration, `\Longrightarrow`, `\simeq`, as visible | A hook or isomorphism sign is not supplied merely because an immersion or isomorphism is expected. |
| Inequalities | `>`, `\geq`, `<`, `\leq`, `\ne` | Read separately. Scan010 retains the greater-than/greater-or-equal doubt; the surprising typed inner product on scan049 remains −1. |
| Limit arrows | `\varinjlim`, `\varprojlim`, or explicitly doubtful Lim with its lower stroke | Small arrows on scans002,004,008 remain marked where their direction is uncertain. |
| Bar, hat and tilde | `\bar`, `\overline`, `\hat`, `\tilde`, `\widetilde` | Preserve distinct accents on geometric points, compactifications, algebras, and highest roots. |
| Double quotation marks | Two backticks and two apostrophes | Used throughout for drawn double quotation marks. The doubled apostrophe/double stroke used as a ditto in scan012 is retained in place. No unobserved guillemets have been introduced. |
| One or two underlines | `\uline{...}`, `\uuline{...}` | Extent checked independently of grammatical phrases; double underlines retained on scans004 and038. |
| Cancellation versus insertion | `\deleted{...}`, `\inserted{...}` | Nested states are preserved, including changes inside cancelled paragraphs. A whole crossed-out typed sheet on scan047 remains a reused typed sheet and is transcribed in full. |
| Marginal content | `\margin{...}` | Content intended as a local insertion is attached at its caret; independent notes remain marginal. |
| Source abbreviation | Literal abbreviated spelling | Expansions appear only in the abbreviation table below. |

## Doubt register

Each occurrence of `\unsure` has its own row, including repetitions and cancelled matter. The first reading follows the ink; an alternative is not silently promoted because it would make the mathematics conventional. “Not resolved” means that no defensible second reading was identified, not that text was omitted. Confidence concerns the proposed visual reading, not the truth of a mathematical claim.

The position column gives an approximate part of the page in reading order, followed by the exact line of the individual `.tex` file as a stable locator. These are not claimed to be physical manuscript line numbers: diagrams, margins, and paragraphs do not share a uniform line grid. Scan003 is especially non-linear, and its local annotation is additionally identified in the final column.

| File/cote | Scan | Approximate position; exact TeX line | Reading | Alternatives | Confidence | Local context |
|---|---:|---|---|---|---|---|
'''

ABBREVIATIONS = [
 ('Alg.; alg.', 'algèbre; in a bibliographic heading, Algèbre'),
 ('Alg. comm.; alg. comm.', 'Algèbre commutative / algèbre commutative'),
 ('an (superscript)', 'analytique'),
 ('augm.', 'augmentée'),
 ('bilin.', 'bilinéaire'),
 ('can.', 'canonique'),
 ('car.; car', 'caractéristique(s)'),
 ('cat.', 'catégorie(s)'),
 ('cf; cf.', 'confer / compare'),
 ('chgts', 'changements'),
 ('coalg.', 'coalgèbre'),
 ('coh.; coh', 'cohomologie / cohomologique'),
 ('comm.', 'commutative'),
 ('conn.', 'connexes'),
 ('cons.; constr.', 'constructible(s); construction in par constr. on scan009'),
 ('constructiblt. (doubtful)', 'constructibilité'),
 ('cor.; Cor.', 'corollaire'),
 ('cpt.', 'compact'),
 ('ct.; cst; cts', 'constant; constant; constants (the written order cts is retained)'),
 ('C fl. (doubtful, cancelled)', 'possibly classe(s) fondamentale(s); the reading and expansion are low confidence'),
 ('chap.', 'chapitre'),
 ('déf.', 'définition'),
 ('Défin.', 'Définition'),
 ('deg.', 'degré'),
 ('Dém', 'Démonstration'),
 ('dim; dim.; Dim.', 'dimension'),
 ('div.', 'diviseurs'),
 ('éd.', 'édition'),
 ('élts; élts.', 'éléments'),
 ('ens', 'ensembles'),
 ('ét (site suffix)', 'étale'),
 ('Ex; Ex.; ex.', 'Exemple / exemple; exact in [ex. et en F] on scan018'),
 ('ext.; Ext.', 'extension; Extension on scan034, distinct from mathematical Ext'),
 ('factⁿ', 'factorisation'),
 ('fin', 'fini / finie, according to its visible context'),
 ('Gaga', 'Géométrie algébrique et géométrie analytique; used here as a comparison label'),
 ('géom.; Géom.', 'géométrique(s); Géométrie in a bibliographic title'),
 ('gr.', 'groupe; gradué in a grading context'),
 ('hom; hom.', 'homomorphisme'),
 ('hyp; hyp.', 'hypothèse(s)'),
 ('i.e.', 'id est / that is'),
 ('imm.', 'immersion'),
 ('int. complète', 'intersection complète'),
 ('isom; isom.; Isom.', 'isomorphisme(s); isomorphe(s)'),
 ('loc; loc.', 'localement'),
 ('localt', 'localement (scan024)'),
 ('spts', 'supports (scan028)'),
 ('slt', 'seulement (scan009)'),
 ('immers', 'immersion (scan020)'),
 ('fond', 'fondamentales (scan036)'),
 ('codim', 'codimension'),
 ('mod.', 'modulo'),
 ('mult.', 'multiplication'),
 ('n°, nᵒ, nᵒˢ', 'numéro, numéros'),
 ('NB; N.B.; NB.', 'nota bene'),
 ('noeth.', 'noethérien(s)'),
 ('obt. (doubtful)', 'obtient'),
 ('O.K.', 'a mark of assent, “okay”; its precise mathematical force depends on the sentence'),
 ('ouv', 'ouverte'),
 ('P.; p.', 'page; par in p.ex.'),
 ('p.ex.; par ex.', 'par exemple'),
 ('Pb', 'Problème'),
 ('présch; présch.', 'préschéma(s)'),
 ('proj.', 'projectif(s)'),
 ('prop. (in a reference)', 'proposition'),
 ('prop. (morphism/property)', 'propre'),
 ('pt; pt.', 'point'),
 ('qconques; quelc; quelc.', 'quelconques'),
 ('qu.', 'quasi'),
 ('qu. cpt.; qu. sép.', 'quasi compact; quasi séparé'),
 ('rés.; rés', 'résiduel(le)(s); résolution(s), according to the sentence'),
 ('resp.', 'respectivement'),
 ('sép.; sep.', 'séparé(e), especially séparablement in corps sép. clos'),
 ('SGA', 'Séminaire de géométrie algébrique'),
 ('sing.', 'singularités'),
 ('spect.', 'spectre'),
 ('ssi', 'si et seulement si'),
 ('suppᵗˢ (doubtful)', 'supports'),
 ('t.f.', 'type fini'),
 ('th; th.; Th.; théor.', 'théorème'),
 ('tjrs (doubtful)', 'toujours'),
 ('top.', 'topologique'),
 ('tt (alternative reading)', 'tout; retained only as an alternative to a visible quantifier-like sign'),
]

def balanced_arguments(s, name):
    for m in re.finditer(r'\\'+name+r'\{', s):
        i=m.end(); j=i; level=1
        while level:
            c=s[j]
            if c=='\\' and j+1<len(s) and not s[j+1].isalpha():
                j+=2; continue
            if c=='{': level+=1
            elif c=='}': level-=1
            j+=1
        yield m.start(),s[i:j-1]

def esc(s):
    return s.replace('|',r'\|').replace('\n',' ').replace('`','&#96;')

def confidence(scan,value):
    low = {
      2: {'uniquement','-','\\operatorname{Spec}'},
      4: {r'\mathop{\mathrm{Lim}}\limits_{\longleftrightarrow}'},
      6: {"résolution sing. pour l'hyp.",'de|les','algèbre','À chaque'},
      8: {'On peut notamment','Il y a aussi des','topos relatifs'},
      12:{'Désignons|Choisissons','un|$\\forall$'},
      14:{'bons préschémas'},
      16:{'U|X',r'\forall|\text{tt}'},
      18:{'bons présch','espaces'},
      20:{'égales que',r'\xi'},
      22:{'et',r'\sim',r'X,i_*(G_{mU}^*)'},
      28:{'$\\forall x$ pt de $X$','pt sur $k$, d\'où','on obt.|on obtient','des C fl. de'},
      36:{'+)',r'H^{2d}_Y','A'},
      38:{'non par des rés. projectives mais'},
      47:{"p(N'_k)=",r'\operatorname{gr}'},
      48:{"n'est|est",'vaut|reste','constructiblt.|constructibilité'},
    }
    if scan==3 or value in low.get(scan,set()): return 'low'
    if value in {'t.f.','propre','Défin.','imm.','18','connues','coh.','supp$^{ts}$'}: return 'high'
    return 'medium'

rows=[]
for p in sorted((ROOT/'pages').glob('*.tex')):
    scan=int(re.search(r'scan(\d+)',p.name)[1]);s=p.read_text();ls=s.splitlines()
    for off,value in balanced_arguments(s,'unsure'):
        line=s.count('\n',0,off)+1
        frac=off/max(1,len(s))
        zone='upper part' if frac<.34 else 'middle part' if frac<.68 else 'lower part'
        # Order-based zones are approximate; exact text line and context remain authoritative locators.
        local=ls[line-1].strip()
        if len(local)>170: local=local[:167]+'…'
        first,*alt=value.split('|')
        rows.append({'scan':scan,'line':line,'value':value,'reading':first,
                     'alternatives':' | '.join(alt) if alt else 'Not resolved',
                     'confidence':confidence(scan,value),'position':zone,'context':local})

out=[NOTATION]
for r in rows:
    out.append('| 33 | %03d | %s; L%d | `%s` | %s | %s | `%s` |\n' % (
        r['scan'],r['position'],r['line'],esc(r['reading']),
        ('`'+esc(r['alternatives'])+'`') if r['alternatives']!='Not resolved' else 'Not resolved',
        r['confidence'],esc(r['context'])))
out.append(f'\n**Register count:** {len(rows)} marked occurrences across the 48 scan pages. No `\\illegible` macro is used: even badly cancelled material has a proposed, explicitly uncertain reading. This does not mean that all such readings are recoverable with confidence.\n')
out.append('\n## Abbreviations encountered\n\nCapitalization and optional stops vary in the source. The table groups visibly related forms for consultation only; the transcription does not expand them. Ordinary mathematical operators (Hom, Ext, Tor, Ker, Tr, Spec, Gal, Ens) are retained as notation, not expanded into prose.\n\n| Written form | Proposed expansion or interpretation (only here) |\n|---|---|\n')
for a,b in ABBREVIATIONS:out.append(f'| {esc(a)} | {esc(b)} |\n')
out.append(r'''
## Legibility and limits of confidence

All 48 supplied whole pages and both supplied halves of each page were inspected by the same reader in scan order. Every page then received an independent rereading against its images; the page records contain the observations made during those passes. No OCR or recognition software was used. Rotation and enlargement of image crops were used only for direct visual inspection.

The typed root-system sheets are usually the most legible, but individual typefaces, damaged letters, and source anomalies still require caution. Several surprising literal readings were rechecked and retained, including “vocables” and “(12+1)” on scan023, a negative inner product and the ambient exponent 4 on scan049, the xi/epsilon ambiguity on scan017, and “injectives” in the left-derived-functor discussion on scan038. None was corrected from an expected mathematical statement. The typed English pages are clear enough to preserve their argument, but the isolated T/F and delta/epsilon switches on scan039 remain doubtful.

The least secure material is the rough, multiply oriented diagram sheet (scan003), the diagonal analytic-comparison marginalia and cancelled paragraph (scan006), the cancelled opening and small diagram annotations on scan008, the insertion about purity hypotheses (scans014 and018), the dense cancellations around fundamental classes (scans022 and028), the patched purity/trace diagram (scan036), the small spectral-sequence exponents (scan040), and the heavily crossed-out formulas on the reused typed sheet (scan047). The gamma/sigma fundamental-class letter remains unresolved across its occurrences rather than being chosen from mathematical familiarity. Several short word endings and cramped abbreviations on scan048 are also insecure.

Diagram topology, arrowheads, inserted labels, and line crossings were checked separately from the surrounding prose. TikZ reproduces the observed geometry approximately rather than tracing every wobble of a pen. Headless shafts, extra parentheses, unfinished words, and unmatched written delimiters have been retained when visible; LaTeX grouping is syntactically balanced without completing the mathematical text. Faint reverse-side show-through is not counted a second time as foreground writing. An inventory marked “yes” records that an element has been represented and checked; it is not a claim of infallibility about its decipherment.

## Audit trail

`records/scanNNN.json` preserves each page's transcription, inventory, and visual observations. `records/uncertainty_index.json` is the machine-readable counterpart of this complete occurrence register. The notation comparison and completion of this register precede the freeze entry in `progress.log`; context-based suggestions, if any, belong exclusively in the research notes.
''')
(ROOT/f'{PACKAGE}_doubts.md').write_text(''.join(out),encoding='utf-8')
(ROOT/'records/uncertainty_index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote {len(rows)} doubt rows and {len(ABBREVIATIONS)} abbreviation entries.')
