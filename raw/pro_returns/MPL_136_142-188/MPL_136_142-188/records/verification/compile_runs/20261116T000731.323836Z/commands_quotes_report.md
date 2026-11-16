# Mechanical command and quotation-form check

Snapshot: `20261116T000731.323836Z`. All source hashes are in `compiled_sources.sha256`.

Checked 46 page fragments; 125 distinct control sequences.

## Editorial commands

| Command | Count |
|---|---:|
| `\cotefile` | 1 |
| `\deleted` | 123 |
| `\diagram` | 24 |
| `\figure` | 35 |
| `\illegible` | 1 |
| `\inserted` | 70 |
| `\margin` | 103 |
| `\mspage` | 1 |
| `\scanpage` | 46 |
| `\uline` | 280 |
| `\unsure` | 331 |
| `\uuline` | 1 |

Other candidate state-marking or definition commands flagged: 0.

## Double-quote command occurrences

`\textquotedbl`: 7 occurrences; 0 outside table/diagram environments and arrow options. Classification is syntactic and does not identify manuscript intent.

Scan 150, TeX line 17; inside_table_or_diagram_environment; environments `array`:

```latex
\text{\textquotedbl}&&\text{\textquotedbl}&&\text{\textquotedbl}\\
```

Scan 150, TeX line 17; inside_table_or_diagram_environment; environments `array`:

```latex
\text{\textquotedbl}&&\text{\textquotedbl}&&\text{\textquotedbl}\\
```

Scan 150, TeX line 17; inside_table_or_diagram_environment; environments `array`:

```latex
\text{\textquotedbl}&&\text{\textquotedbl}&&\text{\textquotedbl}\\
```

Scan 152, TeX line 6; inside_table_or_diagram_environment; environments `array`:

```latex
\text{\textquotedbl}&\\
```

Scan 155, TeX line 8; inside_table_or_diagram_environment; environments `array`:

```latex
&&&\text{\textquotedbl}&\\
```

Scan 186, TeX line 34; inside_table_or_diagram_environment; environments `array`:

```latex
\text{\textquotedbl}&&\\
```

Scan 188, TeX line 27; inside_table_or_diagram_environment; environments `array`:

```latex
&\simeq S\{X_0,X_1,dX_0,dX_1\}/(X_0+X_1-T,dX_0+dX_1)_{\mathrm{pd}}&&\text{\textquotedbl}\\
```

## Exact quote forms

| Form | Syntactic context | Count |
|---|---|---:|
| `"` | tikz_arrow_option_syntax | 56 |
| `''` | inside_table_or_diagram_environment | 6 |
| `''` | outside_table_and_arrow_options | 26 |
| `\textquotedbl` | inside_table_or_diagram_environment | 7 |
| ```` | outside_table_and_arrow_options | 23 |

Every occurrence, including source lines, is retained in `quote_occurrences.csv`. Literal double quotes in TikZ arrow options are recorded separately from other source positions. No visual judgment about quotation marks was made.

## Apostrophe-run accounting

Four outside-table double-apostrophe runs occur as `G''` on scan 185, TeX lines 22, 24, 33 and 34. The source text on scan 163, TeX line 40, has an opening double backtick before its final underlined word with no matching closing double apostrophe on that page. These are source-syntax observations only; no manuscript correction is proposed. Together they explain why the outside-table totals are 23 double-backtick runs and 26 double-apostrophe runs.
