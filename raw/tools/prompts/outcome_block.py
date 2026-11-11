# outcome_block.py -- work file (Claude, Fable 5.2; 11 Nov 2026). The section "What the outcome must be"
# (rule 0 of PUSH_STANDARD_AND_AUDIT_20261111.md; user, 11 Nov 2026, P3193), shared by LM1, LM2, LM4-LM8.
# Imported by push_rewrite_20261111.py and lm12_push_20261111.py.
import re
def outcome(prefix, n_items, extra=""):
    return ("## What the outcome must be\n\n"
"**1. The deliverables.** One ZIP with: `{p}_paper.tex` and its PDF; `{p}_results.csv`; `{p}_readings.csv`; `{p}_references.bib`; `{p}_report.md`; `code/` with every program and its output "
"(their form is fixed under WHAT TO DELIVER below). `{p}_results.csv` has one row for every numbered statement of the paper, with its status, and the paper has at least one numbered statement for "
"each of the {n} items of \"What is to be settled\", for each lead, and for each lettered task (a), (b), … and each numbered follow-up task of every part. `{p}_report.md` opens with a table: "
"one line per item, per lead and per lettered task, giving the statement numbers that answer it and one of the three outcomes below.{x}\n\n"
"**2. What counts as done, for each item, lead and task.** Exactly one of:\n"
"- (a) **proved**: in his form, or in its strongest correct form, with a complete proof;\n"
"- (b) **refuted**: by a complete counterexample, checked by a program when it is finite, together with the strongest true statement in its place, proved;\n"
"- (c) **partly settled**: the cases you proved, the computations you ran (code and output attached), and the obstruction as an exact statement with the smallest undecided instance.\n\n"
"A statement labelled Known counts only together with the derivation of his statement from the cited theorem, in the form he gives it, with the proof of the reduction. "
"A statement labelled Open counts only as outcome (c), with all three of its components on the page.\n\n"
"**3. What is not acceptable.** A survey or a status report; \"open, see [reference]\"; a plan, a sample or an outline; a summary of what would be done; a computation described and not run; "
"an item, a lead or a lettered task without a row.\n\n"
"**4. When the work is finished.** Only when every item, every lead and every lettered task has reached (a), (b) or (c). If you stop before that, the table of `{p}_report.md` says so line by line: "
"each line that has not reached the bar is marked \"unfinished\", with what is missing. Do not present the work as complete while one such line remains.\n\n"
"**5. If the execution environment disconnects.** Wait for it and retry for at least 10 minutes. If it does not come back, the work must still reach us, so write it out in this chat as text: every file in full, each in its own code block headed by its file name. That means the paper's LaTeX as far as it is written, the results and readings CSV, the references, the report, and every program you ran with its output (the code you ran to save each file contains its text: take it from there). Then continue the remaining parts directly in the chat, in the same form, as far as you can. Say at the start which files were lost and which parts are not yet written. An answer that only reports the disconnection, describes what was saved or asks for the files again, without writing out the work, is not acceptable.\n").format(p=prefix, n=n_items, x=(" " + extra if extra else ""))
def words(s): return len(re.findall(r"\S+", s))
