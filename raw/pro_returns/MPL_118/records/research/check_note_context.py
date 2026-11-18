"""Post-freeze context searches for every primary research-note item.

This is a source-discovery ledger, not a mathematical or image-reading check.
The complete notes supply the selected manuscript-page/section locators.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, re, subprocess

R=Path(__file__).resolve().parent
WORK=R.parents[2]
parts=['root_notes.md','root_additional_checks.md','root_claims.md',
       'root_self_flags.md','root_reading_questions.md','root_titles.md']
notes={}
for part in parts:
    s=(R/part).read_text()
    for m in re.finditer(r'^### (MPL118-[A-Z]+\d+) — ([^\n]+)\n([\s\S]*?)(?=^### |^## |\Z)',s,re.M):
        notes[m[1]]={'title':m[2],'text':m[3],'part':part}

topics={
 'class':r'WSF|WSC|Serre|foncteurs propres|smooth.*proper',
 'integral':r'intégr|int[eé]gral|Grothendieck construction|Grothendieck.*integr',
 'filtration':r'filtration|minimum.stage|passage.*limite|Loc.*3',
 'group':r'groupoïde|groupoid|stabilizer|stabilisateur',
 'product':r'produits? (finis|binaires|de repr)|products? of representables|4\.3\.2',
 'infinite':r'fence|zigzag|bounded|produits? infinis|infinite products',
 'pushout':r'cocart[eé]sien|pushout|amalgam|immersion ouverte',
 'saturation':r'saturé|saturat|4\.2\.4',
 'sum':r'sommes|coproduct|nonempt|non.empty',
 'fraction':r'fractions|rectification|cofibrant objects',
 'interval':r'interval|séparant|separating',
 'factor':r'factorisation|factorization|comma|Fib\(',
 'cone':r'cofib[er]|cofibre|cylindre|cylinder|cône|cone',
 'duality':r'dualit|opposit|oppos[eé]|W\^',
 'localizer':r'Loc[ (]|localis[ae]ur|localiz[ae]r|theorem A|théorème A',
 'gluing':r'bifonct|profunct|collage|recollement|H_\{?X',
 'date':r'avril|April|1983|1985|soutenance',
 'title':r'Cohomology properties|Fibre.by.fibre|Fibration.like|Coh\. prop|Immersions fermées',
 'pages':r'pages? 1|pages? 2|2 bis|page count|pagination|pagerange|38 scan|40 pages',
 'total':r'filtrant|filtered|totalement.*asph|totally.*asph',
 'w7':r'W\(7|W7|W_7|reverse.excision|biconditional',
 'dwyer':r'Dwyer|dwy[eé]r|dwy\\',
 'abelian':r'Ab\^|abelian|ab[eé]lien|colim.*exact|exact.*colim',
}
assign={}
def setids(topic, group, nums):
    for n in nums: assign[f'MPL118-{group}{n:02d}']=topic
for topic,group,nums in [
 ('w7','H',[1]),('total','H',[2]),('localizer','H',[3]),
 ('integral','C',[1,2]),('filtration','C',[3,13]),('group','C',[4,7]),
 ('product','C',[5]),('infinite','C',[6]),('cone','C',[8]),
 ('saturation','C',[9,10]),('sum','C',[11]),('pushout','C',[12,14]),
 ('class','M',[1,2,3,4,6]),('duality','M',[5]),('factor','M',[7]),
 ('pushout','M',[8,11,12]),('localizer','M',[9,18]),('integral','M',[10,30]),
 ('gluing','M',[13,14]),('fraction','M',[15]),('interval','M',[16]),
 ('saturation','M',[17]),('sum','M',[19,21]),('infinite','M',[20]),
 ('product','M',[22,23,24,25]),('filtration','M',[26,29]),
 ('class','M',[27]),('dwyer','M',[28]),('abelian','M',[31]),
 ('factor','M',[32,33]),
 ('class','SF',list(range(1,11))),('factor','SF',[11,12]),
 ('cone','SF',[13,14]),('pushout','SF',[15,16,17,18,19,48]),
 ('integral','SF',[20,21]),('fraction','SF',[22,23]),('interval','SF',[24]),
 ('sum','SF',list(range(25,35))),('product','SF',[35,36,37,38]),
 ('infinite','SF',[39,42,43]),('saturation','SF',[40,41,46]),
 ('filtration','SF',[44,45]),('group','SF',[47]),
 ('title','R',[1]),('date','R',[2]),('factor','R',[3]),('class','R',[4,5]),
 ('localizer','R',[6]),('pushout','R',[7,10,11,12]),('gluing','R',[8]),
 ('duality','R',[9]),('infinite','R',[13]),('fraction','R',[14]),
 ('product','R',[15,16,17]),('group','R',[18]),('filtration','R',[19]),
 ('saturation','R',[20]),
 ('title','T',[1,2]),('gluing','T',[3]),('pages','T',[4,5,6,8]),('date','T',[7])
]: setids(topic,group,nums)
assert set(assign)==set(notes), {'unassigned':sorted(set(notes)-set(assign)), 'extra':sorted(set(assign)-set(notes))}
files=subprocess.run(['rg','--files','context'],cwd=WORK,text=True,capture_output=True,check=True).stdout.splitlines()
files=[f for f in files if f.endswith(('.tex','.md'))]
recorded=datetime.now(timezone.utc).isoformat()
rows=[]
for sid,n in notes.items():
    topic=assign[sid];pattern=topics[topic]
    proc=subprocess.run(['rg','--json','--ignore-case','--regexp',pattern,*files],cwd=WORK,text=True,capture_output=True)
    assert proc.returncode in (0,1), (sid,proc.stderr)
    hits=[]
    for line in proc.stdout.splitlines():
        obj=json.loads(line)
        if obj['type']=='match':
            d=obj['data'];hits.append({'file':d['path']['text'],'line':d['line_number'],
                                      'excerpt':d['lines']['text'].strip()[:220]})
    # Prefer the files actually cited in the note, retaining global search scope.
    preferred=[]
    for h in hits:
        if h['file'] in n['text'] or Path(h['file']).name in n['text'] or ('Hua' in n['text'] and '/hua_project/' in h['file']):
            preferred.append(h)
    chosen=(preferred or hits)[:12]
    rows.append({'id':sid,'title':n['title'],'note_file':n['part'],'query':pattern,
                 'topic':topic,'searched_files':len(files),'total_matching_lines':len(hits),
                 'selected_search_hits':chosen,
                 'interpretation':'Search evidence only; the note supplies the evaluated relation and exact contextual section/manuscript-page locator. A hit is not a proof check.'})
(R/'context_search_ledger.json').write_text(json.dumps({'recorded_utc':recorded,
    'scope':'Only supplied post-freeze context text; no image access, OCR, or transcription changes.',
    'note_count':len(rows),'rows':rows},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'primary_note_count':len(rows),'zero_hit_ids':[x['id'] for x in rows if not x['total_matching_lines']]},ensure_ascii=False))
