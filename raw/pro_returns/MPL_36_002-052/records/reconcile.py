from pathlib import Path
import datetime,json,csv
ROOT=Path(__file__).resolve().parents[1]
def revise(scan,old,new,reason):
 p=ROOT/'pages'/f'MPL_36_002-052_36_scan{scan:03}.tex';s=p.read_text();assert old in s,(scan,old)
 p.write_text(s.replace(old,new))
 stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 with (ROOT/'records/audit_changes.jsonl').open('a') as f:f.write(json.dumps({'scan':scan,'utc':stamp,'phase':'notation and integration review','changes':[(old,new)],'notes':reason},ensure_ascii=False)+'\n')
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03} integration correction {stamp}: {reason}\n')
if __name__=='__main__':
 p=ROOT/'pages/MPL_36_002-052_36_scan034.tex';s=p.read_text()
 start=s.index(r"d'où comme en (2.1.4), pour toute ")
 end=s.index(r', un\deleted{e} accouplement',start)
 revise(34,s[start:end],r"d'où comme en (2.1.4), pour toute $\xi\in\operatorname{Biext}(P,Q;G)$",'Removed duplicated oval and leader from the second xi membership: the scan encircles only the first occurrence.')
 p=ROOT/'MPL_36_002-052_inventory.csv';rows=list(csv.DictReader(p.open()));fields=list(rows[0])
 for r in rows:
  if int(r['scan']) in (29,31,33,37,48,50):r['sheet_kind']='reused_typed'
 rows.sort(key=lambda r:(int(r['scan']),r['element']))
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
 with (ROOT/'progress.log').open('a') as f:f.write('inventory classification: handwritten fronts 029,031,033,037,048,050 classified reused_typed because paired typed versos are supplied; sorted by scan and element.\n')
