# Context searches for documentary and doubt candidates

Research began after the parent reported the transcription freeze at 2026-11-15 01:44:43 UTC and the context opening at 01:44:50 UTC. The supplied `context/README.md` and all 152 lines of `context/notes/RESULTS_STATE.md` were read before any candidate notes were written; completion was confirmed by 2026-11-15 01:52:09 UTC. Only frozen textual transcription and supplied context text are used. No manuscript image was consulted by this agent, and no transcription file was modified.

Every search below precedes its associated candidate note. A context entry is treated as an unreviewed return claim, first-pass lead, or planning question unless its own entry explicitly records referee approval. Search absence means absence from the supplied context files, not absence from literature or unavailable source files.

## D01 — Pagination and selected-page count

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "127.?176|126.?175|page.count|cote.?154|c154|154-generisation-cube" context`.
- Results: 2 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/README.md:9:- **154** scans 127-176: "[Système de pseudo-droites] : notes manuscrites (1983-1984, s.d.)." (1983-1984[156]). Book V, V.2 Jordan, immersions, pseudolines; rank 18.
context/notes/RESULTS_STATE.md:122:- **154-generisation-cube** (cote 154, their pp. 153; our scans 154) [conjecture (unsearched) | Lean card: statement, no verdict…] For a position D of an added pseudoline passing through ν ≥ 2 vertices of Σ, the stable generisations of D are the 2^ν vertices of a ν-cube whose ν·2^(ν−1) edges are the generisations through exactly one vertex, incidence being specialisation — whereas a straight line through ν vertices of a line arrangement has only 2ν stable… Our intake: new to us: our package for this cote is waiting
```

## D02 — Dated cancelled title at scan 160

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "1[.]1[.]84|facettes exceptionnelles|Compléments et rectifications|exceptional facets" context`.
- Results: 0 matching lines in the supplied context.
- Search status: no matching entry or matching text for these query terms in the supplied context.

## D03 — Printed computing dates

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "CRAY|JESNEWS|JOB EXECUTION|25/ ?8/ ?82|1982|Cadarache|CFT" context`.
- Results: 1 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/Esquisse_cote119_copy1_API_transcription.tex:1224:1982. La géométrie bidimensionelle fournit de nombreux autres
```

## D04 — Local headings versus supplied catalogue title

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "types de fuseaux|balayages élémentaires|Canali|Canaux|Système de pseudo-droites|cote.?154" context`.
- Results: 3 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/README.md:9:- **154** scans 127-176: "[Système de pseudo-droites] : notes manuscrites (1983-1984, s.d.)." (1983-1984[156]). Book V, V.2 Jordan, immersions, pseudolines; rank 18.
context/README.md:16:and the rest of 154 ("Système de pseudo-droites", 1983-84, on listing paper), whose first 45 scans went as a probe
context/notes/RESULTS_STATE.md:122:- **154-generisation-cube** (cote 154, their pp. 153; our scans 154) [conjecture (unsearched) | Lean card: statement, no verdict…] For a position D of an added pseudoline passing through ν ≥ 2 vertices of Σ, the stable generisations of D are the 2^ν vertices of a ν-cube whose ν·2^(ν−1) edges are the generisations through exactly one vertex, incidence being specialisation — whereas a straight line through ν vertices of a line arrangement has only 2ν stable… Our intake: new to us: our package for this cote is waiting
```

## U01 — Inverse-circuit question answered immediately

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "circuit inverse|circuit.*rive|rive.*orientation|inverse.*circuit" context`.
- Results: 0 matching lines in the supplied context.
- Search status: no matching entry or matching text for these query terms in the supplied context.

## U02 — Deferred sigma operations and later action

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "sigma_0|sigma_1|sigma_2|σ[₀₁₂]|fuseaux|fuseau" context`.
- Results: 2 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/Esquisse_cote119_copy1_API_transcription.tex:520:\[ \underline{C}_2 = \langle \sigma_0,\sigma_1,\sigma_2 \,|\, \sigma_0^{\,2} = \sigma_1^{\,2} = \sigma_2^{\,2} = (\sigma_0\sigma_2)^2 = 1 \rangle \ , \]
context/Esquisse_cote119_copy1_API_transcription.tex:537:\[ \rho_s = \sigma_2\sigma_1 \ , \quad \rho_f = \sigma_1\sigma_0 \ , \quad \sigma = \sigma_0\sigma_2 = \sigma_2\sigma_0 \ , \]
```

## U03 — Uninterpreted double quotient

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "Il faudrait comprendre|sigma_1,?.*sigma|σ.?1.*σ|quotient.*fuseau" context`.
- Results: 2 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/Esquisse_cote119_copy1_API_transcription.tex:520:\[ \underline{C}_2 = \langle \sigma_0,\sigma_1,\sigma_2 \,|\, \sigma_0^{\,2} = \sigma_1^{\,2} = \sigma_2^{\,2} = (\sigma_0\sigma_2)^2 = 1 \rangle \ , \]
context/Esquisse_cote119_copy1_API_transcription.tex:537:\[ \rho_s = \sigma_2\sigma_1 \ , \quad \rho_f = \sigma_1\sigma_0 \ , \quad \sigma = \sigma_0\sigma_2 = \sigma_2\sigma_0 \ , \]
```

## U04 — Questioned circuit closure

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "D_\\{20\\}|D20|circuit.*ferm|circuit.*clos|clos.*circuit" context`.
- Results: 0 matching lines in the supplied context.
- Search status: no matching entry or matching text for these query terms in the supplied context.

## U05 — Number of incident endpoints

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "deux sommets|two.*vertices|vertices.*edge|sommets incidents|P4e|R121-08" context`.
- Results: 3 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/notes/RESULTS_STATE.md:42:- **EXIT_ONE_TYPE P4e** [Proved (the return's claim)] The coarse maquette does not determine the link even among good projective pairs; strata, normal data and inertia are lost; the analytic converse also fails. Where: MPL 149; folio 66; scan 133. (EXIT_ONE_TYPE_results.csv)
context/notes/RESULTS_STATE.md:82:- **MPL_121_049-073+153+155 R121-08** [Incidence is only one part of a stratif… (research note of a returned package, first pass; a lead)] R121-08 — Incidence is only one part of a stratified reconstruction: **Source:** 121:050–052. **Kind:** unpursued implication. **Quote:** “relation d'ordre”; “feuilles fermées”. **Context comparison:** `MPL_147_138-190_transcription.tex`, 179–180 and 185–190:… (MPL_121_049-073+153+155_notes.md)
context/notes/RESULTS_STATE.md:122:- **154-generisation-cube** (cote 154, their pp. 153; our scans 154) [conjecture (unsearched) | Lean card: statement, no verdict…] For a position D of an added pseudoline passing through ν ≥ 2 vertices of Σ, the stable generisations of D are the 2^ν vertices of a ν-cube whose ν·2^(ν−1) edges are the generisations through exactly one vertex, incidence being specialisation — whereas a straight line through ν vertices of a line arrangement has only 2ν stable… Our intake: new to us: our package for this cote is waiting
```

## U06 — Unsecured endpoint reconstruction choices

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "blocage|sommet extrémité|choix naturels|aucun de ces choix|MPL_150_044-084.*N18|MPL_150_044-084.*Q2" context`.
- Results: 2 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/notes/RESULTS_STATE.md:87:- **MPL_150_044-084 N18** [Objectwise deformation equivalences do… (research note of a returned package, first pass; a lead)] N18 — Objectwise deformation equivalences do not remove the attachment data: **Source:** 150/077, (51)–(53), and 081–084. **Kind:** own explanatory deduction. **Anchor:** “recollement des \(V_i\) suivant les \(V_{ij}\).” **Context search:** recollement, homot… (MPL_150_044-084_notes.md)
context/notes/RESULTS_STATE.md:107:- **MPL_150_044-084 Q2** [The postponed realization and the Remor… (research note of a returned package, first pass; a lead)] Q2 — The postponed realization and the Remords: **Source:** 150/073–084, especially 074, 076–077 and 084. **Kind:** unproved claim / bounded historical comparison. **Anchors:** “Description heuristique”; “dépend du choix de rétractions”; “recollement.” **Cont… (MPL_150_044-084_notes.md)
```

## U07 — Universal principal-specialization question

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "principale.*spécialisation|spécialisation.*principale|principal.*speciali|S_D|154-generisation-cube" context`.
- Results: 1 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/notes/RESULTS_STATE.md:122:- **154-generisation-cube** (cote 154, their pp. 153; our scans 154) [conjecture (unsearched) | Lean card: statement, no verdict…] For a position D of an added pseudoline passing through ν ≥ 2 vertices of Σ, the stable generisations of D are the 2^ν vertices of a ν-cube whose ν·2^(ν−1) edges are the generisations through exactly one vertex, incidence being specialisation — whereas a straight line through ν vertices of a line arrangement has only 2ν stable… Our intake: new to us: our package for this cote is waiting
```

## U08 — Incomplete map from frames to stable positions

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "position relative stable|positions relatives|relative position|repères|repère" context`.
- Results: 7 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/Esquisse_cote119_copy1_API_transcription.tex:273:de cette tour, en termes du ``paramètre'' dans $\hat{\pi}_{0,3}$ qui repère l'élé-%
context/Esquisse_cote119_copy1_API_transcription.tex:517:particulièrement simple, via l'ensemble des ``repères'' (ou ``drapeaux'',
context/Esquisse_cote119_copy1_API_transcription.tex:538:opérations de \uline{rotation élémentaire} d'un repère autour d'un sommet,
context/Esquisse_cote119_copy1_API_transcription.tex:868:sur l'ensemble des repères. Dans le cas orienté et en termes de
context/Esquisse_cote119_copy1_API_transcription.tex:881:lière. Elle se trouve épinglée par le choix d'un repère, et son
context/Esquisse_cote119_copy1_API_transcription.tex:998:repère) canonique de l'espace affine ou projectif ambiant, de
context/Esquisse_cote119_copy1_API_transcription.tex:2215:différentes ``positions relatives'' possibles (stables ou non) d'une
```

## W01 — Rejected sigma0 inverse guess

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "serait-ce l.inverse|symétrique.*origine|symétrie centrale|sigma_0|σ₀" context`.
- Results: 2 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/Esquisse_cote119_copy1_API_transcription.tex:520:\[ \underline{C}_2 = \langle \sigma_0,\sigma_1,\sigma_2 \,|\, \sigma_0^{\,2} = \sigma_1^{\,2} = \sigma_2^{\,2} = (\sigma_0\sigma_2)^2 = 1 \rangle \ , \]
context/Esquisse_cote119_copy1_API_transcription.tex:537:\[ \rho_s = \sigma_2\sigma_1 \ , \quad \rho_f = \sigma_1\sigma_0 \ , \quad \sigma = \sigma_0\sigma_2 = \sigma_2\sigma_0 \ , \]
```

## W02 — Principal replaced by criticality at least two

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "supracrit|criticalité|tricalité|principales|principale|critical.*pseudoline" context`.
- Results: 5 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/Esquisse_cote119_copy1_API_transcription.tex:96:de ce que je considérais comme mes principales contributions mathéma-%
context/Esquisse_cote119_copy1_API_transcription.tex:187:fini de $\mathbb{Q}$, qui ont été ma principale source d'inspiration, ainsi
context/Esquisse_cote119_copy1_API_transcription.tex:194:des principales structures et des visions des choses qu'elles expri-%
context/Esquisse_cote119_copy1_API_transcription.tex:227:ou conforme des surface. La principale raison sans doute de cette
context/Esquisse_cote119_copy1_API_transcription.tex:2405:la principale question ouverte pour les fondements d'une ``géométrie
```

## W03 — Corrected sigma1 exchange and cancelled equivalent-looking formula

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "sigma.*sigma|σ.*σ|barycentri|biorient" context`.
- Results: 9 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/notes/RESULTS_STATE.md:26:- **BISITE G.10** [Proved (the return's claim)] Verification of the finite least-vertex geometric dictionary. Let $P$ be a finite poset and $Z=|NP|$. Label a point by the least vertex with positive barycentric coordinate. With downsets open on $P$, this is a continuous map $s:… Where: STRATA A.4 A.5; Part G prerequisite dictionary. (BISITE_results.csv)
context/STATEMENTS_WITH_STATUS.md:29:| STRATA F.9 | Filling punctures and stabilizing define actual forgetful functors | claim (return: Proved) | proved in outline; `φ(Δ_σ) ⊂ Δ_{qσ}` and the typing of arrows followed; the comparison with the geometric map is argued briefly and I did not check it beyond that. |
context/STATEMENTS_WITH_STATUS.md:30:| STRATA F.10 | Full-model entrance forgetful functors are W-infinity-proper | claim (return: Proved) | proved in outline; The reduction of each lifting category to the poset `{ρ ⊇ σ : qρ = η}` followed step by step and is correct. Its contractibility for `σ = ∅` is the tree of Kent–Leininger–Schleimer, Theorem 7.1 (opened), with leaves for the curves that become peripheral; the reduction of general `σ` to that case by cutting along `σ` I followed only in outline. |
context/STATEMENTS_WITH_STATUS.md:62:| RESIDUE H.1 | Let $f:P\to Q$ be a proper functor of finite posets, meaning that \[ L(p,q)=\{r\in P:r\geq p,\ f(r)=q\} \] is weakly contractible whenever $f(p)\leq q$. The geometric direct image along $g=\|Nf\|$ preserves least-vertex-constructible sheaves and agrees with categorical right Kan extension, for space, spectrum, and derived-module coefficients. The proof below replaces BISITE D.11's initiality induction on the poset of fibre cells by normalization of barycentric coordinates, followed by geometric proper base change. | claim (return: Proved) | no review |
context/STATEMENTS_WITH_STATUS.md:64:| RESIDUE H.3 | Fix $\sigma$ upstairs and an exit arrow $\beta:q\sigma\to\eta$ downstairs. Its outgoing lifting category for $Q$ is either weakly contractible or equivalent to $B\mathbb Z$. It is equivalent to $B\mathbb Z$ exactly when forgetting the mark contracts a rational bridge of $\sigma$ and $\beta$ smooths the node produced by that contraction. This classification holds for every stable $(g,n)$. | claim (return: Proved) | no review |
context/Esquisse_cote119_copy1_API_transcription.tex:458:cription de $Sl(2,\mathbb{Z})$ par $(\rho,\sigma \mid \rho^3 = \sigma^2,\ \rho^4 = \sigma^6 = 1)$), on trouvera
context/Esquisse_cote119_copy1_API_transcription.tex:520:\[ \underline{C}_2 = \langle \sigma_0,\sigma_1,\sigma_2 \,|\, \sigma_0^{\,2} = \sigma_1^{\,2} = \sigma_2^{\,2} = (\sigma_0\sigma_2)^2 = 1 \rangle \ , \]
context/Esquisse_cote119_copy1_API_transcription.tex:525:\[ \underline{C}_2^{+} = \langle \rho_s,\rho_f,\sigma \,|\, \rho_s\rho_f = \sigma,\ \sigma^2 = 1 \rangle \ , \]
context/Esquisse_cote119_copy1_API_transcription.tex:537:\[ \rho_s = \sigma_2\sigma_1 \ , \quad \rho_f = \sigma_1\sigma_0 \ , \quad \sigma = \sigma_0\sigma_2 = \sigma_2\sigma_0 \ , \]
```

## W04 — Changed orientation and left/right wording

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "orientation.*rive|rive.*orientation|générisation.*gauche|générisation.*droite|orientation.*fuseau" context`.
- Results: 0 matching lines in the supplied context.
- Search status: no matching entry or matching text for these query terms in the supplied context.

## W05 — Abandoned fuseau nomenclature

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "biparall|paralléli|semi.couloir|couloirs|unilatéraux|fuseau" context`.
- Results: 0 matching lines in the supplied context.
- Search status: no matching entry or matching text for these query terms in the supplied context.

## W06 — Cancelled preimage correction

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "varphi.*-1|φ.*L|facette|facets|K_0|K₀" context`.
- Results: 4 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/STATEMENTS_WITH_STATUS.md:29:| STRATA F.9 | Filling punctures and stabilizing define actual forgetful functors | claim (return: Proved) | proved in outline; `φ(Δ_σ) ⊂ Δ_{qσ}` and the typing of arrows followed; the comparison with the geometric map is argued briefly and I did not check it beyond that. |
context/STATEMENTS_WITH_STATUS.md:31:| STRATA F.11 | Forgetting a marking is always W-infinity-smooth | claim (return: Refuted) | proved; Recomputed: the lifting groupoid is the action groupoid of `K = ker φ` on `KΔ_x/Δ_x`, with stabilizer `K ∩ Δ_x = ⟨t_1 t_2^{-1}⟩ ≅ Z`. |
context/Esquisse_cote119_copy1_API_transcription.tex:634:tres de facettes (sommets, arêtes ou faces) - dès lors l'applica-%
context/Esquisse_cote119_copy1_API_transcription.tex:1015:les facettes soient d'ordre fini, i.e. pour lesquels les para-%
```

## W07 — Cancelled exceptional-facet geometric prescription

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "branche principale|rive privilégiée|ruban généralisé|exceptional.*facet|facette exceptionnelle" context`.
- Results: 0 matching lines in the supplied context.
- Search status: no matching entry or matching text for these query terms in the supplied context.

## W08 — Cancelled trial diagrams and labels

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "cancelled|cancell|withdrawn|rayé|biff|R39" context`.
- Results: 1 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/notes/RESULTS_STATE.md:85:- **MPL_148_029-072 R39** [The cancelled skeleton description reta… (research note of a returned package, first pass; a lead)] R39 — The cancelled skeleton description retains its gluing-data proposal: **Source:** 148/067:10,62–85,87–96. **Kind:** withdrawn in the same text / unpursued implication. **Anchors:** “pondération des … drapeaux”; “anti-isom”. The cancelled description prop… (MPL_148_029-072_notes.md)
```

## W09 — Triangle replacing three lines; negation wording

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "système de trois droites|triangle dual|duaux|assymétrique|jamais.*critique" context`.
- Results: 0 matching lines in the supplied context.
- Search status: no matching entry or matching text for these query terms in the supplied context.

## W10 — Edits inside the surface conditions

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "1-compl|d.ordre pair|multiplicité.*incidence|incidence.*multiplicité|epsilon_s|ε_s" context`.
- Results: 5 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/Esquisse_cote119_copy1_API_transcription.tex:479:topique des plongements d'un 1-complexe topologique dans une surface
context/Esquisse_cote119_copy1_API_transcription.tex:492:complète des classes d'isotopie de plongements de tels 1-complexes,
context/Esquisse_cote119_copy1_API_transcription.tex:504:``isotopique'' des surfaces compactes $X$, munies d'un 1-complexe to-%
context/Esquisse_cote119_copy1_API_transcription.tex:619:comme précédemment du 1-complexe plongé $K = [0,1]$.
context/Esquisse_cote119_copy1_API_transcription.tex:2188:1-complexes topologiques, des immersions d'une surface à bord qui
```

## Q01 — Cube claim and Hua register status

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "154-generisation-cube|stable generisation|pseudoline|pseudo-droite|pseudo.line" context`.
- Results: 10 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/README.md:9:- **154** scans 127-176: "[Système de pseudo-droites] : notes manuscrites (1983-1984, s.d.)." (1983-1984[156]). Book V, V.2 Jordan, immersions, pseudolines; rank 18.
context/README.md:15:Jordan, immersions, pseudolines (V.2 of our plan, rank 18): 71 (with a manuscript by C. Contou-Carrère), 80, 81,
context/README.md:16:and the rest of 154 ("Système de pseudo-droites", 1983-84, on listing paper), whose first 45 scans went as a probe
context/README.md:17:(package 53; return not in yet). For 154 the war game has three readings: tame topology (pseudolines as tame curves in
context/notes/RESULTS_STATE.md:3:Built 2026-11-14 20:11 UTC by `tools_20261113/build_results_state.py` from our own results, selected for this package by its place in the plan (rank 18, Book V: Jordan, immersions, pseudolines), its cotes and its subjects (forms, strata). Rebuilt just before the package is sent, so it is as current as our records.
context/notes/RESULTS_STATE.md:122:- **154-generisation-cube** (cote 154, their pp. 153; our scans 154) [conjecture (unsearched) | Lean card: statement, no verdict…] For a position D of an added pseudoline passing through ν ≥ 2 vertices of Σ, the stable generisations of D are the 2^ν vertices of a ν-cube whose ν·2^(ν−1) edges are the generisations through exactly one vertex, incidence being specialisation — whereas a straight line through ν vertices of a line arrangement has only 2ν stable… Our intake: new to us: our package for this cote is waiting
context/Esquisse_cote119_copy1_API_transcription.tex:2196:pologique-combinatoire des systèmes de droites ou pseudo-droites.
context/Esquisse_cote119_copy1_API_transcription.tex:2214:associée à un système de $n$ pseudo-droites, qui classifie les
context/Esquisse_cote119_copy1_API_transcription.tex:2216:$(n+1)$ème pseudo-droite par rapport au système donné, ou encore :
context/Esquisse_cote119_copy1_API_transcription.tex:2218:différents choix possibles d'une ``pseudo-droite à l'infini''. J'ai
```

## Q02 — Uncertain cube count and straight-line comparison

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "154-generisation-cube|2\\^ν|2ν|straight.lines|polygone.*régulier|diagonales" context`.
- Results: 2 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/notes/RESULTS_STATE.md:122:- **154-generisation-cube** (cote 154, their pp. 153; our scans 154) [conjecture (unsearched) | Lean card: statement, no verdict…] For a position D of an added pseudoline passing through ν ≥ 2 vertices of Σ, the stable generisations of D are the 2^ν vertices of a ν-cube whose ν·2^(ν−1) edges are the generisations through exactly one vertex, incidence being specialisation — whereas a straight line through ν vertices of a line arrangement has only 2ν stable… Our intake: new to us: our package for this cote is waiting
context/Esquisse_cote119_copy1_API_transcription.tex:1020:de tous (moralement celui du polygone régulier à un seul côté !)
```

## Q03 — Disconnectedness marginal remark

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "disconnexe|disconnected|comp.*connexe.*libre|bord du fuseau|couple.*flèches" context`.
- Results: 0 matching lines in the supplied context.
- Search status: no matching entry or matching text for these query terms in the supplied context.

## Q04 — Fuseau definition and isotopy-class bijection

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "fuseau|semi.stable|semi.stble|isotopy.*bank|isotopie.*rive" context`.
- Results: 0 matching lines in the supplied context.
- Search status: no matching entry or matching text for these query terms in the supplied context.

## Q05 — Orientation and duality signs

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "plans projectifs.*duaux|dual.*projective|projective.*dual|non associés|non croisés|épure|équerre" context`.
- Results: 0 matching lines in the supplied context.
- Search status: no matching entry or matching text for these query terms in the supplied context.

## Q06 — Axiomatic surface condition and constant face sum

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "cellulaire|cellular|valence|multiplicity|multiplicité|face.*sum" context`.
- Results: 56 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/notes/RESULTS_STATE.md:19:- **RESIDUE I.7** [Open (the return's claim)] No proof or counterexample is supplied here for the reversible accessible-localizer classification in Part I(2), including its interval between integral homology equivalences and $W_0$. For Part I(3), the unresolved assertion is an assignment $\mathbb D\mapsto\mathbb D'$ on all derivators satisfying Der~1--4, natural in exact m… (RESIDUE_results.csv)
context/notes/RESULTS_STATE.md:37:- **BISITE G.9** [Known (the return's claim)] The exact canonical equivalence criterion for finite posets. For a finite poset $P$ define the colimit-preserving transform \[ (V_PF)(s)= \lim_{t\in P^{\mathrm{op}}} \bigl(\Sigma^\infty_+\operatorname{Hom}_P(t,s)\otimes F(t)\bigr… Where: Lead 4 corrected equivalence; Part G finite posets. (BISITE_results.csv)
context/notes/RESULTS_STATE.md:52:- **STRATA C.2** [Known (the return's claim)] B(E^op) maps by a specified endpoint-compatible weak equivalence to the holink from BB into BX minus BB, whose open stratum retracts to BA. Where: Lead 3; XII ms.59–63. (STRATA_results.csv)
context/notes/RESULTS_STATE.md:53:- **STRATA C.8** [Proved (the return's claim)] Locally constant enhanced coefficients form the Cat_infinity pullback Fun(BA,C) x_Fun(BE,C) Fun(BB,C), with equivalence gluing data. Where: GALOIS A.8/B.3/B.5 comparison; Lead 3 locally constant extension. (STRATA_results.csv)
context/notes/RESULTS_STATE.md:87:- **MPL_150_044-084 N18** [Objectwise deformation equivalences do… (research note of a returned package, first pass; a lead)] N18 — Objectwise deformation equivalences do not remove the attachment data: **Source:** 150/077, (51)–(53), and 081–084. **Kind:** own explanatory deduction. **Anchor:** “recollement des \(V_i\) suivant les \(V_{ij}\).” **Context search:** recollement, homot… (MPL_150_044-084_notes.md)
context/notes/RESULTS_STATE.md:106:- **MPL_150_044-084 N39** [Aspherical strata do not settle normal-… (research note of a returned package, first pass; a lead)] N39 — Aspherical strata do not settle normal-link truncation: **Source:** 150/072 and 077, compared with 147/180 and 149/134. **Kind:** unpursued implication / register comparison. **Anchor:** “comp. connexes”; “équivalence d'homotopie de proespaces.” **Conte… (MPL_150_044-084_notes.md)
context/notes/RESULTS_STATE.md:115:- **WG2 B15 (§1.2)** [question or plan item of the war game (round 2; unchecked)] 1.2 Shape: the bridges (round 1, section 1.2): B15 ; V, VI ; For a finite poset P with the topology of down-sets, spaces over P localized at the maps that are equivalences over every open set are the functors P → spaces. Over the real line the same statement is open in our returns. Tame topology is the setting in which it shoul… (PROGRAM_WARGAME_ROUND2_20261112.md)
context/STATEMENTS_WITH_STATUS.md:14:| STRATA C.2 | B(E^op) maps by a specified endpoint-compatible weak equivalence to the holink from BB into BX minus BB, whose open stratum retracts to BA. | claim (return: Known) | known; The simplicial identification `Map_{Δ[1]}(Δ[1], N(X^op)) = N(E^op)` is an equality; the theorem of Douteau–Waas opened; the retraction of `BX ∖ BB` onto `BA` checked (the coordinates sum to 1). |
context/STATEMENTS_WITH_STATUS.md:15:| STRATA C.3 | The specified map hocolim(BA <- BE -> BB) -> BX is a weak equivalence and agrees with holink evaluation under C.2. | claim (return: Known) | proved; I followed the proof of POLES G.19 as described: the category `P` with fibres `A, E, B`, the functor to `X`, and for `x ∈ B` the endofunctor of `P/x` with natural transformations from the identity and from the constant functor at `(x, id_x)`; for `x ∈ A`, `P/x = A/x`. This also closes "G.19 unverified" of the POLES review. |
context/STATEMENTS_WITH_STATUS.md:20:| STRATA C.8 | Locally constant enhanced coefficients form the Cat_infinity pullback Fun(BA,C) x_Fun(BE,C) Fun(BB,C), with equivalence gluing data. | claim (return: Proved) | proved; From C.3: a pushout of spaces is a pushout of ∞-categories. |
context/STATEMENTS_WITH_STATUS.md:39:| BISITE D.1 | The actual comparison supplied by open tests. For a space $Y$, put \[ \begin{split} W^{\mathrm{opn}}_Y=\{u:X\longrightarrow X'\text{ over }Y:\quad& \Pi(u^{-1}U):\Pi(X\times_YU)\longrightarrow\Pi(X'\times_YU)\\ &\text{is an equivalence for every open }U\subseteq Y\}. \end{split} \] Here $u^{-1}U$ means the displayed restricted map, not an inverse-image operation on morphisms. This class contains the isomorphisms and satisfies two-out-of-three and retract closure. There is a canonical functor \[ C_Y:(\mathrm{Top}/Y)[(W^{\mathrm{opn}}_Y)^{-1}] \longrightarrow\operatorname{CoShv}(Y;\mathcal S),\qquad C_Y(X)(U)=\Pi(X\times_YU). \tag{D.1} \] Its values are hypercomplete cosheaves. This statement does not assert that (D.1) is an equivalence for every $Y$. | claim (return: Known) | Unverified citation (HA 5.5.5, A.3). |
context/STATEMENTS_WITH_STATUS.md:40:| BISITE D.2 | A complete realization theorem for finite Alexandrov bases. Let $P$ be a finite poset with the topology of downsets. There are equivalences \[ (\mathrm{Top}/P)[(W^{\mathrm{opn}}_P)^{-1}] \simeq\operatorname{Fun}(P,\mathcal S) \simeq\operatorname{CoShv}(P;\mathcal S). \tag{D.2} \] The first equivalence sends $f:X\to P$ to the covariant diagram $p\mapsto\Pi f^{-1}(P_{\leq p})$. It includes arbitrary, possibly empty fibres and non-Hausdorff total spaces. For a discrete, possibly infinite base $P$ the same statement holds by decomposition into its open fibres. | claim (return: Proved) | Proved in outline: the adjunction `D ⊣ E`, the continuity of the jump homotopy on both kinds of generators and the induction on downsets followed; the rectification step is HTT 4.2.4.4. |
context/STATEMENTS_WITH_STATUS.md:42:| BISITE D.4 | Proper maps do not preserve open-test equivalences. Even for locally compact Hausdorff spaces, strict pullback along a proper map need not preserve $W^{\mathrm{opn}}$. Thus geometric proper base change for sheaves cannot be read as this assertion about spaces over a base. | claim (return: Refuted) | Statement checked (by hand: over every open set of `[0,1]` the inclusion `(0,1] → [0,1]` is a weak equivalence; over the point `0` it is `∅ → pt`). |
context/STATEMENTS_WITH_STATUS.md:44:| BISITE D.6 | Proper base change is a coefficient theorem. Consider a cartesian square of locally compact Hausdorff spaces \[ \begin{array}{ccc} X'&\xrightarrow{g'}&X\\[-2pt] {\scriptstyle f'}\downarrow&&\downarrow{\scriptstyle f}\\[-2pt] Y'&\xrightarrow{g}&Y. \end{array} \] If $f$ is proper, the canonical mate $g^*f_*\to f'_*g'^*$ is an equivalence on sheaves of spaces. It is also an equivalence on sheaves with values in a stable bicomplete infinity-category. These are ordinary infinity-sheaves; hypercompletion is not silently substituted. | claim (return: Known) | Unverified citation (HTT 7.3.1.18; Volpe). |
context/STATEMENTS_WITH_STATUS.md:45:| BISITE D.7 | A precise smooth topological comparison. A space $K$ is essential when the constant-sheaf functor $\mathcal S\to\operatorname{Shv}(K;\mathcal S)$ has a left adjoint. A shape submersion $g:Z\to Y$ is locally, on its source, a projection $V\times K\to V$ with $V$ open in $Y$ and $K$ essential. Assume either $Y$ is locally compact or all these $K$ are locally compact. Then for any presentable coefficient infinity-category $\mathcal C$ there is an adjunction $g_\sharp\dashv g^*$ on sheaves with these coefficients. In a cartesian square as in D.6 with $g$ a shape submersion and with the same local compactness condition after pullback, the canonical maps \[ g'_\sharp f'^*\longrightarrow f^*g_\sharp, \qquad g^*f_*\longrightarrow f'_*g'^* \] are equivalences. | claim (return: Known) | Unverified citation (Volpe 2025, 3.23–3.27). |
context/STATEMENTS_WITH_STATUS.md:46:| BISITE D.8 | The stable sheaf--cosheaf equivalence and the shriek operation. For a locally compact Hausdorff space $Y$ and a stable bicomplete infinity-category $\mathcal C$, there is an equivalence \[ \mathbb V_Y:\operatorname{Shv}(Y;\mathcal C) \xrightarrow{\ \simeq\ }\operatorname{CoShv}(Y;\mathcal C), \qquad \mathbb V_Y(F)(U)= \operatorname*{colim}_{K\subseteq U\ { m compact}} \operatorname{fib}\bigl(F(Y)\to F(Y\setminus K)\bigr). \tag{D.8} \] For a continuous map $f:X\to Y$ between such spaces, cosheaf pushforward $f_+$ is $(f_+G)(U)=G(f^{-1}U)$. The topological operation with proper support is $f_!=\mathbb V_Y^{-1}f_+\mathbb V_X$ and has a right adjoint $f^!$. For proper $f$ it agrees with $f_*$. This does not identify $f_!$ with the left adjoint $f_\sharp$ of D.7. | claim (return: Known) | Unverified citation (HA 5.5.5.1; Volpe 6.9). |
context/STATEMENTS_WITH_STATUS.md:50:| BISITE D.12 | The unrestricted topological realization and its proposed dual. For a locally compact Hausdorff base $Y$, is the functor $C_Y$ in (D.1), with all topological total spaces allowed, an equivalence? If so, what precise localization of spaces over the same $Y$ presents $\operatorname{Shv}(Y;\mathcal S)$ and is compatible with the proposed dual class of base-change maps? Neither statement is established in this audit for a general $Y$; the first unproved test base in our argument is $\mathbb R$. | claim (return: Open) | Open. |
context/STATEMENTS_WITH_STATUS.md:58:| RESIDUE G.2 | The continuous maps whose strict pullback preserves all open-test weak equivalences include maps which are not shape submersions in the sense of \citet[Definition 3.23]{GHIJVolpe2025}. In particular, the projection from the Cantor space $K=\{0,1\}^{\mathbb N}$ to a point is such a map. | claim (return: Proved) | no review |
context/STATEMENTS_WITH_STATUS.md:60:| RESIDUE G.4 | For a locally compact Hausdorff space $Y$ and a stable infinity-category $\mathcal V$ admitting small limits and colimits, Lurie's covariant Verdier duality identifies $\operatorname{Shv}(Y;\mathcal V)$ with $\operatorname{CoShv}(Y;\mathcal V)$, by $A\mapsto(U\mapsto\Gamma_c(U,A))$ \citep[Theorem 5.5.5.1 and Proposition 5.5.5.10]{GHIJLurie2017}. This known theorem does not by itself provide either raw-space localization in Part G. Its displayed construction fails to be an equivalence for pointed-space coefficients. | claim (return: Proved) | no review |
context/STATEMENTS_WITH_STATUS.md:68:| RESIDUE H.7 | The program \path{code/GHIJ/finite_poset_direct_image.py} independently enumerates all maps between one representative of every poset isomorphism class with at most five objects, including the empty poset. The counts of posets of sizes $0,1,2,3,4,5$ are $1,1,2,5,16,63$. It examines $1,349,916$ monotone maps and recognizes $96,372$ proper maps. Properness is certified by explicit simplicial collapses of every nonempty outgoing lifting order complex; noncontractible cases are rejected by homology over $\mathbb Q$ or $\mathbb F_2$. The program aborts rather than classifying an acyclic but uncertified complex as contractible. No such undecided case occurs in this range. For every proper map and every nonempty target simplex, it computes the categorical stalk and the actual geometric-fibre cellular cohomology, for the constant coefficient and for each principal-cosieve indicator. This gives $5,536,094$ stalk/coefficient cases, each computed over both $\mathbb Q$ and $\mathbb F_2$, with no discrepancy. A fibre cell is indexed by a source chain meeting each level of the target simplex; it is a product of simplices, of dimension $\|\kappa\|-\|\sigma\|$. Its signed boundary deletes one vertex while keeping every level nonempty, using the product-boundary sign. The code verifies that consecutive boundary matrices multiply to zero. Exact rational ranks use integer elimination with gcd reduction, and binary ranks use bit arithmetic. For a principal cosieve, extension from the corresponding closed subcomplex reduces both computations to its intersection with the relevant fibre or lower inverse image. The supplied per-map CSV records all tests as successful; the JSON gives the totals by source and target size. These numerical comparisons check cohomology, not a replacement proof of the canonical mate; the latter is established in H.1. | claim (return: Proved) | no review |
context/Esquisse_cote119_copy1_API_transcription.tex:204:multiplicités modulaires, ce sont celles de Mumford-Deligne pour les
context/Esquisse_cote119_copy1_API_transcription.tex:216:je note $M^{\wedge}_{g,\nu}$ (compactification de la multiplicité ``ouverte''
context/Esquisse_cote119_copy1_API_transcription.tex:220:A vrai dire, il s'agit plutôt du système de \uline{toutes} les multiplicités
context/Esquisse_cote119_copy1_API_transcription.tex:229:système des multiplicités modulaires ``ouvertes'' $M_{g,\nu}$ se réflète
context/Esquisse_cote119_copy1_API_transcription.tex:309:tétraèdre. A fortiori les multiplicités modulaires $M_{0,5}$ (pour les
context/Esquisse_cote119_copy1_API_transcription.tex:342:cf. par. 5) d'une propriété extrêmement plausible des multiplicités
context/Esquisse_cote119_copy1_API_transcription.tex:359:dimension $N \geq 3$. Il est vrai que les multiplicités modulaires ne
context/Esquisse_cote119_copy1_API_transcription.tex:372:à une compréhension complète des quatre multiplicités modulaires
context/Esquisse_cote119_copy1_API_transcription.tex:387:milles constituent d'ailleurs sur les multiplicités envisagées des cour-%
context/Esquisse_cote119_copy1_API_transcription.tex:389:de la structure de ces multiplicités.
context/Esquisse_cote119_copy1_API_transcription.tex:426:la ``grande boite'' se trouve muni d'une décomposition cellulaire cano-%
context/Esquisse_cote119_copy1_API_transcription.tex:434:de structures cellulaires canoniques, qui à leur tour (cf.§3 plus bas)
context/Esquisse_cote119_copy1_API_transcription.tex:463:cellulaire de $M^{\wedge}_{g,\nu}$ généralisant celles qui se présentent sponta-%
context/Esquisse_cote119_copy1_API_transcription.tex:467:envisagées, pour effectuer le découpage cellulaire voulu.
context/Esquisse_cote119_copy1_API_transcription.tex:593:et des faces ne sont autres que les multiplicités des zéros et
context/Esquisse_cote119_copy1_API_transcription.tex:774:ture multiple de la ``tour de Teichmüller'' - les multiplicités modu-%
context/Esquisse_cote119_copy1_API_transcription.tex:777:multiplicités) qui semblent bien mériter l'appellation ``anabélienne''.
context/Esquisse_cote119_copy1_API_transcription.tex:812:sous une multiplicité d'avatars (dont certains ont été effleurés
context/Esquisse_cote119_copy1_API_transcription.tex:1219:Les multiplicités modulaires compactifiées $\hat{M}_{g,\nu}$ de Mumford-%
context/Esquisse_cote119_copy1_API_transcription.tex:1227:comme des ``multiplicités'' plutôt que comme des espaces ou variétés
context/Esquisse_cote119_copy1_API_transcription.tex:1228:au sens ordinaire (les points de ces multiplicité pouvant avoir
context/Esquisse_cote119_copy1_API_transcription.tex:1281:structure de ce type - tout au mieux d'une classe d'équivalence
context/Esquisse_cote119_copy1_API_transcription.tex:1315:un théorème d'équivalence entre deux catégories isotopiques conve-%
context/Esquisse_cote119_copy1_API_transcription.tex:1459:valente à celle des T'-espaces), et même, est une équivalence
context/Esquisse_cote119_copy1_API_transcription.tex:1460:d'homotopie (ce qui signifie qu'on a même une équivalence pour
context/Esquisse_cote119_copy1_API_transcription.tex:1564:une telle structure serait via l'hypothétique équivalence de caté-%
context/Esquisse_cote119_copy1_API_transcription.tex:1591:me un théorème d'équivalence de catégories isotopiques (voire même
context/Esquisse_cote119_copy1_API_transcription.tex:1625:disant ``espace'' modulaire est en fait une \uline{multiplicité} - techni-%
context/Esquisse_cote119_copy1_API_transcription.tex:1645:géométrique et arithmétique, c'est aux multiplicités modulaires
context/Esquisse_cote119_copy1_API_transcription.tex:1693:ma compréhension des multiplicités modulaires, il est d'ailleurs
context/Esquisse_cote119_copy1_API_transcription.tex:2077:multiplicités modulaires $\widehat{M}_{g,\nu}$ et leur structure stratifiée
context/Esquisse_cote119_copy1_API_transcription.tex:2144:vent l'hypothèse supplémentaire que l'immersion soit ``cellulaire'',
context/Esquisse_cote119_copy1_API_transcription.tex:2182:théorie de ``dévissage'' canonique d'une immersion cellulaire sta-%
context/Esquisse_cote119_copy1_API_transcription.tex:2453:(savoir celui des schémas, multiplicités schématiques etc) en
context/Esquisse_cote119_copy1_API_transcription.tex:2578:Dans le cas d'une multiplicité modérée cependant, il faut connaî-%
context/Esquisse_cote119_copy1_API_transcription.tex:2608:ne sont pas des multiplicités à proprement parler) on peut expri-%
```

## Q07 — Uncertain inequality punctuation and truncated algebra

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "alpha.*beta|α.*β|inégalité|inequalit|intervalles" context`.
- Results: 2 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/Esquisse_cote119_copy1_API_transcription.tex:791:$g$ et le ``nombre de trous'' $\nu$ satisfont l'inégalité $2g + \nu \geq 3$,
context/Esquisse_cote119_copy1_API_transcription.tex:1117:les n+(n+1) variables $\underline{\alpha}_i$ $(1 \leq i \leq n)$ et $\underline{\beta}_j$ $(0 \leq j \leq n)$.
```

## Q08 — Uncertain subleading factor and cancelled equality

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "asymptot|n\\^4|n\\^\\{4\\}|n\\(n|critical.*count|comptage" context`.
- Results: 0 matching lines in the supplied context.
- Search status: no matching entry or matching text for these query terms in the supplied context.

## Q09 — Generization-specialization cycle and Delta reading

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "spécialisation|générisation|specialization|generisation|Delta|Δ" context`.
- Results: 10 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/notes/RESULTS_STATE.md:8:**Referee check (14 Nov 2026, two referees, Claude Opus 5.5 at effort max).** LM7_PUSH checkpoint 09 claims, in E.65, that one character Δ on ĜT₀ reduces E.3 to whether Δ vanishes on ĜT; the chain is D.50 → E.58 → E.65. Refereed and proved as claimed: LM4 D.32, LM4 D.34, LM7_PUSH D.44, LM7_PUSH D.50, LM7_PUSH E.58, LM7_PUSH E.61, LM7_PUSH E.62, LM7_PUSH E.64, LM7_PUSH E.65, LM7_PUSH E.67. 
context/notes/RESULTS_STATE.md:122:- **154-generisation-cube** (cote 154, their pp. 153; our scans 154) [conjecture (unsearched) | Lean card: statement, no verdict…] For a position D of an added pseudoline passing through ν ≥ 2 vertices of Σ, the stable generisations of D are the 2^ν vertices of a ν-cube whose ν·2^(ν−1) edges are the generisations through exactly one vertex, incidence being specialisation — whereas a straight line through ν vertices of a line arrangement has only 2ν stable… Our intake: new to us: our package for this cote is waiting
context/STATEMENTS_WITH_STATUS.md:14:| STRATA C.2 | B(E^op) maps by a specified endpoint-compatible weak equivalence to the holink from BB into BX minus BB, whose open stratum retracts to BA. | claim (return: Known) | known; The simplicial identification `Map_{Δ[1]}(Δ[1], N(X^op)) = N(E^op)` is an equality; the theorem of Douteau–Waas opened; the retraction of `BX ∖ BB` onto `BA` checked (the coordinates sum to 1). |
context/STATEMENTS_WITH_STATUS.md:29:| STRATA F.9 | Filling punctures and stabilizing define actual forgetful functors | claim (return: Proved) | proved in outline; `φ(Δ_σ) ⊂ Δ_{qσ}` and the typing of arrows followed; the comparison with the geometric map is argued briefly and I did not check it beyond that. |
context/STATEMENTS_WITH_STATUS.md:31:| STRATA F.11 | Forgetting a marking is always W-infinity-smooth | claim (return: Refuted) | proved; Recomputed: the lifting groupoid is the action groupoid of `K = ker φ` on `KΔ_x/Δ_x`, with stabilizer `K ∩ Δ_x = ⟨t_1 t_2^{-1}⟩ ≅ Z`. |
context/Esquisse_cote119_copy1_API_transcription.tex:1010:ses spécialisations sur des corps de base arbitraires $k$ (via
context/Esquisse_cote119_copy1_API_transcription.tex:1099:décrire en disant que lorsqu'on regarde la spécialisation du po-%
context/Esquisse_cote119_copy1_API_transcription.tex:1107:on voit par des arguments de spécialisation standards.
context/Esquisse_cote119_copy1_API_transcription.tex:1163:haut, pour les spécialisations d'un polyèdre donné, sont celles pour
context/Esquisse_cote119_copy1_API_transcription.tex:1206:de phénomènes de ``degénérescence'' (ou de ``spécialisation'') - les
```

## Q10 — Local elementary-sweep statements

- Search timestamp: 2026-11-15 01:54:05 UTC.
- Command: `rg -n -i -- "balayage|sweep|p.r. critique|critical.*position" context`.
- Results: 1 matching lines in the supplied context.
- Search status: matches recorded below; their status and relevance must be assessed separately in the corresponding candidate note. None is automatically treated as reviewed.

```text
context/Esquisse_cote119_copy1_API_transcription.tex:2154:\uline{mentaires} et leurs inverses, savoir le ``\uline{balayage}'' d'une branche
```

## Q11 — Cycle indices and unequal terminal exponents

- Search timestamp: 2026-11-15 01:54:36 UTC.
- Command: `rg -n -i -- "zeta_0|xi_0|ζ|ξ|u\\^\\{?2n|u\\^\\{?n|cyclic.*order|cyclic.*index" context`.
- Results: 1 matching lines.
```text
context/STATEMENTS_WITH_STATUS.md:68:| RESIDUE H.7 | The program \path{code/GHIJ/finite_poset_direct_image.py} independently enumerates all maps between one representative of every poset isomorphism class with at most five objects, including the empty poset. The counts of posets of sizes $0,1,2,3,4,5$ are $1,1,2,5,16,63$. It examines $1,349,916$ monotone maps and recognizes $96,372$ proper maps. Properness is certified by explicit simplicial collapses of every nonempty outgoing lifting order complex; noncontractible cases are rejected by homology over $\mathbb Q$ or $\mathbb F_2$. The program aborts rather than classifying an acyclic but uncertified complex as contractible. No such undecided case occurs in this range. For every proper map and every nonempty target simplex, it computes the categorical stalk and the actual geometric-fibre cellular cohomology, for the constant coefficient and for each principal-cosieve indicator. This gives $5,536,094$ stalk/coefficient cases, each computed over both $\mathbb Q$ and $\mathbb F_2$, with no discrepancy. A fibre cell is indexed by a source chain meeting each level of the target simplex; it is a product of simplices, of dimension $\|\kappa\|-\|\sigma\|$. Its signed boundary deletes one vertex while keeping every level nonempty, using the product-boundary sign. The code verifies that consecutive boundary matrices multiply to zero. Exact rational ranks use integer elimination with gcd reduction, and binary ranks use bit arithmetic. For a principal cosieve, extension from the corresponding closed subcomplex reduces both computations to its intersection with the relevant fibre or lower inverse image. The supplied per-map CSV records all tests as successful; the JSON gives the totals by source and target size. These numerical comparisons check cohomology, not a replacement proof of the canonical mate; the latter is established in H.1. | claim (return: Proved) | no review |
```

## Match assessment and follow-up source reads

Assessment completed by 2026-11-15 01:58:49 UTC. The context excerpts listed below were read before writing the associated notes, then page markers were mechanically checked; the individual search timestamps above record the actual prior searches.

- API Esquisse 119/12–13: lines 500–545 (page markers 489 and 533), for U02, U03, U08, W01, W03.
- API Esquisse 119/50: lines 2180–2230, with scan119/50 at 2208, for U08, Q01 and the broader pseudoline project.
- API Esquisse 119/28:1210–1234 for the unrelated 1982 match; 119/15:628–638 and 119/23:1009–1023 for unrelated facet/polygon hits.
- API Esquisse 119/48–49:2130–2170, for Q10; scan markers at 2117 and 2163.
- All search excerpts, including the broad Q06 hits, were read from this log before completing the memo. No referenced external source file was treated as supplied or read.

| Candidate | Assessed result, relevance, status, and absence |
|---|---|
| D01 | Direct documentary match: README.md:9 gives the selected range; Hua 154-generisation-cube, RESULTS_STATE.md:122, gives marginal p153/scan154. Hua is an unsearched conjecture with no verdict; the pagination mapping is a separate mechanical observation. |
| D02 | No matching entry or text for the date/title. Absence is limited to supplied context. |
| D03 | The sole 1982 hit is unrelated: API Esquisse 119/28:1223–1224 dates reflections on stratified structures, not computing paper. No matching entry for the printout dates. |
| D04 | README.md:9,16 supplies catalogue metadata; Hua concerns the cube. No matching entry for the local headings or a selected title page. |
| U01 | No matching entry for inverse-circuit reversal. The answer is read directly in frozen scan133:137. |
| U02 | API Esquisse 119/12–13:517–542 is a direct operator-background match, not eye-checked and with no result-register ID. No context resolution of the local geometric task. |
| U03 | Same API cartographic formulas only; no matching entry interpreting the joint quotient. |
| U04 | No matching circuit-closure entry. |
| U05 | EXIT_ONE_TYPE P4e is an unreviewed return claim; R121-08 is a first-pass returned-note lead; Hua is an unsearched conjecture. None matches the endpoint-number doubt. Their external source files were not read. |
| U06 | MPL_150_044-084 N18 and Q2 are first-pass notes concerning attachments/choices, not this blocking construction. Their named source file was not read. No exact matching entry. |
| U07 | Hua 154-generisation-cube matches the same source page but concerns generizations and has no verdict. No answer to the universal principal-specialization question. |
| U08 | API Esquisse 119/12–13 and 119/50 supply repère and relative-position background only; no matching completion of the displayed map. |
| W01 | API Esquisse gives the sigma algebra; no matching entry for the rejected inverse guess. |
| W02 | All hits use principale(s) in unrelated prose; no matching technical-condition entry. |
| W03 | API Esquisse cartographic relations are background only. BISITE G.10, STRATA F.9/F.10, RESIDUE H.1/H.3 and another Esquisse sigma presentation are different objects; no exact four-repère example. |
| W04 | No matching entry for these orientation repairs. |
| W05 | No matching fuseau/couloir nomenclature entry. |
| W06 | STRATA F.9/F.11 use phi in different constructions; API Esquisse facets at 119/15:634 and 119/23:1015 are unrelated. No matching correction formula. |
| W07 | No matching entry for the canceled exceptional-facet geometric prescriptions. |
| W08 | MPL_148_029-072 R39 is a first-pass lead for a different canceled skeleton description at 148/067. No matching entry for these trial diagrams; named source file not read. |
| W09 | No matching entry for either local wording revision. |
| W10 | Generic 1-complex passages in API Esquisse only; no matching K,L condition list. |
| Q01 | Direct exact entry: Hua 154-generisation-cube, RESULTS_STATE.md:122, unsearched conjecture/statement with no verdict, cote154 marginal153/scan154. API Esquisse 119/50:2211–2223 is broader unverified background. |
| Q02 | Hua is the direct comparison, with unsearched/no-verdict status. Its unqualified exponent and straight-line paraphrase are not a correction authority. API Esquisse 119/23:1020 is an unrelated regular polygon. |
| Q03 | No matching disconnectedness-note entry. |
| Q04 | No matching fuseau-bijection entry. |
| Q05 | No matching dual-projective-plane orientation-sign entry. |
| Q06 | Broad words produced generic cellular, equivalence, and multiplicity hits, including independent register statements. None states the K,L conditions or face-sum formula. No matching entry; no register result is used to complete or refute it. |
| Q07 | API Esquisse 119/18:791 and 119/25:1117 contain a genus inequality and unrelated variables respectively; neither matches the calculation. No matching entry. |
| Q08 | No matching counting-expression entry. |
| Q09 | Hua is related by specialization vocabulary only. The LM7_PUSH E.65 character-Delta chain is explicitly refereed, but belongs to a different object; STRATA Delta expressions and API Esquisse specialization prose also do not identify this diagram. No exact matching entry. |
| Q10 | API Esquisse 119/48–49:2139–2168 is a direct thematic match about elementary sweeps, not eye-checked and not a proof of the criticality captions. No matching result-register entry. |
| Q11 | Only RESIDUE H.7, explicitly no review, matched a broad mathematical pattern; it is a different finite-poset enumeration. No matching cyclic-sequence entry. |

## Mechanical scope checks

- Every one of the 50 frozen page files was searched for question marks, explicit hesitation/deferred-work terms, and revision markers; non-diagram prose and the substantive prose labels inside diagram code were read. No images were opened.
- There are 33 unique candidate IDs: D01–D04, U01–U08, W01–W10, Q01–Q11; all 33 have an earlier search block and an assessed status.
- The source scanpage/mspage mapping was checked for all 50 files: scan127–176 maps continuously to marginal126–175, one mspage marker each.
- Date-like matches in drawing coordinates at scan130:83 and scan131:20 were inspected as code and excluded; no calendar reading was inferred from them. Printed date-code fields were not converted.
- The final candidate memo contains 33 compact entries plus a documentary date inventory. Its classification deliberately distinguishes answered questions, explicit questions, incomplete formulations, canceled material, declarative assertions without a local proof, and uncertain readings.
