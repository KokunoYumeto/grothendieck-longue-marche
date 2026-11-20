from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
root=Path('/workspace/scratch/8f839dff4bf0')
work=root/'SP74_C13_143+145_work'
p=json.loads((root/'reader_packets/143_scan009.json').read_text())
a=json.loads((work/'reviews/143_scan009_accepted.json').read_text())
before=(work/'pages/143_scan009.tex').read_text()
assert a['reader']=='B'
old=r"$\unsure{\mathcal E'|\Sigma'}$."
new=r"$\unsure{\mathcal E'|\Sigma'}$\unsure{.}"
assert before.count(old)==1
tex=before.replace(old,new,1)
views=[
 ('crops/143_scan009_readerB_formula25.png',[375,150,1605,325]),
 ('crops/143_scan009_readerB_interline_stabilizer.png',[1095,405,1665,505]),
 ('crops/143_scan009_readerB_cancelled_block26.png',[240,750,1672,1015]),
 ('crops/143_scan009_main_recap_heading.png',[210,1000,1565,1130]),
 ('crops/143_scan009_readerB_under_inclusion.png',[470,1545,875,1710]),
 ('crops/143_scan009_readerB_subgroup_abbreviation.png',[455,1975,1650,2080])
]
finding=dict(
 place='End of canceled compatibility sentence, after the final extension-group glyph',
 before=old,after=new,
 reason='The long horizontal cancellation stroke continues through the area immediately after the final E-prime/Sigma-prime. Several short dark projections appear along its lower edge, but I cannot isolate one independent sentence-final point from that struck area. The possible period is retained with an explicit doubt, rather than either removed or asserted as secure.',
 confidence='low',crop='crops/143_scan009_readerB_cancelled_block26.png',box=[240,750,1672,1015],
 against_C=False,against_H=True,C=r"$\mathcal E'$.",H=r"\struck{compatible avec op.\ de $\Sigma'$}",
 kind='other',consequential=False,marked_in_H=False,decision_updates=[],certainty_only=True,
 existing_difference_revision=dict(index=10,place='Cancelled final line, group',revision='The accepted low-confidence E/Sigma choice remains unchanged. Its final-reading excerpt also carries a sentence-final period; that point should now be explicitly doubtful. This is a certainty-only proposal, not a new material alphabet or punctuation correction.')
)
assert finding['before'] in before and finding['after'] in tex
assert finding['C'] in p['witness_C'] and finding['H'] in p['witness_H']

confirmed=[]
def check(place,observations,crop='page',box=None):
 confirmed.append(dict(place=place,observations=observations,crop=crop,box=box))
check('Opening line and insertion','Read Enfin, on a une famille de scindages and the raised partiels at the upper right. The adjective is an insertion attached to scindages, not a new paragraph or a separate heading.')
check('Formula (25), family and map',r'The left label is (25). The initial Psi bears a crossed superscript; ext remains only tentative. The family has Psi_j, lower j in J and a colon. The source has a tilde, a detached prime before (j), a headed rightward arrow, Hom with G-prime and a separate j subscript, and the primed extension glyph with a canceled X-prime index. Two closing parenthesis curves follow the target. The small superscript belongs to the initial Psi, not Psi_j.','crops/143_scan009_readerB_formula25.png',[375,150,1605,325])
check('Inverse-image parenthesis','Read où cette fois, désigne l’image inverse, de G-prime included in G_X-prime, and dans the extension glyph with X-prime index. The group prime, both X-prime indices, inclusion sign and punctuation were checked locally. The repeated extension glyph remains E/Sigma rather than being renamed from context.')
check('Stabilizer insertion','The first inserted calligraphic G has a detached prime above a separate lower j. The remainder reads le stab. de j dans G-prime. The long curved guide joins the insertion to the end of the inverse-image parenthesis before compatible.','crops/143_scan009_readerB_interline_stabilizer.png',[1095,405,1665,505])
check('Live compatibility sentence','Read compatible avec les opérations de the primed extension glyph, de part et d’autre, including the comma before the canceled continuation. Its wording and cancellation boundary agree with the accepted fragment.')
check('Canceled continuation and formula (26)','The canceled opening supports s’inscrivant, not se prolongeant. The next line has scindages mod op. de pi-one. Formula (26) retains both ext superscripts, the j-in-J family index, the colon-compatible residue, tilde-X-prime with capital J, a headed arrow, Hom, a division slash and Int with pi-one and the primed extension glyph. The possible outer close after (J), possible j on the first Hom argument, and clipped final extent remain uncertain. The horizontal and oblique cancellation strokes apply to the whole block.','crops/143_scan009_readerB_cancelled_block26.png',[240,750,1672,1015])
check('Canceled last sentence','The first word supports également: the g descender, tall l and low ement sequence differ from équivariante. Compatible avec op. de and the primed extension glyph stand. Only the certainty of the last point is proposed to change.','crops/143_scan009_readerB_cancelled_block26.png',[240,750,1672,1015])
check('Section 6 and abandoned restart','A continuous oval surrounds 6; Récapitulons. has two separate underlining strokes. On a donc is followed by two stacked points and the looped X of the abandoned restart. The following canceled line reads schéma de t.f. sur barred Q, un divi; there are no independent seur letters or terminal hyphen to restore.','crops/143_scan009_main_recap_heading.png',[210,1000,1565,1130])
check('Display I, scheme and divisor conditions','Checked the left brace and Roman I, X de t.f. sur barred Q, D equals the sum over i in I of D_i, diviseur effectif sur X à comp., simples, X lisse en les pts maximaux, and de supp D. The lower i and capital I of the sum, repeated scheme letters, barred Q, abbreviation points and comma after simples were inspected; no correction is proposed.')
check('Display I, inclusion and complement','The last line contains J, a proper subset-shaped curve, X-prime(barred Q), a comma and où X-prime = X-D. The tiny lower word has a long returning trace, dark middle join and detached terminal dot; its interior letters remain too compressed to settle fini. M0660 therefore stays undecided with underlined fini only tentative.','crops/143_scan009_readerB_under_inclusion.png',[470,1545,875,1710])
check('Transition and margin mark','On pose has no added colon. The isolated fine curve at the far-left margin is an opening parenthesis; M0661 remains the first reading. No paired closing mark is supplied.')
check('Display II, first definition','Checked calligraphic G-prime, the short gr without expanded oupe, des autom without a following point, du schéma, the raised absolu attached before the scheme letter, and qui invarie D et J. The source’s wording remains unchanged.')
check('Display II, subgroup definition','The initial block G-prime is heavily retraced and retains a lower returning stroke; this does not expose a separate readable canceled token. The abbreviation has two compact s forms, a hyphen and gp, followed by de calligraphic G-prime formé des barred-Q-autom. The terminal point after autom is separate and visible.','crops/143_scan009_readerB_subgroup_abbreviation.png',[455,1975,1650,2080])
check('Display II, inverse limit and Galois group','Checked the T expression with barred Q, the leftward limit arrow with lower n, mu with lower n and barred-Q argument, and Gamma = Gal(barred Q / Q). The bars, lower indices, slash, parentheses and direction of the limit arrow agree with the accepted text. No group-theoretic assertion was proved.')
check('Pagination, scope and alphabet conventions','The faint lower-left pencil mark has two joined loops and is retained as 8, with no author identification. All source text blocks, two numbered formulas, two recap displays, insertions, cancellations and marginal items were inspected. The established mathfrak-X and bold-Q/T renderings are retained without new font-only findings; the repeated E/Sigma alphabet ambiguity remains local uncertainty.')

remaining=[dict(x) for x in a['remaining_doubts']]
remaining.append(dict(place='Final point of the canceled compatibility sentence',reading=r'\unsure{.}',alternatives='sentence-final point / small residue of the cancellation stroke',confidence='low',reason='The horizontal cancellation crosses the terminal area, with several lower-edge projections; no independent point can be isolated securely in the existing crop.'))
report=dict(
 key='143_scan009',reader='C',stage='second reading',first_reader='B',
 image_views=['original','half1','half2'],
 existing_crop_views=[dict(crop=crop,box=box) for crop,box in views],new_crops=[],
 findings=[finding],confirmed=confirmed,remaining_doubts=remaining,
 notes=[
  dict(id='143_scan009-auditC-N1',text='The second reading supports the accepted words, indices, primes, arrow directions, insertion attachments and cancellation boundaries throughout this sheet. No material word, mathematical symbol, numerical label or diagram correction is proposed. The only proposed change is explicit uncertainty on a sentence-final point crossed by the cancellation.'),
  dict(id='143_scan009-auditC-N2',text='All five existing remaining-doubt entries remain. Neither original MARK is newly resolved or reversed: M0660 remains undecided, and M0661’s opening parenthesis is confirmed. No mathematical expectation was used to fill the canceled superscript, possible Hom subscript, delimiter, or tiny under-inclusion word.'),
  dict(id='143_scan009-auditC-N3',text='The page’s claims about partial splittings, compatibility and the recap data were read as source statements. The automorphism-group, inverse-limit and Galois-group lines were checked visually; their validity was not independently proved. The pencil numeral remains assigned to an unnamed hand.'),
  dict(id='143_scan009-auditC-N4',text='The whole original and both existing native halves were each viewed once. Six existing tight crops were reused once each. No new crop, enlarged half, source research, OCR or TeX compilation was used. The accepted fragment and accepted report were not changed.')
 ],
 check_events=[
  dict(statement_id='143_scan009-auditC-N1-upper',type='carried as background without fault found',outcome='Compared the upper partial-splitting formula, inverse-image explanation, stabilizer insertion and canceled continuation with the ink. This checked text and notation only, not existence or compatibility of splittings.'),
  dict(statement_id='143_scan009-auditC-N1-recap',type='carried as background without fault found',outcome='Read every hypothesis and symbol in display I, including the uncertain annotation below the inclusion. No smoothness or finiteness consequence was inferred or proved.'),
  dict(statement_id='143_scan009-auditC-N3',type='carried as background without fault found',outcome='Visually checked both group definitions, the inverse-limit row and the Galois-group row. No independent proof, formal certificate or calculation was performed.')
 ],
 hand_log=[
  dict(habit='Detached short primes are distinct from the long j subscript strokes.',places='143_scan009 formula (25) and stabilizer insertion',scope='The added primes in the accepted text were checked in the existing formula and insertion crops.',misreadings='Both witnesses omit the X-prime and the inserted stabilizer prime; the accepted additions stand.'),
  dict(habit='Crossing cancellation lines can make nearby terminal punctuation inseparable from their own edge projections.',places='143_scan009 canceled last compatibility sentence',scope='One final point is newly left doubtful; this is not applied to clear points elsewhere.',misreadings='The accepted/C final point is not independently secure in the reused cancellation crop.'),
  dict(habit='Heavy retouching can leave an old returning descender without establishing a separately deleted token.',places='143_scan009 subgroup initial G-prime',scope='One retouched initial inspected in the existing subgroup crop.',misreadings='No new deleted character is manufactured beneath the visible G.'),
  dict(habit='Very compressed underwritten words may retain a terminal dot but not distinct interior letters.',places='143_scan009 M0660 under the subset sign',scope='The existing uncertainty is retained after the crop was inspected.',misreadings='Neither expected finiteness nor the prior tentative fini reading settles the ink.')
 ],
 inventory_additions=[],
 existing_doubt_disposition='No existing doubt removed or narrowed. The five accepted entries are retained, and one new local punctuation doubt is added. Original MARKS M0660 and M0661 receive no decision update.',
 accepted_fragment_sha256=hashlib.sha256(before.encode()).hexdigest(),
 completed_at=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
)
for crop,box in views: assert (work/crop).exists()
assert report['reader']!=report['first_reader']
assert set(d['id'] for d in p['marks'])=={'M0660','M0661'}
for f in report['findings']:
 assert f['before'] in before and f['after'] in tex
 assert f['C'] in p['witness_C']
 assert f['H']=='[no witness]' or f['H'] in p['witness_H']
 assert all(d.get('id') in {'M0660','M0661'} for d in f['decision_updates'])
# Structural grouping check only; source parentheses are not normalized.
depth=0
for index,char in enumerate(tex):
 if char not in '{}':continue
 pos=index-1
 while pos>=0 and tex[pos]=='\\':pos-=1
 if (index-1-pos)%2:continue
 depth+=1 if char=='{' else -1
 assert depth>=0,index
assert depth==0
assert sorted(re.findall(r'\\begin\{([^}]+)\}',tex))==sorted(re.findall(r'\\end\{([^}]+)\}',tex))
(work/'reviews/143_scan009_auditC.tex').write_text(tex)
(work/'reviews/143_scan009_auditC.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'candidate':str(work/'reviews/143_scan009_auditC.tex'),'report':str(work/'reviews/143_scan009_auditC.json'),'material_findings':0,'certainty_only_findings':1,'confirmed_checks':len(confirmed),'remaining_doubts':len(remaining),'existing_crops_reused':len(views),'new_crops':0},ensure_ascii=False,indent=2))
