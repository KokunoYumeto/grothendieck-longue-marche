#!/usr/bin/env python3
"""Record the root's actual full-page image inspections for checkpoint 07."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / 'notes/pdf_qa'
SHA = 'ddc2b4623e3565442139392d1154ac179c5e080cac683701db14fbc125c893f2'
assert hashlib.sha256((ROOT / 'GT_TOWER_CHECK_paper.pdf').read_bytes()).hexdigest() == SHA
observations = {
    1: 'Title, complete abstract, attribution and first contents entries fit cleanly; all mathematical accents are legible.',
    9: 'Dense induction proof and displays A.T7--A.T9 have clear tags, margins and line spacing.',
    15: 'Signed matrices, frame displays A.L5--A.L6 and surrounding proof remain legible without collisions.',
    16: 'Completion comparison display, consecutive section headings and A.6.1 statement are clear and within the page.',
    30: 'Conjugation table, two-by-two matrices and displays A.C8--A.C11 fit with separated equation tags.',
    31: 'Displays A.C12--A.C17 and the final pentagon equation fit without clipping or tag overlap.',
    32: 'Boxed main character conclusion, its proof and the finite-check status paragraph are fully visible.',
    34: 'Harmonic subgroup formulas, boxed primitive equation and all tags A.J1--A.J8 are legible.',
    35: 'Harmonic comparison proof and formulas A.J9--A.J13, including the bottom display, fit cleanly.',
    36: 'Parity statement and affine-ring calculations A.J14--A.J20 have clean glyphs and separated tags.',
    42: 'Twelve-row obstruction table, filenames and new braid-word statement fit without clipping.',
    43: 'Peripheral braid identities and the stack comparison formulas are clear and within both margins.',
    44: 'Homology marking matrix, long transport heading and MC.1--MC.2 display fit cleanly.',
    45: 'Core-intersection and automorphism formulas MC.3--MC.7 retain clear tags and line breaks.',
    46: 'Transport equations and finite centralizer matrices FCM.1--FCM.3 fit without collisions.',
    47: 'Graph-cycle proof and FCM.4--FCM.8 are legible; the displaced FCM.7 tag has clear spacing.',
    48: 'Exclusion functional and six-row matrix/word table are fully visible and readable.',
    63: 'Characteristic quotient formulas DR.8--DR.12 and their proof have clear margins and tags.',
    94: 'Form comparison and characteristic input formulas TF.10--TF.13 fit; exponents and subscripts are legible.',
    105: 'Mixed-target proof ending and new binary quotient theorem fit with clear heading and formulas.',
    106: 'Binary source relations, quotient and two-line cocycle formula BFU.7 remain within the page.',
    107: 'Binary action and Coxeter cocycle system, labelled permutations and section equations are legible.',
    108: 'Explicit fusion correction and long centralizer sequence BFU.14 fit with no tag collision.',
    109: 'Class-three theorem heading, long braid formula SP3.4 and Hall-coordinate proof fit cleanly.',
    110: 'Cubic-kernel argument and long commutator expansion SP3.9 have no clipping or tag overlap.',
    111: 'Executed-certificate paragraph, exact nonfactorization proof and quaternary theorem are fully visible.',
}
assignments = json.loads((DIRECTORY / 'checkpoint07_assignments.json').read_text())
assert set(observations) == set(assignments['assignments']['root'])
pages = []
for page, observation in observations.items():
    png = DIRECTORY / f'page_{page:03d}.png'
    pages.append({'page': page, 'visually_inspected': True,
                  'observations': observation,
                  'png_sha256': hashlib.sha256(png.read_bytes()).hexdigest()})
result = {'pdf_sha256': SHA, 'inspector': 'root', 'pages': pages}
(DIRECTORY / 'checkpoint07_root.json').write_text(json.dumps(result, indent=2) + '\n')
print(f'Recorded {len(pages)} actual full-page visual inspections by root.')
