import pandas as pd
from Bio import pairwise2
from colorama import Fore, Style

def highlight_differences(seq1, seq2):
    """Highlight differences between two sequences and return indices of differences."""
    highlighted_seq1 = []
    highlighted_seq2 = []
    difference_indices = []

    for i, (char1, char2) in enumerate(zip(seq1, seq2)):
        if char1 == char2:
            highlighted_seq1.append(char1)
            highlighted_seq2.append(char2)
        else:
            # Highlight mismatches in red and track their indices
            highlighted_seq1.append(Fore.RED + char1 + Style.RESET_ALL)
            highlighted_seq2.append(Fore.RED + char2 + Style.RESET_ALL)
            difference_indices.append(i)

    return ''.join(highlighted_seq1), ''.join(highlighted_seq2), difference_indices

def map_indices_to_regions(difference_indices, row):
    """Map difference indices to annotated regions."""
    mapped_regions = []

    for index in difference_indices:
        region_found = False
        for region in ['CDR1', 'CDR2', 'CDR3']:
            start_col = f"{region}_start"
            end_col = f"{region}_end"

            # Check if the index is within the region
            if start_col in row and end_col in row:
                start = int(row[start_col])
                end = int(row[end_col])

                if start <= index <= end:
                    mapped_regions.append((index, region))
                    region_found = True
                    break

        # If no region matched, append "Unmapped"
        if not region_found:
            mapped_regions.append((index, "Unmapped"))

    return mapped_regions

def align_and_compare_with_annotations(csv_file, column1, column2, filter_column, target_sequence):
    """Align sequences, find differences, and map them to regions based on annotations."""
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Check if specified columns exist
    if column1 not in df.columns or column2 not in df.columns or filter_column not in df.columns:
        raise ValueError(f"Specified columns not found in the CSV.")

    # Filter the row where the filter column matches the target sequence
    filtered_df = df[df[filter_column] == target_sequence]

    if filtered_df.empty:
        print(f"No rows found where {filter_column} matches '{target_sequence}'.")
        return

    # Iterate over the filtered rows (there could be more than one match)
    for index, row in filtered_df.iterrows():
        seq1 = row[column1]
        seq2 = row[column2]
        
        # Perform global alignment
        alignments = pairwise2.align.globalxx(seq1, seq2)
        best_alignment = alignments[0]

        aligned_seq1, aligned_seq2 = best_alignment[0], best_alignment[1]

        # Highlight differences and get indices
        highlighted_seq1, highlighted_seq2, difference_indices = highlight_differences(aligned_seq1, aligned_seq2)

        # Map indices to regions
        mapped_regions = map_indices_to_regions(difference_indices, row)

        # Print the results
        print(f"Row {index + 1}:")
        print(f"Original Sequence 1: {seq1}")
        print(f"Original Sequence 2: {seq2}")
        print("Aligned and Highlighted Differences:")
        print(highlighted_seq1)
        print(highlighted_seq2)
        print(f"Indices of Differences: {difference_indices}")
        print(f"Mapped Regions: {mapped_regions}")
        print("-" * 50)

""" # Example usage
csv_file = "sequences_with_annotations.csv"  # Replace with your CSV file path
column1 = "Column1"                          # Replace with the first column name
column2 = "Column2"                          # Replace with the second column name
filter_column = "FilterColumn"               # Replace with the filter column name
target_sequence = "GATTACA"                  # Replace with the target sequence to filter by

align_and_compare_with_annotations(csv_file, column1, column2, filter_column, target_sequence) """
