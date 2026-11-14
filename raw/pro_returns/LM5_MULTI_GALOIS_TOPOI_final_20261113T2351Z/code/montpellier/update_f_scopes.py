"""Update F.44/F.45 after the proved arithmetic extension and source recovery."""
from pathlib import Path
base = Path(__file__).resolve().parents[1]
text = (base / "F.tex").read_text()
start44 = text.index(r"\paragraph{F.44 ")
start45 = text.index(r"\paragraph{F.45 ")
audit = (base / "F44_centralizer_audit.tex").read_text()
# The radical/height proof is already in the main F.44 scope discussion.
audit = audit[:audit.index("For orientation on the positive arguments")] + \
        audit[audit.index("The finite certificate is"):]
text = text[:start44] + (base / "F44_replacement.tex").read_text() + "\n\n" + audit + "\n\n" \
       + (base.parent / "root" / "F45_replacement.tex").read_text()
(base / "F.tex").write_text(text)
print("F.44 updated: cyclotomic test proved; Q^solv residual test precise.")
print("F.44 centralizer audit included; repeated radical/height proof omitted.")
print("F.45 updated: CYCLOTOMIC and section53 recovered; FLAGGED149 audit remains.")
