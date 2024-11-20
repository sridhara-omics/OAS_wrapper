# OAS_wrapper
A wrapper for visualization and basic statiscal analysis of  Observed Antibody Space (OAS) data.

## Functionalities

The scripts include functionality to do basic statistics and visualization of the OAS data. 

## Separate original OAS data file into metadata and sequences data
metadata_sequences.py -> Given original OAS data file, the script separates the data file into metadata file and the sequences data frame.
```
Usage:
# Example usage
data_unit_file = "SRR5060321_Heavy_Bulk.csv.gz"
output_csv_file = "extracted_sequences.csv"

# Extract metadata and sequences
metadata, sequences = extract_metadata_and_sequences(data_unit_file)

# Save sequences to a CSV file
save_sequences_to_csv(sequences, output_csv_file)

print("Metadata:")
print(metadata)

Sample output

data_unit_file: The path to the gzipped CSV file.
Metadata Extraction:

The metadata is extracted from the column headers (first row of the CSV). It is read as a single row and parsed into a JSON object.
Sequence Extraction:

The sequence data is extracted from the remaining rows (starting from the second row).

Saves the sequences DataFrame to a CSV file using pandas.DataFrame.to_csv.
The index=False parameter ensures that the DataFrame's index is not written to the CSV file.
```


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
## Align sequence to germline and identify mismatches
compare_sequence_to_germline.py -> Given OAS data, the script aligns the sequence to germline, and highlights the regions that are different, giving both positional information of mismatches along with highlighting regions of mismatches.
```
Usage:
align_and_compare_on_row("sequences.csv", "Column1", "Column2", "FilterColumn", "GATTACA")

Sample output:

Row 1:
Original Sequence 1: ATGCCGT
Original Sequence 2: ATGTCGT
Aligned and Highlighted Differences:
ATGC[RED]C[/RED]GT
ATG[RED]T[/RED]CGT
Indices of Differences: [3]
--------------------------------------------------
Explanation of Output:
The script aligns the sequences, highlights mismatches, and outputs the indices where they occur.
For the example above, the mismatch at position 3 (0-based index) is highlighted and its index is printed.


```

## Annotate sequence with CDRs and FWRs and other fields that are present in OAS
annotate_sequence.py -> Given OAS data file, the script annotates sequences explicitly with CDR and FWR regions.
```
Usage:
csv_file = "sequence_annotations.csv"  # Replace with your CSV file path
annotate_from_csv(csv_file)

Sample output

Row 1:
Original Sequence: ATGCCGTAACTG
Annotated Sequence: A(Unannotated)TG(CDR1 2-3)CCG(FWR1 4-6)TA(CDR2 7-8)AC(FWR2 9-10)TG(CDR3 11-12)
--------------------------------------------------
Row 2:
Original Sequence: GATTACAGTGCTA
Annotated Sequence: GAT(CDR1 1-3)TAC(FWR1 4-6)AG(CDR2 7-8)TG(FWR2 9-10)CTA(CDR3 11-13)
--------------------------------------------------

Including Positional Information:

When saving a completed block, the start and end positions of the block are included alongside the region name in the format (Region Start-End).
Dynamic Block Start:

A block_start variable tracks the starting position of each block, ensuring accurate positional reporting.
Simplified Handling of Unannotated Regions:

Regions marked as Unannotated are left as-is without appending positional information.
```
## Grouping by Germline
germline_to_sequence_mappings.py -> Given the OAS data, group the data by germline sequence to see how many sequences originate from germline, along with the VDJ annotations/calls.
```
Usage:
# Example usage
input_csv = "germline_sequences_with_calls.csv"
output_csv = "processed_germline_mappings_with_calls.csv"
process_germline_mappings_with_calls(input_csv, output_csv)

Sample output

Use groupby to group sequences by germline.
Create a list of sequences for each germline and count the number of sequences.
Handling Redundancy:

Use explode to expand the lists of sequences back into individual rows, allowing redundancy in germline and number_of_sequences.
Output CSV: The output CSV contains:

germline: Germline identifier.
number_of_sequences: Number of sequences mapped to the germline.
sequence: A sequence mapped to the germline.
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

