from pathlib import Path
import json
R=Path('out'); s=(R/'readers/006/C/reading.tex').read_text()
s=s.replace("(xy)^{\\unsure{2|''}}=x''y", "(xy)^{\\unsure{2|''}}=\\unsure{x''|x^2}y")
s=s.replace(r'{Q^{\unsure{3|4}}}',r'{Q^3}')
start=s.index('% The following fraction rule')
end=s.index('% Opposite-direction writing',start)
s=s[:start]+r'''% The second fraction rule follows the separate lower tracing beneath the right-middle part.
\figure{\begin{tikzpicture}
\node[inner sep=0pt,anchor=south west] (num) at (0,0)
 {$P''Q^2-Q''PQ-\unsure{2}P'QQ'+2PQ'^{\,2}$};
\path (num.south west)--(num.south east) coordinate[pos=0.48] (partialstart);
\path (num.south west)--(num.south east) coordinate[pos=0.84] (partialend);
\draw ([yshift=-2pt]num.south west)--([yshift=-2pt]num.south east);
\draw ([yshift=-5pt]partialstart)--([yshift=-2.5pt]partialend);
\node[inner sep=0pt,anchor=north,yshift=-7pt] at (num.south) {$Q^3$};
\end{tikzpicture}}
% The small quotient's fraction rule turns back at its right end; no arrow meaning is assigned.
\figure{\begin{tikzpicture}
\node[inner sep=0pt,anchor=base west] (prefix) at (0,0) {$2p^2Q^2\bigl(-$};
\node[inner sep=0pt,anchor=south] at ([xshift=0.36cm,yshift=0.08cm]prefix.east) {$Q'$};
\node[inner sep=0pt,anchor=north] at ([xshift=0.36cm,yshift=-0.10cm]prefix.east) {$Q$};
\draw ([xshift=0.04cm]prefix.east)--([xshift=0.70cm,yshift=0.02cm]prefix.east)
 .. controls ([xshift=0.80cm,yshift=0.01cm]prefix.east) and ([xshift=0.66cm,yshift=-0.07cm]prefix.east)
 .. ([xshift=0.57cm,yshift=-0.10cm]prefix.east);
\node[inner sep=0pt,anchor=west] at ([xshift=0.97cm]prefix.east) {$+$};
\end{tikzpicture}}

'''+s[end:]
(R/'pages/J81-01_81_scan006.tex').write_text(s)
p=R/'crops/006/manifest.json'; a=json.loads(p.read_text());
for t in a:t['viewed']=True
for name,bbox,purpose,width in [
 ('03_inversible',[220,1505,675,1625],'complete word and endpoint beyond determinant crop right edge',2800),
 ('04_eta_endpoint',[170,1250,430,1380],'space after final index in first eta row, clipped in reader crop',2600),
 ('05_prose_predecessor',[220,540,455,730],'complete predecessor ascender and overlapped second-product punctuation',2600)]:
 a.append(dict(path='crops/006/'+name+'.png',bbox=bbox,rotation=180,purpose=purpose,width=width,viewed=True))
p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
viewed=['crops/006/'+x+'.png' for x in ['01_opening_quotient','02_final_system','03_inversible','04_eta_endpoint','05_prose_predecessor']]
viewed+=['readers/006/B/crops/'+x+'.png' for x in ['01_second_derivative','02_log_derivative','04_general_quotient','05_expanded_quotient','06_simplified_quotient']]
viewed+=['readers/006/C/crops/'+x+'.png' for x in ['u04_product','u06_numerator_sign','u06_first_factor','u06_denominator','u08_fragment','r01_determinant','r02_first_row','r03_eta_row','r04_second_pair','r05_third_row','r06_ceta_row','r07_prose_one','r08_prose_two','r09_prose_three','r10_prose_four']]
(R/'checks/scan006_main_decisions.md').write_text('''# Scan 006 — main crop adjudication

Root read all three returned transcriptions and their difference records against C and H. Root did not view a whole-page image or supplied half. All local decisions are preserved in records/scan006.json after approval; the mechanical merge and full source-row mapping are in checks/scan006_record_draft.json and checks/scan006_mapping.md.

The initial combined B04/B05 image call failed with a truncated-output message and displayed no images. Each was then successfully displayed individually. Only successful displays are listed below. Root viewed 20 existing reader crops and made and viewed five new crops. The inversible word endpoint, eta-row punctuation space and prose predecessor ascender required complete target bounds; no settled ink was re-adjudicated in those extra crops.

## Successfully viewed evidence

'''+''.join('- '+x+'\n' for x in viewed)+'''
## Decisions requiring particular qualification

- Product exponents and primes, two overwritten signs, the coefficient before P-prime and several cancelled predecessors remain explicitly doubtful.
- The large Q before the first raised 2 remains readable to the left of the diagonal. The exponent carries uncertain cancellation state, with both states retained and no chronology inferred.
- The expanded-fraction denominator reads 3 from its two curved lobes and lower return.
- Two fraction rules are represented in TikZ: the partial second stroke beneath the larger quotient and the hooked return on the lowest small quotient. No algebraic or arrow role is supplied for the latter.
- The prose's second-product predecessor reads f after its full upper loop was included. Its following comma remains qualified under opposite-orientation writing.
- The detached point below-left of On is retained without an assigned hand, layer, role or cancellation state.
- H's whole omitted expanded display and lowest fragment are each counted once. Their local uncertainty decisions remain independently documented without duplicating H omission counts.
- Root's four algebra computations are recorded separately and do not settle handwritten signs, exponents or cancellation states.
''')
p=Path('out/scripts/validate.py').resolve(); ns={'__file__':str(p)}
exec(p.read_text().split('records=')[0],ns)
result=ns['check_tex']((R/'pages/J81-01_81_scan006.tex').resolve())
(R/'checks/scan006_syntax.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page_written':True,'viewed_crops':len(viewed),'syntax':result},ensure_ascii=False))
