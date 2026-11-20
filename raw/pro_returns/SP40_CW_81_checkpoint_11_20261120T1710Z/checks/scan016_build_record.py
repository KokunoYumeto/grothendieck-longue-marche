"""Source-only scan016 record assembly. No image access or reading adjudication.

Reads only explicitly released reader text files. Produces the three clerk
outputs under checks; root alone chooses ink readings and commits pages.
"""
from pathlib import Path
import argparse, collections, copy, hashlib, json, re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'out'
PACKET = ROOT / 'packets' / '016'
CHECKS = OUT / 'checks'


def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def read_json(path):
    return json.loads(path.read_text())


def fingerprint(path):
    raw = path.read_bytes()
    return {'path': str(path.relative_to(OUT)) if path.is_relative_to(OUT) else str(path.relative_to(ROOT)),
            'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw),
            'lines': raw.decode().count('\n')}


def escape(value):
    if value is None:
        return 'pending'
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=False)
    return str(value).replace('|', '\\|').replace('\n', '<br>')


def table(headers, rows):
    return '| ' + ' | '.join(headers) + ' |\n| ' + ' | '.join('---' for _ in headers) + ' |\n' + ''.join('| ' + ' | '.join(escape(v) for v in row) + ' |\n' for row in rows)


def exact_span(text, literal, occurrence=0, manifest=None):
    starts = [m.start() for m in re.finditer(re.escape(literal), text)]
    if occurrence >= len(starts):
        raise ValueError(f'Exact source literal unavailable: {manifest}: {literal!r} occurrence {occurrence}')
    start = starts[occurrence]
    end = start + len(literal)
    return {'manifest': manifest, 'char_start': start, 'char_end': end,
            'line_start': text.count('\n', 0, start) + 1,
            'line_end': text.count('\n', 0, max(start, end - 1)) + 1,
            'excerpt': literal}


def line_span(text, first, last, manifest):
    lines = text.splitlines(keepends=True)
    start = sum(len(s) for s in lines[:first-1])
    end = sum(len(s) for s in lines[:last])
    return {'manifest': manifest, 'char_start': start, 'char_end': end,
            'line_start': first, 'line_end': last, 'excerpt': text[start:end]}


def crop_path(role, path):
    if not path:
        return None
    return path if str(path).startswith('readers/') else f'readers/016/{role}/{path}'


ORIGINAL = {
 1: ['D01'], 2: ['D02'], 3: ['D03'], 4: ['D04a','D04b'], 5: ['D05'],
 6: ['D06'], 7: ['D07a','D07b','D07c','D07d'], 8: ['D08'], 9: ['D09'],
 10: ['D10a','D10b'], 11: ['D11'], 12: ['D12a','D12b'], 13: ['D13'],
}
JOIN_COMPONENTS = {'D12a':['D12a-old','D12a-live'], 'D12b':['D12b-old','D12b-live']}

# Canonical identifiers express source correspondences only. Reader proposals
# remain independent and no proposal becomes a root reading automatically.
B_MAP = {
 'B016-D01':['D01'], 'B016-D02':['D02'], 'B016-D03':['D03'],
 'B016-D04':['D04a'], 'B016-D05':['D04b'], 'B016-D06':['D05'],
 'B016-D07':['N01b'], 'B016-D08':['D10a'], 'B016-D09':['D10b'],
 'B016-D10':['D06'], 'B016-D11':['D07a'], 'B016-D12':['D07b'],
 'B016-D13':['D07c'], 'B016-D14':['D07d'], 'B016-D15':['D08'],
 'B016-D16':['D09'], 'B016-D17':['D11'],
 'B016-D18':['D12a','D12a-old'], 'B016-D19':['D12a','D12a-live'],
 'B016-D20':['D12b','D12b-old'], 'B016-D21':['D12b','D12b-live'],
 'B016-D22':['D13'], 'B016-D23':['N05'], 'B016-D24':['N02'],
 'B016-D25':['N03'], 'B016-D26':['N04'], 'B016-D27':['G01'],
 'B016-D28':['G02','G03','G02-return'], 'B016-D29':['G08'],
 'B016-D30':['G05'], 'B016-D31':['G06'], 'B016-D32':['G07'],
}
C_MAP = {k:[k] for k in ['D01','D02','D03','D04a','D04b','D05','D06','D07a','D07b','D07c','D07d','D08','D09','D10a','D10b','D11','D13','N01a','N01b','N02','N03','N04','G01','G03','G04','G05','G06','G07','G08','G09','BR01','BR02']}
C_MAP.update({'D12a-old':['D12a','D12a-old'], 'D12a-live':['D12a','D12a-live'],
              'D12b-old':['D12b','D12b-old'], 'D12b-live':['D12b','D12b-live'],
              'G02':['G02','G02-return'], 'G10':['D13-shape'],
              'BR01':['BR01','BR-PAIR'],'BR02':['BR02','BR-PAIR']})
A_MAP = {('A016-'+k):[k] for k in ['D01','D02','D03','D04a','D04b','D05','D06','D07a','D07b','D07c','D07d','D08','D09','D10a','D10b','D11','D13']}
A_MAP.update({'A016-D12a':['D12a','D12a-old','D12a-live'], 'A016-D12b':['D12b','D12b-old','D12b-live'],
 'A016-W20':['N01b'], 'A016-W21':['N05'], 'A016-W22':['N02'], 'A016-W23':['N03'], 'A016-W24':['N04'],
 'A016-G25':['G01'], 'A016-G26':['G02','G02-return'], 'A016-G27':['G03'], 'A016-G28':['G04'],
 'A016-G29':['G06'], 'A016-G30':['G07'], 'A016-G31':['G08']})

LOCI = [
 ('D01','Opening union: predecessor beneath the second Sigma subscript 1'),
 ('D02','Opening verb: cancelled predecessor and live est cluster'),
 ('D03','Opening right: connexe'),
 ('D04a','Right insertion: separator between X and E'),
 ('D04b','Right insertion: subscript 2 at the cut edge'),
 ('D05','Opening third line: cancelled c\'est'),
 ('D06','Opening conclusion: cqfd/qfd'),
 ('D07a','First partition: E predecessor beneath first Sigma'),
 ('D07b','Five-term partition: E predecessor beneath Sigma12'),
 ('D07c','Lower Car argument: E predecessor beneath barred Sigma12'),
 ('D07d','Lower Car argument: Sigma predecessor beneath E1'),
 ('D08','Initial Dans: predecessor beneath D'),
 ('D09','Lower raised insertion: conclurait'),
 ('D10a','Opening sign after egale/egal: à or colon'),
 ('D10b','Opening connective before final inclusion: donc/d\'où'),
 ('D11','Lower raised insertion: en/on'),
 ('D12a','First amended join under final long overbar: physical cluster'),
 ('D12a-old','First final join: square-join predecessor component'),
 ('D12a-live','First final join: live cup/square-join component'),
 ('D12b','Second amended join under final long overbar: physical cluster'),
 ('D12b-old','Second final join: square-join predecessor component'),
 ('D12b-live','Second final join: live cup/square-join component'),
 ('D13','Final right edge: closing-bracket cluster'),
 ('D13-shape','Final closing-bracket cluster: visible return paths'),
 ('N01a','Opening egale/egal: accent'),
 ('N01b','Opening egale/egal: final e'),
 ('N02','Definition: def/déf accent'),
 ('N03','Definition: terminal period'),
 ('N04','After ouverts: endpoint comma'),
 ('N05','First partition: endpoint comma'),
 ('G01','Guide beneath inserted la comp. conn.'),
 ('G02','Lower curved guide beneath right inserted phrase'),
 ('G03','Rule beneath connexe / above right inserted phrase'),
 ('G02-return','Detached return below the lower right guide / following comma'),
 ('G04','Detached point above/right of central Sigma12'),
 ('G05','Detached point below/right of avec'),
 ('G06','Two detached points beside the third closure row'),
 ('G07','Detached point above the second nonempty-intersection formula'),
 ('G08','Cancellation path across lower alors expression'),
 ('G09','Brace beneath first component closure: contour'),
 ('BR-PAIR','Five-term partition: H brace-pair representation parent'),
 ('BR01','Five-term partition: upper brace contour and endpoint'),
 ('BR02','Five-term partition: lower brace contour and endpoint'),
 ('P01','Two partition equations: successive physical rows'),
]

INVENTORY = [
 ('I01','text','opening four lines','et par suite … qfd|cqfd'),
 ('I02','deletion','opening second Sigma subscript','predecessor beneath live 1'),
 ('I03','deletion','opening verb cluster','cancelled sera/sont and live est'),
 ('I04','drawing','opening right, under connexe and above insertion','separate upper rule'),
 ('I05','insertion','above contenant … Sigma2 minus','la comp. conn.'),
 ('I06','drawing','beneath preceding insertion','bent insertion guide'),
 ('I07','insertion','right edge after Sigma2 minus','de X / or setminus E2'),
 ('I08','drawing','beneath right insertion','lower curved guide'),
 ('I09','drawing','below left end of right insertion guide','detached return / following comma'),
 ('I10','deletion','opening third line after donc','qualified c\'est'),
 ('I11','text','opening conclusion on separate physical line','qfd|cqfd'),
 ('I12','text','paragraph before paired partitions','L\'intersection des deux partitions'),
 ('I13','display','upper middle, two physical rows','two partitions of X'),
 ('I14','deletion','first Sigma in first partition','E predecessor'),
 ('I15','text','before five-term partition','de X est'),
 ('I16','display','central five-term partition','X = Sigma1+ amalg E1 amalg Sigma12 amalg E2 amalg Sigma2+'),
 ('I17','drawing','above five-term partition','upper brace and Sigma2 minus label'),
 ('I18','drawing','below five-term partition','lower brace and Sigma1 minus label'),
 ('I19','deletion','central Sigma12','E predecessor'),
 ('I20','drawing','above/right of central Sigma12','detached point'),
 ('I21','text','left of definition','avec'),
 ('I22','display','definition below braces','Sigma12 def= Sigma1 minus cap Sigma2 minus'),
 ('I23','drawing','below/right of avec','detached point'),
 ('I24','text','next two physical prose lines','Dans cette partition … sont fermés, et on a'),
 ('I25','deletion','initial D of Dans','O predecessor'),
 ('I26','display','first closure row','Sigma1 plus, strict inclusion, closure, inclusion'),
 ('I27','display','second closure row','closure Sigma12 and full inclusion chain'),
 ('I28','display','third closure row','Sigma2 plus, strict inclusion, closure, inclusion'),
 ('I29','drawing','right blank margin beside third closure row','two detached point contours'),
 ('I30','text','following paragraph','Notons aussi que'),
 ('I31','display','lower quarter','two nonempty-intersection expressions'),
 ('I32','drawing','above second nonempty-intersection formula','detached point'),
 ('I33','text','last argument, around cancellation','Car si on avait p. ex. … on … live continuation'),
 ('I34','deletion','first expression in lower hypothesis','E beneath barred Sigma12'),
 ('I35','deletion','E1 after cap in lower hypothesis','Sigma predecessor'),
 ('I36','insertion','above cancelled lower phrase','en/on conclurait'),
 ('I37','deletion','lower cancelled line','alors Sigma12 amalg E2 amalg Sigma2'),
 ('I38','drawing','through lower cancelled line','single curved cancellation path'),
 ('I47','display','live continuation beside lower cancellation','closure Sigma1 minus cap E1 = empty, comma'),
 ('I39','display','foot, bracketed line','[ car closure Sigma1 minus = …'),
 ('I40','deletion','first join under final long bar','recognizable square-form component; cancelled/live replacement state qualified, deleted amalg plus cup | live amalg'),
 ('I41','deletion','second join under final long bar','recognizable square-form component; cancelled/live replacement state qualified, deleted amalg plus cup | live amalg'),
 ('I42','drawing','foot right edge','qualified closing-bracket returns'),
 ('I43','drawing','below first component closure in final display','underbrace contour'),
 ('I44','insertion','below preceding underbrace','subset Sigma2 plus cup E2'),
 ('I45','text','foot left','ce qui n\'est pas.'),
 ('I46','text','lower-left archive numeral','15, archive-number comment only'),
]
PACKET_INVENTORY_MAP = {
 '016.01':['I01'], '016.02':['I02'], '016.03':['I03'], '016.04':['I05'],
 '016.05':['I07'], '016.06':['I10'], '016.07':['I11'], '016.08':['I12'],
 '016.09':['I13'], '016.10':['I14'], '016.11':['I15'],
 '016.12':['I16','I17','I18'], '016.13':['I19'], '016.14':['I21'],
 '016.15':['I22'], '016.16':['I24'], '016.17':['I25'], '016.18':['I26'],
 '016.19':['I27'], '016.20':['I28'], '016.21':['I30'], '016.22':['I31'],
 '016.23':['I33'], '016.24':['I34'], '016.25':['I35'], '016.26':['I37'],
 '016.27':['I36'], '016.28':['I39'], '016.29':['I40'], '016.30':['I41'],
 '016.31':['I44'], '016.32':['I45'],
}
B_INVENTORY_MAP = dict(zip([f'B016.I{i:02d}' for i in range(1,40)], [
 ['I01'],['I02'],['I03'],['I05'],['I06'],['I07'],['I04','I08','I09'],['I10'],['I11'],['I12'],
 ['I13'],['I14'],['I15'],['I16','I17','I18'],['I19'],['I21'],['I23'],['I22'],['I24'],['I25'],
 ['I26'],['I27'],['I28'],['I29'],['I30'],['I32'],['I31'],['I33'],['I34'],['I35'],
 ['I36'],['I37'],['I38'],['I39','I42'],['I40'],['I41'],['I43','I44'],['I45'],['I46']
]))
C_INVENTORY_MAP = copy.deepcopy(PACKET_INVENTORY_MAP)
C_INVENTORY_MAP.update({
 '016.C.G01':['I06'], '016.C.G02':['I08','I09'], '016.C.G03':['I04'],
 '016.C.G04':['I20'], '016.C.G05':['I23'], '016.C.G06':['I29'],
 '016.C.G07':['I32'], '016.C.G08':['I38'], '016.C.G09':['I43'],
 '016.C.G10':['I42'], '016.C.archive':['I46'],
})
A_INVENTORY_MAP = dict(zip([f'A016.{i:02d}' for i in range(1,42)], [
 ['I01','I11'],['I02'],['I03'],['I05'],['I06'],['I07'],['I08','I09'],['I04'],['I10'],['I12'],
 ['I13'],['I14'],['I15'],['I16'],['I17','I18'],['I19'],['I20'],['I21'],['I22'],['I24'],
 ['I25'],['I26'],['I27'],['I28'],['I29'],['I30'],['I31'],['I32'],['I33','I45'],['I34'],
 ['I35'],['I37'],['I38'],['I36'],['I47'],['I39','I42'],['I40'],['I41'],['I43','I44'],['I45'],['I46']
]))
B_INVENTORY_MAP['B016.I28'] = ['I33','I47']

# Exact witness literals with occurrence indexes; absence entries retain a
# surrounding source span rather than claiming that a token was present.
WITNESSES = {
 'D01': (r'\Sigma_{\deleted{\unsure{2}}1}^+', r'\Sigma_1^+'),
 'D02': (r'\deleted{\unsure{sera|sont}} est', 'serait'),
 'D03': (r'\unsure{connexe}', 'connexe'),
 'D04a': (r'X\unsure{/|\setminus}E_{\unsure{2}}', (r'X\setminus E_2',1)),
 'D04b': (r'E_{\unsure{2}}', (r'E_2',1)),
 'D05': (r"\deleted{\unsure{c'est}}", r'\struck{\ill{}}'),
 'D06': (r'\unsure{cqfd|qfd}', 'cqfd'),
 'D07a': (r'\deleted{\unsure{E}}\Sigma_1^+', r'X = \Sigma_1^+\sqcup E_1\sqcup\Sigma_1^-,'),
 'D07b': ((r'\deleted{\unsure{E}}\Sigma_{12}',0), r'X = \Sigma_1^+\sqcup E_1\sqcup\Sigma_{12}\sqcup E_2\sqcup\Sigma_2^+'),
 'D07c': (r'\overline{\deleted{\unsure{E}}\Sigma_{12}}', (r'\overline{\Sigma_{12}}',3)),
 'D07d': (r'\deleted{\unsure{\Sigma}}E_1', r'\overline{\Sigma_{12}}\cap E_1=\emptyset'),
 'D08': (r'\deleted{\unsure{O}}Dans', 'Dans'),
 'D09': (r'\unsure{conclurait}', 'considérant'),
 'D10a': (r'\unsure{à|:}', 'égal à'),
 'D10b': (r"\unsure{donc|d'où}", 'donc\n$\\Sigma_1^+'),
 'D11': (r'\unsure{en|on}', r'\add{en considérant}'),
 'D12a': (r'\deleted{\unsure{\amalg}}\unsure{\cup|\amalg}', r'\overline{\Sigma_2^+\sqcup E_2\sqcup\Sigma_{12}}'),
 'D12a-old': ((r'\deleted{\unsure{\amalg}}',0), r'\overline{\Sigma_2^+\sqcup E_2\sqcup\Sigma_{12}}'),
 'D12a-live': (r'\unsure{\cup|\amalg}', r'\overline{\Sigma_2^+\sqcup E_2\sqcup\Sigma_{12}}'),
 'D12b': (r'\deleted{\unsure{\amalg}}\cup\Sigma_{12}', r'\overline{\Sigma_2^+\sqcup E_2\sqcup\Sigma_{12}}'),
 'D12b-old': ((r'\deleted{\unsure{\amalg}}',1), r'\overline{\Sigma_2^+\sqcup E_2\sqcup\Sigma_{12}}'),
 'D12b-live': (r'\deleted{\unsure{\amalg}}\cup\Sigma_{12}', r'\overline{\Sigma_2^+\sqcup E_2\sqcup\Sigma_{12}}'),
 'D13': (r'\unsure{\big]}', r'\Sigma_1^-\cup\overline{\Sigma_{12}}'),
 'D13-shape': (r'\unsure{\big]}', r'\Sigma_1^-\cup\overline{\Sigma_{12}}'),
 'N01a': ('égale', 'égal'), 'N01b': ('égale', 'égal'),
 'N02': (r'\overset{\text{def}}{=}', r'\overset{\mathrm{déf}}{=}'),
 'N03': (r'\Sigma_{12}\overset{\text{def}}{=}\Sigma_1^-\cap\Sigma_2^-', r'\Sigma_{12} \overset{\mathrm{déf}}{=} \Sigma_1^-\cap\Sigma_2^- .'),
 'N04': ('sont ouverts $E_1,E_2$', 'sont ouverts,'),
 'N05': (r'X&=\deleted{\unsure{E}}\Sigma_1^+\amalg E_1\amalg\Sigma_1^-', r'X = \Sigma_1^+\sqcup E_1\sqcup\Sigma_1^-,'),
 'G01': (r'\inserted{la comp. conn.}', r'\add{la comp.\ conn.}'),
 'G02': (r'\inserted{de $X\unsure{/|\setminus}E_{\unsure{2}}$}', r'\add{de $X\setminus E_2$}'),
 'G03': (r'\unsure{connexe} de $X$', 'connexe de $X$'),
 'G02-return': (r'\inserted{de $X\unsure{/|\setminus}E_{\unsure{2}}$}, donc', r'\add{de $X\setminus E_2$}, donc'),
 'G04': (r'\deleted{\unsure{E}}\Sigma_{12}}^{\Sigma_2^-}', r'X = \Sigma_1^+\sqcup E_1\sqcup\Sigma_{12}\sqcup E_2\sqcup\Sigma_2^+'),
 'G05': ('avec', 'avec'),
 'G06': ((r'\Sigma_2^+\subsetneq\overline{\Sigma_2^+}\subset\Sigma_2^+\cup E_2',0), r'\Sigma_2^+ \subsetneq \overline{\Sigma_2^+} \subset \Sigma_2^+\cup E_2'),
 'G07': (r'\overline{\Sigma_{12}}\cap E_2\ne\varnothing', r'\overline{\Sigma_{12}}\cap E_2\neq\emptyset'),
 'G08': (r'\deleted{alors $\Sigma_{12}\amalg E_2\amalg\Sigma_2$}', r'\struck{alors $\Sigma_{12}\sqcup E_2\sqcup\Sigma_2$}'),
 'G09': (r'\underbrace{\overline{\Sigma_2^+}}_{\subset\,\Sigma_2^+\cup E_2}', 'sous $\\overline{\\Sigma_2^+}$, une accolade porte\n$\\subset\\Sigma_2^+\\cup E_2$'),
 'BR01': ('X=\\overbrace{\\Sigma_1^+\\amalg E_1\\amalg\n', "une accolade au-dessus de $\\Sigma_1^+\\sqcup E_1\\sqcup\\Sigma_{12}$ porte\n$\\Sigma_2^-$"),
 'BR02': ('\\rlap{$\\displaystyle\\underbrace{\\phantom{E^{?}\\Sigma_{12}}\\amalg\n E_2\\amalg\\Sigma_2^+}_{\\Sigma_1^-}$}', 'une accolade au-dessous de $\\Sigma_{12}\\sqcup E_2\\sqcup\n\\Sigma_2^+$ porte $\\Sigma_1^-$'),
 'P01': ('X&=\\deleted{\\unsure{E}}\\Sigma_1^+\\amalg E_1\\amalg\\Sigma_1^-\\\\\n X&=\\Sigma_2^+\\amalg E_2\\amalg\\Sigma_2^-', 'X = \\Sigma_1^+\\sqcup E_1\\sqcup\\Sigma_1^-, \\qquad\nX = \\Sigma_2^+\\sqcup E_2\\sqcup\\Sigma_2^-'),
}
WITNESSES['BR-PAIR']=(
 'X=\\overbrace{\\Sigma_1^+\\amalg E_1\\amalg\n \\rlap{$\\displaystyle\\underbrace{\\phantom{E^{?}\\Sigma_{12}}\\amalg\n E_2\\amalg\\Sigma_2^+}_{\\Sigma_1^-}$}\\deleted{\\unsure{E}}\\Sigma_{12}}^{\\Sigma_2^-}',
 '\\note{une accolade au-dessus de $\\Sigma_1^+\\sqcup E_1\\sqcup\\Sigma_{12}$ porte\n$\\Sigma_2^-$, une accolade au-dessous de $\\Sigma_{12}\\sqcup E_2\\sqcup\n\\Sigma_2^+$ porte $\\Sigma_1^-$}')

# Graphic command names are textual source components, not measured contours.
READER_COMPONENTS = {
 'G01': {'A':['GUIDE01'],'B':['G01'], 'C':['G01']},
 'G02': {'A':['GUIDE02'],'B':['G02b'], 'C':['G02']},
 'G03': {'A':['STROKE01 two subpaths'],'B':['G02a1','G02a2'], 'C':['G03']},
 'G02-return': {'A':['ordinary comma node following right insertion'],'B':['G02c'], 'C':['ordinary comma following right insertion']},
 'G04': {'A':['SPOT01'],'C':['G04']}, 'G05': {'B':['M01'], 'C':['G05']},
 'G06': {'A':['SPOTS02a upper fill','SPOTS02b lower fill'],'B':['M02a','M02b'], 'C':['G06 upper fill','G06 lower fill']},
 'G07': {'A':['SPOT03'],'B':['M03'], 'C':['G07']}, 'G08': {'A':['CANCEL01'],'B':['G03'], 'C':['G08']},
 'G09': {'A':['ordinary underbrace'],'B':['ordinary underbrace'], 'C':['G09']},
 'D13-shape': {'A':['qualified full closing-bracket glyph'],'B':['qualified full closing-bracket glyph'], 'C':['G10 upper return','G10 lower return']},
 'BR01': {'A':['BRACE01'],'B':['ordinary overbrace'], 'C':['BR01']},
 'BR02': {'A':['BRACE02'],'B':['ordinary underbrace'], 'C':['BR02']},
}

# Filled only from explicit root sections. No source proposal is a default choice.
def rootchoice(section, final, confidence, C, H, doubt_status=None, remaining=False, **extra):
    return {'root_decision_section':section,'final':final,'confidence':confidence,
            'diff_C':bool(C),'diff_H':bool(H),'C_doubt_status':doubt_status,
            'remaining_doubt':remaining,'main_approved':True,
            'confidence_status':'root supplied local confidence',
            'count_status':'root-selected physical-locus Boolean; main record approval remains with root',**extra}

ROOT_CHOICES = {
 'D01':rootchoice(1,r'\Sigma_{\deleted{\unsure{2}}1}^+','low',0,1,'retained',True),
 'D02':rootchoice(1,r'\deleted{\unsure{sera|sont}} est','low',0,1,'retained',True),
 'D03':rootchoice(2,'connexe','high',1,0,'resolved',False,C_change_class='actual C doubt resolved'),
 'D04a':rootchoice(2,r'\unsure{/|\setminus}','low',0,1,'retained',True,
       qualification='H setminus remains an explicit alternative; root retains slash first.',C_change_class='retained C doubt; no C count'),
 'D04b':rootchoice(2,r'E_{\unsure{2}}','low',0,0,'retained',True,
       qualification='Same primary digit as H; uncertainty alone adds no H count.',C_change_class='retained C doubt; no C count'),
 'G01':rootchoice(2,'A GUIDE01: complete literal bent insertion-guide path.','high',1,1,
       C_change_class='explicit previously unrepresented graphic'),
 'G02':rootchoice(2,'A GUIDE02: complete literal pale bowed path beneath right insertion.','medium',1,1,
       C_change_class='explicit previously unrepresented graphic'),
 'G03':rootchoice(2,'A STROKE01: one draw command with two disconnected subpaths, locally unsure.','medium',1,1,None,True,
       C_change_class='explicit previously unrepresented graphic',hand_role_status='undetermined hand, role and surface origin'),
 'G02-return':rootchoice(2,',','high',0,0,None,False,
       kind='other',C_change_class='unchanged source punctuation; no C count',
       hand_role_status='Root selects the same comma already present in C and H; B G02c maps to this one punctuation mark.'),
 'D05':rootchoice(3,r"\deleted{\unsure{c'est}}",'low',0,1,'retained',True,
       C_change_class='retained C doubt; no C count',qualification='Qualified recovery of one H struck ill placeholder.'),
 'N01a':rootchoice(3,r'\unsure{é|ê}','low',1,0,None,True,
       C_change_class='new local C qualification',qualification='H retains the same acute primary candidate; no H count for qualification alone.'),
 'N01b':rootchoice(3,r'\unsure{|e}','medium',1,0,None,True,
       C_change_class='C primary word-ending reversal',full_word_comparison='égal|égale',
       final_context=r'\unsure{é|ê}gal\unsure{|e}',comparison_scope='Ending only; independent accent choice is 016-N01a.',
       qualification='No final e is primary; H égal shares that primary ending. The e alternative remains.'),
 'D10a':rootchoice(3,r'\unsure{:|à}','medium',1,1,'retained; primary candidate order changed',True,
       C_change_class='retained C doubt with primary reversal',qualification='H à remains the explicit alternative.'),
 'D10b':rootchoice(3,'donc','medium',1,0,'resolved',False,C_change_class='actual C doubt resolved'),
 'D06':rootchoice(4,r'\unsure{qfd|cqfd}','medium',1,1,'retained; primary candidate order changed',True,
       C_change_class='retained C doubt with primary reversal',alternatives=['cqfd'],
       qualification='C/H cqfd remains the explicit second candidate; no terminal point is supplied.'),
 'D07a':rootchoice(5,r'\deleted{\unsure{E}}\Sigma_1^+','low',0,1,'retained',True,
       C_change_class='retained C doubt; no C count'),
 'N05':rootchoice(5,r'\Sigma_1^-','high',0,1,None,False,
       C_change_class='agrees with C; no C count',comparison_scope='Endpoint comma after the first partition; root selects no comma.'),
 'D07b':rootchoice(6,r'\deleted{E}\Sigma_{12}','high',1,1,'resolved',False,
       C_change_class='actual C doubt resolved'),
 'BR-PAIR':rootchoice(6,'A BRACE01 and BRACE02: selected literal brace pair with unchanged labels.','high',0,1,None,False,
       C_change_class='C counts belong to individual brace contours',count_policy='One H count for the single descriptive brace-pair apparatus; two zero-H local path children.'),
 'BR01':rootchoice(6,'A BRACE01: selected literal upper-brace path.','high',1,0,None,False,
       C_change_class='one explicit C brace-geometry change',H_count_parent='016-BR-PAIR'),
 'BR02':rootchoice(6,'A BRACE02: selected literal lower-brace path.','high',1,0,None,False,
       C_change_class='one explicit C brace-geometry change',H_count_parent='016-BR-PAIR'),
 'G04':rootchoice(6,'A SPOT01: exact pale oval-like filled path, locally unsure.','low',1,1,None,True,
       C_change_class='explicit previously unrepresented graphic',hand_role_status='undetermined hand, role and surface origin'),
 'N02':rootchoice(7,r'\text{def}','high',0,1,None,False,
       C_change_class='agrees with C; no C count',comparison_scope='Definition abbreviation accent; text/roman macro spelling adds no count.'),
 'N03':rootchoice(7,r'\Sigma_{12}\overset{\text{def}}{=}\Sigma_1^-\cap\Sigma_2^-','high',0,1,None,False,
       C_change_class='agrees with C; no C count',comparison_scope='Terminal period only; no period selected.'),
 'G05':rootchoice(8,'C G05: complete avec/point group with exact filled contour and local unsure wrapper.','high',1,1,None,True,
       C_change_class='explicit previously unrepresented graphic',hand_role_status='undetermined character, role, hand and surface origin'),
 'D08':rootchoice(9,r'\deleted{\unsure{O}}Dans','low',0,1,'retained',True,
       C_change_class='retained C doubt; no C count'),
 'N04':rootchoice(10,'ouverts','medium',0,1,None,False,
       C_change_class='agrees with C; no C count',comparison_scope='No following comma is supported within surviving source edge.'),
 'G06':rootchoice(12,'A SPOTS02a/b: two exact literal fill commands in the fixed-origin locally unsure wrapper.','high',1,1,None,True,
       C_change_class='one previously unrepresented two-component graphic cluster',
       hand_role_status='undetermined character, role, hand and surface origin'),
 'G07':rootchoice(13,'A SPOT03: exact literal filled path within the complete Notons figure and fixed-origin local unsure wrapper.','high',1,1,None,True,
       C_change_class='explicit previously unrepresented graphic',hand_role_status='undetermined character, role, hand and surface origin'),
 'D07c':rootchoice(15,r'\overline{\deleted{\unsure{E}}\Sigma_{12}}','low',0,1,'retained',True,
       C_change_class='retained C doubt; no C count',comparison_scope='E predecessor only; closure-rule confirmation is 016-S08.'),
 'D07d':rootchoice(15,r'\deleted{\unsure{\Sigma}}E_1','low',0,1,'retained',True,
       C_change_class='retained C doubt; no C count'),
 'D09':rootchoice(16,'conclurait','high',1,1,'resolved',False,C_change_class='actual C doubt resolved'),
 'D11':rootchoice(16,r'\unsure{en|on}','medium',0,0,'retained',True,C_change_class='retained C doubt; no C count'),
 'G08':rootchoice(16,'A CANCEL01: one literal strike with four connected curve segments; semantic deleted copies remain invisible.','high',1,1,None,False,
       C_change_class='one explicit C cancellation-geometry change'),
 'P01':rootchoice(16,'The two partition equations occupy successive physical rows.','high',0,0,None,False,
       C_change_class='common retained row arrangement; no witness count'),
 'D13':rootchoice(19,'C G10: two visible return paths under local unsure; closing-bracket interpretation retained.','low',1,1,'retained',True,
       C_change_class='partial observed geometry replaces complete bracket glyph; interpretation remains qualified',
       alternatives=['closing-bracket interpretation with unseen joining upright unresolved']),
 'D13-shape':rootchoice(19,'C G10 exact two return paths, without an added upright.','medium',0,0,None,True,
       C_change_class='noncounting geometry component of 016-D13',
       qualification='Two-return shape selected; bracket interpretation remains qualified at the physical parent.'),
 'G09':rootchoice(19,'C G09: complete group with literal hooked/retraced underbrace, formula node and lower inclusion label.','high',1,1,None,False,
       C_change_class='one explicit C underbrace-geometry change'),
}
for parent in ['D12a','D12b']:
    ROOT_CHOICES[parent]=rootchoice(18,r'\unsure{\deleted{\amalg}\cup|\amalg}','low',1,1,
        'retained; square-form glyph resolved while predecessor/live state remains qualified',True,
        C_change_class='new C state qualification and square-form glyph recovery within one physical join cluster',
        alternatives=[r'live \amalg'],glyph_status='resolved square-form component',state_status='retained',
        glyph_confidence='high',state_confidence='low')
    ROOT_CHOICES[parent+'-old']=rootchoice(18,r'\amalg','high',0,0,
        'mixed: square-form glyph resolved; predecessor state retained',True,
        C_change_class='noncounting recognized-glyph component; physical parent carries the change',
        glyph_status='resolved',state_status='retained',glyph_confidence='high',state_confidence='low',
        qualification='This firm square-form reading supplies no unqualified assertion of cancelled/predecessor status; the full state alternatives remain at the parent.')
    ROOT_CHOICES[parent+'-live']=rootchoice(18,r'\unsure{\deleted{\amalg}\cup|\amalg}','low',0,0,
        'retained',True,C_change_class='noncounting live-form/state component of physical join parent',
        glyph_status='cup/square-join alternative retained',state_status='retained',
        qualification='The proposed live cup and cancelled square join remain jointly qualified against live amalg.')
for ident,literal in [('S01',r'\overline{\Sigma_1^+}'),('S02',r'\overline{\Sigma_{12}}'),
                      ('S03',r'\overline{\Sigma_1^-}'),('S04',r'\overline{\Sigma_2^-}'),
                      ('S05',r'\overline{\Sigma_2^+}')]:
    ROOT_CHOICES[ident]=rootchoice(11,literal,'high',0,0,None,False,
        S_status='confirmed local overbar; present in both current C and H',
        C_change_class='S confirmation of existing source bar; no witness change')
for ident,section,literal in [('S06',14,r'\overline{\Sigma_{12}}'),
                             ('S07',13,r'\overline{\Sigma_{12}}'),
                             ('S08',15,r'\overline{\deleted{\unsure{E}}\Sigma_{12}}'),
                             ('S09',17,r'\overline{\Sigma_1^-}'),
                             ('S10',18,r'\overline{\Sigma_1^-}'),
                             ('S11',18,r'\overline{\Sigma_2^+\unsure{\deleted{\amalg}\cup|\amalg}E_2'+'\n '+r'\unsure{\deleted{\amalg}\cup|\amalg}\Sigma_{12}}'),
                             ('S12',19,r'\overline{\Sigma_2^+}'),
                             ('S13',19,r'\overline{\Sigma_{12}}'),
                             ('S14',19,r'\overline{\Sigma_{12}}')]:
    ROOT_CHOICES[ident]=rootchoice(section,literal,'high',0,0,None,False,
        S_status='confirmed local overbar; present in both current C and H',
        C_change_class='S confirmation of existing source bar; no witness change')

ACTUAL_CHECK_EVENT = {
 'statement_id':'SP40-016-IMAGE-FRAME',
 'date':'2026-11-20',
 'event_clock':None,
 'event_clock_status':'No clock time was captured for the prior event.',
 'who':'reader A; GPT-6 Astra Pro / effort not separately exposed',
 'type':'computation or formal certificate',
 'outcome':'Existing recorded source-image-frame comparison only: PIL ImageChops.difference compared full-scan im.crop((0,y0,1685,y0+1261)) with each supplied half at fixed origins a:y0=0 and b:y0=1101, then ImageStat.Stat(delta).mean. Recorded mean absolute channel differences: a=[0.004762364192141793,0.004896966045976416,0.007469932251969022]; b=[0.9677270876818125,0.9683662111696006,1.2771885155439255]. Half sizes were 1685x1261. No alignment search or acceptance threshold was recorded; no pixel-identity conclusion. This records the prior finite comparison without rerunning it; no mathematical theorem check was performed.',
 'source_provenance':[{'manifest':'A.report.json','pointer':'/viewing_log/half_coordinate_verification'}, {'manifest':'A.make_crops.py'}, {'manifest':'A.crop_manifest.json'}],
 'authorization':'Root explicit instruction; raw reader check_events remains unchanged.'
}



def attach_final_sources(record, manifest):
    map_path=CHECKS/'scan016_final_source_map.json'
    source_map=read_json(map_path)
    raw_path=Path(source_map['draft_file'])
    if raw_path.is_absolute():
        draft_path=raw_path
    elif raw_path.parts[0]=='out':
        draft_path=ROOT/raw_path
    elif raw_path.parts[0]=='checks':
        draft_path=OUT/raw_path
    else:
        draft_path=CHECKS/raw_path.name
    selected_path=str(draft_path.relative_to(OUT))
    manifest['files']['root.final_draft.tex']=fingerprint(draft_path)
    manifest['files']['root.final_source_map.json']=fingerprint(map_path)
    by_decision={d['id']:d for d in record['decisions']}
    by_inventory={i['element']:i for i in record['inventory']}
    blocks={block['id']:(index,block) for index,block in enumerate(source_map['blocks'])}

    def attachment(item,field,index):
        span=item['draft']
        start=span['character_start']; end=span['character_end_exclusive']
        cover=span.get('covering_lines_inclusive')
        first=span.get('start',{}).get('line')
        last=cover[-1] if isinstance(cover,list) else None
        result={'manifest':'root.final_draft.tex','path':selected_path,
            'char_start':start,'char_end':end,'line_start':first,'line_end':last,
            'group_anchor':item.get('block_id'),
            'assembly_map':{'manifest':'root.final_source_map.json','pointer':f'/{field}/{index}'},
            'scope':item.get('note') or item.get('scope') or 'exact selected source locus',
            'literal_sha256_utf8':span.get('literal_sha256_utf8')}
        block_id=item.get('block_id')
        if block_id in blocks:
            block_index,block=blocks[block_id]
            result['selected_component_source']={'manifest':'root.final_source_map.json','pointer':f'/blocks/{block_index}/source'}
        if field=='overbar_coverage':
            result['packet_C_source']={'manifest':'root.final_source_map.json','pointer':f'/{field}/{index}/source'}
        return result

    for field in ['decision_coverage','overbar_coverage']:
        for index,item in enumerate(source_map.get(field,[])):
            ident=item['decision_id']
            if ident not in by_decision:
                raise ValueError(f'Selected source map has unmapped decision {ident}')
            ref=attachment(item,field,index)
            row=by_decision[ident]
            same=[a for a in row['final_source_attachment'] if a['char_start']==ref['char_start'] and a['char_end']==ref['char_end']]
            if same:
                same[0].setdefault('additional_assembly_map_refs',[]).append(ref['assembly_map'])
            else:
                row['final_source_attachment'].append(ref)
    for index,item in enumerate(source_map['inventory_coverage']):
        ident=item['inventory_id']
        if ident not in by_inventory:
            raise ValueError(f'Selected source map has unmapped inventory {ident}')
        by_inventory[ident]['root_page_sources'].append(attachment(item,'inventory_coverage',index))
    for row in record['decisions']:
        row['root_page_sources']=copy.deepcopy(row['final_source_attachment'])
        row['root_source_attachment_status']='complete selected-source attachment' if row['final_source_attachment'] else 'pending selected-source attachment'
    for row in record['inventory']:
        if row['root_page_sources']:
            row['transcribed']='yes'
            row['final_source_attachment_status']='complete selected-source attachment'
    for row in record['doubts']:
        row['root_page_sources']=copy.deepcopy(by_decision[row['decision_id']]['final_source_attachment'])
    record['source_attachment_map']='checks/scan016_final_source_map.json'
    record['root_selected_source']=selected_path
    record['source_attachment_status']='selected source spans attached; final targeted coverage pass pending'
    record['final_source_missing_attachments']={
        'decisions':[row['id'] for row in record['decisions'] if not row['final_source_attachment']],
        'inventory':[row['element'] for row in record['inventory'] if not row['root_page_sources']],
        'doubts':[row['decision_id'] for row in record['doubts'] if not row['root_page_sources']]}
    return source_map


def build(released,attach_final=False):
    metadata = read_json(PACKET / 'metadata.json')
    source_map = read_json(CHECKS / 'scan016_source_map.json')
    reports = {r:read_json(OUT / 'readers' / '016' / r / 'report.json') for r in released}
    sources = {r:(OUT / 'readers' / '016' / r / 'reading.tex').read_text() for r in released}
    witness_sources = {w:(PACKET / (w+'.tex')).read_text() for w in ['C','H']}
    previous_manifest_path=CHECKS/'scan016_reader_fingerprints.json'
    previous_manifest=read_json(previous_manifest_path) if previous_manifest_path.exists() else {}
    manifest = {'scan':16, 'scope':'source-only immutable reader and witness attachments; no image bytes read', 'files':{}, 'readers':{}, 'root_files':{},
                'frozen_reader_files':copy.deepcopy(previous_manifest.get('frozen_reader_files',
                    {k:v for k,v in previous_manifest.get('files',{}).items() if k.startswith(('A.','B.','C.'))}))}
    for name in ['C.tex','H.tex','C_doubts.txt','C_inventory.json','C_notes.txt','metadata.json','notation.md']:
        manifest['files']['packet.'+name] = fingerprint(PACKET / name)
    for role in released:
        folder = OUT / 'readers' / '016' / role
        text_files = [p for p in folder.iterdir() if p.suffix in {'.tex','.md','.json','.py'}]
        for p in sorted(text_files):
            manifest['files'][role+'.'+p.name] = fingerprint(p)
            manifest['frozen_reader_files'].setdefault(role+'.'+p.name,copy.deepcopy(manifest['files'][role+'.'+p.name]))
        manifest['readers'][role] = {k:copy.deepcopy(v) for k,v in reports[role].items() if k not in ['differences','doubts','inventory']}
    for name in ['scan016_source_map.json','scan016_witness_attention.md','scan016_main_decisions.md','scan016_root_crop_audit.json']:
        p = CHECKS / name
        if p.exists(): manifest['root_files'][name] = fingerprint(p)
    root_manifest_aliases={'root.main_decisions.md':'scan016_main_decisions.md',
        'root.crop_audit.json':'scan016_root_crop_audit.json','root.source_map.json':'scan016_source_map.json',
        'root.witness_attention.md':'scan016_witness_attention.md','root.final_draft.tex':'scan016_final_draft.tex',
        'root.final_source_map.json':'scan016_final_source_map.json'}
    for alias,name in root_manifest_aliases.items():
        if alias in ['root.final_draft.tex','root.final_source_map.json'] and not attach_final:
            continue
        path=CHECKS/name
        if path.exists(): manifest['files'][alias]=fingerprint(path)
    mapping = {'A':A_MAP,'B':B_MAP,'C':C_MAP}
    inventory_mapping = {'A':A_INVENTORY_MAP,'B':B_INVENTORY_MAP,'C':C_INVENTORY_MAP}
    decisions = {}
    original_rows = collections.defaultdict(list)
    for row,ids in ORIGINAL.items():
        for ident in ids:
            original_rows[ident].append(row)
            for child in JOIN_COMPONENTS.get(ident,[]): original_rows[child].append(row)
    for ident,location in LOCI:
        decision = {'id':'016-'+ident,'location':location,'C':None,'H':None,'final':None,
            'readers':{r:None for r in ['A','B','C']}, 'reader_provenance':{r:[] for r in ['A','B','C']},
            'reader_proposals':{r:[] for r in ['A','B','C']}, 'reader_evidence':[],
            'evidence':'Pending a specific root decision section.', 'crop':None, 'available_crops':[],
            'full_scan_boxes':{}, 'confidence':None, 'confidence_status':'pending root',
            'kind':'other','diff_C':None,'diff_H':None, 'count_status':'pending root physical-locus count',
            'C_doubt_status':'pending root' if original_rows[ident] else None,
            'source_C_doubt_rows':original_rows[ident], 'marked_in_H':'no', 'mathematical_consequence':None,
            'main_approved':False,'log_decision':True,'final_source_attachment':[],
            'witness_provenance':{},'root_decision_log':'checks/scan016_main_decisions.md',
            'root_decision_section':None,'remaining_doubt':None,
            'root_source_attachment_status':'pending root-selected final TeX',
            'reader_components':copy.deepcopy(READER_COMPONENTS.get(ident,{}))}
        if ident in WITNESSES:
            for witness, spec in zip(['C','H'],WITNESSES[ident]):
                literal,occurrence = spec if isinstance(spec,tuple) else (spec,0)
                attachment = exact_span(witness_sources[witness],literal,occurrence,'packet.'+witness+'.tex')
                decision['witness_provenance'][witness] = attachment
                decision[witness] = literal
        if ident in JOIN_COMPONENTS:
            decision['physical_cluster'] = ident
            decision['component_decision_ids'] = ['016-'+c for c in JOIN_COMPONENTS[ident]]
            decision['count_policy'] = 'One physical predecessor/live cluster per witness; component children retain local choices without additional witness counts.'
        for parent,children in JOIN_COMPONENTS.items():
            if ident in children:
                decision['physical_cluster'] = parent
                decision['C_count_parent'] = '016-'+parent
                decision['H_count_parent'] = '016-'+parent
                decision['noncounting_component'] = True
        if ident == 'D13-shape':
            decision['physical_cluster'] = 'D13'
            decision['C_count_parent'] = '016-D13'
            decision['H_count_parent'] = '016-D13'
            decision['noncounting_component'] = True
        if ident == 'D13':
            decision['physical_cluster'] = 'D13'
            decision['component_decision_ids'] = ['016-D13-shape']
        if ident in ['G03','G04','G05','G06','G07','G02-return']:
            decision['hand_role_status'] = 'Qualified: pending root; preserve each reader’s hand, role and surface-origin reservations.'
        decisions[ident] = decision

    diff_crosswalk = []
    for role,report in reports.items():
        for index,row in enumerate(report['differences']):
            targets = mapping[role][row['id']]
            pointer = f'/differences/{index}'
            diff_crosswalk.append({'reader':role,'pointer':pointer,'source_id':row['id'],'loci':['016-'+t for t in targets]})
            for target in targets:
                decision = decisions[target]
                ref = {'manifest':role+'.report.json','pointer':pointer,'row_id':row['id']}
                decision['reader_provenance'][role].append(ref)
                decision['reader_proposals'][role].append(copy.deepcopy(row))
                readings = [p.get('reading') for p in decision['reader_proposals'][role]]
                decision['readers'][role] = readings[0] if len(readings)==1 else readings
                decision['reader_evidence'].append({'reader':role,'source_id':row['id'],'excerpt':row.get('evidence','')})
                path = crop_path(role,row.get('readers_crop'))
                if path and path not in decision['available_crops']: decision['available_crops'].append(path)
                if row.get('bbox') is not None: decision['full_scan_boxes'][role+':'+row['id']] = copy.deepcopy(row['bbox'])
                if decision['kind']=='other': decision['kind']=row.get('kind','other')
                if 'ill' in str(decision.get('H')): decision['marked_in_H']='yes'

    # Supplemental reader choices present in their actual TeX/audit/component
    # records, without fabricating a difference-row entry or proposal count.
    supplemental = {
      ('A','N01a'): ('égale','unqualified acute in supplied reader word'),
      ('B','N01a'): (r'\unsure{égal|égale}','unqualified acute in both supplied word alternatives'),
      ('C','N05'): (r'X&=\deleted{\unsure{E}}\Sigma_1^+\amalg E_1\amalg\Sigma_1^-','first-row source contains no endpoint comma'),
      ('A','G05'): ('avec\n\\[','source proceeds directly from avec to its definition, without a separate below-right point'),
      ('B','G04'): (r'\deleted{E}\Sigma_{12}}^{\Sigma_2^-}','central source contains no separately encoded point'),
      ('A','G09'): (r'\underbrace{\overline{\Sigma_2^+}}_{\subset\,\Sigma_2^+\cup E_2}','conventional underbrace source'),
      ('B','G09'): (r'\underbrace{\overline{\Sigma_2^+}}_{\subset\,\Sigma_2^+\cup E_2}','conventional underbrace source'),
      ('A','D13-shape'): (r'\unsure{\big]}','qualified complete bracket glyph in source'),
      ('B','D13-shape'): (r'\unsure{\big]}','qualified complete bracket glyph in source'),
      ('B','BR01'): ('X=\\overbrace{\\Sigma_1^+\\amalg E_1\\amalg\n','conventional overbrace source'),
      ('B','BR02'): ('\\rlap{$\\displaystyle\\underbrace{\\phantom{E\\Sigma_{12}}\\amalg\n E_2\\amalg\\Sigma_2^+}_{\\Sigma_1^-}$}','conventional underbrace source'),
      ('B','BR-PAIR'): ('X=\\overbrace{\\Sigma_1^+\\amalg E_1\\amalg\n \\rlap{$\\displaystyle\\underbrace{\\phantom{E\\Sigma_{12}}\\amalg\n E_2\\amalg\\Sigma_2^+}_{\\Sigma_1^-}$}\\deleted{E}\\Sigma_{12}}^{\\Sigma_2^-}','conventional paired-brace source'),
    }
    supplemental_crosswalk=[]
    for (role,ident),(literal,scope) in supplemental.items():
        if role not in released: continue
        attachment=exact_span(sources[role],literal,0,role+'.reading.tex')
        attachment['scope']=scope
        decisions[ident].setdefault('reader_source_attachments',{}).setdefault(role,[]).append(attachment)
        if decisions[ident]['readers'].get(role) is None: decisions[ident]['readers'][role]=scope+': '+literal
        supplemental_crosswalk.append({'manifest':role+'.reading.tex','attachment':attachment,'loci':['016-'+ident]})
    for role in released:
        literal=WITNESSES['P01'][0]
        attachment=exact_span(sources[role],literal,0,role+'.reading.tex')
        decisions['P01'].setdefault('reader_source_attachments',{})[role]=[attachment]
        decisions['P01']['readers'][role]='Two successive source rows in aligned environment.'
    graphical_crosswalk=[]
    component_map={'STROKE01':'G03','GUIDE01':'G01','GUIDE02':'G02','BRACE01':'BR01','BRACE02':'BR02','SPOT01':'G04','SPOTS02a/b':'G06','SPOT03':'G07','CANCEL01':'G08'}
    if 'A' in released:
        for index,component in enumerate(reports['A']['graphical_components']):
            ident=component_map[component['id']]
            ref={'manifest':'A.report.json','pointer':f'/graphical_components/{index}','row_id':component['id']}
            targets=[ident,'BR-PAIR'] if ident in ['BR01','BR02'] else [ident]
            for target in targets:
                decisions[target].setdefault('supplemental_reader_provenance',{}).setdefault('A',[]).append(ref)
                decisions[target].setdefault('supplemental_reader_components',{}).setdefault('A',[]).append(copy.deepcopy(component))
                decisions[target].setdefault('reader_source_attachments',{}).setdefault('A',[]).append(exact_span(sources['A'],component['reading_tex_anchor'],0,'A.reading.tex'))
                if decisions[target]['readers']['A'] is None: decisions[target]['readers']['A']=component.get('witness_state',component['id'])
            graphical_crosswalk.append({'source':ref,'loci':['016-'+target for target in targets]})
        decisions['BR-PAIR']['readers']['A']='A BRACE01/BRACE02: both source component records and literal paths retained as one paired-brace proposal.'

    # S's fourteen local source bar occurrences remain explicit even with C/H agreement.
    bar_locations = ['first closure row, Sigma1 plus','middle closure row, Sigma12','middle closure row, Sigma1 minus','middle closure row, Sigma2 minus','third closure row, Sigma2 plus','first Notons expression, Sigma12','second Notons expression, Sigma12','Car hypothesis, corrected Sigma12','Car continuation, Sigma1 minus','final equality, first Sigma1 minus','final equality, long bar over three terms','final equality, first component Sigma2 plus','final equality, penultimate Sigma12','final equality, terminal Sigma12']
    for index,location in enumerate(bar_locations):
        ident = f'S{index+1:02d}'
        d = {'id':'016-'+ident,'location':'S closure audit: '+location,'C':None,'H':None,'final':None,
             'readers':{},'reader_provenance':{},'reader_proposals':{},'reader_evidence':[],
             'evidence':'Pending explicit root confirmation or overturning of the local source overbar.',
             'crop':None,'available_crops':[],'confidence':None,'confidence_status':'pending root',
             'kind':'other','diff_C':None,'diff_H':None,'count_status':'pending root; confirmation of a bar already present in C and H adds no error',
             'C_doubt_status':None,'source_C_doubt_rows':[],'marked_in_H':'no','mathematical_consequence':None,
             'main_approved':False,'log_decision':True,'witness_provenance':{},'final_source_attachment':[],
             'S_id':'SA01-K81-06','S_status':'pending root local ink inspection',
             'comparison_scope':'Closure rule only; enclosed letters, states and operators retain their separate local decision/count scopes.',
             'S_evidence_scope':'The supplied S attention map reports an argument-based inference and no scan viewed by S.',
             'root_decision_log':'checks/scan016_main_decisions.md','root_decision_section':None,'remaining_doubt':None,
             'root_source_attachment_status':'pending root-selected final TeX'}
        for witness,text in witness_sources.items():
            starts=[m.start() for m in re.finditer(re.escape(r'\overline{'),text)]
            start=starts[index]; pos=start+len(r'\overline{'); depth=1
            while depth:
                depth+=(text[pos]=='{')-(text[pos]=='}');pos+=1
            literal=text[start:pos]
            a={'manifest':'packet.'+witness+'.tex','char_start':start,'char_end':pos,'line_start':text.count('\n',0,start)+1,'line_end':text.count('\n',0,pos-1)+1,'excerpt':literal}
            d[witness]=literal;d['witness_provenance'][witness]=a
        for role,text in sources.items():
            starts=[m.start() for m in re.finditer(re.escape(r'\overline{'),text)]
            start=starts[index]; pos=start+len(r'\overline{'); depth=1
            while depth:
                depth+=(text[pos]=='{')-(text[pos]=='}'); pos+=1
            literal=text[start:pos]
            a={'manifest':role+'.reading.tex','char_start':start,'char_end':pos,'line_start':text.count('\n',0,start)+1,'line_end':text.count('\n',0,pos-1)+1,'excerpt':literal}
            d['readers'][role]=literal
            d.setdefault('reader_source_attachments',{})[role]=[a]
        decisions[ident]=d

    inventory = {ident:{'sheet_kind':'text','hand':'undetermined hand' if ident in ['I04','I09','I20','I23','I29','I32','I46'] else 'pending root',
      'element':'016-'+ident,'kind':kind,'position':position,'first_words_or_objects':objects,'transcribed':'pending root',
      'source_inventory':[],'reader_hand_proposals':{},'source_element_ids':{},'source_rows':[],
      'root_page_sources':[],'hand_status':'source proposals retained; pending root','final_source_attachment_status':'pending root-selected source'}
      for ident,kind,position,objects in INVENTORY}
    inv_crosswalk=[]
    all_inv=[(r+'.report.json',r,reports[r]['inventory'],inventory_mapping[r]) for r in released]
    all_inv.append(('packet.C_inventory.json','witness_C',read_json(PACKET/'C_inventory.json'),PACKET_INVENTORY_MAP))
    for source,role,rows,imap in all_inv:
        for index,row in enumerate(rows):
            targets=imap[row['element']]
            pointer=f'/inventory/{index}' if role!='witness_C' else f'/{index}'
            ref={'manifest':source,'pointer':pointer,'row_id':row['element']}
            inv_crosswalk.append({'source':source,'pointer':pointer,'source_id':row['element'],'targets':['016-'+t for t in targets]})
            for target in targets:
                item=inventory[target]
                item['source_inventory'].append(copy.deepcopy(ref))
                item['source_rows'].append({'source':copy.deepcopy(ref),'value':copy.deepcopy(row)})
                item['source_element_ids'].setdefault(role,[]).append(row['element'])
                if role=='witness_C': item.setdefault('witness_hand_labels',{})['C']=row.get('hand')
                else: item['reader_hand_proposals'][role]=row.get('hand')

    doubt_crosswalk=[]
    for role,report in reports.items():
        for index,row in enumerate(report['doubts']):
            ids=row.get('difference_ids') or [row.get('id')]
            targets=list(dict.fromkeys(t for sourceid in ids for t in mapping[role][sourceid]))
            doubt_crosswalk.append({'reader':role,'pointer':f'/doubts/{index}','source_difference_ids':ids,'loci':['016-'+t for t in targets], 'source_row':copy.deepcopy(row)})

    original_map=[]
    for src in source_map['categories']['Doubtful readings']:
        row=src['source_row'];primaries=ORIGINAL[row]
        component_ids=[child for parent in primaries for child in JOIN_COMPONENTS.get(parent,[])]
        local_ids=[child for parent in primaries for child in JOIN_COMPONENTS.get(parent,[parent])]
        original_map.append({'source_row':row,'source_line':src['line'],'source_manifest':'packet.C_doubts.txt','source_literal':src['literal'],
           'local_loci':src['local_loci'],'primary_local_decision_ids':['016-'+i for i in primaries],
           'component_decision_ids':['016-'+i for i in component_ids],
           'local_status_decision_ids':['016-'+i for i in local_ids],
           'decision_ids':['016-'+i for i in primaries+component_ids],
           'local_statuses':{'016-'+i:'pending root' for i in local_ids}, 'status':'pending root'})

    for entry in original_map:
        row=entry['source_row']
        entry['reader_source_maps']={}
        for role,field in [('A','C_doubt_source_rows'),('B','source_doubt_rows'),('C','C_doubt_source_map')]:
            if role in released:
                entry['reader_source_maps'][role]={'manifest':role+'.report.json','pointer':f'/{field}/{row-1}','value':copy.deepcopy(reports[role][field][row-1])}
        if row==12:
            entry['source_qualification_scope']='The original source table qualifies both final join forms, including the second cup printed without a local unsure wrapper in C.tex. The table identity and all predecessor/live/state alternatives are preserved.'
            entry['reader_scope_counts']={'A':2,'B':4,'C':4}

    record = {'scan':16,'folder':metadata['folder'],'their_page':metadata['their_page'],'hua_has':metadata['hua_has'],
       'filename':'J81-02_81_scan016.tex','brief_version':'v14','main_adjudicated':False,
       'decisions':list(decisions.values()),'doubts':[], 'inventory':list(inventory.values()),
       'notes':'Source record pending root choices. Original C_notes.txt contains a single blank newline. Reader notes, notation proposals and audit files remain separately attached. One actual prior source-image-frame comparison by reader A is logged separately at root instruction; it was not rerun by the clerk, and no mathematical theorem check was performed.',
       'abbreviations':[{'form':'comp. conn.','expansion':'composante connexe'}, {'form':'cqfd [?]','expansion':"ce qu'il fallait démontrer"}, {'form':'def','expansion':'définition'}, {'form':'p. ex.','expansion':'par exemple'}],
       'check_events':[copy.deepcopy(ACTUAL_CHECK_EVENT)], 'workflow_note':'Source-only clerk assembly from released reader text and actual packet sources. Root decision authority remains checks/scan016_main_decisions.md. No image read, OCR, research, compiler, renderer, numerical geometry or mathematical check performed by the clerk.',
       'source_counts':{'reader_differences':{r:len(v['differences']) for r,v in reports.items()},'reader_inventory':{r:len(v['inventory']) for r,v in reports.items()},
         'C_inventory':32,'C_doubt_rows':13,'C_primary_local_doubts':19,'C_local_status_components':21,
         'reader_remaining_doubt_rows':{r:len(v['doubts']) for r,v in reports.items()},
         'source_inventory_rows':len(inv_crosswalk),'union_inventory_elements':len(inventory),'union_decision_entries':len(decisions)},
       'source_difference_crosswalk':diff_crosswalk,'source_graphical_component_crosswalk':graphical_crosswalk,'source_supplemental_tex_crosswalk':supplemental_crosswalk,'source_doubt_crosswalk':doubt_crosswalk,'source_inventory_crosswalk':inv_crosswalk,
       'actual_C_doubt_map':original_map,'source_manifest':'checks/scan016_reader_fingerprints.json',
       'root_decision_log':'checks/scan016_main_decisions.md','root_actions_pending':['Apply specific root choices and count flags.','Attach selected final TeX.','Root alone may approve/commit the main record.'],
       'source_categories':copy.deepcopy(source_map['categories']),
       'reader_notes':{r:copy.deepcopy(v['notes']) for r,v in reports.items()}, 'reader_notation':{r:copy.deepcopy(v['notation']) for r,v in reports.items()},
       'released_readers':released, 'pending_readers':[r for r in ['A','B','C'] if r not in released],
       'mechanical_verification':{'status':'pending one targeted source coverage/count consistency pass when the draft is complete',
          'no_image_viewed_by_clerk':True,'proof_events':0,'numerical_geometry_checks':0},
       'counts':{'status':'pending root','C':None,'H':None},
       'C_doubt_resolution_counts':{'actual_rows':13,'physical_primary_clusters':19,'local_status_components':21,'resolved_local':None,'retained_local':None},
       'source_attachment_status':'pending root-selected final TeX'}

    root_log=(CHECKS/'scan016_main_decisions.md').read_text()
    section_pattern=re.compile(r'^## (\d+) [—-] (.+)$',re.M)
    matches=list(section_pattern.finditer(root_log))
    sections={}
    for index,match in enumerate(matches):
        end=matches[index+1].start() if index+1<len(matches) else len(root_log)
        sections[int(match.group(1))]={'heading':match.group(2),'text':root_log[match.start():end],
             'char_start':match.start(),'char_end':end}
    for ident,choice in ROOT_CHOICES.items():
        section=choice['root_decision_section']
        if section not in sections: raise ValueError(f'Root section {section} does not exist for {ident}')
        decisions[ident].update(copy.deepcopy(choice))
        decisions[ident]['root_decision_heading']=sections[section]['heading']
        decisions[ident]['evidence']=sections[section]['text'].strip()
        decisions[ident]['root_evidence_source']={'manifest':'root.main_decisions.md','section':section,
             'heading':sections[section]['heading'],'char_start':sections[section]['char_start'],'char_end':sections[section]['char_end']}
        crops=re.findall(r'`((?:readers|crops)/016/[^`]+\.(?:png|jpg))`',sections[section]['text'])
        decisions[ident]['root_crop_paths']=crops
        decisions[ident]['crop']=crops[0] if crops else None
    clarification_heading='## Source-only confidence clarification after section20'
    if clarification_heading in root_log:
        start=root_log.index(clarification_heading)
        clarification=exact_span(root_log,root_log[start:],0,'root.main_decisions.md')
        for ident in ['G08','P01','D12a','D12a-old','D12a-live','D12b','D12b-old','D12b-live']:
            decisions[ident]['root_source_only_clarification']=copy.deepcopy(clarification)
    for entry in original_map:
        entry['local_statuses']={ident:decisions[ident.removeprefix('016-')]['C_doubt_status'] for ident in entry['local_status_decision_ids']}
        entry['status']='root supplied every component choice' if all(decisions[ident.removeprefix('016-')]['main_approved'] for ident in entry['local_status_decision_ids']) else 'pending root choices for one or more components'
    record['root_choices_applied_through_section']=max((v['root_decision_section'] for v in ROOT_CHOICES.values()),default=0)
    record['root_sections_present']=len(sections)
    record['root_ink_pass']=read_json(CHECKS/'scan016_root_crop_audit.json')
    local_statuses=[status for row in original_map for status in row['local_statuses'].values()]
    record['C_doubt_resolution_counts'].update({'resolved_local':sum(status=='resolved' for status in local_statuses),
          'retained_local':sum(str(status).startswith('retained') for status in local_statuses),
          'mixed_glyph_resolved_state_retained_local':sum(str(status).startswith('mixed:') for status in local_statuses),
          'pending_local':sum(status=='pending root' for status in local_statuses)})
    primary_statuses=[decisions[ident.removeprefix('016-')]['C_doubt_status'] for row in original_map for ident in row['primary_local_decision_ids']]
    record['C_doubt_resolution_counts'].update({
        'resolved_physical_primary_clusters':sum(status=='resolved' for status in primary_statuses),
        'retained_physical_primary_clusters':sum(str(status).startswith('retained') for status in primary_statuses),
        'resolved_square_form_subcomponents_with_state_retained':sum(d.get('glyph_status')=='resolved' and d.get('state_status')=='retained' for d in record['decisions']),
        'scope_note':'The 19 primary physical clusters and 21 expanded local component scopes are separate counts. At each final join, a recognizable square-form glyph is firm while predecessor/live chronology remains qualified; these two mixed components are logged without extra witness counts.'})
    record['counts'].update({'approved_subtotal_C':sum(d['diff_C'] is True for d in record['decisions']),
          'approved_subtotal_H':sum(d['diff_H'] is True for d in record['decisions']),
          'pending_physical_or_audit_entries':sum(not d['main_approved'] for d in record['decisions'])})
    explicit_alternatives={
       'D01':[], 'D02':['sont'], 'D04a':[r'\setminus'], 'D04b':[], 'D05':[],
       'D06':['qfd'], 'D07a':[], 'D07c':[], 'D07d':[], 'D08':[],
       'D10a':['à'], 'D10b':["d'où"], 'D11':['on'],
       'N01a':['ê'], 'N01b':['e'],
       'G03':['unestablished role, hand and surface origin'],
       'G04':['unestablished character, role, hand and surface origin'],
       'G05':['unestablished character, role, hand and surface origin'],
       'G06':['unestablished character, role, hand and surface origin'],
       'G07':['unestablished character, role, hand and surface origin'],
    }
    for d in record['decisions']:
        if d.get('remaining_doubt') and not d.get('noncounting_component'):
            raw_components=[]
            for source in doubt_crosswalk:
                if d['id'] in source['loci']:
                    raw_components.append({'reader':source['reader'],'source':{'manifest':source['reader']+'.report.json','pointer':source['pointer']},**copy.deepcopy(source['source_row'])})
            record['doubts'].append({'decision_id':d['id'],'location':d['location'],'reading':d['final'],
                'alternatives':d.get('alternatives',explicit_alternatives.get(d['id'].removeprefix('016-'),[])),
                'confidence':d['confidence'],'reason':d['evidence'],
                'reader_components':raw_components,'final_status':'root-selected uncertainty retained',
                'root_decision_section':d['root_decision_section'],'crop':d['crop'],'root_page_sources':[],
                'local_component_statuses':[{k:child.get(k) for k in ['id','final','C_doubt_status','remaining_doubt','root_decision_section']}
                    for child in record['decisions'] if child.get('noncounting_component') and child.get('physical_cluster')==d.get('physical_cluster') and d.get('physical_cluster')]})
    record['root_approved_decision_entries']=sum(d.get('main_approved',False) for d in record['decisions'])
    record['pending_root_decision_ids']=[d['id'] for d in record['decisions'] if not d.get('main_approved')]
    record['source_counts']['approved_remaining_doubt_clusters']=len(record['doubts'])
    record['source_counts']['reader_original_C_local_scope_counts']={'A':19,'B':21,'C':21}
    if 'G02-return' in ROOT_CHOICES:
        inventory['I09'].update({'kind':'text','hand':'his hand','first_words_or_objects':'comma after the right inserted clause, once',
             'root_decision_section':2,'hand_status':'Root identifies the existing textual punctuation mark; reader source labels retained.'})
    for item in record['inventory']:
        if item['hand']=='pending root' and item['reader_hand_proposals']:
            proposed=set(item['reader_hand_proposals'].values())
            if len(proposed)==1:
                item['hand']=next(iter(proposed))
                item['hand_status']='unanimous returned source label; retained as a proposal pending root record approval'
    if not record['pending_root_decision_ids']:
        by_confidence={w:dict(collections.Counter(d['confidence'] for d in record['decisions'] if d['diff_'+w])) for w in ['C','H']}
        record['counts']={'status':'all local root choices supplied; root record approval pending',
            'C':sum(d['diff_C'] for d in record['decisions']), 'H':sum(d['diff_H'] for d in record['decisions']),
            'by_witness_confidence':by_confidence,'remaining_doubt_loci':len(record['doubts']),
            'inventory_elements':len(record['inventory'])}
        record['notes']=(
            'The supplied page writes two partitions of X and their five-term partition with upper and lower braces, defines Sigma12, and records three closure chains and two nonempty-intersection assertions. Its lower argument ends ce qui n\'est pas. The selected opening abbreviation is qfd|cqfd; the opening accent and final-e ending are qualified separately. Both final joins keep the complete deleted-amalg/cup versus live-amalg state alternatives. These statements and choices are attributed to the supplied writing and exact root sections. All fourteen physical/body closure bars already present in C/H are confirmed under S SA01-K81-06, with no bar-confirmation count; H also repeats the Sigma2-plus bar in its descriptive underbrace apparatus. Small detached shapes retain their unresolved character, role, hand and surface origin. The archive numeral15 remains only in the existing comment, with undetermined hand; the new inventory row repairs coverage without a C text or H text count. C_notes.txt contains one blank newline. One actual prior finite source-image-frame comparison by reader A is logged from the preserved script/report/manifest, without rerunning it. No mathematical theorem check was performed. Declared source placement maps are preserved; no rendered text extents or numerical curve bounds are asserted.')
        record['notes']=record['notes'].replace(
            'Its lower argument ends ce qui n\'est pas.',
            r'The displayed definition is `\Sigma_{12}\overset{\text{def}}{=}\Sigma_1^-\cap\Sigma_2^-`. '
            r'The two assertions after Notons are `\overline{\Sigma_{12}}\cap E_1\ne\varnothing` and `\overline{\Sigma_{12}}\cap E_2\ne\varnothing`. '
            r'The lower written argument starts with `\overline{\deleted{\unsure{E}}\Sigma_{12}}\cap\deleted{\unsure{\Sigma}}E_1=\varnothing` and subsequently writes `\overline{\Sigma_1^-}\cap E_1=\varnothing`. '
            'These are recorded as the page\'s written argument steps, with their predecessor qualifications preserved. Its lower argument ends ce qui n\'est pas.')
        record['workflow_note']=(
            'Three fresh independent readers A/B/C, fork_turns=none and no model override, brief v14. Their actual report timestamps, text sources and audits are preserved by fingerprint. Reader crop totals are A12, B17, C19. The root audit reports20 successful distinct local crop views:14 existing reader crops and6 new root crops, with no root whole-scan or supplied-half view. One initial A crop07 tool delivery returned no image; the same existing PNG was successfully delivered once afterward. All root choices through section20 are applied, including the archive inventory decision. Source-only clerical assembly used no image viewing, OCR, external research, compiler, renderer, numerical geometry or mathematical proof. The prior source-frame comparison belongs to reader A and is recorded as one actual event, separately from the unchanged raw reader empty check_events arrays. Root alone approves and commits the main record.')
        record['abbreviations'][1]={'form':'qfd|cqfd','expansion':"ce qu'il fallait démontrer (the supplied C expansion for the retained cqfd alternative)",
            'source':{'manifest':'packet.C_doubts.txt','line':33},'original_source_form':'cqfd [?]'}
        event=record['check_events'][0]
        event['source_provenance']=[
            {'manifest':'A.report.json','pointer':'/viewing_log/half_coordinate_verification'},
            {'manifest':'A.crop_manifest.json','pointer':'/halves'},
            line_span((OUT/'readers/016/A/make_crops.py').read_text(),8,12,'A.make_crops.py')]
        event['raw_reader_check_events']=[{'manifest':r+'.report.json','pointer':'/check_events','value':copy.deepcopy(reports[r]['check_events'])} for r in released]
        record['record_only_corrections']={'archive_inventory':{
            'element':'016-I46','root_decision_section':20,'reading':'15','hand':'undetermined hand',
            'source_C_text':'existing archive-number comment','source_C_inventory':'no dedicated original row',
            'C_count':0,'H_count':0,'basis':'Root section20 confirms the numeral and explicitly assigns inventory repair only.'}}
        inventory['I45'].update({'root_decision_section':18,'root_ink_choice_status':'common footer and final point confirmed by root'})
        inventory['I46'].update({'root_decision_section':20,'hand':'undetermined hand','hand_status':'explicit root decision, section20',
            'root_ink_choice_status':'archive comment and numeral confirmed; zero witness text counts'})
        record['root_choices_applied_through_section']=20
        record['root_source_only_confidence_clarification_applied']=clarification_heading in root_log
        record['source_counts']['remaining_doubt_clusters']=len(record['doubts'])
        record['source_counts']['S_physical_body_overbars']={'C':14,'H':14}
        record['source_counts']['H_extra_overbar_apparatus_reference']=1
    if attach_final:
        attach_final_sources(record,manifest)
    record['root_actions_pending']=[]
    if record['pending_root_decision_ids']:
        record['root_actions_pending'].append('Apply remaining explicit root choices and count flags: '+', '.join(record['pending_root_decision_ids']))
    if not attach_final:
        record['root_actions_pending'].append('Attach root-selected final TeX.')
    record['root_actions_pending'].append('Root alone may approve and commit the main record.')

    lines=['# Scan016 source union — '+('root choices complete' if not record['pending_root_decision_ids'] else 'root choices pending')+'\n',
      'This source-only union retains the actual witness text, independent reader returns, and original C table identities. Ink choices are attributed to exact sections of `checks/scan016_main_decisions.md`; `main_adjudicated` remains false.\n',
      '## Source scopes\n',
      'Thirteen actual C doubtful-reading rows map to nineteen primary physical clusters. The two final join clusters each retain predecessor and live-sign children; replacing those two parent scopes with four component scopes gives twenty-one local status entries. These scopes are recorded separately.\n',
      table(['Source','Difference rows','Doubt rows','Inventory rows'],[[r,len(v['differences']),len(v['doubts']),len(v['inventory'])] for r,v in reports.items()]+[['packet C','—',13,32]]),
      '\n## Canonical local union\n',
      table(['Locus','Original C rows','Location','Witness C','Witness H','Reader A','Reader B','Reader C','Root section / final'],[[d['id'],d.get('source_C_doubt_rows',[]),d['location'],d.get('C'),d.get('H'),d.get('readers',{}).get('A'),d.get('readers',{}).get('B'),d.get('readers',{}).get('C'),[d.get('root_decision_section'),d.get('final')]] for d in record['decisions']]),
      '\n## Per-locus root counts and statuses\n',
      table(['Locus','Root section','Confidence','C count','H count','C doubt status','Counting parent / class'],
          [[d['id'],d.get('root_decision_section'),d.get('confidence'),d.get('diff_C'),d.get('diff_H'),d.get('C_doubt_status'),
            d.get('C_count_parent',d.get('C_change_class',d.get('count_policy','pending root basis')))] for d in record['decisions']]),
      '\n## Actual C doubt identities\n',
      table(['Original row','Source line','Primary clusters','Status components','Root local statuses'],[[d['source_row'],d['source_line'],d['primary_local_decision_ids'],d['local_status_decision_ids'],d['local_statuses']] for d in original_map]),
      '\n## Every returned difference row\n',table(['Reader','Pointer','Source ID','Union loci'],[[d['reader'],d['pointer'],d['source_id'],d['loci']] for d in diff_crosswalk]),
      '\n## Every returned doubt row\n',table(['Reader','Pointer','Source difference IDs','Union loci'],[[d['reader'],d['pointer'],d['source_difference_ids'],d['loci']] for d in doubt_crosswalk]),
      '\n## Deduplicated inventory\n',table(['Union element','Kind','Position','Content','Source rows'],[[v['element'],v['kind'],v['position'],v['first_words_or_objects'],v['source_inventory']] for v in record['inventory']]),
      '\n## Every inventory source row\n',table(['Source','Pointer','Source ID','Union elements'],[[d['source'],d['pointer'],d['source_id'],d['targets']] for d in inv_crosswalk]),
      '\n## Preserved source disagreements and count rules\n',
      '- A and B retain slash/setminus while C resolves the slash. B retains donc/d’où while A and C resolve donc; each original doubt identity remains unchanged.\n- A resolves cqfd, B prefers qfd with cqfd retained, and C keeps cqfd first under qualification. A retains égale, B prefers égal with égale retained, and C qualifies a final e separately from its new accent qualification.\n- C resolves the colon; A/B keep à as an alternative with colon first.\n- A qualifies final-join chronology/state and form together while reporting the square-join components clear; B resolves both predecessors and live cups, and C resolves predecessors while retaining the live cup/amalg questions. Each raw A combined source row remains mapped to its physical parent and both separately variable components. Two physical join counts and four component statuses remain separate.\n- A resolves raised en while B/C retain en/on. All three resolve conclurait, with local confidence differences preserved.\n- B’s right-note graphic groups four commands. The union preserves its two upper-rule runs, lower guide and detached return. A/C represent the return once as the following comma. Root section02 selects the one comma and the separate upper/lower guide records.\n- C records the central point, the two central brace contours, lower underbrace contour and observed closing-bracket returns. B retains conventional brace/bracket forms in its source.\n- C/H each contain fourteen physical/body closure-bar occurrences. H repeats one bar in its descriptive underbrace apparatus; that reference adds no physical bar locus. All fourteen local scopes are logged under S SA01-K81-06. Root confirmations alone add no witness error.\n- Retained C doubts supply no C count unless root identifies a changed primary reading or a distinct source qualification. New qualifications, actual resolutions, and primary reversals remain distinguishable. H uncertainty alone supplies no count.\n- Small marks retain qualified hand, role and surface-origin labels. No geometry or mathematical proof is inferred. One actual prior finite source-image-frame comparison by A is logged on the root’s explicit instruction and was not rerun.\n',
      '\n## Pending root work\n\n'+ '\n'.join('- '+v for v in record['root_actions_pending'])+'\n']
    if attach_final:
        lines.extend(['\n## Selected-source attachment summary\n',
          'Exact selected-source spans are recorded for decisions, remaining doubts and inventory elements through `checks/scan016_final_source_map.json`. The record preserves compact character-offset attachments and links each to the original selected component.\n',
          table(['Scope','Attached entries','Pending entries'],[
            ['Decisions',sum(bool(d['final_source_attachment']) for d in record['decisions']),record['final_source_missing_attachments']['decisions']],
            ['Inventory',sum(bool(i['root_page_sources']) for i in record['inventory']),record['final_source_missing_attachments']['inventory']],
            ['Remaining doubt clusters',sum(bool(d['root_page_sources']) for d in record['doubts']),record['final_source_missing_attachments']['doubts']]])])
    (CHECKS/'scan016_record_draft.json').write_text(json_text(record))
    (CHECKS/'scan016_reader_fingerprints.json').write_text(json_text(manifest))
    (CHECKS/'scan016_union.md').write_text('\n'.join(lines))
    print(json.dumps({'released_readers':released,'difference_source_rows':len(diff_crosswalk),'doubt_source_rows':len(doubt_crosswalk),'inventory_source_rows':len(inv_crosswalk),'union_decisions':len(decisions),'union_inventory':len(inventory),'main_adjudicated':False},ensure_ascii=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--released',nargs='+',choices=['A','B','C'],required=True)
    parser.add_argument('--attach-final',action='store_true')
    args=parser.parse_args()
    build(args.released,args.attach_final)
