"""Reconcile current metadata after audits 047-050; never edit transcription files."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'pages').glob('*.tex')}
for n in range(47,51):
    path=R/'records'/f'149_scan{n:03}.json';r=json.loads(path.read_text())
    if n==47:
        for d in r.get('unindexed_decisions',[]):
            if d['place']=='Cancelled phrase after first B_U→B_V':d.update(reading=r'\unsure{de tels|dont le|dans le}',ink='The initial d and later l loop remain under two parallel strikes; the low middle and word division leave all three readings open.')
        for e in r['inventory']:
            if e['element']=='E07':e['first_words_or_objects']='On peut aussi regarder de/des tels modèles sur un corps'
            if e['element']=='E12':e['first_words_or_objects']='de tels / dont le / dans le (doubtful cancelled phrase)'
            if e['element']=='E15':e['first_words_or_objects']='élémentaire anabélien, cet homph (doubtful short form) … seulement'
            if e['element']=='E18':e['first_words_or_objects']='il suffit (suffit locally doubtful under the strike)'
    if n==48:
        for h in r['hand_log']:
            if h['habit'].startswith('Script E is rounded'):h['scope']='The first three script forms are clear; the last is retraced and retains script E with B as an alternative. No separately ordered old symbol is invented.'
        for e in r['inventory']:
            if e['element']=='E06':e['first_words_or_objects']='modèle (locally doubtful under the strike)'
            if e['element']=='E13':e['first_words_or_objects']='underlined NB, pr l’instant; V itself elementary anabelian; dim. 1. / donc ending doubtful'
    if n==49:
        for e in r['inventory']:
            if e['element']=='E12':e['first_words_or_objects']=r'\unsure{complets|complètes|compacts} pour U, with two insertion leaders'
        for h in r['hand_log']:
            if h['habit']=='Compressed low joins and terminal hooks':h['places']='Oblique note article, condition ending, risquent ending, and équivt./équiv. short form'
        for t in r['notation']:
            if t['form']==r'\unsure{\Pi|\pi}_U':t.update(form=r'\unsure{\Pi|\pi}_{\unsure{U|K}}',meaning='Group in the action sentence: capital Pi remains primary, with lowercase and an additional U/K subscript doubt.',evidence='Blind B03: the cap and legs do not settle case, and the lowered letter is retraced. The later fixed-subgroup display separately retains subscript U.')
        r['notation'].append(dict(form=r'\unsure{\Pi|\pi}_U^{\Gamma^{\prime\circ}}=\{1\}',meaning='Fixed-subgroup expression with locally clear U and uncertain Pi/pi case.',evidence='Blind B03: the full display retains the U, prime, hollow ring, equality, braces and unit 1.'))
    if n==50:
        for e in r['inventory']:
            if e['element']=='E10':e['first_words_or_objects']='Spec with an uncertain O, clear capital X and uncertain small x subscript, including its parentheses'
            if e['element']=='E13':e['first_words_or_objects']='The doubtful ess./ets./en. abbreviation followed by de type fini sur Q.'
    path.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
after={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'pages').glob('*.tex')}
assert before==after
print('Current metadata reconciled for scans 047-050; all page bytes unchanged.')
