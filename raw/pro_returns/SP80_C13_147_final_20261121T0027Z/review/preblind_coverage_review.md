# Main-reader review of fixed-box coverage

All 23 first readings were committed before the blind phase. The structural
screen is recorded in `preblind_coverage_screen.json`; it is not an image
recognition procedure and does not establish geometric coverage by itself.

The exact-argument candidates were inspected against the box records:

- Scan112: B08 has the whole cancelled formula; `quad` versus `qquad` alone
  causes the string comparison to flag it.
- Scan116: B02 covers the written174, and B03 the tall brace and adjacent
  doubtful curve. The full margin argument is split across those two boxes.
- Scan119: B04–B05 cover the first cancelled sentence; B06–B08 cover the next
  sentence and its entire mathematical line. No words are omitted by the split.
- Scan127: B19–B20 cover the two cancelled margin passages; B21 and B27 cover
  the cancelled prose; B22–B24 cover the boxed mathematical expression, its
  number and the adjacent condition. The candidates result from those splits.
- Scan130: B25 and B26 were added before the baseline freeze to cover the
  complete multiline displays210 and211, in addition to the detail boxes.

The only earlier numeric-token candidate on130 was the `4` in the typesetting
spacing command `hspace{4cm}`, not missing manuscript ink. The added complete
display box includes this encoding as well. No numeric candidates remain.
All reviewed notes have explicit links to check-event records.

First readings and box lists are immutable after
`second/first_readings_frozen.json` is created. Later changes belong only in
the final page, reviewed record and explicit blind adjudications; the first
and second TSVs remain evidence of what each reader wrote before comparison.
