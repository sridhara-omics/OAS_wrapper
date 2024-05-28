import pandas as pd
import matplotlib.pyplot as plt

def plot_string_length_distribution(csv_file, columns_of_interest):
    """
    Read Observed Antibody Space CSV data and plot distributions of string lengths for selected columns.
    
    Parameters:
        csv_file (str): Path to the CSV file containing the data.
        columns_of_interest (list): List of column names to plot distributions for.
    """
    # Read the CSV file into a DataFrame
    data = pd.read_csv(csv_file)
    
    # Iterate over each column of interest
    for column in columns_of_interest:
        # Filter out non-null values and convert to string
        column_values = data[column].dropna().astype(str)
        
        # Calculate the length of each string
        string_lengths = column_values.apply(len)
        
        # Plot histogram of string lengths
        plt.hist(string_lengths, bins=20, alpha=0.7, label=column)
    
    # Add labels and legend
    plt.xlabel('String Length')
    plt.ylabel('Frequency')
    plt.title('Distribution of String Lengths')
    plt.legend()
    
    # Show plot
    plt.show()

# Example usage
# plot_string_length_distribution("observed_antibody_space.csv", ["Antibody_ID", "Antigen_Name", "Binding_Affinity"])
