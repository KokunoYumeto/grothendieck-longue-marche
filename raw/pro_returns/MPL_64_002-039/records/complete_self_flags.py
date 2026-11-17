from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
p=r/'records/apparatus_note_items.json';a=json.loads(p.read_text());d={x['id']:x for x in a}
d['C64-U02']['scans']='012, margin;013–014, orientation relation'
d['C64-U02']['quote']='Attention, cette relation serait inversée ... l’ordre des facteurs (012); Pour vérifier ... il faut expliciter d’abord les conventions (013); On vérifie qu’avec ces conventions (014)'
d['C64-U02']['body']='The margin on012 already warns that transposing the factor order reverses the relation and identifies a question of convention. Scan013 announces the verification and014 says that it works after fixing those conventions, so it is not left explicitly unchecked at the end of the argument. C64-N10 supplies a separate product-order check, agreeing with Hua’s §2 caveat about right versus left action conventions.'
d['C64-U05']['scans']='020, heading margin;021 opening;022 totals'
d['C64-U05']['quote']='À commencer par les \\unsure{2|3}-sous-groupes de Sylow (020); Quels sont les sous-groupes ... ? (021)'
d['C64-U05']['body']='The marginal programme on020 leads into the question on021 and the enumeration closing on022 with thirty subgroups, including the identity and whole group, in eleven conjugacy classes. The doubtful numeral2|3 in the announcement remains a reading issue rather than an authorial question mark. The enumeration is not left open, although the inclusion diagram requested afterwards is; C64-N14 and Hua’s §3 supply the comparison and independently checked count.'
d['C64-U07']['scans']='007, first paragraph;023 final line–024;025 opening'
d['C64-U07']['quote']='en fait ce cube est canoniquement orienté ; cf plus bas (007); Il y aurait lieu d’expliciter (023–024); orientation canonique (024)'
d['C64-U07']['body']='The first forward reference is on007, where the cube is called canonically oriented with cf plus bas. The request on023–024 covers vertices versus order-three rotations, opposite-edge pairs versus reflections, faces versus circular permutations, and an orientation construction. Faces are already identified with circular permutations in023’s definition, and the parity-torsor argument reaches OK on025, but the other requested correspondences are not expanded into explicit conversion maps. Hua’s §4 and C64-N16–N19 provide the comparison without attributing the supplementary orbit calculations to the manuscript.'
d['C64-T01']['title']='Title sheet and supplementary marks'
new=dict(id='C64-U12',title='The five square conversions are announced and carried out',scans='009, after the five descriptions;009–010, following constructions',kind='self-flagged',quote='Je vais expliciter les passages de l’une de ces descriptions à l’autre',body='This is a programme for the immediately following conversion constructions, not an unresolved request at the end of the packet. The page also changes quatre to cinq in counting the descriptions, and C64-N07 compares the resulting dictionary with Hua’s §2 while distinguishing its groupoid-level interpretation.',context='hua_project/64.modern.tex, §2, five square descriptions; current009–010',ledger='No separately reviewed RESULTS_STATE entry; prerequisite of Hua finding 64-gl2-z4-combinatorial-model',query='cinq|descriptions|passages|présentations|carré',checks=['scope:self-flags'],related='C64-N07')
a=[x for x in a if x['id']!='C64-U12'];a.append(new)
a.sort(key=lambda x:(0 if x['id'].startswith('C64-U') else 1,x['id']))
p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=r/'records/root_note_items.json';a=json.loads(p.read_text());d={x['id']:x for x in a}
d['C64-N07']['body']=d['C64-N07']['body'].replace('The five models require a groupoid-level comparison:','After the correction from quatre to cinq on009, the five models require a groupoid-level comparison:')
p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=r/'records/assemble_check_events.py';s=p.read_text()
s=s.replace("for id,out in background.items(): event(id,'carried as background without fault found',out)","for id,out in background.items(): event(id,'used and rechecked in this run' if id.startswith('Hua modernised') else 'carried as background without fault found',out)")
s=s.replace("with (r/'CHECK_EVENTS.tsv').open('w',newline='') as f:","event('C64-U01-C64-U12; C64-T01-C64-T03: apparatus review','used and rechecked in this run','Compared all authorial flags and pagination/headings with frozen text; added explicit012 warning,007 forward reference,009 conversion programme and020 enumeration announcement; clarified closure of023 face correspondence and avoided assigning authorship to pencil40. All18 body-page number marks match; no19 supplied.',congwho)\n\nwith (r/'CHECK_EVENTS.tsv').open('w',newline='') as f:")
p.write_text(s)
print('Completed authorial-marker review:12 U items,3 T records')
