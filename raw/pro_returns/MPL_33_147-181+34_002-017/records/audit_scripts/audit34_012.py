import sys
sys.path.insert(0,'/workspace/scratch/0ad792daea27/MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
revise(34,12,r'$\widetilde V\hookrightarrow\widetilde V\prime$',r'$\widetilde V\hookrightarrow\widetilde V\prime$') if False else None
revise(34,12,r"$\widetilde V\hookrightarrow\widetilde V'$",r"$\widetilde V\unsure{\hookrightarrow|\subset}\widetilde V'$")
revise(34,12,r"L'hom $\pi'_0\longrightarrow\pi_0$",r"L'hom $\pi'_0\unsure{-|\longrightarrow}\pi_0$")
audit(34,12,'Both halves checked object by object across all six diagrams. The surprising K-prime in the prose separable-closure sentence and the reversed denominators Gal(Kbar-prime/K), Gal(Kbar/K-prime) are visibly written and retained. The inclusion-shaped V-tilde connector is now marked hook-arrow/subset, and the pi0-prime connector in the prose prefers a headless dash. The plain connectors in (3.2)–(3.4), altered I-prime/P-prime, and lower-case-looking p in (3.7) remain represented without mathematical repair.')
