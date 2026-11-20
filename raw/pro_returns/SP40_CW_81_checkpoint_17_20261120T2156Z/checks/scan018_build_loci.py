#!/usr/bin/env python3
"""Consolidate exact released source proposals; root ink choices remain pending."""
from pathlib import Path
import hashlib
import json
import copy

BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/checks'
U=json.loads((OUT/'scan018_source_union.json').read_text())
R=json.loads((OUT/'scan018_record_draft.json').read_text())
assert U['released_readers']==['A','B','C']
READERS=U['reader_sources']
BY={r:{x['value']['id']:x for x in READERS[r]['raw_rows']['differences']} for r in 'ABC'}
GROUPS={r:{x['id']:x['source'] for x in READERS[r]['complete_graphical_groups']} for r in 'ABC'}
TEX={r:READERS[r]['complete_tex']['excerpt'] for r in 'ABC'}

def sha(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()
def save(p,x): (OUT/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def exact(r,literal):
    text=TEX[r]
    assert text.count(literal)==1,(r,literal,text.count(literal))
    a=text.index(literal);b=a+len(literal)
    return dict(manifest=f'out/readers/018/{r}/reading.tex',char_start=a,char_end=b,
        offset_convention='zero-based Unicode code points; end exclusive',
        line_start=text.count('\n',0,a)+1,line_end=text.count('\n',0,b-1)+1,
        excerpt=literal,literal_sha256_utf8=sha(literal),scope='Complete supplied local source span; no ink finding inferred from textual absence.')
def group(r,name):
    s=copy.deepcopy(GROUPS[r][name]);s['group_id']=name
    s['scope']='Complete exact graphical group, including its nodes, wrappers, local origins and literal paths.'
    return s
def ending(r):
    text=TEX[r];a=text.index(r'\deleted{\unsure{cela|OK}}') if r=='A' else text.index(r'\deleted{\unsure{OK|cela|et}}') if r=='B' else text.index(r'\deleted{\unsure{OK|cela}}')
    return exact(r,text[a:])

# Each row retains the original raw IDs. Duplicate raw IDs at component rows are
# explicit scope references, never duplicate physical change counts.
SPECS=[
 (1,'opening dernière','A01','B01','D01','C018-R01-1'),
 (2,'parenthetical récurrence / rècurrence','A02','B02','D02','C018-R02-1'),
 (3,'ens and its abbreviation endpoint','A03','B03','D03 P01','C018-R03-1'),
 (4,'de/des following inserted unique','A04','B04','D04','C018-R04-1'),
 (5,'ces n before classes','A05','B05','P02',None),
 (6,'unique insertion guide and adjoining words','A06','B06','G01',None),
 (44,'upper quoted composante/composant ending','','B07','',None),
 (7,'considérons','A07','B08','D05','C018-R05-1'),
 (8,'lemma Pi upper ring','A08','B10','D06b','C018-R06-2'),
 (9,'lemma mark after J: glyph and state','A09','B09','D06a','C018-R06-1'),
 (10,'lemma underline and separate left rule','A10','B11','G02',None),
 (11,'lemma endpoint punctuation','A11','B12','P03',None),
 (12,'proof-opening Dire','A12','B13','D07','C018-R07-1'),
 (13,'qu’une guide and cancelled la paths','A13','B14','G03',None),
 (14,'inserted U subscript','A14','B15','D08a','C018-R08-1'),
 (15,'inserted Pi ring recurrence','A15','B16','N01',None),
 (16,'raised U/Pi insertion guide','A16','B18','G04',None),
 (17,'hook after inserted U: punctuation/guide attachment','A17','B17','M01',None),
 (18,'H additional struck un','A18','B19','R01',None),
 (19,'first corrected E_i predecessor','A19','B20','D09a','C018-R09-1'),
 (20,'first corrected E_i upper rule and role','A20','B21','D14','C018-R14-1'),
 (21,'que il','A21','B22','R02',None),
 (22,'le before Sigma_j','A22','B23','R03',None),
 (23,'second corrected E predecessor','A23','B24','D09b','C018-R09-2'),
 (24,'second corrected E index','A24','B25','D09c','C018-R09-3'),
 (25,'cancelled choisi/choisie ending','A25','B26','D10','C018-R10-1'),
 (26,'literal cancellation across choisi/choisie','A26','','G05',None),
 (27,'two detached points beside cancelled choisi','A26','B27','M02',None),
 (28,'lower quoted composant/composante','A27','B28','D11','C018-R11-1'),
 (29,'live est after cancelled est','A28','B29','R04',None),
 (30,'first accent of l’élément','','B30','A01',None),
 (31,'second accent of l’élément','','B30','A02',None),
 (32,'du before pi_0','A29','B31','R05',None),
 (33,'first accent of lower éléments','','','A03',None),
 (34,'soit Sigma insertion guide','A30','B32','G06',None),
 (35,'cancelled deux under card I=2','A31','B33','D12','C018-R12-1'),
 (36,'raised card I=2 and cancellation path','A32','B34','D12 G07',None),
 (37,'lower hook in card I=2 correction','','','G07',None),
 (38,'cancelled word before fortiori','A33','B35','D13a','C018-R13-1'),
 (39,'accent on a before fortiori','A34','B36','D13b','C018-R13-2'),
 (40,'final U subscript recurrence','','B37','D08b',None),
 (41,'final OK live/cancelled state','A35','B38','',None),
 (42,'final OK transverse path','A36','B38','',None),
 (43,'faint right-edge spot','A37','','',None),
]

def local_tex(n,r):
    if n in [4,5,6]:return group(r,'G01')
    if n in [8,9,10,11]:return group(r,'G02')
    if n==13:return group(r,'G03')
    if n in [14,15,16,17,18]:return group(r,'G03' if r=='B' else 'G04')
    if n==20 and r=='B':return group(r,'G04')
    if n in [25,26,27]:return group(r,'G05')
    if n in [33,34]:return group(r,'G06')
    if n in [35,36,37]:return group(r,'G07')
    if n in [38,39,40,41,42,43]:return ending(r)
    literals={
       1:'cette dernière, si',
       2:{'A':r'(par \unsure{récurrence})','B':r'(par \unsure{rècurrence|récurrence})','C':r'(par r\unsure{è|é}currence)'},
       3:"le cardinal de l'ens des classes est",
       7:'et considérons les deux composantes',
       12:"C'est presque une tautologie : Dire",
       19:{'A':r'contient pas $\deleted{\Sigma}\overline{E_i}$ i.e. est','B':r'pas $\deleted{\Sigma}$','C':r'contient pas $\deleted{\Sigma}\overline{E_i}$ i.e. est'},
       20:{'A':r'contient pas $\deleted{\Sigma}\overline{E_i}$ i.e. est','C':r'contient pas $\deleted{\Sigma}\overline{E_i}$ i.e. est'},
       21:'signifie que il existe un',22:r'tel que le $\Sigma_j^+',
       23:{'A':r'\pi_0(X\setminus\deleted{\Sigma}E_{\unsure{j|J}})','B':r'\pi_0(X\setminus\deleted{\Sigma}E_{\unsure{j|J}})','C':r'\pi_0(X\setminus\deleted{\Sigma}E_j)'},
       24:{'A':r'\pi_0(X\setminus\deleted{\Sigma}E_{\unsure{j|J}})','B':r'\pi_0(X\setminus\deleted{\Sigma}E_{\unsure{j|J}})','C':r'\pi_0(X\setminus\deleted{\Sigma}E_j)'},
       28:{'A':"``composant'' de cette classe",'B':r"``\unsure{composant|composante}'' de cette classe",'C':"``composant'' de cette classe"},
       29:r"de cette classe \deleted{est} est",
       30:{'A':"l'élément du",'B':r"l'\unsure{élêment|élément} du",'C':r"l'\unsure{é|e}l\unsure{é|ê}ment du"},
       31:{'A':"l'élément du",'B':r"l'\unsure{élêment|élément} du",'C':r"l'\unsure{é|e}l\unsure{é|ê}ment du"},
       32:{'A':"l'élément du",'B':r"l'\unsure{élêment|élément} du",'C':r"l'\unsure{é|e}l\unsure{é|ê}ment du"},
       44:{'A':"(ou ``composante'')",'B':r"(ou ``\unsure{composante|composant}'')",'C':"(ou ``composante'')"},
    }
    lit=literals[n];return exact(r,lit[r] if isinstance(lit,dict) else lit)

decisions=[];raw_to_loci={r:{} for r in 'ABC'}
for n,location,a,b,c,part in SPECS:
    lid=f'L018-{n:02d}'
    ids={r:s.split() for r,s in zip('ABC',[a,b,c])}
    proposals={r:[copy.deepcopy(BY[r][i]['value']) for i in ids[r]] for r in 'ABC'}
    report_only={r:[x['reading'] for x in proposals[r]] for r in 'ABC'}
    tex_sources={r:local_tex(n,r) for r in 'ABC'}
    readers={r:(report_only[r] or ['Exact TeX excerpt: '+tex_sources[r]['excerpt']]) for r in 'ABC'}
    for r in 'ABC':
        for source_id in ids[r]:raw_to_loci[r].setdefault(source_id,[]).append(lid)
    first=next(x for r in 'ABC' for x in proposals[r])
    d=dict(id=lid,location=location,C=first.get('C'),H=first.get('H'),final=None,
        readers=readers,readers_report_only=report_only,reader_proposals=proposals,
        reader_provenance={r:[BY[r][i]['source'] for i in ids[r]]+[tex_sources[r]] for r in 'ABC'},
        reader_report_provenance={r:[BY[r][i]['source'] for i in ids[r]] for r in 'ABC'},
        reader_tex_sources=tex_sources,
        report_silent_readers=[r for r in 'ABC' if not ids[r]],
        reader_mapping_status='All A/B/C slots grounded in actual report reading or exact complete local TeX excerpt; report-only map preserved.',
        source_C_doubt_parts=[part] if part else [],source_C_doubt_rows=[part.rsplit('-',1)[0]] if part else [],
        C_doubt_status=None,kind=first['kind'],kind_status='provisional source kind; root choice pending',
        marked_in_H=False,marked_in_H_basis='Complete H source has no editorial uncertainty or ill placeholder at these page loci.',
        evidence=None,confidence=None,confidence_status='pending root',diff_C=None,diff_H=None,
        count_status='pending root; raw report flags are preserved separately',
        physical_count_parent=None,H_count_parent=None,main_approved=False,log_decision=True,
        final_source_attachment=[],root_ink_choice_applied=False)
    if n==20:d['source_scope_attention']='A/C resolve physical stroke presence while C018-R14 also asks bar versus earlier-stroke attachment; B preserves that role alternative. Original raw statuses remain separate from root outcome.'
    if n==40:d['source_scope_attention']='Additional final-U recurrence associated with R08 context. B retains alpha/x, C resolves final alpha, A notation records alpha. Canonical R08 has one primary part; this row does not expand the 18-part catalog.'
    if n==30:d['source_scope_attention']='B30 reports the whole word with first é in both candidates; its new uncertainty concerns the second accent. C:A01 independently qualifies first é/e. Preserve actual full-word source without transferring the second-accent doubt.'
    if n==43:d['source_scope_attention']='A reports the faint spot. B/C exact complete ending spans contain no corresponding separate spot path; this is source absence, with no claim that their crops inspected the entire A spot locus.'
    if n==26:d['source_scope_attention']='A26 also reports the detached points mapped at L018-27; C:G05 describes the already agreed cancellation. B G05 uses the ordinary deleted macro. Root supplies physical parent/count.'
    if n in [35,36,37]:d['source_scope_attention']='Bottom correction source context is shared. Keep deleted-word, raised-placement/cancellation and lower-hook local choices visible; one H correction parent is supplied by root.'
    if n in [41,42]:d['source_scope_attention']='Final-OK state and transverse path share a physical cluster; A35/A36 and B38 raw flags are preserved. Same live-primary qualification alone supplies no H count; literal path counting is root-owned.'
    decisions.append(d)

for r in 'ABC':
    assert set(raw_to_loci[r])==set(BY[r]),(r,set(BY[r])-set(raw_to_loci[r]))
candidate_doubts=[]
for r in 'ABC':
    for item in READERS[r]['raw_rows']['doubts']:
        row=item['value']
        ids=row.get('difference_ids') or ([row['id']] if 'id' in row else [])
        if not ids:
            ids=[i for i,d in BY[r].items() if d['value']['location']==row['location']]
        loci=sorted({l for i in ids for l in raw_to_loci[r].get(i,[])})
        if r=='A' and row['location']=='Detached pair after cancelled choisi/choisie':loci=['L018-27']
        if r=='B' and ids==['B30']:loci=['L018-31']
        if r=='C' and ids==['G07']:loci=['L018-37']
        assert loci,(r,row)
        candidate_doubts.append(dict(reader=r,source_difference_ids=ids,loci=loci,original=item,selected=None,main_approved=False))

U['consolidated_loci']=decisions
U['raw_difference_to_loci']=raw_to_loci
U['candidate_doubts']=candidate_doubts
save('scan018_source_union.json',U)
R.update(decisions=decisions,source_union_sha256=hashlib.sha256((OUT/'scan018_source_union.json').read_bytes()).hexdigest(),
    preliminary_locus_map='out/checks/scan018_locus_map.json',candidate_doubts=candidate_doubts,
    raw_difference_to_loci=raw_to_loci,source_attachment_status='All reader source attachments complete; selected draft attachments await root choices.',
    notes='Complete source-only preliminary A/B/C union. All 115 raw difference rows, 49 raw doubts, 99 source inventory rows, canonical 14 C rows/18 primary parts and original source maps are preserved. Root ink outcomes, physical counts, confidence and final statuses remain pending.',
    reader_notes={r:READERS[r]['extra_source_fields']['notes']['value'] for r in 'ABC'},
    reader_notation={r:[x['value'] for x in READERS[r]['raw_rows']['notation']] for r in 'ABC'},
    reader_raw_check_events={r:[x['value'] for x in READERS[r]['raw_rows']['check_events']] for r in 'ABC'})
R['doubts']=[dict(decision_id=d['id'],location=d['location'],reading=None,alternatives=[],confidence=None,
                   reason='Pending root selection; original local reader doubt rows and candidate order preserved in reader_components.',
                   reader_components=[x for x in candidate_doubts if d['id'] in x['loci']],
                   final_status='pending root',main_approved=False,final_source_attachment=[])
              for d in decisions if any(d['id'] in x['loci'] for x in candidate_doubts)]
save('scan018_record_draft.json',R)
brief=[]
for d in decisions:
    brief.append(dict(id=d['id'],location=d['location'],readers={r:[x['id'] for x in d['reader_proposals'][r]] for r in 'ABC'},
          report_silent_readers=d['report_silent_readers'],C_parts=d['source_C_doubt_parts'],
          scope_attention=d.get('source_scope_attention'),reader_tex_sources=d['reader_tex_sources'],
          main_approved=False))
save('scan018_locus_map.json',dict(scan=18,status='all root choices pending',loci=brief,
    source_union='out/checks/scan018_source_union.json',raw_difference_to_loci=raw_to_loci))
lines=['# Scan018 preliminary consolidated source loci','',
       'All root ink decisions, confidence, physical counts and final statuses remain pending. Each public reader slot has an actual report reading or an exact local TeX source; the original report-only maps are retained.','',
       '| Locus | Location | A raw IDs | B raw IDs | C raw IDs | Original C primary part |',
       '| --- | --- | --- | --- | --- | --- |']
for d in decisions:
    cols=[d['id'],d['location']]+[', '.join(x['id'] for x in d['reader_proposals'][r]) or 'exact TeX source' for r in 'ABC']+[', '.join(d['source_C_doubt_parts']) or '—']
    lines.append('| '+' | '.join(x.replace('|','\\|') for x in cols)+' |')
lines += ['', 'Raw coverage: A 37 differences / 15 doubts / 29 inventories; B 38 / 18 / 26; C 40 / 16 / 27; witness C 17 inventories. Canonical C remains 14 rows and 18 primary parts. The additional final-U recurrence is L018-40 with each reader’s actual local scope preserved.', '',
          'Physical context groups requiring root parent choices: L018-16/17; L018-19/20; L018-23/24; L018-25/26/27; L018-35/36/37; L018-41/42. Reader B’s broad proof-insertions parent remains raw provenance; the clerk assigns no physical parent.', '',
          'Complete source groups differ in adjacency: B G03 contains both insertion guides and classe donnée/ne contient; A G03/G04 and C G03/G04 have their own complete boundaries. C G06 includes the following pi formula; A/B G06 leave it outside. C G07 includes cas and leaves comma outside; A G07 includes comma; B G07 leaves cas and comma outside.']
(OUT/'scan018_locus_map.md').write_text('\n'.join(lines)+'\n')
F=json.loads((OUT/'scan018_source_fingerprints.json').read_text())
F['prepared_files'].update({p:dict(sha256=hashlib.sha256((OUT/p).read_bytes()).hexdigest()) for p in ['scan018_source_union.json','scan018_record_draft.json','scan018_locus_map.json','scan018_locus_map.md']})
F['record_stage']='complete preliminary source union; root choices pending'
save('scan018_source_fingerprints.json',F)
print(json.dumps(dict(loci=len(decisions),raw_difference_rows=sum(len(v) for v in BY.values()),
    raw_doubt_rows=len(candidate_doubts),source_inventory_rows=len(U['candidate_inventory']),
    all_public_reader_slots_complete=all(all(d['readers'][r] for r in 'ABC') for d in decisions),
    root_approval_flags=False)))
