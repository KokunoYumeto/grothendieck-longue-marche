from pathlib import Path
from datetime import datetime,timezone
import json
W=Path(__file__).resolve().parents[1];p=W/'reviews/143_scan016_readerB.json';d=json.loads(p.read_text())
with (W/'reader_schedule.tsv').open('a') as f:f.write(datetime.now(timezone.utc).isoformat()+'\tfirst\t143_scan021\tB\n')
mp={0:('on_aura',[330,80,1095,170]),8:('factorisant',[290,1245,1640,1515]),14:('On_note',[255,2055,1620,2200]),15:('On_note',[255,2055,1620,2200]),16:('On_note',[255,2055,1620,2200]),19:('number15',[18,2280,95,2352])}
for i,(n,b) in mp.items():d['changes'][i].update(crop=f'crops/143_scan016_main_{n}.png',box=b)
d['changes'][14]['marked_in_H']=True
d['decisions'][1].update(crop='crops/143_scan016_main_On_note.png',box=[255,2055,1620,2200])
for i in [17,18]:
 d['changes'][i]['against_C']=True;d['changes'][i]['ink']+=' The X alphabet also follows the shared looped, transversely crossed mathfrak encoding; that font choice alone does not alter the mathematical variable.'
fontrows=[('First display, bracketed cover pair',r"\widetilde X'[j],\widetilde X'[j']",r"\widetilde{\mathfrak{X}}'[j], \widetilde{\mathfrak{X}}'[j']",r"\widetilde{\mathfrak X}'[j],\widetilde{\mathfrak X}'[j']",'readerB_first_isom_display',[375,138,1662,400]),('First display, right torsor pair',r"\widetilde X'(j),\widetilde X'(j')",r"\widetilde{\mathfrak{X}}'(j), \widetilde{\mathfrak{X}}'(j')",r"\widetilde{\mathfrak X}'(j),\widetilde{\mathfrak X}'(j')",'readerB_first_isom_display',[375,138,1662,400]),('Reconstruction paragraph, two X(J) occurrences',r"\widetilde X'(J)",r"\widetilde{\mathfrak{X}}'(J)",r"\widetilde{\mathfrak X}'(J)",'main_reconstructed',[315,600,1635,900]),('Action diagram, lower left pair',r"\widetilde X'(j),\widetilde X'(j')",r"\widetilde{\mathfrak{X}}'(j), \widetilde{\mathfrak{X}}'(j')",r"\widetilde{\mathfrak X}'(j),\widetilde{\mathfrak X}'(j')",'readerB_action_diagram',[420,1505,1665,1862]),('Action diagram, lower right pair',r"\widetilde X'(gj),\widetilde X'(gj')",r"\widetilde{\mathfrak{X}}'(gj), \widetilde{\mathfrak{X}}'(gj')",r"\widetilde{\mathfrak X}'(gj),\widetilde{\mathfrak X}'(gj')",'readerB_action_diagram',[420,1505,1665,1862]),('Operation parenthesis, literal I object',r"\widetilde X'(I)",r"\widetilde{\mathfrak{X}}'(I)",r"\widetilde{\mathfrak X}'(I)",'main_On_note',[255,2055,1620,2200])]
for place,C,H,F,cr,box in fontrows:d['changes'].append(dict(place=place,C=C,H=H,final=F,against_C=True,against_H=False,kind='misread symbol or index',ink='The curled X has a transverse stroke. Its shared mathfrak encoding is a medium-confidence alphabet decision; no new variable is inferred. The primes, tildes and point arguments in this expression were inspected separately.',confidence='medium',crop=f'crops/143_scan016_{cr}.png',box=box,marked_in_H=False,consequential=False))
for e in d['check_events']:
 if e['statement_id']=='143_scan016-N3':e['type']='carried as background without fault found'
d['main_adjudication']='Original, seven reader crops and five main crops inspected. All changes and doubts visually adjudicated; six groups of remaining uncertainty retained. No date is present.'
d['notes'].append({'id':'143_scan016-N6','text':'Main adjudication accepts the candidate with localized doubts at the extra groupoid suffix, prose abbreviation point, cancellation, two low spots and connector tip. No date is written. Repeated X alphabets were checked as glyph encoding, not inferred changes of mathematical variable.'})
p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
