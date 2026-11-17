"""Initialize the work register. This is not a mathematical computation."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
items = ([f"A{i}" for i in range(1, 15)]
         + [f"B{i}" for i in range(1, 10)]
         + [f"C{i}" for i in range(1, 7)]
         + [f"K{i}" for i in range(1, 7)])
report = ["INCOMPLETE", "", "| Item | Statements | Outcome and current state |",
          "|---|---|---|"]
for item in items:
    report.append(f"| {item} | Pending | Open: under active investigation. |")
report += ["", "# Work record", "",
           "AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claimed.",
           "", "The main theorem is the first priority. See the research log and",
           "independent audit notes for the evolving checks. No unchecked claim",
           "of the earlier return is treated as an established result.", ""]
(root / "ANABELIAN_A1_report.md").write_text("\n".join(report))
fields = ["id", "statement", "status", "where_proved", "depends_on",
          "answers (item or check item)", "manuscript_passages (cote; scan)",
          "depends_on_doubtful_reading (scan, alternatives)", "notes"]
with (root / "ANABELIAN_A1_results.csv").open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerow(["A.1", "Universal prime-to-p point-section injectivity "
                     "for proper genus >=2 curves over finite fields",
                     "Open", "sections/A_main.tex", "AG.40--AG.42, under audit",
                     "A1; K6", "149; 35--36", "", "Working audit target"])
print(f"Initialized {len(items)} item rows and one working statement.")
