import json
import pandas as pd

def extract_metadata_and_sequences(data_unit_file):
    """
    Extract metadata and sequence data from a gzipped CSV file.
    
    Parameters:
        data_unit_file (str): Path to the gzipped CSV file.
        
    Returns:
        tuple: A tuple containing:
            - metadata (dict): The metadata extracted from the CSV's first row of column headers.
            - sequences (pd.DataFrame): A DataFrame containing the sequence data.
    """
    # Extract metadata from the first row (column headers)
    metadata = ','.join(pd.read_csv(data_unit_file, nrows=0).columns)
    metadata = json.loads(metadata)

    # Extract sequences from the file (skipping the metadata row)
    sequences = pd.read_csv(data_unit_file, header=1)
    
    return metadata, sequences

# Example usage
data_unit_file = "SRR5060321_Heavy_Bulk.csv.gz"
metadata, sequences = extract_metadata_and_sequences(data_unit_file)

print("Metadata:")
print(metadata)
print("\nSequences:")
print(sequences.head())
