from pathlib import Path
import tempfile,shutil,subprocess
base=Path("research_e106").resolve();gp=Path("research_e52/vendor/pari-2.19.0/gp").resolve()
with tempfile.TemporaryDirectory(prefix="e106_",dir=base) as td:
 t=Path(td)
 for p in (base/"inputs").glob("*.bin"):shutil.copy2(p,t/p.name)
 r=subprocess.run([str(gp),"-q",str(base/"code/e_next_prime_maps.gp")],cwd=t,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 (base/"code/e_next_prime_maps.out").write_text(r.stdout)
 print(r.returncode,r.stdout[-1500:])
