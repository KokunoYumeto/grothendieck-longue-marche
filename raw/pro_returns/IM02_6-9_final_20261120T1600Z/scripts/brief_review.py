#!/usr/bin/env python3
import sys,json
from review import inspect,source_rows,pagename
for page in sys.argv[1:]:
    report,original,edited=inspect(page)
    src={r['id']:r for r in source_rows() if pagename(r)==page}
    print('\nPAGE',page)
    for row in report['rows']:
        r={k:row.get(k) for k in ['id','decision','find','replace','what_the_ink_shows','confidence','note','unsettled']}
        r['source_as_read']=src[row['id']]['as_the_page_reads'];r['source_should_read']=src[row['id']]['should_read'];r['source_kind']=src[row['id']]['kind'];r['source']=src[row['id']]['source']
        print(json.dumps(r,ensure_ascii=False))
    print('CROPS',json.dumps(report.get('crops',[])))
    print('OPEN',json.dumps(report.get('open_questions',[])))
