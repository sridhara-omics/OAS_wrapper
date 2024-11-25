import pandas as pd

def tabulate_query_sequence(query_sequence, data_unit_file, v_sequences_df, d_sequences_df, j_sequences_df, paired=True):
    """
    Given a query sequence that is in the dataset, the output is a table that has relevant fields of interest picked 
    from 200 columns of the OAS dataset. In addition, since the actual V, D, and J sequences are absent, and only 
    the identifiers are provided in the OAS dataset, we use the IMGT table and map the identifier to the sequence 
    and provide the information in the result.

    Args:
        query_sequence (str): query nucleotide sequence
        data_unit_file (str): path of the OAS dataset file
        v_sequences_df (DataFrame): DataFrame of IGHV IMGT file
        d_sequences_df (DataFrame): DataFrame of IGHD IMGT file
        j_sequences_df (DataFrame): DataFrame of IGHJ IMGT file
        paired (bool): If True, '_heavy' suffix is included in column names. Otherwise, it is excluded.

    Returns:
        dict: Dictionary with the filtered information and mapped sequences.
    """
    # Determine column suffix based on paired status
    suffix = "_heavy" if paired else ""

    # Read the data unit file
    df = pd.read_csv(data_unit_file, low_memory=False, skiprows=1)

    # Find the row that matches the input query sequence
    matched_row = df[df[f'sequence{suffix}'] == query_sequence].iloc[0]
    
    # Read relevant data from the matched row
    v_call = matched_row[f'v_call{suffix}']
    d_call = matched_row[f'd_call{suffix}']
    j_call = matched_row[f'j_call{suffix}']
    sequence_alignment = matched_row[f'sequence_alignment{suffix}']
    germline_alignment = matched_row[f'germline_alignment{suffix}']
    
    # Map V, D, and J calls to their respective sequences
    v_sequence = v_sequences_df.loc[v_sequences_df['v_call'] == v_call, 'sequence'].values[0]
    d_sequence = d_sequences_df.loc[d_sequences_df['d_call'] == d_call, 'sequence'].values[0]
    j_sequence = j_sequences_df.loc[j_sequences_df['j_call'] == j_call, 'sequence'].values[0]
    
    # Return relevant fields
    return {
        f'sequence{suffix}': query_sequence,
        'v_call': v_call,
        'v_sequence': v_sequence,
        'd_call': d_call,
        'd_sequence': d_sequence,
        'j_call': j_call,
        'j_sequence': j_sequence,
        f'sequence_alignment{suffix}': sequence_alignment,
        f'germline_alignment{suffix}': germline_alignment
    }

# Example usage
# query_sequence = 'TGGGGGACTCCTGTGCCCCACCATGGACACACTTTGCTCCACGCTCCTGCTGCTGATCATCCCTTCATGGGTCTTGTCCCAGATCACCTTGGAGGAGTCTGGTCCTACACTGGTGAAACCCACACAGACCCTCACGCTGACATGCACCTTTTCTGGGTTCTCACTCAGCACTAGTGGAGTGGGTGTGGGCTGGATCCGTCAGCCCCCAGGAAAGGCCCTGGAGTGGCTTGCACTCATTTATTGGGACGGTAATAACCTCTATAGTCCATCTCTGCAGAACAGGCTCACCATCACCAAGGACACCTCCAAAAACCAGGTGGTCCTTACAATGACCAACATGGACCCTATTGACACAGCCACATATTTCTGTGCTCACTTCTCTGCTACTGTGAGTCGGGGATTTATGAATATCAGGAGAAAAAAGCCCCAGAGTTATGACTACTGGGGCCAGGGAAGTCTGGTCACCGTCTCCTCAGCATCCCCGACCAGCCCCAAGGTCTTCCCGCTGAGCCTCTGCAGCACCCAGCCAGATGGGAACGTGGTCATCGCCTGCCTGGTCCAGGGCTTCTTCCCCCAGGAGCCACTCAGTGTGACCTGGAGCGAAAGCGGACAGGGCGTGACCGCCAGAAACTTCCC'
# result = tabulate_query_sequence(query_sequence, "../data/1279050_1_Paired_All.csv.gz", v_sequences_df, d_sequences_df, j_sequences_df, paired=True)
# print(result)
