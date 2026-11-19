from audit_work import *
p=OUT/'pages/J156-5-03_156-5_scan025.tex';s=p.read_text().replace(r'\unsure{\mathcal J|\mathscr F}',r'\unsure{\mathcal F|\mathcal J}');p.write_text(s)
p=OUT/'records/scan025.json';r=json.loads(p.read_text());d=r['changes'][1];d['final']='unsure mathcal F|mathcal J';d['evidence']+=' Cross-page second audit: 011_audit_figures_glyph.jpg shows the same leftward middle bar, bent stem and hooked top. Consistent F encoding restored as first reading; J retained for the more closed lower loop on 025.'
for d in r['doubts']:
 if d['place']=='figures glyph':d['reading']='mathcal F';d['alternatives']='mathcal J'
r['doubt_decisions'].append('Cross-page audit compared the glyph directly with scan011. Same middle left stroke and hooked stem favor uniform mathcal F encoding; J remains a local alternative on 025.')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');regenerate()
