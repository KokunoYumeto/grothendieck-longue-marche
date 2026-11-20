import json,pathlib
p='H97-01_97_scan019'; root=pathlib.Path('out');r=json.load(open(root/'work'/f'{p}_report.json'))
s=(root/'work'/f'{p}_draft.tex').read_text()
old=r'Z^{1}\llap{\raisebox{-.12ex}[0pt][0pt]{\tiny\unsure{.}}}(X)'
s=s.replace(old,r'Z^{1}(X)')
c=next(c for c in r['changes'] if c['id']=='r23');c.update(final=r'Z^{1}(X)',changed_C=True,changed_H=False,confidence='medium',kind='text not on page',consequential=False,scan_shows='Context: qui est donc un élément de Z^1(X). The isolated small spot below-left of the exponent has no syntactic place and is narrower and lighter than the typed punctuation. Root treats it as a nontextual speck, following the prompt rule; it is not a conjectural extra formula sign. See b20.')
for b in r['boxes']:b['reading']=b['reading'].replace(old,r'Z^{1}(X)')
r['doubts']=[d for d in r['doubts'] if d['line']!='L21']
r['notes']=[n.replace('and tiny dot by Z^1 remain doubtful','remains doubtful; the isolated dot by Z^1 is excluded as a nontextual speck') for n in r['notes']]
r['notation']=[n.replace('and the small dot by Z^1 are separate unresolved marks','is a separate unresolved mark').replace('not inferred from this notation','not inferred from this notation; the isolated low dot near Z^1 is excluded as a speck') for n in r['notation']]
r['notes'].extend(['Root crop adjudication: accepts the first-reader readings of the 31 boxes, including doubled underlined O_U and tentative cancelled positif. Excludes the tiny isolated spot by Z^1 as nontextual. The faint opening prime and obscured cancelled words remain doubtful.', 'Targeted check of the length step in (21.6.6): for regular t, multiplication by t induces an injection A/t′A → A/tt′A with quotient A/tA. Thus 0 → A/t′A → A/tt′A → A/tA → 0 is exact; finite lengths add. This checks the displayed local algebraic step, not all geometric hypotheses of the proposition. The second printed plus is retained as the source continuation sign across a line break.'])
r['check_events'].append({'statement_id':'(21.6.6), local length identity','type':'targeted proof check','outcome':'Verified the exact sequence 0 → A/t′A --×t→ A/tt′A → A/tA → 0 using regularity of t; additivity of finite length gives the claimed identity. This is a local step check, not an independent re-proof of the whole proposition. Repeated source line-break plus retained.'})
r['primary_review']='Root inspected the whole sheet and all 31 saved crops; adjudicated the source states and recorded the local length-step check.'
(root/'pages'/f'{p}.tex').write_text(s)
(root/'work'/f'{p}_decided.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
