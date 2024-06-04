import pandas as pd

def process_query_sequence(query_sequence, df, v_sequences_df, d_sequences_df, j_sequences_df):
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
        'v_sequence': v_sequence,
        'd_sequence': d_sequence,
        'j_sequence': j_sequence,
        'sequence_alignment_heavy': sequence_alignment_heavy,
        'germline_alignment_heavy': germline_alignment_heavy
    }

# Example usage
# Assuming you have loaded your DataFrame and sequences DataFrames (df, v_sequences_df, d_sequences_df, j_sequences_df)
query_sequence = 'your_query_sequence_here'

result = process_query_sequence(query_sequence, df, v_sequences_df, d_sequences_df, j_sequences_df)
print(result)
