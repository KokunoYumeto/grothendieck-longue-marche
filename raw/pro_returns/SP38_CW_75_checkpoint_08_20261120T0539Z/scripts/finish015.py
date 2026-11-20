from pathlib import Path
import json
from datetime import datetime,timezone
o=Path(__file__).resolve().parents[1]
additions={
'notation_current.md':r'''

## Scan 015 additions

- Doubled R and C resolve from distinct internal stems. Later E,V,P,S,A,R are plain capitals; overwritten letters are judged separately.
- The post-existential sign is an uninterrupted bare upright, retained as vert|1 without supplying an exclamation dot. A different raised mark after transformed P has two components and remains prime|! locally.
- The first chain's two lower spurs remain uncertain old commas; its canceled letter is A|B. The later old P resolves, but the live correcting S remains independently uncertain.
- Metrique and cotes lack restored accents. Five local polygône/polygônes occurrences have detached upper marks; the first body polygone does not. The contraction rèal.|réal. and both normalisee|normalisée endings are judged separately.
- The canceled si V P S clause has semicolon|comma after V and a hooked cancellation return. The orientation relation has one shaft and two heads. Enclosure boundaries and both insertion leads are drawn without completing missing edges.
''',
'written_irregularities.md':r'''

- Scan 015: retain P et P′, later ambient V after initial affine E, grâce : centre de gravité, and the bare upright after ∃. Metrique and cotes are unaccented; normalization accents remain local doubts. The earlier embedding requirement excludes an unqualified digon realization, and the equal-angle proof uses interior angles; both qualifications are in mathematical notes only.
''',
'legibility.md':r'''

Scan 015 has readable exercise prose with compressed endings and several heavily overwritten objects. Seven of eighteen original C doubts resolve, eleven remain, and six new uncertainties are retained. H expands abbreviations, replaces the metric phrase, omits correction strokes and changes the singular orientation wording. The main review used 32 crops, reusing 23 and making nine only where the reported half-settled difference lacked a crop. The separate live-S doubt shows why recovering an old letter does not settle its correction.
''',
'lessons.md':r'''

Scan 015: all three complete final returns were compared before the main saw any image. The apparent closed bubble in one return had visibly open boundaries and a separate comma. R2 alone recorded the short underline beneath repeated régulière; R3 supplied the cancellation hook and the distinction between a recoverable old P and its insecure live S correction. Existing crops settled all C doubts; nine new crops covered previously half-settled witness differences. Local accents were assessed separately, and the gravity insertion's baseline continuation was kept beneath its lead. Mathematical qualifications were recorded without changing the written words or signs.
'''}
for name,s in additions.items():
    p=o/'briefs'/name
    with p.open('a') as f:f.write(s)
brief=(o/'briefs/brief_v15_scan015.md').read_text().replace('brief v15 — first used scan 015','brief v16 — first used scan 016',1)
brief+=r'''

## Refinements after scan 015

- The certainty of an overwritten predecessor and the certainty of its live correction are independent. If their shared contour leaves one uncertain, mark that object separately rather than letting the expected formula decide it.
- Preserve the visible open ends of an annotation boundary, especially at the sheet edge. Keep a separate comma in its actual relation to the text and boundary instead of placing it after the whole drawing.
- Inspect accents and short underlines independently from the word. A local ending need not inherit the spelling or confidence of another occurrence. Keep baseline text below an interlinear connector beneath that connector in the actual TikZ layout.
'''
(o/'briefs/brief_v16_scan016.md').write_text(brief)
(o/'briefs/notation_before_scan016.md').write_text((o/'briefs/notation_current.md').read_text())
p=o/'briefs/history.json';h=json.loads(p.read_text());assert all(x['scan']!=16 for x in h)
h.append(dict(scan=16,file='brief_v16_scan016.md',reason='After scan015: distinguish predecessor and live-correction certainty; preserve open boundary ends and comma placement; inspect local accents and short underlines; keep baseline continuation beneath insertion lead.'))
p.write_text(json.dumps(h,ensure_ascii=False,indent=2)+'\n')
with (o/'progress.log').open('a') as f:f.write('scan015 all three final returns compared, 32 main crops inspected, 18 C doubts disposed; draft and audit records synchronized '+datetime.now(timezone.utc).isoformat()+'\n')
print('Scan015 notes and notation updated; scan016 brief prepared.')
