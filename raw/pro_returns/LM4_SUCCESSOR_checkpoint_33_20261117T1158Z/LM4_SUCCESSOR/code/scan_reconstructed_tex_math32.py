"""Recovery32 source-only delimiter scan; no TeX or mathematics is executed."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    'work_A/A95_specified_center_free_boundary_proposed.tex',
    'work_A/A96_sphere_kernel_relative_two_proposed.tex',
    'work_A/A97_sphere_canonical_reflection_proposed.tex',
    'work_A/A98_sphere_cabling_correction_proposed.tex',
    'work_A/A99_regular_cusp_bridge_proposed.tex',
    'work_A/A100_full_GT_coefficient_proposed.tex',
    'work_A/A101_full_ring_Alexander_hexagon_proposed.tex',
    'work_CE/A102_odd_boundary_relative_two_proposed.tex',
    'work_CE/B155_single_fixed_coset_relative_kernel_proposed.tex',
    'work_CE/B156_remaining_family_basis_proposed.tex',
    'work_CE/B159_pre_node_section_delta_defect_proposed.tex',
    'work_DE/B157_recursive_cover_boundary_proposed.tex',
    'work_DE/B158_solvable_affine_boundary_proposed.tex',
    'work_DE/B160_actual_nilpotent_target_exclusion_proposed.tex',
]
MATH_ENVS = {'math','displaymath','equation','equation*','align','align*',
             'alignat','alignat*','flalign','flalign*','gather','gather*',
             'multline','multline*','eqnarray','eqnarray*','array','aligned',
             'alignedat','gathered','split','cases','matrix','pmatrix',
             'bmatrix','Bmatrix','vmatrix','Vmatrix','smallmatrix'}
LITERAL_ARGS = {'path','url','nolinkurl','label','ref','eqref','pageref',
                'cite','citet','citep','citealp','citeauthor','citeyear',
                'input','include'}


def scan(path):
    data = path.read_bytes()
    text = data.decode('utf-8')
    stack = []
    findings = []
    i = 0
    while i < len(text):
        if text[i] == '%':
            end = text.find('\n', i)
            i = len(text) if end < 0 else end + 1
            continue
        if text[i] == '\\':
            if text.startswith('\\(', i) or text.startswith('\\[', i):
                stack.append(text[i:i+2]); i += 2; continue
            if text.startswith('\\)', i) or text.startswith('\\]', i):
                expected = '\\(' if text[i+1] == ')' else '\\['
                if stack and stack[-1] == expected:
                    stack.pop()
                else:
                    findings.append({'line':text.count('\n',0,i)+1,'kind':'unmatched math close','token':text[i:i+2]})
                i += 2; continue
            env = re.match(r'\\(begin|end)\{([^}]+)\}', text[i:])
            if env:
                action, name = env.groups()
                if name in MATH_ENVS:
                    if action == 'begin':
                        stack.append(name)
                    elif stack and stack[-1] == name:
                        stack.pop()
                    else:
                        findings.append({'line':text.count('\n',0,i)+1,'kind':'unmatched math environment','token':env.group(0)})
                i += len(env.group(0)); continue
            command = re.match(r'\\([A-Za-z]+)\*?', text[i:])
            if command:
                name = command.group(1)
                j = i + len(command.group(0))
                if name in LITERAL_ARGS:
                    while j < len(text) and text[j].isspace():
                        j += 1
                    while j < len(text) and text[j] == '[':
                        end = text.find(']',j+1)
                        if end < 0: break
                        j=end+1
                        while j<len(text) and text[j].isspace(): j+=1
                    if j < len(text) and text[j] == '{':
                        depth=1; j+=1
                        while j<len(text) and depth:
                            if text[j]=='\\': j+=2; continue
                            if text[j]=='{': depth+=1
                            elif text[j]=='}': depth-=1
                            j+=1
                        i=j; continue
                i += len(command.group(0)); continue
            i += 2; continue  # escaped punctuation, including \_, \$, \%
        if text[i] == '$':
            mark='$$' if text.startswith('$$',i) else '$'
            if stack and stack[-1]==mark: stack.pop()
            else: stack.append(mark)
            i+=len(mark); continue
        if text[i] in '_^' and not stack:
            line=text.count('\n',0,i)+1
            start=text.rfind('\n',0,i)+1
            end=text.find('\n',i)
            if end<0: end=len(text)
            findings.append({'line':line,'kind':'outside-math script','token':text[i],
                             'context':text[start:end]})
        i+=1
    if stack:
        findings.append({'kind':'unclosed math state','stack':stack})
    return {'path':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(data).hexdigest(),
            'findings':findings}


if __name__ == '__main__':
    result=[scan(ROOT/name) for name in FILES]
    report={'scope':'Source-only lexical scan, not a TeX build or mathematical proof',
            'files':result,'outside_math_or_balance_findings':sum(len(r['findings']) for r in result)}
    print(json.dumps(report,indent=2))
