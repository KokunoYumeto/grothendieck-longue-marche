"""Root approval after the recorded twenty distinct adjudication-crop views."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import json
R=Path(__file__).resolve().parents[1]
r=json.loads((R/'checks/scan011_record_draft.json').read_text())
assert len(r['decisions'])==80
assert not any(r['coverage_status'][k] for k in ('unmapped_report_rows','unmapped_reader_doubts','unmapped_inventory_rows','reader_finalization_pending','root_page_path_details_pending','inventory_page_attachments_pending'))
r.update(main_adjudicated=True,main_approved_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),brief_version='v09',draft_status='Root approved after independent-return comparison, personal inspection of twenty distinct adjudication crops, and source/inventory reconciliation.',approval_followups=[])
D={d['id']:d for d in r['decisions']}
for d in r['decisions']:
    assert d['final'] is not None and d['confidence'] in ('high','medium','low')
    assert isinstance(d['diff_C'],bool) and isinstance(d['diff_H'],bool)
    d.update(main_approval_pending=False,root_decided=True,log_decision=True,marked_in_H='no')
    if d['crop'].startswith('out/'):
        d['source_crop_path']=d['crop'];d['crop']=d['crop'][4:]
    assert (R/d['crop']).is_file()
    if d.get('qualification') is None:d['qualification']=''
D['011-D15']['final']='Raised M/U with cancelled/live alternatives; cancelled H; R with cancelled/live alternatives (local details D16–D19)'
D['011-D15']['qualification']+=' The original C doubt attached here concerns M/U; the H row covers the whole adjoining three-form omission.'
D['011-D18']['qualification']+=' Glyph R is recovered with high confidence; its unresolved cancellation target is retained at D19. The same physical cluster is counted once against C.'
D['011-D09']['qualification']+=' C primary E remains an explicit alternative; the e-first change is qualified.'
D['011-D42']['qualification']+=' Qualified primary reversal: U remains an alternative. No expected mathematical label selects H.'
D['011-D46']['qualification']+=' Qualified primary reversal: V remains an alternative. H local detail is included in D66.'
D['011-D62']['crop']='readers/011/A/16_upper_drawing_disk.png; readers/011/A/15_upper_drawing_junction.png'
D['011-D66']['crop']='readers/011/C/10_diagram_top.png; readers/011/C/11_diagram_vertical.png; readers/011/C/12_diagram_lower_right.png; readers/011/C/13_diagram_left_bar.png'
assert D['011-D18']['diff_C'] and not D['011-D19']['diff_C']
assert not D['011-D15']['diff_C'] and D['011-D16']['diff_C']
assert not D['011-D51']['diff_C'] and not D['011-D68']['diff_C']
# Preserve raw local qualifications; the remaining-doubt table uses one row per physical locus.
r['raw_assembled_doubts']=r['doubts']
alt={'01':r'\Rightarrow','05':'2','07':'2','08':'2','09':r'\mathcal E','15':'U; cancelled/live state at either glyph','19':'R live / R cancelled','26':'0','36':'1','40':'R','42':'U','45':'W','46':'V'}
doubts=[]
for old in r['raw_assembled_doubts']:
    if old['decision_id']=='011-D16':continue
    d=D[old['decision_id']];q=dict(old)
    q['reading']=old['final'];q['alternatives']=alt.get(d['id'][-2:],'Role, hand or surface origin unresolved; graphical reading retained')
    q['reason']=old['remaining_qualification']+' '+d['evidence']+' '+d['qualification']
    q['crop']=d['crop']
    if d['id']=='011-D15':
        q['reading']=r'M/U, with cancelled/live alternatives'
        q['reason']+=' D16 records the separate cancellation-state qualification at this same physical form.'
        q['merged_decision_ids']=['011-D15','011-D16']
    doubts.append(q)
r['doubts']=doubts
for x in r['actual_C_doubt_map']:x['main_approval_pending']=False
assert Counter(x['source_row_final_status'] for x in r['actual_C_doubt_map'])=={'retained':9,'resolved':6}
for i in r['inventory']:
    i['transcribed']='yes'
    if i['element']=='011.I08':i['first_words_or_objects']='M/U with cancelled/live state qualified'
    if i['element']=='011.I09':i['first_words_or_objects']='cancelled H'
    if i['element']=='011.I10':i['first_words_or_objects']='R, with cancelled/live state qualified'
r['notes']=r'''The sheet writes P/Hom expressions, with a question mark over the top relation, a large upper-left sketch, a right-hand diagram and three bottom sketches. The archive numeral 10 remains a comment. No title, authorial date or page count is supplied on this sheet.

The two expressions ending with one closing parenthesis retain that visible endpoint. In the live expression below the cancellation, the two inner arguments read E,Z in this order. The operator and the first argument are recovered from their strokes, while the old top-right predecessor remains e/E. The doubled upper-left P, final looped E, cancelled Hom(X), raised middle H and right R, upper diagram H and arch, small overwritten e, and H beneath the live Gamma are resolved locally. Of the fifteen original C doubt-table rows, six resolve completely and nine retain at least one qualified sublocus; the twenty-five original local subloci remain mapped to their source rows.

The arrow-side glyph favours H with U retained; the product subscript favours Y with V retained. Both choices remain qualified, including H's V as an alternative. The raised M/U and the recovered raised R also retain uncertainty about whether the crossing strokes cancel them. The lower t/1 and left O/0 remain open. No inferred writing chronology is supplied.

All observed cancellation paths, unequal upright rules, retraced arrowhead and shaft, detached lower branches and overlapped diagram letters are represented. The upper sketch preserves the gap at the short curled head, the heavy shaft ending at its centre, the additional rim arc, hooks and lower fork. The bottom polygon retains interrupted upper-edge ink, vertex prongs and foot projections; the middle sketch gains the observed elbow ticks and detached spot. The final oval retains its opening, six crossing curves and two small zigzag/loop groups. Newly retained detached marks near formulas and diagram letters are drawn with explicit uncertainty about role, hand or surface origin.

Two finite computations were actually executed at 12:22:20 UTC and are documented in checks/scan011_finite_functions.json, checks/scan011_finite_functions.md and CHECK_EVENTS.tsv. For X={x}, Z={z0,z1}, E={e0,e1,e2}, the program enumerated the nine functions a:Z×X→E and the nine functions b:X→Hom(Z,E). It evaluated T(a)(x)(z)=a(z,x) and T^-1(b)(z,x)=b(x)(z) on every table and checked both inverse compositions and the image. It also enumerated the eight functions X→Hom(E,Z); the recorded map R sends the lexicographic index 0,…,8 of a to the three binary Z-values given by that index modulo8 in E order. The output records all eight images and the shared image of the first and last inputs. These explicit finite maps establish only those computations. Their outputs supplied no ink reading or intended meaning for manuscript P or E.

The author's written question mark over the relation remains a question mark. Structural source validation passed; no successful compilation or rendered-page verification is claimed.'''
r['workflow_note']='Three fresh independent readers each viewed the whole page once and both halves once; A/B/C-reader made16/14/13 local crops. Root personally inspected20 distinct crops (14 existing reader crops and6 new root crops), never a whole page or half. One attempted root06 display failed at the output cap and was unseen; one successful retry was inspected. All150 report rows, all46 reader doubt entries, all15 source C doubt rows and the inventory union are mapped. Fifty-three inventory elements are present. Root retains25 physical doubt/graphic-qualification loci; M/U glyph and state share one. The diagram was written in genuine tikz-cd with local TikZ overlays. Structural checks only. Mechanical assembly used text alone. The two actual finite computations remain separately logged. Brief v10 records the diagram and state-counting lessons.'
r['counting_policy']='Counts use the approved Boolean diff_C/diff_H fields. Each physical locus is counted once per witness; D18 includes D19 for the raised R. D15 is the single H row for the adjoining raised group. Five H physical-object rows cover the upper sketch, three lower sketches and whole diagram; their local C rows cross-reference those H rows. All15 original C doubt-table identities remain separately mapped, including25 local subloci. Counted confidence describes the primary recovered reading; unresolved alternatives remain explicit.'
r['counts'].update(decision_loci=80,C_difference_loci=sum(d['diff_C'] for d in r['decisions']),H_difference_loci=sum(d['diff_H'] for d in r['decisions']),actual_C_doubts_retained=9,actual_C_doubts_resolved=6,remaining_doubt_or_graphic_uncertainty_loci=len(doubts),inventory_elements=len(r['inventory']))
assert (r['counts']['C_difference_loci'],r['counts']['H_difference_loci'],len(doubts),len(r['inventory']))==(49,31,25,53)
for a in r['abbreviations']:
    a['expansion']=a.get('expansion',a.get('possible_expansion',''))
r['root_page_text_exact']=(R/'pages'/r['filename']).read_text()
r['root_crop_manifest']='crops/011/manifest.json';r['root_adjudication_log']='checks/scan011_main_decisions.md'
assert len(r['check_events'])==2
(R/'records/scan011.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(r['counts'])
