from pathlib import Path
import json,re,datetime,hashlib
R=Path('/workspace/scratch/94548b74fbe0/out/readers/013/A')
r=json.loads((R/'report.json').read_text())
t=(R/'reading.tex').read_text()
plain='\n'.join(line.split('%',1)[0] for line in t.splitlines())
stack=[]
for j,ch in enumerate(plain):
    if ch=='{' and (j==0 or plain[j-1]!='\\'):stack.append(j)
    elif ch=='}' and (j==0 or plain[j-1]!='\\'):
        assert stack,('unmatched closing brace',j)
        stack.pop()
assert not stack,('unclosed braces',stack)
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',plain):
    op,name=m.groups()
    if op=='begin':envs.append(name)
    else:
        assert envs and envs[-1]==name,('environment mismatch',name,envs)
        envs.pop()
assert not envs
assert plain.count('$')%2==0
assert plain.count(r'\scanpage{13}')==1
assert r'\cotefile' not in plain and r'\mspage' not in plain
assert '% archive sheet number: 12' in t
allowed={'scanpage','margin','begin','end','path','draw','fill','node','scriptsize','figure','resizebox','rlap','phantom','deleted','unsure','mathord','mathrm','overline','underline'}
commands=set(re.findall(r'\\([A-Za-z]+)',plain))
assert commands<=allowed,commands-allowed
assert r'\newcommand' not in plain and r'\renewcommand' not in plain
for c in r['crops']:
    assert (R/c['path']).is_file()
    assert c['viewed'] and c['successful_view_count']==1
    l,top,right,bottom=c['bbox'];assert 0<=l<right<=2365 and 0<=top<bottom<=1688
assert len(r['crops'])==24
kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
for d in r['differences']:
    assert d['kind'] in kinds,(d['id'],d['kind'])
    assert d['H'] is None and d['diff_H'] is False
    if d['readers_crop']:assert (R/d['readers_crop']).is_file()
    for c in d.get('additional_crops',[]):assert (R/c).is_file()
for d in r['doubts']:
    if d['crop']:assert (R/d['crop']).is_file()
assert len(r['C_doubt_source_map'])==13
assert sum(len(a['local_decisions']) for a in r['C_doubt_source_map'])==14
assert sum(x['status']=='resolved' for a in r['C_doubt_source_map'] for x in a['local_decisions'])==8
for id in ['A-D03','A-D04','A-D06','A-D08','A-D09']:
    d=next(x for x in r['differences'] if x['id']==id)
    assert d['C_doubt_status']=='retained' and d['diff_C'] is False
actual=[d for d in r['differences'] if d['diff_C']]
groups=[d['change_group'] for d in actual]
assert len(set(groups))==len(groups),('duplicated actual change group',groups)
assert r['check_events']==[]
assert len({i['element'] for i in r['inventory']})==len(r['inventory'])
assert all(i['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for i in r['inventory'])
assert all(i['transcribed']=='yes' for i in r['inventory'])
pathcounts={}
for p,num in [('T01.H',14),('XA.H',5),('XB.H',4),('XC.H',3),('XD.H',4),('XE20.H',4),('XE23.H',4)]:
    pathcounts[p]=len(re.findall(r'^% '+re.escape(p)+r'\d+',t,re.M));assert pathcounts[p]==num
assert len(re.findall(r'^% E\d\d:',t,re.M))==10
for a in ['Méditation','Vers un plus long Voyage','Die Eltern','(Les parents)',"(L'enfant)",'Der Baumeister','(Le Bâtisseur)','Bild und Wahrheit','(Image et Réalité)','Spiel- und Sucht','(Jeu - et Fringale)',"Le ``Maître''"]:
    assert a in plain,a
assert r'\unsure{Méditation' not in plain and r'\unsure{plus}' not in plain
assert '\\begin{tikzcd}' not in plain # the return uses a text layout with its explicit ruling/graphics
r['structural_validation']={'status':'passed','scope':'source-only; no compilation or rendering','balanced_braces':True,'balanced_environments':True,'balanced_inline_dollar_delimiters':True,'macros_within_preamble_and_standard_tools':True,'crop_files_exist':True,'H_rows_absent':True,'source_doubt_rows_mapped':13,'source_doubt_local_subloci':14,'resolved_original_doubts':8,'retained_original_doubts':6,'decision_rows':len(r['differences']),'actual_C_change_groups':len(groups),'inventory_items':len(r['inventory']),'crop_files':len(r['crops']),'cancellation_approximation_path_counts':pathcounts,'edge_path_groups':10,'reading_tex_sha256':hashlib.sha256(t.encode()).hexdigest()}
r['end_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(R/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
(R/'validation.json').write_text(json.dumps(r['structural_validation'],ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'passed','end_utc':r['end_utc'],'decision_rows':len(r['differences']),'actual_C_change_groups':len(groups),'inventory_items':len(r['inventory']),'crops':len(r['crops'])}))
