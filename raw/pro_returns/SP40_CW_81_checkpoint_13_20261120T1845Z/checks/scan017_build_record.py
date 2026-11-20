"""Source-only scan017 record clerk. No image bytes are opened.

Only readers explicitly released by root may be named in --released. Raw JSON
rows, original identities, literal TeX spans, processing records and textual
file hashes are retained. This script supplies no ink decision. Root alone
chooses final readings and approves the main record.
"""
from pathlib import Path
import argparse
import collections
import copy
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'out'
CHECKS = OUT / 'checks'
PACKET = ROOT / 'packets' / '017'
TEXT_SUFFIXES = {'.tex', '.md', '.txt', '.json', '.py'}


def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def rel(path):
    return str(path.relative_to(OUT)) if path.is_relative_to(OUT) else str(path.relative_to(ROOT))


def fingerprint(path):
    # This routine is called only for allow-listed textual suffixes.
    assert path.suffix in TEXT_SUFFIXES, path
    raw = path.read_bytes()
    text = raw.decode('utf-8')
    return {'path': rel(path), 'sha256': hashlib.sha256(raw).hexdigest(),
            'bytes': len(raw), 'lines': text.count('\n')}


def span(text, start, end, manifest, **extra):
    result = {'manifest': manifest, 'char_start': start, 'char_end': end,
              'line_start': text.count('\n', 0, start) + 1,
              'line_end': text.count('\n', 0, max(start, end - 1)) + 1,
              'excerpt': text[start:end], 'literal_sha256_utf8': sha(text[start:end])}
    result.update(extra)
    return result


def exact(text, literal, manifest, occurrence=0, **extra):
    starts = [m.start() for m in re.finditer(re.escape(literal), text)]
    if occurrence >= len(starts):
        raise ValueError(f'Literal unavailable: {manifest}: {literal!r}, occurrence {occurrence}')
    return span(text, starts[occurrence], starts[occurrence] + len(literal), manifest, **extra)


def json_spans(text):
    """Index exact JSON value substrings by JSON pointer without altering rows."""
    decoder = json.JSONDecoder()
    locations = {}

    def ws(pos):
        while pos < len(text) and text[pos].isspace():
            pos += 1
        return pos

    def walk(pos, pointer):
        start = pos = ws(pos)
        if text[pos] == '{':
            pos = ws(pos + 1)
            while text[pos] != '}':
                key, pos = decoder.raw_decode(text, pos)
                pos = ws(pos)
                assert text[pos] == ':'
                escaped = key.replace('~', '~0').replace('/', '~1')
                pos = walk(pos + 1, pointer + '/' + escaped)
                pos = ws(pos)
                if text[pos] == ',':
                    pos = ws(pos + 1)
                else:
                    assert text[pos] == '}'
            end = pos + 1
        elif text[pos] == '[':
            pos = ws(pos + 1)
            index = 0
            while text[pos] != ']':
                pos = walk(pos, pointer + '/' + str(index))
                index += 1
                pos = ws(pos)
                if text[pos] == ',':
                    pos = ws(pos + 1)
                else:
                    assert text[pos] == ']'
            end = pos + 1
        else:
            _, end = decoder.raw_decode(text, pos)
        locations[pointer] = (start, end)
        return end

    end = walk(0, '')
    assert not text[end:].strip()
    return locations


def raw_row(text, locations, pointer, manifest, value, row_id=None):
    start, end = locations[pointer]
    source = {'manifest': manifest, 'pointer': pointer}
    if row_id is not None:
        source['row_id'] = row_id
    return {'source': source, 'value': copy.deepcopy(value),
            'raw_source_text': text[start:end],
            'source_attachment': span(text, start, end, manifest, pointer=pointer)}


def esc(value):
    if value is None:
        return 'pending root'
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=False)
    return str(value).replace('|', '\\|').replace('\n', '<br>')


def table(headers, rows):
    return '| ' + ' | '.join(headers) + ' |\n| ' + ' | '.join('---' for _ in headers) + ' |\n' + ''.join('| ' + ' | '.join(esc(v) for v in row) + ' |\n' for row in rows)


ORIGINAL = {
    1: ['D01a', 'D01b', 'D01c'], 2: ['D02'], 3: ['D03'],
    4: ['D04a', 'D04b'], 5: ['D05'], 6: ['D06a', 'D06b'],
    7: ['D07a', 'D07b'], 8: ['D08a', 'D08b'], 9: ['D09'],
    10: ['D10'], 11: ['D11'], 12: ['D12'],
}

LOCI = [
    ('D01a', 'Opening cancelled subject E_i / Sigma_i'),
    ('D01b', 'Opening cancelled short verb est / soit'),
    ('D01c', 'Opening cancelled adjective rare / dense'),
    ('H01', 'Opening parenthesis: si / où'),
    ('H02', 'Opening cancelled sentence: terminal point'),
    ('H03', 'Raised on ait insertion state'),
    ('D02', 'Cancelled trouve above the equalities'),
    ('H04', 'First displayed equality: endpoint comma'),
    ('S01', 'First displayed Sigma_i-plus closure bar'),
    ('S02', 'Second displayed Sigma_i-minus closure bar'),
    ('G13', 'Second equality endpoint: literal point and period-role choice'),
    ('P01', 'Two upper equalities: successive rows versus H horizontal layout'),
    ('H05', "Prose before third equality: qu'on a / que"),
    ('S03', 'Third displayed Sigma12 closure bar'),
    ('D03', 'Third equality: first join physical cluster'),
    ('D03-shape', 'Third equality: individual curved return paths'),
    ('G02', 'Separator below third equality'),
    ('H06', 'Slanted note opening: introduire / introduisons'),
    ('D04a', 'Slanted-note partition letter Pi / pi'),
    ('D04b', 'Slanted-note E_j predecessor'),
    ('G12', 'Shape reported beside the slanted-note closing brace'),
    ('H-MARGIN-ILL', 'H trailing marginal ill placeholder: one parent'),
    ('N03', 'Considerons / Considérons: local accent'),
    ('G03', 'Upper inserted Pi_J: guide path'),
    ('D05', 'Cancelled wording after de X'),
    ('N04', 'First live definie after cancelled wording: accent'),
    ('D07a', 'First main-text E_j predecessor'),
    ('D06a', 'Cancelled short opening before intersection'),
    ('D06b', 'Live intersection: word, capital and state'),
    ('G04', 'Inserted ternaires Pi_j: guide path'),
    ('N05', 'Plural definies before later E_j: accent'),
    ('D07b', 'Later isolated E/membership glyph and state cluster'),
    ('H-LATER-ILL', 'H later isolated-sign ill placeholder: one parent'),
    ('G05', 'Small upper mark before alpha in coproduct display'),
    ('G05-index', 'C-reader dotless j node and upper-mark attachment component'),
    ('G11', 'Far-right pair of detached shapes'),
    ('G11-upper', 'Far-right pair: upper shape component'),
    ('G11-lower', 'Far-right pair: lower shape component'),
    ('N06', 'Final-paragraph definie: accent'),
    ('G06', 'Detached baseline point before first indexed union'),
    ('D08a', 'Inserted lower Pi_J: upper ring'),
    ('G07', 'Inserted lower Pi_J: guide path'),
    ('D11', 'Middle indexed bigcup: cup and transverse-mark cluster'),
    ('D11-shape', 'Middle indexed bigcup: individual literal paths'),
    ('D11-role', 'Middle indexed bigcup: local qualification of stroke role'),
    ('D08b', 'Binary partition Pi_J,j: upper ring'),
    ('G09', 'Inserted quantifier and induites: continuous guide/opening parenthesis'),
    ('G09-open', 'Induites guide: local opening-parenthesis interpretation component'),
    ('D12', 'U subscript: predecessor and complete-state cluster'),
    ('D12-final', 'U subscript: separately named final J component'),
    ('G10', 'Raised U expression and guide to sur/X gap'),
    ('G10-state', 'Raised U expression: insertion-state component'),
    ('D09', 'Final quantified g / j'),
    ('H07', 'Final extra closing parenthesis in H'),
    ('D10', 'Final Pour / Puis'),
    ('ARCHIVE', 'Archive numeral 16 comment and inventory coverage'),
]

# Canonical IDs are source-correspondence labels. They select no reader proposal.
A_MAP = {
    'A017-D01':['D01a'], 'A017-D02':['D01b'], 'A017-D03':['D01c'],
    'A017-D04':['H01'], 'A017-D05':['H02'], 'A017-D06':['H03'],
    'A017-D07':['D02'], 'A017-D08':['H04'], 'A017-D09':['H05'],
    'A017-D10':['D03','D03-shape'], 'A017-D11':['G02'],
    'A017-D12':['H06'], 'A017-D13':['D04a'],
    'A017-D14':['D04b','H-MARGIN-ILL'], 'A017-D15':['N03'],
    'A017-D16':['G03'], 'A017-D17':['D05'], 'A017-D18':['N04'],
    'A017-D19':['D07a'], 'A017-D20':['D06a'], 'A017-D21':['D06b'],
    'A017-D22':['G04'], 'A017-D23':['N05'],
    'A017-D24':['D07b','H-LATER-ILL'], 'A017-D25':['G05'],
    'A017-D26':['N06'], 'A017-D27':['G06'], 'A017-D28':['D08a'],
    'A017-D29':['G07'], 'A017-D30':['D11','D11-shape','D11-role'],
    'A017-D31':['D08b'], 'A017-D32':['G09','G09-open'],
    'A017-D33':['D12'], 'A017-D34':['D12-final'], 'A017-D35':['G10','G10-state'],
    'A017-D36':['D09'], 'A017-D37':['H07'], 'A017-D38':['D10'],
    'A017-D39':['G11','G11-upper','G11-lower'],
}
B_MAP = {k:[k] for k in [k for rows in ORIGINAL.values() for k in rows] + ['H01','H02','H03','H04','H05','H06','H07','N03','N04','N05','N06']}
B_MAP.update({'D03':['D03','D03-shape'], 'D07b':['D07b','H-LATER-ILL'],
              'D11':['D11','D11-shape','D11-role'], 'N01':['G02'],
              'N02':['G12','H-MARGIN-ILL'], 'N07':['G03'], 'N08':['G04'],
              'N09':['G06'], 'N10':['G07'], 'N11':['G09','G09-open'], 'N12':['G10','G10-state']})
C_MAP = {
    'D01':['D01a'], 'D02':['D01b'], 'D03':['D01c'], 'D04':['H02'],
    'D05':['H03'], 'D06':['H01'], 'D07':['D02'], 'D08':['H04'],
    'D09':['G13'], 'D10':['H05'], 'D11':['D03','D03-shape'],
    'D12':['G02'], 'D13':['H06'], 'D14':['D04a'],
    'D15':['D04b','H-MARGIN-ILL'], 'D16':['N03'], 'D17':['G03'],
    'D18':['D05'], 'D19':['D07a'], 'D20':['D06a'], 'D21':['D06b'],
    'D22':['G04'], 'D23':['D07b','H-LATER-ILL'],
    'D24':['G05','G05-index'], 'D25':['G11','G11-upper','G11-lower'],
    'D26':['D08a'], 'D27':['G07'], 'D28':['D11','D11-shape','D11-role'],
    'D29':['D08b'], 'D30':['G09'], 'D31':['G09-open'],
    'D32':['D12'], 'D33':['G10-state'], 'D34':['G10'],
    'D35':['D09'], 'D36':['H07'], 'D37':['D10'],
}
MAPS = {'A':A_MAP,'B':B_MAP,'C':C_MAP}

GRAPHICS = {
    'A': {'G01':['D03','D03-shape'],'G02':['G02'],'G03':['G03'],'G04':['G04'],
          'G05':['G05'],'G06':['G06'],'G07':['G07'],'G08':['D11','D11-shape','D11-role'],
          'G09':['G09'],'G10':['G10'],'G11':['G11','G11-upper','G11-lower']},
    'B': {'G01':['D03','D03-shape'],'G02':['G02'],'G03':['G12','H-MARGIN-ILL'],
          'G04':['G03'],'G05':['G04'],'G06':['G06'],'G07':['G07'],
          'G08':['D11','D11-shape','D11-role'],'G09':['G09'],'G10':['G10']},
    'C': {'M01':['G13'],'G01':['D03','D03-shape'],'G02':['G02'],
          'G03':['G03'],'G04':['G04'],'M03':['G05','G05-index'],
          'M02':['G11','G11-upper','G11-lower'],'G05':['G07'],
          'G06':['D11','D11-shape','D11-role'],'G07':['G09','G09-open'],'G08':['G10','G10-state']},
}

CHILDREN = {
    'D03-shape':'D03', 'G11-upper':'G11', 'G11-lower':'G11',
    'D11-shape':'D11', 'D11-role':'D11', 'D12-final':'D12',
    'G05-index':'G05', 'G09-open':'G09', 'G10-state':'G10',
}
ZERO_COUNT = set(CHILDREN) | {'S01','S02','S03','ARCHIVE'}

INVENTORY = [
    ('I01','text','heading','Cas particuliers'),
    ('I02','text','upper paragraph','Supposons que; signed Sigmas and complement'),
    ('I03','deletion','opening cancelled clause','subject, short verb, adjective, dans X.'),
    ('I04','insertion','above opening cancellation','on ait'),
    ('I05','deletion','above first display','Alors on trouve que'),
    ('I06','display','upper quarter','two closure equalities'),
    ('I39','drawing','second equality endpoint','point/period source representations'),
    ('I07','text','before third equality',"Alors je dis qu'on a"),
    ('I08','display','third equality','Sigma12 closure equality'),
    ('I26','drawing','first join in third equality','individual returned curved paths'),
    ('I27','drawing','below third equality','separator'),
    ('I09','margin note','slanted left note','partition note'),
    ('I10','deletion','inside marginal E_j','predecessor'),
    ('I28','drawing','beside marginal closing brace','reported short wedge; attachment pending'),
    ('I11','deletion','under divider','Supposons'),
    ('I12','text','middle line','Soit J subset I'),
    ('I13','text','main lower paragraph','Considérons/Considerons and partition prose'),
    ('I14','insertion','above first de X','Pi_J'),
    ('I29','drawing','under first Pi_J','insertion guide'),
    ('I15','deletion','after de X','cancelled wording'),
    ('I16','deletion','under first main E_j','predecessor'),
    ('I17','deletion','before intersection','short opening'),
    ('I18','insertion','following partitions','ternaires Pi_j'),
    ('I30','drawing','under ternaires Pi_j','bent guide'),
    ('I19','deletion','after later E_j','isolated sign/state'),
    ('I20','display','lower middle','indexed coproduct partition'),
    ('I31','drawing','before upper alpha','detached upper mark'),
    ('I32','drawing','far right below coproduct','paired detached shapes'),
    ('I21','text','final paragraph',"c'est aussi la partition through final word"),
    ('I33','drawing','before first lower bigcup','baseline point'),
    ('I22','insertion','above lower de','Pi_J with upper ring'),
    ('I34','drawing','under lower Pi_J','curved guide'),
    ('I35','drawing','middle indexed bigcup','cup and transverse stroke'),
    ('I23','insertion','above induites','(j in J)'),
    ('I36','drawing','over induites','continuous guide'),
    ('I24','insertion','above sur','U expression'),
    ('I25','deletion','U subscript','predecessor/complete state'),
    ('I37','drawing','under U expression','descending guide'),
    ('I38','text','lower-left foot','archive numeral 16 comment'),
]
PACKET_INV = {f'017.{i:02d}':[f'I{i:02d}'] for i in range(1,26)}
A_INV = dict(zip([f'017.A.{i:02d}' for i in range(1,38)], [[k] for k in [
    'I01','I02','I03','I04','I05','I06','I07','I08','I26','I27','I09','I10',
    'I11','I12','I13','I14','I29','I15','I16','I17','I18','I30','I19','I20',
    'I31','I21','I33','I22','I34','I35','I23','I36','I24','I25','I37','I38','I32']]))
B_INV = copy.deepcopy(PACKET_INV)
B_INV.update(dict(zip([f'017.B{i}' for i in range(26,37)], [[k] for k in ['I26','I27','I28','I29','I30','I33','I34','I35','I36','I37','I38']])))
C_INV = dict(zip([f'017.C.{i:02d}' for i in range(1,39)], [[k] for k in [
    'I01','I02','I03','I04','I05','I06','I39','I07','I08','I26','I27','I09',
    'I10','I11','I12','I13','I14','I29','I15','I16','I17','I18','I30','I19',
    'I20','I31','I32','I32','I21','I22','I34','I35','I23','I36','I24','I25','I37','I38']]))
INVENTORY_MAPS = {'A':A_INV,'B':B_INV,'C':C_INV}

WITNESSES = {
 'D01a':(r'\unsure{E_i|\Sigma_i}',r'\struck{$E_i$ soit rare dans $X$}'),
 'D01b':(r'\unsure{est}','soit'), 'D01c':(r'\unsure{rare|dense}','rare'),
 'H01':('(si','(où'), 'H02':('dans $X$.','dans $X$'),
 'H03':(r'\inserted{on ait}','on ait'), 'D02':(r'\unsure{trouve}','trouve'),
 'H04':(r'\overline{\Sigma_i^+} &= \Sigma_i^+\cup E_i\\',r'\overline{\Sigma_i^+} = \Sigma_i^+\cup E_i, \qquad'),
 'S01':(r'\overline{\Sigma_i^+}',r'\overline{\Sigma_i^+}'),
 'S02':(r'\overline{\Sigma_i^-}',r'\overline{\Sigma_i^-}'),
 'G13':(r'\Sigma_i^-\cup E_i .',r'\Sigma_i^-\cup E_i .'),
 'P01':(r'\begin{aligned}'+'\n'+r'\overline{\Sigma_i^+} &= \Sigma_i^+\cup E_i\\'+'\n'+r'\overline{\Sigma_i^-} &= \Sigma_i^-\cup E_i .'+'\n'+r'\end{aligned}',
         r'\overline{\Sigma_i^+} = \Sigma_i^+\cup E_i, \qquad'+'\n'+r'\overline{\Sigma_i^-} = \Sigma_i^-\cup E_i .'),
 'H05':("Alors je dis qu'on a",'Alors je dis que'),
 'S03':(r'\overline{\Sigma_{12}}',r'\overline{\Sigma_{12}}'),
 'D03':(r'\unsure{\cup|\amalg}',r'\Sigma_{12}\cup E_1\cup E_2'),
 'G02':(r'\noindent\rule{2.4cm}{0.3pt}\par',r'\struck{Supposons}'),
 'H06':('introduire','introduisons'),
 'D04a':(r'\unsure{\Pi|\pi}_j',r'\Pi_j = \{E_j'),
 'D04b':(r'\deleted{\unsure{\Sigma}}E_j',r'\Pi_j = \{E_j, \Sigma_j^+, \Sigma_j^-\}'),
 'G12':(r'\Sigma_j^-\}$}',r'\Sigma_j^-\}$ \ill{}'),
 'H-MARGIN-ILL':(r'\Sigma_j^-\}$}',r'\Sigma_j^-\}$ \ill{}'),
 'N03':('Considérons','Considérons'),
 'G03':(r'\inserted{$\Pi_J$} de',r'\add{$\Pi_J$} de'),
 'D05':(r'\deleted{\unsure{des parties|définie}}',r'\struck{définie}'),
 'N04':('définie par les','définie par les'),
 'D07a':(r'\deleted{\Sigma}E_j',r'définie par les $E_j$'),
 'D06a':(r'\deleted{\unsure{et}}',r'\struck{intersection} \add{intersection}'),
 'D06b':(r'\unsure{intersection}',r'\struck{intersection} \add{intersection}'),
 'G04':(r'\inserted{ternaires $\Pi_j$}',r'\add{ternaires $\Pi_j$}'),
 'N05':('définies','définies'),
 'D07b':(r'\deleted{$\unsure{E|\in}$}',r'définies par les $E_j$ \ill{}'),
 'H-LATER-ILL':(r'\deleted{$\unsure{E|\in}$}',r'définies par les $E_j$ \ill{}'),
 'G05':(r'\Sigma_j^\alpha',r'\Sigma_j^{\alpha}'),
 'G11':(r'\Sigma_j^\alpha',r'\Sigma_j^{\alpha}'),
 'N06':("c'est aussi la partition définie", "c'est aussi la partition définie"),
 'G06':(r'celle de $\displaystyle\bigcup_{j\in J}E_j$',r'celle de $\bigcup_{j\in J}E_j$'),
 'D08a':(r'\Pi_J^{\unsure{\circ|0}}',r'\Pi_J^0'),
 'G07':(r'\inserted{$\Pi_J^{\unsure{\circ|0}}$} de',r'\add{$\Pi_J^0$} de'),
 'D11':(r'\mathop{\unsure{\overline{\bigcup}|\bigcup}}\limits_{j\in J}',r'\add{$\Pi_J^0$} de $X\setminus\bigcup_{j\in J}E_j$'),
 'D08b':(r'\Pi_{J,j}^{\circ}',r'\Pi_{J,j}^0'),
 'G09':(r'\inserted{$(j\in J)$} induites',r'\add{($j\in J$)}'+'\n(induites'),
 'D12':(r'U_{\deleted{\unsure{J|j}}J}',r'U_J'),
 'G10':(r'\inserted{$U_{\deleted{\unsure{J|j}}J}={}$}',r'sur $U_J = X\setminus'),
 'D09':(r'\unsure{g|j}',r'($j\in J$)).'),
 'H07':(r'$(\unsure{g|j}\in J)$.',r'($j\in J$)).'),
 'D10':(r'\unsure{Pour|Puis}',r'\uncertain{Pour}'),
 'ARCHIVE':('% archive sheet number: 16',r'\page{16}'),
}
for child, parent in CHILDREN.items():
    WITNESSES[child] = WITNESSES[parent]


def make_decision(local_id, location, Ctex, Htex):
    C_literal, H_literal = WITNESSES[local_id]
    return {'id':'017-'+local_id, 'location':location, 'C':C_literal, 'H':H_literal,
            'final':None, 'readers':{}, 'reader_provenance':{}, 'reader_proposals':{},
            'reader_evidence':[], 'evidence':None, 'crop':None, 'available_crops':[],
            'full_scan_boxes':{}, 'confidence':None, 'confidence_status':'awaiting root ink decision',
            'kind':None, 'diff_C':False if local_id in ZERO_COUNT else None,
            'diff_H':False if local_id in ZERO_COUNT or local_id in {'D06b','D07b'} else None,
            'count_status':'noncount component/confirmation' if local_id in ZERO_COUNT else 'awaiting root physical-cluster count',
            'C_doubt_status':None, 'source_C_doubt_rows':[row for row, ids in ORIGINAL.items() if local_id in ids or CHILDREN.get(local_id) in ids],
            'marked_in_H':None, 'mathematical_consequence':None, 'main_approved':False,
            'log_decision':True, 'final_source_attachment':[],
            'witness_provenance':{'C':exact(Ctex,C_literal,'packet.C.tex'), 'H':exact(Htex,H_literal,'packet.H.tex')},
            'root_decision_log':'checks/scan017_main_decisions.md','root_decision_section':None,
            'root_source_attachment_status':'waiting for dedicated assembler current map and hash',
            'physical_count_parent': '017-'+CHILDREN[local_id] if local_id in CHILDREN else None,
            'H_count_parent':'017-D06a' if local_id=='D06b' else ('017-H-LATER-ILL' if local_id=='D07b' else None)}


def semantic_blocks(tex, role):
    """Disjoint full-source coverage with explicit local decision/inventory maps."""
    lower_pi = {'A':'G07','B':'G07','C':'G05'}[role]
    upper_guide = {'A':'G03','B':'G04','C':'G03'}[role]
    ternary = {'A':'G04','B':'G05','C':'G04'}[role]
    uguide = {'A':'G10','B':'G10','C':'G08'}[role]
    specs = [
        ('opening', 0, ['D01a','D01b','D01c','H01','H02','H03'], ['I01','I02','I03','I04']),
        ('upper_equalities', tex.index(r'\deleted{Alors'), ['D02','H04','S01','S02','G13','P01'], ['I05','I06','I39']),
        ('sigma12_equality', tex.index("Alors je dis qu'on a"), ['H05','S03','D03','D03-shape'], ['I07','I08','I26']),
        ('divider', tex.index('% G02:'), ['G02'], ['I27']),
        ('margin', tex.index('% slanted'), ['H06','D04a','D04b','G12','H-MARGIN-ILL'], ['I09','I10','I28']),
        ('soit', tex.index(r'\deleted{Supposons}'), [], ['I11','I12']),
        ('main_opening', tex.index('Consid'), ['N03','G03','D05','N04','D07a','D06a','D06b'], ['I13','I14','I29','I15','I16','I17']),
        ('ternary_insertion', tex.index('% '+ternary+':'), ['G04','N05','D07b','H-LATER-ILL'], ['I18','I30','I19','I13']),
        ('coproduct', tex.index(r'\['+'\nX=E_j'), ['G05','G05-index','G11','G11-upper','G11-lower'], ['I20','I31','I32']),
        ('lower_opening', tex.index("-- c'est aussi"), ['N06','G06'], ['I21','I33']),
        ('lower_pi_and_union', tex.index('% '+lower_pi+':'), ['D08a','G07','D11','D11-shape','D11-role'], ['I22','I34','I35']),
        ('binary_partition', tex.index('intersection des partitions binaires'), ['D08b','G09','G09-open'], ['I23','I36']),
        ('u_and_final_line', tex.index('% '+uguide+':'), ['D12','D12-final','G10','G10-state','D09','H07','D10'], ['I24','I25','I37','I21']),
        ('archive', tex.index('% archive sheet number: 16'), ['ARCHIVE'], ['I38']),
    ]
    starts=[s[1] for s in specs]
    assert starts==sorted(starts) and len(set(starts))==len(starts),(role,starts)
    result=[]
    for index,(label,start,loci,inventory) in enumerate(specs):
        end=starts[index+1] if index+1<len(starts) else len(tex)
        result.append({'reader':role,'block_index':index,'block_id':label,
                       'loci':['017-'+k for k in loci],'inventory':['017-'+k for k in inventory],
                       'attachment':span(tex,start,end,role+'.reading.tex'),
                       'purpose':'complete literal source coverage; direct span-to-locus map, without selected reading'})
    assert ''.join(b['attachment']['excerpt'] for b in result)==tex
    return result


def lexical_supplements(tex, role):
    """Exact source choices also capture report-silent word/mark alternatives."""
    rows=[]
    def add(literal, loci, scope, occurrence=0, report_silent=False):
        attachment=exact(tex,literal,role+'.reading.tex',occurrence,scope=scope)
        rows.append({'manifest':role+'.reading.tex','reader':role,'attachment':attachment,
                     'loci':['017-'+k for k in loci], 'report_silent_choice':report_silent,
                     'root_selection':None,'count_status':'source wording/component only; root physical count pending'})
    for local,literal in [('S01',r'\overline{\Sigma_i^+}'),('S02',r'\overline{\Sigma_i^-}'),('S03',r'\overline{\Sigma_{12}}')]:
        add(literal,[local],'literal current-reader closure bar; already in both witnesses')
    upper=re.search(r'\\begin\{aligned\}.*?\\end\{aligned\}',tex,re.S)
    assert upper
    rows.append({'manifest':role+'.reading.tex','reader':role,
                 'attachment':span(tex,upper.start(),upper.end(),role+'.reading.tex',scope='exact first/second equality layout'),
                 'loci':['017-P01'],'report_silent_choice':True,'root_selection':None,
                 'count_status':'source layout logged for root classification; first comma has separate H04 locus'})
    add('% archive sheet number: 16',['ARCHIVE'],'literal archive comment; no C text or H text change')
    add('Considerons' if role=='A' else r'Consid\unsure{e|é}rons',['N03'],'exact local first-word accent proposal')
    add(r'\deleted{définie}' if role=='C' else r'\deleted{definie}',['D05'],'cancelled word and its literal accent')
    add('définie par les' if role=='C' else 'definie par les',['N04'],'following live word and its literal accent',report_silent=role=='C')
    add('définies par les' if role=='C' else 'definies par les',['N05'],'plural word and its literal accent',report_silent=role=='C')
    add("c'est aussi la partition définie" if role=='C' else "c'est aussi la partition definie",['N06'],'final-paragraph word and its literal accent',report_silent=role=='C')
    add(r'\Pi_{J,j}^{\circ}',['D08b'],'second local circle/zero scope: plain first-candidate macro under recurring-doubt convention')
    add(r'U_{\unsure{\deleted{J}J|\deleted{j}J|J}}',['D12','D12-final'],'exact complete-state alternatives, including final J',report_silent=role!='A')
    if role in {'A','B'}:
        add(r'\Sigma_i^-\cup E_i .',['G13'],'ordinary period representation at second equality endpoint',report_silent=True)
    else:
        add(r'\mathpunct{\unsure{',['G13'],'local graphic/period-role qualification prefix')
    if role=='A':
        add(r'\Sigma_j^{\unsure{\prime|\cdot}\alpha}',['G05','G05-index'],'ordinary dotted j plus separately qualified prime/dot upper mark')
        add(r'\unsure{.}\,\bigcup_{j\in J}E_j',['G06'],'qualified point before first union')
        add(r'\mathop{\unsure{\vcenter{',['D11-role'],'middle-union graphic has explicit local unsure wrapper')
    elif role=='B':
        add(r'\Sigma_j^\alpha',['G05','G05-index'],'plain dotted j and alpha, with no separate upper-mark representation',report_silent=True)
        add(r'\Sigma_j^\alpha'+'\n'+r'\]'+'\n\n'+"-- c'est aussi la partition definie par celle de",['G11','G11-upper','G11-lower'],'complete display endpoint to following prose; no right-pair source component',report_silent=True)
        add(r'\mathop{\vcenter{',['D11-role'],'middle-union graphic has no local unsure wrapper',report_silent=True)
    else:
        add(r'\Sigma_{\jmath}^{\alpha}',['G05','G05-index'],'dotless j in text node; mark drawn by M03 with attachment uncertainty')
        add(r'celle de $\displaystyle\bigcup_{j\in J}E_j$',['G06'],'first-union context has no separately represented preceding point',report_silent=True)
        add(r'\mathop{\unsure{\begin{tikzpicture}',['D11-role'],'middle-union graphic has explicit local unsure wrapper')
    margin_match=re.search(r'\\margin\{.*?\\normalmarginpar',tex,re.S)
    assert margin_match
    rows.append({'manifest':role+'.reading.tex','reader':role,
                 'attachment':span(tex,margin_match.start(),margin_match.end(),role+'.reading.tex',scope='complete slanted-note source through closing wrapper'),
                 'loci':['017-H06','017-D04a','017-D04b','017-G12','017-H-MARGIN-ILL'],
                 'report_silent_choice':False,'root_selection':None,
                 'count_status':'exact margin and any detached-shape representation; one H placeholder target awaits root'})
    return rows


def graphic_commands(tex, role):
    marks = list(re.finditer(r'^% ((?:G|M)\d+)(?:[ab])?(?::| is\b| and\b)',tex,re.M))
    result=[]
    local_counts=collections.Counter()
    for match in re.finditer(r'\\(?:draw|fill)\b[^;]*;',tex,re.S):
        preceding = [g for g in marks if g.start() < match.start()]
        if not preceding:
            raise ValueError(f'Unmapped graphical command in {role}: {match.group()[:80]}')
        gid=preceding[-1].group(1)
        if gid not in GRAPHICS[role]:
            raise ValueError(f'Unmapped graphic label {role}:{gid}')
        local_counts[gid]+=1
        targets=GRAPHICS[role][gid]
        if (role=='A' and gid=='G11') or (role=='C' and gid=='M02'):
            targets=['G11','G11-upper' if local_counts[gid]==1 else 'G11-lower']
        result.append({'reader':role,'graphic_id':gid,'command_index':len(result)+1,
                       'component_index_in_graphic':local_counts[gid],
                       'loci':['017-'+x for x in targets],
                       'attachment':span(tex,match.start(),match.end(),f'{role}.reading.tex'),
                       'count_status':'literal path component; physical parent determines witness count'})
    return result


def assemble(released):
    if not released or any(role not in MAPS for role in released):
        raise ValueError('Explicit released-reader list is required.')
    if 'C' in released and not C_MAP:
        raise ValueError('C source map must be prepared after root explicitly releases C.')
    Ctex=(PACKET/'C.tex').read_text()
    Htex=(PACKET/'H.tex').read_text()
    metadata=json.loads((PACKET/'metadata.json').read_text())
    preparation=json.loads((CHECKS/'scan017_source_map.json').read_text())
    manifest={'scan':17,'scope':'source-only immutable textual files; no image bytes read',
              'files':{},'readers':{},'root_files':{},'frozen_reader_files':{},
              'released_readers':released,'pending_readers':[r for r in 'ABC' if r not in released]}
    for p in sorted(PACKET.iterdir()):
        if p.suffix in TEXT_SUFFIXES:
            manifest['files']['packet.'+p.name]=fingerprint(p)
    manifest['files']['PREAMBLE.tex']=fingerprint(OUT/'PREAMBLE.tex')
    for filename in ['scan017_source_map.json','scan017_witness_attention.md']:
        manifest['files']['prep.'+filename]=fingerprint(CHECKS/filename)
    manifest['files']['brief.v15']=fingerprint(OUT/'briefs/brief_v15_scan017.md')
    manifest['files']['clerk.script']=fingerprint(Path(__file__))
    attention=CHECKS/'scan017_source_attention.md'
    if attention.is_file():
        manifest['files']['qa.source_attention.md']=fingerprint(attention)
    reports={};texts={};indices={}
    for role in released:
        directory=OUT/'readers'/'017'/role
        for p in sorted(directory.iterdir()):
            if p.suffix in TEXT_SUFFIXES:
                key=role+'.'+p.name
                manifest['files'][key]=fingerprint(p)
                manifest['frozen_reader_files'][key]=manifest['files'][key]['sha256']
        text=(directory/'report.json').read_text()
        reports[role]=json.loads(text);texts[role]=text;indices[role]=json_spans(text)
        manifest['readers'][role]={k:reports[role].get(k) for k in ['scan','reader','start_utc','end_utc','model','effort','full_image_viewed','halves_viewed','complete_visual_read']}
        manifest['readers'][role]['files']=[k for k in manifest['files'] if k.startswith(role+'.')]

    decisions=[make_decision(i,location,Ctex,Htex) for i,location in LOCI]
    byid={d['id'][4:]:d for d in decisions}
    differences=[];doubts=[];inventory_rows=[];graphics=[];tex_paths=[];supplemental=[];source_blocks=[];processing=[];tex_edits=[]
    for role, report in reports.items():
        missing=set(d['id'] for d in report['differences'])-set(MAPS[role])
        assert not missing,(role,missing)
        for index,row in enumerate(report['differences']):
            pointer='/differences/'+str(index); targets=MAPS[role][row['id']]
            preserved=raw_row(texts[role],indices[role],pointer,role+'.report.json',row,row['id'])
            differences.append({'reader':role,'pointer':pointer,'source_id':row['id'],
                                'loci':['017-'+k for k in targets],**preserved})
            for key in targets:
                d=byid[key]
                d['reader_proposals'].setdefault(role,[]).append(copy.deepcopy(row))
                d['reader_provenance'].setdefault(role,[]).append(preserved['source'])
                d['readers'].setdefault(role,[]).append(row['reading'])
                d['reader_evidence'].append({'reader':role,'source_id':row['id'],'excerpt':row['evidence']})
                if row.get('readers_crop'):
                    crop=f'readers/017/{role}/'+row['readers_crop']
                    if crop not in d['available_crops']:d['available_crops'].append(crop)
                if row.get('bbox') is not None:d['full_scan_boxes'][role+':'+row['id']]=copy.deepcopy(row['bbox'])
        for index,row in enumerate(report['doubts']):
            ids=row.get('difference_ids') or [row.get('difference') or row.get('id')]
            targets=list(dict.fromkeys(k for rid in ids for k in MAPS[role][rid]))
            pointer='/doubts/'+str(index)
            doubts.append({'reader':role,'pointer':pointer,'source_difference_ids':ids,
                           'loci':['017-'+k for k in targets],
                           **raw_row(texts[role],indices[role],pointer,role+'.report.json',row,row.get('id'))})
        for index,row in enumerate(report['inventory']):
            targets=INVENTORY_MAPS[role][row['element']]
            pointer='/inventory/'+str(index)
            inventory_rows.append({'source':role+'.report.json','pointer':pointer,
                                   'source_id':row['element'],'targets':['017-'+k for k in targets],
                                   'raw':raw_row(texts[role],indices[role],pointer,role+'.report.json',row,row['element'])})
        for field in ['graphics','graphical_components']:
            for index,row in enumerate(report.get(field,[])):
                gid=row['id'];pointer='/'+field+'/'+str(index)
                graphics.append({'reader':role,'loci':['017-'+k for k in GRAPHICS[role][gid]],
                                 **raw_row(texts[role],indices[role],pointer,role+'.report.json',row,gid)})
        event_path='/notes/actual_computations' if role=='A' else '/processing_events'
        event_rows=report['notes'].get('actual_computations',[]) if role=='A' else report.get('processing_events',[])
        for index,row in enumerate(event_rows):
            processing.append({'reader':role,'rerun_by_clerk':False,
                               **raw_row(texts[role],indices[role],event_path+'/'+str(index),role+'.report.json',row,row.get('id'))})
        tex=(OUT/'readers'/'017'/role/'reading.tex').read_text()
        tex_paths.extend(graphic_commands(tex,role))
        blocks=semantic_blocks(tex,role)
        source_blocks.extend(blocks)
        supplemental.extend(lexical_supplements(tex,role))
        # Preserve every line-level source edit, including formatting and comments.
        # These source operations carry no automatic witness count.
        base=Ctex.splitlines(keepends=True); proposed=tex.splitlines(keepends=True)
        matcher=difflib.SequenceMatcher(a=base,b=proposed,autojunk=False)
        for tag,a0,a1,b0,b1 in matcher.get_opcodes():
            if tag=='equal':continue
            cs=sum(map(len,base[:a0]));ce=sum(map(len,base[:a1]))
            ps=sum(map(len,proposed[:b0]));pe=sum(map(len,proposed[:b1]))
            overlapping=[x for x in tex_paths if x['reader']==role and x['attachment']['char_start']<pe and x['attachment']['char_end']>ps]
            covered=[b for b in blocks if b['attachment']['char_start']<pe and b['attachment']['char_end']>ps]
            # A deletion has a zero-width reader interval; retain its insertion-point block.
            if not covered:
                covered=[b for b in blocks if b['attachment']['char_start']<=ps<=b['attachment']['char_end']][-1:]
            tex_edits.append({'reader':role,'operation':tag,
                              'C_attachment':span(Ctex,cs,ce,'packet.C.tex'),
                              'reader_attachment':span(tex,ps,pe,role+'.reading.tex'),
                              'loci':list(dict.fromkeys(k for b in covered for k in b['loci'])),
                              'inventory':list(dict.fromkeys(k for b in covered for k in b['inventory'])),
                              'source_blocks':[b['block_id'] for b in covered],
                              'graphical_paths':[{'graphic_id':p['graphic_id'],'component_index':p['component_index_in_graphic']} for p in overlapping],
                              'count_status':'exact textual source operation; no automatic witness count',
                              'mapping_status':'complete literal source-block and component mapping'})

    packet_inv_text=(PACKET/'C_inventory.json').read_text();packet_inv=json.loads(packet_inv_text);packet_inv_spans=json_spans(packet_inv_text)
    for source_choice in supplemental:
        role=source_choice['reader']
        for target in source_choice['loci']:
            byid[target[4:]].setdefault('reader_tex_proposals',{}).setdefault(role,[]).append(copy.deepcopy(source_choice))
    for index,row in enumerate(packet_inv):
        pointer='/'+str(index)
        inventory_rows.append({'source':'packet.C_inventory.json','pointer':pointer,'source_id':row['element'],
                               'targets':['017-'+k for k in PACKET_INV[row['element']]],
                               'raw':raw_row(packet_inv_text,packet_inv_spans,pointer,'packet.C_inventory.json',row,row['element'])})
    inventory=[]
    for key,kind,position,objects in INVENTORY:
        supporting=[r for r in inventory_rows if '017-'+key in r['targets']]
        inventory.append({'sheet_kind':'text','hand':None,'element':'017-'+key,'kind':kind,
                          'position':position,'first_words_or_objects':objects,'transcribed':None,
                          'selection_status':'source-union candidate; root final wording, hand and coverage pending',
                          'source_inventory':[r['raw']['source'] for r in supporting],
                          'source_rows':[copy.deepcopy(r['raw']) for r in supporting],
                          'source_element_ids':{source:[r['source_id'] for r in supporting if r['source']==source] for source in dict.fromkeys(r['source'] for r in supporting)},
                          'root_page_sources':[],'final_source_attachment_status':'waiting for current assembler map/hash'})

    actual=[]
    for source in preparation['categories']['Doubtful readings']:
        row=source['source_row'];local=ORIGINAL[row]
        components=['D12-final'] if row==12 else []
        maps={}
        for role in released:
            field=reports[role]['notes']['C_source_row_map'] if role=='A' else reports[role]['C_source_row_map']
            pointer=f'/notes/C_source_row_map/{row-1}' if role=='A' else f'/C_source_row_map/{row-1}'
            maps[role]=raw_row(texts[role],indices[role],pointer,role+'.report.json',field[row-1])
        actual.append({'source_row':row,'source_line':source['line'],'source_manifest':'packet.C_doubts.txt',
                       'source_literal':source['literal'],'local_loci':source['local_loci'],
                       'source_attachment':exact((PACKET/'C_doubts.txt').read_text(),source['literal'],'packet.C_doubts.txt'),
                       'primary_local_decision_ids':['017-'+k for k in local],
                       'component_decision_ids':['017-'+k for k in components],
                       'local_status_decision_ids':['017-'+k for k in local+components],
                       'decision_ids':['017-'+k for k in local+components],
                       'local_statuses':{'017-'+k:None for k in local+components},
                       'status':'awaiting root ink choices','reader_source_maps':maps})

    events=[]
    if 'B' in released:
        P03=reports['B']['processing_events'][2]
        assert P03['id']=='P03'
        events.append({'id':'SP40-017-SOURCE-COORDINATES','type':'computation or formal certificate',
                       'actor':'reader B; GPT-6 Astra Pro; effort not separately exposed',
                       'date':'2026-11-20','event_clock':None,'event_clock_note':'event clock not captured',
                       'statement_or_location':'Approximate placement of guide G05 in reader B reading.tex; canonical 017-G04',
                       'inputs':copy.deepcopy(P03['inputs']),'mapping':P03['mapping'],'result':copy.deepcopy(P03['result']),
                       'scope':P03['scope'],'rerun_by_clerk':False,'mathematical_theorem_check':False,
                       'source':raw_row(texts['B'],indices['B'],'/processing_events/2','B.report.json',P03,'P03'),
                       'qa_instruction':'Verify source linkage and copied inputs/map/results only. Do not recalculate.'})
        build=(OUT/'readers/017/B/build_record.py').read_text()
        build_line=next(line for line in build.splitlines() if "'id':'P03'" in line)
        crop_script=(OUT/'readers/017/B/make_crops.py').read_text()
        crop_line=next(line for line in crop_script.splitlines() if "'crop09_ternaires.png'" in line)
        crop_text=(OUT/'readers/017/B/crop_manifest.json').read_text()
        crop_data=json.loads(crop_text);crop_locations=json_spans(crop_text)
        assert crop_data['crops'][8]['path']=='crop09_ternaires.png'
        events[-1]['source_linkages']={
            'serialized_event_literal':exact(build,build_line,'B.build_record.py'),
            'fixed_crop_specification':exact(crop_script,crop_line,'B.make_crops.py'),
            'stored_crop_manifest':raw_row(crop_text,crop_locations,'/crops/8','B.crop_manifest.json',crop_data['crops'][8]),
            'manual_final_guide_paths':[copy.deepcopy(p['attachment']) for p in tex_paths if p['reader']=='B' and p['graphic_id']=='G05'],
            'scope':'Stored source linkage only. No arithmetic, image processing or path calculation rerun.'}

    record={'scan':17,'folder':metadata['folder'],'their_page':metadata['their_page'],
            'hua_has':metadata['hua_has'],'filename':'J81-02_81_scan017.tex','brief_version':'v15',
            'main_adjudicated':False,'decisions':decisions,'doubts':[], 'inventory':inventory,
            'notes':"The supplied sources title the page Cas particuliers. They write `\\overline{\\Sigma_i^+}=\\Sigma_i^+\\cup E_i`, `\\overline{\\Sigma_i^-}=\\Sigma_i^-\\cup E_i`, the Sigma12 closure equality with its locally disputed first join, `I=J\\amalg\\{i\\}`, and the indexed coproduct partition `X=E_j\\amalg\\coprod_{\\alpha\\in\\pi_0(X\\setminus E_j)}\\Sigma_j^\\alpha`. The author's words include Supposons que, Alors je dis, and c'est aussi la partition. C retains the written complement `X\\setminus\\Sigma_i`; H prints that complement and adds its editorial sic proposal. The three Sigma closure bars are already in C and H and await root confirmation under S SA01-K81-06. The middle indexed union's transverse mark remains its separate original C doubt row11. These are exact source-formula and wording reports; no proof is claimed. Final ink readings and final notes await root selection.",
            'abbreviations':[{'form':'comp. conn.','possible_expansion':'composantes connexes','source_literal':preparation['categories']['Abbreviations'][0]['literal']}],
            'check_events':events,'processing_provenance':processing,
            'workflow_note':'Source-only clerk. Only explicitly released reader text files and the permitted packet/preparation sources were read. No image bytes, compiler, renderer, OCR, external research, image-comparison or mathematical/geometry computation was used. Recorded prior reader operations are copied without rerun. Root alone chooses ink and approves/commits.',
            'source_counts':{'reader_differences':{r:len(x['differences']) for r,x in reports.items()},
                             'reader_inventory':{r:len(x['inventory']) for r,x in reports.items()},
                             'reader_remaining_doubt_rows':{r:len(x['doubts']) for r,x in reports.items()},
                             'C_inventory':len(packet_inv),'C_doubt_rows':12,'C_primary_local_doubts':18,
                             'source_inventory_rows':len(inventory_rows),'union_inventory_elements':len(inventory),
                             'union_decision_entries':len(decisions),'literal_graphic_path_commands':dict(collections.Counter(x['reader'] for x in tex_paths)),
                             'reader_original_C_named_parts':{r:sum(len(row['parts'] if 'parts' in row else row['local_parts']) for row in (x['notes']['C_source_row_map'] if r=='A' else x['C_source_row_map'])) for r,x in reports.items()},
                             'S_physical_body_overbars':{'C':3,'H':3}},
            'source_difference_crosswalk':differences,'source_graphical_component_crosswalk':graphics,
            'source_graphical_path_crosswalk':tex_paths,'source_supplemental_tex_crosswalk':supplemental,
            'source_tex_edit_crosswalk':tex_edits,
            'source_complete_tex_blocks':source_blocks,'source_doubt_crosswalk':doubts,
            'source_inventory_crosswalk':inventory_rows,'actual_C_doubt_map':actual,
            'source_manifest':'checks/scan017_reader_fingerprints.json','root_decision_log':'checks/scan017_main_decisions.md',
            'root_actions_pending':(['Complete source map after root releases every reader.'] if len(released)<3 else [])+['Apply root ink decisions only after supplied choices.','Attach the dedicated assembler exact current final-source map and hash.','Root approval and commit.'],
            'source_categories':copy.deepcopy(preparation['categories']),
            'reader_notes':{r:copy.deepcopy(x['notes']) for r,x in reports.items()},
            'reader_notation':{r:copy.deepcopy(x['notation']) for r,x in reports.items()},
            'reader_raw_check_events':{r:copy.deepcopy(x['check_events']) for r,x in reports.items()},
            'released_readers':released,'pending_readers':[r for r in 'ABC' if r not in released],
            'mechanical_verification':{'status':'source-only scaffold; final verification pending',
                                       'no_image_viewed_by_clerk':True,'numerical_geometry_checks_by_clerk':0,
                                       'mathematical_theorem_checks':0,'raw_difference_rows_preserved':len(differences),
                                       'raw_doubt_rows_preserved':len(doubts),'raw_inventory_rows_preserved':len(inventory_rows),
                                       'recorded_prior_coordinate_event_rerun':False},
            'counts':{'status':'root ink and physical-cluster selection pending','C':None,'H':None,
                      'remaining_doubt_loci':None,'inventory_elements':None},
            'C_doubt_resolution_counts':{'actual_rows':12,'physical_primary_clusters':18,'resolved_local':None,
                                          'retained_local':None,'pending_primary_local':18,
                                          'scope_note':"A names nineteen components: R12 final J is a noncount child of its predecessor/state cluster. B names nineteen parts: its two R12 descriptions share D12. C names eighteen primary parts. The twelve original source identities and eighteen primary loci are preserved."},
            'source_attachment_status':'pending dedicated assembler current map/hash',
            'source_counting_constraints':[
                {'parent':'017-H-MARGIN-ILL','witness':'H','count':None,'children':['017-D04b','017-G12'],
                 'status':'A and B assign the marginal placeholder differently; root must select its physical attachment before any count.'},
                {'parent':'017-H-LATER-ILL','witness':'H','count':None,'children':['017-D07b'],'local_children_H_count':False},
                {'parent':'017-D06a','witness':'H','count':None,'children':['017-D06b'],'local_children_H_count':False},
                {'parents':['017-D03','017-D11','017-D12','017-G11'],'scope':'Each physical glyph/state/graphic cluster counts at most once per witness; named components retain log_decision true with false count flags.'}],
            'source_macro_mappings':[
                {'C':r'\uline{Cas particuliers}','H':r'\emph{Cas particuliers}','locus':'heading span Cas particuliers','count':False,'basis':'same named span and supplied H emphasis convention; ink width/underline selection pending root'},
                {'C':r'I=J\amalg\{i\}','H':r'I=J\sqcup\{i\}','locus':'Soit line square join','count':False,'basis':'explicit local macro substitution amalg -> sqcup; A and B reports map both to the individually inspected square form'},
                {'C':r'X=E_j\amalg\coprod','H':r'X = E_j \sqcup \coprod','locus':'coproduct display first join','count':False,'basis':'explicit local macro substitution amalg -> sqcup; A and B reports map both to the individually inspected square form'}]}

    union='# Scan017 source union — no ink choices\n\n'
    union+='Released readers: '+', '.join(released)+'. Pending readers: '+(', '.join(record['pending_readers']) or 'none')+'. Every final selection and witness total remains pending root. No image bytes were read by the clerk.\n\n'
    union+='## Original C identities and reader granularity\n\n'+table(['Original row','Packet primary loci','Reader maps'],[(x['source_row'],x['primary_local_decision_ids'],{r:v['value'] for r,v in x['reader_source_maps'].items()}) for x in actual])
    union+='\nA names the final J separately within R12; B names predecessor and complete state separately under its one D12. C preserves eighteen named primary parts. Those maps retain the same twelve original source rows and eighteen primary loci.\n\n'
    union+='## Decisions awaiting root\n\n'+table(['ID','Location','C literal','H literal']+released+['Root'],[(d['id'],d['location'],d['C'],d['H'],*[d['readers'].get(r,[]) or ['TeX: '+x['attachment']['excerpt'] for x in d.get('reader_tex_proposals',{}).get(r,[])] for r in released],d['final']) for d in decisions])
    union+='\n## Source totals\n\n```json\n'+json.dumps(record['source_counts'],ensure_ascii=False,indent=2)+'\n```\n\n'
    union+='## Count and attachment questions\n\n'
    union+="The one H marginal ill placeholder has competing source attachments: A associates it with the uncertain marginal predecessor; B associates it with the separate reported wedge. Both raw claims survive. Root supplies the actual target and count. H's later ill placeholder is one parent for the later glyph/state cluster; the H intersection state cluster likewise has one count parent. All local children stay in the log. The three Sigma bars already occur in C/H and have no current-witness omission count. The middle union transverse mark has its own row11.\n\n"
    union+='## Recorded reader computation\n\n'
    union+='B P03 is preserved as one SP40-017-SOURCE-COORDINATES event, with exact inputs, map and recorded outputs. It was not rerun. All image processing, coordinate declarations and structural-check records remain separate provenance. The event gives the restricted guide-placement scope and makes no theorem claim.\n\n'
    union+='## Literal source preservation\n\n'
    union+='The JSON draft preserves every released raw difference, doubt and inventory row as its original object plus verbatim JSON substring and source offsets. Every draw/fill path has its literal command span and source component index. Disjoint full TeX blocks cover every character and map all lexical content, state wrappers, guide placement and line-edit spans to local decisions and inventory. Additional exact snippets preserve report-silent accents, the second ring, the C-reader dotless j node, the B-reader unqualified middle-union graphic, and ordinary-point or absent-mark representations. Final selected-source attachments await the dedicated assembler current map and hash.\n'
    (CHECKS/'scan017_record_draft.json').write_text(json_text(record))
    (CHECKS/'scan017_union.md').write_text(union)
    (CHECKS/'scan017_reader_fingerprints.json').write_text(json_text(manifest))
    print(json_text({'released':released,'pending':record['pending_readers'],'decisions':len(decisions),
                     'differences':len(differences),'doubts':len(doubts),'inventory_rows':len(inventory_rows),
                     'union_inventory':len(inventory),'path_commands':record['source_counts']['literal_graphic_path_commands'],
                     'main_adjudicated':False,'ink_choices':0}))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--released',nargs='+',required=True,choices=['A','B','C'])
    args=parser.parse_args()
    assemble(args.released)
