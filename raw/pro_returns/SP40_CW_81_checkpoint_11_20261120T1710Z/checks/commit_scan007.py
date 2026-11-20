from pathlib import Path
from datetime import datetime,timezone
import json
R=Path('out');reports={k:json.loads((R/f'readers/007/{k}/report.json').read_text()) for k in 'ABC'}
source=Path('packets/007/C.tex').read_text()
drawing=r'''% The phrase is visibly drawn once by rlap. The phantom preserves its deletion
% annotation and text dimensions without adding the generic horizontal rule.
\begin{tikzpicture}[baseline=(cancelled.base)]
\node[inner sep=0pt,outer sep=0pt] (cancelled)
 {\rlap{ou $p=1$}\phantom{\deleted{ou $p=1$}}};
\draw[line width=.55pt] ([xshift=-1.5mm,yshift=-1.5mm]cancelled.south west) -- ([xshift=3mm,yshift=4mm]cancelled.north east);
\draw[line width=.25pt] ([xshift=-1.5mm,yshift=-2mm]cancelled.south west) -- ([xshift=3mm,yshift=3.65mm]cancelled.north east);
\end{tikzpicture}
'''
assert source.count(r'\deleted{ou $p=1$}')==1
page=source.replace(r'\deleted{ou $p=1$}',drawing)
(R/'pages/J81-01_81_scan007.tex').write_text(page)
choices=[
('Opening blacked-out item before Soit',r'\deleted{\illegible{1}}','low','readers/007/C/01_top_cancel.png','The root crop view shows dense overlaid black loops and projecting strokes, without a recoverable internal character sequence. The placeholder denotes one compact unreadable item; it does not establish the original word count.'),
('Pale marginal note, initial character',r'\unsure{a|\alpha}','medium','readers/007/B/crops/02_pale_note.png','The small low loop joins a rightward descending tail. These visible strokes support both a and alpha, without settling the choice; the existing candidate order is retained.'),
('Pale marginal note, verb ending',r"\unsure{n'exist|n'existe}",'medium','readers/007/B/crops/02_pale_note.png','The word ends in a tall stroke with a short bent return to the right. A separate final e cannot be isolated confidently; both readings remain. The two C doubt-table entries concern this one physical locus.')]
dec=[];doubts=[]
for i,(loc,reading,conf,crop,ev) in enumerate(choices,1):
 src={k:reports[k]['differences'][i-1] for k in 'ABC'}
 dec.append(dict(id=f'007-{i:02}',location=loc,C=reading,H=None,final=reading,readers={k:v['reading'] for k,v in src.items()},evidence=ev,crop=crop,confidence=conf,kind='other',diff_C=False,diff_H=False,C_doubt_status='retained',marked_in_H='no',reader_provenance=src,root_decided=True))
 alt=[['unrecoverable original sequence'],[r'\alpha'],["n’existe"]][i-1]
 doubts.append(dict(location=loc,reading=reading,alternatives=alt,confidence=conf,reason=ev,crop=crop))
dec.append(dict(id='007-04',location='Soit p sentence, paired cancellation strokes over ou p=1',C=r'\deleted{ou $p=1$}',H=None,final=drawing,readers={'A':r'\deleted{ou $p=1$}; report describes two close rising strokes','B':reports['B']['differences'][3]['reading'],'C':r'\deleted{ou $p=1$}; report describes two rising strokes'},evidence='Root viewed crops/007/01_cancellation_pair.png. A dark upper diagonal and a paler, nearly parallel lower stroke run from below ou at the left to above the equality and numeral at the right. The letters ou and p=1 remain readable. Both lines are represented explicitly.',crop='crops/007/01_cancellation_pair.png',confidence='high',kind='drawing or diagram',diff_C=True,diff_H=False,C_doubt_status=None,marked_in_H='no',qualification='This adds physical stroke geometry. The wording and cancellation state already agree with C. The local macro redefinition in reader B’s proposal is replaced by standard rlap/phantom boxing, preserving the active deleted annotation and adding no visible third line.',root_decided=True))
inv=reports['B']['inventory']
for i,x in enumerate(inv,1):x['element']=f'007.{i:02}';x['transcribed']='yes'
inv[10]['first_words_or_objects']='ou p=1, cancelled by the explicitly drawn dark upper and pale lower rising strokes'
notes='''The page introduces a,b,c,q, the inserted equation a^q+b^q=c^q, and the written pairwise-coprimality conditions. It expands (a+b′)^q, writes the numbered equality (1), then gives divisibility pairs and a chain involving α, α′, b′ and b″. This reports the manuscript’s argument. The phrase ou p=1 is cancelled with two rising strokes; both are drawn. The pale note reads a/α n’exist/n’existe pas si on avait p=1, with the two stated editorial doubts retained. The opening blacked-out item is unreadable. No title, date or authorial uncertainty phrase was observed. Archive numeral6 remains a comment.

The readers inspected the small binomial indices, primes, comparison marks and crowded lower sums. Their ink readings agree with C; no mathematical expectation changed a glyph. Three unique C doubts remain, including the note ending listed twice in the supplied doubt table. H supplies no text. The inventory retains the supplied anonymous other-hand designation for the upright main writing; no personal identity is established, and the pale note’s hand remains undetermined.

One exact arithmetic instance was checked at11:09:38 UTC: a=3,b=4,c=5,q=2,p=2,b′=2,α=2,α′=1,b″=1. The binomial and factored values are16; the final bracket and divisor are both8, with quotient1 and remainder0. Coprimality and the two exact valuations were checked numerically. The evaluation morphism and full certificate are in checks/scan007_arithmetic.md. This finite calculation checks that instance of the displayed substitution/exponent pattern; it supplies no general proof of the page’s implications.'''
record=dict(scan=7,folder='J81-01',their_page='6',hua_has='nothing',filename='J81-01_81_scan007.tex',brief_version='v06',main_adjudicated=True,main_approved_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),decisions=dec,doubts=doubts,inventory=inv,notes=notes,abbreviations=[],check_events=json.loads((R/'checks/scan007_check_events.json').read_text()),workflow_note='Each reader viewed the whole scan and both supplied halves once. A/B/C made3/3/6 crops. Root compared all three returns and viewed two existing reader crops plus one new crop, with no whole/half image view. All three original C doubts remain; the duplicated note-ending entry is counted once. The only C difference adds the paired cancellation geometry already described by all readers. The final TikZ uses standard boxing and the supplied deletion macro, without macro redefinition or an extra horizontal stroke. The main text otherwise equals C exactly. The opening placeholder denotes one compact unreadable unit, not a recovered word count. H has no rows. Reader A omitted the archive numeral from its inventory but included its comment; B/C inventories include it and the final inventory does too. No reader mathematical check was claimed; the one root finite-instance computation is separately scoped.',source_reports=reports)
p=Path('out/scripts/validate.py').resolve();ns={'__file__':str(p)};exec(p.read_text().split('records=')[0],ns)
check=ns['check_tex']((R/'pages/J81-01_81_scan007.tex').resolve());assert not check['errors'],check
(R/'checks/scan007_syntax.json').write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n')
(R/'records/scan007.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
(R/'crops/007/manifest.json').write_text(json.dumps([dict(path='crops/007/01_cancellation_pair.png',bbox=[800,800,1100,940],rotation=0,width=2800,purpose='paired cancellation stroke geometry reported as a C difference by B',viewed=True)],indent=2)+'\n')
(R/'checks/scan007_main_decisions.md').write_text('''# Scan007 — root adjudication

Root compared all three complete proposals and reports. Successfully viewed evidence: readers/007/C/01_top_cancel.png; readers/007/B/crops/02_pale_note.png; crops/007/01_cancellation_pair.png. No full or half scan was viewed by root. The three original C doubts remain with explicit physical limits. The one added graphic detail preserves both visible cancellation strokes over ou p=1. No text, formula or deletion state is changed from C. H supplies no text.

The three readers described the paired strokes; only B drew them explicitly. Root retains that geometry and replaces B’s local macro redefinition with standard rlap/phantom boxing. The visible phrase is drawn once, while the phantom carries its deleted annotation and dimensions without a horizontal rule. All nineteen inventory entries are present, including the archive-number comment. Structural validation passed, without compilation.
''')
with (R/'notation.md').open('a') as f:f.write(r'''

| Positive-integer alphabet | `\mathbb N^*` | Scan007, repeated membership conditions; doubled left N strokes and raised star | Three independent visual readings agree |
| Bowl with lower numeral | `\mathrel{\underset{1}{\smile}}` | Scan007, pairwise line and two lower expressions; shallow bowl with separate hooked1 | Parenthesis reads premiers entre eux deux à deux |
| Binomial coefficient and sum indices | `C_q^i`; `\sum_{i=0}^{q}`, later `\sum_{i=1}^{q-1}` | Scan007, upper expansion through final sums; separately dotted i and lowered q | Crowded lower occurrences checked by independent reader crops |
| Divisibility and implication | `\mid`, `\nmid`, `\Longrightarrow` | Scan007, two divisibility pairs and lower chain | Plain/crossed upright and broad two-shaft arrow preserved |
| Main-hand and pale-note alpha forms | `\alpha`, `\alpha'`; pale `\unsure{a|\alpha}` | Scan007, main exponents versus small pale note | Preserve pale-note uncertainty independently |
| Comparison strokes | `\geqslant`, `\leqslant` | Scan007, parenthetical conditions and valuation inequality | Separate lower slant retained |
''')
print({'scan':7,'C_loci':1,'H_loci':0,'doubts':3,'inventory':len(inv),'hash':check['sha256']})
