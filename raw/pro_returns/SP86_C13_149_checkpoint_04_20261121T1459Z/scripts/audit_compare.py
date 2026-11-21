from pathlib import Path
import csv,re,json,difflib,sys,hashlib
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parents[1]

def reader_name(value):
 match=re.search(r'reader_[abc]',value)
 if not match:raise ValueError('Unknown reader identity: '+value)
 return match.group(0)

def utc_datetime(value):
 return datetime.fromisoformat(value.replace(' UTC','+00:00').replace('Z','+00:00')).astimezone(timezone.utc)

def read_tsv(path):
 with path.open() as f:return list(csv.DictReader(f,delimiter='\t'))
def tokens(s):
 # Token-by-token lexical comparison; spellings, primes, punctuation and case survive.
 return re.findall(r'\\[A-Za-z]+|\\.|[^\W\d_]+|\d+|[^\s]',s,re.UNICODE)
def compare(page):
 manifest=json.loads((BASE/'second'/'input_manifest.json').read_text())['pages'][page]
 for suffix in ['boxes','first']:
  actual=hashlib.sha256((BASE/'second'/f'{page}_{suffix}.tsv').read_bytes()).hexdigest()
  if actual!=manifest[suffix+'_sha256']:raise ValueError(f'{page}: frozen {suffix} changed')
 reader=json.loads((BASE/'second'/f'{page}_reader.json').read_text())
 if reader_name(reader['reader'])==reader_name(manifest['first_reader']):raise ValueError(f'{page}: reader previously read this page')
 if not reader.get('completed_utc'):raise ValueError(f'{page}: independent reading is not complete')
 a={x['box']:x['reading'] for x in read_tsv(BASE/'second'/f'{page}_first.tsv')}
 b={x['box']:x['reading'] for x in read_tsv(BASE/'second'/f'{page}_second.tsv')}
 if a.keys()!=b.keys():raise ValueError(f'{page}: missing/extra second boxes: {a.keys()-b.keys()}, {b.keys()-a.keys()}')
 rows=[]
 for box in a:
  ta,tb=tokens(a[box]),tokens(b[box]);ops=[]
  for tag,i,j,k,l in difflib.SequenceMatcher(None,ta,tb,autojunk=False).get_opcodes():
   if tag!='equal':ops.append({'operation':tag,'first_tokens':ta[i:j],'second_tokens':tb[k:l]})
  rows.append({'box':box,'first':a[box],'second':b[box],'different':'yes' if ops else 'no','token_differences':json.dumps(ops,ensure_ascii=False)})
 out=BASE/'second'/f'{page}_comparison.tsv'
 with out.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['box','first','second','different','token_differences'],delimiter='\t');w.writeheader();w.writerows(rows)
 meta={'compared_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'reader_completed_utc':reader['completed_utc'],'first_sha256':manifest['first_sha256'],'second_sha256':hashlib.sha256((BASE/'second'/f'{page}_second.tsv').read_bytes()).hexdigest()}
 (BASE/'second'/f'{page}_comparison.json').write_text(json.dumps(meta,indent=2)+'\n')
 return {'page':page,'boxes':len(rows),'differences':sum(x['different']=='yes' for x in rows)}
if __name__=='__main__':
 for p in sys.argv[1:]:print(json.dumps(compare(p)))
