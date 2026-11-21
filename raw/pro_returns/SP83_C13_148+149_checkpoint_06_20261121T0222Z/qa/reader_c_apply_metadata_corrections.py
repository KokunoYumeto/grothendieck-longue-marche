"""Apply only authorized metadata synchronization; preserve all transcription files."""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
PAGES = ['148_scan053', '148_scan056', '148_scan058', '148_scan061',
         '148_scan063', '148_scan064', '148_scan067']
raw = {p: (ROOT/'records'/f'{p}.json').read_bytes() for p in PAGES}
before = {p: json.loads(raw[p]) for p in PAGES}
data = copy.deepcopy(before)
edits = []

def sha(value):
    return hashlib.sha256(value).hexdigest()

def position(page, field, key, value):
    hits = [i for i, row in enumerate(data[page][field]) if row.get(key) == value]
    assert len(hits) == 1, (page, field, key, value, hits)
    return hits[0]

def set_field(page, path, value, basis, evidence):
    obj = data[page]
    for key in path[:-1]:
        obj = obj[key]
    old = copy.deepcopy(obj[path[-1]])
    if old == value:
        return
    obj[path[-1]] = value
    edits.append({
        'page': page,
        'json_pointer': '/'+'/'.join(str(k).replace('~','~0').replace('/','~1') for k in path),
        'operation': 'replace',
        'before': old,
        'after': value,
        'basis': basis,
        'existing_evidence': evidence,
        'new_ink_decision': False,
    })

def note(page, number, text, basis, evidence):
    i = position(page, 'notes', 'id', page+'-'+number)
    set_field(page, ['notes',i,'text'], text, basis, evidence)

def event(page, number, outcome, basis, evidence):
    i = position(page,'check_events','statement_id',page+'-'+number)
    set_field(page,['check_events',i,'outcome'],outcome,basis,evidence)

def notation(page, sign, updates, basis, evidence):
    i = position(page,'notation','sign',sign)
    for key,value in updates.items():
        set_field(page,['notation',i,key],value,basis,evidence)

def append_field(page, field, value, basis, evidence):
    i=len(data[page][field])
    data[page][field].append(value)
    edits.append({'page':page,'json_pointer':f'/{field}/{i}','operation':'add',
                  'before':None,'after':value,'basis':basis,
                  'existing_evidence':evidence,'new_ink_decision':False})

p='148_scan053'
ev=['records/148_scan053.json: notes 148_scan053-N-audit; changes 148_scan053-29, 148_scan053-62',
    'crops/148_scan053_lower_diagram.png']
note(p,'N02',
     'The lower diagram distinguishes forgetting the choice of R′ from erasing the marked points themselves. Two oblique arrows meet at the weighted-graph target; the further right annotation retains a local sigma/gamma weighting doubt and excludes r weighting. At the lower target the b/ph-like group is cancelled while the adjacent dotted i remains live. The overwritten labels and these local alternatives are preserved rather than silently repaired.',
     ['BQA-006','NQ01'],ev)
notation(p,r'\unsure{\sigma|\gamma}',{
    'meaning_or_form':'The low closed oval and long top return favour sigma locally; gamma remains an explicit alternative after comparison with the variable-height gamma forms on 067. This local glyph is not resolved by the shared weighting context.',
    'places':'Lower diagram side note, par the doubtful sigma/gamma glyph, mais non par r.',
    'universality':'One overlapping local occurrence; the sigma/gamma alternatives remain, with no global substitution.'
},['NQ01'],ev+['crops/148_scan067_second_B05.png','crops/148_scan067_second_B09.png','crops/148_scan067_second_B11.png'])

p='148_scan056'
note(p,'N03',
     'The two-level margin and the opening cancelled draft retain several unresolved readings. The (ouverte) insertion has a genuine uncertainty of cancellation scope; the source strike crosses its ending and then all of qui. The final phrase concerning unique isomorphism is kept in its baseline order. The raised soit tuple lies directly below objet/de-category and is linearized immediately after objet; its R decoration retains the R_1, hat-R_1 and prime-R_1 alternatives.',
     ['authorized stale-note synchronization against the existing completed audit'],
     ['records/148_scan056.json: audit_changes B19, B20','crops/148_scan056_second_B19.png','crops/148_scan056_second_B20.png'])
note(p,'N05',
     'The framed old item now has 4 with a raised degree as its leading reading, with A) retained as an alternative under the cancellation. The page has the author’s upper number 12 and lower handwritten number 55. These and every numeric index or exponent fall within the original-image audit boxes.',
     ['authorized stale-note synchronization against the existing completed audit'],
     ['records/148_scan056.json: audit_changes B02; notes 148_scan056-N-audit','crops/148_scan056_second_B02.png'])
notation(p,r'\widetilde\Sigma / \Sigma',{
    'meaning_or_form':'The cancelled opening has a separated wavy accent over Sigma. An additional curved stroke above Sigma inside the live pi-zero formula favours a tilde, but it nearly joins the top bar.',
    'places':'Clear tilde in the cancelled opening; local tilde/plain Sigma doubt in the live component formula in B11.',
    'universality':'The clear cancelled accent is a comparison form, not a resolution of the live ambiguity. No blanket tilde is added to other Sigma symbols.'
},['NQ02'],['crops/148_scan056_old_para3.png','crops/148_scan056_second_B11.png'])

p='148_scan058'
i=position(p,'changes','id','148_scan058-01')
assert data[p]['changes'][i]['final']==r'\deleted{\unsure{ord.|sol.}} \inserted{liées}'
set_field(p,['changes',i,'diff_h'],True,['BQA-001'],
          ['records/148_scan058.json: changes 148_scan058-01; audit_changes B06','crops/148_scan058_second_B06.png'])
note(p,'N03',
     'The marked case is described as recoverable up to a finite ambiguity from the result of the operation. The short expression in the parenthesis remains doubtful en près; the earlier en plus alternative was dropped in the completed audit. The verb remains réverser/inverser. The grammatical oddity of en près is not corrected. No existence or uniqueness proof of the inverse construction is supplied on this page.',
     ['BQA-008'],['records/148_scan058.json: decisions M0746; changes 148_scan058-19','crops/148_scan058_second_B13.png'])
note(p,'N07',
     'The completed audit changed the cancelled edge adjective from the witnesses’ expanded ordinaires to the doubtful abbreviation ord./sol., while retaining the raised liées replacement. Change 148_scan058-01 therefore differs from both C and H and remains one material place; the earlier macro-order-only exclusion is superseded. The handwritten phi denotes the same empty set and is a diplomatic glyph correction, not a change to the mathematical condition.',
     ['BQA-001'],['records/148_scan058.json: changes 148_scan058-01; notes 148_scan058-N-audit','crops/148_scan058_second_B06.png'])

p='148_scan061'
ev=['records/148_scan061.json: changes 148_scan061-28; notes 148_scan061-N-audit',
    'crops/148_scan061_second_B09.png']
note(p,'N01',
     'The sheet recapitulates the operations in the displayed 0-through-7 arrangement, while retaining the first main item numeral as doubtful 4°/1° under retracing rather than correcting it from sequence. The margins classify operations as irreversible, weak strengthening or weakening, and réversible = anodin. These are the author’s classifications. They are transcribed here; no proof of the geometric classifications was attempted on this page.',
     ['NQ03'],['records/148_scan061.json: notes 148_scan061-N-audit; final doubt First main item number','crops/148_scan061_second_B03.png'])
note(p,'N03',
     'Item3 writes an extension quotient with unindexed first and final Z letters in the target. Its remaining local uncertainty is the multiplier d/d_a before r_a, not an a index on the numerator. Both Z_a indices are distinct on the preceding source quotient. No missing index has been supplied from the expected group construction.',
     ['BQA-005','NQ03'],ev)
event(p,'N03',
      'Preserved the indexed source quotient, the unindexed target Z letters and the retained d/d_a multiplier doubt. This is synchronization with the completed transcription audit; no formal correction or proof was used to determine a missing index.',
      ['BQA-005','NQ03'],ev)
notation(p,r'\mathbb Z',{
    'universality':'All clear live Z shapes on this page have the doubled diagonal alphabet. In item3 the first and last target Z are unindexed; the local remaining uncertainty is d/d_a in the multiplier, while the source Z_a indices remain explicit.'
},['BQA-005','NQ03'],ev)

p='148_scan063'
note(p,'N06',
     'Several old readings remain unresolved because cancellation obscures letters. The final ou before the S T/T pair is clear and stands outside the first-word doubt; a possible comma remains uncertain. The run replaced by structures is retained as a cancelled fl.-like group, a possible opening parenthesis, des and doubtful unités/données. The fl. abbreviation is not expanded and no closing parenthesis is supplied. No old word is inferred from the clear replacement.',
     ['BQA-007'],
     ['records/148_scan063.json: notes 148_scan063-N-audit; final doubt Cancelled run replaced by structures'])

p='148_scan064'
ev=['records/148_scan064.json: notes 148_scan064-N-audit; audit_changes B18',
    'crops/148_scan064_second_B18.png']
note(p,'N04',
     'The margin says that the displayed, decoratively doubtful Sigma datum ne joue aucun rôle and proposes working in S T_top^± instead of S T D_top^±. This supersedes the first reading’s formally-empty wording. The cancelled predecessor of rôle and the compressed middle phrase remain doubtful. The two category names and au lieu de were read directly; H’s inclusion symbol is unsupported. The larger groupoïdes on the right of the margin crop belongs to the main paragraph and is not repeated in the note.',
     ['BQA-003','NQ02'],ev)
event(p,'N04',
      'The claim that the Sigma datum plays no role, followed by the proposed change of working category, is carried as the margin’s background statement. No equivalence of categories or reason for discarding the datum is independently proved here, and the doubtful middle prose is not used to infer additional assumptions.',
      ['BQA-003'],ev)
ev_parentheses=['records/148_scan064.json: notes 148_scan064-N-audit; audit_changes B09',
                'crops/148_scan064_second_B09.png']
note(p,'N05',
     'Three long curved strokes function as attachment leaders under raised additions: Pi_1(X;R), the nonempty condition, and the defining phrase. The completed audit distinguishes those leader strokes from separately visible opening parentheses before en tant que and d’un, which are retained. The literal opening square bracket before the defining phrase is retained without an invented closing bracket; the source closing parentheses after opération and X also remain.',
     ['BQA-004'],ev_parentheses)
notation(p,'Curved insertion leaders',{
    'universality':'The same leader structure is visible at these three local additions. Separately visible opening parentheses before en tant que and d’un are retained and are not absorbed into those leaders.',
    'witness_errors':'C places two additions before/after the wrong baseline phrase; its opening parenthesis before en tant que is supported by the completed audit and is not a witness error. H treats en tant que and d’un as part of additions.'
},['BQA-004'],ev_parentheses)
notation(p,r'\unsure{\widetilde{\Sigma}|\Sigma}',{
    'places':'Middle entry of the triple only.',
    'universality':'The tuple retains its own tilde/plain Sigma ambiguity. The marginal opening is a separate occurrence with an additional bar alternative, recorded separately.'
},['BQA-009','NQ02'],['records/148_scan064.json: audit_changes B08','crops/148_scan064_second_B08.png'])
append_field(p,'notation',{
    'sign':r'\unsure{\widetilde{\Sigma}|\overline{\Sigma}|\Sigma}',
    'meaning_or_form':'The marginal opening has a compact Sigma body and a flatter upper run that may be a flattened tilde or bar; plain Sigma also remains an explicit alternative.',
    'places':'Opening sign of the marginal note.',
    'universality':'This three-way ambiguity is local to the margin. It does not enlarge or settle the tuple’s separate tilde/plain alternatives.',
    'witness_errors':'C gives plain Sigma and H a secure tilde here; the completed audit additionally retains the bar alternative without resolving the upper decoration.'
},['BQA-009','NQ02'],ev)

p='148_scan067'
ev_c=['records/148_scan067.json: audit_changes B04; notes 148_scan067-N-audit; final doubt Eight retraced inter-hole initials',
      'crops/148_scan067_second_B04.png']
note(p,'N02',
     'The upper-right construction includes the raised drapeaux de types 0,1, marqué and anti- additions. The large cancellation is retained as the primary state for the definition, equality and torsor construction, but its extent remains explicitly doubtful. The possible elevated stars and old underbrace alpha are ink uncertainties, not readings decided from the mathematics.',
     ['NQ01; existing final cancellation-state mapping'],
     ['records/148_scan067.json: final doubt Extent of the large cancellation; notes 148_scan067-N-audit'])
note(p,'N05',
     'The eight inter-hole initials in the pants figure retain c as a low-confidence primary reading, with a_i^0 and b_i^1 alternatives matching the witnesses. Their retraced outer and inner strokes do not support the earlier unqualified claim that both witnesses misnamed them. The sphere sketch separately has five visible 0–1 curves, whereas the pants sketch has four inter-hole arcs. Both observed counts are retained; no compatibility repair is imposed.',
     ['NQ06'],ev_c)
note(p,'N07',
     'The small triangle retains the apparent c5 rather than silently normalizing to the expected b5, with b5 as an alternative. Its third left-side b_3 label remains individually doubtful. The extra small loop beside the right a2 and the possible earlier a layers under the base c labels remain open. The pale A-like side and base fragments are now recorded explicitly as doubtful A, A_0 and A_infinity; their full letter identity and layer assignment are not asserted.',
     ['NQ04; existing accepted audit B13'],
     ['records/148_scan067.json: audit_changes B13','crops/148_scan067_second_B13.png'])
notation(p,r'c_i^0,\ c_i^1',{
    'sign':r'\unsure{c_i^0|a_i^0},\ \unsure{c_i^1|b_i^1}',
    'meaning_or_form':'Open outer c-like curves coexist with retraced closed or ascending inner strokes compatible with a on the 0 side and b on the 1 side. The accepted c primary remains low confidence.',
    'universality':'All eight inter-hole labels were checked separately and retain their local c/a or c/b alternatives; no unqualified c rule is imposed.',
    'witness_errors':'Both witnesses give a_i^0 and b_i^1; those forms remain explicit alternatives in the accepted doubtful labels rather than being described as secure misnamings.'
},['NQ06'],ev_c)
i=position(p,'doubts','place','Loop interval annotation')
set_field(p,['doubts',i,'alternatives'],'[0,alpha][1,beta); [1,alpha][1,beta)',
          ['NQ05'],['records/148_scan067.json: decisions M0785; audit_changes B08','crops/148_scan067_second_B08.png'])
set_field(p,['doubts',i,'reason'],
          'The opening digit remains doubtful between 0 and 1 beside arc strokes. The completed B08 audit retains alpha in both caption alternatives; gamma is no longer a current alternative.',
          ['NQ05'],['records/148_scan067.json: decisions M0785; audit_changes B08','crops/148_scan067_second_B08.png'])
assert not any(x.get('place')=='Small triangle, third left-side label' for x in data[p]['doubts'])
append_field(p,'doubts',{
    'place':'Small triangle, third left-side label',
    'reading':r'\unsure{b_3}',
    'alternatives':'b_3 as a tentative reading; no additional letter or index candidate is supplied',
    'confidence':'low',
    'reason':'The accepted B13 final tracing already leaves this third left-side b_3 label explicitly doubtful. This entry maps that existing local letter/index uncertainty individually; it is separate from the inter-hole b_3^1 alternative and does not introduce a new ink decision. Existing evidence: crops/148_scan067_second_B13.png.'
},['NQ04; corrected locator'],['records/148_scan067.json: audit_changes B13','crops/148_scan067_second_B13.png'])

# Guard the authorized scope before writing any record.
for page in PAGES:
    for key in ['page','reader','lines_read','decisions','implicit_decisions','inventory',
                'second_boxes','audit_changes','audit']:
        assert data[page].get(key)==before[page].get(key), (page,key)
    for i,row in enumerate(data[page]['changes']):
        old=before[page]['changes'][i]
        if page=='148_scan058' and row['id']=='148_scan058-01':
            expected=copy.deepcopy(old);expected['diff_h']=True
            assert row==expected
        else:
            assert row==old,(page,row.get('id'))
for change_id in ['148_scan067-15','148_scan067-26']:
    old=next(x for x in before['148_scan067']['changes'] if x['id']==change_id)
    new=next(x for x in data['148_scan067']['changes'] if x['id']==change_id)
    assert new==old and new['diff_c'] is False

protected = sorted((ROOT/'pages').glob('*.tex')) + sorted((ROOT/'second').glob('*'))
protected = [f for f in protected if f.is_file()]
protected_hashes={str(f.relative_to(ROOT)):sha(f.read_bytes()) for f in protected}
for page in PAGES:
    path=ROOT/'records'/f'{page}.json'
    assert path.read_bytes()==raw[page], f'Concurrent change to {path}; no overwrite allowed'
for page in PAGES:
    (ROOT/'records'/f'{page}.json').write_text(json.dumps(data[page],ensure_ascii=False,indent=2)+'\n')
for rel,expected in protected_hashes.items():
    assert sha((ROOT/rel).read_bytes())==expected, f'Protected file changed during this operation: {rel}'

log={
    'schema_version':1,
    'editor':'reader_c',
    'performed_at_utc':datetime.now(timezone.utc).isoformat(),
    'authorization':'Root explicitly authorized metadata corrections in records 053,056,058,061,063,064,067; no page TeX, frozen second files, other pages or aggregate assembly.',
    'basis_reports':['result/qa/reader_c_notation_findings.json','result/qa/reader_b_static_findings.json'],
    'edited_record_files':[str(ROOT/'records'/f'{p}.json') for p in PAGES],
    'record_hashes':{p:{'before_sha256':sha(raw[p]),'after_sha256':sha((ROOT/'records'/f'{p}.json').read_bytes())} for p in PAGES},
    'edits':edits,
    'edit_count':len(edits),
    'protected_flags':{'148_scan067-15.diff_c':False,'148_scan067-26.diff_c':False,'status':'unchanged; complete change objects verified identical'},
    'protected_files_verification':{'page_and_second_file_count':len(protected),'unchanged_during_operation':True},
    'new_ink_decisions':[],
    'left_for_root':[
        'Rebuild aggregate tables, notation_final and hand logs from the corrected records; aggregate assembly was not touched.',
        'Retain 053 sigma/gamma and all local Sigma/divisor/index alternatives; none was resolved by this metadata task.',
    ],
    'report_errata':[
        {'report':'result/qa/reader_c_notation_findings.json / .md','finding':'NQ04',
         'incorrect_locator':'small-triangle right side; crops/148_scan067_second_B12.png',
         'correct_locator':'small triangle third left-side label; crops/148_scan067_second_B13.png',
         'action':'Correct locator used in the new record doubt and this log; accepted B13 tracing already contained unsure b_3.'}
    ],
    'not_modified':[
        'All accepted page TeX files','All second/frozen reading files','Records 071,072,149003,149004 and every other unlisted page',
        'Aggregate assembly, hand logs and consolidated notation files','261 supplied decisions and all implicit decisions',
        'Historical first/second audit readings and prior audit conclusions'
    ],
}
(ROOT/'qa/reader_c_metadata_corrections.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'records':len(PAGES),'field_edits':len(edits),
                  'log':str(ROOT/'qa/reader_c_metadata_corrections.json'),
                  'by_page':{p:sum(x['page']==p for x in edits) for p in PAGES},
                  'protected_flags_unchanged':True},indent=2))
