"""Independent blind reading of scan032; no first reading or comparison used.

Only source inputs: the copied scan.jpg and boxes.tsv named below.  The
prescribed rectangles were cropped once by blind_io.py crop 32; all later
inspection used those saved crops, including magnified/rotated whole-crop
displays.  This script writes the reading and then its examination journal.
It intentionally performs no OCR, source discovery, comparison, or TeX run.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import io
import json
import os
import tempfile

ROOT = Path('/workspace/scratch/8132fe1cca43')
PACKET = ROOT / 'work/blind_inputs/148_scan032'
OUT = ROOT / 'work/SP82_C13_148/second'
EVIDENCE = ROOT / 'work/SP82_C13_148/crops/second/148_scan032'
DISPLAY = ROOT / 'work/blind_display/148_scan032'

READINGS = {
    'B032-01': r'''\figure{\begin{tikzpicture}[x=0.02cm,y=-0.02cm,line cap=round,line join=round]
\path[use as bounding box] (0,0) rectangle (416,371);
\clip (0,0) rectangle (416,371);
% Outer curve: the lower and right ends remain open.
\draw[line width=.28pt] (27,346) .. controls (9,322) and (8,275) .. (12,243)
 .. controls (17,213) and (45,183) .. (75,155)
 .. controls (112,122) and (154,94) .. (199,77)
 .. controls (241,61) and (289,44) .. (325,46)
 .. controls (349,46) and (371,66) .. (381,91);
\draw[line width=.22pt] (384,103) .. controls (393,126) and (394,151) .. (390,174);
% Inner curve and its lighter near-parallel return.
\draw[line width=.36pt] (235,-2) .. controls (219,24) and (195,61) .. (169,88)
 .. controls (143,116) and (112,144) .. (83,174)
 .. controls (54,204) and (39,240) .. (41,274)
 .. controls (39,303) and (53,324) .. (82,336)
 .. controls (106,346) and (139,350) .. (163,346);
\draw[line width=.18pt] (217,62) .. controls (176,82) and (130,120) .. (98,152)
 .. controls (68,183) and (48,216) .. (43,248);
\draw[line width=.18pt] (45,205) .. controls (66,176) and (99,146) .. (128,125);
\draw[line width=.19pt] (90,339) .. controls (121,350) and (148,353) .. (177,345);
% Small loop/retrace on the descending upper stroke.
\draw[line width=.25pt] (210,39) .. controls (204,39) and (208,33) .. (213,34);
% Small dark angular mark, preserved as strokes rather than normalized.
\draw[line width=.7pt] (149,111) -- (156,116) -- (157,107);
\draw[line width=.35pt] (156,114) -- (159,119);
\node[inner sep=0,font=\scriptsize] at (56,296) {$\unsure{\sqrt{1}|\pi}$};
% The right-hand marker is visibly open underneath.
\draw[line width=.62pt] (376,199) .. controls (378,190) and (384,189) .. (387,197);
\fill (378,185) circle (.65);
\end{tikzpicture}}''',
    'B032-02': r'''\figure{\begin{tikzpicture}[x=.012cm,y=-.012cm,line cap=round,line join=round]
\path[use as bounding box] (0,0) rectangle (678,844);
\clip (0,0) rectangle (678,844);
% Face-side machine printing, inverted relative to the manuscript drawing.
% The first O and final character are clipped by the rectangle; do not expand.
\node[rotate=180,anchor=west,inner sep=0,font=\ttfamily\fontsize{11}{11}\selectfont] at (686,754) {OR PREDONT DELIVER AT 0000 - PREDO\illegible{1}};
\node[rotate=180,anchor=west,inner sep=0,font=\ttfamily\fontsize{11}{11}\selectfont] at (686,789) {OR PREDONT DELIVER AT 0000 - PREDO\illegible{1}};
\node[rotate=180,anchor=west,inner sep=0,font=\ttfamily\fontsize{11}{11}\selectfont] at (686,823) {OR PREDONT DELIVER AT 0000 - PREDO\illegible{1}};
% Only isolated letter-edge fragments of a further printed row enter at y=844.
\foreach \x in {5,26,47,68,88,108,128,169,188,208,229,250,271,291,312,333,354,375,397,418,438,459,480,501,522,543,563,584,605,626,647,668}
  {\draw[line width=.55pt] (\x,844) -- (\x+2,842.9);}
% Upward curved tail from the high ring, with its free hooked end.
\draw[line width=.44pt] (257,279) .. controls (265,233) and (283,174) .. (304,155)
 .. controls (313,149) and (322,153) .. (327,158);
% Long faint open strokes entering from the upper-right crop boundary.
\draw[line width=.22pt] (669,-3) .. controls (629,67) and (580,144) .. (541,201)
 .. controls (483,281) and (423,338) .. (361,390);
\draw[line width=.32pt] (663,-2) .. controls (642,57) and (596,145) .. (562,218)
 .. controls (528,272) and (468,337) .. (407,394) -- (362,390);
\draw[line width=.2pt] (645,54) .. controls (606,122) and (569,187) .. (543,225);
\draw[line width=.18pt] (503,227) .. controls (520,224) and (541,232) .. (559,226);
% Main visible connections.
\draw[line width=.34pt] (257,283) .. controls (196,377) and (91,510) .. (29,597);
\draw[line width=.3pt] (28,597) .. controls (84,560) and (148,525) .. (200,490);
\draw[line width=.38pt] (9,613) .. controls (89,582) and (188,584) .. (281,581);
\draw[line width=.3pt] (283,578) .. controls (338,559) and (398,533) .. (444,504);
\draw[line width=.28pt] (211,490) .. controls (294,493) and (371,500) .. (440,503);
\draw[line width=.55pt] (258,285) .. controls (301,330) and (350,374) .. (384,417)
 .. controls (407,450) and (425,481) .. (445,500);
\draw[line width=.2pt] (263,291) .. controls (319,344) and (363,390) .. (392,430)
 .. controls (414,459) and (430,486) .. (446,501);
% Separate central descents, including a free lower end and retracing.
\draw[line width=.39pt] (255,286) .. controls (246,345) and (223,414) .. (211,466);
\draw[line width=.42pt] (256,287) .. controls (247,353) and (254,408) .. (265,455)
 .. controls (271,492) and (278,543) .. (282,575);
\draw[line width=.23pt] (263,291) .. controls (263,356) and (264,405) .. (270,449)
 .. controls (274,486) and (277,532) .. (281,568);
% The left vertical starts below the open ring, leaving the visible gap.
\draw[line width=.4pt] (191,508) .. controls (193,578) and (196,669) .. (199,746)
 .. controls (200,760) and (200,775) .. (202,781);
\draw[line width=.23pt] (192,532) .. controls (188,608) and (189,690) .. (181,751)
 .. controls (177,775) and (170,794) .. (162,804);
\draw[line width=.2pt] (194,589) .. controls (197,664) and (198,723) .. (203,774);
% Descending left fan: gaps near its top and distinct multiple strokes.
\draw[line width=.6pt] (29,615) .. controls (72,664) and (121,713) .. (169,751)
 .. controls (181,761) and (192,772) .. (201,780);
\draw[line width=.65pt] (43,619) .. controls (91,678) and (144,731) .. (190,766)
 .. controls (198,772) and (202,776) .. (206,781);
\draw[line width=.43pt] (19,621) .. controls (33,660) and (58,707) .. (83,747)
 .. controls (104,780) and (120,816) .. (130,844);
\draw[line width=.33pt] (16,624) .. controls (19,670) and (40,722) .. (64,759)
 .. controls (88,797) and (103,826) .. (111,844);
\draw[line width=.29pt] (20,621) .. controls (9,616) and (10,638) .. (16,651);
% Right fan, including both heavy near-parallel strokes and lighter diagonals.
\draw[line width=.62pt] (282,581) .. controls (264,648) and (236,719) .. (203,779);
\draw[line width=.7pt] (290,576) .. controls (277,637) and (248,710) .. (208,782);
\draw[line width=.26pt] (279,589) .. controls (257,666) and (234,727) .. (202,784)
 .. controls (193,807) and (183,830) .. (176,844);
\draw[line width=.37pt] (437,513) .. controls (365,589) and (280,688) .. (206,780);
\draw[line width=.2pt] (419,527) .. controls (357,601) and (277,699) .. (210,785);
\draw[line width=.28pt] (374,544) .. controls (338,587) and (288,658) .. (235,723)
 .. controls (221,744) and (207,765) .. (197,777);
% Point rings, kept irregular and retraced rather than converted to solid nodes.
\draw[line width=.82pt] (261,278) .. controls (259,269) and (250,273) .. (250,282)
 .. controls (252,289) and (261,291) .. (262,280) -- (259,276);
\draw[line width=.42pt] (256,275) ellipse (3.5 and 5.2);
\fill (256,281) circle (1.3);
\draw[line width=.75pt] (21,599) .. controls (22,591) and (31,588) .. (35,594)
 .. controls (36,600) and (24,605) .. (21,601);
\draw[line width=.33pt] (25,602) -- (32,592);
\draw[line width=.68pt] (199,489) .. controls (198,484) and (207,480) .. (211,485)
 .. controls (216,491) and (203,495) .. (200,490);
\draw[line width=.4pt] (206,484) -- (204,491);
\draw[line width=.78pt] (439,502) .. controls (440,495) and (451,494) .. (454,500)
 .. controls (455,507) and (443,515) .. (440,508) -- (447,500);
\draw[line width=.36pt] (439,505) .. controls (448,508) and (456,500) .. (448,495);
\draw[line width=.72pt] (280,575) .. controls (286,570) and (289,574) .. (286,582)
 .. controls (282,590) and (278,588) .. (280,575);
\draw[line width=.3pt] (275,586) -- (289,572);
\draw[line width=.49pt] (198,776) .. controls (205,771) and (208,779) .. (203,786)
 .. controls (200,790) and (195,783) .. (198,776);
\draw[line width=.6pt] (160,799) .. controls (166,796) and (169,806) .. (163,811)
 .. controls (158,813) and (157,803) .. (160,799);
\draw[line width=.4pt] (160,800) -- (160,794);
% Small isolated manuscript marks.
\draw[line width=.55pt] (129,663) -- (137,662) -- (140,664);
\draw[line width=.45pt] (313,427) .. controls (317,421) and (320,425) .. (315,429);
\fill (503,480) circle (1.25);
\fill (521,480) circle (.8);
\fill (526,478) circle (.6);
\fill (319,709) circle (.65);
\fill (357,688) circle (.55);
% Partial neighboring curvilinear drawing, crossing the right crop edge.
\draw[line width=.25pt] (678,408) .. controls (625,439) and (589,482) .. (577,524)
 .. controls (568,565) and (572,600) .. (590,626);
\draw[line width=.32pt] (678,430) .. controls (636,465) and (611,505) .. (606,543)
 .. controls (602,577) and (608,601) .. (629,615)
 .. controls (645,626) and (660,628) .. (678,628);
\draw[line width=.19pt] (678,419) .. controls (638,451) and (609,493) .. (600,535);
\node[inner sep=0,font=\scriptsize] at (618,577) {$\unsure{\sqrt{1}|\pi}$};
\end{tikzpicture}}''',
    'B032-03': r'''\margin{31}''',
}

JOURNAL = {
    'reader': 'blind_d',
    'page': '148_scan032',
    'source_inputs': [str(PACKET / 'scan.jpg'), str(PACKET / 'boxes.tsv')],
    'helper_read': str(ROOT / 'work/SP82_C13_148/scripts/blind_io.py'),
    'crop_command': 'python /workspace/scratch/8132fe1cca43/work/SP82_C13_148/scripts/blind_io.py crop 32',
    'crop_rule': 'One fixed crop per listed rectangle; subsequent displays magnify or rotate the same entire saved crop only.',
    'successfully_viewed_boxes': ['B032-01', 'B032-02', 'B032-03'],
    'successful_views': {
        'B032-01': [str(DISPLAY / 'B032-01.jpg'), str(EVIDENCE / 'B032-01.jxl'), str(DISPLAY / 'B032-01_magnified.png'), str(DISPLAY / 'B032-01_rotated.png')],
        'B032-02': [str(DISPLAY / 'B032-02.jpg'), str(EVIDENCE / 'B032-02.jxl'), str(DISPLAY / 'B032-02_rotated.png')],
        'B032-03': [str(DISPLAY / 'B032-03.jpg')],
    },
    'blindness': 'Reading committed without opening any witness, first transcription, review, comparison, notes, another page, or another reader output. No OCR, external research, or TeX compilation.',
    'print_decision': 'The inverted machine text in B032-02 is not laterally reversed when the same crop is rotated 180 degrees. It is face-side text and is retained. Incidental printed ruling/hatching is not transcribed as words.',
    'residual_uncertainties': [
        {'box': 'B032-01', 'item': 'Lower-left small label', 'reading': r'\unsure{\sqrt{1}|\pi}', 'reason': 'The short heavy top stroke, lower left hook and right downstroke resemble a radical with numeral 1, but pi remains plausible.'},
        {'box': 'B032-01', 'item': 'Small angular mark near upper crossing', 'reading': 'Preserved as separate angular strokes in TikZ.', 'reason': 'May be an arrowhead or a small v-like letter. Direction and text identity are not secure.'},
        {'box': 'B032-01', 'item': 'Right-hand cap-shaped mark', 'reading': 'Preserved as a downward-open curved mark.', 'reason': 'May be an incomplete point ring or a small letter; no closure is invented.'},
        {'box': 'B032-02', 'item': 'Faint retraced connections', 'reading': 'Separate paths preserve visible geometry, gaps and open ends.', 'reason': 'Exact continuity beneath the printed hatching is sometimes uncertain; no mathematical completion is imposed.'},
        {'box': 'B032-02', 'item': 'Small loop near (162,805)', 'reading': 'Loop plus short upright stroke retained geometrically.', 'reason': 'Could be a ring along a descending line or a b-like label; printed characters partly surround it.'},
        {'box': 'B032-02', 'item': 'Printed line boundaries', 'reading': r'OR PREDONT DELIVER AT 0000 - PREDO\illegible{1}', 'reason': 'Three repeated rows are legible in the rotated crop. The first O is partially clipped, and only a piece of the next character after PREDO remains; the unreadable clipped character is not expanded from the repetition.'},
        {'box': 'B032-02', 'item': 'Fourth machine-printed row at bottom boundary', 'reading': 'Only tiny clipped glyph-edge strokes are represented.', 'reason': 'The fragments are insufficient for an independent letter reading and are not expanded into a repeated sentence.'},
        {'box': 'B032-02', 'item': 'Overlapping label', 'reading': r'\unsure{\sqrt{1}|\pi}', 'reason': 'Same handwritten label as the left edge of B032-01; preserved again because both fixed boxes contain it.'},
    ],
    'confident_readings': [{'box': 'B032-03', 'reading': r'\margin{31}'}],
}


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=path.name + '.', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='') as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def main():
    with (PACKET / 'boxes.tsv').open(encoding='utf-8', newline='') as handle:
        box_ids = [row['box'] for row in csv.DictReader(handle, delimiter='\t')]
    assert box_ids == list(READINGS), 'Must include precisely all listed boxes in order.'
    text = io.StringIO(newline='')
    writer = csv.writer(text, delimiter='\t', lineterminator='\n')
    writer.writerow(['box', 'reading'])
    for box in box_ids:
        writer.writerow([box, READINGS[box]])
    target = OUT / '148_scan032_second.tsv'
    atomic_write(target, text.getvalue())
    JOURNAL['reading_written_utc'] = datetime.now(timezone.utc).isoformat()
    JOURNAL['reading_path'] = str(target)
    atomic_write(OUT / '148_scan032_blind_journal.json', json.dumps(JOURNAL, ensure_ascii=False, indent=2) + '\n')
    print(f'Wrote {target}; {len(box_ids)} independently read boxes; journal saved.')


if __name__ == '__main__':
    main()
