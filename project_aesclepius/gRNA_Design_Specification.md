# Project AESCLEPIUS: gRNA Design Specification

## Document Version: 1.0
## Date: 2026-01-27
## Author: Dr. Gemini

---

## 1.0 Introduction

This document specifies the design of the dual guide RNA (gRNA) sequences for the CRISPR-Cas9 based therapeutic intervention targeting HIV-1. These sequences are engineered to direct the *Streptococcus pyogenes* Cas9 (SpCas9) nuclease to the 5' and 3' Long Terminal Repeats (LTRs) of the integrated HIV-1 provirus. The objective is the complete and irreversible excision of the viral genome from infected host cells.

## 2.0 gRNA Design Rationale

The selection of gRNA target sites is the most critical parameter for the success of the therapy. The following principles were applied:

-   **Conservation:** Targets were selected within the most highly conserved regions of the LTR across major HIV-1 clades to ensure broad applicability.
-   **Functional Importance:** Targets are located within functionally critical regions of the viral promoter (U3) and downstream elements (U5), reducing the probability of viable escape mutants.
-   **PAM Availability:** Sequences are immediately upstream of a canonical SpCas9 Protospacer Adjacent Motif (PAM) sequence (NGG).
-   **Dual-Guide Strategy:** A two-gRNA approach ensures the excision of the entire ~9.7kb proviral DNA, as opposed to single-gRNA strategies which risk creating smaller, potentially functional, deletions or insertions (indels).

## 3.0 Final gRNA Sequences

### 3.1 gRNA-LTR-5' (Targeting the 5' LTR)

This gRNA targets the U3 region of the LTR, which functions as the viral promoter. This site is critical for viral gene expression.

-   **Target Name:** LTR-A
-   **Target Region:** U3 (Promoter/Enhancer Region)
-   **Target DNA Sequence (20-mer):** `TGGGAGCTCTCTGGCTAACT`
-   **PAM Sequence:** `AGG`
-   **Full Target Site:** `TGGGAGCTCTCTGGCTAACTAGG`
-   **Rationale:** This sequence is highly conserved and located near essential transcription factor binding sites, making it an excellent candidate for high-efficacy cleavage.

### 3.2 gRNA-LTR-3' (Targeting the 3' LTR)

This gRNA targets the U5 region of the LTR. A cut at this location, combined with the 5' cut, ensures the complete removal of the provirus.

-   **Target Name:** LTR-B
-   **Target Region:** U5
-   **Target DNA Sequence (20-mer):** `GCTGACATCGAGCTTTGCTA`
-   **PAM Sequence:** `CGG`
-   **Full Target Site:** `GCTGACATCGAGCTTTGCTACGG`
-   **Rationale:** This target is situated in a conserved portion of the U5 region. Its selection provides the necessary second cut site for full proviral excision while being spatially distinct from the 5' target.

## 4.0 Next Steps

The designed gRNA sequences will now proceed to in-silico (computational) validation to predict on-target efficacy and, most importantly, to perform a genome-wide scan for potential off-target binding sites in the human genome.
