"""Apply the scan-checked outcomes of the 33 open fixes to second_pass/PKG_checked_fixed.tex. Each edit is an exact
string that must occur once; a dated copy of every file is kept in this folder before it is changed.
usage: python -I apply_merge.py [--go]"""
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).resolve().parent
SP = W.parent
GO = "--go" in sys.argv

EDITS = {
    "LM_P011": [("LM_FIX_01-013",
                 "\\[\nI=S_0(\\overline K)\\subset S(\\overline K)\n\\qquad[\\text{vide \\unsure{si|ssi} }S=\\varnothing]\n"
                 "\\]\n\\diagram{[Sous \\(S(\\overline K)\\), le signe \\(\\simeq\\) écrit verticalement (un trait ondulé "
                 "à côté d'un trait droit), puis\n\\(S_0(\\overline K)\\wedge_\\Sigma\\Gamma\\) : on lit \\(S(\\overline K)"
                 "\\simeq S_0(\\overline K)\\wedge_\\Sigma\\Gamma\\).]}",
                 "\\diagram{\\begin{tikzcd}[ampersand replacement=\\&,row sep=0.15em,column sep=0.4em]\n"
                 "I=S_0(\\overline K)\\subset \\& S(\\overline K) \\& \\qquad[\\text{vide \\unsure{si|ssi} }S=\\varnothing] \\\\\n"
                 "\\& \\rotatebox{90}{$\\simeq$} \\& \\\\\n"
                 "\\& S_0(\\overline K)\\wedge_\\Sigma\\Gamma \\&\n"
                 "\\end{tikzcd}}")],
    "LM_P013": [("LM_FIX_09-009", "$F\\deleted{\\illegible{1}}=(F_U,F_D,\\varphi)$",
                 "$F\\deleted{_{\\unsure{U}},\\unsure{E|e}_{\\unsure{i}}}=(F_U,F_D,\\varphi)$")],
    "LM_P017": [("LM_FIX_01-030 (Pi_1 struck)", "\\& B_{\\unsure{\\Pi_1}X} \\&\n\\arrow[from=pr,to=pl",
                 "\\& B_{\\deleted{\\unsure{\\Pi_1}}X} \\&\n\\arrow[from=pr,to=pl")],
    "LM_P019": [("LM_FIX_09-013", "\\(\\deleted{\\illegible{1}}2-2g\\,(=\\mathrm{EP})",
                 "\\(\\deleted{\\unsure{\\geq}2}2-2g\\,(=\\mathrm{EP})")],
    "LM_P022": [("LM_FIX_09-021", "\\unsure{de} $U_{g,\\nu}\\simeq\\illegible{1}$",
                 "\\unsure{de} $U_{0,1}\\simeq\\mathbb C$"),
                ("LM_FIX_09-022", "G\\times\\deleted{\\illegible{1}}\\unsure{A_{g,\\nu+k}^{\\circ}}$",
                 "G\\times A_{g,\\deleted{\\illegible{1}}\\unsure{\\nu+}k}^{\\circ}$")],
    "LM_P024": [("LM_FIX_02-010 (doubled display (65) removed)",
                 "\\[\n(65)\\qquad\n\\Pi_2(A_0^\\circ)\\xleftarrow{\\sim}\\Pi_2(\\mathrm{GP}(1,\\mathbb C))\n"
                 "\\xleftarrow{\\sim}\\Pi_2(\\deleted{\\unsure{\\mathrm{Sl}(2,\\mathbb C)}}\\inserted{S^3}/\\pm1)\n\\]\n"
                 "\\diagram{",
                 "\\diagram{"),
                ("LM_FIX_02-010 (Sl as read by the second pass)",
                 "\\Pi_2\\bigl(\\deleted{\\unsure{\\mathrm{SL}(2,\\mathbb C)}}\\inserted{S^3}/\\pm1\\bigr)",
                 "\\Pi_2\\bigl(\\deleted{\\unsure{\\mathrm{Sl}(2,\\mathbb C)}}\\inserted{S^3}/\\pm1\\bigr)")],
    "LM_P025": [("LM_FIX_02-012",
                 "\\diagram{[À gauche : $f_T,g_T:T\\longrightarrow T'$, deux flèches parallèles\ndirigées vers $T'$, "
                 "marquées chacune d'un $\\simeq$, traits plusieurs fois repassés.\nÀ droite : $f_{\\mathcal G},"
                 "g_{\\mathcal G}:\\mathcal G\\longrightarrow\\mathcal G'$,\ndeux flèches parallèles dirigées vers "
                 "$\\mathcal G'$, marquées chacune d'un $\\simeq$.]}",
                 "\\diagram{\\begin{tikzcd}[ampersand replacement=\\&,column sep=3.4em]\n"
                 "f_T,g_T:\\ T\n"
                 " \\arrow[r,shift left=2.6ex,line width=0.7pt,\"\\unsure{\\simeq}\"]\n"
                 " \\arrow[r,phantom,\"\\unsure{\\deleted{\\xrightarrow{\\sim}}}\" description]\n"
                 " \\arrow[r,shift right=2.6ex,\"\\sim\"]\n"
                 "\\& T'\n"
                 "\\& f_{\\mathcal G},g_{\\mathcal G}:\\mathcal G\n"
                 " \\arrow[r,shift left=1.6ex,\"\\unsure{\\simeq}\"]\n"
                 " \\arrow[r,shift right=1.6ex,\"\\unsure{\\simeq}\"]\n"
                 "\\& \\mathcal G'\n"
                 "\\end{tikzcd}}")],
    "LM_P026": [("LM_FIX_09-025", "(1,v)=\\deleted{\\illegible{1}}(v,v)(v^{-1},1)",
                 "(1,v)=\\deleted{(\\unsure{v^{-1}},1)}(v,v)(v^{-1},1)"),
                ("LM_FIX_09-026", "\\rho\\deleted{\\illegible{1}}(1,v)=\\rho(v,v)",
                 "\\rho\\deleted{_{\\unsure{\\widetilde A}_{g,\\nu}}}(1,v)=\\rho(v,v)")],
    "LM_P032": [("LM_FIX_10-011", "\\deleted{\\unsure{\\prod_i}\\,\\unsure{[x_i,y_i]}\\,\\illegible{2}}",
                 "\\deleted{\\unsure{\\prod_i}\\,\\unsure{[x_i,y_i]}\\,\\unsure{\\cdots[x_g,y_g]\\ell_1}}")],
    "LM_P033": [("LM_FIX_10-015", "\\unsure{\\widehat{\\mathcal{T}}_{g,\\nu}}\\longrightarrow \\illegible{1}\\)}",
                 "\\unsure{\\widehat{\\mathcal{T}}_{g,\\nu}}\\longrightarrow \\unsure{\\Gamma}\\)}")],
    "LM_P034": [("LM_FIX_10-017", "\\overset{\\deleted{\\illegible{1}}}{\\mathcal T_{g,\\nu}}",
                 "\\overset{\\deleted{\\unsure{\\widehat{\\wedge}}}}{\\mathcal T_{g,\\nu}}")],
    "LM_P035": [("LM_FIX_10-024", "\\Gamma_\\Sigma=\\deleted{\\illegible{1}}\\mathcal N_\\Sigma^{!}/\\Sigma^{!}",
                 "\\Gamma_\\Sigma=\\deleted{\\widehat{\\widehat{\\mathcal T}}}\\mathcal N_\\Sigma^{!}/\\Sigma^{!}")],
}

ok = True
for pkg, edits in EDITS.items():
    p = SP / f"{pkg}_checked_fixed.tex"
    t = p.read_text(encoding="utf-8")
    for iid, old, new in edits:
        n = t.count(old)
        print(f"{pkg} {iid}: found {n}")
        if n != 1:
            ok = False
            continue
        t = t.replace(old, new, 1)
    if GO and ok:
        bak = W / f"{pkg}_checked_fixed_before_20261112.tex"
        if not bak.exists():
            shutil.copy2(p, bak)
        p.write_text(t, encoding="utf-8")
print("all found once" if ok else "SOME EDITS NOT FOUND ONCE", "| written" if GO and ok else "| dry run")
