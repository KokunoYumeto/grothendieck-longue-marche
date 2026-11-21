# Difference-table parsing incident

The supplied C/H difference TSV has853 physical data rows, each with exactly5 literal tab-separated fields. It is not CSV-quoted data. The original preparation used default CSV quote handling; a leading quotation mark at the end of scan129 caused its final parsed field to absorb the40 rows of scan130 and29 rows of scan131. Reader_c reported the trailing rows on opening its129 packet and ignored them. No foreign page image or full witness page was consulted by that reader.

The preparation now uses QUOTE_NONE for this input only, while the emitted packet TSV remains properly CSV-quoted. Packets129–131 were regenerated and verified at45,40,29 rows respectively. Reader_c is excluded from blind130 and131; this is enforced by prepare_second.py and validate.py. If the original three readers had been reused, their eligible blind readers would have been b and a respectively. Instead, the blind phase uses three fresh reader contexts, blind_a, blind_b and blind_c, with no first-pass material; the exposure exclusions remain recorded and enforced.

The audit of all earlier parsing found one additional same-page merge on124, joining adjacent rows about the S label and the dashed D-bang connection. No other cross-page absorption occurred. Both124 subjects had already been examined in its diagram195 crop, discussed in its report and placed in its complete second-reading diagram box; no further settled-place crop was made. Its difference packet was repaired to33 rows.

This records an accidental first-pass packet-boundary violation and its mitigation. The final independent readings remain subject to different-reader and witness-exposure exclusions.
