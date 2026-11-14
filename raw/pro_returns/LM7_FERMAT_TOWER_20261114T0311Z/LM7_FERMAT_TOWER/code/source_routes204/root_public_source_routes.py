"""Read exact public bibliographic endpoints; record failures without bypasses."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
DEST = ROOT / "source_route_raw"
DEST.mkdir(exist_ok=True)
routes = [
    ("gdz_bloch_mets", "https://gdz.sub.uni-goettingen.de/mets/PPN243919689_0350.mets.xml"),
    ("ihara_openalex", "https://api.openalex.org/works/https://doi.org/10.2307/1971352"),
    ("coleman_openalex", "https://api.openalex.org/works/https://doi.org/10.2969/aspm/01710055"),
    ("ihara_crossref", "https://api.crossref.org/works/10.2307/1971352"),
    ("coleman_crossref", "https://api.crossref.org/works/10.2969/aspm/01710055"),
]

def fetch(item):
    name, url = item
    record = {"name": name, "url": url}
    try:
        with urlopen(Request(url, headers={"User-Agent": "LM7-source-verification/1.0"}), timeout=20) as r:
            data = r.read(4_000_001)
            record.update({"status_code": r.status, "final_url": r.url,
                           "content_type": r.headers.get("Content-Type")})
        assert len(data) <= 4_000_000, "response exceeds read bound"
        path = DEST / (name + (".xml" if "mets" in name else ".json"))
        path.write_bytes(data)
        record.update({"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(), "raw_path": str(path)})
        if "mets" in name:
            doc = ET.fromstring(data)
            matches = []
            for e in doc.iter():
                if e.tag.endswith("div") and "Algebraic cycles" in e.attrib.get("LABEL", ""):
                    matches.append(ET.tostring(e, encoding="unicode"))
                if e.tag.endswith("mods") and "Bloch" in ET.tostring(e, encoding="unicode"):
                    matches.append(ET.tostring(e, encoding="unicode"))
            record["matching_article_metadata"] = matches
        else:
            obj = json.loads(data)
            if "crossref" in name:
                m = obj.get("message", {})
                record["public_locations"] = {k: m.get(k) for k in ["title", "DOI", "URL", "link", "resource"]}
            else:
                record["public_locations"] = {k: obj.get(k) for k in ["id", "title", "doi", "open_access", "best_oa_location", "locations"]}
        record["status"] = "read"
    except HTTPError as e:
        record.update({"status": "HTTP failure; no retry or bypass", "status_code": e.code, "reason": str(e)})
    except Exception as e:
        record.update({"status": "retrieval failure", "reason": type(e).__name__ + ": " + str(e)})
    return record

with ThreadPoolExecutor(max_workers=len(routes)) as pool:
    results = list(pool.map(fetch, routes))
output = {"scope": "Exact public metadata URLs already opened through the web reader. No credentials, authentication, access challenge or restricted content was bypassed.", "routes": results}
(ROOT / "root_public_source_routes.json").write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(output, indent=2, ensure_ascii=False))
