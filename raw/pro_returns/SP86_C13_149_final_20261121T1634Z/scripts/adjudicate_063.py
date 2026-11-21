"""Root decisions on the six differing blind crops of scan 063."""
from pathlib import Path
import json
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan063';rp=B/'reviews'/f'{page}.json';r=json.loads(rp.read_text());assert not r.get('audit')
p=B/'pages'/f'{page}.tex';t=p.read_text();old='suffira';new=r'suffi\unsure{r.|ra|t.}';assert t.count(old)==1;p.write_text(t.replace(old,new))
ev='The initial s and flattened u lead into two tall f strokes, followed by the dotted low i. The next short stroke rises and turns right, favoring r over t. The terminal dark mark is a detached compact point; its small size does not settle a full a-loop. The reading is therefore qualified among suffir., suffira and suffit., preserving the point-like ending without expanding it.'
for c in r['changes']:
 if c['id']=='P03':c.update(final=new,evidence=ev,confidence='medium',against_C=False)
r['doubts'].append(dict(place='line 3, cela suffi..., B04',reading=new,alternatives='suffir.; suffira; suffit.',confidence='medium',reason=ev))
r['notes']=[n.replace('cela suffira peut-être','cela '+new+' peut-être') for n in r['notes']]
r['notes'].append('Blind crop B04 reopens the ending after suffi: the final mark is point-like, while a very compressed a remains possible. The page keeps the written alternatives and the following peut-être. No grammatical completion or mathematical check is added.')
for h in r['hand']:
 if h['form']=='f in suffira and renforce':h.update(form='f in suffi... and renforce',observation='The f may have a long descending stroke and low leftward return. The suffi... group has two tall stems; its ending remains qualified after blind inspection. Renforce has one tall f between the low ren and orce portions.')
for d in r['diff_coverage']:
 if d['row']==5:d['reason']='Two tall f stems and dotted i support suffi; its following r/t and point/a ending are qualified after blind inspection.'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(b,decision,evidence):D[b]=dict(keep_first=True,changed=False,decision=decision,evidence=evidence)
keep('B02','Retain the underlined heading','The continuous rule runs below Conjecture and B. The isolated upper-right stroke is the prime; the dark rule endpoint lies beneath it. The second reading places only the same B-prime in a math wrapper, with no source-token change.')
keep('B03','Keep the opening word unresolved','A large S is followed by a low joined group, a detached dot, a long flattened run and the angular terminal t. The internal strokes do not separate sufficiently to exclude either Soient or Soit. The shorter blind reading does not resolve the existing mark.')
D['B04']=dict(final=new,changed=True,decision='Qualify the terminal letter and point',evidence=ev)
keep('B06','Retain the same indexed Gamma formula','Both large Gamma forms, the two equality bars and the lowered K letters are visible. The first K bears a short detached bar. The separator between them is upright. Bar/braces, mid/vertical-bar and inline-math wrappers map to these same written components.')
keep('B07','Retain the calligraphic X reading','Gamma carries a small round raised loop. Agissant has the low a, looped descending g, dotted i and connected ss/a/n/t. The final X has two opposed curved branches with hooked feet and a crossing horizontal flourish, supporting the calligraphic X already used for this written form on the page.')
keep('B12','Retain the localized V/que/q. uncertainty','The large leading group has a descending branch, low vertex, rising branch and one short rightward terminal. It supports the V-like first alternative without securely settling the word alternatives. The following U has a long curved left entry and low cup, followed by slash and pi; its looped form supports the retained calligraphic U. No separate pair of equality bars appears in the gap. The blind checkmark option describes the same angular group and supplies no further readable letter.')
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D));record(page);assign('reader_b')
