from workflow import *
boxes=dict(these=(1111,82,1220,157),initial_cancel=(296,250,353,311),cancel_two=(365,336,1097,564),cancel_trial=(330,583,842,704),E_Phi=(735,765,976,950),Lambda_exp=(937,1517,1027,1598),r_left=(265,1620,460,1702),r_right=(791,1674,949,1778),box_end=(1229,1683,1277,1790))
log('scan 362 open places after whole and overlapping halves: '+', '.join(boxes)+'; one bounded crop per open place.')
for k,b in boxes.items():crop(362,k,b)
