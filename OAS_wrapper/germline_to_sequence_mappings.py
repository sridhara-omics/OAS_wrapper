import pandas as pd

def process_germline_mappings_with_calls(data_unit_file, required_columns):
    """
    Process germline mappings from a CSV file and generate a DataFrame with 
    germline, the number of sequences mapped, and sequences, while preserving 
    specified columns.
    
    Parameters:
        data_unit_file (str): Path to the input CSV file containing the data.
        required_columns (set): A set of required column names to ensure are present
                                in the input data (e.g., {"sequence", "germline", "v_call"}).
    
    Returns:
        pd.DataFrame: Processed data as a DataFrame.
    """
    # Read the input CSV
    df = pd.read_csv(data_unit_file, low_memory=False, skiprows=1)
    
    # Validate that necessary columns exist
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise ValueError(f"Input CSV must contain the following columns: {', '.join(missing)}")
    
    # Preserve additional columns
    other_columns = [col for col in df.columns if col not in required_columns]

    # Group by germline and count sequences
    grouped = df.groupby("germline")["sequence"].apply(list).reset_index()
    grouped["number_of_sequences"] = grouped["sequence"].apply(len)

    # Explode the sequences back into individual rows
    result = grouped.explode("sequence").reset_index(drop=True)

    # Merge back with the original DataFrame to preserve additional columns
    result = result.merge(df, on=["germline", "sequence"], how="left").drop_duplicates()

    # Rearrange columns for clarity
    final_columns = ["germline", "number_of_sequences", "sequence"] + list(required_columns - {"germline", "sequence"}) + other_columns
    result = result[final_columns]

    # Return the DataFrame
    return result

""" # Example usage
data_unit_file = "germline_sequences_with_calls.csv"
required_columns = {"sequence", "germline", "v_call", "d_call", "j_call"}
processed_df = process_germline_mappings_with_calls(data_unit_file, required_columns)
print(processed_df.head())
 """