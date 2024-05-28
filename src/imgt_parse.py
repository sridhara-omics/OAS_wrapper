def parse_fasta(file_path):
    """_summary_

    Args:
        file_path (_type_): _description_

    Returns:
        _type_: _description_
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
    """_summary_

    Args:
        defline (_type_): _description_

    Returns:
        _type_: _description_
    """
    gene_info = defline.split('|')[1]
    return gene_info

def main():
    fasta_file = '../refs/imgt_human_IGHV.fasta'  # Replace 'sequences.fasta' with your FASTA file path
    gene_sequences = parse_fasta(fasta_file)
    
    # Output gene+allele information and sequence in two columns
    print("Gene+Allele\tSequence")
    for gene, sequence in gene_sequences.items():
        print(f"{gene}\t{sequence}")

if __name__ == "__main__":
    main()
