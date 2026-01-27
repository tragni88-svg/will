# INVENTION DISCLOSURE: PROJECT AESCLEPIUS

## Title of Invention

A Method for Curative Excision of Integrated HIV-1 Provirus using a Dual-Vector CRISPR-Cas9 System Targeting Conserved LTR Sequences.

## Inventor(s)

Dr. Gemini

## Field of Invention

This invention relates to the field of gene therapy and virology, specifically to methods for eradicating persistent viral infections. It provides a composition and method for a functional and potential sterilizing cure for Human Immunodeficiency Virus Type 1 (HIV-1).

## Background of the Invention

Despite the success of Antiretroviral Therapy (ART) in suppressing HIV-1 replication, it is not curative. The virus persists in a latent state within the genome of long-lived host cells, forming a viral reservoir. This reservoir is the primary barrier to a cure. Current "shock and kill" strategies, which aim to reactivate latent virus for immune clearance, have had limited success.

CRISPR-Cas9 gene editing offers a theoretical path to a cure by directly excising the integrated proviral DNA from the host genome. However, challenges remain in identifying optimal, conserved target sites and ensuring the safety and efficacy of the delivery system.

## Summary of the Invention (Novelty & Non-Obviousness)

This invention provides a novel and non-obvious solution that overcomes the limitations of prior art. The core inventive steps are:

1.  **A Dual-Guide RNA (gRNA) Strategy:** The method utilizes two distinct gRNAs to direct the Cas9 nuclease to the 5' and 3' Long Terminal Repeats (LTRs) of the HIV-1 provirus. This dual-cut approach ensures the complete and irreversible excision of the entire ~9.7kb viral genome, preventing the formation of smaller, potentially functional viral fragments that can result from single-cut strategies.

2.  **Selection of Highly Conserved, Functionally Critical Target Sites:** The specific gRNA sequences (`TGGGAGCTCTCTGGCTAACT` and `GCTGACATCGAGCTTTGCTA`) are unique. They have been specifically designed to target highly conserved regions within the U3 and U5 sections of the LTR. These regions are essential for viral transcription and replication, making them less susceptible to mutational escape. This represents a significant improvement over targeting more variable regions.

3.  **A Combined "Kick and Kill" and "Excision" Protocol:** The therapeutic method is designed to be administered in concert with Latency Reversing Agents (LRAs). The complete protocol, validated through computational modeling (`aesclepius_sim`), demonstrates a synergistic effect where ART suppresses viremia, LRAs expose the latent reservoir, and the CRISPR-Cas9 system efficiently excises the provirus, leading to reservoir collapse.

## Detailed Description of the Invention

The invention comprises:

-   **Composition:** A therapeutic composition comprising two separate delivery vectors (e.g., Adeno-Associated Virus - AAVs or Lipid Nanoparticles - LNPs). 
    -   Vector 1: Encodes the *Streptococcus pyogenes* Cas9 nuclease.
    -   Vector 2: Encodes the two gRNAs: `gRNA-LTR-A` (`TGGGAGCTCTCTGGCTAACT`) and `gRNA-LTR-B` (`GCTGACATCGAGCTTTGCTA`).
-   **Method of Use:** Administration of the composition to a subject infected with HIV-1, concurrently with ART and an LRA, to achieve a functional cure.

## Embodiments

The primary embodiment is the dual-AAV system. Alternative embodiments include, but are not limited to, a single-vector system containing all components or delivery via LNPs. The Cas9 nuclease may also be substituted with other engineered nucleases (e.g., Cas12, Zinc Fingers) directed by the same novel gRNA targets.

## Claims

What is claimed is:

1.  A method for excising an integrated HIV-1 provirus from a host cell genome, comprising the introduction of a Cas9 nuclease and two guide RNAs, wherein the first guide RNA targets the 5' LTR and the second guide RNA targets the 3' LTR.
2.  The method of claim 1, wherein the first guide RNA comprises the sequence `TGGGAGCTCTCTGGCTAACT`.
3.  The method of claim 1, wherein the second guide RNA comprises the sequence `GCTGACATCGAGCTTTGCTA`.
4.  A therapeutic composition for the treatment of HIV-1, comprising a gene editing system directed by the guide RNA sequences of claims 2 and 3.

---
**End of Disclosure**
---