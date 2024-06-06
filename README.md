# OAS_wrapper
A wrapper for visualization and basic statiscal analysis of  Observed Antibody Space (OAS) data.

## Functionalities

The scripts include functionality to do basic statistics and visualization of the OAS data. 

## Column summaries:
column_summary.py -> Given OAS dataset as input, the function provides basic statistics on the unique and total counts of a column of interest.

```
# Usage:
summary_table = column_summary("observed_antibody_space.csv", ["Antibody_ID", "Antigen_Name", "Binding_Affinity"])
print(summary_table)
```
## Length distributions:
plot_string_length_distribution.py -> Given OAS dataset as input, the function provides basic visualization plots of length distributions of different fields e.g., V, D, J, FWR1-FWR4, CDR1-CDR3 etc.

```
# Usage: 
plot_string_length_distribution("observed_antibody_space.csv", ["Antibody_ID", "Antigen_Name", "Binding_Affinity"])
```

## Tabulate results for query sequence:
tabulate_query_sequence.py -> Given query sequence and IMGT database, the V/D/J sequences along with other relevant information is obtained for the query sequence. 

```
# Usage: 
# Assuming you have loaded your DataFrame and sequences DataFrames (df, v_sequences_df, d_sequences_df, j_sequences_df)
query_sequence = 'TGGGGGACTCCTGTGCCCCACCATGGACACACTTTGCTCCACGCTCCTGCTGCTGATCATCCCTTCATGGGTCTTGTCCCAGATCACCTTGGAGGAGTCTGGTCCTACACTGGTGAAACCCACACAGACCCTCACGCTGACATGCACCTTTTCTGGGTTCTCACTCAGCACTAGTGGAGTGGGTGTGGGCTGGATCCGTCAGCCCCCAGGAAAGGCCCTGGAGTGGCTTGCACTCATTTATTGGGACGGTAATAACCTCTATAGTCCATCTCTGCAGAACAGGCTCACCATCACCAAGGACACCTCCAAAAACCAGGTGGTCCTTACAATGACCAACATGGACCCTATTGACACAGCCACATATTTCTGTGCTCACTTCTCTGCTACTGTGAGTCGGGGATTTATGAATATCAGGAGAAAAAAGCCCCAGAGTTATGACTACTGGGGCCAGGGAAGTCTGGTCACCGTCTCCTCAGCATCCCCGACCAGCCCCAAGGTCTTCCCGCTGAGCCTCTGCAGCACCCAGCCAGATGGGAACGTGGTCATCGCCTGCCTGGTCCAGGGCTTCTTCCCCCAGGAGCCACTCAGTGTGACCTGGAGCGAAAGCGGACAGGGCGTGACCGCCAGAAACTTCCC'
df = pd.read_csv("../data/1279050_1_Paired_All.csv.gz", low_memory=False, skiprows=1)
v_sequences_df = pd.read_csv("../refs/imgt_human_IGHV_sequences.txt", names=("v_call", "sequence"), header=None, sep="\t")
d_sequences_df = pd.read_csv("../refs/imgt_human_IGHD_sequences.txt", names=("d_call", "sequence"), header=None, sep="\t")
j_sequences_df = pd.read_csv("../refs/imgt_human_IGHJ_sequences.txt", names=("j_call", "sequence"), header=None, sep="\t")

result = process_query_sequence(query_sequence, df, v_sequences_df, d_sequences_df, j_sequences_df)
print(result)

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

