#!/usr/bin/env python3
"""Create an external XeLaTeX validation wrapper using page filenames only.

This script never reads page contents and never modifies page sources. Run the
generated wrapper with support/run_xelatex.py only when compilation is wanted.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PAGE_NAME = re.compile(r'_(\d+)_scan(\d+)\.tex$')

PREAMBLE = r'''% External compilation wrapper; not part of the diplomatic transcription.
% Editorial states are color-coded for validation, including whole blocks.
\documentclass[11pt,a4paper]{article}
\usepackage[margin=18mm]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb,mathrsfs,bm,array,longtable,mathtools}
\usepackage{tikz-cd}
\usepackage[normalem]{ulem}
\usetikzlibrary{arrows.meta,patterns,calc,decorations.markings,
  decorations.pathreplacing,decorations.pathmorphing,shapes.geometric,
  positioning,intersections,bending,fit,matrix}
\definecolor{ValidationDoubt}{RGB}{155,84,0}
\definecolor{ValidationDeletion}{RGB}{160,25,45}
\definecolor{ValidationInsertion}{RGB}{0,85,150}
\definecolor{ValidationMargin}{RGB}{105,45,135}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.45em}
\setlength{\emergencystretch}{3em}
\newcommand{\ValidationCote}{?}
\NewDocumentCommand{\cotefile}{m}{\gdef\ValidationCote{#1}}
\NewDocumentCommand{\scanpage}{m}{%
  \clearpage
  \typeout{VALIDATION COTE \ValidationCote\space SCAN #1 PDFPAGE \thepage}%
  {\large\bfseries Cote \ValidationCote, scan #1\par}%
  {\scriptsize Compilation validation.\quad
   {\color{ValidationDoubt}Doubt}\quad
   {\color{ValidationDeletion}Deletion}\quad
   {\color{ValidationInsertion}Insertion}\quad
   {\color{ValidationMargin}Margin note}\par}\medskip}
\NewDocumentCommand{\mspage}{m}{%
  \ifmmode\text{[MS page #1]}\else
  \par{\footnotesize\itshape MS page #1\par}\fi}
% Unboxed, long groups allow paragraphs, displays, and drawings to pass through.
\NewDocumentCommand{\unsure}{+m}{\begingroup\color{ValidationDoubt}#1\endgroup}
\NewDocumentCommand{\deleted}{+m}{\begingroup\color{ValidationDeletion}#1\endgroup}
\NewDocumentCommand{\inserted}{+m}{\begingroup\color{ValidationInsertion}#1\endgroup}
\NewDocumentCommand{\margin}{+m}{\begingroup\color{ValidationMargin}#1\endgroup}
\NewDocumentCommand{\illegible}{m}{%
  \ifmmode\text{\color{ValidationDoubt}[illegible: #1]}\else
  {\color{ValidationDoubt}\textit{[illegible: #1]}}\fi}
% Ulem handles text; native math underlining preserves the surrounding math style.
\let\ValidationTextUline\uline
\let\ValidationTextUuline\uuline
\RenewDocumentCommand{\uline}{+m}{%
  \ifmmode\underline{#1}\else\ValidationTextUline{#1}\fi}
\RenewDocumentCommand{\uuline}{+m}{%
  \ifmmode\underline{\underline{#1}}\else\ValidationTextUuline{#1}\fi}
% Retokenization lets a tikzcd body use ordinary & even inside a macro argument.
% It also accommodates TikZ matrices and nested figures without rewriting pages.
\NewDocumentCommand{\ValidationRescan}{+m}{%
  \begingroup\endlinechar=-1\relax\scantokens{#1\empty}\endgroup}
\NewDocumentCommand{\diagram}{+m}{\ValidationRescan{#1}}
\RenewDocumentCommand{\figure}{+m}{\ValidationRescan{#1}}
\errorcontextlines=100
\begin{document}
'''


def discover_pages(pages_dir: Path) -> list[tuple[int, int, Path]]:
    """Read filenames/stat metadata only; page bytes are never opened."""
    pages = []
    for path in pages_dir.glob('*.tex'):
        if not path.is_file():
            continue
        match = PAGE_NAME.search(path.name)
        if match is None:
            raise ValueError(f'Page filename lacks cote/scan suffix: {path.name}')
        resolved = path.resolve()
        if any(char in str(resolved) for char in '{}\r\n'):
            raise ValueError(f'Unsupported brace or newline in page path: {path.name}')
        pages.append((int(match[1]), int(match[2]), resolved))
    if not pages:
        raise ValueError(f'No .tex page files found in {pages_dir}')
    return sorted(pages)


def build_wrapper(pages_dir: Path, output: Path, *, landscape: bool = False) -> dict:
    pages = discover_pages(pages_dir)
    output = output.resolve()
    if output.is_relative_to(pages_dir.resolve()) or output in [page for _, _, page in pages]:
        raise ValueError('The validation wrapper must be outside the source pages directory.')
    preamble = PREAMBLE.replace(r'\usepackage[margin=18mm]{geometry}',
                               r'\usepackage[landscape,margin=14mm]{geometry}') if landscape else PREAMBLE
    body = [preamble]
    for cote, scan, path in pages:
        body.append(f'\n% Source filename only: {path.name}\n')
        body.append(f'\\cotefile{{{cote}}}\n')
        body.append('\\input{\\detokenize{' + str(path) + '}}\n')
    body.append('\n\\end{document}\n')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(''.join(body), encoding='utf-8')
    return {'wrapper': str(output), 'page_count': len(pages),
            'sources': [{'cote': cote, 'scan': scan, 'filename': path.name}
                        for cote, scan, path in pages],
            'landscape': landscape,
            'page_contents_read': False,
            'page_sources_modified': False}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pages_dir', type=Path)
    parser.add_argument('--output', required=True, type=Path,
                        help='External validation wrapper path, outside the pages directory.')
    parser.add_argument('--landscape', action='store_true',
                        help='Use A4 landscape with 14 mm margins for wide figures.')
    args = parser.parse_args()
    try:
        report = build_wrapper(args.pages_dir, args.output, landscape=args.landscape)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
