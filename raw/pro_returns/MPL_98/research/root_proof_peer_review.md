# Focused peer review of the root proof checks

**Run:** MPL98. **Reviewer:** ChatGPT GPT-6 Astra Pro; effort inherited/unspecified; agent `/root/norm_research`. **Record prepared:** 2026-11-18 02:46:57 UTC. The mathematical review occurred immediately before the parent's request to save this record; individual check times were not captured separately.

## Scope and evidence

Read the complete research drafts `root_proof_checks.md` and `standing_sections.md` in bounded text chunks. The assignment was a focused check for substantive mathematical errors or missing hypotheses, not a new literature search or a manuscript audit. No manuscript images, page transcriptions, or combined transcription were inspected. Root-reported source readings and inventory statements were treated as supplied data, without certifying their ink or provenance.

Two mathematical qualifications and one identifier correction were reported. The parent subsequently reported that all three had been applied. This memorandum records the completed review and that reported disposition; the corrected files were not reread, in accordance with the instruction to document the work without further review.

## B15: the scope of Hom base change after stratification

The kernel argument is valid for a finitely presented module once the indicated flatness hypotheses hold over the parameter ring. A necessary clarification concerns the starting family on a locally closed stratum: first restrict the family to that stratum and compute its Hom module; the argument then proves that this Hom commutes with further base change from the stratum. Flatness of the restricted modules alone does not identify it with the restriction of the original global Hom module.

The distinction was checked by the example
\[
A=k[t],\qquad M=A/(t),\qquad N=A.
\]
The presentation of \(M\) gives multiplication by \(t\) on \(N\), whose kernel is zero. Thus \(\operatorname{Hom}_A(M,N)=0\). After restriction to \(t=0\), the map is zero on \(k\), and the newly computed Hom is \(k\). Both the restricted \(N\) and the restricted cokernel are flat over \(k\). Therefore their flatness does not repair the comparison from the original zero Hom module. The recommendation was to state explicitly that Hom is recomputed after restriction and that the resulting assertion concerns subsequent base changes. **Disposition:** parent reports this clarification applied.

## T07: coefficient columns and the left kernel

The rank-nullity repair is correct when the coefficient matrix is oriented explicitly. Put
\[
C_{ij}=\text{coefficient of the \(j\)-th monomial in }f_i,
\qquad \lambda\in K^{n+1}.
\]
A prefix of coefficient conditions imposes \(\lambda^{\mathsf T}C_{\mathrm{prefix}}=0\). The solution space is the left kernel, of dimension \((n+1)-\operatorname{rank}(C_{\mathrm{prefix}})\). At the first prefix of rank \(n+1\), this space is zero; the preceding prefix has rank \(n\), because adjoining one column raises rank by at most one, and therefore has a one-dimensional left kernel. Calling this simply a kernel while adjoining columns could instead be read as changing the number of column variables. The recommendation was to specify the left kernel or transpose the coefficient matrix. **Disposition:** parent reports the orientation clarified.

## T14 and the remaining checks

The positive gluing argument is valid with full compatibility of the pairwise identifications, including the condition preventing additional identifications within a piece, and with either all overlaps open in both pieces or all overlaps closed in both pieces. The saturation argument then supplies the corresponding open or closed sets in the quotient and proves that each piece is embedded. The finite negative example in T13 is compatible with this result: its quotient has opens \(\varnothing,\{b\},\{b,c\},\{a,b,c\}\), so its trace on the discrete piece \(\{a,b\}\) omits \(\{a\}\). The interval argument uses bounded closed subsets of \([0,1]\), whose integral translates form a locally finite closed family. The positive-gluing heading still used T03 during review; **the parent reports its correction to T14**. T03 now refers to the product assertions.

No further substantive error was found in the reviewed arguments under their stated or cross-referenced hypotheses. This includes N04 and N15; the examples and mechanisms B11–B13, B15, B25, B30–B31; and T02–T09, T11–T14 as applicable. In particular, the norm linearization, inseparable-support example, varying primary component, quotient-subspace criterion, Picard-zero pullback inference, and coefficient-flag argument were mathematically consistent. The canonicity argument for Ext was checked conditional on the resolution and flatness hypotheses to which that paragraph expressly refers; this review did not reopen the earlier Ext memorandum.

`standing_sections.md` contained no substantive mathematical issue found in this review. It distinguishes supplied register statuses, selected mathematical checks, uncertainty in source readings, and the absence of an established typescript author or edition. Its inventory and transcription claims were not independently audited.

## Changes and limitations

The reviewer made no changes to either reviewed file. Only this memorandum and its companion event TSV were written on the final documentation request. No new web search, formal verification, or computational certificate was performed for this focused review. The event dates record the actual UTC date of the checks; the preparation timestamp above is not represented as the exact time of each individual check.

