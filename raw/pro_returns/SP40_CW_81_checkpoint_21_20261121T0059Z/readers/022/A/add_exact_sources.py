from pathlib import Path
import json,hashlib
OUT=Path('/workspace/scratch/94548b74fbe0/out/readers/022/A')
ROOT=Path('/workspace/scratch/94548b74fbe0')
r=json.loads((OUT/'report.json').read_text())
h=(ROOT/'packets/022/H.tex').read_text().splitlines()
c=(ROOT/'packets/022/C.tex').read_text().splitlines()
def excerpt(a,start,end):return '\n'.join(a[start-1:end])
hmap={
'D01':(2,2),'D02':(2,2),'D03':(2,3),'D04':(4,5),'D05':(5,5),'D06':(5,5),'D07':(5,5),'D08':(6,8),'D09':(9,20),'D10':(19,20),'D11':(19,20),'D12':(13,20),'D13':(13,20),'D14':(13,14),'D15':(27,30),'D16':(27,30),'D17':(27,30),'D18':(32,34),'D19':(35,36),'D20':(39,39),'D21':(40,41),'D22':(40,40),'D23':(40,40),'D24':(46,46),'D25':(42,46),'D26':(45,45),'D27':(43,43),'D28':(43,43),'D29':(48,48),'D30':(44,46),'D31':(58,58),
'GD01':(3,4),'GD02':(4,5),'GD03':(13,13),'GD04':(14,14),'GD05':(28,28),'GD06':(29,30),'GD07':(32,34),'GD08':(37,37),'GD09':(42,42),'GD10':(42,42),'GD11':(51,51),
'MD01':(22,22),'MD02':(32,34),'MD03':(48,48),'MD04':(48,48),'MD05':(51,51),'MD06':(51,51)}
cmap={
'D01':(2,2),'D02':(2,2),'D03':(2,2),'D04':(2,2),'D05':(2,2),'D06':(2,2),'D07':(2,2),'D08':(2,2),'D09':(4,11),'D10':(6,6),'D11':(6,6),'D12':(6,6),'D13':(6,6),'D14':(7,7),'D15':(17,18),'D16':(18,18),'D17':(18,18),'D18':(22,22),'D19':(24,24),'D20':(26,28),'D21':(28,28),'D22':(28,28),'D23':(28,28),'D24':(28,28),'D25':(30,30),'D26':(30,30),'D27':(32,32),'D28':(32,32),'D29':(34,34),'D30':(22,32),'D31':(42,42),
'GD01':(2,2),'GD02':(2,2),'GD03':(6,6),'GD04':(7,7),'GD05':(17,17),'GD06':(18,18),'GD07':(22,22),'GD08':(26,26),'GD09':(30,30),'GD10':(30,30),'GD11':(36,36),
'MD01':(13,13),'MD02':(22,22),'MD03':(34,34),'MD04':(34,34),'MD05':(36,36),'MD06':(36,36)}
for row in r['differences']:
 key=row['id'].removeprefix('A022-')
 hs,he=hmap[key];cs,ce=cmap[key]
 row.setdefault('H_reading_summary',row['H'])
 row['H']=excerpt(h,hs,he)
 row['H_source_exact']=row['H']
 row['H_source_lines']=[hs,he]
 row['C_source_exact']=excerpt(c,cs,ce)
 row['C_source_lines']=[cs,ce]
 row['local_H_marker_scope_note']='Only the actual local marker scope controls marked_in_H; a nearby ill marker in this broader exact excerpt does not qualify another word.'
# Actual local H scopes are literal, with the physical line wrap retained where present.
hm=r['H_local_marker_audit']
hm['actual_local_markers'][0]['exact_scope']=excerpt(h,39,39)
hm['actual_local_markers'][1]['exact_scope']=excerpt(h,40,41)
hm['actual_local_markers'][1]['local_substring']=r'Or \ill{} par construction'
hm['source_file_sha256']=hashlib.sha256((ROOT/'packets/022/H.tex').read_bytes()).hexdigest()
# Preserve table-mentioned contextual recurrences separately from the seven source-row identities.
mp={v['id']:v for v in r['C_doubt_source_map']}
mp['C022-R01']['local_parts'] += [
{'part':'initial si opening parenthesis, table contextual argument','status':'confirmed context, not additional source doubt','selected':'(','bbox':[880,175,906,233],'crop':'crops/03_initial_formula.png'},
{'part':'final outer closing parenthesis, table contextual argument','status':'confirmed context, not additional source doubt','selected':')','bbox':[1645,260,1671,301],'crop':'crops/02_parenthetical_end.png'}]
mp['C022-R03']['local_parts'].append({'part':'replacement immediately to the right, source contextual preference','status':'independently confirmed context, not additional source doubt','selected':r'\ne\varnothing','bbox':[936,397,1020,477],'crop':'crops/04_first_brace.png'})
mp['C022-R04']['local_parts'].append({'part':'left vertical equals named in source evidence','status':'independently confirmed context, not additional source doubt','selected':'two vertical equality ticks','bbox':[686,748,708,773],'crop':'crops/05_main_equality.png'})
mp['C022-R05']['local_parts'].append({'part':'following peut named in source contextual preference','status':'independently read context, not additional source doubt','selected':'peut','bbox':[942,1343,1059,1391],'crop':'crops/09_or_and_noun.png','difference_id':'A022-D22'})
mp['C022-R07']['local_parts'] += [
{'part':'later live Y named in source contextual evidence','status':'independently confirmed context, not additional source doubt','selected':'Y','bbox':[636,1973,684,2029],'crop':'crops/13_YZ.png'},
{'part':'later live Z named in source contextual evidence','status':'independently confirmed context, not additional source doubt','selected':'Z','bbox':[903,1968,970,2018],'crop':'crops/13_YZ.png'}]
# All source rows receive original packet line identity, including literal context cells.
rows=(ROOT/'packets/022/C_doubts.txt').read_text().splitlines()
source_rows=[(idx+1,line) for idx,line in enumerate(rows) if line.startswith('| 22 |')][-7:]
for obj,(num,line) in zip(r['C_doubt_source_map'],source_rows):
 obj['source_packet_line']=num;obj['complete_source_row_literal']=line
# Exact source inputs used in this independent reading only.
paths=['out/briefs/brief_v20_scan022.md','out/PREAMBLE.tex','packets/022/C.tex','packets/022/H.tex','packets/022/metadata.json','packets/022/C_doubts.txt','packets/022/C_notes.txt','packets/022/C_inventory.json','packets/022/S_rows.json','packets/022/notation.md','source/SP40_CW_81_scans/J81-03_81_scan022.jpg','source/SP40_CW_81_scans/J81-03_81_scan022_a.jpg','source/SP40_CW_81_scans/J81-03_81_scan022_b.jpg']
inputs=[]
for path in paths:
 b=(ROOT/path).read_bytes();inputs.append({'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
r['provenance']['exact_input_manifest_file']='input_audit.json'
r['provenance']['H_source_field_policy']='Each H field is a literal packet excerpt with exact line bounds; the prior concise integrated reading is preserved in H_reading_summary. Local uncertainty flags apply only to their exact marked locus.'
r['provenance']['C_source_field_policy']='Each difference includes a complete literal C source excerpt and source line bounds, alongside the local reading summary.'
r['structural_validation_file']='structural_validation.json'
(OUT/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
(OUT/'H_marker_audit.json').write_text(json.dumps(hm,ensure_ascii=False,indent=2)+'\n')
(OUT/'C_doubt_map.json').write_text(json.dumps(r['C_doubt_source_map'],ensure_ascii=False,indent=2)+'\n')
(OUT/'input_audit.json').write_text(json.dumps(inputs,ensure_ascii=False,indent=2)+'\n')
print('Added exact literal C/H excerpts to all',len(r['differences']),'difference rows; original C rows and all named contextual recurrences mapped.')
