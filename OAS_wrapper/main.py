from column_summary import column_summary
from plot_string_length_distribution import plot_string_length_distribution

def main():
    print("Calling column summaries:")
    column_summary("../data/1279050_1_Paired_All.csv.gz",["sequence_heavy","sequence_alignment_heavy"])

    print("Calling plot distributions:")
    plot_string_length_distribution("../data/1279050_1_Paired_All.csv.gz",["sequence_heavy","sequence_alignment_heavy"])
    
if __name__ == "__main__":
    main()
