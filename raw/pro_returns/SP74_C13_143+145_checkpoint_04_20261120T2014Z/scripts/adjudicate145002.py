from pathlib import Path
import json
R=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
p=R/'reviews/145_scan002_readerB.json';t=R/'reviews/145_scan002_readerB.tex';d=json.loads(p.read_text());s=t.read_text();assert 'main_adjudication' not in d
# Reproduce the two shallow flat brackets instead of curly underbraces.
def bracket(obj,label):
 return r'\underset{'+label+r'}{\begin{gathered}'+obj+r'\\[-.8ex]\begin{tikzpicture}[x=1cm,y=1cm,baseline=0pt]\draw (0,.09) .. controls (-.04,-.01) and (-.01,-.05) .. (.10,-.05)--(1.25,-.05) .. controls (1.38,-.05) and (1.38,.03) .. (1.30,.09);\end{tikzpicture}\end{gathered}}'
old1=r"\underbrace{\pi'\subset\pi}_{\substack{\text{\unsure{ss=gr.|ss-gr.}}\\\text{d'indice fini}}}"
old2=r"\underbrace{\pi''\subset\pi}_{\text{id.}}"
new1=bracket(r"\pi'\subset\pi",r"\substack{\text{\unsure{ss=gr.|ss-gr.}}\\\text{d'indice fini}}")
new2=bracket(r"\pi''\subset\pi",r'\text{id.}')
assert old1 in s and old2 in s;s=s.replace(old1,new1).replace(old2,new2)
for n,(c,h,f) in enumerate([(r"\underbrace{\pi'\subset\pi}_{\substack{\text{ss-gr.}\\\text{d'indice fini}}}",r"\underbrace{\pi' \subset \pi}_{\substack{\text{ss-gr.} \\ \text{d'indice fini}}}",new1),(old2,r"\underbrace{\pi'' \subset \pi}_{\text{id.}}",new2)],1):
 d['changes'].append(dict(place=f'Definition of H: shallow bracket beneath inclusion {n}',C=c,H=h,final=f,against_C=True,against_H=True,kind='drawing or diagram',ink='A shallow horizontal bracket curves upward at both ends. It has no central downward cusp of a curly underbrace. The annotation beneath it remains attached to the same inclusion.',confidence='high',crop='crops/145_scan002_readerB_h_definition.png',box=[742,526,1584,782],marked_in_H=False,consequential=False))
for r in d['changes']:
 if r['place']=='First marginal note: alleged deleted de':
  r['place']='First marginal note: live starred v instead of alleged deleted de'
  r['ink']+=' The separate low star belongs to that same live graph; the deletion-state and missing-star findings are one physical locus, counted once.'
  r['consequential']=True
 if r['place']=='Square: commutatif at the right':r['crop']='crops/145_scan002_main_commutatif.png';r['box']=[1250,785,1650,890]
 if r['place']=='Pencil footer pagination':r['crop']='crops/145_scan002_main_footer.png';r['box']=[15,2250,160,2362]
d['changes']=[r for r in d['changes'] if r['place']!='First marginal note: star after v']
for r in d['inventory']:
 if r['element']=='E09':r['first_words_or_objects']="two shallow flat brackets with upturned ends, labelled ss=gr./ss-gr., d'indice fini; id."
for r in d['remaining_doubts']:
 if r['place']=='Subgroup abbreviation under first underbrace':r['place']='Subgroup abbreviation under first shallow bracket'
d['notes'].append(dict(id='145_scan002-N8',text="A targeted check of the marginal calculation confirms its side of multiplication, conditional on the written covering notation: for gamma in pi'', the quotient projection satisfies p'' composed with gamma = p''. Associativity then gives p'' composed with (gamma composed with u) = (p'' composed with gamma) composed with u = p'' composed with u = v composed with p'. This verifies the displayed identity under that stated action convention. It does not establish the uniqueness claims, the group structure of H_n, or the quotient/germs identification. The unmatched final parenthesis is preserved independently of this check."))
d['check_events'].append(dict(statement_id='145_scan002-N8',who='GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; main reader',type='targeted proof check',outcome="Assuming p'' is the quotient projection by the pi'' action and p''u=vp', checked the three equalities by p''gamma=p'' and associativity. This supports the visible left-multiplication phrase; no obscured letter or punctuation was supplied from the calculation, and no broader lifting/group claim was proved."))
d['notes'].append(dict(id='145_scan002-N9',text='Main also checked the two annotations under the defining inclusions: each uses a shallow flat bracket with raised curved ends, without a central brace cusp. The TikZ lines preserve that shape while keeping the same labels.'))
d['main_adjudication']=dict(original_seen=True,existing_crops_seen=13,main_crops_seen=2,decision='All differences and unresolved loci inspected. Twelve local doubt groups retained; first-reader substantive readings accepted. Two flat-bracket shapes added against both witnesses. The marginal live v-star/deletion interpretation is one physical locus and counted once. Conditional algebraic check recorded separately.')
d['unresolved_for_main']=[]
t.write_text(s);p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
(R/'reviews/145_scan002_main.md').write_text('''# Main-reader adjudication — 145_scan002

Main viewed the original once, all thirteen existing crops, and two new crops for the right-side commutatif placement and pencil footer. The original full diagram, insertion, cancellation and marginal inventory was checked. All forty-five first-reader findings were adjudicated; the two findings about the same marginal v-star graph were merged as one locus, and two bracket-shape corrections were added.

The first NB's u, pi-prime, pi-double-prime, v order and u-star map are retained. The margin's live v-star is a letter plus star, not a cancelled de. The second NB supports ces conditions and u est connu. Gamma and the angular membership/plus-shaped sign remain as localized uncertainty. The two reduced à/colon graphs remain marked in their own places. Germes and literal H-groupes are supported by the short word and H crossbar/stems; no expected ss prefix is substituted.

The two shallow flat brackets under the subgroup inclusions lack a central curly-brace point and are reproduced in TikZ. Both v and the wave lie above the square's lower shaft; commutatif stands to the right. The small margin inclusions are open curves, without arrow shafts or heads. The last equation's closing parenthesis has no matching opening parenthesis, and stays. The definition has no closing set brace, and the page stops at et pi d'indice.

The conditional marginal calculation was checked directly by associativity and the defining quotient-projection identity. Its limited scope is stated in note N8 and CHECK_EVENTS. No proof of the other group, lifting or quotient assertions is claimed. The pencil footer 1 remains of unnamed hand.
''')
