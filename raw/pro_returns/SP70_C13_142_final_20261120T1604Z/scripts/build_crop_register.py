#!/usr/bin/env python3
"""Build a crop-provenance register without opening or reading any image.

Existing CHANGES/decisions entries supply coordinates. Filename associations
marked inferred_from_label are bookkeeping inferences from crop names and
logged places, not original tool-command receipts. Reader-confirmed recovery
and exact-pixel recovery are separately identified. Top/bottom/left/right
halves are excluded. Unknown crop coordinates remain blank; never guessed.

Usage: python3 scripts/build_crop_register.py --views ../views --through 48
Re-run as pages are completed; new unmapped crop names will be flagged.
"""
from pathlib import Path
import argparse,csv,json,re
from collections import defaultdict

# Source pointer syntax: changes/decision ID, with optional zero-based box index.
# These filename associations were inferred from names and logged place labels.
ASSOCIATIONS = {
'026_NB.png':('026-14',0),'026_dans.png':('026-04',0),'026_diagram14.png':('026-07',0),
'026_formula14.png':('026-05',0),'026_formula16.png':('M0006',0),'026_formula19.png':('026-15',0),
'026_margin.png':('026-08',0),'026_word_group.png':('026-01',0),
'027_alpha24.png':('027-16',0),'027_cancel24.png':('027-17',0),'027_deleted.png':('027-04',0),
'027_formula25.png':('027-18',0),'027_marginal.png':('027-14',0),
'028_diagram.png':('028-20',0),'028_marginal.png':('028-19',0),'028_sphere.png':('028-12',0),'028_topwords.png':('028-02',0),
'029_NB.png':('029-03',0),'029_cancelled.png':('029-07',0),'029_exponent.png':('029-25',0),'029_lowerNB.png':('029-21',0),
'030_bottomnote.png':('030-19',1),'030_initialP.png':('030-04',0),
'030_les.png':('030-26',0),'030_note.png':('030-02',0),'030_poles.png':('030-08',0),
'031_ainsi.png':('031-18',0),'031_cancelled.png':('031-11',0),'031_dindex.png':('M0041',0),
'031_finalwords.png':('031-20',0),'031_leftnote.png':('031-01',0),'031_poles.png':('031-07',0),
'031_rightnote.png':('031-02',0),'031_sigma.png':('031-14',0),
'033_cancellations51.png':('033-17',0),'033_entre.png':('033-15',0),'033_hom.png':('033-07',0),
'033_omega49.png':('033-12',0),'033_pi.png':('033-13',0),'033_torseur.png':('033-04',0),
'034_cancelled.png':('034-22',0),'034_de.png':('M0052',0),'034_groupnote.png':('034-14',0),'034_psi54.png':('034-06',0),
'035_deletedblock.png':('035-13',0),'035_est.png':('035-02',0),'035_formula59.png':('035-21',0),
'035_norm.png':('035-01',0),'035_phi57.png':('035-11',0),'035_resume.png':('035-16',0),
'036_cancelledlines.png':('036-18',0),'036_rho60.png':('036-07',0),'036_se.png':('036-17',0),
'037_avant.png':('037-18',0),'037_cancelledalpha.png':('037-13',0),'037_leftnote.png':('037-01',0),
'037_paren64.png':('037-20',0),'037_rho63.png':('037-08',0),'037_rightnote.png':('037-09',0),'037_triangle.png':('037-22',0),
'038_la.png':('038-26',0),'038_pas.png':('038-24',0),'038_pole.png':('038-05',0),
'038_same_deleted.png':('038-10',0),'038_sigma67.png':('038-03',0),'038_sphereVII.png':('038-12',0),'038_verticalsign.png':('038-16',0),
'039_arrow68.png':('039-05',0),'039_equationword.png':('039-14',0),'039_rho70.png':('039-16',0),'039_word70prime.png':('039-19',0),
'040_beta75.png':('040-16',0),'040_cancellations73.png':('040-12',0),'040_first72.png':('040-06',0),
'040_margin72.png':('M0090',0),'040_reference75.png':('040-17',0),
'041_alpha75prime.png':('041-06',0),'041_cancelledblock.png':('041-08',0),'041_deces.png':('041-05',0),
'041_finalnumber.png':('041-19',0),'041_qualifier.png':('041-15',0),
'042_avec.png':('042-01',0),'042_deletedending.png':('042-07',0),
'044_also.png':('044-09',0),'044_cancelgroup.png':('044-10',0),'044_category.png':('044-17',0),
'044_neq.png':('044-14',0),'044_quiestrature.png':('044-15',0),'044_scalar.png':('044-19',0),
'044_spaces.png':('044-23',0),'044_stokes.png':('044-24',0),'044_tousrature.png':('044-16',0),
'044_vquotient.png':('044-21',0),'044_warning.png':('044-01',0),
'045_margin.png':('045-08',0),'045_ordinal.png':('045-01',0),'045_prenant.png':('045-06',0),'045_sont.png':('045-04',0),
'046_desdits.png':('046-05',0),'046_index10.png':('046-01',0),
'047_bottomnote.png':('047-12',0),'047_cancelA.png':('047-07',0),'047_cancelP.png':('047-02',0),
'047_minus3.png':('047-05',0),'047_obtenu.png':('047-04',0),'047_topnote.png':('047-01',0),
'048_deleted15.png':('048-06',0),'048_deleteddes.png':('048-05',0),'048_dt.png':('048-04',0),
'048_firstdiagram.png':('048-02',0),'048_margin.png':('048-12',0),'048_terminal.png':('048-10',0),
}
# Exact values recovered by the root reader from preserved command history.
READER_RECOVERED = {
'028_audit_roman.png':(1490,1240,1660,1410),
'045_un.png':(290,1245,690,1330),
'047_identified.png':(1290,650,1555,745),
'049_articles.png':(275,275,650,375),'049_partant.png':(905,575,1535,680),
'049_le.png':(600,1385,680,1475),'049_cette.png':(1430,1450,1615,1550),
'050_ring0.png':(110,580,380,835),'050_ring1.png':(680,600,905,815),
'050_ringinf.png':(340,450,590,655),'050_topP.png':(515,125,590,205),
'050_cancelled16.png':(1060,300,1215,385),'050_definition.png':(1075,635,1660,785),
'050_margin19.png':(20,1050,720,1660),'050_boundarysentence.png':(315,1115,1070,1260),
'050_nb.png':(20,1640,335,1985),'050_orientation.png':(310,1740,1630,1950),
'050_cancelledblock.png':(330,1930,1640,2345),
'051_margintop.png':(15,180,940,610),'051_rep.png':(15,600,395,1045),
'051_number20.png':(315,85,420,180),'051_dispose.png':(1050,70,1310,150),
'051_arcs.png':(1090,390,1210,445),'051_deduit.png':(1460,670,1640,740),
'051_destination.png':(820,1010,935,1115),'051_explicite.png':(955,1195,1310,1290),
'051_dec24.png':(1350,1250,1665,1455),'051_decbody.png':(770,1640,1295,1765),
'051_formula27.png':(175,1990,950,2125),'051_margin27.png':(20,2105,345,2335),
}
READER_ROTATIONS={'051_margintop.png':-32,'051_rep.png':-40}
READER_CONFIRMED_NAMES = {'045_prenant.png','047_minus3.png'}
BOX_RE=re.compile(r'\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)')
FIELDS=['scan','crop_file','x0','y0','x1','y1','rotation_degrees','coordinate_status','filename_association','source_documentation','recorded_crop','notes']


def crop_boxes(value):
    matches=list(BOX_RE.finditer(value))
    result=[]
    for i,match in enumerate(matches):
        box=tuple(map(int,match.groups()))
        trailer=value[match.end():matches[i+1].start() if i+1<len(matches) else len(value)]
        rotation=re.search(r'(?:rotated|rotation)\s*([−-]?\d+(?:\.\d+)?)',trailer)
        angle=rotation.group(1).replace('−','-') if rotation else ''
        result.append((box,angle))
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work',type=Path,default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--views',type=Path)
    parser.add_argument('--through',type=int)
    parser.add_argument('--check',action='store_true',help='Check current register without changing it')
    args=parser.parse_args();work=args.work.resolve();views=(args.views or work.parent/'views').resolve()
    done=[int(n) for n in re.findall(r'(?m)^scan (\d+) done ',(work/'progress.log').read_text())]
    covered=set(n for n in done if args.through is None or n<=args.through)
    names=sorted(p.name for p in views.glob('*.png') if re.match(r'^\d{3}_',p.name) and int(p.name[:3]) in covered and p.stem.split('_',1)[1] not in {'top','bottom','left','right'})
    records={};refs=defaultdict(list)
    for filename in ('CHANGES.tsv','decisions.tsv'):
        with (work/filename).open(newline='',encoding='utf-8') as handle:
            for row in csv.DictReader(handle,delimiter='\t'):
                records[row['id']]={'filename':filename,**row}
                for box,_ in crop_boxes(row['crop']):refs[(int(row['scan']),box)].append(f"{filename}:{row['id']}")
    # Supplementary exact-pixel recovery is a numerical certificate, not a reading decision.
    pixel_records={}
    certificate=work/'CROP_PIXEL_RECOVERY.tsv'
    if certificate.exists():
        with certificate.open(newline='',encoding='utf-8') as handle:
            pixel_records={r['crop_file']:r for r in csv.DictReader(handle,delimiter='\t')}
    rows=[];issues=[]
    for name in names:
        scan=int(name[:3]);row=dict.fromkeys(FIELDS,'');row.update(scan=f'{scan:03d}',crop_file=name)
        if name in pixel_records and pixel_records[name].get('status')=='exact_pixel_match':
            record=pixel_records[name];row.update({k:record[k] for k in ('x0','y0','x1','y1','rotation_degrees')})
            row.update(coordinate_status='recovered_exact_pixels' if name not in ASSOCIATIONS and name not in READER_RECOVERED else 'documented_pixel_verified',
                       filename_association='exact_pixel_match',source_documentation=record.get('source_documentation','')+'; CROP_PIXEL_RECOVERY.tsv; scripts/verify_crop_pixels.py',
                       recorded_crop=f"{scan:03d} ({', '.join(str(row[k]) for k in ('x0','y0','x1','y1'))})",
                       notes='Filename/rectangle association verified by exact decoded-RGB equality after reconstructing crop.py; no text recognition or visual reading.')
        elif name in ASSOCIATIONS:
            pointer,index=ASSOCIATIONS[name]
            if pointer not in records or len(crop_boxes(records[pointer]['crop']))<=index:
                issues.append(f'{name}: source coordinate pointer unavailable: {pointer}[{index}]')
                row.update(coordinate_status='unknown',filename_association='not_established',notes='Source pointer missing or changed; no coordinate guessed.')
            else:
                record=records[pointer];box,angle=crop_boxes(record['crop'])[index]
                row.update(zip(('x0','y0','x1','y1'),box))
                sources=list(refs[(scan,box)])
                status='reader_confirmed' if name in READER_CONFIRMED_NAMES else 'inferred_from_label'
                if status=='reader_confirmed':sources.append('CROP_COORDINATE_RECOVERY.md')
                row.update(rotation_degrees=angle if angle else ('0' if status=='reader_confirmed' else ''),coordinate_status='documented',filename_association=status,
                           source_documentation='; '.join(sources),recorded_crop=record['crop'],
                           notes='Coordinate is copied from the cited record. Filename association is inferred from its label and logged place, not proved by a saved crop command.' if status=='inferred_from_label' else 'Filename/coordinate association confirmed by root reader from preserved run summary.')
        elif name in READER_RECOVERED:
            box=READER_RECOVERED[name];row.update(zip(('x0','y0','x1','y1'),box))
            original_refs=refs[(scan,box)]
            row.update(rotation_degrees=str(READER_ROTATIONS.get(name,0)),coordinate_status='documented' if original_refs else 'reader_recovered_command',filename_association='reader_confirmed',source_documentation='; '.join(original_refs+['CROP_COORDINATE_RECOVERY.md']),
                       recorded_crop=f"{scan:03d} ({', '.join(map(str,box))})",notes='Filename/rectangle confirmed by the root reader from exact command coordinates. '+('Corroborating original record references are listed.' if original_refs else 'No coordinate in the original changes/decision rows.')+' No reading outcome inferred here.')
        else:
            issues.append(f'{name}: coordinate not recovered')
            row.update(coordinate_status='unknown',filename_association='not_established',notes='Image filename exists; no supported coordinate association recovered. Coordinates deliberately left blank.')
        rows.append(row)
    output=work/'CROPS.tsv'
    if args.check:
        if not output.exists():issues.append('CROPS.tsv missing')
        else:
            with output.open(newline='',encoding='utf-8') as handle:
                current=list(csv.DictReader(handle,delimiter='\t'))
            expected=[{k:str(v) for k,v in row.items()} for row in rows]
            if current!=expected:issues.append('CROPS.tsv differs from current source-derived register; rebuild required.')
    else:
        with output.open('w',newline='',encoding='utf-8') as handle:
            writer=csv.DictWriter(handle,fieldnames=FIELDS,delimiter='\t');writer.writeheader();writer.writerows(rows)
    print(json.dumps({'status':'PASS' if not issues else 'ISSUES','covered_scans':[f'{n:03d}' for n in sorted(covered)],'crop_files':len(names),
                      'known_coordinates':sum(r['coordinate_status']!='unknown' for r in rows),'unknown_coordinates':sum(r['coordinate_status']=='unknown' for r in rows),'issues':issues},indent=2))
    return bool(issues)

if __name__=='__main__':raise SystemExit(main())
