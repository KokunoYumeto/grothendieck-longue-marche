"""Exact based comparison for the staged full nine-strand certificate.

The output retains the actual standard-chart path G, the reference-to-
source path T, and the endpoint offset whiskers H.  The geometric source
producer proves the two-parameter offset homotopy is collision free on
every segment.  This producer checks all endpoint projection orders and
certifies the additional five-segment original-label chart path.
"""

from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import hashlib
import json

import full_cross_source_geometry_stage as st

C, nf, gr = st.C, st.nf, st.gr


def configuration_values(configuration, endpoint):
    return [gr.peval(n,Q(endpoint))*gr.cinv(gr.peval(d,Q(endpoint)))
            for n,d in configuration]


def endpoint_check(values, label):
    rows = []
    for i,j in combinations(range(9),2):
        original = (gr.PROJECTION*(values[i]-values[j])).re
        shifted = original+st.PROJECTION_OFFSET*(i*i-j*j)
        assert original.sign() != 0
        assert original.sign() == shifted.sign(), (label,i,j)
        rows.append({"pair":[i,j], "original_projected_difference":original.encoded(),
                     "shifted_projected_difference":shifted.encoded(),
                     "common_sign":original.sign()})
    return {"label":label, "values":[v.encoded() for v in values],
            "endpoint_whisker_offsets":[(gr.cinv(gr.PROJECTION)*(st.PROJECTION_OFFSET*i*i)).encoded()
                                         for i in range(9)],
            "pairwise_order_checks":rows}


def main():
    producer=Path(__file__).resolve()
    folder=producer.with_name("full_cross_source_stage")
    folder.mkdir(exist_ok=True)
    # Labels are 0,1,v_1,v_zeta,v_zeta2,v_zeta3,v_zeta4,p,n.
    # Their standard projection order is 0,1,v_zeta,v_1,v_zeta2,v_zeta3,v_zeta4,p,n.
    standard=[C(0),C(1),C(3),C(2),C(4),C(5),C(6),
              st.POSITIVE_REFERENCE,st.NEGATIVE_REFERENCE]
    target=st.fixed_points()+[st.POSITIVE_REFERENCE,st.NEGATIVE_REFERENCE]
    state=standard[:]
    chart_configs=[]
    chart_segments=[]
    for label in range(2,7):
        configuration=[([value],[C(1)]) for value in state]
        configuration[label]=([state[label],target[label]-state[label]],[C(1)])
        chart_configs.append(configuration)
        chart_segments.append(st.segment(configuration,f"standard_chart_label_{label}"))
        state[label]=target[label]
    assert state==target
    chart_word=nf.red([letter for segment in chart_segments for letter in segment["braid"]])
    assert chart_segments[0]["initial_order"]==[0,1,3,2,4,5,6,7,8]
    raw_configs=[(f"chart_{i}",c) for i,c in enumerate(chart_configs)]
    raw_configs += [(f"reference_{i}",c) for i,c in enumerate(st.transport_configurations())]
    for label,center in zip(st.RAW,st.CENTERS):
        corner=center+C(st.HALF,st.HALF)
        route=[st.BASE,corner,center+C(-st.HALF,st.HALF),
               center+C(-st.HALF,-st.HALF),center+C(st.HALF,-st.HALF),corner]
        raw_configs += [(f"{label[0]}_{i}",st.configurations(a,b))
                        for i,(a,b) in enumerate(zip(route,route[1:]))]
    endpoint_count=0
    for label,configuration in raw_configs:
        for endpoint in (0,1):
            endpoint_check(configuration_values(configuration,endpoint),f"{label}_{endpoint}")
            endpoint_count+=1
    paths={"standard":endpoint_check(standard,"H_standard"),
           "reference":endpoint_check(target,"H_reference"),
           "source":endpoint_check(configuration_values(st.configurations(st.BASE,st.BASE),0),"H_source")}
    record={"status":"PASS_BASED_STAGE_PENDING_INDEPENDENT_AUDIT",
            "producer_sha256":hashlib.sha256(producer.read_bytes()).hexdigest(),
            "chart_path_segments":chart_segments,"chart_path_braid":chart_word,
            "standard_order":chart_segments[0]["initial_order"],
            "reference_order":chart_segments[-1]["final_order"],
            "endpoint_configurations_checked":endpoint_count,
            "endpoint_pairwise_sign_comparisons":36*endpoint_count,
            "explicit_endpoint_whiskers":paths,
            "based_identity":"G*T*gamma_original*T^-1*G^-1 is homotopic to H_standard*(G_offset*T_offset*gamma_offset*T_offset^-1*G_offset^-1)*H_standard^-1. Every endpoint H has zero projected crossings, and its coordinate-wise linear formula is retained. The original-basepoint source transport is the F20 polygon eta; Xi=G*T*phi(eta)^-1 carries these words back to the original F19 groups."}
    output=folder/"basepath_comparison.json"
    output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":record["status"],"chart_forward_segments":len(chart_segments),
                      "chart_crossings":sum(s["crossing_count"] for s in chart_segments),
                      "chart_braid_length":len(chart_word),
                      "endpoint_configurations_checked":endpoint_count,
                      "endpoint_pairwise_sign_comparisons":36*endpoint_count,
                      "output_sha256":hashlib.sha256(output.read_bytes()).hexdigest()},indent=2))


if __name__=="__main__":main()
