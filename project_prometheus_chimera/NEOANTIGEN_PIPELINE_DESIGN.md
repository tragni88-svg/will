# Project Chimera: Neoantigen Discovery Pipeline Design

## 1. Overview

This document specifies the architecture for the automated computational pipeline to identify patient-specific, therapeutically actionable neoantigens for personalized mRNA vaccines.

**Input:** Raw FASTQ files from paired tumor/normal whole-exome sequencing.
**Output:** A ranked list of peptide sequences for vaccine inclusion.

## 2. Pipeline Stages

The pipeline consists of five distinct computational stages:

### Stage 1: Somatic Mutation Calling

*   **Objective:** To identify all genetic mutations unique to the tumor.
*   **Steps:**
    1.  **Alignment:** Align tumor and normal sequencing reads to the GRCh38 human reference genome using the BWA-MEM algorithm.
    2.  **Duplicate Removal:** Mark and remove PCR duplicates using GATK's MarkDuplicates.
    3.  **Somatic Variant Calling:** Use a consensus-based approach with three independent callers:
        *   **MuTect2:** For high-sensitivity detection of single nucleotide variants (SNVs) and small insertions/deletions (indels).
        *   **VarScan2:** For robust performance in variable tumor purity.
        *   **Strelka2:** For high-specificity calling.
    4.  **Consensus Filtering:** A variant is carried forward only if it is called by at least two of the three callers. The final output is a high-confidence VCF (Variant Call Format) file.

### Stage 2: HLA Typing

*   **Objective:** To determine the patient's specific Human Leukocyte Antigen (HLA) alleles, which govern how peptides are presented to the immune system.
*   **Steps:**
    1.  **HLA Allele Prediction:** Use the OptiType algorithm on the normal sequencing data to predict the patient's Class I HLA-A, HLA-B, and HLA-C alleles with high accuracy.
    2.  **Output:** A list of the patient's six Class I HLA alleles (e.g., A*02:01, A*03:01, B*07:02, B*44:02, C*04:01, C*07:02).

### Stage 3: In-Silico Translation & Peptide Generation

*   **Objective:** To generate all possible peptide sequences resulting from the tumor's mutations.
*   **Steps:**
    1.  **Variant Annotation:** Use the Ensembl Variant Effect Predictor (VEP) to annotate the somatic mutations from the VCF file.
    2.  **Peptide Generation:** For each non-synonymous mutation, generate all possible 8, 9, 10, and 11-amino-acid-long peptide sequences (k-mers) centered on the mutated amino acid.

### Stage 4: Peptide-MHC Binding Prediction

*   **Objective:** To predict which of the generated peptides will bind effectively to the patient's HLA alleles.
*   **Steps:**
    1.  **Binding Affinity Prediction:** Use the NetMHCpan-4.1 deep learning model. For each peptide and each of the patient's HLA alleles, predict the binding affinity (IC50 nM).
    2.  **Filtering:** A peptide is considered a 'binder' if it has a predicted IC50 < 500 nM. Strong binders are those with IC50 < 50 nM.

### Stage 5: Immunogenicity & Target Prioritization

*   **Objective:** To rank the binding peptides by their likelihood of provoking a powerful T-cell response.
*   **Steps:**
    1.  **Immunogenicity Score:** Calculate an immunogenicity score for each peptide-HLA pair. This score will be a weighted function of:
        *   **Binding Affinity:** (From Stage 4). Stronger binding is better.
        *   **Tumor Expression:** The expression level of the gene containing the mutation (measured from tumor RNA-seq data, if available).
        *   **Foreignness:** A score measuring how different the mutated peptide is from any corresponding normal human peptide (to minimize risk of autoimmunity).
    2.  **Final Ranking:** Generate a final, ranked list of the top 20 neoantigen candidates. This list is the direct input for the mRNA vaccine manufacturing process.

## 3. Implementation

The entire pipeline will be containerized using Docker and orchestrated using Nextflow for scalability, reproducibility, and deployment on high-performance computing clusters.
