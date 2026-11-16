#!/usr/bin/env python3
"""Primary reader's final notation, abbreviation and doubt-register decisions."""
from pathlib import Path
from datetime import datetime, timezone
import json, re, importlib.util

root=Path(__file__).resolve().parents[1]
np=root/'records/notation.md'
s=np.read_text()
s=s.replace('# Working notation register','# Final notation register')
s=s.replace('Readings are based only on the supplied scans.',
'''Readings are based only on the supplied scans. The primary reader compared recurring forms before the freeze, after the second visual reading of all 46 pages. Differences retained below reflect visible variants or explicit doubts, not normalization from mathematical expectations.

## Cross-page alphabet and punctuation decisions

- Straight divisor-bundle L is `\\underline L`; curved Lie and graded-quotient letters are `\\mathcal L`, with the independent underline retained as `\\underline{\\mathcal L}` where visible. The lower-half graded quotients on 006 were compared directly with 007 and corrected to the curved form. Ordinary L in the field-level argument on 007 remains straight.
- Script E in the elliptic-curve section is `\\mathcal E`; typed module E remains ordinary E. The doubled-looking affine-space E on 011 is explicitly `\\unsure{\\mathbb E|E}`. It is never replaced by A.
- The independently doubled diagonal of handwritten Z is `\\mathbb Z`, including the quotient-group diagrams. Filled/retraced Z on 019 and the live Z_2 on 032 retain explicit plain/doubled-letter alternatives. Typed double underlines under Q and Z on 035 and 037 remain `\\underline{\\underline Q}` and `\\underline{\\underline Z}`.
- Most projective-space P letters have one stem and are ordinary P. The possibly doubled stem on 005 is `\\unsure{\\mathbb P|P}`; the reinforced central P on 050 is `\\unsure{\\mathbf P|P}`. The thin marginal P on that same leaf remains plain. G_m uses ordinary G, distinct from the ornate symmetric-group sign `\\mathfrak S`.
- Underlined structure-sheaf O is `\\underline O`, not calligraphic O. The typewritten m and n on the n°276 sheets are upright `\\mathrm m`, `\\mathrm n`; the underlined ideals on n°272 are separately `\\underline{\\mathrm p}` and `\\underline{\\mathrm m}`.
- Short slanting accents are primes; pullback stars are `^*`; circumflexes are hats; the visibly wavy initial-form accents on 049 are tildes, while the straight accents on 047 are bars. No exponent was converted to an exclamation mark from mathematical context.
- Double quotation marks are two opening backticks and two closing apostrophes. The detached double-stroke repetition mark on 019 is retained as a repetition mark, not paired with invented closing quotation marks.
- Arrowheads, equal signs, inclusions and headless strokes are distinguished in the code. A headless handwritten correspondence is not silently promoted to a map. Repeated equation number (11) on 040 is retained.
- Abbreviations remain unexpanded in the LaTeX. Their proposed expansions are listed separately below in the final doubts document.''')
s=s.replace('The tangent sheaf glyph is very stylized; provisional underlined T, with an explicit doubt at first occurrence.',
            'The tangent-sheaf glyph is very stylized; compared with 007 and retained as underlined T, with the script-T alternative explicitly marked at its first occurrence.')
s=s.replace('The manuscript changes between calligraphic L and an underlined ordinary L in the graded algebra discussion. This difference is retained pending the cross-page ink audit.',
            'The upper graded quotients have curved L without a separate underline; the lower graded quotients have curved L with an independent underline. Comparison with 007 resolved the latter as underlined calligraphic L, not underlined ordinary L.')
s=s.replace('Underlined curved L in the corollary and derivation formula is represented `\\underline{\\mathcal L}`. Straight L and curved L must be rechecked across scans 004–007 before freeze.',
            'Underlined curved L in the corollary and derivation formula is represented `\\underline{\\mathcal L}`. Its shape was compared directly across 004–007; the straight L in the direct proof is a visible variant, not silently unified.')
s=s.replace('Affine space handwritten E, not A.','Affine-space letter is E, not A; its doubled-looking left stroke is explicitly uncertain between mathbb E and plain E.')
s=s.replace('Continue ornate symmetric-group glyph as \\mathfrak S_3, pending full consistency audit.',
            'The ornate symmetric-group glyph was compared with 028–030 and the later torsor pages: continue \\mathfrak S_3. This is distinct from plain G in the extension diagram.')
s=s.replace('A replacement invariant appears i while subsequent occurrences look j; do not normalize without visual audit.',
            'The replacement invariant was visually compared with the later occurrences: initial i and later j remain different, with explicit alternatives where retraced. No normalization between them is made.')
s=s.replace('typewritten ideal m is Gothic; Lie algebra g plain italic, as scan 045.',
            'typewritten ideal m is upright roman, compared with 020, 024, 026 and 049; Lie algebra g remains plain, as scan 045.')
s=s.replace('Local ring O is plain capital O, unlike sheaf underlined calligraphic O.',
            'Local ring O is plain capital O; the sheaf letter is the same plain O with an independent underline.')
np.write_text(s)

spec=importlib.util.spec_from_file_location('consolidate',root/'scripts/consolidate_doubts.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
rows=[json.loads(x) for x in (root/'records/doubts.jsonl').read_text().splitlines() if x.strip()]
updates={
 1:('cohomolgt plats en ttes dimension','cohomologt; toute; cancellation obscures the endings'),
 4:("d'injections linéaires","d'injection; final word and plural endings faint"),
 38:('BXY² and CY³ (alternative CY²); cancelled X²+AXY²','The small exponents are retained from the ink; the first cancelled symbol is overwritten'),
 120:("permutant à : S_6 (c'est d'ailleurs le seul, sauf","S_3; avec; the parenthesis continues on scan030; no editorial ellipsis substitutes for words"),
 131:('il est / est isomorphe / encore','qui est under the cancellation; the supralinear replacement is retained at its visible attachment'),
 181:('À déduire des formalismes','À déduire les formules; the phrase continues on scan046'),
 206:('Donn. non canoniq. par quoi','Donn. non canonique; possibly Donc; final two short words exceptionally uncertain')}
for i,(reading,alt) in updates.items():
    rows[i-1]['reading']=reading;rows[i-1]['alternatives']=alt
rows.sort(key=lambda r:int(r['scan']))
cell=mod.cell
out=['# MPL_62_002-050: Notation, doubts and abbreviations','','## Notation table','',
     'This is the package-wide notation table finalized before the context archive was opened. Font choices and retained variants were compared by the primary reader against the supplied images.','',
     '| Scan or scope | Reading and LaTeX encoding |','|---|---|']
out += ['| '+cell(a)+' | '+cell(b)+' |' for a,b in mod.notation_rows(s)]
out += ['','## Reader’s doubt register','',
        'Approximate locations refer to the manuscript layout. This table records uncertain words, symbols, attachment, cancellation extent and graphic features, including decisions resolved during the visual audit. Earlier working observations have been reconciled here with the final page files; their original versions remain in the work records. Confidence concerns the reading, not the validity of the mathematics.','',
        '| File | Scan page | Approximate line or location | Final reading or retained decision | Alternatives or qualification | Confidence |',
        '|---|---:|---|---|---|---|']
for r in rows:
    out.append('| '+' | '.join(cell(v) for v in ['62.pdf',f"{int(r['scan']):03}",r['line'],r['reading'],r['alternatives'],r['confidence']])+' |')

abbr=[
('alg.; alg. with superscript t','005, 050','algébriquement','high'),
('Br.','042','Brauer, in Br. Severi','high'),
('C.Q.F.D','035',"ce qu’il fallait démontrer",'high'),
('can.','034','canoniquement','high'),
('canoniq.','050','canonique; the reading of the abbreviated form is uncertain','low'),
('car.; car','007, 008, 015, 017, 030, 032, 042, 044, 050','caractéristique','high'),
('cf.','010, 022, 029','confer; compare / see','high'),
('Ch.; Chap.','029, 041, 043','chapitre','high'),
('chgt','017','changement','high'),
('coeff.','011, 012','coefficients','high'),
('coh.','005–007','cohomologiquement in coh. plat; cohomologique in platitude coh.','high'),
('cohomolgt / cohomologt','004','cohomologiquement; exact abbreviated spelling uncertain','medium'),
('comm.','006','commutative','high'),
('comp.','042','compatible, possibly a different compressed word; unfinished parenthesis','low'),
('conv.','024','convergence','medium'),
('cor.','029, 031, 035, 037','corollaire','high'),
('diff','007','différentielle or différentiation; the cancelled abbreviation is not securely read','low'),
('dim','005','dimension','high'),
('Donn.','050','donnée(s), if the first word is correctly read; Donc remains possible','low'),
('ds','034','dans; this is an alternative in an uncertainty mark','medium'),
('déf.','007','définition','medium'),
('ens.; ens','012, 030','ensemble(s)','high'),
('etc','008','et cetera; the manuscript’s own abbreviation is retained','high'),
('except with superscript ns','030','exceptions','medium'),
('Exerc.','022','exercice(s)','high'),
('exp. car.','007','exposant caractéristique','high'),
('ext.; Ext.','015, 019','extension(s)','high'),
('faisc.','004','faisceau','high'),
('fid. plat','013','fidèlement plat; cancellation retained','high'),
('gal.','042','galoisiens / galoisien','high'),
('gr.; gr','019, 028','groupe; the repeated gr. gr. on 028 is uncertain','medium'),
('gr. ann.','006','probably gradué / anneau gradué associé; exact abbreviated expression unresolved','low'),
('hom','006, 007','homomorphisme(s)','high'),
('i.e.','004, 008, 009, 014, 015, 017, 022, 024, 030, 041, 042, 044, 050','id est; c’est-à-dire','high'),
('intr.','042','intrinsèque, possibly another adjective','low'),
('inv.','004, 005, 014','inversible','high'),
('inv.','007','invariante, qualifying a derivation','high'),
('isom.; isom','006, 012–014','isomorphisme / isomorphie, according to the construction','high'),
('loc.','004–006, 014, 016','localement','high'),
('m.','015','morphismes, if this alternative reading is right; not the ideal symbol m of the typed sheets','low'),
('mod.','029, 039, 049','modulo','high'),
('N.','022','probably an unfilled exercise-number reference, not a supplied exercise number','low'),
('N.B.','017','nota bene','high'),
('nilpotts','019','nilpotents','medium'),
('n°; n with superscript o or circle','reused typed sheets','numéro','high'),
('p.ex.','038, 040','par exemple','high'),
('pr','019','possibly pour; occurs only as an uncertain alternative to another reading','low'),
('pro','013','possibly the prefix pro-; cancelled, and no fuller word can be supplied','low'),
('prop.; Prop','005, 008, 009, 012, 029, 031, 033, 035, 037, 039, 043','proposition','high'),
('pt; pts','007, 010, 016, 028, 030, 032, 042, 044','point; points','high'),
('quelc','013','quelconque; the abbreviated reading is uncertain','medium'),
('repr.','012','représente / représenté; cancelled abbreviated word','low'),
('représ.','050','représentations, possibly another abbreviated noun','low'),
('resp.; resp with superscript t','024, 028, 031, 037, 049','respectivement','high'),
('rev.; revt; revêt; revêtts','030, 032, 036, 042, 046','revêtement(s)','high'),
('RR','005','Riemann–Roch','high'),
('s. s. s.','050','si et seulement si; unusual spacing/letter sequence retained','medium'),
('schém.','042','schéma; the abbreviated word itself remains uncertain','low'),
('ss-schéma; ss-groupe','042, 032','sous-schéma; sous-groupe','high'),
('ss élémts nilpotts','019','sans éléments nilpotents; the abbreviated phrase is uncertain','medium'),
('ssi','005, 007, 008','si et seulement si','high'),
('st.ble','030','stable','medium'),
('suppl.','009','supplément','medium'),
('surj.','013','surjective','high'),
('th.','033','théorème','high'),
('tjrs','032','toujours','high'),
('top.','022, 024','topologies / topologie','high'),
('Top. Gén.; Top.Gén.','041, 043, 045','Topologie générale, the cited work','high'),
('topologt / topol.?','043','topologiquement / topologique; faint handwritten annotation','low'),
('tt; tte; ttes','004, 005, 008, 010, 012, 013, 016, 017, 046','tout / tous; toute; toutes, according to the visible abbreviated form','high'),
('Évidt','042','Évidemment','high'),
('élémts','019','éléments','medium'),
('épim.','007','épimorphisme','medium'),
('Aut; Hom; id; GL; Max; Spec; Symm','mathematical operators, where present','automorphismes; homomorphismes; identité; groupe linéaire général; maximum; spectre; construction symétrique','high')]
out += ['','## Abbreviations and proposed expansions','',
        'Expansions are supplied only in this register, never in the transcription. A low-confidence entry may concern both the ink and the expansion. Mathematical letter names, sentence-final full words, and accidental lexical candidates are excluded.','',
        '| Form as encountered | Scan(s) | Proposed expansion or explanation | Confidence |','|---|---|---|---|']
out += ['| '+' | '.join(cell(v) for v in row)+' |' for row in abbr]

def brace_arg(src,start):
    assert src[start]=='{'
    depth=1;i=start+1
    while i<len(src):
        if src[i]=='\\':
            if i+1<len(src) and src[i+1] in '{}%':i+=2;continue
        if src[i]=='{':depth+=1
        if src[i]=='}':
            depth-=1
            if not depth:return src[start+1:i],i+1
        i+=1
    raise ValueError('unclosed macro argument')
inline=[]
for path in sorted((root/'pages').glob('*.tex')):
    src=path.read_text();scan=int(re.search(r'scan(\d+)',path.name).group(1))
    for m in re.finditer(r'\\(unsure|illegible)\{',src):
        arg,end=brace_arg(src,m.end()-1)
        inline.append((scan,src.count('\n',0,m.start())+1,m.group(1),arg))
out += ['','## Complete index of inline uncertainty marks','',
        'This mechanical index includes every `\\unsure` and `\\illegible` occurrence in the final page files, including nested marks, cancelled passages, formulas, and diagram labels. Locations are exact lines in the saved page LaTeX, not a claim to reproduce manuscript lineation; the preceding reader’s table supplies the manuscript-location descriptions and confidence judgments. The vertical bar inside an argument separates the preferred reading from its alternative.','',
        '| File | Scan | Saved LaTeX line | Macro | Exact argument |','|---|---:|---:|---|---|']
out += ['| '+' | '.join(cell(v) for v in ['62.pdf',f'{n:03}',line,'\\'+macro,arg])+' |' for n,line,macro,arg in inline]
out += ['','## Legibility and limits','',
        'The typed reused sheets are generally much more legible than the rapid manuscript prose, although type defects, overtyping, punctuation, underlines, and added handwriting still create local doubt. The handwritten mathematical displays are often clearer than their connecting prose. Long near-horizontal pen movements can conceal word endings; neither grammatical agreement nor mathematical plausibility has been used to silently complete them.',
        '',
        'I trust least the intertwined revisions on scans 006, 009, 013–017; the compressed Kummer qualifications and lower diagram on 019; the right-edge naming note on 028 and faint margin on 030; the structural-object wording on 042; and the small interlinear insertion near the bottom of 050. Those passages carry explicit doubt marks. The final two words attempted as “par quoi” on 050 are especially insecure. The three physically unreadable cancelled words on 006 are the only use of \\illegible; no formula or diagram symbol has been replaced by that macro.',
        '',
        'All 46 pages received a second visual reading by the same primary reader, and recurring alphabets and accents were compared before freezing. TikZ reproductions preserve the observed shapes, labels, connections, and rough relative placement; they are approximations of the pen drawings, not facsimiles. Compilation verifies syntax only. The presence of uncertainty marks and a complete inventory does not certify an error-free transcription or an independently reviewed reading.',
        '',
        f'The final register contains {len(rows)} detailed reader observations and {len(inline)} inline uncertainty occurrences. Repetition and nested marks are counted separately in the latter figure.','']
target=root/'MPL_62_002-050_doubts.md'
target.write_text('\n'.join(out))
mod.abbreviation_candidates(root)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:
    f.write(f'final doubts and abbreviations completed {now}; {len(rows)} reader observations; {len(inline)} indexed inline uncertainty marks; context remains closed.\n')
print(json.dumps({'output':str(target),'reader_observations':len(rows),'inline_marks':len(inline),'abbreviation_entries':len(abbr),'time_utc':now}))
