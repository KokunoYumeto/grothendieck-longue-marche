"""Download published primary-source copies for the proof audit."""
import urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
root=Path('work/primary');root.mkdir(exist_ok=True,parents=True)
urls={
'a_mazur1977.pdf':'https://www.numdam.org/item/PMIHES_1977__47__33_0.pdf',
'a_kisin2009.dvi':'https://people.math.harvard.edu/~kisin/dvifiles/serre2.dvi',
'a_serre1972.pdf':'https://wstein.org/sage_summer/bsd_comp/Serre-properties_galoisiennes_des_points_dordre_fini_des_courbes_elliptiques.pdf',
'a_rubin_kolyvagin.pdf':'https://wstein.org/edu/Fall2003/252/references/rubin-kolyvagin/Rubin-The_work_of_Kolyvagin_on_the_arithmetic_of_elliptic_curves.pdf',
}
def get(item):
 name,url=item
 try:
  with urllib.request.urlopen(url,timeout=12) as r:
   data=r.read()
  (root/name).write_bytes(data)
  return name,len(data)
 except Exception as e:return name,type(e).__name__,str(e)
with ThreadPoolExecutor(max_workers=4) as pool:
 for result in pool.map(get,urls.items()):print(result,flush=True)
