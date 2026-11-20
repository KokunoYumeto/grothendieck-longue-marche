from audit import *
t=begin(26)
t=t.replace(r'\unsure{\widetilde{\mathfrak S}_J|G_J}',r'\mathcal G_J')
for identifier in ['026-02','026-03']:
    amend(identifier,final=r'\mathcal G_J',scan_shows='Second visual reading: the open lower coil and internal horizontal stroke are the same G form as the clear instances on scan 051. The upper flourish belongs to G, not an independent tilde.',confidence='high',against_C='no',against_H='yes',consequential='G_J is the acting group; the earlier provisional tilde-S reading is withdrawn.')
r.hand('audit: acting group resolved','Both G_J occurrences on scan 026 have the same open lower curve and internal bar as the clear later forms, especially scan 051. The earlier provisional tilde-S alternative is withdrawn. The cancelled ξ-like annotation above (19) remains uncertain and is not automatically changed to the later parameter ζ.')
finish(t,'The entire page was reread, including the sphere, both path rows, the marginal sketch, cancellation states and every prime in (19). Both provisional group-symbol readings are resolved as G_J. The cancellation above the last formula remains explicitly doubtful; the later ζ notation does not determine that cancelled sign.')
