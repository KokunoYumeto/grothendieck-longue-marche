#!/usr/bin/env bash
set -eu
TASK_ROOT=$(cd "$(dirname "$0")/.." && pwd)
TASK_QA=/workspace/scratch/60a038f0158e/qa
cd "$TASK_ROOT"
TEXINPUTS=.:/usr/share/texlive/texmf-dist/tex//:/usr/share/texmf/tex//: \
TEXFORMATS="$TASK_QA//:" \
TFMFONTS=/usr/share/texlive/texmf-dist/fonts/tfm//:/usr/share/texmf/fonts/tfm//: \
ENCFONTS=/usr/share/texlive/texmf-dist/fonts/enc//:/usr/share/texmf/fonts/enc//: \
T1FONTS=/usr/share/texlive/texmf-dist/fonts/type1//:/usr/share/texmf/fonts/type1//: \
VFFONTS=/usr/share/texlive/texmf-dist/fonts/vf//:/usr/share/texmf/fonts/vf//: \
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$TASK_QA" records/validation_wrapper.tex > "$TASK_QA/compile_console.txt" 2>&1
