#!/usr/bin/env python3
"""Mechanical source collation only; no images, OCR, mathematics or compilation.

Writes only scan011_record_draft.json and scan011_mapping.md beside this script.
The root's own written crop decisions supply every populated final decision.
All source identities are retained by compact references and exact local readings.
"""
from pathlib import Path
import json
import hashlib
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'out/checks'
READERS = 'ABC'
report_paths = {r: f'out/readers/011/{r}/report.json' for r in READERS}
tex_paths = {r: f'out/readers/011/{r}/reading.tex' for r in READERS}
audit_paths = {r: f'out/readers/011/{r}/reading.md' for r in READERS}
reports = {r: json.loads((ROOT / report_paths[r]).read_text()) for r in READERS}
tex = {r: (ROOT / tex_paths[r]).read_text().splitlines() for r in READERS}
source_rows = {r: {x['id']: (i, x) for i, x in enumerate(reports[r]['differences'])} for r in READERS}
metadata = json.loads((ROOT / 'packets/011/metadata.json').read_text())
witness_inventory = json.loads((ROOT / 'packets/011/C_inventory.json').read_text())
root_log_path = 'out/checks/scan011_main_decisions.md'
root_log = (ROOT / root_log_path).read_text()
root_events_path = 'out/checks/scan011_check_events.json'
root_events = json.loads((ROOT / root_events_path).read_text())
root_page_path='out/pages/J81-02_81_scan011.tex'
root_page_lines=(ROOT/root_page_path).read_text().splitlines() if (ROOT/root_page_path).exists() else []
ROOT_FOLLOWUP_EXACT = """Root dispositions: D27 absent semicolon, Cfalse Htrue high; crop B/02 (blank endpoint space and separately placed lower expression confirmed). D68 lower-left arrow already represented by C; final retain arrow direction/head, Cfalse Hfalse, high, crop C/13 shows its head; no separate count, covered whole diagram. D50 short branches extents/weight/endtip refinement makes Ctrue (actual graphic change from full schematic lines), high. D09 H acknowledged unspecified predecessor state but omitted recovered candidate glyph: Htrue for candidate omission only; explicitly state state already acknowledged, low candidate. D14 Ctrue Hfalse: H already biffe, no extra H cancellation-state omission; geometry countedC. D62 Htrue, high: H5raydescription vs3through-directions with6visible ends plus missingfinepaths; onephysicalsketchcount. D66 wholeHdiagram high supportedstructural differences, note its Y/V remainsqualified notconclusiveglypherror. Confidences: D10medium,D13high,D14high,D19low(state),D20medium,D23high,D24high,D25high,D34high,D35high,D37medium,D48medium,D49medium,D51high(noindependentcount),D54high,D55high,D57high,D58high,D59medium,D60medium,D61medium,D65high,D67high,D80medium. Root page written out/pages/J81-02_81_scan011.tex by checks/write_scan011.py; structural check passed. Reconcile reading-path/inventory without images and flag missing details. Source72–76 page has one additional tiny right-bottom polygon projection in same root04 crop; includeD76geometry foot+right-bottom corner detail, no newrow requiredsameboundaryrefinement. Source phrase inlogtopE font sameH note explicit."""

def ref(path, pointer=None, lines=None):
    v = {'path': path}
    if pointer is not None: v['pointer'] = pointer
    if lines is not None: v['line_start'], v['line_end'] = lines
    return v

def report_ref(reader, row_id):
    index, _ = source_rows[reader][row_id]
    return ref(report_paths[reader], f'/differences/{index}') | {'row_id': row_id}

def compact_id(reader, suffix):
    return 'B011.' + suffix if reader == 'B' else suffix

def R(a='', b='', c=''):
    return {r: [compact_id(r, x) for x in words.split()] for r, words in zip(READERS, (a,b,c))}

# Each source row may support several independently located subloci. Its source
# identity remains one row in actual_C_doubt_map below.
SPECS = []
def add(n, location, C, H, rows, source_row=None, local=None, region=None,
        hgroup=None, role='local', note=None):
    SPECS.append(dict(n=n, location=location, C=C, H=H, rows=rows,
                      source_row=source_row, local=local, region=region,
                      hgroup=hgroup, role=role, note=note))

add(1,'Detached upper-edge sign',r'\unsure{=|\Rightarrow}','[omitted]',R('A01','D01','CD01'),1,'edge sign','edge')
add(2,'Upper-left P alphabet',r'\unsure{P|\mathbb{P}}',r'\mathbb{P}',R('A02','D02','CD02'),2,'P alphabet','upper_left')
add(3,'Upper-left X: detached upper-left terminal and four end strokes','X','X',R('A02','G01','CD02'),region='upper_left',note='A and C discuss the terminal but use the X glyph; B supplies explicit paths. This is a construction/geometry proposal, separate from P.')
add(4,'Top product, leading P alphabet','P',r'\mathbb{P}',R('A16','H01','H01'),region='top_product')
add(5,'Top product, first rounded Z',r'\unsure{Z|2}','Z',R('A03a','D03a','CD03a'),3,'top product rounded Z','top_product')
add(6,'Top Hom product, live angular Z','Z','Z',R('A03b','D03b','CD03b'),3,'top-right product live Z','top_hom')
add(7,'Central inner Hom(X,Z), rounded Z recurrence','Z','Z',R('','','CD03c'),3,'central Hom rounded Z','central',note='A/B audit this recurrence in notation and reading.md; C gives its own local report row. The first per-page Z/2 marker carries the recurrence qualification.')
add(8,'Central P(Hom(X,Z), rounded Z recurrence','Z','Z',R('','','CD03d'),3,'central P(Hom rounded Z','central_lower',note='A/B audit this recurrence in notation and reading.md; C gives its own local report row. No new source row is created.')
add(9,'Predecessor beneath top-right Z',r'\deleted{\unsure{\mathcal E|e}}',r'\note{une première lettre surchargée en $Z$}',R('A04','D04','CD04'),4,'top Z predecessor','top_hom',note='H expressly records overwriting but supplies no precursor candidate. A reports no H difference; B/C report a difference. Root classification remains explicit.')
add(10,'Detached small point immediately below top-right overwritten factor','[omitted]','[omitted]',R('','','N01'),region='top_hom')
add(11,'Final argument of top Hom',r'\unsure{\mathscr E|\mathcal E}',r'\mathcal{E}; note: une grande capitale bouclée',R('A05','D05','CD05'),5,'top final E','top_hom')
add(12,'Cancelled Hom expression and terminal closure',r'\deleted{\unsure{\operatorname{Hom}(X)|\operatorname{Hom}(X,)}}',r'\struck{$\underline{\mathrm{Hom}}(X)$}',R('A06','D06','CD06'),6,'cancelled Hom text','cancelled')
add(13,'Cancelled Hom, independent underline reading','No independent underline',r'\underline{\mathrm{Hom}}(X)',R('A30','H02','H02'),region='cancelled')
add(14,'Cancelled Hom cluster, crossing paths and endpoint geometry','Generic deleted wrappers and overset group','biffé',R('A41','D06','G01'),region='cancelled',note='Visible-path proposals are kept separate from the already-shared cancellation state. A reports no H geometry difference; C reports one; root decides the H classification.')
add(15,'First raised shape over cancelled Hom, glyph',r'\deleted{\unsure{M|U}}','[three raised forms omitted]',R('A15a','D15a','CD15a'),15,'first raised M/U glyph','cancelled',hgroup='011-HG02')
add(16,'First raised M/U, cancellation target/state',r'\deleted{\unsure{M|U}}','[included in raised-form omission]',R('A42','D15a','CD15a'),region='cancelled',hgroup='011-HG02',note='New state qualification belongs to the same written glyph but does not create a sixteenth C source-doubt row.')
add(17,'Middle raised shape over cancelled Hom',r'\deleted{\unsure{H|X}}','[included in raised-form omission]',R('A15b','D15b','CD15b'),15,'middle raised H/X glyph','cancelled',hgroup='011-HG02')
add(18,'Last raised shape over cancelled Hom, glyph',r'\deleted{\unsure{R|P}}','[included in raised-form omission]',R('A15c','D15c','CD15c'),15,'last raised R/P glyph','cancelled',hgroup='011-HG02')
add(19,'Last raised R, cancellation target/state',r'\deleted{\unsure{R|P}}','[included in raised-form omission]',R('A43','D15c','CD15c'),region='cancelled',hgroup='011-HG02',note='The R/P source glyph question and the later state qualification stay separately traceable; source row 15 is counted once.')
add(20,'Detached mark above initial cancelled Hom upright','[omitted]','[omitted]',R('A40','','N02'),region='cancelled')
add(21,'Live operator below cancelled expression',r'\unsure{\operatorname{Hom}}',r'\mathrm{Hom}',R('A07a','D07a','CD07a'),7,'live outer Hom operator','live')
add(22,'Live inner Hom, first argument',r'\unsure{\mathscr E|Z}','Z',R('A07b','D07b','CD07b'),7,'live inner first argument','live',note='A/C report the entire argument pair together; B has one row for each position. The exact pair remains available in both combined rows.')
add(23,'Live inner Hom, final argument','Z',r'\mathcal{E}',R('A07b','H03','CD07b'),region='live',note='Mapped separately from the first-argument source-doubt sublocus; no additional C doubt is assigned.')
add(24,'Live nested Hom, terminal delimiter count','One final closing parenthesis','Two final closing parentheses',R('A22','H04','H03'),region='live')
add(25,'Upper pair of parallel oblique strokes, orientation and placement',r'\mathrel{/\!/}','=',R('A20','H05','H04'),region='cancelled')
add(26,'Left second-line oval',r'\unsure{O|0}','O',R('A08','D08','CD08'),8,'left second-line O/0','left_second')
add(27,'Punctuation between the two left expressions','[no semicolon]',';',R('A26','H14','H05'),region='upper_left')
add(28,'Central pair of parallel oblique strokes',r'\mathrel{/\!/}','=',R('A21','H06','H06'),region='central_lower')
add(29,'Central P(Hom...), P alphabet','P',r'\mathbb{P}',R('A17','H07','H07'),region='central_lower')
add(30,'Central P(Hom...), Hom underline',r'\operatorname{Hom}',r'\underline{\mathrm{Hom}}',R('A24','H08','H08'),region='central_lower')
add(31,'Central P(Hom...), terminal delimiter count','One final closing parenthesis','Two final closing parentheses',R('A23','H09','H09'),region='central_lower')
add(32,'First lower inclusion, P alphabet','P',r'\mathbb{P}',R('A18','H10','H10'),region='lower_first')
add(33,'First lower inclusion, terminal comma','[no comma]',',',R('A27','H13','H11'),region='lower_first')
add(34,'Second lower inclusion, Hom underline',r'\operatorname{Hom}',r'\underline{\mathrm{Hom}}',R('A25','H12','H12'),region='lower_second')
add(35,'Second lower inclusion, P alphabet','P',r'\mathbb{P}',R('A19','H11','H13'),region='lower_second')
add(36,'Second lower inclusion, predecessor beneath live Z',r'\deleted{\unsure{t|1}}','[omitted]',R('A09','D09','CD09'),9,'lower Z predecessor','lower_second')
add(37,'Detached bent trace and points above lower overwritten Z','[omitted]','[omitted]',R('A38','G02','N03'),region='lower_second',note='A draws one detached point; B/C draw a second pale point. Preserve this local graphic disagreement as well as the shared shape/role qualification.')
add(38,'Diagram, raised cancelled H above X',r'\deleted{\unsure{H|U}}','[omitted]',R('A10a','D10a','CD10a'),10,'raised diagram H','diagram',hgroup='011-HG01')
add(39,'Diagram, arch below raised H',r'\unsure{\frown}','[omitted]',R('A10b','D10b','CD10b'),10,'diagram arch','diagram',hgroup='011-HG01')
add(40,'Diagram, predecessor beneath first P',r'\deleted{\unsure{H|R}}','P only',R('A11a','D11a','CD11a'),11,'diagram first P predecessor','diagram',hgroup='011-HG01')
add(41,'Diagram, looped predecessor beneath first multiplication sign',r'\deleted{\unsure{e}}',r'\times only',R('A11b','D11b','CD11b'),11,'diagram multiplication predecessor','diagram',hgroup='011-HG01')
add(42,'Diagram, crossed label beside downward arrow',r'\deleted{\unsure{U|H}}','[omitted]',R('A12','D12','CD12'),12,'diagram crossed arrow-side label','diagram',hgroup='011-HG01')
add(43,'Diagram, overwritten H beneath rightmost object',r'\deleted{\unsure{H|F}}','H live',R('A13a','D13b','CD13'),13,'underlying right-object H','diagram',hgroup='011-HG01')
add(44,'Diagram, heavy live rightmost object',r'\unsure{\Gamma|F}','H',R('A13b A13a','D13a','CD13'),13,'live right-object Gamma','diagram',hgroup='011-HG01')
add(45,'Diagram, lower large letter left of horizontal arrow',r'\unsure{V|W}','V',R('A14a','D14b','CD14b'),14,'lower large V/W','diagram',hgroup='011-HG01')
add(46,'Diagram, subscript between the U factors',r'\unsure{V|Y}','V',R('A14b','D14a','CD14a'),14,'product subscript V/Y','diagram',hgroup='011-HG01')
add(47,'Diagram, unequal long and short rules beside lower-left P',r'{\big|}\,P','P only',R('A37','G04','N05'),region='diagram',hgroup='011-HG01',note='A/B/C have different explicit lower-start positions for the shorter rule; exact source paths are preserved by references.')
add(48,'Diagram, dark detached spot left of downward arrowhead','[omitted]','[omitted]',R('A39','G05','N04'),region='diagram',hgroup='011-HG01')
add(49,'Diagram, pale detached spot below-right of downward arrowhead','[omitted]','[omitted]',R('','G05',''),region='diagram',hgroup='011-HG01',note='B reports two spots; A/C report only the left dark spot. Keep the pale spot as its own local candidate.')
add(50,'Diagram, two short descending unheaded branches above bottom P','Two dash links','V leftarrow U au-dessus d’un P; branches not specified',R('A45','G06','G03'),region='diagram',hgroup='011-HG01',note='C source conveys both links. A/B supply dark/pale explicit paths and endpoint details; C-reader shortens the tikz-cd links. Root determines any physical-geometry change count.')
add(51,'Diagram, cancellation paths and overlapping predecessor placement','Generic deletion wrappers and separated tokens','Local candidate text in whole-diagram description',R('A44','','CD10a CD12 CD13'),region='diagram',hgroup='011-HG01',note='This composite geometry audit cross-references D38,D40,D41,D42,D43,D44. Root must assign any independent physical change count; wrapper syntax alone is excluded.')
add(52,'Detached mark above-left of long diagram upright','[omitted]','[omitted]',R('','','N06'),region='diagram',hgroup='011-HG01')
add(53,'Upper sketch, interrupted rising diagonal and small junction head','Continuous diagonal ends at (87,163); no separate short head','General petal/ray description',R('A28','G03','G02'),region='upper_sketch',hgroup='011-HG03',note='A breaks the diagonal and draws a hooked head; B retains the C diagonal and adds two short strokes; C retains it and adds a curl plus gray fragment.')
add(54,'Upper sketch, short detached bowed dash','[omitted]','Not individually described',R('A29','','G02'),region='upper_sketch',hgroup='011-HG03')
add(55,'Upper sketch, small inner J-shaped return','[omitted]','Not individually described',R('A31','','G02'),region='upper_sketch',hgroup='011-HG03')
add(56,'Upper sketch, thick vertical segment below centre','Thick path continues (111,337)--(121,383)','épaisse au-dessus du centre',R('A32','','G02'),region='upper_sketch',hgroup='011-HG03',note='Only A shortens the thick segment to its centre. B/C retain the longer explicit C thick path; C G02 concerns fine additions and does not report this thickness as changed.')
add(57,'Upper sketch, second lower rim arc','One closed disk rim','Small disk, no local rim detail',R('A33','','G02'),region='upper_sketch',hgroup='011-HG03')
add(58,'Upper sketch, returning lower-right ray endpoint','Straight endpoint','Not individually described',R('A34','','G02'),region='upper_sketch',hgroup='011-HG03')
add(59,'Upper sketch, narrow loop continuing the right petal at disk rim','Path ends at (145,317)','Not individually described',R('A35','',''),region='upper_sketch',hgroup='011-HG03')
add(60,'Upper sketch, short lower shaft branch','One descending end','Not individually described',R('A36','','G02'),region='upper_sketch',hgroup='011-HG03')
add(61,'Upper sketch, small hook at upper end of outer descending path','No separate upper hook','Not individually described',R('','','G02'),region='upper_sketch',hgroup='011-HG03')
add(62,'Upper-left physical sketch: H description as a whole','Upper disk, rays, loops and outer arrow, with local proposed details','One sketch described at H lines 3–5; five centre rays, three extending beyond rim; heavy segment above centre',R('A46 A28 A29 A31 A32 A33 A34 A35 A36','G03','G02'),region='upper_sketch',hgroup='011-HG03',role='H structural group',note='One physical upper sketch. Repeated H note/drawing descriptions create no second sketch identity. Local omitted paths do not each create H rows.')
add(63,'Bottom-left physical polygon sketch','C lower-left paths','Six-sided polygon, two consecutive heavy lower sides, small circle and thin tangle',R('A47','G07','G04'),region='bottom_left',hgroup='011-HG04',role='H structural group')
add(64,'Bottom-middle physical angular sketch','C middle paths','Thick open V doubled by thin strokes',R('A47','G07','G05'),region='bottom_middle',hgroup='011-HG05',role='H structural group')
add(65,'Bottom-right physical oval sketch','C oval paths and localized zigzags','Ellipse crossed by six nearly vertical curves',R('A47','G07','G06'),region='bottom_right',hgroup='011-HG06',role='H structural group')
add(66,'Right-hand diagram as one H structural locus','Complete C diagram with qualified local predecessors/marks','P×X×Y ⊃ H; H→P×X; downward arrow; P×X→P; U×_V U; V←U above P',R('A10a A10b A11a A11b A12 A13a A13b A14a A14b A37 A39 A44 A45','D10a D10b D11a D11b D12 D13a D13b D14a D14b G04 G05 G06','CD10a CD10b CD11a CD11b CD12 CD13 CD14a CD14b N04 N05 N06 G03'),region='diagram',hgroup='011-HG01',role='H structural group',note='Local H quoted candidates and source flags remain available. Only this structural parent can carry the whole-diagram H count.')
add(67,'Diagram lower horizontal arrow, repeated shaft/return and head extension','Single tikz-cd left arrow',r'V\leftarrow U',R('A14a','D14b','CD14b'),region='diagram',hgroup='011-HG01',note='Source-level geometry: A adds a curved return and upper tip extension; B adds an extra head stroke; C uses the standard left arrow. The glyph source-doubt row is D45, not this geometry audit.')
add(68,'Diagram lower-left oblique arrow, weight and head geometry','Standard down-left tikz-cd arrow',r'P\times X\to P',R('A44','G04',''),region='diagram',hgroup='011-HG01',note='A/B explicitly give a heavy shaft/head; C-reader retains the tikz-cd connection. This source geometry candidate remains for root disposition.')
add(69,'Diagram bottom P, detached lower continuation','P only','P only',R(),region='diagram',hgroup='011-HG01',note='Root-only locus in paragraph 11: separate near-vertical dark continuation beneath P, with a small gap. All reader sources give only P.')
add(70,'Diagram lower-left P, pale upright/hook immediately above cap','[omitted]','[omitted]',R(),region='diagram',hgroup='011-HG01',note='Root-only locus in paragraph 12, approximately full x1187–1196,y855–880. Lower part meets P cap; no character supplied.')
add(71,'Tiny detached curved/dashed mark left of first lower Hom','[omitted]','[omitted]',R(),region='lower_first',note='Root-only locus in paragraph 18, approximately full (374,651)–(386,661).')
add(72,'Compact trace group beneath second lower right-member P','[omitted]','[omitted]',R(),region='lower_second',note='Root-only locus in paragraph 19: short left dash, two joined short humps, and right short upright; x824–853,y850–864.')
add(73,'Dot and pale fragments beneath second lower right-member Z','[omitted]','[omitted]',R(),region='lower_second',note='Root-only locus in paragraph 19; x938–973,y837–847.')
add(74,'Bottom-left polygon, upper slanted boundary interruptions','One continuous upper slanted segment','Overall polygon description',R(),region='bottom_left',hgroup='011-HG04',note='Root-only detail in paragraph 20: two light gaps between three segments and separate gap at upper-left meeting.')
add(75,'Bottom-left polygon, upper-right vertex prongs','[not separately represented]','Overall polygon description',R(),region='bottom_left',hgroup='011-HG04',note='Root-only detail in paragraph 20: small endpoint prongs.')
add(76,'Bottom-left polygon, lower-left foot projection','[not separately represented]','Overall polygon description',R(),region='bottom_left',hgroup='011-HG04',note='Root-only detail in paragraph 20: short projecting stroke.')
add(77,'Bottom-middle angular sketch, hooked tick below left elbow','[omitted]','Overall angular sketch description',R(),region='bottom_middle',hgroup='011-HG05',note='Root-only detail in paragraph 21.')
add(78,'Bottom-middle angular sketch, two projections at right elbow','[omitted]','Overall angular sketch description',R(),region='bottom_middle',hgroup='011-HG05',note='Root-only detail in paragraph 21: two short projecting strokes at one local elbow.')
add(79,'Bottom-middle angular sketch, detached spot above central gap','[omitted]','[omitted]',R(),region='bottom_middle',hgroup='011-HG05',note='Root-only locus in paragraph 21, approximately full x565–571,y963–970.')
add(80,'Diagram downward arrowhead, retraced crossing/loop geometry','Standard arrowhead','Downward arrow description',R(),region='diagram',hgroup='011-HG01',note='Root paragraph 10 records this additional visible arrowhead detail; no report gives its own row.')

# Compact line regions: endpoints are recomputed from stable source anchors so
# reader finalization can change line numbering without changing source identity.
def find_line(reader, needle, occurrence=1):
    xs = [i+1 for i,l in enumerate(tex[reader]) if needle in l]
    return xs[occurrence-1] if len(xs) >= occurrence else None

def region_lines(reader, region):
    ls = tex[reader]
    diagrams = [i+1 for i,l in enumerate(ls) if l.startswith(r'\diagram{')]
    figures = [i+1 for i,l in enumerate(ls) if l.startswith(r'\figure{')]
    f1, f2 = figures[0], figures[-1]
    d = diagrams[0]
    if region == 'edge': return (3,3)
    if region == 'upper_left':
        start=find_line(reader,r'\mathbb')
        end=find_line(reader,r'P(X\times\unsure{Z|2})')-1
        return (start,end)
    if region == 'top_product':
        k=find_line(reader,r'P(X\times\unsure{Z|2})'); return(k,k)
    if region == 'top_hom':
        k=find_line(reader,r'\operatorname{Hom}('); return(k,k)
    if region == 'cancelled':
        if reader=='A': return(find_line(reader,r'\mathrel{/\!/}'),find_line(reader,r'\operatorname{Hom}(X,\underline')-2)
        if reader=='B': return(find_line(reader,r'\hspace{6em}'),find_line(reader,r'\hspace{9em}')-1)
        return(find_line(reader,r'&\qquad\mathrel{/\!/}'),find_line(reader,r'\unsure{O|0}')-1)
    if region == 'live':
        k=find_line(reader,r'\operatorname{Hom}(X,\underline')
        if k is None: k=find_line(reader,r'\unsure{\operatorname{Hom}}(X,\underline')
        return(k,k)
    if region == 'left_second':
        k=find_line(reader,r'\unsure{O|0}'); return(k,k)
    if region == 'central':
        k=find_line(reader,r'\operatorname{Hom}(\mathscr E,\underline'); return(k,k)
    if region == 'central_lower':
        k=find_line(reader,r'P(\operatorname{Hom}(X,Z)'); return(k-1,k)
    if region == 'lower_first':
        k=find_line(reader,r'\underline{\operatorname{Hom}}(X,Y)'); return(k,k)
    if region == 'lower_second':
        k=find_line(reader,r'\underline{\operatorname{Hom}}(X,Y)'); return(k+1,d-1)
    if region == 'upper_sketch': return(f1,find_line(reader,r'\underline{\operatorname{Hom}}(X,Y)')-2)
    if region == 'diagram': return(d,f2-1)
    if region == 'bottom_left':
        return(find_line(reader,r'\draw (13,425)'),find_line(reader,r'\draw (319,271)')-1)
    if region == 'bottom_middle':
        return(find_line(reader,r'\draw (319,271)'),find_line(reader,r'\draw (627,259)')-1)
    if region == 'bottom_right':
        return(find_line(reader,r'\draw (627,259)'),find_line(reader,'% archive sheet number: 10')-1)
    return(1,len(ls))

def tex_ref(reader, region):
    start,end = region_lines(reader,region)
    v=ref(tex_paths[reader],lines=(start,end))
    if start is not None and end is not None and end-start<=2:
        v['exact_excerpt']='\n'.join(tex[reader][start-1:end])
    return v

def local_candidate(spec, reader):
    ids=spec['rows'][reader]
    v={'report_row_ids':ids,'tex':tex_ref(reader,spec['region'])}
    if not ids:
        v['mapping_note']='No separate difference row for this sublocus; the exact proposed source region is referenced. This does not infer a visual decision.'
    return v

decisions=[]
for s in SPECS:
    provenance={r:local_candidate(s,r) for r in READERS}
    readers={r:'; '.join(source_rows[r][rid][1]['reading'] for rid in s['rows'][r]) or
             '[no separate report row; exact reading.tex region referenced]' for r in READERS}
    if s['role']=='H structural group':
        readers={r:'Complete physical-object source referenced; exact local candidates occur in the child decision rows.' for r in READERS}
    crops=sorted({f"out/readers/011/{r}/{source_rows[r][rid][1]['readers_crop']}"
                  for r in READERS for rid in s['rows'][r]
                  if source_rows[r][rid][1].get('readers_crop')})
    decisions.append({'id':f"011-D{s['n']:02d}",'location':s['location'],
      'C':s['C'],'H':s['H'],'final':None,'evidence':None,'crop':None,
      'confidence':None,'kind':None,'diff_C':None,'diff_H':None,
      'marked_in_H':None,'C_doubt_status':None,
      'C_doubt_source_row':s['source_row'],'C_doubt_sublocus':s['local'],
      'root_decided':False,'main_approval_pending':True,
      'readers':readers,'reader_provenance':provenance,
      'candidate_crop_references':crops,'role':s['role'],
      'H_count_group':s['hgroup'],'count_locus_key':f"scan011-physical-{s['n']:02d}",
      'main_counting_decision_pending':True,'assembly_note':s['note'],
      'root_decision_source':None})
byid={x['id']:x for x in decisions}

# Root-authored statements are copied as evidence. All unspecified categories and
# counts remain pending rather than being decided by this assembler.
root_paragraphs={int(n):t.strip() for n,t in re.findall(r'(?ms)^(\d+)\. (.*?)(?=^\d+\. |\Z)',root_log)}
def root_decision(n, paragraph, final, confidence, diff_C=None, diff_H=None,
                  status=None, kind=None, crop=None, qualification=None):
    if paragraph not in root_paragraphs: return
    d=byid[f'011-D{n:02d}']
    d.update(final=final,confidence=confidence,evidence=root_paragraphs[paragraph],
             root_decided=True,diff_C=diff_C,diff_H=diff_H,C_doubt_status=status,
             kind=kind,crop=crop,
             root_decision_source=ref(root_log_path,f'numbered-entry-{paragraph}'))
    d['qualification']=qualification
    # A populated reading is never a main approval.
    d['main_approval_pending']=True

root_decision(1,1,r'\unsure{=|\Rightarrow}','low',False,True,'retained','omission','out/readers/011/C/01_edge.png')
root_decision(2,2,r'\mathbb P','high',True,False,'resolved','other','out/readers/011/B/02_upper_left.png')
root_decision(3,2,'B explicit X paths with four endpoint strokes and detached upper-left serif','high',True,True,None,'drawing or diagram','out/readers/011/B/02_upper_left.png')
root_decision(4,3,'P','high',False,True,None,'misread symbol or index','out/readers/011/C/03_top_product.png')
root_decision(5,3,r'\unsure{Z|2}','medium',False,False,'retained','other','out/readers/011/C/03_top_product.png')
root_decision(6,4,'Z','high',True,False,'resolved','other','out/readers/011/C/04_top_right.png')
root_decision(9,4,r'\deleted{\unsure{e|\mathcal E}}','low',True,None,'retained',None,'out/readers/011/C/04_top_right.png','Former E-first candidate survives as an explicit alternative; H acknowledges the overwrite and supplies no precursor candidate.')
root_decision(10,4,'Detached small dark point below factor; role, hand and origin unknown',None,True,True,None,'omission','out/readers/011/C/04_top_right.png')
root_decision(11,4,r'\mathscr E','medium',True,False,'resolved','other','out/readers/011/C/04_top_right.png')
root_decision(12,5,r'\deleted{\operatorname{Hom}(X)}','high',True,False,'resolved','other','out/readers/011/C/05_crossed_cluster.png')
root_decision(13,5,'No independent Hom underline; preserve crossing strokes',None,False,True,None,None,'out/readers/011/C/05_crossed_cluster.png')
root_decision(14,5,'Separate transverse/rising cancellation paths with their endpoints; no additional independent underline',None,True,None,None,'drawing or diagram','out/readers/011/C/05_crossed_cluster.png')
root_decision(15,5,r'\unsure{M|U}','low',False,False,'retained',None,'out/readers/011/C/05_crossed_cluster.png','H omission of the three-form group is counted once through 011-HG02; glyph and state qualification remain locally separate.')
root_decision(16,5,'Explicit cancelled/live alternatives for M/U','low',True,False,None,'deletion state (struck given live or live given struck)','out/readers/011/C/05_crossed_cluster.png')
root_decision(17,5,r'\deleted{H}','medium',True,False,'resolved','other','out/readers/011/C/05_crossed_cluster.png')
root_decision(18,5,'R','high',True,False,'resolved','other','out/readers/011/C/05_crossed_cluster.png')
root_decision(19,5,'Explicit cancelled/live alternatives for R',None,True,False,None,'deletion state (struck given live or live given struck)','out/readers/011/C/05_crossed_cluster.png')
root_decision(20,5,'Small detached dark mark above initial cancelled H; role and hand unknown',None,True,True,None,'omission','out/readers/011/C/05_crossed_cluster.png')
root_decision(21,6,r'\operatorname{Hom}','medium',True,False,'resolved','other','out/readers/011/C/05_crossed_cluster.png')
root_decision(22,6,r'\mathscr E','medium',True,True,'resolved',None,'out/readers/011/C/05_crossed_cluster.png')
root_decision(23,6,'Z',None,False,True,None,None,'out/readers/011/C/05_crossed_cluster.png')
root_decision(24,6,'One final closing parenthesis',None,False,True,None,'text not on the page','out/readers/011/C/05_crossed_cluster.png')
root_decision(25,6,r'\mathrel{/\!/}, to the left of the cancelled line',None,False,True,None,'insertion or placement','out/readers/011/C/05_crossed_cluster.png')

root_decision(7,8,'Z under first-occurrence Z/2 qualification','medium',False,False,'retained','other','out/readers/011/C/08_middle_hom.png')
root_decision(8,17,'Z under first-occurrence Z/2 qualification','medium',False,False,'retained','other','out/crops/011/root_01_middle_P.png')
root_decision(26,7,r'\unsure{O|0}','medium',False,False,'retained','other','out/readers/011/C/06_left_second.png')
root_decision(28,17,r'\mathrel{/\!/} on the separate intervening level','high',False,True,None,'insertion or placement','out/crops/011/root_01_middle_P.png')
root_decision(29,17,'P','high',False,True,None,'misread symbol or index','out/crops/011/root_01_middle_P.png')
root_decision(30,17,r'\operatorname{Hom}, no underline','high',False,True,None,'text not on the page','out/crops/011/root_01_middle_P.png')
root_decision(31,17,'One final closing parenthesis','high',False,True,None,'text not on the page','out/crops/011/root_01_middle_P.png')
root_decision(32,18,'P','high',False,True,None,'misread symbol or index','out/crops/011/root_02_lower_first.png')
root_decision(33,18,'No terminal comma','high',False,True,None,'text not on the page','out/crops/011/root_02_lower_first.png')
root_decision(34,15,r'\operatorname{Hom}, no underline',None,False,True,None,'text not on the page','out/readers/011/C/09_last_hom.png')
root_decision(35,19,'P',None,False,True,None,'misread symbol or index','out/crops/011/root_03_lower_second_right.png')
root_decision(36,15,r'\deleted{\unsure{t|1}}Z','low',False,True,'retained','omission','out/readers/011/C/09_last_hom.png')
root_decision(37,15,'Detached shallow wave and two separated spots, graphically qualified',None,True,True,None,'drawing or diagram','out/readers/011/C/09_last_hom.png','Unknown hand, surface origin and role; the second pale spot in B/C is included.')
root_decision(38,9,r'\deleted{H}, with oblique crossing paths and extended lower right stem','high',True,False,'resolved','other','out/readers/011/C/10_diagram_top.png')
root_decision(39,9,'Independent downward-open arch without arrowhead','high',True,False,'resolved','other','out/readers/011/C/10_diagram_top.png')
root_decision(40,9,r'\deleted{\unsure{H|R}}P','low',False,False,'retained','other','out/readers/011/C/10_diagram_top.png')
root_decision(41,9,r'\deleted{e}\times','medium',True,False,'resolved','other','out/readers/011/C/10_diagram_top.png')
root_decision(42,10,r'\deleted{\unsure{H|U}}, with long lower return and rising cancellation','medium',True,False,'retained','misread symbol or index','out/readers/011/C/11_diagram_vertical.png')
root_decision(43,9,r'\deleted{H} beneath heavy \Gamma','high',True,False,'resolved','other','out/readers/011/C/10_diagram_top.png')
root_decision(44,9,r'\Gamma','high',True,False,'resolved','other','out/readers/011/C/10_diagram_top.png')
root_decision(45,11,r'\unsure{V|W}','medium',False,False,'retained','other','out/readers/011/C/12_diagram_lower_right.png')
root_decision(46,11,r'\unsure{Y|V}','medium',True,False,'retained','misread symbol or index','out/readers/011/C/12_diagram_lower_right.png','H/B V remains an explicit alternative; H comparison occurs only in the structural diagram parent.')
root_decision(47,12,'Two unequal near-parallel uprights; shorter right path begins near lower middle and diverges right before its endpoint','high',True,False,None,'drawing or diagram','out/readers/011/C/13_diagram_left_bar.png')
root_decision(48,10,'Detached dark point left of downward arrowhead',None,True,False,None,'drawing or diagram','out/readers/011/C/11_diagram_vertical.png','Unknown role, origin and hand.')
root_decision(49,10,'Detached pale point lower-right of downward arrowhead',None,True,False,None,'drawing or diagram','out/readers/011/C/11_diagram_vertical.png','Unknown role, origin and hand; B reported this additional spot.')
root_decision(50,11,'Two detached short slants: left dark and gently bent; right pale with dark lower tip',None,None,False,None,'drawing or diagram','out/readers/011/C/12_diagram_lower_right.png')
root_decision(51,9,'Retain actual local crossing paths and overwritten positions; refer to local glyph/geometry decisions',None,False,False,None,'other','out/readers/011/C/10_diagram_top.png','Coverage audit; no additional count for invisible wrappers or a repeat of local decisions.')
root_decision(52,16,'Detached compact dark shape above-left of long diagram upright','medium',True,False,None,'drawing or diagram','out/readers/011/C/13_diagram_left_bar.png','Unknown role, origin and hand.')
root_decision(53,13,'A disconnected rising endpoint at (105,154) and separate curled leftward head','medium',True,False,None,'drawing or diagram','out/readers/011/A/15_upper_drawing_junction.png')
root_decision(54,13,'Shallow detached curve as A path',None,True,False,None,'drawing or diagram','out/readers/011/A/15_upper_drawing_junction.png')
root_decision(55,13,'Small J-shaped hook as A path',None,True,False,None,'drawing or diagram','out/readers/011/A/15_upper_drawing_junction.png')
root_decision(56,14,'Heavy shaft ends at central point; its continuation below centre is thin','high',True,False,None,'drawing or diagram','out/readers/011/A/16_upper_drawing_disk.png')
root_decision(57,14,'Second lower-left rim arc',None,True,False,None,'drawing or diagram','out/readers/011/A/16_upper_drawing_disk.png')
root_decision(58,14,'Lower-right ray hook',None,True,False,None,'drawing or diagram','out/readers/011/A/16_upper_drawing_disk.png')
root_decision(59,14,'Right-inner dangling curl',None,True,False,None,'drawing or diagram','out/readers/011/A/16_upper_drawing_disk.png')
root_decision(60,14,'Short fork at shaft lower end',None,True,False,None,'drawing or diagram','out/readers/011/A/16_upper_drawing_disk.png')
root_decision(61,13,'C-reader hooked upper end of the outer right descending path',None,True,False,None,'drawing or diagram','out/readers/011/A/15_upper_drawing_junction.png')
root_decision(62,14,'One upper-left sketch with the root-selected fine paths in D53–D61',None,False,None,None,'drawing or diagram','out/readers/011/A/16_upper_drawing_disk.png')
root_decision(63,20,'C major polygon paths with root interruptions/prongs/foot projection D74–D76','high',False,True,None,'drawing or diagram','out/crops/011/root_04_bottom_polygon.png')
root_decision(64,21,'C three thick runs and companion paths with root ticks/spot D77–D79','high',False,True,None,'drawing or diagram','out/crops/011/root_05_bottom_broken_line.png')
root_decision(65,22,'C oval open at left, six crossing/sloping curves and two localized zigzag/loop groups retained',None,False,True,None,'drawing or diagram','out/crops/011/root_06_bottom_oval.png')
root_decision(66,9,'Whole diagram with local overwritten letters, qualified subscript, rules, branches and graphical marks',None,False,True,None,'drawing or diagram','out/readers/011/C/10_diagram_top.png')
root_decision(67,11,'Left arrow with doubled shaft and extended upper head stroke',None,True,False,None,'drawing or diagram','out/readers/011/C/12_diagram_lower_right.png')
root_decision(69,11,'Separate near-vertical dark continuation below bottom P, with small gap','high',True,False,None,'drawing or diagram','out/readers/011/C/12_diagram_lower_right.png','Unknown role and hand; all reader sources give only P.')
root_decision(70,12,'Small pale upright/hook immediately above left P cap; lower part meets the cap','medium',True,False,None,'drawing or diagram','out/readers/011/C/13_diagram_left_bar.png','Unknown role, hand and origin; no character supplied.')
root_decision(71,18,'Tiny detached thin curved/dashed mark with darker endpoint left of lower Hom','medium',True,True,None,'drawing or diagram','out/crops/011/root_02_lower_first.png','Unknown role, hand and origin.')
root_decision(72,19,'Compact group below P: short left dash, two joined humps, right upright','medium',True,True,None,'drawing or diagram','out/crops/011/root_03_lower_second_right.png','Unknown role, hand and surface origin; no character supplied.')
root_decision(73,19,'Dark dot and adjacent pale fragments below lower RHS Z rule','medium',True,True,None,'drawing or diagram','out/crops/011/root_03_lower_second_right.png','Unknown role, hand and surface origin; no character supplied.')
root_decision(74,20,'Two small light gaps between three upper-edge segments, plus gap at upper-left meeting','high',True,False,None,'drawing or diagram','out/crops/011/root_04_bottom_polygon.png')
root_decision(75,20,'Small endpoint prongs at upper-right polygon vertex','high',True,False,None,'drawing or diagram','out/crops/011/root_04_bottom_polygon.png')
root_decision(76,20,'Short projecting stroke at lower-left polygon foot','high',True,False,None,'drawing or diagram','out/crops/011/root_04_bottom_polygon.png')
root_decision(77,21,'Small hooked tick below left angular-sketch elbow','high',True,False,None,'drawing or diagram','out/crops/011/root_05_bottom_broken_line.png')
root_decision(78,21,'Two short projecting strokes at right angular-sketch elbow','high',True,False,None,'drawing or diagram','out/crops/011/root_05_bottom_broken_line.png')
root_decision(79,21,'Detached dark/gray mark above central gap of angular sketch','medium',True,False,None,'drawing or diagram','out/crops/011/root_05_bottom_broken_line.png','Unknown role, hand and origin.')
root_decision(80,10,'Retraced crossing/loop geometry of downward arrowhead',None,True,False,None,'drawing or diagram','out/readers/011/C/11_diagram_vertical.png')

# Glyph and cancellation state at one raised form share one physical-count key.
# The records preserve both questions while preventing a summed double count.
for a,b,key in [(15,16,'scan011-raised-left-form'),(18,19,'scan011-raised-right-form')]:
    for n in [a,b]: byid[f'011-D{n:02d}']['count_locus_key']=key
byid['011-D51']['role']='coverage audit'
byid['011-D51']['count_weight']=0
byid['011-D51']['main_counting_decision_pending']=False
for d in decisions:
    if d['crop'] and '/root_' in d['crop']:
        d['crop']=d['crop'].replace('/root_', '/')

def followup(n,**updates):
    d=byid[f'011-D{n:02d}']
    d.update(updates)
    d['root_followup_source']={'record_field':'root_messages_exact','index':0}
followup(27,final='No semicolon',confidence='high',diff_C=False,diff_H=True,
         kind='text not on the page',root_decided=True,
         crop='out/readers/011/B/02_upper_left.png',
         evidence='Root follow-up: blank endpoint space and separately placed lower expression confirmed.')
followup(68,final='Retain the already represented down-left arrow direction and head',
         confidence='high',diff_C=False,diff_H=False,kind='other',root_decided=True,
         crop='out/readers/011/C/13_diagram_left_bar.png',role='coverage audit',
         count_weight=0,main_counting_decision_pending=False,
         evidence='Root follow-up: this arrow is already represented by C; no separate change count, covered by whole diagram.')
followup(50,diff_C=True,confidence='high')
followup(9,diff_H=True,kind='omission',qualification='H already acknowledges the overwritten state. The H difference is only omission of the recovered qualified predecessor candidate e/E, whose reading remains low confidence.')
followup(14,diff_C=True,diff_H=False)
followup(62,diff_H=True,confidence='high',qualification='One sketch: root records three through-directions with six visible ends; H states five rays, plus it omits the fine paths. Local detail omissions are not separately counted against H.')
followup(66,confidence='high',qualification='One supported structural diagram difference; Y/V remains qualified and H V survives as the explicit alternative. No conclusive glyph error is asserted for that index.')
for n,level in {10:'medium',13:'high',14:'high',19:'low',20:'medium',23:'high',24:'high',25:'high',34:'high',35:'high',37:'medium',48:'medium',49:'medium',51:'high',54:'high',55:'high',57:'high',58:'high',59:'medium',60:'medium',61:'medium',65:'high',67:'high',80:'medium'}.items():
    followup(n,confidence=level)
followup(13,kind='text not on the page')
followup(15,kind='omission',diff_H=True)
followup(22,kind='misread symbol or index')
followup(23,kind='misread symbol or index')
followup(76,final='Short projecting strokes at lower-left foot and right-bottom polygon corner',
         qualification='Root follow-up groups these endpoint refinements in D76, with no additional row.')
byid['011-D76']['location']='Bottom-left polygon, lower-left foot and right-bottom corner projections'
followup(19,diff_C=False,local_diff_C=True,counted_with='011-D18',
         qualification='Cancellation-state qualification is an actual local proposal, but root directs the Boolean C count to D18 for this same raised R locus. This D19 row carries no second C count.')

QUALIFICATIONS={
 1:'Sign remains = / double-arrow qualified.',
 5:'First rounded Z/2 occurrence; primary Z retained.',
 7:'Recurring rounded Z/2 qualification carried by D05.',
 8:'Recurring rounded Z/2 qualification carried by D05.',
 9:'Overwritten e/E candidate remains open; e first.',
 10:'Visible point; hand, role and origin unassigned.',
 15:'M/U glyph remains open.',16:'Deleted/live scope at the same M/U form remains open.',
 19:'Deleted/live scope at R remains open despite resolved R glyph.',
 20:'Visible detached mark; hand and role unassigned.',
 26:'O/0 remains open.',36:'t/1 predecessor remains open.',
 37:'Detached wave and two points retain graphical qualification; hand, role and origin unassigned.',
 40:'Diagram predecessor H/R remains open.',42:'H/U remains open, H first.',
 45:'V/W remains open, V first.',46:'Y/V remains open, Y first; H V remains an alternative.',
 48:'Dark detached point; hand, role and origin unassigned.',
 49:'Pale detached point; hand, role and origin unassigned.',
 52:'Detached compact mark and pale fragment; hand, role and origin unassigned.',
 69:'Separated lower P continuation; hand and role unassigned.',
 70:'Pale upright/hook meeting P cap; hand, role and origin unassigned.',
 71:'Tiny detached trace; hand, role and origin unassigned.',
 72:'Compact trace group; hand, role and surface origin unassigned.',
 73:'Dot and pale fragments; hand, role and surface origin unassigned.',
 79:'Detached dark/gray mark; hand, role and origin unassigned.'}
for n,qualification in QUALIFICATIONS.items():
    byid[f'011-D{n:02d}']['remaining_qualification']=qualification

# The complete final-page text is read only for source-to-record attachment.
# It is neither edited nor compiled by this script.
def rootline(needle,occurrence=1):
    matches=[i+1 for i,l in enumerate(root_page_lines) if needle in l]
    return matches[occurrence-1] if len(matches)>=occurrence else None

root_region={}
if root_page_lines:
    fs=[i+1 for i,l in enumerate(root_page_lines) if l.startswith(r'\figure{')]
    diagram_start=rootline(r'\diagram{')
    lower_start=rootline(r'\begin{tikzpicture}[baseline=(hom.base)')
    lower_second=rootline(r'\operatorname{Hom}(\begin{tikzpicture}')
    root_region={
      'edge':(3,3),'upper_left':(rootline(r'\mathbb P\left('),rootline(r'P(X\times\unsure{Z|2})')-1),
      'top_product':(rootline(r'P(X\times\unsure{Z|2})'),rootline(r'P(X\times\unsure{Z|2})')),
      'top_hom':(rootline(r'\operatorname{Hom}(\underset'),rootline(r'\operatorname{Hom}(\underset')),
      'cancelled':(rootline(r'&\qquad\mathrel{/\!/}'),rootline(r'\unsure{O|0}')-1),
      'live':(rootline(r'\operatorname{Hom}(X,\underline'),rootline(r'\operatorname{Hom}(X,\underline')),
      'left_second':(rootline(r'\unsure{O|0}'),rootline(r'\unsure{O|0}')),
      'central':(rootline(r'\operatorname{Hom}(\mathscr E,\underline'),rootline(r'\operatorname{Hom}(\mathscr E,\underline')),
      'central_lower':(rootline(r'P(\operatorname{Hom}(X,Z)')-1,rootline(r'P(\operatorname{Hom}(X,Z)')),
      'upper_sketch':(fs[0],lower_start-3),'lower_first':(lower_start,lower_second-1),
      'lower_second':(lower_second,diagram_start-1),'diagram':(diagram_start,fs[-1]-1),
      'bottom_left':(rootline(r'\draw (13,425)'),rootline(r'\draw (319,271)')-1),
      'bottom_middle':(rootline(r'\draw (319,271)'),rootline(r'\draw (627,259)')-1),
      'bottom_right':(rootline(r'\draw (627,259)'),rootline('% archive sheet number: 10')-1)}
    for d,s in zip(decisions,SPECS):
        d['root_page_source']=ref(root_page_path,lines=root_region[s['region']])

# Short exact path signatures make the reader geometry alternatives concrete
# without copying every entire TikZ figure into each decision.
SIGNATURES={
 3:{'A':[(r'\mathbb P(X)',0,1)],'B':[(r'\draw[line width=.5pt]',0,3)],'C':[(r'\mathbb{P}(X)',0,1)]},
 37:{'A':[(r'\draw (0,0) -- (.45,.42)',0,2)],'B':[(r'\draw (0,4)',0,2)],'C':[(r'\draw (0,0) -- (.08,.06)',0,3)]},
 47:{'A':[(r'\draw (11,365)',0,1)],'B':[(r'\draw (18,363)',0,2)],'C':[(r'\draw (-.08,1.0)',0,2)]},
 48:{'A':[(r'\node[inner sep=0pt] at (155,246)',0,3)],'B':[(r'\fill (165,246)',0,1)],'C':[(r'\node at (.38,-.06)',0,1)]},
 49:{'B':[(r'\fill[gray] (218,266)',0,1)]},
 50:{'A':[(r'\draw (190,498)',0,3)],'B':[(r'\draw (199,500)',0,3)],'C':[(r'\& \unsure{V|W}\arrow[dr,dash',0,1)]},
 52:{'C':[(r'\node[inner sep=0] at (-1.03,.91)',0,2)]},
 53:{'A':[(r'\draw (105,154)',0,1),(r'\draw (98,157)',0,1)],'B':[(r'\draw (87,163)',0,1),(r'\draw (88,164) -- (98,158)',0,1)],'C':[(r'\draw (87,163)',0,1),(r'\draw (105,160)',0,2)]},
 54:{'A':[(r'\draw (127,139)',0,1)],'C':[(r'\draw (126,141)',0,1)]},
 55:{'A':[(r'\draw (144,90)',0,2)],'C':[(r'\draw (133,95)',0,2)]},
 56:{'A':[(r'\draw[line width=1.4pt]',0,1)],'B':[(r'\draw[line width=1.4pt]',0,1)],'C':[(r'\draw[line width=1.4pt]',0,1)]},
 57:{'A':[(r'\draw (73,355)',0,2)],'C':[(r'\draw (67,360)',0,1)]},
 58:{'A':[(r'\draw (189,385)',0,1)],'C':[(r'\draw (52,315)',0,1)]},
 59:{'A':[(r'\draw (145,317)',0,2)]},
 60:{'A':[(r'\draw (119,400)',0,1)],'C':[(r'\draw (116,388)',0,1)]},
 61:{'C':[(r'\draw (211,190)',0,1)]},
 67:{'A':[(r'\draw[line width=1.3pt] (291,446)',0,4)],'B':[(r'\draw[line width=1.5pt] (300,445)',0,3)],'C':[(r'\& \unsure{V|W}\arrow[dr,dash',0,1)]},
 68:{'A':[(r'\draw[line width=1.25pt] (161,364)',0,2)],'B':[(r'\draw[line width=1.5pt] (170,365)',0,2)],'C':[(r'\& P\times X\arrow[dl]',0,1)]}}
for n,byreader in SIGNATURES.items():
    for r,locators in byreader.items():
        chunks=[]
        for needle,offset,length in locators:
            k=find_line(r,needle)
            if k is not None:
                start=k+offset; end=start+length-1
                chunks.append(ref(tex_paths[r],lines=(start,end))|{'exact_excerpt':'\n'.join(tex[r][start-1:end])})
        byid[f'011-D{n:02d}']['reader_provenance'][r]['local_exact_tex']=chunks

ROOT_DETAIL_ANCHORS={
 37:(r'\draw (0,0) -- (.08,.06)',3),
 48:(r'\node[inner sep=0] at ([xshift=-12pt',1),49:(r'\node[inner sep=0] at ([xshift=14pt',1),
 50:(r'\draw (-42,-102)',3),52:(r'\node[inner sep=0] at (-1.03,.91)',2),
 67:(r'\draw[line width=.45pt]',4),69:(r'\node[inner sep=0] at (2,21)',4),
 70:(r'\node[inner sep=0] at (.21,.03)',3),71:(r'\node[inner sep=0] at (-.78,.12)',4),
 72:(r'\draw (-13,0)',3),73:(r'\fill (-8,0)',3),
 74:(r'\draw (13,425)',4),75:(r'\draw (215,4) -- (210,-3)',1),
 76:(r'\draw (13,425) -- (6,414)',1),77:(r'\draw (416,389)',1),
 78:(r'\draw (562,388)',1),79:(r'\node[inner sep=0] at (523,276)',3),
 80:(r'\draw ([xshift=-5pt,yshift=9pt]',3)}
for n,(needle,length) in ROOT_DETAIL_ANCHORS.items():
    k=rootline(needle)
    if k is not None:
        byid[f'011-D{n:02d}']['root_exact_tex']=ref(root_page_path,lines=(k,k+length-1))|{'exact_excerpt':'\n'.join(root_page_lines[k-1:k+length-1])}
    else:
        byid[f'011-D{n:02d}']['root_source_detail_pending']='Expected root path anchor not found; root must review source mapping.'

# Original table rows, copied only once each. Notation/retained-slip/abbreviation
# material stays in separate categories and creates no additional doubtful row.
doubt_text=(ROOT/'packets/011/C_doubts.txt').read_text()
sections={}
heading=None
for line in doubt_text.splitlines():
    if line.startswith('## '): heading=line[3:]; sections[heading]=[]
    elif heading and line.startswith('| 11 |'): sections[heading].append(line)
actual_map=[]
for i,line in enumerate(sections['Doubtful readings'],1):
    ids=[d['id'] for d in decisions if d['C_doubt_source_row']==i]
    local=[{'decision_id':x,'local_identity':byid[x]['C_doubt_sublocus'],
            'status':byid[x]['C_doubt_status'],'root_decided':byid[x]['root_decided']} for x in ids]
    statuses=[x['status'] for x in local]
    overall='retained' if 'retained' in statuses else ('resolved' if statuses and all(x=='resolved' for x in statuses) else None)
    actual_map.append({'source_row':i,'source_id':f'C011-Doubtful-readings-{i:02d}',
       'source_row_exact':line,'source':ref('packets/011/C_doubts.txt','Doubtful readings'),
       'decision_ids':ids,'local_subloci':local,'source_row_count_weight':1,
       'source_row_final_status':overall,'main_approval_pending':True,
       'status_basis':'Mechanical aggregation of root local dispositions: a row with any retained original sublocus remains retained.'})
byid['011-D06']['C_difference_basis']='The angular Z is already unmarked in C.tex, but the actual source doubtful-readings row explicitly names the right-product region. Root records its local resolution under the standing convention; original source row 3 remains retained overall.'

UNCHANGED = [
 {'id':'011-U01','location':'Central Hom, locally inspected first E and both closing curves',
  'C':r'\operatorname{Hom}(\mathscr E,\underline{\operatorname{Hom}}(X,Z))',
  'H':r'\mathrm{Hom}(\mathcal{E},\ \underline{\mathrm{Hom}}(X,Z))',
  'readers':{r:tex_ref(r,'central') for r in READERS},
  'source_rows':{'B':[report_ref('B','B011.D07c')]},
  'diff_C':False,'diff_H':False,'C_doubt_status':None,
  'note':'Contextual recurrence audited independently; no extra C source-doubt row. H editorial doubt of E is not manuscript ink.'},
 {'id':'011-U02','location':'Question mark above top relation',
  'reading':r'\overset{?}{\simeq}',
  'readers':{r:tex_ref(r,'top_product') for r in READERS},
  'diff_C':False,'diff_H':False,
  'note':'The literal question mark is the author uncertainty recorded by C_notes. No theorem or proof-check status is inferred.'},
 {'id':'011-U03','location':'Archive numeral',
  'reading':'% archive sheet number: 10','diff_C':False,'diff_H':False,
  'readers':{r:ref(tex_paths[r],lines=(find_line(r,'% archive sheet number: 10'),find_line(r,'% archive sheet number: 10'))) for r in READERS},
  'note':'Hand attribution differs across reader inventory wording and remains for root.'}
]

EXCLUSIONS=[
 {'id':'011-X01','location':'Opening cote/page markers','C':r'\cotefile{81}\scanpage{11}','H':r'\page{10}',
  'reading':r'\scanpage{11}; archive 10 in comment',
  'source_rows':{'C':[report_ref('C','ADM01')]},
  'classification':'Source convention; excluded from physical C/H collation counts',
  'authority':ref('out/briefs/brief_v09_scan011.md'),'note':'All reader page proposals remove the repeated cote marker; H page reference maps to scan minus one.'},
 {'id':'011-X02','classification':'Macro syntax and apparatus prose excluded',
  'specific_maps':[r'\mathrm{Hom} → \operatorname{Hom} for the same literal Hom token',r'\mathbb{P} → \mathbb P',r'\struck → \deleted for the same recorded cancellation',r'\note/\drawing prose → source description retained in the comparison record'],
  'note':'Literal quoted candidates, underlines, endpoint punctuation, cancellation states and described paths remain mapped to decisions; the prose is not supplied as manuscript text.'}
]

H_GROUPS=[
 {'id':'011-HG01','location':'One right-hand arrow diagram','count_decision':'011-D66','child_decisions':[f'011-D{i:02d}' for i in list(range(38,53))+[67,68,69,70,80]],
  'H_source':ref('packets/011/H.tex',lines=(23,26)),
  'H_quotes_exact':[r'$P\times X\times Y\supset H$',r'$H\to P\times X$',r'$P\times X\times Y\to P\times X$',r'$P\times X\to P$',r'$U\times_V U$',r'$V\leftarrow U$'],
  'policy':'Whole H diagram description counted once after root classification; local candidates retained without additional H omission counts.'},
 {'id':'011-HG02','location':'Adjoining three raised forms above cancelled Hom','count_decision':'011-D15','child_decisions':[f'011-D{i:02d}' for i in range(15,20)],
  'H_source':ref('packets/011/H.tex',lines=(11,12)),
  'policy':'One omitted raised group counted at D15; independently traceable glyph and state subloci are not extra H rows.'},
 {'id':'011-HG03','location':'One upper-left sketch','count_decision':'011-D62','child_decisions':[f'011-D{i:02d}' for i in range(53,62)],
  'H_source':ref('packets/011/H.tex',lines=(3,5)),
  'H_quotes_exact':['cinq traits issus de son centre, dont trois dépassent le bord','épaisse au-dessus du centre'],
  'policy':'Repeated H descriptions refer to one physical sketch; local details do not create separate H sketch counts.'},
 {'id':'011-HG04','location':'One bottom-left sketch','count_decision':'011-D63','child_decisions':['011-D74','011-D75','011-D76'],
  'H_source':ref('packets/011/H.tex',lines=(26,28)),'policy':'One physical polygon sketch; repeated notes do not duplicate it.'},
 {'id':'011-HG05','location':'One bottom-middle sketch','count_decision':'011-D64','child_decisions':['011-D77','011-D78','011-D79'],
  'H_source':ref('packets/011/H.tex',lines=(26,28)),'policy':'One physical angular sketch; A/B combined three-sketch report row maps here and to the other two objects.'},
 {'id':'011-HG06','location':'One bottom-right sketch','count_decision':'011-D65','child_decisions':[],
  'H_source':ref('packets/011/H.tex',lines=(26,28)),'policy':'One physical oval sketch.'}
]
for group in H_GROUPS:
    group['main_classification_pending']=True
    for child in group['child_decisions']:
        if child != group['count_decision']:
            byid[child]['H_count_suppressed_by_group']=group['id']

# Inventory union: each object has one canonical identity; compound original
# inventory rows can map to several explicit objects without becoming new source
# rows. Main approval and hand selection remain pending.
INV=[]
def inv(n,kind,position,objects,source_indices,decisions_=(),hand='his hand'):
    src={}
    for source,indices in source_indices.items():
        rows=witness_inventory if source=='witness_C' else reports[source]['inventory']
        path='packets/011/C_inventory.json' if source=='witness_C' else report_paths[source]
        src[source]=[ref(path,(f'/{i-1}' if source=='witness_C' else f'/inventory/{i-1}')) |
                     {'source_element':rows[i-1]['element'],'source_hand':rows[i-1]['hand'],
                      'source_transcribed':rows[i-1]['transcribed']} for i in indices]
    INV.append({'sheet_kind':'text','hand':hand,'element':f'011.I{n:02d}','kind':kind,
      'position':position,'first_words_or_objects':objects,'transcribed':None,
      'source_inventory':src,'decision_ids':[f'011-D{i:02d}' for i in decisions_],
      'main_approval_pending':True,'note':'Source transcribed=yes remains source-attributed; no final page is approved by this draft.'})

inv(1,'display','upper edge','= / double-arrow candidate',{'witness_C':[1],'A':[1],'B':[1],'C':[1]},[1])
inv(2,'display','upper left','double-stem P(X)',{'witness_C':[2],'A':[2],'B':[2],'C':[2]},[2])
inv(3,'drawing','upper-left X','four terminal strokes, upper-left detached',{'B':[3]},[3])
inv(4,'display','upper centre to right','P(X times Z), question over relation, Hom',{'witness_C':[3],'A':[3],'B':[4],'C':[3]},[4,5,6,11])
inv(5,'deletion','under top Hom Z','looped predecessor',{'witness_C':[4],'A':[4],'B':[5],'C':[4]},[9])
inv(6,'drawing','below top overwritten factor','detached point',{'C':[5]},[10],'undetermined hand')
inv(7,'deletion','upper right crossed line','Hom(X), explicit crossing paths',{'witness_C':[5],'A':[5],'B':[6],'C':[6]},[12,13,14])
inv(8,'deletion','raised left above crossed Hom','M/U with state qualification proposed',{'witness_C':[6],'A':[6],'B':[7],'C':[7]},[15,16])
inv(9,'deletion','raised middle above crossed Hom','H/X source candidates',{'witness_C':[6],'A':[7],'B':[8],'C':[8]},[17])
inv(10,'deletion','raised right above crossed Hom','R/P source candidates; state qualification proposed',{'witness_C':[6],'A':[8],'B':[9],'C':[9]},[18,19])
inv(11,'drawing','above cancelled initial H','detached small mark',{'A':[34],'C':[10]},[20],'undetermined hand')
inv(12,'display','left of crossed Hom','paired oblique strokes',{'witness_C':[7],'A':[9],'B':[10]},[25])
inv(13,'display','below cancelled Hom','Hom(X, underlined Hom(E,Z), one closure',{'witness_C':[7],'A':[10],'B':[11],'C':[11]},[21,22,23,24])
inv(14,'display','left second line','O/0 subset doubled P(X)',{'witness_C':[8],'A':[11],'B':[12],'C':[12]},[26,27])
inv(15,'display','central line','Hom(E, underlined Hom(X,Z))',{'witness_C':[10],'A':[12],'B':[14],'C':[14]},[7])
inv(16,'display','between central lines','paired oblique strokes',{'witness_C':[11],'A':[13],'B':[15],'C':[15]},[28])
inv(17,'display','below centre','P(Hom(X,Z), one closure',{'witness_C':[11],'A':[14],'B':[15],'C':[15]},[8,29,30,31])
inv(18,'drawing','upper-left sketch','long shaft, disk and central point, crossing rays, loops, arrow',{'witness_C':[9],'A':[15],'B':[13],'C':[13]},[62])
inv(19,'drawing','upper sketch junction','small junction head, bowed dash, inner J-shaped return',{'A':[16]},[53,54,55])
inv(20,'drawing','upper disk and lower shaft','rim return, curled ray end, narrow right loop, lower branch',{'A':[17]},[56,57,58,59,60,61])
inv(21,'display','first lower inclusion','underlined Hom(X,Y) subset P(X times Y)',{'witness_C':[12],'A':[18],'B':[16],'C':[16]},[32,33])
inv(22,'text','under first lower Hom','single underline',{'A':[19]},[])
inv(23,'display','second lower inclusion','Hom(Z times X,Y) subset P(Z times X times Y)',{'witness_C':[13],'A':[20],'B':[17],'C':[17]},[34,35])
inv(24,'deletion','under lower first Z','t/1 predecessor',{'witness_C':[14],'A':[21],'B':[18],'C':[18]},[36])
inv(25,'drawing','above lower first Z','detached bent/wavy trace and points',{'A':[35],'B':[19],'C':[19]},[37],'undetermined hand')
inv(26,'diagram','right middle to foot','products, overwritten letters, arrows, lower objects and branches',{'witness_C':[15],'A':[22],'B':[20],'C':[20]},[66])
inv(27,'deletion','above diagram X','cancelled H',{'witness_C':[16],'A':[23],'B':[21],'C':[21]},[38])
inv(28,'drawing','below raised diagram H','short arch',{'A':[24],'B':[22],'C':[22]},[39])
inv(29,'deletion','under diagram first P','H/R predecessor',{'witness_C':[17],'A':[25],'B':[23],'C':[23]},[40])
inv(30,'deletion','under diagram first multiplication sign','e predecessor',{'witness_C':[17],'A':[26],'B':[24],'C':[24]},[41])
inv(31,'deletion','left of vertical diagram arrow','H/U crossed character',{'witness_C':[18],'A':[27],'B':[25],'C':[25]},[42])
inv(32,'deletion','under diagram rightmost object','H beneath heavy Gamma',{'witness_C':[19],'A':[28],'B':[26],'C':[27]},[43,44])
inv(33,'drawing','left of diagram down-arrow head','detached dark spot',{'A':[36],'B':[27],'C':[26]},[48],'undetermined hand')
inv(34,'drawing','below-right of diagram down-arrow head','detached pale spot',{'B':[27]},[49],'undetermined hand')
inv(35,'drawing','left of lower-left diagram P','two unequal upright rules',{'A':[29],'B':[28],'C':[28]},[47])
inv(36,'drawing','below lower V and U','short unheaded descending branches',{'A':[30],'B':[29]},[50])
inv(37,'drawing','above-left of long diagram upright','detached dot and faint neighboring trace candidate',{'C':[33]},[52],'undetermined hand')
inv(38,'drawing','bottom left','polygon, repeated sides, long loop, diagonals and arrow',{'witness_C':[20],'A':[31],'B':[30],'C':[29]},[63])
inv(39,'drawing','bottom middle','thick open broken line and thin companion paths',{'witness_C':[21],'A':[32],'B':[31],'C':[30]},[64])
inv(40,'drawing','bottom right','oval, six curves and short localized zigzags',{'witness_C':[21],'A':[33],'B':[32],'C':[31]},[65])
inv(41,'text','bottom-left margin','archive numeral 10, comment only',{'A':[37],'B':[33],'C':[32]},[],'undetermined hand')
inv(42,'drawing','below bottom diagram P','detached near-vertical lower continuation',{},[69],'undetermined hand')
inv(43,'drawing','above left diagram P cap','small pale upright/hook meeting cap',{},[70],'undetermined hand')
inv(44,'drawing','left of first lower Hom','tiny detached curved/dashed trace',{},[71],'undetermined hand')
inv(45,'drawing','beneath second lower right-member P','short dash, joined humps and short upright',{},[72],'undetermined hand')
inv(46,'drawing','beneath second lower right-member Z','dark point and pale fragments',{},[73],'undetermined hand')
inv(47,'drawing','upper slanted polygon boundary','three ink segments, two inner gaps and upper-left meeting gap',{},[74])
inv(48,'drawing','upper-right polygon vertex','small endpoint prongs',{},[75])
inv(49,'drawing','lower-left polygon foot and right-bottom corner','short projecting endpoint strokes',{},[76])
inv(50,'drawing','below broken-line left elbow','small hooked tick',{},[77])
inv(51,'drawing','broken-line right elbow','two short projecting strokes',{},[78])
inv(52,'drawing','above broken-line central gap','small detached dark/gray mark',{},[79],'undetermined hand')
inv(53,'drawing','downward diagram arrowhead','retraced crossing/loop geometry',{},[80])
for item in INV:
    if not item['source_inventory']:
        ds=[byid[d] for d in item['decision_ids']]
        item['root_source']=[d['root_decision_source'] for d in ds]
        item['note']='Root-only addition from written adjudication log; no independent reader source inventory row. Final page approval pending.'
    item['root_page_sources']=[byid[d].get('root_exact_tex',byid[d].get('root_page_source')) for d in item['decision_ids']]
    if item['element']=='011.I22':
        item['root_page_sources']=[ref(root_page_path,lines=root_region['lower_first'])]
    if item['element']=='011.I41':
        k=rootline('% archive sheet number: 10')
        item['root_page_sources']=[ref(root_page_path,lines=(k,k))]
    item['transcribed']='yes' if item['root_page_sources'] and all(item['root_page_sources']) else None
    item['transcribed_basis']='Material attached to the proposed root page source; main approval remains pending.'

# Source-row mapping with original IDs, without copying long evidence/crop arrays.
row_coverage={r:[] for r in READERS}
for r in READERS:
    for rid,(index,row) in source_rows[r].items():
        targets=[d['id'] for d,s in zip(decisions,SPECS) if rid in s['rows'][r]]
        targets += [u['id'] for u in UNCHANGED if any(x.get('row_id')==rid for x in u.get('source_rows',{}).get(r,[]))]
        targets += [x['id'] for x in EXCLUSIONS if any(t.get('row_id')==rid for t in x.get('source_rows',{}).get(r,[]))]
        row_coverage[r].append({'source':report_ref(r,rid),'decision_or_audit_ids':targets,
          'reported_diff_C':row['diff_C'],'reported_diff_H':row['diff_H'],
          'reported_C_doubt_status':row.get('C_doubt_status'),'reported_kind':row['kind'],
          'mapped':bool(targets)})

doubt_targets={
 'A':[[1],[5,7,8],[9],[11],[26],[36],[40],[42],[46],[45],[15],[16],[19],[20],[37],[48]],
 'B':[[1],[5,7,8],[9],[21],[26],[36],[40],[41],[42],[46],[45],[15,16],[18,19],[37]],
 'C':[[1],[5,7,8],[9],[15],[17],[26],[36],[40],[42],[46],[45],[10],[20],[37],[48],[52]]}
doubt_coverage={}
for r in READERS:
    doubt_coverage[r]=[]
    for i,x in enumerate(reports[r]['doubts']):
        targets=doubt_targets[r][i] if i<len(doubt_targets[r]) else []
        doubt_coverage[r].append({'source':ref(report_paths[r],f'/doubts/{i}'),
          'location_exact':x['location'],'reading_exact':x['reading'],
          'alternatives_exact':x.get('alternatives',[]),'decision_ids':[f'011-D{n:02d}' for n in targets],
          'mapped':bool(targets)})

inventory_coverage={}
for r in ['witness_C',*READERS]:
    rows=witness_inventory if r=='witness_C' else reports[r]['inventory']
    inventory_coverage[r]=[]
    for x in rows:
        targets=[it['element'] for it in INV if any(s['source_element']==x['element'] for s in it['source_inventory'].get(r,[]))]
        inventory_coverage[r].append({'source_element':x['element'],'merged_elements':targets,'mapped':bool(targets)})

all_paths=['packets/011/C.tex','packets/011/H.tex','packets/011/C_doubts.txt','packets/011/C_notes.txt','packets/011/C_inventory.json','packets/011/metadata.json',root_log_path,root_events_path,root_page_path,'out/checks/scan011_witness_crosswalk.md','out/briefs/brief_v09_scan011.md']+list(report_paths.values())+list(tex_paths.values())+list(audit_paths.values())
fingerprints={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in all_paths if (ROOT/p).exists()}
seen_C=set(); seen_H=set()
for d in decisions:
    key=d['count_locus_key']
    d['counted_diff_C']=bool(d['diff_C'] and key not in seen_C)
    if d['diff_C']: seen_C.add(key)
    hkey=d['H_count_group'] or key
    d['counted_diff_H']=bool(d['diff_H'] and hkey not in seen_H and not d.get('H_count_suppressed_by_group'))
    if d['counted_diff_H']: seen_H.add(hkey)
    if d['diff_C'] and not d['counted_diff_C']:
        d['count_note']='Local change retained in this subdecision; the same physical count key is counted once in its earlier linked subdecision.'
pending=[]
for d in decisions:
    missing=[k for k in ['final','confidence','kind','diff_C','diff_H'] if d[k] is None]
    if not d['root_decided']: missing.insert(0,'root visual decision')
    if d['main_counting_decision_pending']: missing.append('root counting decision')
    d['pending_fields']=missing
    if missing: pending.append({'decision_id':d['id'],'pending_fields':missing})

record={
 'scan':11,'folder':metadata['folder'],'their_page':metadata['their_page'],'hua_has':metadata['hua_has'],
 'filename':'J81-02_81_scan011.tex','brief_version':'v09','main_adjudicated':False,'main_approved_utc':None,
 'draft_status':'Mechanical draft only. Root-supplied decisions are attributed; all remaining reading, confidence, H-category and counting choices are flagged.',
 'decisions':decisions,
 'doubts':[{'decision_id':d['id'],'location':d['location'],'final':d['final'],'confidence':d['confidence'],
            'source_C_row':d['C_doubt_source_row'],'root_decided':d['root_decided'],
            'source_doubt_refs':[x['source'] for rr in doubt_coverage.values() for x in rr if d['id'] in x['decision_ids']],
            'remaining_qualification':d['remaining_qualification'],
            'count_locus_key':d['count_locus_key'],
            'root_page_source':d.get('root_exact_tex',d.get('root_page_source')),
            'status':'root retains qualification; exact final-page source reference below'}
           for d in decisions if d.get('remaining_qualification')],
 'inventory':INV,
 'notes':'Handwritten P/Hom formulas, an upper-left sketch, a right-hand diagram and three bottom sketches. The literal question mark over the first relation is recorded. Two single terminal closures are preserved in all proposed readings. Root alone determines final readings and review status.',
 'abbreviations':[{'form':'Hom','possible_expansion':'homomorphismes','source':ref('packets/011/C_doubts.txt','Abbreviations'),'expanded_in_transcription':False}],
 'check_events':root_events,
 'reader_check_events':{r:reports[r]['check_events'] for r in READERS},
 'check_events_source':ref(root_events_path),
 'check_events_note':'The two existing root event objects are copied verbatim. This assembler performed no mathematical check and generated no event.',
 'workflow_note':'Source-text assembly only. No image or crop was opened by the assembler; no OCR, external research, mathematical check, compiler, delegation, approved-record write or nextpage preparation occurred.',
 'source_reports':{r:ref(report_paths[r]) for r in READERS},
 'source_readings':{r:ref(tex_paths[r]) for r in READERS},
 'source_audits':{r:ref(audit_paths[r]) for r in READERS},
 'source_fingerprints':fingerprints,
 'reader_completion':{r:{k:reports[r].get(k) for k in ['start_utc','end_utc','full_image_viewed','halves_viewed','complete_visual_read']} for r in READERS},
 'root_adjudication_log':root_log_path,
 'root_page_source':root_page_path,
 'root_messages_exact':[ROOT_FOLLOWUP_EXACT],
 'root_final_count_instruction':'Root directs Boolean counting, because build_records.py ignores weights/count keys: D18 counts the raised R glyph/state change once; D19 diff_C=false with local change and cross-reference preserved. D15 glyph is unchanged (diff_C=false), D16 state change has diff_C=true. Keep 80 decision rows.',
 'actual_C_doubt_map':actual_map,
 'C_doubt_source_classification':{
   'actual_doubtful_readings_source_rows':15,
   'source_rows_by_section':{k:len(v) for k,v in sections.items()},
   'source_sections_exact':{k:v for k,v in sections.items() if k!='Doubtful readings'},
   'row3_scope':'Four separated top/middle local regions; the two middle recurrences use the first qualification. A/B give two explicit report rows plus recurrence audits; C gives four local rows. Source-row count remains one.',
   'row7_scope':'Outer live Hom and first inner E are the two doubtful subloci. Central E is an independently inspected context recurrence in U01, not a new source doubt.',
   'retained_slips_mapping':{'middle P(Hom(X,Z)':'011-D31','upper-right Hom(X,Hom(E,Z)':'011-D24'}},
 'H_collation_groups':H_GROUPS,
 'source_row_coverage':row_coverage,'source_doubt_coverage':doubt_coverage,'inventory_coverage':inventory_coverage,
 'unchanged_audit':UNCHANGED,'excluded_source_conventions':EXCLUSIONS,
 'counting_policy':'Preserve 15 C doubtful-readings source identities once each. Local glyph/state and geometry proposals remain explicit. Repeated H descriptions map to one physical sketch each; all right-diagram local candidates map to one structural H locus. Source report flags are retained without mechanically adding their totals. Final C/H counts, confidence totals and source-row resolution summaries require root approval.',
 'counts':{'decision_candidates':len(decisions),'actual_C_doubt_source_rows':15,
   'actual_C_doubt_local_subloci':sum(len(x['local_subloci']) for x in actual_map),
   'source_difference_rows':{r:len(reports[r]['differences']) for r in READERS},
   'source_doubt_rows':{r:len(reports[r]['doubts']) for r in READERS},
   'source_inventory_rows':{r:len(reports[r]['inventory']) for r in READERS},
   'witness_C_inventory_rows':len(witness_inventory),'inventory_union_candidates':len(INV),
   'C_difference_loci':None,'H_difference_loci':None,'actual_C_doubts_retained':None,
   'actual_C_doubts_resolved':None,'remaining_doubt_or_graphic_uncertainty_loci':None,
   'provisional_unique_C_difference_loci':sum(d['counted_diff_C'] for d in decisions),
   'provisional_unique_H_difference_loci':sum(d['counted_diff_H'] for d in decisions),
   'root_disposed_C_source_rows_retained':sum(x['source_row_final_status']=='retained' for x in actual_map),
   'root_disposed_C_source_rows_resolved':sum(x['source_row_final_status']=='resolved' for x in actual_map),
   'remaining_qualified_local_records':sum(bool(d.get('remaining_qualification')) for d in decisions),
   'remaining_qualified_unique_count_keys':len({d['count_locus_key'] for d in decisions if d.get('remaining_qualification')}),
   'check_events':len(root_events)},
 'assembly_timestamp_utc':datetime.now(timezone.utc).isoformat(),
 'assembly_revision':'Root-supplied readings and confidence entered; compact mechanical mapping with final counting/approval pending.',
 'approval_followups':pending,
 'coverage_status':{'unmapped_report_rows':[{ 'reader':r,**x} for r,rows in row_coverage.items() for x in rows if not x['mapped']],
   'unmapped_reader_doubts':[{'reader':r,**x} for r,rows in doubt_coverage.items() for x in rows if not x['mapped']],
   'unmapped_inventory_rows':[{'source':r,**x} for r,rows in inventory_coverage.items() for x in rows if not x['mapped']],
   'reader_finalization_pending':[r for r in READERS if not reports[r].get('end_utc')],
   'root_page_path_details_pending':[d['id'] for d in decisions if d.get('root_source_detail_pending')],
   'inventory_page_attachments_pending':[x['element'] for x in INV if x['transcribed'] is None],
   'method':'Mechanical source mapping; no visual or mathematical validation by assembler.'}
}
(OUT/'scan011_record_draft.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')

def mdtext(v):
    return str(v).replace('|',r'\|').replace('\n',' ')
lines=['# Scan011 — mechanical draft mapping','',
 'Main adjudication remains **false**. The assembler has read text sources only. Root decisions, confidence, H classifications and approval remain with root. This mapping preserves exact reader report readings and compact source references in the JSON draft.','',
 '## Source status','',
 '| Source | Difference rows | Doubt entries | Inventory rows | Final timestamp |',
 '|---|---:|---:|---:|---|']
for r in READERS:
    lines.append(f"| {r} | {len(reports[r]['differences'])} | {len(reports[r]['doubts'])} | {len(reports[r]['inventory'])} | {reports[r].get('end_utc') or 'PENDING'} |")
lines+=['','## Fifteen original C doubt rows','',
 '| Source row | Exact source row | Local decisions | Root local status |',
 '|---:|---|---|---|']
for x in actual_map:
    statuses='; '.join(f"{p['decision_id']} {p['status'] or 'PENDING'}" for p in x['local_subloci'])
    lines.append(f"| {x['source_row']} | {mdtext(x['source_row_exact'])} | {', '.join(x['decision_ids'])} | {statuses} |")
lines+=['','Seven notation rows, two retained-slip rows, and one abbreviation row remain separate source categories. The source-row count is 15 regardless of the number of local decisions.','',
 '## Local reading and source-row map','',
 '| Decision | Location | A report rows | B report rows | C-reader report rows | Root final / pending |',
 '|---|---|---|---|---|---|']
for d,s in zip(decisions,SPECS):
    ids=['; '.join(s['rows'][r]) or 'TeX / audit' for r in READERS]
    outcome=mdtext(d['final']) if d['root_decided'] else '**PENDING**'
    if d['root_decided'] and d['pending_fields']: outcome+='; pending '+', '.join(d['pending_fields'])
    lines.append(f"| {d['id']} | {mdtext(d['location'])} | {ids[0]} | {ids[1]} | {ids[2]} | {outcome} |")
lines+=['','## H physical grouping','',
 '| Group | Physical object | Count-bearing decision | Local decisions |',
 '|---|---|---|---|']
for g in H_GROUPS:
    lines.append(f"| {g['id']} | {g['location']} | {g['count_decision'] or 'PENDING: select one raised-group row'} | {', '.join(g['child_decisions'])} |")
lines+=['','All H note/drawing prose remains apparatus. Quoted manuscript candidates remain in the JSON with the source locations. Macro conversion alone creates no row. Local H flags from reports are source-attributed; they are not summed.','',
 '## Inventory union','',
 '| Union item | Kind | Physical object | Source inventory identities | Decision links |',
 '|---|---|---|---|---|']
for x in INV:
    src='; '.join(k+': '+', '.join(z['source_element'] for z in vv) for k,vv in x['source_inventory'].items())
    lines.append(f"| {x['element']} | {x['kind']} | {mdtext(x['position']+' — '+x['first_words_or_objects'])} | {src} | {', '.join(x['decision_ids'])} |")
lines+=['','## Still-qualified reader loci','',
 '| Reader | Source doubt entry | Exact reading | Exact alternatives | Decision links |',
 '|---|---|---|---|---|']
for r,rows in doubt_coverage.items():
    for i,x in enumerate(rows,1):
        lines.append(f"| {r} | {i}: {mdtext(x['location_exact'])} | {mdtext(x['reading_exact'])} | {mdtext('; '.join(x['alternatives_exact']))} | {', '.join(x['decision_ids'])} |")
lines+=['','## Mechanical coverage and pending work','',
 f"- Report rows lacking a map: {len(record['coverage_status']['unmapped_report_rows'])}.",
 f"- Reader doubt entries lacking a map: {len(record['coverage_status']['unmapped_reader_doubts'])}.",
 f"- Source inventory rows lacking a map: {len(record['coverage_status']['unmapped_inventory_rows'])}.",
 '- Exact A/B/C local report readings and TeX source regions are stored per decision in `scan011_record_draft.json`.',
 '- The two existing root check-event objects are copied verbatim; reader check-event lists remain empty.',
 '- All final counting decisions remain pending. H local omissions are grouped without erasing their source flags.',
 '- Root will implement the right diagram with tikz-cd and explicit geometry. A/B TikZ proposals and C tikz-cd proposal remain source references; this assembler selects no diagram implementation.',
 '- No approved record, page, cumulative file, or nextpage material has been written.','']
(OUT/'scan011_mapping.md').write_text('\n'.join(lines))
print(json.dumps({'draft':'out/checks/scan011_record_draft.json','mapping':'out/checks/scan011_mapping.md',
                  'decision_candidates':len(decisions),'root_readings_entered':sum(d['root_decided'] for d in decisions),
                  'coverage_status':record['coverage_status']},ensure_ascii=False,indent=2))
