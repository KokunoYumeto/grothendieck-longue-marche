"""Root consolidation of the independently reread underline on scan095."""
from audit_support import load, replace_exact, commit

r,a,s=load(95)
c=a['changes'][0]
s=replace_exact(s,c['before'],c['after'])
row=next(x for x in r['changes'] if x['id']=='095-37')
row.update(final=r'\uline{un}',c_changed=True,h_changed=False,
           scan_shows=c['scan_shows'],confidence='high',
           math_note='Second reading reverses the first consolidation’s double underline. H’s italic macro represents the single source emphasis and creates no substantive difference.')
row['audit_history']='Originally read as two underlines with C unchanged and H changed. The full second reading and root’s reused crop distinguish the connected letter bodies from one independent underline; flags reversed accordingly.'
r['hand_log'].extend(a['hand_log_additions'])
old='H italic extérieures is treated as representing the source underline; no macro-only difference row is counted. Its single emphasis on un does not encode the visibly doubled underline. The margin separator is preserved as a simple TikZ stroke.'
new='H italic extérieures and un are treated as representing the respective single source underlines; no macro-only difference row is counted. The second reading corrects the initial double-underline interpretation of un. The margin separator is preserved as a simple TikZ stroke.'
assert old in r['notes'];r['notes'][r['notes'].index(old)]=new
r['notes'].extend([
    'The complete second reading finds one separate straight underline below the connected bodies of un in the first marginal note. The main reader reused margin_first and agrees. Existing comparison row 095-37 is revised: C explicitly doubles the underline; H preserves the corresponding single emphasis.',
    'Two tiny dark points directly below-left of the stable-sous Theta oval, approximately x847–854/y1794–1808, have no independent textual or annotative position. Auditor and main reader separately inspected them in star_map_lift and exclude them as incidental pen traces. No punctuation, drawing or inventory element is invented.',
    'All 27 inventory elements, 44 inherited comparison loci and 18 mark decisions were checked in the full second reading. All nine inherited doubts remain. No mathematical check event was added.'
])
commit(95,r,a,s,
    'Complete independent second reading by reader_c. All 44 inherited comparison loci, 18 mark decisions and 27 inventory elements were reviewed. The main reader inspected the saved marginal crop and accepted one single-underline correction at existing row 095-37; its C/H flags are revised, without adding another counted place. All nine doubts remain. Two incidental points below Theta were explicitly excluded after independent inspection. No missing element or mathematical check event.',
    [{'id':c['id'],'decision':'accepted','reading':r'\uline{un}','evidence':c['scan_shows'],'crop':c['crop'],'confidence':'high','revised_row':'095-37'}])
