from pathlib import Path
p=Path(__file__).resolve().parent/'build_reading.py';s=p.read_text()
anchor="F=lambda n:fragments['B026-'+n]"
new=r'''# Complete fixed-origin groups keep nearby marks at their observed vertical positions.
graphic('B026-GMAIN',(440,1222,613,1318),[],[(475,1297,'$'+fragments['B026-S09']+'$'),(440,1315,fragments['B026-M03'])],reading='main barred Sigma with the separate pale arc to its left',candidates=['barred Sigma and independent pale arc; arc character, role, hand and surface origin unresolved'],crop='08_barred_formulas',role='complete source-coordinate group; S09 and M03 occur once',baseline=1297)
graphic('B026-GROOF10',(1095,1169,1248,1240),[],[(1095,1234,'$'+fragments['B026-S10']+'$'),(1169,1190,fragments['B026-M02'])],reading='first parenthetical barred Sigma and small detached trace below its roof',candidates=['barred Sigma; trace attached to alpha','barred Sigma; trace attached to closure rule','barred Sigma; independent trace'],crop='08_barred_formulas',role='complete source-coordinate group; S10 and M02 occur once',baseline=1234)
graphic('B026-GPEUT',(655,1345,750,1438),[],[(660,1390,'peut'),(714,1424,fragments['B026-M04'])],reading='peut with three separate flecks below it',candidates=['peut; flecks with unestablished role, attachment, hand and surface origin'],crop='09_parenthesis_end',role='word-bearing group owns peut exactly once and positions M04 below it',baseline=1390)
graphic('B026-CAPFINAL',(744,2286,795,2334),[path([(19,20),(28,7),(42,18)],.45)],[(744,2329,fragments['B026-M06'])],reading='first final-row intersection arch and the separate low-left slant',candidates=['intersection arch with detached continuation','intersection arch with independent low-left slant'],crop='16_final_row',role='complete relation/mark group; M06 remains individually qualified and occurs once',baseline=2310)
F=lambda n:fragments['B026-'+n]'''
assert anchor in s;s=s.replace(anchor,new)
a="F('M03')+F('S09')";assert a in s;s=s.replace(a,"F('GMAIN')")
a="F('S10')+F('M02')";assert a in s;s=s.replace(a,"F('GROOF10')")
a="F('S13')+r'''$ ne peut\n'''+F('M04')+r''' être "
b="F('S13')+r'''$ ne '''+F('GPEUT')+r''' être "
assert a in s;s=s.replace(a,b)
a="F('S34')+r'''\\cap'''+F('M06')+F('S35')";b="F('S34')+F('CAPFINAL')+F('S35')";assert a in s;s=s.replace(a,b)
p.write_text(s)
