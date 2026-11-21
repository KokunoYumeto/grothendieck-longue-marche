"""Assemble source-grounded reports; no OCR or LaTeX compilation."""
from pathlib import Path
from collections import Counter
import csv, json, re, sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
PREFIX = 'SP84_C13_149'

def tsv(path, fields, rows, delimiter='\t'):
    with path.open('w', newline='') as f:
        w=csv.DictWriter(f, fieldnames=fields, delimiter=delimiter, extrasaction='ignore')
        w.writeheader(); w.writerows(rows)

def cell(v):
    if isinstance(v,(dict,list)): v=json.dumps(v,ensure_ascii=False)
    return str(v if v is not None else '').replace('|','&#124;').replace('\n','<br>')

def table(fields, rows):
    return '| '+' | '.join(fields)+' |\n| '+' | '.join('---' for _ in fields)+' |\n'+''.join('| '+' | '.join(cell(r.get(k,'')) for k in fields)+' |\n' for r in rows)

def report_paths():
    return [p for p in sorted((ROOT/'reviews').glob('149_scan*.json')) if json.loads(p.read_text()).get('root_approved')]

def neutral_kind(kind):
    """Do not leak a proposed reading to the independent image-only reader."""
    k=kind.lower()
    if 'diagram' in k:return 'diagram'
    if 'delet' in k or 'struck' in k or 'cancel' in k:return 'struck passage with context'
    if 'insert' in k:return 'insertion with context'
    if 'margin' in k or 'diagonal' in k:return 'marginal note'
    if any(w in k for w in ('formula','math','display','arrow','map','relation')):return 'mathematical expression with context'
    if any(w in k for w in ('number','numeral','folio','digit','zero')):return 'handwritten number with context'
    return 'prose with context'

def notation_introduction(reports):
    """Describe actual audit status without claiming a pending audit is done."""
    expected=set(range(5,28))
    done={r['scan'] for r in reports if r.get('audited')}
    pending=sorted(expected-done)
    status=('All 23 pages have completed the independent image-only audit. '
            if not pending else
            'Independent audits remain pending for scans '+', '.join(f'{n:03d}' for n in pending)+'. ')
    return ('# Notation table\n\nThis table records notation from the current authoritative page reports. '
            +status+'The actual completion records are preserved in progress.log. '
            'Cross-page comparison outcomes are documented in documentation/notation_review.md. '
            'Differences of handwriting, distinct alphabets and local uncertainty are not silently regularized. '
            'A literal headless shaft remains a dash. Abbreviations, quotation marks and small raised strokes were read locally.\n\n')

def build():
    reports=[json.loads(p.read_text()) for p in report_paths()]
    notation_intro=notation_introduction(reports)
    notation_rows=[]
    for r in reports:
        for v in r.get('notation',[]):
            notation_rows.append({'scan':f"{r['scan']:03d}",'written form':v['written'],'rendering':v['rendering'],'meaning / evidence':v['meaning']+'; '+v['evidence']})
    (ROOT/'notation_current.md').write_text(notation_intro+table(['scan','written form','rendering','meaning / evidence'],notation_rows))
    counts=[]; all_changes=[]; collation=[]; decisions=[]; inv=[]; doubts=[]; hand=[]; abbrev=[]; checks=[]
    changes_body=[]; notes=['# Reading notes — SP84_C13_149\n\nThe manuscript is the source. Page summaries report its claims; they do not certify those claims. Only the actual mathematical checks listed in CHECK_EVENTS.tsv are claimed as checks. No external texts were consulted.\n\nThe supplied method identifies EXTRA STRONG as a possible paper watermark; no such pale or reversed paper marks were treated as manuscript text in this run. A positive watermark reading was not established from these scans.\n']
    for r in reports:
        n=r['scan']; changes=[c for c in r.get('changes',[]) if c.get('against_C') or c.get('against_H')]
        counts.append({'scan':f'{n:03d}','against C':sum(bool(c.get('against_C')) for c in changes),'against H':sum(bool(c.get('against_H')) for c in changes),'high':sum(c['confidence']=='high' for c in changes),'medium':sum(c['confidence']=='medium' for c in changes),'low':sum(c['confidence']=='low' for c in changes),'places':len(changes)})
        display=[]
        for c in changes:
            c=dict(c,scan=n);all_changes.append(c)
            crop=c.get('crop','page');box=c.get('box',[])
            ev=c['evidence']+(f' Crop: `{crop}`; original pixels {tuple(box)}.' if crop!='page' else '')
            if c.get('audit_first') is not None:
                ev+=f" Independent audit: first `{c['audit_first']}`; second `{c.get('audit_second','')}`."
            display.append({'place':c['place'],'C':c.get('C',''),'H':c.get('H',''),'final':c['final'],'scan evidence':ev,'confidence':c['confidence']})
            if c.get('against_H'):
                collation.append({'folder':'149','their_page':n-1,'our_scan':n,'line':c['place'],'their_reading':c.get('H',''),'codex_reading':c.get('C',''),'final_reading':c['final'],'scan_shows':ev,'kind':c['kind'],'marked_in_H':'yes' if c.get('marked_in_H') else 'no','confidence':c['confidence']})
        changes_body.append(f'\n## Scan {n:03d}\n\n'+table(['place','C','H','final','scan evidence','confidence'],display))
        audit_path=ROOT/f'second/149_scan{n:03d}_adjudications.tsv'
        if audit_path.exists():
            with audit_path.open() as stream:
                audit_rows=list(csv.DictReader(stream,delimiter='\t'))
            changed_audit=[]
            for a in audit_rows:
                if a.get('changed')!='yes':continue
                changed_audit.append({'box':a['box'],'first reading':a['first_reading'],
                    'independent reading':a['second_reading'],'final reading':a['final_reading'],
                    'scan evidence':a['evidence']+' Crop: `'+a['crop']+'`'+
                        ('; original pixels '+a['pixel_box'] if a.get('pixel_box') else '')})
            changes_body.append('\n### Changes after the independent reading\n\n'+
                (table(['box','first reading','independent reading','final reading','scan evidence'],changed_audit)
                 if changed_audit else 'No reading was changed by the independent comparison.\n'))
            changes_body.append('\nAll token differences, including retained readings and differences of representation, are recorded in `second/149_scan'+f'{n:03d}'+'_adjudications.tsv`. Certainty-only changes in this audit table are not added to the substantive witness counts.\n')
        unresolved=r.get('doubts',[])
        changes_body.append('\nUnresolved: '+('; '.join(f"{x['place']}: `{x['reading']}`" for x in unresolved) if unresolved else 'none identified.')+'\n')
        for d in r.get('decisions',[]):
            crop=d.get('crop','page');box=d.get('box',[])
            decisions.append({'id':d['id'],'cote':'149','scan':n,'decision':d['decision'],'reading':d['reading'],'what the ink shows':d['evidence'],'crop':crop+(f' {tuple(box)}' if crop!='page' else ''),'confidence':d['confidence']})
        inv.extend(r.get('inventory',[]))
        doubts.extend(dict(x,scan=f'{n:03d}') for x in unresolved)
        hand.extend(r.get('hand',[]));abbrev.extend(dict(x,scan=f'{n:03d}') for x in r.get('abbreviations',[]));checks.extend(r.get('checks',[]))
        note=r.get('notes','')
        if isinstance(note,list):note='\n\n'.join(map(str,note))
        notes.append(f'\n## Scan {n:03d}\n\n{note}\n')
    total={'scan':'TOTAL'}
    for k in ['against C','against H','high','medium','low','places']:total[k]=sum(x[k] for x in counts)
    header='# Changes — SP84_C13_149\n\nCounts are distinct substantive places, not token counts. A place may differ from both witnesses. The against-C and against-H counts compare the adopted readings, not macro syntax or certainty alone. A new or narrowed uncertainty with no change of adopted reading is documented in the doubts file and review records rather than counted here. A compound formula is one place where its interacting marks are decided together. Decisions about the original doubt marks also appear in decisions.tsv.\n\n'
    header+=table(['scan','against C','against H','high','medium','low','places'],counts+[total])
    math=[c for c in all_changes if c.get('mathematical')]
    header+='\n## Consequential readings\n\n'+('\n'.join(f"- Scan {c['scan']:03d}, {c['place']}: `{c['final']}` — {c['evidence']}" for c in math) or 'No mathematical correction identified in pages finalized so far.')+'\n'
    (ROOT/f'{PREFIX}_changes.md').write_text(header+''.join(changes_body))
    tsv(ROOT/f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
    mark_order={r['id']:i for i,r in enumerate(csv.DictReader((BASE/'source/SP84_C13_149_texts/MARKS.tsv').open(),delimiter='\t'))}
    decisions.sort(key=lambda d:mark_order[d['id']])
    tsv(ROOT/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decisions)
    tsv(ROOT/f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv,',')
    (ROOT/f'{PREFIX}_notes.md').write_text(''.join(notes))
    tsv(ROOT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks)
    doubt_text='# Notation, doubts and abbreviations — SP84_C13_149\n\n'+(ROOT/'notation_current.md').read_text()
    doubt_text+='\n## Remaining doubts\n\n'+table(['scan','place','reading','alternatives','confidence','reason'],doubts)
    # One entry per observed abbreviated spelling and proposed expansion.
    grouped={}
    for a in abbrev:
        key=(a['form'],a['expansion']);grouped.setdefault(key,[]).append(a['scan']+': '+a.get('place',''))
    ar=[{'form':k[0],'proposed expansion':k[1],'places':'; '.join(v)} for k,v in grouped.items()]
    doubt_text+='\n## Abbreviations\n\nExpansions here are explanatory proposals only; the transcription retains the written forms.\n\n'+table(['form','proposed expansion','places'],ar)
    leg=ROOT/'legibility_note.md'
    doubt_text+='\n## Legibility and limits\n\n'+(leg.read_text() if leg.exists() else 'Assessment in progress; see each remaining doubt and the page-specific crop evidence. No claim of a human-verified edition is made.\n')
    (ROOT/f'{PREFIX}_doubts.md').write_text(doubt_text)
    hand_text='# Hand log — SP84_C13_149\n\nEarlier observations from scans 003–004 were treated as hypotheses; the rows below record only observations on this run’s scans. Local similarities are not licenses to normalize clear counterexamples.\n\n'
    hand_text+=table(['habit','pages','consistency','misread'],hand)
    (ROOT/f'{PREFIX}_hand_log.md').write_text(hand_text)
    cats=['Symbols and indices','Words','Omissions','Drawings and diagrams','Readable ink left as illegible','Insertions put in the wrong place','Struck text','Abbreviations expanded, spelling modernised','Text that is not on the page','Other']
    ctr=Counter(c.get('error_category','Other') for c in all_changes)
    feedback='# Error-sheet feedback — SP84_C13_149\n\nCounts classify recorded substantive places by their primary error-sheet category; a place is counted once, even if it has secondary features. They are not an estimate of errors per token or a count of all examples inspected.\n\n'
    feedback+=table(['kind','places','locations'],[{'kind':cat,'places':ctr[cat],'locations':'; '.join(f"{c['scan']:03d}/{c['id']}" for c in all_changes if c.get('error_category','Other')==cat)} for cat in cats])
    extra=ROOT/'feedback_addendum.md'
    if extra.exists():feedback+='\n'+extra.read_text()
    (ROOT/f'{PREFIX}_sheet_feedback.md').write_text(feedback)
    combined='\\cotefile{149}\n\n'+'\n'.join((ROOT/f"pages/149_scan{r['scan']:03d}.tex").read_text().rstrip()+'\n' for r in reports)
    (ROOT/f'{PREFIX}_transcription.tex').write_text(combined)
    print(json.dumps({'pages':len(reports),'changes':len(all_changes),'against_C':total['against C'],'against_H':total['against H'],'decisions':len(decisions),'inventory':len(inv),'doubts':len(doubts)},ensure_ascii=False))

def approve(n):
    p=ROOT/f'reviews/149_scan{n:03d}.json';r=json.loads(p.read_text())
    required=[m['id'] for m in csv.DictReader((BASE/'source/SP84_C13_149_texts/MARKS.tsv').open(),delimiter='\t') if int(m['scan'])==n]
    assert [d['id'] for d in r['decisions']]==required,(required,r['decisions'])
    for c in r.get('changes',[]):
        assert c['confidence'] in ('high','medium','low')
        assert (ROOT/c['crop']).is_file(),c
    for d in r['decisions']:
        if d['decision']!='undecided':assert d.get('crop')!='page' and (ROOT/d['crop']).is_file(),d
    assert r.get('root_reviewed_crops') is not None,'Record root crop review before approval.'
    assert all(c['crop'] in r['root_reviewed_crops'] for c in r.get('changes',[]))
    src=ROOT/f'reviews/149_scan{n:03d}.tex';dest=ROOT/f'pages/149_scan{n:03d}.tex'
    if not dest.exists():dest.write_bytes(src.read_bytes())
    assert f'\\scanpage{{{n}}}' in dest.read_text()
    r['root_approved']=True;p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    # Freeze initial audit box readings before the independent reader sees only boxes.
    boxes=r.get('audit_boxes',[])
    tsv(ROOT/f'second/149_scan{n:03d}_boxes.tsv',['box','kind','x0','y0','x1','y1'],[dict(b,kind=neutral_kind(b['kind'])) for b in boxes])
    tsv(ROOT/f'second/149_scan{n:03d}_first.tsv',['box','reading'],boxes)
    build()
    from datetime import datetime,timezone
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    crops=set(r['root_reviewed_crops'])
    substantive=sum(bool(c.get('against_C') or c.get('against_H')) for c in r.get('changes',[]))
    with (ROOT/'progress.log').open('a') as f:f.write(f"scan {n:03d} done {now} cote 149: {r['lines_read']} lines read, {len(crops)} places cropped, {substantive} rows\n")

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='approve':approve(int(sys.argv[2]))
    else:build()
