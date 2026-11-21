"""Root decisions after visually reading every differing blind crop on scan 059."""
import json
from pathlib import Path
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan059'
p=B/'pages'/f'{page}.tex';rp=B/'reviews'/f'{page}.json';r=json.loads(rp.read_text());assert not r.get('audit')
t=p.read_text()
glyph=r'\unsure{U|\deleted{K}|\deleted{U}}'
oldsymbol=r'\deleted{$\unsure{\widetilde U_i^{a}|\widetilde U_i}$}'
symbol=r'\deleted{$\unsure{\bar U_i^{a}|\widetilde U_i^{a}|\bar U_i^{\alpha}|\widetilde U_i}$}'
for a,b in [(r'\unsure{U|\deleted{K}}',glyph),(oldsymbol,symbol),(r'\uline{Conjecture B}',r'\uline{Conjecture} \uline{B}'),(r"et $=$ l'action",r"et $\unsure{=|\overline m}$ l'action"),('finie i.e.','finie ie.'),('scindages distinctes)',r'scindages distinct\unsure{es|s})')]:
 assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
p.write_text(t)
c={x['id']:x for x in r['changes']}
c['P02a'].update(final=glyph,evidence='Two heavy upright strokes join in a lower U-shaped cup. Thin diagonal strokes also cross the interior and meet the upper-right and lower-right parts. These support both letter and cancellation alternatives, including a cancelled U; the ink does not settle the sequence of rewriting.',confidence='low')
c['P08a'].update(final=symbol,evidence='The cancelled group retains an almost horizontal upper stroke, a heavily crossed U-shaped body, a low dotted i-like index and a small upper-right loop with a right return. The bar is the leading reading of the upper stroke, with tilde still open under the crossing; the small upper mark admits a/alpha and its relation to the cancellation remains uncertain. The live barred U_i lies outside the hatching.',confidence='low')
c['P10'].update(final=r'\uline{Conjecture} \uline{B}',evidence='A long underline ends after Conjecture. A visible gap precedes the independent shorter underline beneath B. Both readings underline exactly these two written units; separate wrappers now preserve the pen gap. No point follows B.')
c['P12a'].update(final=r'\unsure{=|\overline m}',against_C=False,confidence='medium',evidence='The sign has a detached upper bar and a lower stroke with a distinct left cup, shallow central rise and long right return. The recurring two-level shorthand permits both equals and a compressed barred letter; the local crop leaves that glyph reading open. M1160 is reopened without expanding the shorthand.')
c['P18']=dict(id='P18',place='line 18, abbreviation before the fixed-point formula',C='i.e.',H='i.e.',final='ie.',evidence='The initial i has a dark short stem, an upper dot and a hooked lower return. An open low e follows, then one distinct baseline point. No separate baseline point is visible between i and e.',crop='crops/149_scan059_B18_second.png',box=[337,1967,1013,2106],confidence='medium',against_C=True,against_H=True,kind='abbreviation expanded or spelling modernised',error_category='Abbreviations expanded, spelling modernised',marked_in_H=False,consequential=False)
r['changes'].append(c['P18'])
for d in r['decisions']:
 if d['id']=='M1160':d.update(decision='undecided',reading=c['P12a']['final'],evidence=c['P12a']['evidence'],crop='crops/149_scan059_B16_second.png (21,1595,325,2093)',confidence='medium')
for d in r['doubts']:
 if 'before -autom' in d['place']:d.update(reading=glyph,alternatives=r'U|\deleted{K}|\deleted{U}',reason=c['P02a']['evidence'])
 if 'cancelled indexed' in d['place']:d.update(reading=symbol,alternatives=r'\bar U_i^{a}|\widetilde U_i^{a}|\bar U_i^{\alpha}|\widetilde U_i',reason=c['P08a']['evidence'])
end_evidence='The final word has the d ascender, dotted i, s/t strokes and low joined ending after the last tall t. The short ending is close to the scan edge and its e body cannot be separated securely from the s return. The written primary es is retained with s as an alternative; grammatical agreement supplies neither reading.'
r['doubts'].extend([dict(place='margin note, after et',reading=c['P12a']['final'],alternatives=r'=|\overline m',reason=c['P12a']['evidence'],confidence='medium'),dict(place='last line, distinctes ending',reading=r'distinct\unsure{es|s}',alternatives='es|s',reason=end_evidence,confidence='medium')])
for x in r['inventory']:
 if x['element']=='E04':x['first_words_or_objects']='$'+glyph+'$-autom'
 if x['element']=='E06':x['first_words_or_objects']=symbol
 if x['element']=='E08':x['first_words_or_objects']=r'\uline{Conjecture} \uline{B} Toute telle action'
 if x['element']=='E10':x['first_words_or_objects']=x['first_words_or_objects'].replace('$=$',r'$\unsure{=|\overline m}$')
r['deletion_insertion_review'][1]=c['P08a']['evidence'];r['deletion_insertion_review'][2]=c['P02a']['evidence']
for n in r['notation']:
 if n['form']=='=':n.update(form=r'\unsure{=|\overline m}',meaning='Two-level prose shorthand with a cupped lower entrance; the glyph remains unresolved and unexpanded.')
for h in r['hand']:
 if h['form']=='prose equals sign':h.update(form='two-level prose shorthand',observation=c['P12a']['evidence'],scope='this occurrence remains uncertain after the blind crop comparison',witness_errors='C retains the equals/barred-m alternatives; H omits the sign.')
for a in r['abbreviations']:
 if a['written']=='i.e.':a['written']='ie.'
r['notes']=[n for n in r['notes'] if not n.startswith('Root accepted the remaining')]
r['notes']=[n.replace('The equals sign is retained literally.','The two-level sign remains unresolved between equals and barred m, without expansion.') for n in r['notes']]
r['notes'].append('Independent audit: six box readings were changed or marked uncertain. The heading is encoded with two underline segments; ie. has only its visible final stop. The cancelled symbol, crossed U/K source state, marginal shorthand and final distinctes ending remain explicitly qualified. Source mathematical claims remain attributed to the manuscript.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(n,decision,evidence):D[n]=dict(keep_first=True,changed=False,decision=decision,evidence=evidence)
def change(n,final,decision,evidence):D[n]=dict(final=final,changed=True,decision=decision,evidence=evidence)
keep('B02','Retain the opening fragment prète','A long p descender precedes the compressed r/e run and a detached accent. A separate tall t stroke and low final e return follow. The tall final stroke and accented middle favor prète; no preceding syllable is supplied.')
keep('B03','Retain the doubtful first inserted word and separate avec','The small first group is crossed by a descender from the baseline above. Its p-like descent and later tall strokes remain crowded. A distinct right group has the low a/v/e/c sequence. The whole automorphismes reading does not account as well for this separated final group; compatibles remains explicitly uncertain and the attachment uncertainty is preserved.')
change('B04','$'+glyph+'$-autom','Broaden the crossed glyph source-state alternatives',c['P02a']['evidence']+' After the hyphen a low a/u run, tall t and o/m ending support autom; no tall d with its own oval supports endom.')
keep('B06','Retain évident, the NB parenthesis, and s\'identifie','The first word has an accent, v, dotted i and tall d. The next group has an opening curve followed by two capital-height strokes and its separate underline. After barred K there is a curved s, a high apostrophe and dotted i before the d; these retain NB and s\'identifie.')
keep('B08','Retain three points and the edge closing curve','Three separate dark points follow naturelle. A much paler descending curve lies at the extreme right edge and curls left below the baseline; it remains the closing parenthesis at medium confidence. No further point is supplied.')
keep('B09','Retain et at the crop edge','The tilde, U and following comma are clear. At the right edge the low looped e joins a tall t whose right return is clipped; the two letters support the retained et.')
keep('B10','Retain simple-discrète with its accent doubt','The first group has s, dotted i, a compressed minim run, a long p descender, tall l and low e return before the hyphen. The second has d with oval/ascender, dotted i, s and c/r forms, ending in a tall crossed t and low return. Only the accent remains insecure.')
change('B11',symbol+r' $\bar U_i$','Broaden the cancelled whole-symbol reading',c['P08a']['evidence'])
keep('B12','Retain finis and the decorated-U sequence','The opening letter has a tall loop and descending stroke of f, followed by the compressed i/n/i/s run. After entre the first U has a curved short upper stroke; the last U has a straight bar. Three points, a closing curve and a final stop remain visible.')
change('B13',c['P10']['final'],'Preserve the gap between the two underline strokes',c['P10']['evidence'])
keep('B15','Retain the single margin rule','The rotated crop contains one long continuous ruled stroke with small deviations and a thick terminal ink deposit. The dark end remains attached to the same stroke. Both encodings map their single path to this rule; the second adds a separate filled circle that the ink does not establish as an independent point.')
change('B16',r"\margin{et $\unsure{=|\overline m}$ l'action induite de $\Gamma^\circ$ doit avoir un pt fixe et un seul --- cf plus bas.}",'Reopen the shorthand while retaining the circular superscript',c['P12a']['evidence']+' The Gamma modifier is a small open circular loop at the top-right; circ retains its shape. Six physical lines have the same word sequence, one dash and a final point; newline tokens only encode those wraps.')
change('B18',r'ie. $\widetilde x\in\widetilde U^\Gamma$, alors 1°)','Remove the unsupported internal abbreviation point',c['P18']['evidence']+' The tilde-x, membership sign, tilde-U with raised Gamma, comma and written 1 with small circle and closing parenthesis remain unchanged; math wrappers account for the remaining token differences.')
keep('B19','Retain the same section citation','The source has th, a detached point, numeral 3, du, the double-curved section sign and numeral 1. The S macro and literal section glyph refer to that same sign; spacing introduces no written unit.')
change('B20',r'scindages distinct\unsure{es|s}) et','Mark the final ending uncertain',end_evidence)
main(dict(page=page,root_viewed=[f'crops/{page}_{n}_second.png' for n in D],decisions=D));record(page);assign('reader_c')
