# First-pass crop coordinate recovery — reader_b

Recovered at 2026-11-21 15:10:09 UTC.

## 149_scan011_c17.png

The exact original rectangle is `(970, 777, 1660, 898)`, in original-image pixel coordinates `(x0, y0, x1, y1)`.

Evidence is the preserved first-reader builder `documentation/first_reader_working_files/write_reader_b_011.py`, line 41, whose literal assignment is:

```python
boxes['c17']=[970,777,1660,898]
```

The assignment was recovered by parsing that script as Python syntax and reading its literal list; the builder was not executed. Its SHA-256 is `b9beca78d645d3a79a347c20a5dd3889aeb01bfd517a65ac24289c4cedce6730`. The corresponding PNG already exists, is 2900 by 509 pixels, and has no embedded coordinate metadata. Those dimensions are consistent with enlargement of the recorded 690 by 121 pixel rectangle; they were not used to estimate its position.

The saved `reader_b_011_boxes.json` lists only c01–c16, explaining why extraction from that file omitted c17. The inline c17 assignment adds the wider context crop for the prose formula ending in E_i. The later audit box b16 is a different, narrower rectangle and was not substituted. The complete display (12) has its own audit box b12, also not substituted.

One supported row was appended to `documentation/first_crop_coordinates.tsv`. No image, page transcription, frozen audit file, historical builder, or report was changed by this recovery.
