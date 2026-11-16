import sys, json, datetime
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from search_context import search,ROOT
queries = {
"D01":"faisceaux de Weil|foncteurs de Weil|quasi.sch|flasque|finite surjective|finite covers",
"D02":"extension du corps|changement de base|base.change|corps algébriquement clos",
"D03":"Greenberg|Néron|limites inductives|inductive limits",
"D04":"injective|adjunction|adjoint|injectifs",
"D05":"acycli|spectral sequence|suite spectrale|Hom.*inject",
"D06":"acycli|spectral sequence|suite spectrale|Ext.*Hom",
"D07":"cohomological dimension|dim.*coh|galoisi|Galois|perfect closure",
"D08":"Cartier|G_a|affine|affines|unipot",
"D09":"Pontryagin|Pontrjagin|Frobenius|Lang|dualité de Serre",
"D10":"Tate|dualit|duality|biextension|accouplement",
"D11":"shift|décal|Ext|Ext.*i-1|degr",
"D12":"bidual|completion|complété|pi_1|Tate module",
"D13":"extension|splitting|product|produit|unipot",
"D14":"Kummer|tensor|otimes.*mathbb Q|transition",
"D16":"support|Matlis|local duality|local cohomology",
"D17":"complét|completion|inverse limit|varprojlim",
"D18":"Matlis|injective hull|local duality|Ext",
"D19":"fid.*plat|faithful.*flat|Weil|catégorie abélienne",
"D20":"trace|bifonctor|functorial|Hom|pushforward",
"D21":"Cartier|abelian|abélien|affine|torsion",
"D22":"Cartier|twist|shift|décal|mu_n",
"D23":"shift|décal|idélique|adélique|complexe",
"D24":"hens|support|local duality|Ext",
"D25":"premier.*p|prime.to|Kummer|mu_n",
"D26":"locali[sz]ation|triangle|support|compatib",
"D27":"long exact|suite exacte|boundary|connecting|compatib",
"D28":"extension.*zero|extension.*zéro|support|local cohomology|i_!",
"D29":"extension.*zero|extension.*zéro|support|local cohomology|i_!",
"R01":"James|intrinsic join|Thom|S-homotopy|Spanier",
"R02":"Stiefel|J\\\\\\(|S-reducible|cross.section|finite order",
"R03":"Atiyah|James|Thom|Hirzebruch",
"R04":"composantes connexes|geometric.*connect|universellement ouvert|universally open",
"R05":"multiplicité|multiplicit|plat|flat|length",
"R06":"multiplicité|multiplicit|plat|flat|length",
"R07":"Chow|cohérent|coherent|Leray|spectral",
"R08":"Cohen|Macaulay|équidimension|equidimension",
"R09":"1963|James|Bott|Grassm|morphismes plats",
"R10":"Euler|Hilbert|polynom|polynôm|leading coefficient",
"R11":"régulier|regular|dimension|profond|depth",
"R12":"fid.*plat|faithful.*flat|B.*otimes_A|descent",
"R13":"mou|soft sheaf|partition.*unit|faisceau|sheaf",
"R14":"fine sheaf|faisceau fin|extension|stalk",
"R15":"stalk|tensor|injective|injection"
}
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
records=[]
for note,pattern in queries.items():
 hits=search(pattern)
 records.append({'note':note,'utc':stamp,'scope':'all supplied context .md/.tex/.txt files; this script does not search PDF image data','pattern':pattern,'count':len(hits),'hits':hits})
 scans=sorted(set(f"{h['cote']}:{h['scan']}" for h in hits if h['cote']))
 print(note,len(hits),'CT',','.join(scans))
(ROOT/'records/research_root_note_searches.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records),encoding='utf-8')

