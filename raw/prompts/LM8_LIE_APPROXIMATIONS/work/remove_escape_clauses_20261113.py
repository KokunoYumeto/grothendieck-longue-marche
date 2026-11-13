"""LM8: the rules of proof and the deliverables still held clauses that let an item end without a proof or a refutation
(the same ones the ANABELIAN_149 writer removed from LM6 on 13 Nov 2026: M-18, M-19a, M-19b, M-21, M-22), plus rule 8's
"carry it to where it stops" and rule 1's "keep ... as open". Each old text must occur exactly once.
usage: python -I -B remove_escape_clauses_20261113.py"""
import shutil
from pathlib import Path

UP = Path(r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\LM8_LIE_APPROXIMATIONS\PROMPT.md")
WK = Path(__file__).resolve().parent
B = WK / "PROMPT_before_escape_clauses_20261113.md"
assert not B.exists()
shutil.copy2(UP, B)
R = [
    ("name it as one and keep the general statement on your list as open.",
     "name it as one and keep attacking the general statement."),
    ("and to carry it to where it stops; it is not a survey.",
     "and to carry it through to proofs and refutations; it is not a survey."),
    ("What you cannot settle stays on the page as an exact statement, with what you tried, the step that fails and the "
     "smallest undecided instance. Never write it up as proved, and never drop it.",
     "What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and "
     "you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it."),
    ("An Open statement records your own attack:",
     "A statement may be labelled Open only in a return marked INCOMPLETE (point 4 of \"What the outcome must be\"); it "
     "then records your own attack:"),
    (" without your own attempt is unfinished.", " is not acceptable."),
    ("corrections to the leads and to the notes, what remains open)",
     "corrections to the leads and to the notes, and, only in a return marked INCOMPLETE, the state of every undecided line)"),
    ("Write the files from the start and extend them as you go.",
     "Write the files from the start and extend them as you go, so that an interruption loses little."),
]
t = UP.read_text(encoding="utf-8")
for old, new in R:
    n = t.count(old)
    print(n, "x", old[:60])
    if n == 1:
        t = t.replace(old, new)
UP.write_text(t, encoding="utf-8")
