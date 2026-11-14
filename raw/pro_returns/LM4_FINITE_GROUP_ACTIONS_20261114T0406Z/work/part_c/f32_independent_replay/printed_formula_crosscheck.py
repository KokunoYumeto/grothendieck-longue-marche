"""Read the frozen F.32 displays themselves and compare exact Laurent forms.

The small parser below implements integer arithmetic independently of the
certificate helpers. It accepts only the six specified variables, P_4/P_6,
integer powers, sums, products and divisions by signed Laurent monomials.
No producer/checker program is executed. The checker row strings are read
from the literal return value in its AST.
"""
from ast import FunctionDef, Return, literal_eval, parse as ast_parse, walk
from collections import Counter
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PROOF = ROOT / 'work/part_a/f_nonproduct_first_character_one_images.tex'
CHECKER = ROOT / 'work/part_a/code/affine_nonproduct_r1_independent_audit.py'
CHECKED = ROOT / 'work/part_a/code/affine_nonproduct_r1_independent_audit_output.json'
GENERAL = ROOT / 'work/part_a/code/affine_nonproduct_boundary_quotient_stage_output.json'
EXPECTED_PROOF = 'b91fd2611f1d9bd5cde096c6307004dca0fc740463971c164aa0fe52a146af13'
COUNTS = Counter()
ZERO_EXP = (0,)*6
ONE = {ZERO_EXP: 1}


def bind(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(data),
            'sha256': sha256(data).hexdigest()}


def plus(a, b):
    c = dict(a)
    for e, value in b.items():
        c[e] = c.get(e, 0)+value
        if c[e] == 0:
            del c[e]
    return c


def neg(a):
    return {e: -v for e, v in a.items()}


def times(a, b):
    result = {}
    for e, av in a.items():
        for f, bv in b.items():
            result = plus(result, {tuple(x+y for x, y in zip(e, f)): av*bv})
    return result


def power(a, exponent):
    if exponent < 0:
        assert len(a) == 1, 'Only monomial denominators are admitted.'
        e, v = next(iter(a.items()))
        assert v in (-1, 1), 'Only signed unit coefficients are inverted.'
        return {tuple(n*exponent for n in e): v**(-exponent)}
    result = ONE
    for _ in range(exponent):
        result = times(result, a)
    return result


class LaurentParser:
    def __init__(self, source, definitions=None):
        text = source.replace('**', '^')
        text = text.replace(r'\{', '(').replace(r'\}', ')')
        text = text.translate(str.maketrans({'{': '(', '}': ')', '[': '(', ']': ')'}))
        self.text = re.sub(r'\s+', '', text)
        self.tokens = re.findall(r'P_[46]|[htuvwz]|\d+|[()+*/^\-]', self.text)
        assert ''.join(self.tokens) == self.text, ('unaccepted token', source)
        self.index = 0
        self.definitions = definitions or {}

    def peek(self):
        return self.tokens[self.index] if self.index < len(self.tokens) else None

    def take(self):
        value = self.peek()
        assert value is not None
        self.index += 1
        return value

    def expression(self):
        value = self.term()
        while self.peek() in ('+', '-'):
            operation = self.take()
            term = self.term()
            value = plus(value, term if operation == '+' else neg(term))
        return value

    def term(self):
        value = self.unary()
        while self.peek() is not None and self.peek() not in ('+', '-', ')'):
            operation = self.peek()
            if operation in ('*', '/'):
                self.take()
            else:
                operation = '*'
            term = self.unary()
            value = times(value, power(term, -1) if operation == '/' else term)
        return value

    def unary(self):
        if self.peek() in ('+', '-'):
            sign = self.take()
            value = self.unary()
            return neg(value) if sign == '-' else value
        return self.factor()

    def factor(self):
        token = self.take()
        if token == '(':
            value = self.expression()
            assert self.take() == ')'
        elif token in 'htuvwz' and len(token) == 1:
            value = {tuple(int(i == 'htuvwz'.index(token)) for i in range(6)): 1}
        elif token in self.definitions:
            value = self.definitions[token]
        else:
            assert token.isdigit(), token
            value = {} if int(token) == 0 else {ZERO_EXP: int(token)}
        if self.peek() == '^':
            self.take()
            bracket = self.peek() == '('
            if bracket:
                self.take()
            sign = -1 if self.peek() == '-' else 1
            if self.peek() in ('+', '-'):
                self.take()
            number = self.take()
            assert number.isdigit()
            if bracket:
                assert self.take() == ')'
            value = power(value, sign*int(number))
        return value

    def result(self):
        value = self.expression()
        assert self.peek() is None
        return value


def polynomial(text, definitions=None):
    return LaurentParser(text, definitions).result()


def equal(left, right, category):
    assert left == right, category
    COUNTS[category] += 1


def determinant(rows):
    result = {}
    for order in permutations(range(5)):
        parity = sum(order[i] > order[j] for i in range(5) for j in range(i+1, 5))
        term = neg(ONE) if parity % 2 else ONE
        for i, j in enumerate(order):
            term = times(term, rows[i][j])
        result = plus(result, term)
    return result


def main():
    assert bind(PROOF)['sha256'] == EXPECTED_PROOF
    source = PROOF.read_text()
    checked = json.loads(CHECKED.read_text())
    assert checked['verifier_sha256'] == bind(CHECKER)['sha256']
    tree = ast_parse(CHECKER.read_text())
    fn = next(n for n in tree.body if isinstance(n, FunctionDef) and n.name == 'prescribed_rows')
    checker_rows = literal_eval(next(n.value for n in walk(fn) if isinstance(n, Return)))

    # The two auxiliary polynomial bodies are taken from the TeX, not retyped.
    p4match = re.search(r'P_4=\{\}&(.*?)\\\\\s*P_6=\{\}&(.*?)\.\s*\\end\{aligned\}', source, re.S)
    assert p4match
    assert p4match[1].rstrip().endswith(',')
    definitions = {'P_4': polynomial(p4match[1].rstrip()[:-1]),
                   'P_6': polynomial(p4match[2])}
    row_pattern = (
        r'\\widehat q_(\d+|\{\d+\})\^\{\\mathsf T\}\s*=\s*'
        r'(?:\\frac1\{([^}]+)\})?\s*\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}')
    raw_rows = {}
    rows = {}
    for match in re.finditer(row_pattern, source, re.S):
        index = int(match[1].strip('{}'))
        assert index not in rows
        denominator = polynomial(match[2] or '1')
        raw = match[3].split(r'\\')
        assert len(raw) == 5
        values = [times(polynomial(x, definitions), power(denominator, -1)) for x in raw]
        rows[index] = values
        raw_rows[str(index)] = {'denominator_tex': match[2] or '1', 'numerators_tex': raw}
        for got, expected in zip(values, checker_rows[index]):
            equal(got, polynomial(expected), 'printed_row_entry_vs_independent_checker')
    assert set(rows) == {1, 3, 4, 5, 6, 8, 9, 10}

    # Read the four displayed determinant entries, then recompute each directly
    # from the forty source-parsed entries by the 120-term Leibniz formula.
    determinant_table = re.search(
        r'a&\\det\\widehat R_a\\\\\\hline\s*(.*?)\\end\{array\}', source, re.S)
    assert determinant_table
    determinant_rows = [x.strip() for x in determinant_table[1].split(r'\\') if x.strip()]
    extracted_determinants = {}
    for line in determinant_rows:
        label, formula = line.split('&')
        index = int(label)
        expected_record = next(x for x in checked['determinants']
                               if x['sources_zero_based'][-1] == index)
        printed = polynomial(formula)
        equal(printed, polynomial(expected_record['compact_determinant']),
              'printed_determinant_vs_checked_record')
        actual = determinant([rows[i] for i in [1, 8, 9, 10, index]])
        equal(actual, printed, 'source_parsed_row_determinant')
        extracted_determinants[str(index)] = formula
    assert set(extracted_determinants) == {'3', '4', '5', '6'}

    # Parse all eight literal root-table lines.
    roots_match = re.search(
        r'l&\\text\{base roots of \}Q_l&b_l\\\\\\hline\s*(.*?)\\end\{array\}', source, re.S)
    assert roots_match
    expected_roots = {
        1: (['1', '(v*w)^-1'], '(t*z)^-1'),
        3: (['1', '(u*z)^-1'], '(t*w)^-1'),
        4: (['1', '(v*z)^-1'], '(t*u)^-1'),
        5: (['1', '(u*w)^-1'], '(t*v)^-1'),
        6: (['1', '(v*w)^-1', '(h/u)^2'], '(t*z)^-1'),
        8: (['1', '(u*z)^-1', '(h/v)^2'], '(t*w)^-1'),
        9: (['1', '(v*z)^-1', '(h/w)^2'], '(t*u)^-1'),
        10: (['1', '(u*w)^-1', '(h/z)^2'], '(t*v)^-1')}
    extracted_roots = {}
    for line in roots_match[1].split(r'\\'):
        if not line.strip():
            continue
        label, bases, moving = line.strip().split('&')
        index = int(label)
        actual_bases = bases.split(',')
        expected_bases, expected_moving = expected_roots[index]
        equal([polynomial(x) for x in actual_bases],
              [polynomial(x) for x in expected_bases], 'printed_base_roots')
        equal(polynomial(moving), polynomial(expected_moving), 'printed_moving_root')
        extracted_roots[str(index)] = {'base_roots_tex': actual_bases, 'moving_root_tex': moving}
    assert len(extracted_roots) == 8

    scalar_tables = {}
    for symbol, expected in [
        ('lambda', ['1', '1', 't', '1', '1', '1', 'u^-2', '(h*t)^-1', 'v^-2', 'w^-2', 'z^-2']),
        ('nu', checked['quotient_characters'])]:
        pattern = r'\(\\'+symbol+r'_0,\\ldots,\\'+symbol+r'_\{10\}\)=\s*\((.*?)\)\.'
        match = re.search(pattern, source, re.S)
        assert match, symbol
        raw = match[1].split(',')
        assert len(raw) == 11
        for got, wanted in zip(raw, expected):
            equal(polynomial(got), polynomial(wanted), 'printed_'+symbol+'_scalar')
        scalar_tables[symbol] = raw

    # Preserve the scope of the old general-data diagnostics explicitly.
    first = json.loads(GENERAL.read_text())['records'][0]
    assert first['source_zero_r_h_quadratic_zero'] is False
    assert first['source_zero_trace_equals_5r_plus_h'] is False
    report = {
        'status': 'PASS_F32_ACTUAL_TEX_FORMULA_COMPARISON',
        'program': bind(Path(__file__).resolve()),
        'proof': bind(PROOF), 'checker': bind(CHECKER), 'checker_output': bind(CHECKED),
        'general_producer_output': bind(GENERAL),
        'arithmetic': 'Independent integer Laurent dictionary parser; no SymPy or certificate helper imported; signed monomial inverses only.',
        'rows_read_from_tex': raw_rows,
        'auxiliary_polynomials_read_from_tex': {'P_4': p4match[1], 'P_6': p4match[2]},
        'determinants_read_from_tex': extracted_determinants,
        'roots_read_from_tex': extracted_roots,
        'scalar_tables_read_from_tex': scalar_tables,
        'checks': dict(COUNTS), 'total_exact_checks': sum(COUNTS.values()),
        'unused_general_diagnostics': {
            'source_zero_r_h_quadratic_zero': False,
            'source_zero_trace_equals_5r_plus_h': False,
            'scope': 'These are retained exploratory tests, not F.32 proof premises. The replay separately checks the actual r=1 core identity G_0=h^(-1)I_5.'},
        'all_source_files_unchanged': bind(PROOF)['sha256'] == EXPECTED_PROOF,
    }
    output = Path(__file__).with_name('printed_formula_crosscheck_output.json')
    assert not output.exists()
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status': report['status'], 'checks': report['checks'],
                      'total_exact_checks': report['total_exact_checks'],
                      'output': bind(output)}, indent=2))


if __name__ == '__main__':
    main()
