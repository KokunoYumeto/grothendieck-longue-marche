"""Render complete finite coefficient rank matrices as compact TeX tables."""
import csv,itertools
from pathlib import Path
from a_main_cubic_census import OUT,ROOT
DEST=ROOT/"deliverable/tables"
DEST.mkdir(exist_ok=True)

def main():
    for family,m in [("cubic",3),("quartic",4),("sextic",6)]:
        with (OUT/f"a_main_{family}_census.csv").open() as f:rows=list(csv.DictReader(f))
        assert len(rows)==(m**4 if m==3 else 2*m**4)
        ranks={}
        for row in rows:
            sign=1 if m==3 else int(row["sign"])
            key=(sign,)+tuple(int(row[f"e{p}"]) for p in (2,3,5,7))
            assert row["analytic_rank"] in ("0","1","2","3")
            ranks[key]=row["analytic_rank"]
        pre=["{",r"\scriptsize",r"\setlength{\tabcolsep}{2pt}"]
        align="rrr|"+"|".join(["r"*m]*m)
        pre.append(r"\begin{longtable}{"+align+"}")
        pre.append(r"\caption{Complete certified "+family+r" analytic ranks; rows give $(\varepsilon,e_2,e_3)$ and columns give $(e_5,e_7)$.}\\")
        pre.append(r"\toprule")
        pre.append(r"$\varepsilon$&$e_2$&$e_3$&"+
             "&".join(r"\multicolumn{"+str(m)+r"}{c}{$e_5="+str(i)+r"$}" for i in range(m))+r"\\")
        pre.append("&&&"+"&".join(str(j) for i in range(m) for j in range(m))+r"\\")
        pre.append(r"\midrule")
        pre.append(r"\endfirsthead")
        pre.append(r"\toprule")
        pre.append(r"$\varepsilon$&$e_2$&$e_3$&"+
             "&".join(r"\multicolumn{"+str(m)+r"}{c}{$e_5="+str(i)+r"$}" for i in range(m))+r"\\")
        pre.append("&&&"+"&".join(str(j) for i in range(m) for j in range(m))+r"\\")
        pre.append(r"\midrule")
        pre.append(r"\endhead")
        pre.append(r"\bottomrule\endfoot")
        for sign in ((1,) if m==3 else (1,-1)):
            for e2,e3 in itertools.product(range(m),repeat=2):
                values=[ranks[(sign,e2,e3,e5,e7)] for e5,e7 in itertools.product(range(m),repeat=2)]
                pre.append(("+1" if sign==1 else "-1")+f"&{e2}&{e3}&"+"&".join(values)+r"\\")
        pre.extend([r"\end{longtable}","}"])
        (DEST/f"a_main_{family}_ranks.tex").write_text("\n".join(pre)+"\n")
        print(family,len(rows),"ranks written")
if __name__=="__main__":main()
