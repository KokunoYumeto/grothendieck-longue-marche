"""Join visually confirmed historical pagination defects to exact repairs.

This verifies source coverage only.  Final publication-page confirmation is a
separate, hash-bound visual inspection after the books have been rebuilt.
"""
from pathlib import Path
import json,re,hashlib,collections
import layout_repairs

ROOT=Path(__file__).resolve().parents[2]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    data=ROOT/'work/data'
    reviewed=json.loads((data/'pagination_review_before_repairs.json').read_text())
    bindings=json.loads((data/'layout_tag_bindings.json').read_text())
    applied={(r['id'],r['language']):r for r in json.loads((data/'layout_repairs_applied.json').read_text())}
    joined=[];cleared=[]
    for q in reviewed['candidates']:
        if q['decision']!='confirmed detached tag':
            cleared.append({k:q.get(k) for k in ['reader','page','tag','decision','observation','historical_pdf_sha256','native_pair_image_sha256']});continue
        lang='en' if '_EN_' in q['reader'] else 'fr'
        tag=re.sub('[^0-9a-z]','',q['tag'].lower())
        package=q.get('source_package');scan=q.get('source_scan')
        contexts={(str(v['cote']),int(v['scan'])) for field in ['scan_context','adjacent_scan_context'] for v in q.get(field,[])}
        matches=[r for r in bindings if r['language']==lang and r['tag']==tag
                 and(not package or r['package']==package) and(not scan or r['scan']==int(scan))
                 and(bool(package) or bool(scan) or (layout_repairs.COVERAGE[r['package']]['cote'],r['scan']) in contexts)]
        trailing='after_previous' in q['direction']
        matches=[r for r in matches if ('trailing' in r['id'])==trailing]
        basis='Canonical reviewed source location' if package or scan else 'Unique exact binding of the reviewed tag in the historical linked scan context'
        if len(matches)>1 and q.get('source_line'):
            exact=[r for r in matches if applied[(r['id'],lang)]['source_line']==int(q['source_line'])]
            if len(exact)==1:matches=exact;basis+='; exact raw-source line selects the repeated tag'
        assert len(matches)==1,(q['reader'],q['page'],q['tag'],[r['id'] for r in matches])
        b=matches[0];r=applied[(b['id'],lang)]
        joined.append(dict(reader=q['reader'],historical_page=q['page'],historical_adjacent_page=q['adjacent_page'],
            tag=q['tag'],direction=q['direction'],historical_pdf_sha256=q['historical_pdf_sha256'],
            before_image=q.get('final_archive_image',q.get('native_pair_image')),
            before_image_sha256=q.get('native_pair_image_sha256'),repair_id=b['id'],language=lang,
            source_path=r['source_path'],package=r['package'],cote=r['cote'],scan=r['scan'],
            source_line=r['source_line'],source_offset_start=r['source_offset_start'],source_offset_end=r['source_offset_end'],
            source_byte_start=r['source_byte_start'],source_byte_end=r['source_byte_end'],
            source_resolution_basis=basis,expected_match_count=1,source_binding_confirmed=True,
            final_publication_visual_status='Awaiting rebuilt publication PDF and actual final-page inspection'))
    assert len(joined)==80 and len(cleared)==26
    kinds=collections.Counter(r['kind'] for r in bindings)
    obj=dict(schema='exact-source-pagination-reconciliation-v1',historical_primary_candidates=len(reviewed['candidates']),
        confirmed_detached_instances=len(joined),cleared_same_page_instances=len(cleared),
        all_confirmed_instances_bound_exactly=True,exact_binding_records=len(bindings),paired_binding_sites=len(bindings)//2,
        covered_standalone_leading_tag_sites=113,leading_tag_binding_sites=112,
        confirmed_trailing_tag_sites=2,section_opening_binding_sites=1,
        overlap_resolution='Section140-3:548 V and its leading equation(1) use one complete opening group; no redundant nested binding is emitted.',
        affected_packages=len({r['package'] for r in bindings}),record_kinds=dict(kinds),
        layout_tag_bindings='data/layout_tag_bindings.json',layout_tag_bindings_sha256=digest(data/'layout_tag_bindings.json'),
        layout_module_sha256=digest(ROOT/'work/scripts/layout_repairs.py'),
        stress_probe_summary='work/layout_probes/tag_pattern_stress_validation.json',
        final_page_inspection_is_a_separate_required_gate=True,confirmed_instances=joined,cleared_instances=cleared)
    (data/'layout_pagination_reconciliation.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    print(len(joined),'confirmed book instances joined to',len({r['repair_id'] for r in joined}),'exact paired source bindings;26 cleared cases retained; final-page inspection pending.')

if __name__=='__main__':main()
