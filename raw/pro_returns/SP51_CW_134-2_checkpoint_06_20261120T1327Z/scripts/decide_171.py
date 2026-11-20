from decision_helpers import *
import copy
r=load_reports(171)
diffs=[]
for i in [0,2,3,5,6,7,8,9,10,11]:
 d=row(r,'C',i)
 if i==0:d['crop']='crops/scan171/main/01_quotes.jpg';d['evidence']='Paired high short strokes open and close the phrase; neither pair forms angular guillemets.'
 if i==5:d['crop']='crops/scan171/A/L08_pas.png'
 if i==11:d['crop']='crops/scan171/main/02_separator.jpg';d['evidence']='Three separate horizontal pen strokes descend in decreasing length and shift right. All three are reproduced; H’s note calls them a double trait and supplies no drawing.'
 diffs.append(d)
diffs.insert(5,row(r,'B',5))
diffs.extend([row(r,'B',12),row(r,'B',13)])
comparisons=[
 {'place':'L4–5 high mark before hyperrecouvrements','A':"single apostrophe: de 'hyperrecouvrements",'B':r"de \unsure{'|''}hyperrecouvrements",'C':"single apostrophe: de 'hyperrecouvrements",'decision':'One vertical high stroke, with broken ink along its height, rather than two adjacent strokes. Select the single apostrophe (C/l04_articles_and_high_stroke.png). Keep the low e before it: no contraction is supplied.'},
 {'place':'L9 punctuation after schéma','A':'schéma. Pour','B':'schéma, Pour','C':'schéma. Pour','decision':'Select B’s comma. The dark detached head has a down-left tail (B/l09_schema_punctuation.png); a following capital is not grounds to make it a period.'},
 {'place':'L18 point between X and closing parenthesis','A':'X).','B':r'X\unsure{.}).','C':'X).','decision':'Select A/C. The tiny stipple is aligned with and nearly contiguous to the lower-right terminal of X, not securely a separate punctuation mark. The full stop after the parenthesis is distinct (B/l18_final_punctuation.png).'},
 {'place':'Right margin between L21 and L22','A':'separate short stroke','B':'separate short stroke','C':'not separately inventoried','decision':'Include the continuous dark upward-right stroke, distinct from the lower line-end hyphen (B/l22_margin_stroke.png). Its hand and function are not certain.'},
 {'place':'Below/right of final qu’en','A':'nontext isolated point, origin uncertain','B':'nontext isolated point, origin uncertain','C':r'qu’en\unsure{.}','decision':'Reproduce the compact dark point as a nontext margin mark, without assigning sentence punctuation (B/l23_final_mark.png). It is distinct from pale grain but could be pen ink or reproduction debris; its origin remains unresolved.'},
 {'place':'L4 name joining stroke and L7 sentence dash','A':'short -; H -- flagged','B':'short -; no difference row','C':'short -; H -- flagged','decision':'Keep the short strokes in the transcription (main/03_name_dash.jpg and main/04_sentence_dash.jpg). Exclude these from counts and H collation: both encodings denote the same single handwritten horizontal punctuation stroke, with no difference in wording or number of marks.'}
]
review=[
 {'place':'L4 before nerfs','earlier':r'\unsure{de nerfs de|des nerfs de|de nerfs des|des nerfs des}','decision':'resolved: first de','evidence':'C/l04_articles_and_high_stroke.png: d and low e, no further s before n.'},
 {'place':'L4 after nerfs','earlier':'same four-way phrase doubt','decision':'resolved: second de','evidence':'Same contiguous phrase crop: d followed by a low e exit before the raised mark.'},
 {'place':'L4–5 before hyperrecouvrements','earlier':r"\unsure{'|''}",'decision':'resolved: one apostrophe','evidence':'One high vertical stroke; see three-reader decision.'},
 {'place':'L9 sur','earlier':r'\unsure{sur|sûr}','decision':'resolved: sur','evidence':'C/l09_sur_accent.png: no continuous circumflex above u.'},
 {'place':'L13 before pi_1','earlier':r'\unsure{du|des}','decision':'retained: du|des','evidence':'C/l13_article_pi1.png: compressed post-d cup and flat exit do not separate u from es.'},
 {'place':'L13 category capital','earlier':r'\unsure{\mathcal E|E}_n','decision':'retained: calligraphic/ordinary E','evidence':'C/l13_category_capital.png: looped E and clear low n, typographic alphabet not uniquely determined.'},
 {'place':'L14 before ind-structure','earlier':r'\unsure{la|le}','decision':'retained, preference reordered: le|la','evidence':'C/l14_article_ind.png: small terminal closed bowl has no decisive a stem; all three readers prefer le, while la remains possible.'}
]
unresolved=copy.deepcopy(r['C']['unresolved'][:3])
unresolved.append({'place':'Below/right of final qu’en','reading':'isolated nontext point','alternatives':['incidental pen ink','reproduction debris'],'confidence':'low','reason':'The compact dark point is physically distinct, but its origin and function cannot be established. It is drawn, not assigned sentence punctuation.'})
notes='''**S171-notes.** The continuation supposes that X is “localement homotopiquement trivial” and says that its Artin-Mazur pro-simplicial object is then essentially constant in the ordinary homotopy category. It says this is not the case for the étale topos of a scheme, proposes a pro-n-groupoid fundamental object and an ind-n-category, and relates the ind structure to local triviality under increasingly fine coverings. After the separator, the writer acknowledges resistance to retaining only the homotopy type of a topos. The paragraph ends in the unfinished “je suis persuadé qu’en”.

The author’s phrases “ceci de supposer que X est”, “doit être conçu comme un”, and “je suis persuadé qu’en” mark a supposition, a proposed formulation, and a conviction. No proof, computation or independent theorem check was attempted on this page. Mathematical context prompted inspection of the negative **pas**, the pro/ind distinction, π₁ and E_n; it did not decide their ink. The apparent rule under n in pro-n-groupoïde is the returning descender of g, while pro itself has two independent rules. The category alphabet and two compressed articles remain doubtful.

This is author page **26**, archive pencil **171**, a letter continuation without date, title, salutation, signature or total-page statement. Three horizontal strokes precede the indented second paragraph. A separate short right-margin stroke is reproduced. The isolated point below/right of the unfinished final word is drawn without assigning punctuation or certain origin. The heavy retracing of final en and the opening parenthesis before ind-structure does not establish a separately readable deletion.'''
viewed=['C/l04_articles_and_high_stroke.png','C/l09_sur_accent.png','B/l09_schema_punctuation.png','C/l11_pro_n_underlines.png','C/l13_article_pi1.png','C/l13_category_capital.png','C/l14_article_ind.png','B/l18_final_punctuation.png','B/l22_margin_stroke.png','B/l23_final_mark.png','A/L08_pas.png','main/01_quotes.jpg','main/02_separator.jpg','main/03_name_dash.jpg','main/04_sentence_dash.jpg']
write_decision(171,'A',[('schéma. Pour','schéma, Pour')],diffs,comparisons,unresolved,r['B']['inventory'],notes,[],review,['crops/scan171/'+p for p in viewed],workflow_note='All three independently read 23 lines. Main reused 11 reader crops and made 4 new crops. Three crop images requested together before context compaction were not displayed because the output was truncated; those existing files were displayed once successfully afterward, with no new crops. Packet extraction was corrected to include C notes spanning the page boundary, and the same page-relevant addition was sent to all three readers. Short-dash encoding differences were excluded as equivalent readings; punctuation tails and the role of isolated points required adjudication.')
add_notation([
 ('Fundamental group index',r'$\pi_1$','Scan 171 L13: low 1 is clear.'),
 ('pro-n-groupoïde emphasis',r'\uuline{pro}-$n$-groupoïde','Scan 171 L11: two rules under pro; apparent line under n is g’s returning descender.'),
 ('ind prefix',r'$(\mathrm{ind})$-$n$-catégorie','Scan 171 L14: parentheses belong to ind prefix; following article remains le|la.'),
 ('Raised mark before hyperrecouvrements',"de 'hyperrecouvrements",'Scan 171 L4–5: low e followed by a single raised vertical stroke; unusual spelling preserved.'),
 ('Unaccented sur','sur','Scan 171 L9: no circumflex visible; do not generalize absence to other occurrences.')
])
brief=(ROOT/'briefs/brief_v02_scan171.md').read_text().replace('Reader brief v02 — first used on scan 171','Reader brief v03 — first used on scan 172')
brief+='''\n## Clarifications introduced after scan 171\n\n- A physically separate short stroke is distinct from an ordinary line-end hyphen. Locate each before adding it to the inventory. Reproduce a coherent nontext stroke without inventing its function. Do not promote faint copy grain to manuscript ink. A compact isolated point may remain of uncertain origin; if reproduced, distinguish that physical mark from an inferred sentence full stop, and record the uncertainty.\n- A change from one TeX hyphen to two is not itself a collation difference when both represent the same single handwritten punctuation stroke. Report any actual difference in number, placement or reading of marks; keep mere typesetting choices out of counts.\n- Crop views must actually be visible. If an image result is truncated or fails to display, document the failure and display the same saved crop successfully; do not make a replacement crop or claim the failed display was an inspection.\n'''
(ROOT/'briefs/brief_v03_scan172.md').write_text(brief)
with (ROOT/'records/brief_changes.md').open('a') as f:f.write('\n## v02 → v03, first used on scan 172\n\nScan 171 exposed different treatment of a terminal point, a missed independent margin stroke, and short-dash encoding rows. The brief now distinguishes a physical nontext mark from an inferred linguistic function, warns against copy-grain overinterpretation, and excludes dash encodings when the underlying reading is identical. It also requires honest recording of a failed image display and reuse of the existing crop.\n')
print('171 decision saved')
