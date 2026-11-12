#!/usr/bin/env bash
set -euo pipefail
CYCLOTOMIC_BUNDLE_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd -- "$CYCLOTOMIC_BUNDLE_DIR"
lualatex -interaction=nonstopmode -halt-on-error -file-line-error CYCLOTOMIC_KERNEL_paper.tex > build_lualatex_1.log 2>&1
bibtex CYCLOTOMIC_KERNEL_paper > build_bibtex.log 2>&1
lualatex -interaction=nonstopmode -halt-on-error -file-line-error CYCLOTOMIC_KERNEL_paper.tex > build_lualatex_2.log 2>&1
lualatex -interaction=nonstopmode -halt-on-error -file-line-error CYCLOTOMIC_KERNEL_paper.tex > build_lualatex_3.log 2>&1
pdfinfo CYCLOTOMIC_KERNEL_paper.pdf
