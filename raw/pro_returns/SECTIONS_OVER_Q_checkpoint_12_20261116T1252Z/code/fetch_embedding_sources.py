from pathlib import Path
import subprocess
import urllib.request
import re

root = Path(__file__).resolve().parents[1]
sources = {
    "nsw23": "https://www.mathi.uni-heidelberg.de/~schmidt/NSW2e/NSW2.3.pdf",
    "fehm_legrand2022": "https://www.numdam.org/item/10.5802/jtnb.1215.pdf",
    "kim_koenig2021": "https://arxiv.org/pdf/1911.08742",
    "neftin2012": "https://neftin.net.technion.ac.il/files/2015/10/20-6-12.pdf",
}
for name, url in sources.items():
    pdf = root / "sources" / (name + ".pdf")
    txt = pdf.with_suffix(".txt")
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            content = response.read()
        if not content.startswith(b"%PDF"):
            print(name, "not a PDF", len(content), response.url)
            print("links", re.findall(r'href=[\"\x27]([^\"\x27]+)', content.decode("latin1"), re.I))
            continue
        pdf.write_bytes(content)
        subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True)
        print(name, "downloaded and extracted", len(content), "bytes")
    except Exception as error:
        print(name, type(error).__name__, str(error))
