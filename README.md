# OAS_wrapper
A wrapper to parse Observed Antibody Space (OAS) data for better visualization, annotation and comparison of sequence to germline.

## Functionalities

The scripts include functionalities to:
1. Provide basic metrics and visualizations of sequences and their annotations
2. Provide original IMGT sequences for V, D and J calls made in OAS data using IMGT reference database
3. Align sequence and germline to highlight regions of mismatches, providing positional information e.g.,  
```
Example Output:
Original Sequence 1: GAGGTGCAGCTGTTGGAGTCTGGGGGAGGCTTAGTACAGCCTGGGGGGTCCCTGAGACTCTCCTGTGTAGCCTCTGGATTCACCTTTAGCAGCTATGCCATGAGCTGGGTCCGCCAGGCTCCAGGGAAGGGGCTGGAGTGGGTCTCAGGTATTAGTGCTAGTGGTGCTAGCACATACTACGCAGACTCCGTGAAGGGCCGGTTCACCATCTCCAGAGACAATTCCAAGAACACGCTGTATCTGCAAATGAACAGCCTGAGAGCCGAGGACACGGCCGTATATTACTGTGCGAAAACCCCCAAATACGATGTTTGGAGTGGTTATTATACGTCCAATGCCTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAG
Original Sequence 2: GAGGTGCAGCTGTTGGAGTCTGGGGGAGGCTTGGTACAGCCTGGGGGGTCCCTGAGACTCTCCTGTGCAGCCTCTGGATTCACCTTTAGCAGCTATGCCATGAGCTGGGTCCGCCAGGCTCCAGGGAAGGGGCTGGAGTGGGTCTCAGCTATTAGTGGTAGTGGTGGTAGCACATACTACGCAGACTCCGTGAAGGGCCGGTTCACCATCTCCAGAGACAATTCCAAGAACACGCTGTATCTGCAAATGAACAGCCTGAGAGCCGAGGACACGGCCGTATATTACTGTGCGAAANNNNNNNNNTACGATTTTTGGAGTGGTTATTATACNNNNNATGCTTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAG
Aligned and Highlighted Differences:
GAGGTGCAGCTGTTGGAGTCTGGGGGAGGCTT[31mA[0mGTACAGCCTGGGGGGTCCCTGAGACTCTCCTGTG[31mT[0mAGCCTCTGGATTCACCTTTAGCAGCTATGCCATGAGCTGGGTCCGCCAGGCTCCAGGGAAGGGGCTGGAGTGGGTCTCAG[31mG[0mTATTAGTG[31mC[0mTAGTGGTG[31mC[0mTAGCACATACTACGCAGACTCCGTGAAGGGCCGGTTCACCATCTCCAGAGACAATTCCAAGAACACGCTGTATCTGCAAATGAACAGCCTGAGAGCCGAGGACACGGCCGTATATTACTGTGCGAAA[31mA[0m[31mC[0m[31mC[0m[31mC[0m[31mC[0m[31mC[0m[31mA[0m[31mA[0m[31mA[0mTACGAT[31mG[0mTTTGGAGTGGTTATTATAC[31mG[0m[31mT[0m[31mC[0m[31mC[0m[31mA[0mATGC[31mC[0mTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAG
GAGGTGCAGCTGTTGGAGTCTGGGGGAGGCTT[31mG[0mGTACAGCCTGGGGGGTCCCTGAGACTCTCCTGTG[31mC[0mAGCCTCTGGATTCACCTTTAGCAGCTATGCCATGAGCTGGGTCCGCCAGGCTCCAGGGAAGGGGCTGGAGTGGGTCTCAG[31mC[0mTATTAGTG[31mG[0mTAGTGGTG[31mG[0mTAGCACATACTACGCAGACTCCGTGAAGGGCCGGTTCACCATCTCCAGAGACAATTCCAAGAACACGCTGTATCTGCAAATGAACAGCCTGAGAGCCGAGGACACGGCCGTATATTACTGTGCGAAA[31mN[0m[31mN[0m[31mN[0m[31mN[0m[31mN[0m[31mN[0m[31mN[0m[31mN[0m[31mN[0mTACGAT[31mT[0mTTTGGAGTGGTTATTATAC[31mN[0m[31mN[0m[31mN[0m[31mN[0m[31mN[0mATGC[31mT[0mTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAG
Indices of Differences: [32, 67, 148, 157, 166, 294, 295, 296, 297, 298, 299, 300, 301, 302, 309, 329, 330, 331, 332, 333, 338]
--------------------------------------------------

```
5. Group data by germline, to infer sequences that originate from germline, including providing information on V, D and J annotations
```
Example Output:
germline_alignment_heavy    CAGGTGCAGCTGCAGGAGTCGGGCCCAGGACTGGTGAAGCCTTCAC...
number_of_sequences                                                        16
sequence_heavy              GGGAGGGTCCTGCTCACATGGGAAATACTTTCTGAGAGTCCTGGAC...
j_call_heavy                                                         IGHJ4*02
v_call_heavy                                                      IGHV4-31*03
d_call_heavy                                                      IGHD3-10*01
```
   
7. Annotate sequence with CDRs and FWRs for easy inference of regions of interest
```
Example Output:  
'AGCTCTGAGAGAGGAGCCCAGCCCTGGGATTTTCAGGTGTTTTCATTTGGTGATCAGGACTGAACAGAGAGAACTCACCATGGAGTTTGGGCTGAGCTGGCTTTTTCTTGTGGCTATTTTAAAAGGTGTCCAGTGTGAGGTGCAGCTGTTGGAGTCTGGGGGAGGCTTAGTACAGCCTGGGGGGTCCCTGAGA(cdr1 170-193) CTCTCCTGTGTAGCCTCTGGATTCACCTTTAGCAGCTATGCCATGAGCTGGGTCCGCCAG(cdr2 245-253) GCTCCAGGGAAGGGGCTGGAGTGGGTCTCAGGTATTAGTGCTAGTGGTGCTAGCACATACTACGCAGACTCCGTGAAGGGCCGGTTCACCATCTCCAGAGACAATTCCAAGAACACGCTGTATCTGCAAATGAACAGCCTG(cdr3 362-394) AGAGCCGAGGACACGGCCGTATATTACTGTGCGAAAACCCCCAAATACGATGTTTGGAGTGGTTATTATACGTCCAATGCCTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG'
```

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project.
├── data 
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
└── src                <- Source code for use in this project.
```

--------

