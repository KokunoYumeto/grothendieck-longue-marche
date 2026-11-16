import json
L = json.load(open('layout_c5.json')); types = L['types']; edges = L['edges']
# colour language shared by every picture: arrow families in three groups
FAM = {  # family: (colour, group)
 'f_B_s': '#ffb000', 'f_Q_a': '#ff7a00', 'gamma_pp_pi_s': '#ff4d6d', 'gamma_pi_s': '#ffd23f', 'gamma_r_0': '#ff8fab',
 'gamma_r_2prime': '#f15bb5', 'tau_pi_s': '#06d6a0', 'tau_r_0': '#2ec4b6', 'tau_pi_rho': '#4cc9f0', 'tau_r_1': '#4895ef',
 'gamma_pi_rho': '#b5179e', 'gamma_r_1': '#9b5de5', 'gamma_r_1prime': '#7209b7', 'gamma_r_2': '#c77dff'}
TC = {'I10': '#ffd23f', 'I6': '#ff6b6b', 'I4': '#4ecdc4', 'II2': '#e0aaff', 'IIp2': '#c77dff', 'II1': '#9d4edd',
      'III2': '#caf0f8', 'III1': '#90e0ef', 'IIIp2': '#48cae4'}
SZ = {'I10': 0.30, 'I6': 0.24, 'I4': 0.20}
with open('out/cote148_hairball.dot', 'w') as f:
    f.write('graph G {\n bgcolor="#0b0d17"; outputorder=edgesfirst; overlap=prism; splines=false;\n')
    f.write(' node [shape=circle, style=filled, label="", penwidth=0];\n edge [penwidth=0.7];\n')
    for i, t in enumerate(types):
        f.write(f' n{i} [fillcolor="{TC[t]}", width={SZ.get(t, 0.10 if t.startswith("III") else 0.14)}];\n')
    for fam, s, t in edges:
        f.write(f' n{s} -- n{t} [color="{FAM[fam]}b0"];\n')
    f.write('}\n')
json.dump({'FAM': FAM, 'TC': TC}, open('tools/palette.json', 'w'))
