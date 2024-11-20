def parse_fasta(file_path):
    """Parse a FASTA file and return a dictionary of gene sequences.

    Args:
        file_path (str): Path to the input FASTA file.

    Returns:
        dict: A dictionary containing gene names as keys and their corresponding sequences as values.
    """
    gene_sequences = {}
    with open(file_path, 'r') as f:
        current_gene = None
        current_sequence = ''
        for line in f:
            if line.startswith('>'):
                if current_gene is not None:
                    gene_sequences[current_gene] = current_sequence
                current_gene = extract_gene_info(line.strip())
                current_sequence = ''
            else:
                current_sequence += line.strip()
        # Add the last sequence
        if current_gene is not None:
            gene_sequences[current_gene] = current_sequence
    return gene_sequences

def extract_gene_info(defline):
    """Extract gene information from the definition line of a FASTA entry.

    Args:
        defline (str): The definition line of a FASTA entry.

    Returns:
        str: The extracted gene information.
    """
    gene_info = defline.split('|')[1]
    return gene_info

def process_fasta_files(file_paths):
    """Process multiple FASTA files and produce output for each.

    Args:
        file_paths (list): A list of file paths to input FASTA files.
    """
    for file_path in file_paths:
        gene_sequences = parse_fasta(file_path)
        output_file = file_path.replace('.fasta', '_sequences.txt')  # Output file name based on input file name
        with open(output_file, 'w') as file:
            for gene, sequence in gene_sequences.items():
                file.write(f"{gene}\t{sequence}\n")

def main():
    fasta_files = ['../refs/imgt_human_IGKJ.fasta', '../refs/imgt_human_IGKV.fasta','../refs/imgt_human_IGLJ.fasta', '../refs/imgt_human_IGLV.fasta']  # Replace with a list of your FASTA file paths
    process_fasta_files(fasta_files)

if __name__ == "__main__":
    main()
