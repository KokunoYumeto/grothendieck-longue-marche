from audit_work import *
p=OUT/'pages'/Path(mapping(18)['codex_file']).name
p.write_text(p.read_text().replace(r'\delta A',r'\partial A'))
q=OUT/'records/scan018.json';r=json.loads(q.read_text())
d=r['changes'][18]
assert d['place']=='boundary symbol'
d.update(final='partial A, twice',c_changed=True,h_changed=False,confidence='high',evidence='002_audit_boundary.jpg, 015_audit_boundary.jpg, 018_audit_boundary.jpg and 018_audit_boundary_lower.jpg: the upper leftward hook and lower loop recur, including the nearly horizontal head immediately before A. The two forms on scan002 itself match the rounded and angular forms of scans015/018. The folder-three delta encoding is harmonized to partial; this is a comparison of visible strokes, not a topological correction.')
r['notation_audit']='Boundary glyph compared directly to scans002 and015; partial retained throughout boundary formulas; Greek delta proposition labels are separate.'
q.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
regenerate()
audit(18,'Second visual reading of dated heading, top replacements, topological restrictions, both slanted notes and cancellations. Direct crops of scans002,015,018 identify the repeated boundary glyph; replaced folder-three delta by partial in its two occurrences. Retained the uncertain lower ordinal phrase and dense cancelled marginal draft.')
