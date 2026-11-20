"""Root decisions after complete returns and 27 actual local image views."""
from pathlib import Path
import copy,json,datetime
w=Path(__file__).resolve().parents[1]
rs=[json.loads((w/f'readers/scan033/R{k}/return.json').read_text()) for k in (1,2,3)]
# R2 supplies the separated locus scheme. Exact reader mapping was reviewed manually.
mp1=list(range(1,27))+[27,28,17,29,21,30,31,32]
mp3=list(range(1,27))+[27,29,30,31,32,33,34,35]
assert len(mp1)==len(mp3)==34
obs={
1:'Extra crossed diagonals survive within the live Sigma, but their whole earlier contour remains merged. Retain older X|Sigma with R1/R3; record R2’s resolved X.',
2:'Only one detached horizontal is present, without an independent cancellation or a second equality bar. Read the dash with uncertainty over its live/deleted state.',
3:'A small enclosed area and extra low bars merge with the live non-equality. Keep both older identity and layer/state uncertain, as R2 does.',
4:'The tall looped S and dotted i share a low connected return, without an independently extending strike. Resolve live Si with R2/R3; R1’s cancellation alternative is recorded.',
5:'The detached short tick below (5) has a thick top and low tail. Comma/apostrophe identity remains open.',
6:'The first raised sign is a thick closed ring with a pale center. Retain circle/o/zero and use circle for matching recurrences. Main eq8_rings.png separately shows the four recurring round superscripts and the three full overbars in (8); the (7) rings are visible in R2 crop 05.',
7:'The worked left cup and rounded low right cup with upward finish match the clearer omega in (7). Resolve omega with R1/R2; R3’s w alternative remains in the reader comparison.',
8:'Two rightward arms meet a bent descending stroke at their left, continuing below the lower arm. Put membership first with R1/R3; retain non-equality and equality rather than replace the strokes from the adjacent parenthesis.',
9:'The small older form has an angled high turn and a low foot, favouring 2. Its identity and overwritten state remain inseparable from the dense retouching; retain both uncertainties.',
10:'A low dark upright, little foot and crossing/return survive beside epsilon. The crossing cannot be independently separated from the letter return. Retain identity and state uncertainty with R3.',
11:'The separate low mark is a compact round dot with no descending comma tail. Resolve the point.',
12:'The high prime after the second epsilon is separate and clear. The lower dense curl/bar remains 2/minus uncertain, with its cancellation boundary also uncertain. H’s note locates prime corrections in the parenthesis; its left formula remains unprimed.',
13:'A separate high short stroke stands above/right of the first parenthetical epsilon, matching the independently visible second prime. Resolve the prime. H’s note explicitly records both corrected primes; the low suffixes are separate state findings.',
14:'The first parenthetical epsilon’s lower return adjoins a short thick upright/bar. Retain old 1/plus with uncertainty over state; H retains its numbered suffix in the corrected reading.',
15:'The second parenthetical epsilon’s lower end adjoins a short bar/downward spur. Retain old 2/minus with uncertainty over state; H retains its numbered suffix in the corrected reading.',
16:'The terminal mark has an upper loop, middle arm/stem and low tail. Put epsilon-plus-comma first with R2/R3, retaining semicolon, epsilon and comma. The distinct high dot and raised comma on the preceding Sigma are clear.',
17:'The open c, small rounded a and final low s remain visible beneath the cancellation. Resolve cas.',
18:'The initial o and n are low, unlike the tall On directly above. Resolve lowercase on.',
19:'The c-o-n run ends with the d ascender, loop and rightward exit. No separate i stem/dot or final abbreviation point follows. Resolve cond without completing the abandoned word.',
20:'A lighter curled older form survives beneath/left of the live 1, with its contour merged into the dark replacement. Retain older epsilon|2.',
21:'One tall l-like rise and a smaller adjoining rise occur amid compressed medial waves. Retain parallèles|paralèles; H’s same first spelling alone adds no collation difference.',
22:'The main prose crop shows one isolated round dot after un, with no comma tail. Resolve the point and retain its written placement.',
23:'A separate short upright occurs between the second 1 and the b ascender. Lead with 11’bis, keeping the two alternatives for attachment/spacing. The short mark is lower than a clear high prime.',
24:'The second prose Sigma’s low cap is broader than the nearby upright 1 and bends down at the right. Keep 2 first with 1 retained; H’s primary 2 agrees.',
25:'The d, compressed e, tall f, two i dots and terminal s are visible. There is no intervening e before s and no detached acute over the first e. Resolve definis with R1, recording R2’s accent and R3’s accent uncertainty.',
26:'The last low index has a short cap and down-right hook with a compressed foot, resembling the adjacent fuller 2. Retain 2|1 with R2, recording R1’s 1-first and R3’s resolved 2. The pair’s expected pattern does not settle it.',
27:'The small d/e/f label has no detached acute over e. Preserve def.',
28:'The crossed word exposes its tall t, connected r/o, i dot and final s. Read cancelled trois rather than H’s illegibility mark.',
29:'The cancelled opening separates tall On, a small detached a, and le. Preserve On a le against H’s dans le.',
30:'The cap and two descending legs recur in both (9) families, both prose names and the final pair definitions. The final first-family glyph has curved feet. Keep pi/Pi uncertainty first, using pi consistently afterwards. Additional main crops: eq9_second_pi, prose_dot_and_pi and final_first_pi; R1 crop 15 shows the final second family.',
31:'The single underline lies beneath parallèles, beginning after its p descender; non is left of the rule. H’s emphasis includes non. This is a scope difference, independently of the spelling doubt.',
32:'After équivaut are an upper slanted tick and a lower filled point, with no independently separated a body or additional punctuation group. Put colon first, retaining compressed à with R3. H’s additional à-plus-colon is not supported as two groups.',
33:'The corresponding two separated marks after encore again favour colon. The shared colon/à uncertainty is marked at the first occurrence and documented for both here; use the same first rendering.',
34:'The final label has initial 1 and a roof/long descent for the next digit, without a clear lower horizontal foot. Retain 17|12, all three readers’ order, acknowledging H’s explicit 12/17 doubt note.'
}
d={'scan':33,'folder':'J81-04','their_page':32,'hua_has':'text','filename':'J81-04_81_scan033.tex','status':'decided','findings':[]}
for i,base in enumerate(rs[1]['findings'],1):
 f=copy.deepcopy(base)
 src=[rs[0]['findings'][mp1[i-1]-1],base,rs[2]['findings'][mp3[i-1]-1]]
 f['id']=f'SP41-033-{i:03d}'
 f['readers']={f'R{k}':s['reading'] for k,s in enumerate(src,1)}
 f['reader_source_ids']={f'R{k}':s['id'] for k,s in enumerate(src,1)}
 f['marked_in_H']='yes' if i in [10,12,13,14,15,28,34] else 'no'
 f['crop']=str(Path(f['crop']).relative_to(w)) if f.get('crop') else ''
 f['evidence']='Main reader, cited local crop(s): '+obs[i]
 f['main_adjudication']='All three complete texts, findings and inventories compared; root personally viewed the cited local evidence. See decisions/scan033_main_observations.md.'
 if i==1:f.update(reading=r'\deleted{\unsure{X|\Sigma}}',against_C=False,c_doubt_status='retained',confidence='low')
 if i==7:f.update(confidence='medium',crop='readers/scan033/R1/04_eq6_parenthesis.png')
 if i==8:f.update(reading=r'\unsure{\in|\ne|=}',against_C=True)
 if i in [10,14]:f.update(reading=r'\unsure{\deleted{1|+}}',against_C=True)
 if i==12:f.update(reading=r"\varepsilon'_{\unsure{\deleted{2|-}}}",against_C=True)
 if i==15:f.update(reading=r'\unsure{\deleted{2|-}}',against_C=True)
 if i==13:f['h']=r"Displayed \varepsilon_1; note explicitly gives corrected \varepsilon'_1 and calls the indices uncertain."
 if i==23:f.update(reading=r"\unsure{11'bis|11bis|11 bis}",against_C=True)
 if i in [21,24,26]:f['against_H']=False
 if i==25:f.update(reading='definis',against_H=True,crop='readers/scan033/R1/13_definis.png',kind='abbreviation expanded or spelling modernised')
 if i==26:f['crop']='readers/scan033/R1/15_last_formula.png'
 if i==22:f['crop']='crops/scan033/main_prose_dot_and_pi.png'
 if i==28:f['crop']='crops/scan033/main_trois.png'
 if i==31:f['crop']='readers/scan033/R1/10_paralleles.png'
 if i==32:f.update(reading=r'condition qui équivaut \unsure{:|à}',confidence='medium',kind='other')
 if i==33:f.update(reading='ou encore :',confidence='medium',crop='readers/scan033/R3/13_encore_ending.png')
 if i in [12,13]:f['consequential']='The separate high prime is preserved; the two entries in (7)’s parenthesis are both visibly primed, while the first live epsilon in the union expression is unprimed. No consistency repair is inserted.'
 if i==8:f['consequential']='The joined relation in (6) is retained as membership/non-equality/equality uncertain, with membership first; H’s clean equality does not settle the ink.'
 d['findings'].append(f)

t=(w/'readers/scan033/R1/reading.tex').read_text()
for old,new in [
 (r'\text{\unsure{Si|\deleted{Si}} les }',r'\text{Si les }'),
 (r'\deleted{\unsure{=|\varnothing}}',r'\unsure{\deleted{=|\varnothing}}'),
 (r'\deleted{\unsure{2|\varepsilon}}',r'\unsure{\deleted{2|\varepsilon}}'),
 (r'\deleted{\unsure{1|+}}',r'\unsure{\deleted{1|+}}'),
 (r'\deleted{\unsure{2|-}}',r'\unsure{\deleted{2|-}}'),
 (r'\unsure{;|\varepsilon,|\varepsilon|,}',r'\unsure{\varepsilon,|;|\varepsilon|,}'),
 ('condition qui équivaut :',r'condition qui équivaut \unsure{:|à}'),
 (r'\Sigma_{\unsure{1|2}}^-',r'\Sigma_{\unsure{2|1}}^-')]:
 assert old in t,old
 t=t.replace(old,new)
(w/'pages'/d['filename']).write_text(t)
d['inventory']=copy.deepcopy(rs[1]['inventory'])
for x in d['inventory']:
 s=x['first_words_or_objects']
 s=s.replace(r'\deleted{X}',r'\deleted{\unsure{X|\Sigma}}')
 s=s.replace(r'\deleted{\unsure{1|+}}',r'\unsure{\deleted{1|+}}').replace(r'\deleted{\unsure{2|-}}',r'\unsure{\deleted{2|-}}')
 s=s.replace('sont définis','sont definis').replace('condition qui équivaut :','condition qui équivaut colon/à').replace('(11bis)','(11’bis|11bis|11 bis)')
 x['first_words_or_objects']=s
d['unresolved']=[]
for f in d['findings']:
 if f['c_doubt_status']=='retained' or f['id'].endswith(('-030','-032','-034')):
  d['unresolved'].append({'place':f['place'],'reading':f['reading'],'alternatives':'Alternatives and written-state uncertainty are explicit in the retained reading; all three readings appear in the changes table.','confidence':f['confidence'],'reason':f['evidence'],'finding_id':f['id']})
d['notation']=copy.deepcopy(rs[1]['notation'])
for a in d['notation']:
 if a['form']==r'\deleted{X}\Sigma^\varepsilon':a.update(form=r'\deleted{\unsure{X|\Sigma}}\Sigma^\varepsilon',reading=r'\deleted{\unsure{X|\Sigma}}\Sigma^\varepsilon',evidence='Extra older diagonals merge with the live Sigma; older X/Sigma identity remains open.')
 if 'after omega' in a['form']:a.update(form=r'\in|\ne|= after omega in (6)',reading=r'\unsure{\in|\ne|=}')
 if a['form'].startswith('colon after'):a.update(reading=r'\unsure{:|à} after équivaut; recurring first reading : after encore',evidence='R2 crop 11 and R3 crop 13: two vertically paired short marks; no separate a body, but its very compressed form remains possible.')
d['notation'].extend([
 {'scan':33,'form':'Four old low suffixes in (7)','evidence':'R2 crops 05/06: dense uprights, low curls and bars remain inseparable from epsilon returns.','reading':r'\unsure{\deleted{1|+}} and \unsure{\deleted{2|-}}, with uncertainty over identity and state.'},
 {'scan':33,'form':'Final short Sigma indices','evidence':'R1 crops 12/15: broad cap/right hook with compressed lower return, unlike the nearby straight 1.','reading':r'\unsure{2|1} in both final prose and final formula.'},
 {'scan':33,'form':'definis','evidence':'R1 crop 13: two i dots and terminal s; no separate medial e before s or acute above the first e.','reading':'definis'}])
d['abbreviations']=copy.deepcopy(rs[1]['abbreviations'])
texts=[
 'A wholly handwritten working sheet opens “Notons les implications” and contains the heading “1.2. Deux décompositions binaires”. A pencil 32 is retained as archive numbering. No date, author page number, diagram, drawing or explicit authorial verification/question annotation was identified by the three readers.',
 'Display (5) has an upper rightward double arrow and a lower two-headed double arrow. Live Si is resolved from its connected baseline stroke, with R1’s possible cancellation recorded. Older capital/comparison marks and the isolated dash remain represented. The terminal lower point is already present in both C and H; R3’s proposed C-omission finding was rejected after exact text comparison.',
 'Display (6) writes a chain of differences and intersections beginning with the round-sign epsilon Sigma. The round sign remains circle/o/zero uncertain. Omega is resolved by its rounded cups and the directly compared cleaner occurrence in (7). The following joined relation retains membership first, then non-equality/equality alternatives; the cleaner adjacent equality does not replace it.',
 'Display (7) places E between two Sigma terms with union signs, followed by “de X en” and cancelled “trois”, then “ens. mutuellement disjoints.” Both parenthetical epsilons have separate high primes, while the first live epsilon in the union is unprimed. This written discrepancy prompted close comparison and remains. Five older exponent/suffix loci retain identity/state uncertainty. H’s explicit note about uncertain indices and corrected parenthetical primes is included in the apparatus.',
 'Display (8) has three bars extending across Sigma and its raised circle/epsilon group. The last Sigma has a separate high dot and a raised comma between circle and epsilon. Its isolated low terminal mark remains epsilon-plus-comma/semicolon/epsilon/comma uncertain. No mathematical meaning supplies its identity.',
 'Two separately cancelled openings read “On a le cas” and “on s’intéresse à la cond”. The last d and exit are visible, with no separate i or abbreviation point. The abandoned word is not completed. The earlier cancelled trois is readable rather than illegible.',
 'Section 1.2 writes two indexed families. Their recurring cap-and-two-leg glyph is marked pi/Pi uncertain at its first occurrence, with pi used subsequently. Only parallèles/paralèles is underlined; non lies outside the rule. The complete interlinear phrase “si elles sont distinctes, et” attaches before “s’il existe”, as its bent leader shows. H explicitly recognizes that insertion. A detached dot after un is preserved.',
 'The lower formulas write (10) Sigma_1^+ intersection Sigma_2^+ equals empty set, followed by (11) Sigma_1^+ subset Sigma_2^- and the bis line Sigma_2^+ subset Sigma_1^-. Their connecting prose reads “condition qui équivaut” followed by a colon/à-uncertain group and “ou encore” with the same first rendering. S SA01-K81-01’s formulas are confirmed from the main local crop; its quoted prepositions are qualified by this punctuation reading. The manuscript’s asserted equivalence is retained in the transcription.',
 'The final prose reads definis without a visible acute. The two small final Sigma indices retain 2|1, and the final tag retains 17|12, with 17 first from its roof and long descent. The extra short stroke before bis remains in 11’bis|11bis|11 bis. Expected matching indices and sequential numbering did not supply missing strokes.',
 'All 26 C doubts have decisions: nine resolved and seventeen retained. Twenty uncertainty loci remain overall, including the first family-case mark, the shared colon/à group and the final tag. All three full returns were compared. No OCR, external research or compilation was performed. Source reading and local glyph comparisons are distinguished from the concrete mathematical computation below.'
]
d['notes']=[{'id':f'scan033-note-{i:02d}','text':s} for i,s in enumerate(texts,1)]
d['notes'].append({'id':'scan033-counterexample-01','text':'Concrete supplied interval example (S SA01-R81-07), checked in this run: X=[0,3], Sigma_1^+=[1,2], Sigma_1^-=[0,1] union [2,3], Sigma_2^+=[2,3], Sigma_2^-=[0,2]. All four are nonempty closed subsets of X. Each pair covers X, each has distinct members, and the two unordered pairs are distinct. Direct interval intersections give Sigma_1^+ subset Sigma_2^- and Sigma_2^+ subset Sigma_1^-, while Sigma_1^+ intersection Sigma_2^+={2}. Thus this concrete pair satisfies both written inclusions and fails (10). Its four cross-intersections are {2}, [1,2], [2,3] and [0,1] union {2}, respectively. This refutes the equivalence claimed at the lower connecting prose. The manuscript text remains unchanged by the calculation.'})
d['notes'].append({'id':'scan033-certificate-01','text':'The computation uses seven nonempty disjoint cells {0}, (0,1), {1}, (1,2), {2}, (2,3), {3}, whose union is X. Each of the four specified interval sets is a union of whole cells. The map sending a cell union to its cell-index set has inverse sending an index set to the union of its indexed cells. Nonemptiness and disjointness give both inverse identities; membership in a cell gives exact preservation of union, intersection, difference and inclusion. The saved operations therefore certify these concrete interval sets exactly. Execution time: 2026-11-20 10:24:25 UTC. Files: scripts/scan033_interval_check.py and validation/scan033_interval_certificate.json.'})
who='GPT-6 Astra Pro; inherited effort not exposed; main reader scan033'
d['check_events']=[{'statement_id':a['id'],'date':'2026-11-20','who':who,'type':'carried as background without fault found','outcome':'Account of manuscript wording, witness comparison and local ink decisions only; no proof check is claimed for this source-account note.'} for a in d['notes'][:10]]
d['check_events'] += [
 {'statement_id':'scan033-counterexample-01 / scan033-certificate-01','date':'2026-11-20','who':who,'type':'computation or formal certificate','outcome':'Exact seven-cell computation executed at 10:24:25 UTC. Both inclusions true; positive intersection exactly {2}; pair coverage/distinctness checks true. Inverse cell-union/index-set maps and preservation of operations are documented in the script and certificate.'},
 {'statement_id':'scan033 manuscript lower prose after (10), asserted equivalence with (11) and bis','date':'2026-11-20','who':who,'type':"refuted, with the refined statement's id",'outcome':'Concrete refutation: scan033-counterexample-01, verified by scan033-certificate-01. The two written inclusions hold for the stated closed binary pairs, while their positive intersection is {2}. No replacement theorem is asserted and no transcription is corrected from this computation.'}]
d['sweep']=[{'id':'SA01-K81-01','s':'Quotes (10), condition qui équivaut à (11), ou encore à (11bis); cites interval example SA01-R81-07 against the asserted equivalence.','decision':'The three formula bodies and the words condition qui équivaut / ou encore are confirmed. Each following two-stroke group favours colon, with à retained as a shared alternative; the transcription records that ink uncertainty. The supplied concrete interval counterexample was verified exactly and entered in separate notes/check events.','evidence':'crops/scan033/main_equivalence_10_11bis.png; readers/scan033/R2/11_equivaut_terminal.png; readers/scan033/R3/13_encore_ending.png; validation/scan033_interval_certificate.json. The sweep’s assertions about subsequent use are not treated as proved here.'}]
d['rejected_candidates']=[{'reader_id':'scan033-R3-F028','reason':'C and H both already contain the final period in (5); root viewed the point in main_eq5_period.png and checked the exact C string. All three readings also contain it. No changed locus exists.'}]
d['main_crop_views']={'R2':list(range(1,14)),'R1':[4,10,12,13,15],'R3':[11,13],'main_new':7,'total':27}
d['crop_counts']={'R1':15,'R2':13,'R3':17,'main':7,'total':52}
d['decided_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(w/'decisions/scan033.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print(json.dumps({'scan':33,'findings':len(d['findings']),'C_changes':sum(f['against_C'] for f in d['findings']),'H_changes':sum(f['against_H'] for f in d['findings']),'uncertainties':t.count('\\unsure{'),'unresolved':len(d['unresolved'])}))
