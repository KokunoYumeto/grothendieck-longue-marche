from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

out=Path(__file__).resolve().parents[1]
receipt=out/'records/notes_condensation_004_007.json'
assert not receipt.exists()
notes={
4:[
"Landscape handwritten working sheet with six principal sketches, no title, date or author folio; archive 3 is a comment. The readers found no continuous recoverable type in the pale background, so H's typed-verso description does not establish another transcribable passage. The sheet is classified text.",
"The upper Ob/Fl diagram contains closed-loop ell arguments where both witnesses give C; its top source is Ob C_4, the target index n/1 remains uncertain, and the live lower replacement has a clear 1. In the subsequent F_3 product the third argument is ell_3. Two wedge signs are literally <, including one read as multiplication by both witnesses, and the separator after F_n is a connected 2-shaped stroke rather than two equality bars. Expected products or equality do not replace this surprising ink. These are reading observations, not demonstrated mathematical errors.",
"The lower work records inclusions, a product ending literally (- ?), starred pairs, and an amalgamation after (F x I). The question mark is the author's explicit doubt; no verbal à vérifier, sauf erreur or je présume is present. F alphabets are judged locally: separate returning stems support doubled forms, while the third F_3 Fl and last F_n Fl retain a shared plain/doubled doubt. The final starred pair has an uncertain old O/0, live O_3/O_n and overwritten F index n/n+1/3; H's definite n+1 is not established. The right-hand O/F composites retain uncertain overwrite order, with distinct large hats and a smaller dot-like mark; B remains possible in the small composite.",
"Sketches preserve open boundaries, interrupted strokes, a detached arrowhead, tiny counters in dark knots, separate points and the hatched lens. No mathematical meaning or universal property is assigned to those shapes. H's drawing code was compared with the source by all readers and reported differences adjudicated. No theorem was proved or used as mathematical background; this page has no check event."
],
7:[
"The page introduces M with (i) every arrow monic and (ii) every endomorphism an identity, and names a category from an ordered set as an example. The conditions are carried as hypotheses (007-HYPOTHESES), not an independently checked external example. Author folio 1 and archive 6 are recorded; no date or separate title appears.",
"For D it defines the ordered subobjects, written as tilded plain D, and identifies D with their greatest element. The starred map Hom_M(D-prime,D) to that order sends an arrow to its represented subobject. The main check and subsequent re-proof of 007-INJECTIVE verify injectivity and the image description: the subobjects M-isomorphic to D-prime. Equality of images yields a domain automorphism, hence the identity by (ii). The small M- belongs before isomorphes. The two-row map retains M below the final m of Hom and its unequal arrow starts.",
"Object classes are denoted first by plain N, then locally doubled N. The insertion says Il est en fait ordonné, grâce à (ii), with ordonné underlined. Checks of 007-CLASS-ORDER establish antisymmetry of reachability: arrows in both directions compose to identities. Representatives D_n and their subobject orders are described à isom unique près; the resulting family has doubled J_n. Checks of 007-CANONICAL-TRANSPORT verify uniqueness of the object isomorphism and its induced order transport, including identity/composition compatibility.",
"Uniqueness of every abstract order isomorphism is stronger and is not attributed as the author's intended claim. Its checked counterexample (007-SUBOBJECT-ALL-ISOS) has two objects and two parallel arrows: the two incomparable subobjects below the top can be exchanged, whereas canonical transport is fixed. The set-level size convention remains ambient; (i)/(ii) alone do not prove the collections are sets.",
"Cancellations, inserted end and M-, corrected alphabet forms and disputed wording remain literal; mathematical expectations settle no glyph. No explicit author question or verbal doubt is recorded. CHECK_EVENTS preserves all nine actual events and full arguments: five main events and four from a text audit that saw the proposed arguments, so was not blind. The image readers report no mathematical checks."
]}
hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (out/'pages').glob('*.tex')}
changes=[]
for n,paras in notes.items():
    p=out/f'records/scan{n:03d}/decision.json'
    d=json.loads(p.read_text()); old=d['notes']; d['notes']=paras
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    changes.append(dict(scan=n,prior_notes=old,prior_words=len(' '.join(old).split()),new_words=len(' '.join(paras).split())))
lines=['# SP48_CW_104: notes while reading','','These notes concern only the supplied pages. A statement being transcribed is not thereby proved. Actual checks and limited background uses are identified in CHECK_EVENTS.tsv.','']
for p in sorted((out/'records').glob('scan*/decision.json')):
    d=json.loads(p.read_text()); lines += [f"## Scan {int(d['scan']):03d}",'']
    for para in d['notes']:lines += [para,'']
(out/'SP48_CW_104_notes.md').write_text('\n'.join(lines)+'\n')
assert hashes=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (out/'pages').glob('*.tex')}
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
receipt.write_text(json.dumps(dict(date=stamp,scope='Editorial condensation of notes only; mathematical outcomes and full check-event arguments unchanged; no new check or image inspection',changes=changes,page_hashes_unchanged=hashes),ensure_ascii=False,indent=2)+'\n')
with (out/'progress.log').open('a') as f:f.write(f'Notes condensed {stamp}: scans004/007; full check arguments preserved; seven page hashes and CHECK_EVENTS unchanged.\n')
print([(x['scan'],x['prior_words'],x['new_words']) for x in changes])
