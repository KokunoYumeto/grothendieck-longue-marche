"""Utilities for explicit, human-reviewable main-reader decisions.

These functions do not decide a reading. The main reader supplies selections,
readings, evidence and confidence after personally viewing the relevant crops.
"""
from pathlib import Path
import json
OUT=Path(__file__).resolve().parents[1]
ROOT=OUT.parent
def load(scan):
 packet=ROOT/'staging'/f'scan{scan:03d}'
 info=json.loads((packet/'page.json').read_text())
 reports={r:json.loads((OUT/'readers'/f'scan{scan:03d}'/r/'report.json').read_text()) for r in ['R1','R2','R3']}
 texts={r:(OUT/'readers'/f'scan{scan:03d}'/r/'reading.tex').read_text() for r in reports}
 return info,reports,texts
def row_from(report,index,**overrides):
 r=report['differences'][index-1]
 row={k:r.get(k) for k in ['place','c','h','against_c','against_h','kind','marked_in_H','confidence','crop']}
 row['final']=r['reading'];row['scan_shows']=r['evidence'];row['readers']={};row.update(overrides)
 return row
def normal_crop(scan,reader,value):
 if not value:return None
 p=Path(value)
 if p.is_absolute():return str(p.relative_to(OUT))
 if (OUT/p).exists():return str(p)
 d=OUT/'readers'/f'scan{scan:03d}'/reader
 if (d/p).exists():return str((d/p).relative_to(OUT))
 candidates=list(d.rglob(p.name))
 if len(candidates)==1:return str(candidates[0].relative_to(OUT))
 raise ValueError('Cannot resolve crop: '+value)
def start(scan,baseline='R1'):
 info,reports,texts=load(scan);r=reports[baseline]
 d=dict(scan=scan,folder=info['folder'],their_page=int(info['their_page']),filename=Path(info['codex_file']).name,main_adjudication_complete=False,rows=[],doubts=r.get('remaining_doubts',[]),inventory=r['inventory'],notes=r['notes'],abbreviations=r.get('abbreviations',[]),check_events=r.get('check_events',[]),slips=[],workflow={})
 return d,reports,texts
def save(d,text):
 assert d.get('main_adjudication_complete') is True
 (OUT/'pages'/d['filename']).write_text(text)
 (OUT/'decisions'/f"scan{d['scan']:03d}.json").write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
