# OAS_wrapper

**Antibody sequence analysis made easy, with tools for parsing, annotation, alignment, visualization, and reporting of Observed Antibody Space (OAS) data.**

[PyPI](https://pypi.org/project/OAS-wrapper/) [Python](https://www.python.org/) [License: MIT]  

This tool is a wrapper to parse Observed Antibody Space (OAS) data for better visualization, annotation and comparison of sequence to germline.

## What each functionality returns

The package covers five tasks. This table summarizes the kind of output each one gives; the examples earlier in this README show the
format (they use short toy sequences for illustration).

| Task | Output |
|---|---|
| Basic metrics and visualizations | Summary statistics and plots of sequences and their annotations |
| IMGT reference lookup | Original IMGT germline sequences for the V, D and J calls made in the OAS data |
| Sequence vs germline alignment | Aligned sequences with mismatches highlighted, the indices of the differences, and the region (for example CDR2) each difference falls in |
| Grouping by germline | A table per germline with the sequence count and the V, D and J annotations (and per-sequence fields such as quality and source) |
| CDR/FWR annotation | The sequence split into complementarity-determining and framework regions for quick inspection |

## Information on Outputs of Functionalities

The scripts include functionalities to:
1. Provide basic metrics and visualizations of sequences and their annotations
   ![image](https://github.com/user-attachments/assets/ebcf2891-23fb-423a-beb6-3149e6279085)

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
4. Group data by germline, to infer sequences that originate from germline, including providing information on V, D and J annotations
```
Example Output:
germline_alignment_heavy    CAGGTGCAGCTGCAGGAGTCGGGCCCAGGACTGGTGAAGCCTTCAC...
number_of_sequences                                                        16
sequence_heavy              GGGAGGGTCCTGCTCACATGGGAAATACTTTCTGAGAGTCCTGGAC...
j_call_heavy                                                         IGHJ4*02
v_call_heavy                                                      IGHV4-31*03
d_call_heavy                                                      IGHD3-10*01
```
   
5. Annotate sequence with CDRs and FWRs for easy inference of regions of interest
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
## Installation

OAS-wrapper is published on PyPI:

```bash
pip install OAS-wrapper
```

To upgrade or check the installed version:

```bash
pip install --upgrade OAS-wrapper
pip show OAS-wrapper
```

To work from source (for development):

```bash
git clone https://github.com/sridhara-omics/OAS_wrapper.git
cd OAS_wrapper
pip install -e .
```

**Requirements:** Python 3.10+. Dependencies are installed automatically by `pip`.

## Data sources and attribution

- **Observed Antibody Space (OAS)** data is made available by the Oxford Protein Informatics Group under CC-BY 4.0. If you use OAS data,
  please cite the OAS publications (see the OAS website for the current citation list):
  - Kovaltsuk, A. et al. *Observed Antibody Space: A Resource for Data Mining Next-Generation Sequencing of Antibody Repertoires.*
    The Journal of Immunology (2018).
  - Olsen, T. H., Boyles, F., Deane, C. M. *Observed Antibody Space: A diverse database of cleaned, annotated, and translated unpaired and
    paired antibody sequences.* Protein Science (2022).
- **IMGT** reference sequences are used for the V, D and J lookups. Please follow the terms of use and citation guidance on the
  [IMGT website](https://www.imgt.org/).

## Limitations

- Intended for research and exploratory analysis; it is not a clinical or diagnostic tool.
- Results depend on the OAS annotations and the IMGT reference version used. 

## Contributing and issues

Bug reports and suggestions are welcome via [GitHub Issues](https://github.com/sridhara-omics/OAS_wrapper/issues). When reporting a problem,
please include the package version, your Python version, and a minimal example of the input that triggers it.

## Citation

If OAS-wrapper is useful in your work, please cite it together with OAS and IMGT:

```bibtex
@software{sridhara_oas_wrapper,
  author  = {Sridhara, Vish},
  title   = {OAS-wrapper: a wrapper to parse Observed Antibody Space data for visualization, annotation and comparison to germline},
  year    = {2024},
  version = {1.1},
  url     = {https://github.com/sridhara-omics/OAS_wrapper}
}
```


