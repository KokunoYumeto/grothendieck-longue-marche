import sys
sys.path.insert(0,'/workspace/scratch/0ad792daea27/MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
for n in (177,179):
    p=page(33,n);t=p.read_text();t=t.replace(r'\mathbf{S}',r'\unsure{\mathbf{S}|\mathbb{S}}').replace(r'\mathbf{H}',r'\unsure{\mathbf{H}|\mathbb{H}}');p.write_text(t)
audit(33,179,'Both rotated halves read against the text. The literal KJ=Kf and later KL=Kf are retained, along with u in the theorem versus b in the preceding criterion. Cross-page comparison with 177 shows uneven filled versus hollow overprinted S/H; filled-looking instances on both pages now carry an explicit bold/double-struck alphabet doubt, while clearly hollow forms remain double-struck. No missing rho has been supplied.')
