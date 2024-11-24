import pandas as pd

def column_summary(data_unit_file, columns_of_interest):
    """
    Read Observed Antibody Space CSV data and generate a summary table for selected columns.
    
    Parameters:
        csv_file (str): Path to the CSV file containing the data.
        columns_of_interest (list): List of column names to summarize.
    
    Returns:
        pandas.DataFrame: Summary table containing column name, total count, and unique count.
    """
    # Read the CSV file into a DataFrame
    data = pd.read_csv(data_unit_file, skiprows=1, low_memory=False)
    
    # Initialize an empty list to store summary information
    summary = []
    
    # Iterate over each column of interest
    for column in columns_of_interest:
        # Total count of non-null values in the column
        total_count = data[column].count()
        
        # Unique count of values in the column
        unique_count = data[column].nunique()
        
        # Append the summary information to the list
        summary.append({'Column Name': column, 'Total Count': total_count, 'Unique Count': unique_count})
    
    # Create a DataFrame from the summary list
    summary_df = pd.DataFrame(summary)
    
    return summary_df

# Usage:
# summary_table = column_summary("observed_antibody_space.csv", ["sequence_heavy", "v_sequence_alignment_heavy", "germline_alignment_heavy"])
# print(summary_table)

