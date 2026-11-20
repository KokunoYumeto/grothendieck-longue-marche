from audit_amend import *
t=(WORK/'pages/16_scan016.tex').read_text()
old=r'\inserted{et les $\boldsymbol\pi_i$ en les $\pi_i$ \deleted{$\unsure{\pi_i}$} (donc $\pi_i\in\mathcal E$)}'
new=r'\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node at (0,.6) {et les $\boldsymbol\pi_i$ en les $\pi_i$ \deleted{$\unsure{\pi_i}$}};\node at (2,-.2) {(donc $\pi_i\in\mathcal E$)};\draw (-3.5,-.55) .. controls (-3.6,.05) and (-3.35,.2) .. (-2.7,.23) .. controls (-.6,.23) and (2.4,.25) .. (3.6,.23);\end{tikzpicture}}}'
assert old in t;t=t.replace(old,new)
# The first inventory already separately records this long leader as element 5.
amend('16','016',t,[change('top projector insertion leader','words inserted but leader not drawn','baseline words; no drawn leader','inserted two-line reading with long attachment leader','A long light stroke runs beneath the added projector words, turns downward at their left attachment, and passes above the lower parenthetical donc phrase.','drawing or diagram',c=True)])
