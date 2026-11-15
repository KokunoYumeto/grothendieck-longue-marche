import sys,csv
from pathlib import Path
sys.path.insert(0,'MPL_105_work/scripts')
from audit_page import audit_page
p=Path('MPL_105_work/pages/MPL_105_105_scan016.tex')
t=p.read_text(); old=t[t.index('\\margin{by '):t.index('\n\nThus, the axiom')]
new=r'''\margin{by \deleted{\unsure{the object}} \inserted{\unsure{simply}} \unsure{modifying|adjoining} \unsure{$\{0,1\}$ in $I$}, \unsure{if there is only one point}. \unsure{namely it can be embedded in an injective} --- but this is \unsure{always} true, because the Lawvere object is injective!!!}'''
audit_page(16,[(old,new),(r'L_{\mathcal A}\longrightarrow e',r'L_{\mathcal A}-e'),(r'I\times X\longrightarrow X',r'I\times X-X')],note='Re-read whole page and the diagonal margin in three rotated crops. Revised its provisional wording, retaining low confidence for the first clause; the final Lawvere-object sentence is clearer. Removed two unsupported arrowheads; both bottom squares checked.')
p=Path('MPL_105_work/MPL_105_inventory.csv')
rows=list(csv.DictReader(p.open())); sr=[r for r in rows if int(r['scan'])==16]; mx=max(int(r['element'].split('-')[-1]) if '-' in r['element'] else int(r['element']) for r in sr) if sr and sr[0]['element'].isdigit() else None
# Add a separately located insertion; preserve existing inventory identifiers.
rows.append(dict(cote='105',scan='16',sheet_kind='text',element='105-016-audit-insertion',kind='insertion',position='left diagonal margin above cancelled word',first_words_or_objects='simply (uncertain)',transcribed='yes'))
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']);w.writeheader();w.writerows(rows)
audit_page(17,[(r'TAILLE MINIMUM',r'TAILLE MINIMUN'),(r'\texttt{*}&\texttt{-}&\texttt{*}',r'\texttt{*}&\unsure{\texttt{--------------------------------------}}&\texttt{*}')],note='Both JESNEWS panels re-read in upright orientation. Retained the printed MINIMUN spelling; restored the full dashed underline under the HSM announcement, with its exact repeat count marked doubtful.')
audit_page(18,[(r'A\times I\longrightarrow A',r'A\times I-A'),(r'(I\longrightarrow e)',r'(I-e)'),(r'B\underset',r'B\underset')] if False else [(r'A\times I\longrightarrow A',r'A\times I-A'),(r'(I\longrightarrow e)',r'(I-e)'),(r"B'\longrightarrow B",r"B'-B")],note='All five numbered conditions, revised factorization, two marginal retract diagrams and source question about saturation compared. Headless strokes in three expressions retained; questionable formulas were not corrected mathematically.')
audit_page(19,note='Six JCL records, side handwriting and folio compared with upright image; no change.')
audit_page(20,[(r'f:X\longrightarrow Y',r'f:X-Y')],note='Compared the interval objection, two class inclusions, first! insertion, four question marks and both examples. Retained doubt about the overwritten product in the final insertion; one headless stroke corrected.')
p=Path('MPL_105_work/pages/MPL_105_105_scan021.tex');t=p.read_text(); old=next(l for l in t.splitlines() if r'RR\phantom{000000}RR' in l);new=old.replace(r'DD\phantom{00000000}DD\phantom{00}00',r'DD\phantom{0000000}DD\phantom{000}00')
audit_page(21,[(old,new)],note='Re-read all four zero glyphs and twelve banner rows, six START records and the two notices. Corrected the indentation in row ten of the D glyph; spacing elsewhere remains approximate to the fixed-pitch source.')
audit_page(22,[(r'F:X\longrightarrow Y',r'F:X-Y'),(r"Y'\longrightarrow Y",r"Y'-Y"),(r"X'\longrightarrow X",r"X'-X")],note='Four problems and their short argument compared, including admitted factorization and the right-properness condition. Three plain connecting strokes retained without arrowheads; marginal lifting diagram checked.')
