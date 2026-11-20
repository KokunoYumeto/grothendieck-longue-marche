"""Assemble a scan-005 decision draft from text records only.

This script never opens images, renders, compiles, changes the page, or updates
cumulative files. The main reader's completed observations are authoritative.
Its only output file is records/scan005/decision_draft.json.
"""
from pathlib import Path
from collections import Counter
import copy
import json
import re

O = Path(__file__).resolve().parents[1]
P = O / 'records/scan005'
R = {a: json.loads((P / f'reader_{a}/report.json').read_text()) for a in 'ABC'}
I = {a: {x['id']: x for x in R[a]['issues']} for a in 'ABC'}
READINGS = {a: (P / f'reader_{a}/reading.tex').read_text() for a in 'ABC'}
WITNESSES = {a: (O.parent / f'reader_inputs/scan005/{a}.tex').read_text() for a in 'CH'}
PAGE = (O / 'pages/H104-01_104_scan005.tex').read_text()
MAIN = (P / 'main_observations.md').read_text()
M = {int(n): body.strip() for n, body in re.findall(
    r'^([0-9]+)\. (.*?)(?=\n[0-9]+\. |\nAll 37 planned|\Z)', MAIN, re.M | re.S)}
assert set(M) == set(range(1, 38)), 'Expected the 37 completed main observations.'

def rp(a, name):
    return f'records/scan005/reader_{a}/crops/{name}.png'

def mp(name):
    return f'crops/scan005_{name}.png'

# Exactly the files delivered to and inspected by the main reader. No rejected
# partial c-target crop or background crop is substituted as main evidence.
MC = {
    1: rp('A', '01_chain_left'), 2: rp('B', '02_chain_end'),
    3: mp('chain_label'), 4: rp('B', '20_detached_curves'),
    5: rp('A', '03_Dn_point'), 6: rp('C', '03_upper_trial'),
    7: rp('B', '05_F_array'), 8: rp('A', '05_small_maps'),
    9: rp('C', '06_Ci_opening'), 10: rp('C', '07_Ci_boundaries'),
    11: rp('C', '08_Ci_equalities'), 12: rp('C', '09_Ci_ending'),
    13: mp('Ci_brace'), 14: rp('B', '11_E0_condition'),
    15: rp('C', '11_pi0_surj'), 16: mp('b_map'),
    17: mp('b_witness'), 18: rp('A', '12_level1'),
    19: rp('A', '24_bprime_start'), 20: rp('B', '22_E1_map_indices'),
    21: rp('A', '25_bprime_membership'), 22: mp('bp_witness'),
    23: rp('B', '13_E1_arrow'), 24: rp('C', '13_E1_cancel'),
    25: mp('bp_pi'), 26: rp('B', '15_c_opening'),
    27: rp('A', '26_c_wprime_membership'), 28: mp('c_target_complete'),
    29: mp('uv_sketch'), 30: mp('E2_label'),
    31: rp('C', '20_cp_opening'), 32: rp('A', '27_cprime_wprime_membership'),
    33: mp('cp_map'), 34: rp('A', '28_cprime_w_membership'),
    35: rp('C', '16_cp_cancel'), 36: rp('C', '18_final_pi'),
    37: rp('C', '17_lower_drawing'),
}
assert len(set(MC.values())) == 37
assert sum(p.startswith('crops/') for p in MC.values()) == 10

# A16 is the upper-right element of the array already represented by A15.
# It is merged there so the same omitted array is not counted twice against H.
# Broader source issues can cover two distinct loci; source_issue_map records
# that relation without creating a second decision for a single physical place.
MAP = {
 1: ('B01','chain_Fleft'), 2: ('B02','chain_index'),
 3: ('B03|B04','chain_alphabets'), 4: ('B05','chain_label'),
 5: ('B07','chain_mark'), 6: ('B08','upper_loose'),
 7: ('B09|B10','Dn_deletion|Dn_dot'), 8: ('B11|B12','brace_x'),
 9: ('B13','trial_arguments'), 10: ('B14','trial_parens_first'),
 11: ('B15','trial_parens_last'), 12: ('B17','trial_bracket'),
 13: ('B16','trial_low_glyph'), 14: ('B18b','trial_dotstroke'),
 15: ('B19','array'), 17: ('B20','array_stroke'),
 18: ('B21','small_s'), 19: ('B22','small_t'), 20: ('B23','small_old_u'),
 21: ('B24','small_maps'), 22: ('B26','Ci_Fprime'),
 23: ('B27','Ci_cancel_phrase'), 24: ('B28','Ci_old_s'),
 25: ('B29','Ci_F'), 26: ('',''), 27: ('B30','Ci_donner|Ci_On'),
 28: ('B31','Ci_u_index'), 29: ('B32','Ci_v_insert'),
 30: ('B33','Ci_de_level'), 31: ('B34',''), 32: ('B34','Ci_conditions'),
 33: ('B35','Ci_ui'), 34: ('B36','Ci_uprimei'), 35: ('B37','Ci_resp'),
 36: ('B38','Ci_g'), 37: ('B39','Ci_vi'), 38: ('B40','Ci_vprimei'),
 39: ('B41','Ci_de_plus'), 40: ('B42','Ci_que_cancel'),
 41: ('B44','Ci_NB'), 42: ('B45','Ci_NB_words'), 43: ('B46','Ci_NB_function'),
 44: ('B48','E0_label'), 45: ('B49','a_label'), 46: ('',''),
 47: ('B50|B51','a_F0'), 48: ('B52','a_map'), 49: ('B53','a_pi_deleted'),
 50: ('B54','a_pi_dash'), 51: ('B55','a_pi_live'),
 52: ('B56|B59','b_membership|b_findices'), 53: ('B57','b_F1'),
 54: ('B58','b_dash'), 55: ('B60','E1_label'), 56: ('B60','bp_circle'),
 57: ('',''), 58: ('B61|B62|B81','bp_fmap|bp_membership'),
 59: ('B62b','bp_udash'), 60: ('B63','bp_label'), 61: ('B65','bp_cancel'),
 62: ('B66','bp_pi_note'), 63: ('B67','c_cancel_F'), 64: ('B68','c_F1'),
 65: ('B69','c_si'), 66: ('B81b','c_membership_prime'),
 67: ('B71|B81c','c_membership'), 68: ('B70','c_oldf_target'),
 69: ('B71','c_oldf_target'), 70: ('B72','c_pi_index'), 71: ('B73','uv_drawing'),
 72: ('B75',''), 73: ('B74','cp_F1'), 74: ('B81d','cp_membership_prime'),
 75: ('B76','cp_f_dash'), 76: ('B81e','cp_membership'),
 77: ('B77','cp_cancel_word'), 78: ('B78','cp_wprime'),
 79: ('B79','final_note'), 80: ('B80','lower_paths|lower_dots'),
}
MN = {
 1:[1],2:[1],3:[1,2],4:[3],5:[2],6:[4],7:[5],
 **{n:[6] for n in range(8,15)},15:[7],
 **{n:[8] for n in range(17,22)},
 **{n:[9] for n in range(22,27)},
 **{n:[10] for n in range(27,31)},31:[10,11],
 **{n:[11] for n in range(32,39)},
 **{n:[12] for n in range(39,44)},
 **{n:[14] for n in range(44,49)},
 **{n:[15] for n in range(49,52)},
 52:[16],53:[17],54:[17],55:[18],56:[18],57:[19],
 58:[20,21],59:[22],60:[23],61:[24],62:[25],
 63:[26],64:[26],65:[26],66:[27],67:[28],68:[28],69:[28],70:[28],
 71:[29],72:[30],73:[31],74:[32],75:[33],76:[34],
 77:[35],78:[35],79:[36],80:[37],
}

def ids(value):
    return value.split('|') if value else []

def reader_value(a, keys, fallback):
    return '; '.join(I[a][k]['reading'] for k in keys) if keys else fallback

issues = []
for n, (b, c) in MAP.items():
    x = copy.deepcopy(I['A'][f'A{n:02d}'])
    akeys = [f'A{n:02d}'] + (['A16'] if n == 15 else [])
    src = {'A': akeys, 'B': ids(b), 'C': ids(c)}
    x['id'] = f'005A{n:02d}'
    x['final'] = x.pop('reading')
    x['source_issues'] = src
    x['readers'] = {a: reader_value(a, src[a], 'No separate issue; see reading.tex.') for a in 'ABC'}
    x['reader_evidence'] = {a: [{'id': k, 'evidence': I[a][k]['evidence']} for k in src[a]] for a in 'ABC'}
    x['main_observations'] = MN[n]
    x['crops'] = list(dict.fromkeys(MC[k] for k in MN[n]))
    x['crop'] = x['crops'][0]
    x['evidence'] = ' '.join(f'Main {k}: {M[k]}' for k in MN[n])
    if len(x['crops']) > 1:
        x['evidence'] += ' Additional main crop: ' + '; '.join(x['crops'][1:]) + '.'
    x['marked_in_H'] = 'no'
    issues.append(x)
D = {int(x['id'][-2:]): x for x in issues}

def upd(n, **kw):
    D[n].update(kw)

def extra(n, location, final, main, C, H, src, confidence='high',
          unresolved=False, diff_C=True, diff_H=True, kind='drawing or diagram',
          bbox=None, fallbacks=None, marked_in_H='no'):
    keys = {a: ids(src.get(a, '')) for a in 'ABC'}
    fb = fallbacks or {}
    paths = list(dict.fromkeys(MC[k] for k in main))
    x = {'id': f'005N{n:02d}', 'location': location, 'C': C, 'H': H,
         'final': final, 'evidence': ' '.join(f'Main {k}: {M[k]}' for k in main),
         'confidence': confidence, 'diff_C': diff_C, 'diff_H': diff_H,
         'kind': kind, 'marked_in_H': marked_in_H, 'unresolved': unresolved,
         'crop': paths[0], 'crops': paths, 'main_observations': main,
         'source_issues': keys,
         'readers': {a: reader_value(a, keys[a], fb.get(a, 'Omitted in reading.tex.')) for a in 'ABC'},
         'reader_evidence': {a: [{'id': k, 'evidence': I[a][k]['evidence']} for k in keys[a]] for a in 'ABC'}}
    if bbox is not None:
        x['bbox'] = bbox
    issues.append(x)
    return x

# Each actual change to a witness-C doubt is counted, including a resolution
# to its former leading candidate. Shared-doubt encoding is not a resolution.
C_CHANGED = {1,2,5,6,7,9,10,11,12,13,14,17,18,19,20,22,23,24,25,26,
             27,28,29,30,32,33,35,40,41,44,45,47,50,51,52,55,57,58,
             60,61,63,64,65,66,67,68,70,71,73,74,76,77,79,80}
for n, x in D.items():
    x['diff_C'] = n in C_CHANGED
    x['diff_H'] = n not in {25,46}
    x['marked_in_H'] = 'yes' if n in {7,23,27,30,31,32,35,36,37,38,42,48,60,68,69,77} else 'no'

upd(1, final=r'\mathbb F', unresolved=False, confidence='high')
upd(2, final=r'\unsure{n-2|n\,2|n-1}', confidence='low', unresolved=True)
upd(3, final=r'\mathbb F_{n-1}; F_n; \mathbb F_{n+1}')
upd(4, C='Left-pointing arrow with its default label below the shaft.',
    final=r't_n-s_n below the joined left-pointing arrow', diff_C=False,
    counting_note='Witness C uses the correct default side. B misdescribes its placement; equivalent arrow syntax does not create a C difference.')
D[4]['readers']['B'] += '; report says below, but its primed label syntax places it above in reading.tex.'
upd(5, final='Literal compact cross-like trace with a rising right upright and short lower-right foot; function unassigned.')
upd(6, final='Detached broken descending curve with a short right foot; two detached rising short strokes to its upper right.')
upd(7, final=r'\deleted{D_n}, with a separate raised point outside the deletion')
upd(8, final=r'Left brace enclosing x\in F_n; separate equality at upper right.')
upd(9, final=r'\unsure{y|f} at the first argument; y at the next three under the same unresolved doubt.',
    confidence='medium', unresolved=True, diff_H=True)
upd(10, final='First t_n argument has its closing parenthesis and no separate inner opening parenthesis; outer opening and final closures retained.')
upd(11, final='Last s_n argument has a closing parenthesis and no inner opening parenthesis; a second outer closing curve follows.')
upd(12, final='Flat low bracket with upturned ends, starting under the outer t-index and ending before the first term closes; bare 0 below.')
upd(13, final=r'\unsure{E_7|E_3|\xi}', confidence='low', unresolved=True)
upd(14, final='Small detached low right dash/point, traced without an assigned function.')
upd(15, final=r'F_0 with a detached shallow smile; plain F_1; plain F\prime_0; doubled \mathbb F\prime_1; no connecting arrows.',
    C=r'F_0 with shallow smile; F_1; F\prime_0; \mathbb F\prime_1.',
    unresolved=False, confidence='high',
    counting_note='A15 and A16 are one array locus. The main reader rejects A16’s extra upper-right alphabet doubt; the array is unchanged from C.')
upd(17, final=r'\unsure{1|\prime}', confidence='low', unresolved=True)
upd(18, final=r'\unsure{s|f}', confidence='low', unresolved=True)
upd(19, final='t at the right end of a left-pointing arrow', unresolved=False)
upd(20, final=r'\exists\deleted{u}s,u\prime', confidence='high', unresolved=False)
upd(22, final=r'w\prime\in\mathbb F\prime_i')
upd(23, final=r'\deleted{si on \unsure{retient|retire}}', confidence='low', unresolved=True)
upd(24, final=r'\deleted{s}\exists', unresolved=False)
upd(25, final=r'\exists w\in F_i', unresolved=False)
upd(26, final='Separate point after F_i and before tel que.',
    readers={'A': I['A']['A26']['reading'], 'B': 'Point omitted in reading.tex.', 'C': 'Point omitted in reading.tex.'})
upd(27, final='On peut se donner d’avance', confidence='high', unresolved=False)
upd(28, final=r'u_{\unsure{i|i-1}}=s_i(w)', confidence='low', unresolved=True)
upd(29, final=r'\inserted{v_i=}t_i(w)', confidence='medium', unresolved=False)
upd(30, final=r'\inserted{de F_{i-1}} (no following comma)', confidence='high', unresolved=False)
D[30]['readers']['B'] += '; reading.tex nevertheless supplies a comma after the level.'
upd(31, final='soumis aux seules conditions ... que', confidence='high', unresolved=False)
D[31]['readers']['C'] = 'soumis aux seules conditions ... que, retained in reading.tex; cancelled de recorded separately.'
upd(32, final=r'\deleted{de} que', confidence='high', unresolved=False)
upd(33, final=r'u_{\unsure{\cdot|i|1}} inside f', confidence='low', unresolved=True)
upd(34, final=r'u\prime_{\unsure{i|1}}', confidence='low', unresolved=True)
upd(35, final=r'\unsure{rp|resp}, without a terminal period.', confidence='medium', unresolved=True)
upd(36, final=r'\unsure{g|f}(v_i)=v\prime_i', confidence='medium', unresolved=True,
    counting_note='The g/f doubt and its order are retained from witness C, despite both B and reader C resolving g.')
upd(37, final=r'v_i inside the argument, retaining i|1 from the preceding u\prime index.', confidence='low', unresolved=True)
upd(38, final=r'v\prime_i, retaining i|1 from the preceding u\prime index.', confidence='low', unresolved=True)
upd(39, final=r'et, \deleted{de} plus, si i-1\geq1 i.e i\geq2', confidence='high', unresolved=False,
    counting_note='Only de is cancelled; plus is live, as clarified by the main reader and encoded in the consolidated page.')
upd(40, final=r'\deleted{que}', unresolved=False)
upd(41, final='NB, without full stops.', unresolved=False)
upd(42, final='on n’exige pas que', unresolved=False)
upd(43, final=r'g(u)=u\prime, with the retained g|f doubt shared from the preceding equality.',
    confidence='low', unresolved=True, diff_C=False,
    counting_note='The local g/f uncertainty is retained. Using its first candidate with a comment is equivalent shared-doubt encoding.')
upd(44, final=r'\unsure{\Xi|E}_0', confidence='medium', unresolved=True)
upd(45, final=r'Circled \unsure{b)|a)}', confidence='low', unresolved=True)
upd(46, location='First quantified s-prime, proposed underline',
    final='s-prime without a distinct separate underline.', confidence='high', unresolved=False,
    readers={'A': I['A']['A46']['reading'], 'B': 'No underline in reading.tex.', 'C': 'No underline in reading.tex.'},
    counting_note='The main reader rejects A’s proposed underline. Both witnesses are retained here.')
upd(47, final=r'\exists s\in\mathbb F_0, u\in\mathbb F\prime_1; preceding F\prime_0 plain.',
    confidence='medium', unresolved=False)
D[47]['readers']['C'] += r'; F\prime_1 after u remains plain in reading.tex.'
upd(49, final=r'\deleted{\pi_0(f)\ \unsure{surj}}', confidence='medium', unresolved=True,
    counting_note='The cancelled word remains doubtful. A/B/C-reader certainty is not adopted; witness C’s word doubt is retained.')
upd(50, final='Detached short dash before the live pi_0(f).', confidence='high', unresolved=False)
upd(51, final=r'\pi_0(f) followed by readable surj with two underlines.', confidence='medium', unresolved=False)
upd(52, final=r'u\prime above downward-open membership (rotation -90 degrees), plain F\prime_1 below; f_0(s)\longrightarrow f_0(t).',
    C=r'u\prime above membership rotated +90 degrees and plain F\prime_1; f_0(s)\longrightarrow f_0(t).',
    confidence='high', unresolved=False)
upd(53, final=r'\exists u\in\mathbb F_1', unresolved=False)
upd(54, final=r'u:s\mathbin{-}t, headless.', unresolved=False)
upd(55, final=r'\Xi_1, retaining the Xi|E doubt marked at level 0.', confidence='medium', unresolved=True)
upd(56, final='Circled b-prime with a separate closing parenthesis crossing the circle.', unresolved=False)
upd(57, final=r'\forall s,t\in\mathbb F_0', confidence='high', unresolved=False,
    readers={'A': I['A']['A57']['reading'], 'B': 'Plain F_0 retained in reading.tex.', 'C': 'Plain F_0 retained in reading.tex.'})
upd(58, final=r'f_0(s)\mathbin{-}f_0(t), headless; u\prime above downward-open membership (rotation -90 degrees), plain F\prime_1 below.',
    C=r'Headless f_0(s)-f_0(t); u\prime above membership rotated +90 degrees and plain F\prime_1.',
    confidence='high', unresolved=False)
upd(59, final=r'\exists u\in F_1; u:s\mathbin{-}t, headless.', confidence='high', unresolved=False)
upd(60, final=r'\ell above the right-pointing f(u)-to-u\prime arrow.', confidence='medium', unresolved=False)
upd(61, final=r'\deleted{\unsure{w|\exists\,w|u}\in F_2}', confidence='low', unresolved=True)
upd(62, final=r'\pi_0(f) inj. et \pi_1(f) surj; the latter phrase has two long underlines with short upturned ends.', unresolved=False)
upd(63, final=r'\deleted{\forall s,t\in\mathbb F_0,}', confidence='medium', unresolved=False)
upd(64, final=r'u,v\in\unsure{F|\mathbb F}_1', confidence='low', unresolved=True)
upd(65, final=r's_i(u)=s_1(v); t_1(u)=t_1(v).', confidence='high', unresolved=False)
upd(66, final=r'w\prime above downward-open membership (rotation -90 degrees), \mathbb F\prime_2 below.', confidence='high', unresolved=False)
upd(67, final=r'\exists w above downward-open membership (rotation -90 degrees), \mathbb F_2 below.', confidence='high', unresolved=False)
upd(68, final=r'\deleted{\unsure{f_1|f}} before live u', confidence='low', unresolved=True)
upd(69, final=r'u\mathbin{-}v, headless.', confidence='high', unresolved=False)
upd(70, final=r'\pi_{\unsure{f|1}}(f) inj.', confidence='medium', unresolved=True)
upd(71, final='Two right-headed arcs, upper labelled u and lower labelled v; both left and right endpoint pairs remain separated.', confidence='high', unresolved=False)
upd(72, final='E_2 with a visible left vertical; circled c-prime without an added closing parenthesis.', confidence='high', unresolved=False)
D[72]['readers']['C'] = 'E_2 and circled c-prime retained in reading.tex.'
upd(73, final=r'\forall(u,v)\in\mathbb F_1', confidence='medium', unresolved=False)
upd(74, final=r'w\prime above downward-open membership (rotation -90 degrees), \mathbb F\prime_2 below.', confidence='high', unresolved=False)
upd(75, final=r'f(u)\mathbin{-}f(v), headless.', confidence='high', unresolved=False)
upd(76, final=r'\exists w above downward-open membership (rotation -90 degrees), \mathbb F_2 below.', confidence='high', unresolved=False)
upd(77, final=r'\deleted{et} before tel que.', confidence='medium', unresolved=False)
upd(78, final=r'w\prime\sim f(w)', confidence='high', unresolved=False)
upd(79, final=r'\pi_1(f) inj et \pi_2(f), with surj below; long curved left-and-top enclosure, no central cusp or bottom boundary.', confidence='high', unresolved=False)
upd(80, final='Separated upper and lower arc endpoints; upper headless, lower with one short acute returning tip. Downstroke with a blunt tip lies between w and prime; three separate low points.', confidence='high', unresolved=False)

extra(1, 'Top chain, first connector',
      'Detached shallow curved left head and separate horizontal shaft, with a visible gap.', [1],
      'Ordinary joined left arrow.', 'Ordinary joined left arrow.', {'B':'B06'},
      bbox=I['B']['B06']['bbox'],
      fallbacks={'A':'Ordinary joined left arrow in reading.tex.', 'C':'Ordinary joined left arrow in reading.tex.'})
extra(2, 'Upper difference, two tiny segments below first t_n',
      'Two detached tiny oblique segments.', [6], 'Omitted.', 'Omitted.', {'B':'B18'},
      bbox=I['B']['B18']['bbox'])
extra(3, 'C_i heading, two points above-left of C',
      'Two detached points inside the parenthesis, above-left of C; no accent assigned.', [9],
      'Omitted.', 'Omitted.', {'B':'B25'}, bbox=I['B']['B25']['bbox'])
extra(4, 'C_i, t comparison after the two level inequalities',
      r't(u)\unsure{\equiv|=}t(v)', [12], r't(u)=t(v)', r't(u)=t(v)', {'B':'B43'},
      confidence='medium', unresolved=True, kind='misread symbol or index',
      bbox=I['B']['B43']['bbox'],
      fallbacks={'A':r't(u)=t(v)', 'C':r't(u)=t(v)'})
extra(5, 'C_i, long side brace',
      'Long irregular curved side brace with central step and final angular foot; C’s existing approximate path retained.',
      [13], 'Existing traced side brace.', 'Omitted.', {'B':'B47','C':'Ci_brace'},
      diff_C=False, bbox=I['B']['B47']['bbox'],
      fallbacks={'A':'C’s existing side-brace path retained in reading.tex.'})
extra(6, 'b-prime, wavy stroke overlapping the lifted-arrow shaft',
      'Right-pointing arrow with wavy/looped stroke overlapping its shaft, encoded as literal paths.', [23],
      'Right arrow with a separate sim below.', r'\ill{} between f(u) and u\prime.',
      {'B':'B64','C':'bp_wavy'}, marked_in_H='yes', bbox=I['B']['B64']['bbox'],
      fallbacks={'A':'Separate sim below the arrow in reading.tex; comment says it crosses the shaft.'})
extra(7, 'c-prime, t_1 comparison', r't_1(u)\mathbin{-}t_1(v)', [31],
      r't_1(u)=t_1(v)', r't_1(u)=t_1(v)', {'C':'cp_t_relation'},
      kind='misread symbol or index', bbox=I['C']['cp_t_relation']['bbox'],
      fallbacks={'A':r't_1(u)=t_1(v)', 'B':r't_1(u)=t_1(v)'})
extra(8, 'c-prime, low rule beneath cancelled et',
      'Separate low horizontal rule meeting the downward cancellation return; no emphasis assigned.', [35],
      'Omitted.', 'Omitted.', {'C':'cp_cancel_rule'}, bbox=I['C']['cp_cancel_rule']['bbox'])
extra(9, 'Bottom sketch, label above the upper arc', r'\unsure{fu)|f(u)}', [37],
      r'f(u)', 'Omitted.', {'C':'lower_label'}, confidence='low', unresolved=True,
      kind='misread symbol or index', bbox=I['C']['lower_label']['bbox'],
      fallbacks={'A':r'f(u)', 'B':r'f(u)'})

# Metadata/recoverability records cover B82/B83 without treating them as ink
# changes. No unviewed reader crop is presented as main-reader evidence.
non_text_records = [
    {'id':'005X01', 'location':'Archive digit at bottom left',
     'source_issues':{'A':[], 'B':['B82'], 'C':[]},
     'final':'Archive sheet number 4, represented only in a comment.',
     'evidence':'All three reading.tex files retain archive sheet number 4. H’s page macro is metadata, not a textual difference.',
     'diff_C':False, 'diff_H':False, 'counted':False},
    {'id':'005X02', 'location':'Pale background impressions',
     'source_issues':{'A':[], 'B':['B83'], 'C':[]},
     'final':'No additional complete typed word is securely recoverable.',
     'evidence':'The three independent reader reports agree on the recoverability limit. The main reader did not inspect a background crop. No background words or illegible-word counts are invented.',
     'diff_C':False, 'diff_H':False, 'counted':False},
]

source_issue_map = {a: {k: [] for k in I[a]} for a in 'ABC'}
for x in issues + non_text_records:
    for a, keys in x['source_issues'].items():
        for k in keys:
            source_issue_map[a][k].append(x['id'])
for a in 'ABC':
    assert all(source_issue_map[a].values()), (a, [k for k,v in source_issue_map[a].items() if not v])
assert len({x['id'] for x in issues}) == len(issues)
for x in issues:
    assert x['crop'] in MC.values()
    assert all(p in MC.values() and (O / p).is_file() for p in x['crops'])
    assert x['confidence'] in {'high','medium','low'}
    assert x['marked_in_H'] in {'yes','no'}

inv = copy.deepcopy(R['C']['inventory'])
INV_UPDATES = {
 'Ci_heading':'(C_i), with two detached upper-left points; universal doubled F′_i; existential plain F_i and following point',
 'top_chain':'Four bracketed terms; first F doubled and n-2/n2/n-1 uncertain; first left head detached; t_n-s_n below middle arrow',
 'F_array':'Plain F_0 with detached shallow smile, plain F_1; plain F′_0, doubled F′_1; isolated 1/prime doubt',
 'upper_loose_strokes':'Broken descending curve with short right foot; two separated rising strokes',
 'Ci_body':'On peut se donner d’avance; u_i/i-1; inserted v_i=; inserted de F_{i-1} without comma; seules conditions',
 'upper_difference':'Four y/f arguments with missing first/last inner opening parentheses; flat low bracket, bare 0, tiny marks',
 'trial_low_glyph':'E_7/E_3/xi, unresolved low overwritten glyph',
 'Ci_equalities':'f(u_dot/i/1)=u′_i/1; g/f(v_i/1)=v′_i/1; s(u)=s(v), t(u) equiv/= t(v)',
 'Ci_resp':'rp/resp, no terminal period',
 'Ci_de_plus':'Only de cancelled; plus remains live',
 'a_pi_cancel':'Cancelled π_0(f) and uncertain surj',
 'E0_a':'Xi/E_0; circled b)/a); plain F′_0, doubled F_0 and F′_1; f_0(s) to s′ labelled u; no s underline',
 'a_pi_live':'Detached dash, π_0(f), readable surj with two underlines',
 'b':'b) forall s,t in plain F_0; u′ over downward-open membership and plain F′_1; doubled F_1 witness; headless s-t',
 'Ci_NB':'NB on n’exige pas que g/f(u)=u′; function doubt retained',
 'E1_bp':'Xi/E_1; circled b′); doubled F_0, downward-open membership over plain F′_1; headless f_0 and s-t maps; looped ell and wave on arrow shaft',
 'bp_cancel':'Cancelled w/exists w/u in plain F_2',
 'c':'c) cancelled universal doubled F_0; live plain/doubled F_1; s_i(u)=s_1(v); downward memberships to doubled F′_2 and F_2',
 'c_oldf':'Cancelled f_1/f before live headless u-v',
 'c_cancel_opening':'Cancelled forall s,t in doubled F_0',
 'final_pi_note':'π_1(f) inj et π_2(f), surj below the first line',
 'E2_cp':'E_2 with upright; circled c′; doubled F_1; s equality and single t dash; downward memberships to doubled F′_2 and F_2',
 'cp_cancel':'Cancelled et, with separate low horizontal rule and downward cancellation return',
 'lower_small_drawing':'fu)/f(u) label; separate arcs, upper headless and lower acute return; downstroke between w and prime; three dots',
}
for x in inv:
    x['sheet_kind'] = 'text'
    if x['element'] in INV_UPDATES:
        x['first_words_or_objects'] = INV_UPDATES[x['element']]

def inv_add(element, kind, position, text, main):
    inv.append({'element':element, 'kind':kind, 'position':position,
                'first_words_or_objects':text, 'sheet_kind':'text',
                'hand':'his hand', 'transcribed':'yes', 'crop':MC[main]})

inv_add('first_connector_gap','drawing','top chain, first connector',
        'Detached shallow curved left head and horizontal shaft',1)
inv_add('Ci_heading_points','drawing','inside C_i heading parenthesis, above-left of C',
        'Two small detached points',9)
inv_add('Ci_post_Fi_point','drawing','right column, after existential F_i',
        'Separate point before tel que',9)
inv_add('trial_tiny_segments','drawing','below the first inner t_n',
        'Two tiny oblique detached segments',6)
inv_add('trial_flat_bracket_zero','drawing','beneath left part of upper difference',
        'Flat bracket with upturned ends, bare 0 below',6)
inv_add('Ci_t_relation','display','right column, last t comparison',
        'Three-bar relation/equality doubt between t(u) and t(v)',12)
inv_add('c_pi_note','display','to the right of condition c',
        'π_f/1(f) inj., f first and unresolved',28)
inv_add('cp_t_relation','display','c-prime, second boundary line',
        't_1(u)-t_1(v), one horizontal mark',31)
inv_add('cp_low_rule','drawing','beneath cancelled et',
        'Separate low rule meeting downward cancellation return',35)
inv_add('lower_sketch_dots','drawing','beneath the lower arc of the bottom sketch',
        'Three distinct low points',37)
inv_add('E0_circle','drawing','first condition label',
        'Oval around uncertain b)/a)',14)
inv_add('E1_circle','drawing','b-prime label',
        'Oval around b-prime and overlapping closing parenthesis',18)
inv_add('E2_circle','drawing','c-prime label',
        'Oval around c-prime, no added closing parenthesis',30)

remaining = [{'location':x['location'], 'reading':x['final'],
              'alternatives':x['final'], 'confidence':x['confidence'],
              'reason':x['evidence'], 'decision_id':x['id'], 'crop':x['crop']}
             for x in issues if x.get('unresolved')]


# Main-reader clerical normalization: order element rows top to bottom and
# separate the alternative candidate from the complete reading in the doubts table.
anchor = {
 'first_connector_gap':'top_chain','Ci_heading_points':'Ci_heading',
 'Ci_post_Fi_point':'Ci_heading','trial_tiny_segments':'upper_difference',
 'trial_flat_bracket_zero':'upper_difference','Ci_t_relation':'Ci_equalities',
 'c_pi_note':'c','cp_t_relation':'E2_cp','cp_low_rule':'cp_cancel',
 'lower_sketch_dots':'lower_small_drawing','E0_circle':'E0_a',
 'E1_circle':'E1_bp','E2_circle':'E2_cp',
}
positions = {}
for row in inv:
    box = re.search(r'\[(\d+),(\d+),(\d+),(\d+)\]', row['position'])
    if box:
        positions[row['element']] = (int(box[2]), int(box[1]))
for key, parent in anchor.items():
    y,x = positions[parent]
    positions[key] = (y + 0.1,x)
inv.sort(key=lambda row: positions.get(row['element'],(99999,99999)))
shared_alternatives = {'005A37':'1 (index)', '005A38':'1 (index)',
                       '005A43':'f (function)', '005A55':'E (level glyph)'}
for row in remaining:
    candidates = re.findall(r'\\unsure\{([^{}]+)\}',row['reading'])
    alternatives = [v.split('|',1)[1] for v in candidates if '|' in v]
    row['alternatives'] = '; '.join(alternatives) if alternatives else shared_alternatives.get(
        row['decision_id'],'No distinct alternative; the canceled word remains insecure.')

notes = [
 'The sheet contains an upper chain, an unfinished upper difference, a four-entry array, small maps, a right-column condition C_i, and three labelled levels of further conditions.',
 'The first chain index remains n-2/n2/n-1. The upper argument glyph remains y/f, and the low overwritten glyph remains E_7/E_3/xi. Missing inner opening parentheses are retained.',
 'F alphabets are recorded separately at each occurrence. The free array has plain F_1. The first existential condition, b-prime opening, and several lower membership levels have doubled F.',
 'The right column retains uncertainty in the first boundary index, the four small equality indices, rp/resp, both g/f occurrences, and the three-bar t relation. Only de is cancelled before live plus. NB has no full stops.',
 'The first two level glyphs retain Xi/E doubt. The first circled label remains b/a. The deleted surj remains doubtful, while the live surj is readable and has two underlines. The pi_1(f) surj phrase also has two underlines.',
 'The c-prime t relation is a single dash. The first s index in c is i. The right pi index remains f/1. These written forms are retained without supplying intended mathematical corrections.',
 'Drawings preserve the detached first arrowhead, small isolated traces, downward-open membership signs, the wave on the lifted-arrow shaft, separate arc endpoints, low cancellation rule, three bottom points, and the final curved top-and-left enclosure.',
 'The bottom sketch label remains fu)/f(u). The archive digit 4 is metadata. The three reader reports identify no securely recoverable complete typed background word; no background passage is supplied.',
 'H drawing 01-4 belongs to scan 006 and is excluded from scan 005. Its x-loop is not a scan-005 discrepancy. The main reader inspected 10 new and 27 reused decision crops once each. No mathematical check event was performed.',
]


# Consequential transcription decisions: these report literal changes and do
# not certify or repair the manuscript's mathematical assertions.
consequential = {
 '005A01':'The first chain object has doubled F, rather than the witnesses\' plain F.',
 '005A02':'The first chain index has n-2 first; n2 and n-1 remain alternatives. No index sequence is supplied.',
 '005A03':'The second and fourth chain F forms are doubled; H\'s uniform plain alphabet is not retained.',
 '005A08':'The open membership brace and its detached equality are retained as unfinished notation.',
 '005A09':'The four upper arguments are y/f, y first, rather than confidently f.',
 '005A10':'The first inner opening parenthesis is absent, so the formula is not silently balanced.',
 '005A11':'The last inner opening parenthesis is also absent; the two visible closing curves remain.',
 '005A18':'The upper small-map source remains s/f; its letter is not inferred from the map.',
 '005A19':'The small-map target is resolved as t.',
 '005A21':'Both lower maps and the zero indices are retained; H omits them.',
 '005A22':'The first C_i membership has doubled F-prime.',
 '005A25':'The existential C_i membership has plain F, contrary to witness C\'s doubled alphabet.',
 '005A28':'The prescribed source index remains i/i-1; the dimension is not corrected from the surrounding condition.',
 '005A29':'The inserted boundary is v_i=, preserving its written attachment.',
 '005A30':'The inserted level de F_{i-1} is recovered rather than left illegible.',
 '005A33':'The first equality\'s argument index remains point/i/1, with the point first.',
 '005A36':'The second equality uses g/f, g first; it is not normalized to the first function f.',
 '005A43':'The closing NB clause retains the same g/f uncertainty and is not treated as a secure f equality.',
 '005A44':'The first level glyph has Xi/E, Xi first; it is not normalized to the unambiguous later E_2.',
 '005A47':'The first existential condition has doubled F_0 and doubled F-prime_1.',
 '005A48':'The visible map is f_0(s) to s-prime labelled u; H\'s incomplete f(u) reading is not retained.',
 '005A52':'The b membership arch opens downwards, and both map indices are zero.',
 '005A53':'The b witness belongs to doubled F_1; H\'s prime on that membership is not retained.',
 '005A54':'The b witness connector s-t is headless, without H\'s added arrowhead.',
 '005A55':'The second level label shares the unresolved Xi/E form.',
 '005A57':'The b-prime universal membership is doubled F_0.',
 '005A58':'The b-prime first connector is headless, both indices are zero, and the membership arch opens downwards.',
 '005A59':'The b-prime witness uses plain F_1 and a headless s-t connector.',
 '005A60':'The lifted-arrow label is looped ell, not a numeral 1.',
 '005A61':'The canceled witness fragment remains w/exists w/u in F_2; a complete existential is not supplied.',
 '005A62':'The written pi_0 injectivity and pi_1 surjectivity annotation is retained.',
 '005A63':'The canceled c opening has doubled F_0.',
 '005A64':'The live c membership remains plain/doubled F_1, without imposing one alphabet.',
 '005A65':'The first c source index is i, followed by s_1(v); the unequal indices are preserved.',
 '005A66':'The c prime witness has downward membership to doubled F-prime_2.',
 '005A67':'The c witness has downward membership to doubled F_2.',
 '005A68':'The canceled target-side character remains f_1/f; it is not promoted into live notation.',
 '005A69':'The c target connector u-v has no arrowhead.',
 '005A70':'The right pi index remains f/1, f first, rather than being normalized to pi_1.',
 '005A73':'The c-prime quantified membership has doubled F_1.',
 '005A74':'The c-prime prime witness has downward membership to doubled F-prime_2.',
 '005A75':'The c-prime connector f(u)-f(v) is headless.',
 '005A76':'The c-prime witness has downward membership to doubled F_2.',
 '005A78':'The last comparison is w-prime similar f(w), retaining the prime absent from H.',
 '005A79':'The final pi_1 injectivity/pi_2 surjectivity note keeps its visible two-line grouping.',
 '005N01':'The first chain connector has a detached head, not a continuously joined arrow.',
 '005N04':'The right-column t relation has three-bar/equality uncertainty, with the three-bar reading first.',
 '005N06':'The lifted arrow carries a visible wave on its shaft.',
 '005N07':'The final t_1(u)-t_1(v) relation is a single bar, not the witnesses\' equality.',
 '005N09':'The bottom label remains fu)/f(u), with the absent opening parenthesis not supplied as certain.',
}
for row in issues:
    if row['id'] in consequential:
        row['consequential'] = consequential[row['id']]


# Exact returned syntax exposes the otherwise generic membership summaries.
for row in issues:
    if row['id'] in {'005A52','005A58','005A66','005A67','005A74','005A76'}:
        for reader in 'AB':
            row['readers'][reader] += r'; actual return: \rotatebox{90}{\(\in\)} (upward opening).'
        row['readers']['C'] += r'; actual return: \rotatebox{-90}{\(\in\)} (downward opening).'
        if row['id'] in {'005A66','005A74'}:
            row['readers']['C'] += r" Lower alphabet: plain F'_2."
            row['readers']['B'] += r" Lower alphabet: plain F'_2."
            row['readers']['A'] += r" Lower alphabet: \mathbb F'_2."
        elif row['id'] in {'005A67','005A76'}:
            row['readers']['C'] += r' Lower alphabet: plain F_2.'
            row['readers']['B'] += r' Lower alphabet: plain F_2.'
            row['readers']['A'] += r' Lower alphabet: \mathbb F_2.'

decision = {
    'scan':5, 'folder':'H104-01', 'issues':issues, 'remaining':remaining,
    'inventory':inv, 'notes':notes, 'checks':[],
    'crop_counts':{'A':29,'B':23,'C':20,'main':10},
    'main_reused_crop_count':27, 'main_total_decision_crop_count':37,
    'main_adjudication_complete':True,
    'assembly_status':'draft; authoritative page and main observations read as text only',
    'source_issue_map':source_issue_map, 'non_text_records':non_text_records,
    'excluded_packet_material':[{'item':'H drawing 01-4','belongs_to_scan':6,
      'reason':'Its own header identifies PDF page 6; excluded from all scan-005 collation and inventory.'}],
    'counting_policy':'Each unique locus is counted once per differing witness. C doubt resolution, pruning, extension and reordering count. Shared-doubt macros, equivalent syntax, archive metadata, unchanged side brace and already headless dashes do not.',
    'residual_questions':[],
}

# A few exact text guards prevent recording a resolved alternative that differs
# from the main reader's consolidated page. These are clerical assertions only.
for literal in [r'\unsure{E_7|E_3|\xi}', r'\unsure{rp|resp}',
                r'u_{\unsure{\cdot|i|1}}', r'\unsure{g|f}(v_i)',
                r't_1(u)\mathbin{-}t_1(v)', r'\unsure{fu)|f(u)}']:
    assert literal in PAGE, f'Consolidated page differs at {literal}'
assert r'\deleted{de} plus' in PAGE
assert r'\arrow[l,"{t_n-s_n}"]' in PAGE

(P / 'decision_draft.json').write_text(json.dumps(decision,ensure_ascii=False,indent=2)+'\n')
counts = Counter()
for x in issues:
    for witness in 'CH':
        if x[f'diff_{witness}']:
            counts[witness] += 1
            counts[f'{witness}_{x["confidence"]}'] += 1
print(json.dumps({'issues':len(issues), 'remaining':len(remaining),
                  'inventory':len(inv), 'counts':dict(counts),
                  'reader_issue_coverage':{a:len(source_issue_map[a]) for a in 'ABC'}},
                 ensure_ascii=False))
