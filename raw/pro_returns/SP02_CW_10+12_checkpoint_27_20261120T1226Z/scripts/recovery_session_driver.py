import sys,termios,json,io,contextlib,traceback
cfg=termios.tcgetattr(sys.stdin)
cfg[3]&=~(termios.ECHO|termios.ICANON)
termios.tcsetattr(sys.stdin,termios.TCSANOW,cfg)
ns={}
print('READY',flush=True)
for line in sys.stdin:
 out=io.StringIO()
 try:
  req=json.loads(line)
  with contextlib.redirect_stdout(out): exec(req['code'],ns)
  result={'ok':True,'stdout':out.getvalue()}
 except BaseException as exc: result={'ok':False,'error':str(exc),'traceback':traceback.format_exc()}
 print(json.dumps(result,ensure_ascii=False),flush=True)