"""Fill the verdict column of pilot/pilot_new_findings.tsv for the new findings looked at on crops (pilot/crops/m_*.png)."""
import csv, pathlib
BASE = pathlib.Path(__file__).resolve().parent.parent
V = {1: "doubt mark justified: the typed letter looks like c (m_ps1)", 2: "doubt mark justified: e for c (m_ps1)",
     12: "confirmed: the page has only '25.' and no title (m_ps3)", 22: "confirmed: typed 'he' (m_ps1)",
     23: "confirmed: 'this' struck by hand (m_ps1)", 33: "confirmed: the s of 'intervals' is overtyped with x (m_kint)",
     38: "confirmed: 'just' struck by hand (m_ps2)", 39: "confirmed: handwritten X in the margin (m_ps1)",
     40: "confirmed: 'thise' with the e x-ed out (m_ps2)", 55: "confirmed: typed 'ih' (m_ps2)",
     58: "plausible: handwritten ending over the typed one (m_ps2)", 60: "plausible: no comma after the insertion on the page (m_ps2)",
     63: "confirmed: typed do'nt (m_ps3)", 70: "confirmed: a handwritten mark after 'microseminar' (m_ps2)",
     72: "confirmed: 'Notes.' (m_esq2)", 74: "confirmed: 'convenanble' (m_esq2)", 76: "confirmed: 'est connu' (esq019_connu)",
     80: "confirmed: 'correspondants' (esq019_corresp)", 81: "confirmed: comma after '2-cartographique' (m_esq1)",
     82: "confirmed: comma after 'présent' (m_esq1)", 83: "confirmed: 'res-treint' (m_esq2)",
     84: "confirmed: 'les caractéristique 2 et 5' (m_esq2)", 87: "confirmed: no comma after 'Très vite' (m_esq1)",
     89: "confirmed: 'd'une notion de' (m_esq1)", 90: "confirmed: 's'est agit' (m_esq1)", 92: "confirmed: 'van Kampen' (m_esq2)",
     93: "confirmed: 'chapître' (m_esq1)", 94: "confirmed: 'terre / à terre' without hyphens (m_esq2)",
     98: "confirmed: quotes around 'l'Esquisse Thématique' (m_esq2)"}
rows = list(csv.DictReader(open(BASE / "pilot" / "pilot_new_findings.tsv", encoding="utf-8"), delimiter="\t"))
for i, r in enumerate(rows):
    r["verdict_on_crop"] = V.get(i, "not looked at individually")
w = csv.DictWriter(open(BASE / "pilot" / "pilot_new_findings.tsv", "w", encoding="utf-8", newline=""), fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(rows)
print(sum(1 for r in rows if r["verdict_on_crop"] != "not looked at individually"), "of", len(rows), "looked at")
