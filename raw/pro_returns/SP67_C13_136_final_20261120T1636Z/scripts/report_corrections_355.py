from workflow import *
p=ROOT/'records/scan355.py'
r=ast.literal_eval(p.read_text())
r['changes']=[x for x in r['changes'] if x['place']!='H next section heading']
for x in r['changes']:
 if x['place']=='callout linking B_0 to upper Ab_* annotation':
  x['H']='Ab_* written on the earlier equality line; callout omitted'
  x['dh']=True
 if x['place']=='enclosure of F(X_*) formula': x['H']='regular box'
r['inventory'][5]['first_words_or_objects']='equivalence Ab_* with curved headless callout from B0'
r['inventory'][16]['first_words_or_objects']='F(X_*) in irregular sloping, open-right enclosure'
r['note']+=' H’s final section heading for the following Eilenberg–Zilber section is editorial and is excluded from the collation count.'
p.write_text(pprint.pformat(r,sort_dicts=False,width=120)+'\n')
p=ROOT/'scripts/audit_355.py';s=p.read_text().replace("'annotation with connection described'","'Ab_* written on the earlier equality line; callout omitted'").replace("'drawing or diagram',True,False,'high','page'),change('enclosure", "'drawing or diagram',True,True,'high','page'),change('enclosure").replace("'box described'","'regular box'")
p.write_text(s)
log('report metadata corrected scan355: verified H callout omission and regular box; removed editorial section-heading row; inventory descriptions enlarged; no transcription changed')
rebuild()
