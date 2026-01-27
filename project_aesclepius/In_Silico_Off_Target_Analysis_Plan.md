# Project AESCLEPIUS: In-Silico Off-Target Analysis Plan

## Document Version: 1.0
## Date: 2026-01-27
## Author: Dr. Gemini

---

## 1.0 Objective

To computationally predict and quantify the potential for off-target cleavage events by the LTR-A and LTR-B gRNA/Cas9 complexes within the latest assembly of the human genome (GRCh38/hg38). The primary goal is to generate a comprehensive risk profile for each gRNA candidate before proceeding to *in vitro* validation.

## 2.0 Methodology

This analysis will employ a multi-tiered computational approach, combining exhaustive search algorithms with sophisticated scoring models to identify and rank potential off-target sites (POTS).

-   **Primary Search Tool:** `Cas-OFFinder`, an open-source tool designed for rapid and flexible identification of POTS with a specified number of mismatches.
-   **Scoring Algorithm:** The Cutting Frequency Determination (CFD) score will be used to estimate the cleavage efficiency at each identified POTS. The CFD score accounts for the position and identity of mismatches between the gRNA and the DNA target, providing a more accurate prediction of off-target activity than simple mismatch counting.
-   **Reference Genome:** The human reference genome assembly GRCh38/hg38 will be used as the search space.

## 3.0 Input Data

-   **gRNA Sequence 1 (LTR-A):** `TGGGAGCTCTCTGGCTAACT`
-   **gRNA Sequence 2 (LTR-B):** `GCTGACATCGAGCTTTGCTA`
-   **PAM Sequence:** `NGG` (for *S. pyogenes* Cas9)

## 4.0 Analysis Protocol

1.  **Exhaustive Genome-Wide Search:**
    -   `Cas-OFFinder` will be run for each gRNA against the GRCh38/hg38 genome.
    -   The search will be configured to allow for up to **4 mismatches** between the gRNA and the genomic DNA sequence. This provides a highly sensitive screen for potential binding sites.

2.  **Scoring of Potential Off-Target Sites (POTS):**
    -   The complete list of POTS generated in Step 1 will be processed.
    -   The CFD score will be calculated for each POTS. The score ranges from 0 to 1, where 1 indicates a cleavage likelihood equal to the on-target site.

3.  **Genomic Annotation:**
    -   All POTS with a CFD score > 0.05 will be annotated using the Ensembl Variant Effect Predictor (VEP) or a similar tool.
    -   Annotation will determine the location of each POTS relative to critical genomic features, including:
        -   Exons (protein-coding regions)
        -   Introns
        -   Promoter regions
        -   Enhancers
        -   Known oncogenes or tumor suppressor genes.

## 5.0 Risk Assessment & Deliverable

A final report will be generated containing a ranked list of all identified POTS. The list will be prioritized based on the CFD score. Any POTS that meets the following criteria will be flagged as **High-Risk** and will necessitate re-evaluation of the gRNA design:

-   **Criterion 1:** A CFD score > 0.1.
-   **Criterion 2:** The site is located within an exon of a protein-coding gene.
-   **Criterion 3:** The site is located within a known cancer-related gene (e.g., from the COSMIC database).

The final deliverable will be this ranked and annotated list, which will serve as the basis for a go/no-go decision for the *in vitro* testing phase.