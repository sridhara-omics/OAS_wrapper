import pandas as pd

def process_query_sequence(query_sequence, df, v_sequences_df, d_sequences_df, j_sequences_df):
    """ Given a query sequence that is in the dataset, the output is a table that has relevant fields of interest picked from 200 columns of OAS dataset.
    In addition, since the actual V, D and J sequences are absent, and only the identifiers are provided in OAS dataset, we use IMGT table and map the identifier to the sequence and provide the information in the result.


    Args:
        query_sequence (_type_): query nucleotide sequence
        df (_type_): path of the OAS dataset file
        v_sequences_df (_type_): path of IGHV IMGT file
        d_sequences_df (_type_): path of IGHD IMGT file
        j_sequences_df (_type_): path of IGHJ IMGT file

    Returns:
        _type_: List that has the information filtered out from a large subset of columns, along with V/D/J sequences mapped to original IMGT database.
    """
    # Find the row that matches the input query sequence
    matched_row = df[df['sequence_heavy'] == query_sequence].iloc[0]
    
    # Read relevant data from the matched row
    v_call_heavy = matched_row['v_call_heavy']
    d_call_heavy = matched_row['d_call_heavy']
    j_call_heavy = matched_row['j_call_heavy']
    sequence_alignment_heavy = matched_row['sequence_alignment_heavy']
    germline_alignment_heavy = matched_row['germline_alignment_heavy']
    
    # Map V, D, and J calls to their respective sequences
    v_sequence = v_sequences_df.loc[v_sequences_df['v_call'] == v_call_heavy, 'sequence'].values[0]
    d_sequence = d_sequences_df.loc[d_sequences_df['d_call'] == d_call_heavy, 'sequence'].values[0]
    j_sequence = j_sequences_df.loc[j_sequences_df['j_call'] == j_call_heavy, 'sequence'].values[0]
    
    # Return relevant fields
    return {
        'v_call': v_call_heavy,
        'v_sequence': v_sequence,
        'd_call': d_call_heavy,
        'd_sequence': d_sequence,
        'j_call': j_call_heavy,
        'j_sequence': j_sequence,
        'sequence_alignment_heavy': sequence_alignment_heavy,
        'germline_alignment_heavy': germline_alignment_heavy
    }

# Example usage
# Assuming you have loaded your DataFrame and sequences DataFrames (df, v_sequences_df, d_sequences_df, j_sequences_df)
# query_sequence = 'TGGGGGACTCCTGTGCCCCACCATGGACACACTTTGCTCCACGCTCCTGCTGCTGATCATCCCTTCATGGGTCTTGTCCCAGATCACCTTGGAGGAGTCTGGTCCTACACTGGTGAAACCCACACAGACCCTCACGCTGACATGCACCTTTTCTGGGTTCTCACTCAGCACTAGTGGAGTGGGTGTGGGCTGGATCCGTCAGCCCCCAGGAAAGGCCCTGGAGTGGCTTGCACTCATTTATTGGGACGGTAATAACCTCTATAGTCCATCTCTGCAGAACAGGCTCACCATCACCAAGGACACCTCCAAAAACCAGGTGGTCCTTACAATGACCAACATGGACCCTATTGACACAGCCACATATTTCTGTGCTCACTTCTCTGCTACTGTGAGTCGGGGATTTATGAATATCAGGAGAAAAAAGCCCCAGAGTTATGACTACTGGGGCCAGGGAAGTCTGGTCACCGTCTCCTCAGCATCCCCGACCAGCCCCAAGGTCTTCCCGCTGAGCCTCTGCAGCACCCAGCCAGATGGGAACGTGGTCATCGCCTGCCTGGTCCAGGGCTTCTTCCCCCAGGAGCCACTCAGTGTGACCTGGAGCGAAAGCGGACAGGGCGTGACCGCCAGAAACTTCCC'
# df = pd.read_csv("../data/1279050_1_Paired_All.csv.gz", low_memory=False, skiprows=1)
# v_sequences_df = pd.read_csv("../refs/imgt_human_IGHV_sequences.txt", names=("v_call", "sequence"), header=None, sep="\t")
# d_sequences_df = pd.read_csv("../refs/imgt_human_IGHD_sequences.txt", names=("d_call", "sequence"), header=None, sep="\t")
# j_sequences_df = pd.read_csv("../refs/imgt_human_IGHJ_sequences.txt", names=("j_call", "sequence"), header=None, sep="\t")

# result = process_query_sequence(query_sequence, df, v_sequences_df, d_sequences_df, j_sequences_df)
# print(result)
