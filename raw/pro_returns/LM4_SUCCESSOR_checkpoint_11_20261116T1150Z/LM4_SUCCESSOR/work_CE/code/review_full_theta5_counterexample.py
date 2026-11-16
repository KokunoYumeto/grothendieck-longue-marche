"""Independent rerun of the full theta5 certificate, output redirected to CE."""
from pathlib import Path
p=Path(__file__).resolve().parents[2]/'work_DE/next_joint_rigid_symplectic/refute_full_theta5.py'
s=p.read_text()
s=s.replace("(HERE/'full_theta5_noninjection_certificate.json')",'Path('+repr(str(Path(__file__).resolve().parents[1]/'full_theta5_independent_certificate.json'))+')')
exec(compile(s,str(p),'exec'),{'__file__':str(p),'__name__':'_CE_full_theta5_review'})
