"""Root comparison: all eleven differing readings inspected; no text change."""
from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];p='151_scan045';dec={}
def d(b,e):dec[b]={'decision':'retain first','changed':'no','evidence':e}
d('b01','The dark authorial 10 is at the head, distinct from pale lower foliation. Formalisme has the f descender and l/isme sequence, and the half sign is plainly present between it and simplicial. The omitted half is restored by retaining the first text.')
d('b02','Both marks are retained in the existing à/colon doubt. The compact lower body cannot be narrowed to a certain colon.')
d('b03','The ending has t, dotted i, crossed/slanted s-z-like stroke, accented e and final s; no descending q supports faisceautique. Faisceautisés remains, with its unmatched opening quote.')
d('b04','The final word has initial s, a low u, dotted i, tall t and reduced e, supporting suite. The high vertical stroke in the crop is separate from that low sequence. La remains before suite; fait/point do not match the lower word.')
d('b05','The low initial a/m is followed by an accented e and n/e/r/a sequence. Arrive lacks the visible accent and does not account for those humps. The leader puts alors after amènera.')
d('b06','The connected word has n/o/r/m, an a loop and tall l followed by e; it is normale. There is no separate un or second word boundary before the low m/a/l/e sequence. Des has a final return.')
d('b07','The old crossed group remains wholly doubtful. The separated dot supports i; the apparent low x is inseparable from the cancellation path. There is no independently recoverable X_x alternative.')
d('b08','The second X has both upper and lower heavy serif-like retracing. Its upper horizontal touches the diagonals and is not a separate overbar. Retain a live X_i without inventing an old layer.')
d('b10','Every letter, comma, index, inequality, subset and the double-shaft implication agrees. Only display delimiters differ.')
d('b11','The second coordinate has a separate dot and a retraced small lower body. The existing doubtful i preserves that ambiguity; an epsilon is not independently established as a distinct letter beneath the retracing. The whole coproduct/set formula is retained.')
d('b13','The lower verb starts with a reversed-curved s then e/r/o/n and a final tall t, reading seront. The t/i/s-é/s ending of faisceautisés excludes faisceautique. The first reading already includes the upper continuation tions and physical stratifica-/tion break.')
(W/'audit'/f'{p}_adjudication.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
r=json.loads((W/'reports'/f'{p}.json').read_text());r['second_changes']=[];r['notes'].append('scan045.N11: All eleven token differences in the blind reading were inspected on their saved crops. The first reading stands, including the half sign in the heading, amènera with raised alors, normale, seront and faisceautisés. The old indexed group and the retraced pair coordinate retain their existing doubts; no new deletion or overbar is inferred from retracing.');(W/'reports'/f'{p}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
