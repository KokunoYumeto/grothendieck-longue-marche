from pathlib import Path
from datetime import datetime,timezone
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_15_195-228+18_002-017'
def audit(cote,scan,observations,images=None):
 expected=json.loads((ROOT/'records/expected_pages.json').read_text())
 idx=expected.index({'cote':cote,'scan':scan})
 for e in expected[:idx]:
  assert (ROOT/'records'/f'audit_{e["cote"]}_{e["scan"]:03d}.json').exists(),e
 log=(ROOT/'progress.log').read_text()
 assert 'transcription frozen ' not in log
 rec=ROOT/'records'/f'audit_{cote}_{scan:03d}.json'
 assert not rec.exists()
 page=ROOT/'pages'/f'{PREFIX}_{cote}_scan{scan:03d}.tex'
 now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 rec.write_text(json.dumps({'cote':cote,'scan':scan,'audited':now,'observations':observations,'images_inspected':images or ['whole'],'page_sha256_after_audit':hashlib.sha256(page.read_bytes()).hexdigest()},ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'progress.log').open('a') as f:f.write(f'{cote} scan {scan:03d} audited {now}\n')
 print(f'{cote} scan {scan:03d} audited {now}')
def pencil_folio(cote,scan):
 p=ROOT/'pages'/f'{PREFIX}_{cote}_scan{scan:03d}.tex'
 s=p.read_text();s=re.sub(r'\\mspage\{([^{}]+)\}',r'\\margin{\1}',s);p.write_text(s)
