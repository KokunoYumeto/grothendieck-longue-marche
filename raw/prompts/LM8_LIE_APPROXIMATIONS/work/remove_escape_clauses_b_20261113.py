"""LM8 line 89: 'prove the strongest case within reach ... smallest undecided instance. Carry each part to where it
stops.' is a way to finish early (AGENTS.md, prompts rule of 12 Nov 2026). usage: python -I -B remove_escape_clauses_b_20261113.py"""
from pathlib import Path

UP = Path(r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\LM8_LIE_APPROXIMATIONS\PROMPT.md")
t = UP.read_text(encoding="utf-8")
old = ("Where a statement resists, prove the strongest case within reach (the types `(0,3)`, `(0,4)`, `(1,1)`; low weight; "
       "one prime), compute, and state the obstruction as an exact statement with its smallest undecided instance. "
       "Carry each part to where it stops.")
new = ("Where a statement resists, the cases within reach (the types `(0,3)`, `(0,4)`, `(1,1)`; low weight; one prime) and "
       "the computations are steps: record them, state the obstruction exactly, and attack it from the smallest undecided "
       "instance. Carry each part through to a proof or a refutation.")
assert t.count(old) == 1, t.count(old)
UP.write_text(t.replace(old, new), encoding="utf-8")
print("replaced")
