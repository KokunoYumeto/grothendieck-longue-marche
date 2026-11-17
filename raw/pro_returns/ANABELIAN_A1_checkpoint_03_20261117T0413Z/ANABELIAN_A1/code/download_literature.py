#!/usr/bin/env python3
"""Fetch only the primary PDFs opened for this audit, then record hashes.

Existing files are preserved. Network failures are recorded, never silently
replaced by a different edition. Run from any directory with Python 3 and
Poppler pdftotext installed. The output is a reproducibility manifest.
"""
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "sources"
SOURCES = [
    ("Mochizuki2007", "https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations.pdf", "turn2view1"),
    ("Mochizuki2007_latex", "https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations%20(LaTeX%20version).pdf", "turn1view3"),
    ("Mochizuki2014_comments", "https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations%20(comments).pdf", "turn2view0"),
    ("MochizukiTamagawa2008", "https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Algebraic%20and%20Anabelian%20Geometry%20of%20Configuration%20Spaces.pdf", "turn4view3"),
    ("MochizukiTamagawa2015_comments", "https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Algebraic%20and%20Anabelian%20Geometry%20of%20Configuration%20Spaces%20(comments).pdf", "turn2view2"),
    ("SaidiTamagawa2009_journal", "https://www.kurims.kyoto-u.ac.jp/~prims/pdf/45-1/45-1-5.pdf", "turn16view1"),
    ("SaidiTamagawa2017", "https://arxiv.org/pdf/1708.08773", "turn50view0"),
    ("Wakabayashi2016", "https://arxiv.org/pdf/1507.00622", "turn50view1"),
    ("Stix2005_monodromy_arxiv", "https://arxiv.org/pdf/math/0408315", "turn23view1"),
    ("BoggiZalesskii2019", "https://arxiv.org/pdf/1408.5419", "turn14view1"),
    ("SGA1", "https://arxiv.org/pdf/math/0206203", "downloaded-local; web open failed"),
    ("Sun2025_virtual", "https://arxiv.org/pdf/2505.06826v2", "turn2view3 HTML plus local PDF"),
    ("Sun2026_virtual", "https://arxiv.org/pdf/2604.23485v1", "turn2view4 HTML plus local PDF"),
    ("CiperianiStix2015", "https://jtnb.centre-mersenne.org/item/10.5802/jtnb.892.pdf", "turn50view2"),
    ("Poonen2005_etale", "https://math.mit.edu/~poonen/papers/etale.pdf", "turn38view0"),
    ("BogomolovTschinkel2002", "https://cims.nyu.edu/~tschinke/papers/yuri/02ram/ram4.pdf", "turn38view1"),
    ("AchterPries2015", "https://www.math.colostate.edu/~pries/Preprints/15suprank1015arxiv.pdf", "turn42view0"),
    ("KedlayaLittWitaszek2023", "https://arxiv.org/pdf/2010.01130", "turn68view0"),
    ("Raynaud2000_ordinarite", "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/16AB72912D3CE32BFC5D012B1025A8E4/S0010437X00000440a.pdf/revetements-des-courbes-en-caracteristique-pandgt0-et-ordinarite.pdf", "turn81view0"),
    ("OzmanPries2019", "https://archive.intlpress.com/site/pub/files/_fulltext/journals/ajm/2019/0023/0003/AJM-2019-0023-0003-a005.pdf", "turn78view1"),
    ("Lepage2013_log", "https://www.numdam.org/article/AIF_2013__63_4_1427_0.pdf", "turn87view0; independently opened by literature auditor"),
    ("KhassaKhanduja2010", "https://www.impan.pl/shop/en/publication/transaction/download/product/87611", "turn94view0"),
    ("HoshiSawadaTsujimura2024", "https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1984.pdf", "turn98view0"),
    ("HoshiTsujimura2026", "https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS2007.pdf", "turn98view1"),
    ("AchingerHubnerLaraStix2024_beyondfs", "https://arxiv.org/pdf/2411.13662", "turn108view0"),
    ("MilneAV2008", "https://www.jmilne.org/math/CourseNotes/AV.pdf", "root turn112view0; II Lemma 1.3 and Remark 1.4, pp77--78"),
    ("Hassett2003_weighted", "https://www.math.brown.edu/bhassett/papers/weights/weights10.pdf", "turn123view0; Theorem 2.1"),
    ("Knudsen1983_II", "https://journals.msp.org/mscand/article/download/1622/1621/1653", "turn123view1; publisher PDF, scanned; metadata turn121view0"),
    ("ADH_online2025", "https://www.mat.univie.ac.at/~maschenbrenner/pdf/mt.pdf", "turn126view0; Lemma 3.4.2 independently opened; online version January 2025"),
    ("Zapponi2010_Lame", "https://arxiv.org/pdf/1004.3695", "turn640500930view0; turn891547806view1; Proposition 2.1 and Theorem 2.2, not the erroneous blanket supersingularity sentence in Appendix B.2"),
    ("LandesmanLitt2024_Prill", "https://api.algebraicgeometry.nl/Article/20170/2024-2-009.pdf", "turn256309751view1; turn569124275view0; Theorem 1.2 and Proposition 2.4 explicitly over C"),
    ("BooherPries2025_genus5", "https://arxiv.org/pdf/2410.20262v2", "turn256309751view2; Theorem 1.2, existence of special genus-three bases in p=3 mod4"),
]

def fetch(entry):
    stem, url, ref = entry
    out = {"name": stem, "url": url, "tool_ref": ref}
    pdf = DEST / (stem + ".pdf")
    txt = DEST / (stem + ".txt")
    try:
        if not pdf.exists():
            request = urllib.request.Request(url, headers={"User-Agent": "Mathematical-source-audit/1.0"})
            with urllib.request.urlopen(request, timeout=35) as response:
                data = response.read()
            if not data.startswith(b"%PDF"):
                raise ValueError("Response is not a PDF")
            pdf.write_bytes(data)
            out["action"] = "downloaded"
        else:
            out["action"] = "preserved existing"
        if not txt.exists():
            subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True)
        out.update(status="ok", bytes=pdf.stat().st_size,
                   sha256=sha256(pdf.read_bytes()).hexdigest(),
                   text_bytes=txt.stat().st_size)
    except Exception as error:
        out.update(status="failed", error=str(error))
    return out

def main():
    DEST.mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=4) as executor:
        result = list(executor.map(fetch, SOURCES))
    output = json.dumps(result, indent=2, ensure_ascii=False)
    (ROOT / "code" / "download_literature.json").write_text(output + "\n")
    print(output)

if __name__ == "__main__":
    main()
