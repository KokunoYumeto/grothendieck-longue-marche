from pathlib import Path
import json
r=Path(__file__).resolve().parents[1];s=r/'second';n=105
comp=json.loads((s/'149_scan105_comparison.json').read_text());boxes={x['box']:x for x in json.loads((r/'review/accepted/149_scan105.json').read_text())['audit_boxes']}
evidence={
'b01':"The final n arch is followed by a distinct short terminal s bend before the comma. The plural d'extensions stands; the second reading's uncertainty does not overturn those strokes.",
'b02':"The dark authorial number consists of 5 and 2. The difference is only the page-number wrapper; 52 remains in the manuscript-page field.",
'b04':"The first word has initial r, accented e and v, with no initial p descender: révision. The still-open terminal word was inspected in audit_b04_ending: after the long low n return there is a separate descending s bend, then a detached stop. Retain notations.",
'b05':"The initial j descends below e; note is live. In the struck prefix the low closed d loop and following e survive, but an accent cannot be separated from the hatching. Add de as an alternative to dé. The cancelled group letter has two open lobes, supporting E rather than G, and subscript X.",
'b06':"The group letter has two open lobes; the next symbol has a flat cap and straight capital-height posts followed by a separate 1. Formula (1), E and Pi_1 remain; the added E/G alternative is not adopted.",
'b08':"Two open lobes support E; the full-height cap and two posts support Pi. Parenthesized tilde X, the semicolon, Aut_X and its argument match. Remaining differences are braces and a second-reader uncertainty not supported by a closed G body.",
'b09':"The word above begins with the double curve of s followed by o-u-v-e-n-t, not recouvrant. The curve before si rises into the equality insertion and is a leader, not an opening parenthesis. The upper X has the looping form of nearby X; a free tilde cannot be securely separated. Retain the X/tilde-X alternatives in their current order.",
'b10':"The full line visibly reads est une A-algèbre telle que Spec(tilde A)=tilde X. The two readings have the same words and indices; their difference is TeX bracing.",
'b11':"The small initial loop has a detached accent, hence à. The short isom group has no d ascender and is followed by a separate n-o-n group before unique. No stop is visible after isom. Retain à isom non unique.",
'b12':"The point sign has a short head and a long inflected stem. The same two alternatives are offered in opposite orders. Its identity remains unresolved; retain zeta/xi consistently pending cross-page notation review.",
'b14':"The complete formula retains the three group objects, Pi_1 and its comma, and the same unresolved point signs. The still-open last word was examined in audit_b14_abbreviation: after the tall forked r is a closed e loop and an open v return, not r-o after p. The terminal stroke is continuous with v, while a detached stop remains insecure. Retain rev/rev. rather than pro/pro-.",
'b15':"The line reads X pointé en, the recurring long inflected point sign, a separate stop, then Le choix. The sign is not newly settled by the second reader's reversed preference.",
'b16':"The thin foliation reads 104, with a closed 0 and angular final 4. It remains a margin number, distinct from the dark authorial 52. The wrapper difference changes no ink reading."
}
rows=[]
for c in comp:
 if not c['different']:continue
 b=c['box'];final=c['first'];changed=b=='b05'
 if changed: final=final.replace(r'\unsure{dé}',r'\unsure{dé|de}')
 row={'box':b,'root_visually_inspected':True,'final':final,'evidence':evidence[b],'crop':f'crops/149_scan105_second_{b}.png','bbox':boxes[b]['bbox'],'confidence':'medium' if b in ['b04','b05','b09','b12','b14','b15'] else 'high','changed':changed}
 if b=='b04':row['additional_evidence']=[{'crop':'crops/149_scan105_audit_b04_ending.png','bbox':[1120,190,1440,320]}]
 if b=='b14':row['additional_evidence']=[{'crop':'crops/149_scan105_audit_b14_abbreviation.png','bbox':[1430,2020,1680,2215]}]
 rows.append(row)
(s/'149_scan105_adjudications.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
data=json.loads((r/'review/accepted/149_scan105.json').read_text());old=next(x for x in data['changes'] if x['id']=='p03')
plan={'scan':105,'page_replacements':[{'old':r'\deleted{\unsure{dé}}note','new':r'\deleted{\unsure{dé|de}}note'}],'changes_updates':[{'id':'p03','patch':{'final':old['final'].replace(r'\unsure{dé}',r'\unsure{dé|de}'),'evidence':old['evidence']+' Independent audit: the accent cannot be distinguished from cancellation strokes; de is explicitly retained as an alternative to dé. This refines uncertainty, without another witness-error count.'}}],'doubts_updates':[{'place':'line 3, struck prefix before note','patch':{'reading':r'\deleted{\unsure{dé|de}}','alternatives':'dé; de. The d loop and e survive; the accent is not separable from cancellation strokes.','confidence':'low'}}],'inventory_updates':[{'element':'e05','patch':{'first_words_or_objects':'doubtful dé/de'}}],'notes_append':['Independent audit: all thirteen token-different boxes were adjudicated on their crops. Tight crops of the still-open notations ending and rev abbreviation confirmed the first lexical readings. The cancelled prefix now explicitly carries dé/de; no additional correction against either witness is counted for this uncertainty refinement.']}
(s/'149_scan105_update_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
