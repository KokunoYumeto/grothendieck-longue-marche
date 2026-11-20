from record import *
p=ROOT/'pages/J71-06_71_scan044.tex'
t=p.read_text(); assert t.count('autrement')==1
p.write_text(t.replace('autrement',r'autre\textsuperscript{.}\\ment'))
change(44,'044-C08','last word, division after autre','autrement','no source text',r'autre\textsuperscript{.}\\ment','Second reading. A discrete solid raised dot follows the e of autre at the right edge; ment resumes on the next line. Both the dot and the division are retained, without assigning a syntactic function. Scan 44 crop (1465,2150,1648,2256).',c=True,kind='omission')
hand('A raised dot can accompany a word division','44, final autre [raised dot] / ment','One observed occurrence; no general substitution of dots for hyphens is inferred.','C joins autrement and drops the visible dot; 044-C08.')
with (ROOT/'SP60_CW_71_notes.md').open('a') as f:f.write('\n### Second-reading addition — scan 44\n\nThe last word is divided after `autre`, with a separate raised dot before `ment` resumes on the next line. The dot is retained without interpreting its purpose; 044-C08.\n')
with (ROOT/'progress.log').open('a') as f:f.write('scan 044 audited '+utc()+' — complete second reading against whole image; one new crop restores the raised dot in the final divided word, 044-C08.\n')
render()
