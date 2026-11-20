from pathlib import Path
import json,datetime,re
root=Path('/workspace/scratch/4770596940a0');out=root/'out/readers/R3'
p=out/'scan032.json';r=json.loads(p.read_text())
sup=json.loads((out/'scan032_supplement_start.json').read_text());crop=sup['crop'];crop['viewed']=True
texpath=out/'scan032.tex';tex=texpath.read_text()
old=r"A\in F\setminus G'\subset F'"
new=r"""A\in F\mathbin{\underset{\text{\begin{tikzpicture}[x=.25cm,y=.25cm]
\draw[line width=.45pt,line cap=round,line join=round] (.18,.43) -- (0,.05) -- (.15,.02);
\draw[line width=.45pt,line cap=round,line join=round] (.30,.60) .. controls (.36,.40) and (.26,.18) .. (.10,.04);
\end{tikzpicture}}}{\setminus}}G'\subset F'"""
assert tex.count(old)==1
tex=tex.replace(old,new,1)
tex=tex.replace('% @ upper part, two cases; both first-case G primes are visible','% @ upper part, two cases; both first-case G primes are visible\n% Supplemental recheck: separate two-stroke hooked/arrow-like mark is drawn beneath the set-difference slash. Its function is unresolved.')
texpath.write_text(tex)
row={'id':'D52','place':'first-case formula, immediately below the set-difference slash, approximately x1420,y315','C':'no lower mark','H':'no lower mark','reading':'Separate two-stroke hooked/downward-left-arrow-like mark preserved in TikZ beneath the slash; no definite textual or mathematical role assigned.','ink':'Left short stroke slopes down-left to a low heavy foot; right stroke begins higher and curves down-left into the same low region. A white gap separates both from the thick set-difference slash above. The high prime after G is a different mark.','confidence':'medium','existence_confidence':'high','identity_confidence':'low','kind':'drawing or diagram','crop':'complement_submark','against_C':True,'against_H':True,'marked_in_H':False,'supplement':'S01'}
assert not any(d['id']=='D52' for d in r['differences'])
r['differences'].append(row)
r['inventory'].append({'id':'I45','kind':'unidentified drawing','position':'below the set-difference slash in first-case A∈F\\G′⊂F′','first_words_or_objects':'two-stroke hooked/downward-left-arrow-like mark','crop':'complement_submark','included_in_tex':True,'supplement':'S01'})
r['crops'].append(crop)
r['images_viewed'].append({'sequence':len(r['images_viewed'])+1,'path':crop['path'],'role':'supplemental enlarged source crop','crop_id':crop['id']})
r['remaining_doubts'].append({'difference_id':'D52','place':row['place'],'reading':'Identity and function of lower hooked/arrow-like mark unresolved; strokes preserved.','confidence':'low'})
r['notation'].append({'symbol':'small mark below first-case set-difference slash','reading':'nonverbal two-stroke drawing; identity/function unresolved','evidence':'Supplement S01 crop shows a separate lower mark, with no contact to slash and no target text.'})
r['notes_while_reading'].append('Supplement S01: a small separate hooked/arrow-like mark below the first-case set-difference slash had been missed in the first inventory. It is now preserved graphically. No mathematical assertion about its function is made, and no new mathematical check was performed.')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
r.setdefault('supplements',[]).append({'id':'S01','scope':'scan032 only; below first-case complement slash','start_utc':sup['start_utc'],'end_utc':now,'difference_ids':['D52'],'inventory_ids':['I45'],'crop_ids':['complement_submark'],'original_report_end_utc_preserved':r['end_utc'],'other_readings_consulted':False,'new_math_check_events':[]})
# Structural checks on the augmented proposed text.
s='\n'.join(line.split('%',1)[0] for line in tex.splitlines());bal=0
for ch in s:
 if ch=='{':bal+=1
 elif ch=='}':bal-=1
 assert bal>=0
assert bal==0
stack=[]
for typ,env in re.findall(r'\\(begin|end)\{([^}]+)\}',s):
 if typ=='begin':stack.append(env)
 else:assert stack and stack.pop()==env
assert not stack and s.count('$')%2==0 and s.count(r'\[')==s.count(r'\]')==5
r['validation'].update({'difference_count':len(r['differences']),'inventory_count':len(r['inventory']),'crop_count':len(r['crops']),'supplement_validation':'S01 passed balanced braces/environments/math delimiters; lower mark exists in proposed TEX and inventory; original D01–D51 and original end_utc preserved. No compilation.'})
p.write_text(json.dumps(r,ensure_ascii=False,indent=2))
cp=out/'scan032_crops.json';cr=json.loads(cp.read_text());cr.append(crop);cp.write_text(json.dumps(cr,ensure_ascii=False,indent=2))
print(json.dumps({'supplement':'S01','end_utc':now,'differences':len(r['differences']),'inventory':len(r['inventory']),'crops':len(r['crops']),'validation':'passed'},indent=2))
