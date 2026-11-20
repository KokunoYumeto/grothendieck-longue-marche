"""Apply the accepted scan182 audit clarification to one evidence field only."""

from copy import deepcopy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "records/scan182/decision.json"
PLACE = "horizontal rule followed directly by De ces cogitations"
OLD = (
    "The top half shows the separate continuous rule and the new indented "
    "paragraph, with no star or section heading. No crop was needed. "
    "Main inspected crops/scan182/main/03_separator.jpg."
)
NEW = (
    "The top half shows the separate continuous rule and the new indented "
    "paragraph, with no star or section heading. Reader C settled this in "
    "the top-half view without a crop. Main subsequently inspected "
    "crops/scan182/main/03_separator.jpg."
)


def main():
    raw = TARGET.read_text()
    data = json.loads(raw)
    row = data["doubt_review"][9]
    if row["place"] != PLACE:
        raise RuntimeError("Unexpected doubt_review[9] locus; no file changed.")
    if row["evidence"] == NEW:
        print("scan182 audit clarification already applied; no file changed.")
        return
    if row["evidence"] != OLD:
        raise RuntimeError("Unexpected evidence wording; no file changed.")

    old_token = json.dumps(OLD, ensure_ascii=False)
    new_token = json.dumps(NEW, ensure_ascii=False)
    if raw.count(old_token) != 1:
        raise RuntimeError("Expected one exact evidence token; no file changed.")
    updated = raw.replace(old_token, new_token, 1)
    expected = deepcopy(data)
    expected["doubt_review"][9]["evidence"] = NEW
    if json.loads(updated) != expected:
        raise RuntimeError("Change exceeds the authorized evidence field.")

    TARGET.write_text(updated)
    print("Changed only decision.json doubt_review[9].evidence.")
    print(NEW)


if __name__ == "__main__":
    main()
