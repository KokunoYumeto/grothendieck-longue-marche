#!/usr/bin/env python3
"""Assemble research notes only; never read images or write frozen deliverables."""
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[1]
REC = ROOT / 'records'

def sections(path):
    text = path.read_text()
    matches = list(re.finditer(r'^### ((?:W|LN|SM|M)\d{2}) — (.+)$', text, re.M))
    result = {}
    for i,m in enumerate(matches):
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        block = text[m.start():end]
        stop = re.search(r'^## ', block, re.M)
        if stop: block=block[:stop.start()]
        result[m.group(1)] = block.strip()
    return result

def root_note(n):
    head = f"### {n['id']} — {n.get('title',n['section'])}\n\n"
    head += f"**Witness:** {n['location']}. **Kind:** {n['kind']}. "
    if n.get('quote'):
        head += f"**Quotation:** “{n['quote']}”. "
    else:
        head += '**Quotation:** none; this is an editorial inventory calculation, not an authorial statement. '
    head += f"**Context search:** `{n['query']}`. **Context relation:** {n['context']} **RS:** {n['rs']}"
    if n.get('confidence'):
        head += f" **Confidence:** {n['confidence']}; {n['reason']}"
    return head+'\n\n'+n['body']

weights = sections(REC/'research_weights.md')
linear = sections(REC/'research_linear_nonlinear.md')
motives = sections(REC/'research_context_motives.md')
root_notes=json.loads((REC/'root_notes.json').read_text())
roots={n['id']:n for n in root_notes if n['id']!='H04'}

roots['T07']['quote']=''
roots['H01'].update({
 'title':'The negative twist on scan 113 and the separate duality-set discrepancy',
 'body':"The literal set discrepancy on scan 112 is analyzed in W15, which gives the mathematical reason for Hua's correction without changing the frozen reading. On scan 113 the frozen expression gives the weight 2n−ν−2k for the negative twist, whereas Hua's footnote reports a positive-twist reading of its page 112. That second discrepancy is a reading question in its own right and is not resolved by correcting the set on the preceding scan."
})

title_map={
'R01':'The three retained textual units and the limits of this selection',
'R02':'Virtual Betti numbers retain graded additive information',
'R03':'Generic-fibre definitions do not yet supply the desired pullback formalism',
'ODA1':'Oda gives finite-group-scheme content to the realization question',
'ODA2':'The general proper smooth case is an inclusion, not the abelian isomorphism',
'H02':'Proposition numbering and the disputed final phrase',
'H03':'Base-field and functor-symbol normalizations in Hua',
'T01':'The opening title and the handwritten page number 1',
'T02':'Internal headings without total extents',
'T03':'The reused Local Cohomology cover and its proof annotation',
'T04':'Selected handwritten faces and the unselected report faces',
'T05':'Motifs lisses versus Isomotifs lisses',
'T06':'The abstract-construction cover begins a longer unit',
'T07':'Actual retained scan and inventory counts'}
for k,v in title_map.items(): roots[k]['title']=v

roots['R04']={
 'id':'R04','title':'The global Legendre example answers both sharper bounds on scan 108',
 'section':'Weights','location':'12/108, both boxed upper-weight questions; compare 12/120',
 'kind':'own idea','quote':'peut-on remplacer 2n+2j par 2n+j ?; peut-on remplacer 2i+2j par 2i+j ?',
 'query':'poids|2n.*j|2i.*j|strictement.sp.cial|Deligne',
 'context':"Hua, modernised reading of cote 12, 'Poids de la cohomologie ℓ-adique d’une variété singulière ou non propre (pages 104 à 108)' and 'Le cas d’une immersion : les feuilles de calcul (pages 115, 117 et 119)': adds a global counterexample to the two proposed sharpenings, separately from W13's local counterexample; it also differs from the blanket direct-image bound in 'La filtration par le niveau (pages 34 et 35)'.",
 'rs':'WG2 §2.4 #3 and §3.2 #7 (unchecked plans); `12-immersion-level-bound` is a constant-coefficient candidate and is not refuted by this coefficient example.',
 'confidence':'high','reason':'geometric monodromy, curve duality, localization, and the Leray edge map explicitly determine a nonzero weight-4 quotient; independently checked in the research phase.',
 'body':r"Use the Legendre family \(y^2=x(x-1)(x-t)\) on \(U=\mathbf P^1_{\mathbf F_q}-\{0,1,\infty\}\), with odd \(q\), \(-1\) a square, \(a:U\hookrightarrow\mathbf P^1\), and \(F=R^1\pi_*\mathbf Q_l\), whose geometric monodromy is \(\mathrm{SL}_2\) (Katz, 2012, Chapter 15). All following cohomology is over \(\overline{\mathbf F}_q\) with its inherited Frobenius action: duality gives \(H_c^2(U,F)=0\), and \(0\to a_!F\to a_*F\to B\to0\), with \(B\) supported on the boundary, gives \(H^2(\mathbf P^1,a_*F)=0\). The Leray edge map therefore surjects from \(H^1(U,F)\) onto \(H^0(\mathbf P^1,R^1a_*F)\), whose two rational boundary stalks at 0 and 1 give the quotient \(\mathbf Q_l(-2)^2\) computed in W13. Its weight is 4, so both proposed global bounds \(2n+j\) and \(2i+j\) fail for \(i=n=j=1\), including the stated \(i\le n\) range."
}

# One assembly-only clarification of the direction in the lattice example.
linear['SM03']=linear['SM03'].replace(
 'take the rational Tate object with lattices `E_l=l⁻¹ Z_l` at every prime and compare it to the standard lattice system.',
 'take the rational Tate object with lattices `E_l=l⁻¹ Z_l` at every prime and take Hom from the standard lattice system into this modified system.')
linear['SM16']=linear['SM16'].replace(
 'A map from a closed point of S has no map from its residue field into the generic field K, so an object defined only over K plus unramified realizations does not automatically have a motivic fibre there.',
 'For a closed point s distinct from the generic point η, the morphism s→S does not factor through η, so an object defined only over K plus unramified realizations does not automatically have a motivic fibre at s.')
linear['LN05']=linear['LN05'].replace(
 'If a normalized procyclic subgroup has cyclotomic conjugation on a nonzero l-adic component and that component survives in a proper Jacobian\'s Tate module, the Frobenius eigenvalue mismatch in the table excludes it.',
 'If an arithmetic subgroup with open image in G_K normalizes a procyclic subgroup, acts on a nonzero l-adic component through the cyclotomic character of that projection, and this component survives equivariantly in a proper Jacobian\'s Tate module, the Frobenius mismatch in the table excludes it after the corresponding finite base extension.')
linear['SM13']=linear['SM13'].replace(
 'One cited example is `R=W(k)[[x,y]]/(p−(xy)^(p−1))`;',
 'One cited example is `R=W(k)[[x,y]]/(p−(xy)^(p−1))`, with k perfect of characteristic p;')
linear['LN06']=linear['LN06'].replace('has the toric boundary contribution of Tate type','has a possibly zero toric boundary contribution of Tate type')
linear['SM05']=linear['SM05'].replace('a counterexample inside the torsion part admitted in 12/141','a generic torsion counterexample to the claimed extension closure, using the torsion data admitted in 12/141')
linear['SM15']=linear['SM15'].replace(
 'Vasiu–Zink (2010, Corollary 4) prove extension over a regular local mixed-characteristic base when `p∉m^p`, equivalently when its absolute ramification index is at most `p−1`.',
 'Vasiu–Zink (2010, Corollary 4) prove that abelian schemes over the punctured spectrum of a regular local mixed-characteristic ring R of dimension at least two extend to Spec R when `p∉m^p`, equivalently when its absolute ramification index is at most `p−1`.')
motives['M02']=motives['M02'].replace(
 'The proof later requires biproducts, so its starting “additive” category must have finite biproducts, or must first receive its finite additive hull.',
 'The proof requires finite biproducts in its starting additive category; if they are first adjoined, semisimplicity must also hold for the endomorphism algebras of the newly formed objects.')
motives['M17']=motives['M17'].replace(
 'the printed names themselves are verified in Grothendieck (1969, §§2–4) and Kleiman (1968, introduction and §3).',
 'the printed names themselves are independently verified in Kleiman (1968, introduction and §2), with Grothendieck (1969b) retained as the historical companion reference.')
motives['M19']=motives['M19'].replace('finite motivic representations are Artin','motives with finite monodromy are Artin')
motives['M20']=motives['M20'].replace(
 'For a rational Tannakian motivic theory with effective Galois descent and compatible fibre functors, Kahn (2025, Theorem 5.10) yields 1→G_mot(Q̄)→G_mot(Q)→Γ_Q→1. His framework includes rational Nori motives, with the relevant descent established in §10. The identification of the geometric kernel with the identity component, or a splitting over Q, is an additional assertion and is not supplied by this exactness theorem or these frozen pages.',
 'For rational Nori motives, fix a complex embedding and compatible Q-valued Betti fibre functors, and identify the category over Q̄ with the filtered 2-colimit over finite extensions as in Kahn (2025, §5.8). Theorem 5.10 then yields 1→G_mot(Q̄)→G_mot(Q)→Γ_Q→1, with Nori descent supplied by Theorem 10.2 and the application identified in Remark 10.3. More generally, this formulation requires the corresponding neutral fibre-functor and effective-descent hypotheses, rather than the existence of a tensor category alone. Identifying the geometric kernel with the identity component, or splitting the sequence over Q, remains a separate assertion not supplied by this exactness theorem or these frozen pages.')

intro=(REC/'notes_introduction.md').read_text().rstrip()
parts=[intro,'## 3. Linear statement / non-linear statement\n\nThe four pairs are a planning comparison, not four equivalences written in these scans.']
lin_text=(REC/'research_linear_nonlinear.md').read_text()
start=lin_text.index('| Pair and manuscript anchor')
end=lin_text.index('### LN01')
parts.append(lin_text[start:end].strip()
 .replace('At a good finite place,','At a good finite place of residue characteristic different from l,')
 .replace('semisimplicity of a neutral Tannakian category corresponds to pro-reductivity of its group','semisimplicity of a neutral Tannakian category corresponds to pro-reductivity of the identity component of its group'))
parts.append('## 4. Scope and contextual connections')
for id in ['R01','R02','R03']: parts.append(root_note(roots[id]))
parts.append('## 5. Weights, levels, admissibility, and direct images')
for id in sorted(weights):
    parts.append(weights[id].replace('Grothendieck (1969,','Grothendieck (1969a,'))
    if id=='W14': parts.append(root_note(roots['R04']))
parts.append('## 6. Limits of the linear / non-linear analogies')
for id in sorted(k for k in linear if k.startswith('LN')):parts.append(linear[id])
parts.append('## 7. Smooth integral motives and extension over the base')
for id in sorted(k for k in linear if k.startswith('SM')):parts.append(linear[id])
parts.append('## 8. Abstract motives, Lefschetz structures, Galois descent, and periods')
for id in sorted(motives):parts.append(motives[id].replace('Grothendieck (1969,','Grothendieck (1969b,'))
parts.append('## 9. The supplied Oda paper and integral realization data')
for id in ['ODA1','ODA2']:parts.append(root_note(roots[id]))
parts.append('## 10. Additional reading questions raised after the freeze\n\nThe related formula and wording questions already appear in W11, W15, W19, W21, W28–W31, SM09, SM17, and M07–M08; none has been incorporated into the transcription.')
for id in ['H01','H02','H03']:parts.append(root_note(roots[id]))
parts.append('## 11. Steps the manuscript itself marks as unverified\n\nThis is a compact index of the authorial reservations and admitted inputs analyzed in the numbered notes, not a second set of research claims. Quotation marks, doubt macros, and interrogative wording below reproduce the frozen reading; an editorial `\\unsure` by itself is not an authorial doubt. Full tables of abbreviated proof transitions and visible revisions are retained in `records/manuscript_explicit_unverified_steps.md`.')
reg=(REC/'manuscript_explicit_unverified_steps.md').read_text()
for heading,prefix in [('Explicit questions and reservations','SF'),('Admitted or invoked dependencies','AI')]:
    table_header='### '+heading+'\n\n| Cote/scan | His words | Notes |\n|---|---|---|'
    rows=[]
    for line in reg.splitlines():
        if not re.match(r'\| '+prefix+r'\d+',line):continue
        cols=re.split(r'(?<!\\)\|',line)[1:-1]
        if len(cols)!=4:raise ValueError(('table split',line,cols))
        location=cols[1].strip()
        quotation=cols[2].strip()
        refs=', '.join(dict.fromkeys(re.findall(r'\b(?:W|M|SM|LN)\d{2}(?:[–-](?:(?:W|M|SM|LN))?\d{2})?',cols[3])))
        rows.append('| '+location+' | '+quotation+' | '+refs+' |')
    parts.append(table_header+'\n'+'\n'.join(rows))
parts.append("The conspicuous cross-scan restriction is 12/113→114: the theorem is narrowed to strictly special coefficients, and the broader statement returns under a semisimplicity hypothesis (W17–W20). The essential-image qualification is within 12/142 itself (SM11); the universal-property wording is refined across 12/144–146 and qualified on 148 (M01, M10), but “ou le cas échéant” on 144–145 alone is an alternative formulation rather than proof of a retraction. The source's final words on 137 remain a reading disagreement with Hua (W31/H02), not secure evidence that this exact last step is explicitly left untreated.")
parts.append('## 12. Title sheets and page-count evidence')
for id in [f'T{i:02}' for i in range(1,8)]:parts.append(root_note(roots[id]))
parts.append('## 13. References\n\nPrimary literature is cited in APA author–date form with exact theorem or section locators in the notes. Dates below are publication dates, except the explicitly identified Stix preprint and Riou lecture notes; corrected author versions are identified. Supplied contextual files are documented in §1 rather than represented as independently published scholarship.')

# Keep bibliographies in their checked forms, then normalize duplicated year labels.
mt=(REC/'research_context_motives.md').read_text()
mb=mt.split('## Primary bibliography and exact checked passages')[1].split('## Web reference IDs')[0]
mb='\n\n'.join(p.strip()[2:] for p in mb.split('\n\n') if p.strip().startswith('- '))
mb=mb.replace('Grothendieck, A. (1969).','Grothendieck, A. (1969b).')
lb=lin_text.split('## 3. Primary bibliography, in APA form')[1].split('## 4. Retrieval')[0].strip()
wt=(REC/'research_weights.md').read_text()
wb=wt.split('## Primary references actually inspected')[1].split('## Primary lead not fully inspected')[0].strip()
wb=re.sub(r'^\d+\. ', '', wb, flags=re.M)
wb=re.sub(r' Web refs?:.*?(?=\n|$)', '', wb)
wb=wb.replace('Grothendieck, A. (1969).','Grothendieck, A. (1969a).')
extra=(REC/'bibliography_extra.md').read_text().strip()
entries=[]
for b in [mb,lb,wb,extra]:
    for line in b.splitlines():
        if not line.strip():continue
        entry=re.sub(r'^(?:- |\d+\. )','',line.strip())
        entry=entry.split(' — ')[0]
        entry=entry.split(' . Checked')[0]
        entry=entry.split(' ; inspected')[0]
        entry=entry.split(' . Publisher metadata')[0]
        entry=entry.replace(' . Only the finite-étale-cover extension assertion in clause (1) is used.','')
        entries.append(entry.rstrip(' .')+'.')
entries.sort(key=lambda x:x.casefold())
parts.append('\n\n'.join(entries))
parts.append('### Bibliographic lead with an access limit\n\n'+wt.split('## Primary lead not fully inspected')[1].split('## Algebraic checks')[0].strip().split('Publisher attempt:')[0].strip())
parts.append('## 14. Research and technical verification limits\n\nAll main note IDs have individual context-search records and explicit source relationships. The mathematics of the counterexamples was checked independently during research, but this is not an external peer review and does not change any RS status; the Durfee (1983) full-text limitation and the missing cote 14/18 witnesses remain explicit. The TeX files were checked structurally, including their frozen hashes and exact concatenation, but no successful PDF compilation is claimed because the installed TeX environment lacks the required class and packages; the separate visual audits were performed directly against the supplied images before context was opened.')

out='\n\n'.join(parts).rstrip()+'\n'
out=out.replace('Choudhury & Gallauer,','Choudhury & Gallauer Alves de Souza,')
out=out.replace('Choudhury and Gallauer (2017,','Choudhury and Gallauer Alves de Souza (2017,')
dest=ROOT/'MPL_12_099-149_notes.md'
dest.write_text(out)
ids=re.findall(r'^### ((?:W|M|LN|SM|R|ODA|H|T)\d{1,2}) —',out,re.M)
if len(ids)!=len(set(ids)):raise ValueError('duplicate note IDs')
manifest={'note_ids':ids,'note_count':len(ids),'word_count':len(out.split()),'assembled_from':['records/root_notes.json','records/notes_introduction.md','records/research_weights.md','records/research_linear_nonlinear.md','records/research_context_motives.md','records/manuscript_explicit_unverified_steps.md','records/bibliography_extra.md'],'protected_files_written':False}
(REC/'notes_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(REC/'root_notes_assembled.json').write_text(json.dumps(list(roots.values()),ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(dest),'note_count':len(ids),'words':len(out.split())}))
