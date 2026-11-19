#!/usr/bin/env python3
"""Root reader's explicit, ink-led final notation decisions; no OCR.

Run once before the freeze. The source crops were read personally by /root.
"""
from pathlib import Path
import json
from record_page import ROOT, rebuild, utc

assert not (ROOT/'records/frozen.sha256').exists(), 'Transcription already frozen'

def record(n):
    p=ROOT/'records'/f'scan{n:03}.json'
    return p,json.loads(p.read_text())

for n in (30,32,38,41):
    p,d=record(n)
    page=ROOT/'pages'/d['filename']
    s=page.read_text()
    if n==30:
        s=s.replace(r'^{\unsure{b|*|\varnothing}}',r'^{\unsure{\partial|b|*|\varnothing}}')
        for row in d['changes']:
            if 'exponent' in row['place'] or 'superscript' in row['place']:
                row['final']=r'\unsure{\partial|b|*|\varnothing}'
                row['evidence']+=' Final visual comparison with scan032: the small lower loop and rising hooked stroke favour partial; heavy retracing prevents resolution. evidence/notation_drap_crosspage.jpg'
        for row in d['doubts']:
            if row[0]=='Drap exponent':
                row[1:]=[r'\partial','b; *; empty-like sign','low','Same lower loop and rising hook as 032, but overtraced. The shared form is not enough to remove doubt.']
    if n in (38,41):
        s=s.replace(r'\unsure{\mathrm{Drop}|\mathrm{Drap}|\mathrm{Drp}}',r'\operatorname{Drap}')
        for row in d['changes']:
            if ('Drap' in row['final'] or 'Drop' in row['final']) and ('operator' in row['place'] or 'flag' in row['place'] or 'name' in row['place']):
                row['final']=row['final'].replace(r'\unsure{Drop|Drap|Drp}','Drap').replace(r'\unsure{\mathrm{Drop}|\mathrm{Drap}|\mathrm{Drp}}',r'\operatorname{Drap}')
                row['c_diff']=True
                row['evidence']+=' Final visual comparison: the same compact a between r and descending p occurs on 030, 032, 038 and 041; the label drapeaux below the 030 map supplies a written comparison. Resolved as Drap. evidence/notation_drap_crosspage.jpg'
        d['doubts']=[row for row in d['doubts'] if row[0] not in ('flag operator','flag name','Drap name','flag operator name')]
    # The two powerset glyphs have the same tall stem and extended cap, with
    # rounded/triangular bowls. No particular typeset script can be certified.
    if n==30:
        s=s.replace(r'\unsure{\mathcal P|\mathscr P}',r'\unsure{\mathcal P|\mathscr P|\mathrm P}')
        for row in d['changes']:
            if row['place']=='map, target alphabet':
                row['final']=r'\unsure{\mathcal P|\mathscr P|\mathrm P}'
                row['c_diff']=True
                row['evidence']+=' Compared with the angular P on 041: use one explicit font doubt rather than silently identifying a printed script family.'
        for row in d['doubts']:
            if row[0]=='target alphabet':row[2]=r'\mathscr P; \mathrm P'
    if n==41:
        s=s.replace(r'\unsure{\mathrm P|\mathcal P|\mathfrak P}',r'\unsure{\mathcal P|\mathscr P|\mathrm P}')
        for row in d['changes']:
            if 'alphabet' in row['place'] and 'P' in row['place']:
                row['final']=r'\unsure{\mathcal P|\mathscr P|\mathrm P}_2(L)'
                row['evidence']+=' Compared with 030: tall stem and extended cap, but no securely Gothic construction; the same explicit P-font doubt is used on both pages.'
        for row in d['doubts']:
            if 'P alphabet' in row[0] or row[0]=='power-set alphabet':
                row[1:3]=[r'\mathcal P',r'\mathscr P; \mathrm P']
    page.write_text(s)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

# Repair escaped apostrophes in apparatus strings (never in source witnesses).
for p in (ROOT/'records').glob('scan[0-9][0-9][0-9].json'):
    d=json.loads(p.read_text())
    def clean(x):
        if isinstance(x,str): return x.replace(r'\u0027',"'")
        if isinstance(x,list): return [clean(y) for y in x]
        if isinstance(x,dict): return {k:clean(v) for k,v in x.items()}
        return x
    p.write_text(json.dumps(clean(d),ensure_ascii=False,indent=2)+'\n')

notation=[
['Boundary sign','Looped partial sign before the letter, distinct from a mark above it',r'\partial T; \partial L','026–032, 039; extremes and generalized endpoint sets, without silently identifying their uses'],
['Frontier point','Compact detached point beyond the right end of the letter cap',r'T^\bullet; X^\bullet','026, 034, 039–040; second audit distinguishes this from a prime and from a centred accent'],
['Centred frontier point','Dot above the middle/right portion of the T cap, not beyond it',r'\dot T','039 cancelled Fr(T)=dot T; this visible positional variant is preserved'],
['Dot attachment at a union','Point between T-prime and the left side of a cup',r"\unsure{T'\dot\cup|{T'}^\bullet\underline{\cup}}",'027; unresolved attachment, not decided by the expected formula'],
['Prime','Detached elongated high stroke; occasionally retraced',r"T'; X'; X''",'027, 031–037; 033 meet-zero formula retains double-prime/single-prime doubt'],
['Interior','Small hollow high circle',r'X^\circ','033 retains circle/o doubt; 034 has hollow circles contrasting with solid frontier points'],
['Closure','Broad straight overbar covering its written operand',r'\overline X; \overline{X\vee Y}','033–039; scope follows each actual bar'],
['Earlier closure-like mark','Broad wavy upper stroke',r"\widetilde{T'}",'026 rotated NB; not flattened into an overbar'],
['Disjoint-union sign','Rounded cup with a separate heavy baseline',r'\underline{\cup}','026 box; not silently replaced by ordinary cup'],
['Set union versus lattice join','Rounded bowl versus two angular oblique legs',r'\cup; \vee; \bigvee','028–040; notably the rounded cups in the 033 De Morgan line are retained'],
['Intersection versus meet','Rounded arch versus angular inverted V',r'\cap; \wedge','028, 033–039; 039 opening equality uses cap'],
['Order signs','Single opposed oblique legs versus doubled legs',r'<; \ll','028–032; 028 initial less-than/prec doubt and 031 isolated single < remain'],
['Ambient order letter','Narrow looped L with a low rightward exit',r'L','026–041; no systematic conversion to calligraphic L'],
['Abstract moderate structure','Swept entry and two tall joined arches',r'\mathcal M','032–039; same chosen alphabet throughout, including nested subscripts and exponent labels'],
['Flag family','Round capital Phi with a descending upright and horizontal foot',r'\Phi','030–032, 038–039; not a lowercase varphi'],
['Components','Two tall uprights sharing a horizontal cap',r'\Pi_0','030, 032; capital resolved in both, local 0/o doubts retained'],
['Flag operator','D followed by r, a compact a, and a descending p',r'\operatorname{Drap}','030, 032, 038, 041; compared directly in evidence/notation_drap_crosspage.jpg, with drapeaux written below 030'],
['Flag superscript, early pages','Small lower loop with hooked rising stroke; 030 heavily retraced',r'\unsure{\partial|b|*|\varnothing}; \unsure{\partial|\alpha|b|*}','030, 032; partial favoured in both but unresolved. Do not impose the different-looking 038 glyph'],
['Flag superscript, later page','Dark short intersecting strokes',r'\unsure{*|K}','038; visibly different from the cleaner loop in 032'],
['Tronçon operator','Tr, with an additional rounded trace in the crowded later occurrence',r'\operatorname{Tr}; \unsure{\mathrm{Tro}|\mathrm{Tr}_0|\mathrm{Tr}}','030, 032 versus 038; extra trace not suppressed by harmonization'],
['Power-set letter','Tall upright stem and extended cap; bowl rounded in 030 and angular in 041',r'\unsure{\mathcal P|\mathscr P|\mathrm P}','030, 041; shared explicit font uncertainty, no securely Gothic form'],
['Epsilon','Small three-shaped curved letter',r'\varepsilon','030 exceptional endpoint set; 041 unordered pair'],
['Complement operation','Tall curved complementary-set operator with subscript',r'\complement_A; \complement_{\mathcal M_A}; \complement_{\mathrm{mod}}','036, 041; distinguished from a merely typed letter C'],
['Earlier complement notation','Large ordinary C with mod below it',r'C_{\mathrm{mod}}','031; adjoining argument remains U U)/(U)/U) doubtful'],
['Extreme-element names','Omega has a short double arch; alpha has a loop with a rightward tail',r'\omega; \alpha','026; written exclusions retained even where their order is surprising'],
['Changing letters','Earlier letter remains under the replacement diagonals',r'\deleted{U}X; \deleted{X}A; \deleted{Y}Z','030–031 and 035–037; unrevised U and stray X/Y are not globally corrected'],
['Quotation marks','Two short marks on each written side, sometimes only an opening pair',"``...''",'Throughout; no guillemets substituted; missing closing quotes not supplied'],
['Abbreviation endings','Small raised t, d, or ts; reduced unraised endings elsewhere',r'\textsuperscript{t}; \textsuperscript{d}; \textsuperscript{ts}','033–040; superscripts preserved, expansions confined to abbreviation table'],
['Equivalence abbreviation','Sometimes three joined hooked s-like strokes, sometimes two plus an i', 'sss; ssi','032–040; the visible distinction is preserved rather than standardized'],
['Revised numbers','Older numeral remains below/through the replacement',r'\deleted{...}...','033–034, 036–037; original and surviving numbers both retained'],
['Literal anomalous expressions','Clear marks conflicting with a plausible intended statement','non majoré/mijoré; 1_MA=X; ]t1,t3[; Fr X union Fr X','032, 035, 040, 034; interpretation is deferred to research notes, not used to change ink']
]
(ROOT/'records/notation.json').write_text(json.dumps(notation,ensure_ascii=False,indent=2)+'\n')
abbreviations=[
['abrég','abrégé / abrégation'],['adh.; adh','adhérence'],['alg.; Alg.','algèbre'],['autom.','automatiquement'],['b. / borne sup; borne inf','borne supérieure; borne inférieure (written forms vary)'],['can.; canonique','canonique; only the abbreviated form is expanded here'],['Card','cardinalité / cardinal'],['cf','confer, compare'],['comp.','composante(s)'],['compl.','complément / complémentaire'],['conn.','connexe(s)'],['Cor','corollaire'],['De =; de =','de même'],['def; déf','définition / par définition'],['dim','dimension'],['ds','dans (uncertain local abbreviated reading, 027)'],['él.; élém; élmt; élémt; élts','élément(s); exact written ending is retained in place'],['ens','ensemble'],['Ex','exemple'],['Fr','frontière'],['généralemt','généralement (ending uncertain in 031)'],['gr superscript d','grand'],['i.e.; i.e','id est, c’est-à-dire'],['inf; Inf','infimum / inférieur according to position'],['mod.; mod','modéré(e)(s)'],['mor superscript t','moralement (likely; 038)'],['mut.; mut superscript t; mutuell superscript t; mutuellemt','mutuellement'],['NB','nota bene'],['OK','okay, acknowledgement that the step is accepted'],['op.','opération(s)'],['OPS','on peut supposer'],['p.r.; par.','par rapport (the literal abbreviated forms vary)'],['pos.','position'],['Prop','proposition'],['ps.; ps.tr.; ps. tr.; psTronçon; pstronçon; pstr.','pseudo-tronçon(s); prefixes and spacing retained as written'],['pt; p superscript t; pts','point; points'],['qd / q','quand (uncertain abbreviated reading on 027)'],['rel.; rel superscript t','relative / relativement, according to syntax'],['sss; ssi','si et seulement si; the author’s differing letter forms are retained'],['strictemt','strictement (ending uncertain on 029)'],['sup; Sup','supremum / supérieur according to position'],['t.q.; tq','tel(s) que'],['top.; top','topologie'],['tot.; tot','totalement'],['tr.; tronç.; Tr','tronçon(s); Tr also names the set of pseudo-tronçons'],['interst.','interstitiel'],['ferm; fer','fermé(s); Mod fer is retained literally, not lengthened']
]
(ROOT/'records/abbreviations.json').write_text(json.dumps(abbreviations,ensure_ascii=False,indent=2)+'\n')
(ROOT/'records/legibility.md').write_text('''The main lines are generally readable, but the handwriting is highly compressed and its variable letters are repeatedly overwritten. The least secure passages are the two slanted notes on 026–027, the end of the components margin on 030, the dense cancelled distributivity draft on 033, small overwritten labels on 034–037, and the crowded formulas at the right edge of 038 and 041. The remaining doubts are genuine visual limits after enlargements, not invitations to supply a mathematically expected phrase. The two illegible words in the cancelled 033 draft are physically covered by crossing strokes; uncertainty in formulas is expressed with candidate symbols, never an illegible-symbol placeholder.

The consolidated text preserves unrevised letters, malformed grammar, unmatched punctuation and apparent slips. A compact upper-right frontier point, a centred dot, a hollow interior circle and a prime are distinguished where the marks allow it. Script-font choices are less secure than letter identity: the P glyph is therefore explicitly doubtful on both of its occurrences, while the swept M is represented consistently by calligraphic M. The final cross-page comparison is documented in the notation table and its crop.

C supplies a useful diplomatic scaffold and generally preserves more of the written state than H. Many changes against C resolve its own marked doubts; others restore an insertion, cancellation, abbreviated ending or index. H is often useful as an alternative reading, but on these pages it more frequently expands abbreviated prose, smooths the grammar, omits marginal fragments or supplies mathematically expected notation. Neither agreement nor the supplied historical error-rate estimates were treated as evidence. The counts above are apparatus-place counts, including doubt resolutions and graphical-state decisions; they are not independently measured error rates or counts of incorrect words.

All sixteen whole-page images and their supplied halves were personally read by the root reader in order, followed by targeted enlargements and a second visual reading of every page. This is one model reader making two visual passes, not a claim of human verification or two independent final readers. No OCR, text-recognition service, external source or context prose was used to establish the readings; no TeX compilation was performed. Research interpretation begins only after the recorded hash freeze.
''')
(ROOT/'records/witness_s_disposition.md').write_text('''## Witness S: scope and disposition

Only the supplied `readings/156-3_CORRECTIONS.tsv` was opened during transcription; the sweep prose stayed closed. S mixes image-reading proposals, mathematical repairs, later nomenclature and claims expressly not checked on an image. These are kept distinct.

| S row | Relevant place | Ink disposition in this pass |
|---|---|---|
| SA21-K3-01 | 018–021 and following; later correction on 156-7/071 | The later sheet is outside the supplied scans and is not image-verified here. The words modérées / fermées actually written on 030–041 are retained; no later renaming is retrofitted. |
| SA21-K3-02 | 014 | Outside scans 026–041; no image available in this task, so neither confirmed nor overturned as a reading. |
| SA21-K3-03 | 032 case table | The descending j supports majoré/mijoré, not minoré. S’s proposed repair is declined as a diplomatic reading; its mathematical issue is deferred. |
| SA21-K3-04 | 040 atom list | Literal t1 in ]t1,t3[ confirmed against the enlarged ink; proposed t2 is not inserted. |
| SA21-K3-05 | 035 unit | Literal X confirmed by two diagonals with no A crossbar; proposed A is not inserted. |
| SA21-K3-06 | 019, referring also to 030 | The 019 statement is outside the scan set. The quoted 030 caveat “mais pas pour la top canonique” is confirmed in the rotated margin; the broader mathematical refinement is not adjudicated during transcription. |
| SA21-K3-07 | 032 margin | The order-definability question, meet sign, existe and three question marks are confirmed. S’s proposed refutation is reserved for research notes. |
| SA21-K3-08 | 023 | Outside scans 026–041; no image verification here. The topological answer is context for later notes only. |
''')
when=utc()
(ROOT/'records/notation_audit.json').write_text(json.dumps({'reader':'/root; GPT-6 Astra Pro; effort not exposed','time_utc':when,'evidence':'evidence/notation_drap_crosspage.jpg','method':'Direct comparison of previously read ink; context still closed'},ensure_ascii=False,indent=2)+'\n')
with (ROOT/'progress.log').open('a') as f:f.write(f'notation harmonized {when}; context remains closed\n')
rebuild()
print('Final notation and abbreviation apparatus written at',when)
