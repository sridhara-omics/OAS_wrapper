import pandas as pd
import re

def annotate_sequence(sequence, annotations):
    """Annotate a sequence with combined annotations and positional information."""
    # Initialize a list to store annotations for each position
    position_annotations = ["Unannotated"] * len(sequence)

    # Apply each annotation region to the positions
    for region, (start, end) in annotations.items():
        for i in range(start, end + 1):  # Inclusive range
            if 0 <= i < len(sequence):  # Ensure indices are within bounds
                position_annotations[i] = region

    # Combine contiguous regions with the same annotation and include positional info
    annotated_sequence = []
    current_annotation = position_annotations[0]
    current_block = sequence[0]
    block_start = 0

    for i in range(1, len(sequence)):
        if position_annotations[i] == current_annotation:
            # Continue the current block
            current_block += sequence[i]
        else:
            # Save the completed block with annotation and positions
            if current_annotation != "Unannotated":
                annotated_sequence.append(
                    f"{current_block}({current_annotation} {block_start + 1}-{block_start + len(current_block)})"
                )
            else:
                annotated_sequence.append(current_block)
            # Start a new block
            current_annotation = position_annotations[i]
            current_block = sequence[i]
            block_start = i

    # Add the final block
    if current_annotation != "Unannotated":
        annotated_sequence.append(
            f"{current_block}({current_annotation} {block_start + 1}-{block_start + len(current_block)})"
        )
    else:
        annotated_sequence.append(current_block)

    return ''.join(annotated_sequence)

def get_annotations(row):
    """
    Extract annotation regions dynamically from a row based on 
    column naming patterns like 'cdr*_start*', where:
    - The first '*' represents a number.
    - The second '*' can be blank or a string.
    """
    annotations = {}
    for col_name in row.index:
        # Match columns like 'cdr*_start*'
        match = re.match(r"cdr\d+_start.*", col_name)
        if match:
            region_name = col_name.split("_start")[0]  # Extract region name (e.g., 'cdr1', 'cdr12')
            start_col = col_name
            # Find the corresponding end column
            end_col = col_name.replace("_start", "_end")

            if end_col in row:
                annotations[region_name] = (int(row[start_col]), int(row[end_col]))
    return annotations

def annotate_query_sequence(data_unit_file, sequence_col, query_sequence):
    """
    Annotate a query sequence based on matching row in a CSV file.
    
    Parameters:
        data_unit_file (str): Path to the input CSV file.
        sequence_col (str): Name of the column containing sequences.
        query_sequence (str): The sequence to annotate.
        
    Returns:
        str: Annotated query sequence.
    """
    # Read the CSV file
    df = pd.read_csv(data_unit_file, low_memory=False, skiprows=1)

    # Check for mandatory sequence column
    if sequence_col not in df.columns:
        raise ValueError(f"CSV file must contain a '{sequence_col}' column.")

    # Find the row matching the query sequence
    matching_rows = df[df[sequence_col] == query_sequence]

    if matching_rows.empty:
        raise ValueError("Query sequence not found in the dataset.")

    # There could be multiple matches; we'll use the first one
    row = matching_rows.iloc[0]

    # Extract annotation regions dynamically
    annotations = get_annotations(row)

    # Annotate the query sequence
    annotated_sequence = annotate_sequence(query_sequence, annotations)

    # Return the annotated sequence
    return annotated_sequence

""" # Example usage
csv_file = "sequence_annotations.csv"  # Replace with your CSV file path
sequence_column = "Sequence"  # Replace with the column name in your CSV
query_sequence = "ACTGACTGACTG"  # Replace with your query sequence

annotated_sequence = annotate_query_sequence(csv_file, sequence_column, query_sequence)
print("Annotated Sequence:")
print(annotated_sequence)
"""
