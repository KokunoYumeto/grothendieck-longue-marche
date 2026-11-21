"""Record root's cross-page notation decisions without changing frozen audits."""
from pathlib import Path
from datetime import datetime, timezone
import json
import assemble
B=Path(__file__).resolve().parents[1];stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
items=[('055','P09b','M1145',r'$=$',r'$\unsure{=|\overline m}$','undecided','medium',False,'The lower stroke begins with a shallow cup and then runs into a smooth low plateau. Beside the pronounced cup and central cusp on 070 P03 and 071 P04, this flattened contour does not settle equals versus barred m. Reopen M1145 with both written candidates; H’s full même remains an expansion. The comparison concerns the visible component contours at these recorded occurrences.'),('071','P04','M1196',r'\unsure{=|\overline{m}}',r'\overline{m}','first','high',True,'The lower component has a distinct entrance cup followed by a central upward cusp and a long low right return. The same cup/cusp/return sequence is visible in the confirmed barred-m form at 070 P03; the upper component is the separate bar. This positive contour correspondence supports barred m here. The blind B04 independently supplied that reading; the cross-page comparison supplies the final graphical decision.')]
for n,cid,mid,old,new,decision,confidence,against,ev in items:
 page='149_scan'+n;rp=B/'reviews'/f'{page}.json';r=json.loads(rp.read_text());assert r.get('audit');assert not r.get('post_audit_notation_changes')
 p=B/'pages'/f'{page}.tex';t=p.read_text();assert t.count(old)==1;t=t.replace(old,new);p.write_text(t)
 c=next(x for x in r['changes'] if x['id']==cid);oldrow=c['final'];c.update(final=new,evidence=ev,confidence=confidence,against_C=against)
 d=next(x for x in r['decisions'] if x['id']==mid);d.update(decision=decision,reading=new.strip('$'),evidence=ev,confidence=confidence)
 r['doubts']=[x for x in r['doubts'] if mid not in x['place']]
 if decision=='undecided':r['doubts'].append(dict(place=cid+' / '+mid+', prose shorthand',reading=new.strip('$'),alternatives='equals sign; barred m',confidence=confidence,reason=ev))
 for x in r['hand']:
  if (n=='055' and x['form']=='=') or (n=='071' and x['form']=='two-component prose shorthand'):
   x.update(form=new.strip('$'),observation=ev,scope='The local contour is compared with 070 P03 and the other explicitly listed shorthand crops; no unviewed occurrence is settled by this comparison.',witness_errors='H expands the written shorthand to même. '+('C’s mark remains undecided.' if decision=='undecided' else 'C’s first candidate is resolved from the compared cup/cusp contour.'))
 found=False
 for x in r['notation']:
  if mid in x.get('places','') or (n=='055' and x.get('form')=='='):
   x.update(form=new.strip('$'),meaning='The written prose shorthand at this occurrence, retained unexpanded. '+('The lower contour remains too flattened to decide its two candidates.' if decision=='undecided' else 'The lower cup/cusp/return matches the recorded barred-m contour.'));found=True
 if not found:r['notation'].append(dict(form=new.strip('$'),meaning='The two-component prose shorthand; its shallow lower contour leaves equals/barred-m open.',places='line 8, P09 / M1145'))
 for x in r.get('abbreviations',[]):
  if x.get('written') in ['=',r'\unsure{=|\overline{m}}',r'\overline m',r'\overline{m}'] and ('P09' in x.get('places','') or 'P04' in x.get('places','') or mid in x.get('places','')):x['written']=new.strip('$')
 r['post_audit_notation_changes']=[dict(utc=stamp,place=c['place'],previous_reading=oldrow,final_reading=new,evidence=ev,crop=c['crop'],coords=c['box'],comparison_crops=['crops/149_scan055_P09.png','crops/149_scan070_P03.png','crops/149_scan071_P04.png'])]
 r['notes'].append('Final cross-page notation comparison: '+ev+' The fixed blind inputs, return and original audit decision remain unchanged; the subsequent amendment is separately dated in the changes log.')
 rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=B/'notation_crosscheck.json';r=json.loads(p.read_text());r['partial_reconciliation_utc']=stamp;r['shorthand_055_071']=[dict(scan=n,mark=mid,reading=new,evidence=ev) for n,cid,mid,old,new,dec,conf,ag,ev in items];p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
with (B/'progress.log').open('a') as f:f.write('notation comparison '+stamp+': 055 M1145 reopened as equals/barred-m; 071 M1196 resolved to barred-m by the compared lower cup/cusp contour; frozen audit records unchanged\n')
print(assemble.build())
