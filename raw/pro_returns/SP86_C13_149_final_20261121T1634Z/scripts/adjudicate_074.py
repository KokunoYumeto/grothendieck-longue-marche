"""Root decisions after viewing every differing fixed blind crop of scan 074."""
from pathlib import Path
import json
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan074';rp=B/'reviews'/f'{page}.json'
r=json.loads(rp.read_text());assert not r.get('audit');p=B/'pages'/f'{page}.tex';t=p.read_text()
oldmargin=r'* anabélien est inutile -- il suffit que les fibres de dim 1 des ``fibrations élémentaires\'\' de $U$ ne soient pas des \unsure{typ|types} $(0,0)$ ou $(0,1)$ -- i.e. à $\pi_1$ nul'
oldmargin=oldmargin.replace("\\'", "'")
margin=r'''* anabélien est inutile -- il suffit que les fibres de dim 1 de la ``fibration élémentaire'' de $U$ ne soient pas du \unsure{type|typ} $(0,0)$ ou $(0,1)$ -- i.e. à $\pi_1$ nul'''
repls=[(r'\deleted{Considérons une}',r'\deleted{Considérons \unsure{une}}'),(r'\deleted{section pt',r'\deleted{\unsure{section} pt'),('un carré cartésien',r'un carr\unsure{é|e} cartésien'),('sous-groupe nor.','sous-groupe '+r'\unsure{nor.|plus}'),(oldmargin,margin)]
for a,b in repls:
 assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
p.write_text(t)
evune='The baseline strike runs through the short group following Considérons; the upper joins of u/n and the small terminal e are merged with its dark stroke. Retain une tentatively. The separate higher On a donc has an open O, low n, detached a and d/o/n/c bodies, with no strike across that raised row.'
evsec='The old baseline begins with an S-like curve and a compressed e/c/t/i/o/n run under the cancellation; the inner joins are obscured, so section remains tentative. The following pt, K-rationnel de U_K and the separate low comma are retained, with the comma still uncertain in cancellation scope. Above this baseline sit un, carr followed by a low e-like body, cartésien, de groupes profinis. No independent accent over that first e can be separated confidently, so carré/carre remains open. The entire upper phrase is visibly interlinear and remains an insertion.'
evnor='The short group has an initial dark upright, a second high curved entry, a long compressed low middle and a hooked right end, followed by a separate dark curved mark. These strokes support the first nor. reading but leave the blind plus reading admissible where the middle bodies and final mark merge. Neither crop supplies a separable mal ending for H’s normal. Preserve the written-short-form alternatives without expansion.'
evmargin='The rotated crop reads de la after dim 1: a tall l loop follows the small de and ends in a compact a body, rather than a terminal s. The quoted next row has f/i/b/r/a/t/i/o/n and élémentaire, each ending without a separate s turn before the gap or closing quotation ticks. Below de U ne soient pas, the article has a d bowl and low u return, supporting du. The next word has t/y/p with a long p descender and a small low rightward return admitting e; type/typ remains open without an added stop. The initial dim has a d bowl/ascender and compressed i/m strokes. The star, anabélien est, inutile, dash, il suffit, que les fibres de, both numeral pairs, ou, and final dash i.e. à pi_1 nul were read throughout the same crop.'
c={x['id']:x for x in r['changes']}
c['P13'].update(final=c['P13']['final'].replace(r'\deleted{section pt',r'\deleted{\unsure{section} pt').replace('un carré cartésien',r'un carr\unsure{é|e} cartésien'),evidence=evsec)
c['P16'].update(final=r'\unsure{nor.|plus}',evidence=evnor,confidence='medium')
c['P17'].update(final=margin,evidence=evmargin,confidence='medium')
for x in r['doubts']:
 if x['place'].startswith('P17,'):x.update(reading=r'\unsure{type|typ}',alternatives='type; typ',reason=evmargin)
for place,reading,alts,ev in [('P12, canceled word after Considérons',r'\deleted{\unsure{une}}','tentative une',evune),('P13, beginning of canceled clause',r'\deleted{\unsure{section}}','tentative section',evsec),('P13, raised carré/carre',r'carr\unsure{é|e}','carré; carre',evsec),('P16, compressed short form after sous-groupe',r'\unsure{nor.|plus}','nor.; plus',evnor)]:
 r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='medium',reason=ev))
for x in r['inventory']:
 for a,b in repls:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,b)
for x in r['abbreviations']:
 if x['written']=='nor.':x.update(written=r'\unsure{nor.|plus}',expansion='normal is a proposed expansion of nor. only; the written alternative plus remains explicit')
 if x['written']==r'\unsure{typ|types}':x.update(written=r'\unsure{type|typ}',expansion='type; the final e remains unresolved, so no expansion is supplied in the transcription')
for x in r['hand']:
 if x['form']=='nor. and compressed typ/types':x.update(form='compressed nor./plus and type/typ',observation=evnor+' '+evmargin,witness_errors='H expands the main short form to normal. C pluralizes the marginal fibration élémentaire and gives des before the type word; the local singular forms and du are retained from the rotated crop.')
 if x['form']=='paired quotation ticks and foliation':x['observation']=x['observation'].replace('fibrations élémentaires','fibration élémentaire')
 if x['form']=='cancellation and raised replacement':x['observation']=evune+' '+evsec;x['witness_errors']='H’s upper une suite extension does not match the surviving un carr… cartésien bodies. Three local letter/accent doubts are retained beneath or above the old clause.'
r['notes'][3]='Source revision: Considérons followed by tentative une and section (tentative) pt K-rationnel de U_K are canceled. The higher replacements are On a donc and un carré/carre cartésien de groupes profinis, with the first accent locally doubtful. Underlined d’où precedes the four-arrow diagram. The manuscript calls this a carré cartésien; its mathematical property was not checked.'
r['notes'][4]='Source marginal qualification: the starred note begins anabélien est inutile, continues il suffit que les fibres de dim 1 de la quoted fibration élémentaire de U ne soient pas du, then type/typ and the pairs (0,0), (0,1). It ends -- i.e. à pi_1 nul. Singular wording follows the rotated independent-audit crop. This records the author’s qualification.'
r['notes'][8]='Material C departures are the recovered overlaid S/T extent, restored marginal quotation ticks, and the singular marginal wording de la fibration élémentaire and du. The added letter, accent and cancellation-state doubts, including nor./plus and type/typ, contribute no separate material C count. Both supplied MARKS remain undecided.'
r['notes'].append('The root viewed all twelve differing independent-audit crops. The fixed first and second readings remain unchanged in second/. The audit qualifies canceled une and section, the raised carré accent, and the compressed nor./plus form, and corrects the singular marginal wording. No mathematical check was added.')
r['deletion_insertion_review'][3]=evune
r['deletion_insertion_review'][4]=evsec
r['open_issues']=['Nine local doubts remain in the doubt table: canceled numeral, following question group, S/T overwrite order, old comma state, type/typ ending, canceled une, canceled section, raised é/e, and nor./plus.']
for x in r['diff_coverage']:
 if x['row']==17:x['reason']='Both witnesses place une in the old canceled clause; its letter bodies remain tentative beneath the strike after the blind audit. No second word is added.'
 if x['row']==19:x['reason']='The raised replacement reads un carré/carre cartésien de groupes profinis, with a locally uncertain accent. The old section letters and comma state remain explicit doubts.'
 if x['row']==25:x['reason']='The compressed group is retained as nor./plus; no mal ending establishes H’s expanded normal.'
 if x['row']==27:x['reason']='The rotated audit crop supports de dim 1 de la, quoted fibration élémentaire, and du before type/typ. The singular forms replace the first-pass plurals; H’s editorial diagram note is not source text.'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(b,title,e):D[b]=dict(keep_first=True,changed=False,decision=title,evidence=e)
keep('B02','Retain eta from the arched nested index','The index under U has a short left upright continuous with a curved arch and a lower hooked right return. The adjoining E_K has an independent tall stem and angular K branches. The blind η/n alternative maps its n candidate to this same arched small body; retain eta from the recorded recurring form. E and mathcal E encode the same two-lobed source glyph at each of these coordinates.')
keep('B06','Retain the canceled numeral candidates and question group','Several cancellation hatches cross the numeral, but a lower curved bowl and bent upper entry remain compatible with 2/3. They support explicit candidates rather than a wholly unreadable count. The following question hook and dot and the right parenthesis are distinct; the possible left parenthesis merges with the canceled cluster. The title’s point and lower underline remain visible.')
keep('B07','Retain both recoverable overwrite orders','The group contains the broad upper/lower curves of S and a T crossbar with central stem. Omitting the overwritten layer would lose those recovered strokes. Their intersections do not establish order, so both deleted-S/T and deleted-T/S sequences remain open.')
keep('B10','Retain the complete formula with coordinate-matched alphabets','Each E/mathcal E pair refers to the same two-lobed glyph, U/mathcal U to the same open-topped cup. The low 1 indices, first semicolon, tilde, second comma, bar on K, similarity sign and parenthesized Gal expression occupy identical positions in both encodings; the full formula is preserved.')
keep('B11','Retain the full excerpt including par','The pi stems, equality, low 1, nested barred K, comma and tilde over the final U match. The first excerpt includes the baseline par to the left and the concluding point; the blind excerpt selects the mathematical expression only. The p descender and low following bodies are visible at the crop’s left edge.')
D['B12']=dict(final=r'\deleted{Considérons \unsure{une}} \inserted{On a donc}',changed=True,decision='Qualify the canceled une',evidence=evune)
D['B13']=dict(final=c['P13']['final'],changed=True,decision='Qualify canceled letters and the raised accent',evidence=evsec)
keep('B14','Retain the lower stroke as an underline','The independent long stroke starts at the lower edge of the d bowl and runs beneath the d/o bodies toward the low terminal u return. It does not traverse the tall d ascender or apostrophe; its rise at the right touches the low last body. That path supports the existing underlining, with the word live.')
keep('B15','Retain the four objects, four arrows and their labels','The top-right nested index has a curved arch with a low right return matching B02. The lower-right index has a distinct left stem and angular junction into the right branch, matching K in the following Gal expression. The two horizontal shafts point left and the two vertical shafts point down, each with one head and a surj label. The labels retain their physical side of the shaft. Each E/mathcal E and U/mathcal U wrapper pair maps to the same glyph at the same node. The overlapping lower equality/G baseline does not supply a separately traceable cancellation of the full formula.')
D['B16']=dict(final=r'\unsure{nor.|plus}',changed=True,decision='Keep the compressed short form open',evidence=evnor)
D['B17']=dict(final=r'\margin{'+margin+'}',changed=True,decision='Restore singular marginal wording and retain the ending doubt',evidence=evmargin)
keep('B19','Retain the same attached asterisk and comma','The word ends in the low e/n run; the star stands above/right of it and the separate comma curves down below. Both encodings attach that single star to anabélien and retain the following comma. The superscript wrapper changes the encoding of the same marginal anchor, without adding a second source mark.')
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D));record(page);assign('reader_a')
