import pandas as pd
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from colorama import Fore, Style

def highlight_differences(seq1, seq2):
    """Highlight differences between two sequences using color."""
    highlighted_seq1 = []
    highlighted_seq2 = []

    for char1, char2 in zip(seq1, seq2):
        if char1 == char2:
            highlighted_seq1.append(char1)
            highlighted_seq2.append(char2)
        else:
            # Highlight mismatches in red
            highlighted_seq1.append(Fore.RED + char1 + Style.RESET_ALL)
            highlighted_seq2.append(Fore.RED + char2 + Style.RESET_ALL)
    
    return ''.join(highlighted_seq1), ''.join(highlighted_seq2)

def align_and_compare(csv_file, column1, column2):
    """Align sequences in two columns of a CSV file and highlight differences."""
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Check if specified columns exist
    if column1 not in df.columns or column2 not in df.columns:
        raise ValueError(f"Columns '{column1}' and/or '{column2}' not found in the CSV.")

    # Iterate over rows and align sequences
    for index, row in df.iterrows():
        seq1 = row[column1]
        seq2 = row[column2]
        
        # Perform global alignment
        alignments = pairwise2.align.globalxx(seq1, seq2)
        best_alignment = alignments[0]

        aligned_seq1, aligned_seq2 = best_alignment[0], best_alignment[1]

        # Highlight differences
        highlighted_seq1, highlighted_seq2 = highlight_differences(aligned_seq1, aligned_seq2)

        # Print the results
        print(f"Row {index + 1}:")
        print(f"Original Sequence 1: {seq1}")
        print(f"Original Sequence 2: {seq2}")
        print("Aligned and Highlighted Differences:")
        print(highlighted_seq1)
        print(highlighted_seq2)
        print("-" * 50)

# Example usage
csv_file = "sequences.csv"  # Replace with your CSV file path
column1 = "Column1"         # Replace with the first column name
column2 = "Column2"         # Replace with the second column name
align_and_compare(csv_file, column1, column2)
