from pathlib import Path
import json
W=Path(__file__).resolve().parents[1]
evidence={
'151_scan004':{
'B01':"The entire header and both separator rules were read in the upright crop. ACADEMIE and ACADEMIQUE have no accents. The two dark dots to the right of ACADEMIQUE are diagonally displaced and not aligned as the printed colon would be; nearby isolated copy dots have the same character. They do not establish punctuation. Bold versus margin wrappers and rule widths encode the same visible header; retain the original placement and separate rules.",
'B03':"The complete a/l/o/r/s letters are visible before the border, including the final s. The preceding ai is the end of demanderai, already in the full page, and is only an excerpt-boundary difference; it is not an additional word.",
'B04':"The detached upper loop, tall curved stem, low loop and short narrow turns form one autograph with a long connected oval flourish. They do not isolate a separate NB, exclamation or question mark. The lower separate line is clipped to a few tiny character tops. Retain the unreadable autograph and physically clipped line separately, without inventing missing letter bodies or a name."
},
'151_scan006':{
'B01':"The full typed words par l’Inspection Académique were inspected. The isolated block above a has no two sloping arms of a circumflex; an analogous detached irregular dot occurs above c. Both differ from the complete slanting acute over é. These copy marks do not securely establish an extra accent. Retain Académique, with the rejected accent hypothesis documented here rather than treating a print blemish as a new letter.",
'B02':"The complete final s of alors survives immediately before the border. The preceding ai belongs to demanderai, already transcribed in the full sentence; this is a crop-boundary difference only.",
'B03':"The autograph has the same continuous upper loop, narrow turns and connected long flourish within this crop; a complete letter-by-letter name cannot be separated. The independent lower line exposes only upper bowls and strokes. Retain both illegible units, and do not complete the second from the sender name.",
'B04':"The closer view shows two top bowls, paired upright tips and paired sloping tips. No R leg, U base or X crossing survives below the black image edge. Although these tops permit the conjecture ROUX, they cannot establish those complete letters. Physical clipping, not a recovered name, is recorded."
}}
for pg,ee in evidence.items():
 p=W/'records'/f'{pg}.json';r=json.loads(p.read_text());assert not r.get('audited')
 notes={k:{'viewed':True,'evidence':v} for k,v in ee.items()}
 (W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
 r['notes']+='\n### Blind crop adjudication\n\nEvery differing box was inspected upright. The apparent ai addition is the end of the already transcribed demanderai. The autograph and separate edge-clipped line remain unreadable; no name is completed from the sender block. '+('The diagonal pair of copy dots after ACADEMIQUE does not establish a printed colon.' if pg.endswith('004') else 'The detached irregular blocks above c and a in Académique do not establish a circumflex; the actual acute over é is distinct.')+' No transcription change was justified by the blind comparison.\n'
 p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
 print(pg,len(notes),'differing boxes personally viewed; zero changed.')
