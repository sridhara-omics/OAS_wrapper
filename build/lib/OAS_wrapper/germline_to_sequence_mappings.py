import pandas as pd

def process_germline_mappings_with_calls(data_unit_file, output_csv):
    """
    Process germline mappings from a CSV file and generate a new CSV file with 
    germline, the number of sequences mapped, and sequences, while preserving 
    'v_call', 'd_call', 'j_call', and other columns.
    
    Parameters:
        input_csv (str): Path to the input CSV file containing 'sequence', 'germline',
                         'v_call', 'd_call', and 'j_call' columns.
        output_csv (str): Path to the output CSV file to save the processed data.
    """
    # Read the input CSV
    df = pd.read_csv(data_unit_file, low_memory=False, skiprows=1)
    
    # Validate that necessary columns exist
    required_columns = {"sequence", "germline", "v_call", "d_call", "j_call"}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise ValueError(f"Input CSV must contain the following columns: {', '.join(missing)}")
    
    # Preserve additional columns
    other_columns = [col for col in df.columns if col not in {"sequence", "germline", "v_call", "d_call", "j_call"}]

    # Group by germline and count sequences
    grouped = df.groupby("germline")["sequence"].apply(list).reset_index()
    grouped["number_of_sequences"] = grouped["sequence"].apply(len)

    # Explode the sequences back into individual rows
    result = grouped.explode("sequence").reset_index(drop=True)

    # Merge back with the original DataFrame to preserve additional columns
    result = result.merge(df, on=["germline", "sequence"], how="left").drop_duplicates()

    # Rearrange columns for clarity
    final_columns = ["germline", "number_of_sequences", "sequence", "v_call", "d_call", "j_call"] + other_columns
    result = result[final_columns]

    # Save to the output CSV
    result.to_csv(output_csv, index=False)
    print(f"Processed data saved to {output_csv}")

""" # Example usage
input_csv = "germline_sequences_with_calls.csv"
output_csv = "processed_germline_mappings_with_calls.csv"
process_germline_mappings_with_calls(input_csv, output_csv)
 """