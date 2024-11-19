import pandas as pd

def annotate_sequence(sequence, annotations):
    """Annotate a sequence with combined annotations for contiguous regions."""
    # Initialize a list to store annotations for each position
    position_annotations = ["Unannotated"] * len(sequence)

    # Apply each annotation region to the positions
    for region, (start, end) in annotations.items():
        for i in range(start, end + 1):  # Inclusive range
            if 0 <= i < len(sequence):  # Ensure indices are within bounds
                position_annotations[i] = region

    # Combine contiguous regions with the same annotation
    annotated_sequence = []
    current_annotation = position_annotations[0]
    current_block = sequence[0]

    for i in range(1, len(sequence)):
        if position_annotations[i] == current_annotation:
            # Continue the current block
            current_block += sequence[i]
        else:
            # Save the completed block with annotation
            annotated_sequence.append(f"{current_block}({current_annotation})")
            # Start a new block
            current_annotation = position_annotations[i]
            current_block = sequence[i]

    # Add the final block
    annotated_sequence.append(f"{current_block}({current_annotation})")

    return ''.join(annotated_sequence)

def get_annotations(row):
    """Extract annotation regions dynamically from a row."""
    annotations = {}
    for col_name in row.index:
        if "_start" in col_name:
            region_name = col_name.replace("_start", "")
            start_col = col_name
            end_col = f"{region_name}_end"

            if end_col in row:
                annotations[region_name] = (int(row[start_col]), int(row[end_col]))
    return annotations

def annotate_from_csv(csv_file):
    """Annotate sequences based on regions from a CSV file."""
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Check for mandatory Sequence column
    if "Sequence" not in df.columns:
        raise ValueError("CSV file must contain a 'Sequence' column.")

    # Process each row
    for index, row in df.iterrows():
        sequence = row['Sequence']

        # Extract annotation regions dynamically
        annotations = get_annotations(row)

        # Annotate the sequence
        annotated_sequence = annotate_sequence(sequence, annotations)

        # Print the results
        print(f"Row {index + 1}:")
        print(f"Original Sequence: {sequence}")
        print(f"Annotated Sequence: {annotated_sequence}")
        print("-" * 50)

# Example usage
csv_file = "sequence_annotations.csv"  # Replace with your CSV file path
annotate_from_csv(csv_file)
