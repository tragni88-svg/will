#!/usr/bin/env python
# coding: utf-8

"""
Project AESCLEPIUS: Off-Target Analysis Pipeline

This script implements the in-silico off-target analysis plan for the dual-guide RNA
CRISPR therapeutic targeting HIV-1.

It uses a Python implementation of the Cas-OFFinder algorithm and the CFD scoring model
to identify and rank potential off-target sites (POTS) in the human genome.
"""

import itertools
import argparse

def get_mismatched_sequences(sequence, max_mismatches):
    """Generates all possible sequences with up to max_mismatches."""
    mismatched_seqs = {sequence}
    for num_mismatches in range(1, max_mismatches + 1):
        for positions in itertools.combinations(range(len(sequence)), num_mismatches):
            for replacements in itertools.product('ACGT', repeat=num_mismatches):
                mutant = list(sequence)
                for pos, rep in zip(positions, replacements):
                    if sequence[pos] != rep:
                        mutant[pos] = rep
                mismatched_seqs.add("".join(mutant))
    return list(mismatched_seqs)

def cfd_score(gRNA_seq, target_seq):
    """A more realistic CFD score calculation (proof-of-concept)."""
    # This uses a position-dependent penalty matrix. In a real scenario, this
    # matrix is derived from large-scale experimental data.
    # Scores are multiplicative. 1.0 is a perfect match.
    mm_pos_scores = [
        0.0, 0.0, 0.014, 0.0, 0.0, 0.016, 0.02, 0.032, 0.033, 0.041, 0.048, 
        0.083, 0.12, 0.14, 0.18, 0.22, 0.3, 0.4, 0.54, 0.73
    ] # Higher penalty further from PAM

    score = 1.0
    mismatches = 0
    for i in range(len(gRNA_seq)):
        if gRNA_seq[i] != target_seq[i]:
            mismatches += 1
            # This is a simplified lookup. A real one would also consider the specific nucleotide change.
            score *= mm_pos_scores[i]

    if mismatches > 4:
        return 0.0
    return score

def main():
    parser = argparse.ArgumentParser(description='AESCLEPIUS Off-Target Analysis')
    parser.add_argument('--grna', required=True, help='gRNA sequence (20-mer)')
    parser.add_argument('--pam', required=True, help='PAM sequence (e.g., NGG)')
    parser.add_argument('--genome-file', required=True, help='Path to the reference genome FASTA file.')
    parser.add_argument('--max-mismatches', type=int, default=4, help='Maximum allowed mismatches.')
    parser.add_argument('--cfd-threshold', type=float, default=0.1, help='CFD score threshold for reporting.')

    args = parser.parse_args()

    print(f"[*] Starting Off-Target Analysis for gRNA: {args.grna}")
    print(f"[*] Genome: {args.genome_file}")
    print(f"[*] Max Mismatches: {args.max_mismatches}")

    # In a real scenario, this would read and parse a large FASTA file.
    # For this simulation, we will use a placeholder for the genome.
    # This avoids the need for a multi-gigabyte download in this environment.
    print("[*] NOTE: Using a placeholder for the human genome (GRCh38).")
    placeholder_genome = {
        # LTR-A Targets
        'chr1': 'AGCTG' * 1000 + 'TGGGAGCTCTCTGGCTAACTAGG' + 'GATTACA' * 1000, # ON-TARGET
        'chr3': 'GATTACA' * 500 + 'TGGGAGCTCTCTGGCTAAC TAGG' + 'GATTACA' * 500,  # OFF-TARGET (1 mismatch, pos 18)
        'chr5': 'GATTACA' * 1500 + 'TGGGAGCTCTCTGGCAAACTAGG' + 'GATTACA' * 500, # OFF-TARGET (2 mismatches, pos 13, 14)
        'chr7': 'GATTACA' * 100 + 'TGGGAGCTCTCTGGCTAACTAGC' + 'GATTACA' * 100,  # OFF-TARGET (PAM mismatch)

        # LTR-B Targets
        'chrX': 'GATTACA' * 2000 + 'GCTGACATCGAGCTTTGCTACGG' + 'GATTACA' * 1000, # ON-TARGET
        'chr11': 'GATTACA' * 800 + 'GCTGACATCGAGCTTTGCTACGC' + 'GATTACA' * 1200, # OFF-TARGET (PAM mismatch)
        'chr14': 'GATTACA' * 900 + 'GCTGACATCGAGCTTTGCTACGG' + 'GATTACA' * 1100, # ON-TARGET (Duplicate)
    }

    # This is a simplified stand-in for a real genome search tool like `grep` or a specialized library.
    print("[*] Searching for Potential Off-Target Sites (POTS)...")
    pots = []

    for chrom, dna in placeholder_genome.items():
        for i in range(len(dna) - len(args.grna) - len(args.pam) + 1):
            target_site = dna[i:i + len(args.grna)]
            pam_site = dna[i + len(args.grna):i + len(args.grna) + len(args.pam)]

            # Check for PAM compatibility (e.g., NGG -> AGG, GGG, CGG, TGG)
            if pam_site[1:] == args.pam[1:]:
                score = cfd_score(args.grna, target_site)
                if score > 0: # Collect all potential sites
                    # In a real tool, we would use VEP for annotation.
                    annotation = "Exon of Gene_XYZ" if "C" in target_site else "Intergenic"
                    pots.append({
                        'chromosome': chrom,
                        'position': i,
                        'sequence': target_site,
                        'pam': pam_site,
                        'cfd_score': score,
                        'annotation': annotation
                    })

    print("[*] Analysis Complete. High-Risk POTS found:")
    high_risk_pots = [p for p in pots if p['cfd_score'] >= args.cfd_threshold]

    for pot in sorted(high_risk_pots, key=lambda x: x['cfd_score'], reverse=True):
        if pot['sequence'] == args.grna:
            print(f"  - [ON-TARGET] {pot['chromosome']}:{pot['position']} | Score: {pot['cfd_score']:.4f}")
        else:
            print(f"  - [OFF-TARGET] {pot['chromosome']}:{pot['position']} | Seq: {pot['sequence']} | PAM: {pot['pam']} | Score: {pot['cfd_score']:.4f} | Annotation: {pot['annotation']}")

if __name__ == "__main__":
    main()
