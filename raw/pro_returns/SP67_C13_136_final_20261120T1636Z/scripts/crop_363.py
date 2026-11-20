from workflow import *
boxes=dict(Sym_sub=(513,180,572,229),Li_sub=(789,539,833,589),vertical_relation=(804,601,849,653),Sym_close=(862,644,970,751),axioms=(773,1181,946,1284),G_exp=(1269,1281,1494,1351),underbrace=(790,1834,943,1958),up_arrow=(702,1689,764,1780),cancel_diagram=(1120,1636,1666,1988),cancel_word=(1036,1855,1144,1907),cancel_range=(420,2143,640,2202))
log('scan 363 open places after whole and overlapping halves: '+', '.join(boxes)+'; one bounded crop per open place.')
for k,b in boxes.items():crop(363,k,b)
