from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
p=r/'records/root_note_items.json'
a=json.loads(p.read_text()); d={x['id']:x for x in a}
d['C64-N02']['body']=d['C64-N02']['body'].replace('makes the following faithful conjugation action on V correct','makes the induced conjugation action of S4/V on V faithful')
d['C64-N06']['body']='For a nonidentity x in V, the centralizer in S4 has order eight and is a Sylow2-subgroup, whereas the cyclic subgroup with unique involution x has order four. The first diagram on007 targets cyclic groups, while the later triangle separates the two families; on020 the full-centralizer assertion for D-plus is likewise false if interpreted in S4, since D-plus is only the rotation subgroup of that centralizer. This run confirms all three centralizer orders, agreeing with Hua’s warning in §1 while identifying the same remaining erroneous clause in his §3; neither the frozen arrows nor their superscripts has been repaired.'
d['C64-N10']['quote']='il faut expliciter d’abord les conventions'
d['C64-N14']['quote']='six → trois (021); Cela fait en tout28 sous-groupes (022)'
d['C64-N15']['body']='The finite certificate supplies the omitted subgroup poset as s4_subgroups.csv and s4_hasse_edges.csv:30 actual subgroups and66 covering inclusions, with exact indices. This completes the requested inclusion calculation, while the diagram of all equivariant homogeneous-space maps additionally requires transporter cosets, Hom_G(G/H,G/K)≃{gK:g⁻¹Hg⊆K}, computed from those actual subgroups. Confidence is high because every subgroup and intervening inclusion was enumerated in S4; Hua’s §3 also records that the manuscript does not draw the diagram.'
d['C64-N17']['body']='The map sending i∈I to its block in each of the three pair-partitions embeds I in an eight-element product; after temporarily labelling each two-element factor, its image is one parity fibre. Intrinsically I is a torsor under the four-element augmentation kernel and selects a point in the two-element contracted product, so the stated trivialization retains none of those temporary labels. The exact four-set calculation confirms this description, and Hua’s §4 gives the same argument; the word OK on025 closes this part of the preceding proposed orientation construction.'
d['C64-N27']['body']=d['C64-N27']['body'].replace('the two central involutions','the centre {±I}')
p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print('Applied targeted review corrections to research notes only')
