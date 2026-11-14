"""Apply and record the first observed checkpoint-200 TeX layout repairs."""
from pathlib import Path
import difflib
import hashlib
import json
import re
import shutil

ROOT = Path('/workspace/scratch/e34c61ec5a35')
BASE = ROOT / 'LM7_FERMAT_TOWER'
P = BASE / 'sections/E_first_unit_norms.tex'
old = P.read_text()
assert hashlib.sha256(old.encode()).hexdigest() == '020f0807708fe6275906992686bb019cf9f15a18645ac469a15c0326c73cbd77'
new = old

def replace(a, b):
    global new
    assert new.count(a) == 1, a
    new = new.replace(a, b)

replace(r''' \zeta^2+\zeta+1=0,\quad \xi^3=\zeta,\quad
 \beta_1^3=17\zeta,\quad\beta_2^3=\beta_1,\qquad
 L_i=\mathbb Q(\zeta,\beta_i),\quad B_i=L_i(\xi),
 \quad c_1=\beta_1+1+3\zeta.''', r''' \begin{gathered}
 \zeta^2+\zeta+1=0,\quad \xi^3=\zeta,\quad
 \beta_1^3=17\zeta,\quad\beta_2^3=\beta_1,\\
 L_i=\mathbb Q(\zeta,\beta_i),\quad B_i=L_i(\xi),
 \quad c_1=\beta_1+1+3\zeta.
 \end{gathered}''')

original_matrix = r''' -37103278413&25225148828&-5743099426&-1117338456&415980086&-548768638\\
 161479643843&-70558353324&-3192102308&5646166658&-6279927666&1260332509\\
 -551544947582&-108462373370&26395251042&-53737480949&14839765429&-2202740637'''
transposed_matrix = r''' -37103278413&161479643843&-551544947582\\
 25225148828&-70558353324&-108462373370\\
 -5743099426&-3192102308&26395251042\\
 -1117338456&5646166658&-53737480949\\
 415980086&-6279927666&14839765429\\
 -548768638&1260332509&-2202740637'''
rows = [list(map(int, re.findall(r'-?\d+', s))) for s in original_matrix.split(r'\\')]
trows = [list(map(int, re.findall(r'-?\d+', s))) for s in transposed_matrix.split(r'\\')]
assert rows == [list(v) for v in zip(*trows)]
replace(r''' \begin{pmatrix}U_0\\U_1\\U_2\end{pmatrix}
 =\frac1{16578519}
 \begin{pmatrix}
''' + original_matrix + r'''
 \end{pmatrix}
 \begin{pmatrix}1\\b\\b^2\\b^3\\b^4\\b^5\end{pmatrix}.''', r''' \begin{gathered}
 (U_0,U_1,U_2)^t=\frac1{16578519}\mathcal U
       (1,b,b^2,b^3,b^4,b^5)^t,\\
 \mathcal U^t=\begin{pmatrix}
''' + transposed_matrix + r'''
 \end{pmatrix}.
 \end{gathered}''')

replace(r''' A=\begin{pmatrix}0&0&\epsilon\\1&0&0\\0&1&0\end{pmatrix},
 \quad S=\operatorname{diag}(1,\zeta,\zeta^2),
 \quad B=(U_0I+U_1A+U_2A^2)S.
 \quad A^3=\epsilon I,\quad B^3=bI,\quad BA=\zeta AB.''', r''' \begin{gathered}
 A=\begin{pmatrix}0&0&\epsilon\\1&0&0\\0&1&0\end{pmatrix},
 \quad S=\operatorname{diag}(1,\zeta,\zeta^2),\\
 B=(U_0I+U_1A+U_2A^2)S,\\
 A^3=\epsilon I,\quad B^3=bI,\quad BA=\zeta AB.
 \end{gathered}''')

for label in ('E101.20', 'E101.21'):
    end = new.index(r' \tag{' + label + '}')
    start = new.rfind(r'\[', 0, end)
    piece = new[start:end]
    assert piece.count(r'\begin{pmatrix}') == piece.count(r'\end{pmatrix}') == 1
    edited = piece.replace(r'\begin{pmatrix}', r'\left(\begin{array}{*{15}{r}}').replace(r'\end{pmatrix}', r'\end{array}\right)')
    assert re.findall(r'-?\d+', piece) == re.findall(r'-?\d+', edited.replace('{*{15}{r}}', ''))
    replace(piece, edited)

shutil.copy2(BASE / 'code/build200.out', BASE / 'code/build200_initial_layout_failure.out')
P.write_text(new)
entry = {
    'path': str(P.relative_to(BASE)),
    'frozen_sha256': hashlib.sha256(old.encode()).hexdigest(),
    'presented_sha256': hashlib.sha256(new.encode()).hexdigest(),
    'reason': 'Observed TeX column-limit failure and three overfull displays. The wide coefficient matrix is written via its explicit transpose, with all 18 entries checked exactly. Other changes are line breaks and equivalent array delimiters. No proof assertion or arithmetic program changed.',
    'coefficient_transpose_exact': True,
    'fifteen_column_matrix_entries_unchanged': True,
    'diff': ''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile='frozen proof', tofile='presented proof')),
}
(BASE / 'ledger/checkpoint200_layout_corrections.json').write_text(json.dumps([entry], indent=2) + '\n')
print(json.dumps({'status': 'PASS', **{k:v for k,v in entry.items() if k != 'diff'}}, indent=2))
