from workflow import *
updates={332:{'left curved connection and third object':{'H':'left brace (accolade) joining the two Gamma objects, with xi-to-gamma label','ink':'The connection is one bowed headless shaft without a brace cusp; the third Gamma object and its label are written beside it.'}},355:{'circle around erased node':{'H':'surrounding enclosure explicitly described','dh':False},'four lower connectors':{'H':'objects and connecting strokes described generically; four lower routes not specified'},'vertical paths above L-star':{'H':'connections to an overworked upper symbol described; long bypass and short descent not distinguished'}},358:{'large cancellation geometry':{'H':'the whole parenthesized block explicitly described as crossed by a large X','dh':False}}}
removals={350:{'first formula insertion'},359:{'cancelled upper-right trial'},362:{'deleted -i after star'}}
for n in sorted(set(updates)|set(removals)):
 p=ROOT/f'records/scan{n}.py';r=ast.literal_eval(p.read_text())
 for x in r['changes']:
  if x['place'] in updates.get(n,{}):x.update(updates[n][x['place']])
 r['changes']=[x for x in r['changes'] if x['place'] not in removals.get(n,set())]
 p.write_text(pprint.pformat(r,sort_dicts=False,width=120)+'\n')
log('final H-description review: credited H for355 enclosing oval and358 whole-block X cancellation; credited H for350 raised C*(U) insertion; removed certainty-only359 cancelled-expression and362 deleted-index rows already conveyed by H; clarified332 brace/curve and355 unspecified connector differences; no manuscript reading changed')
rebuild()
