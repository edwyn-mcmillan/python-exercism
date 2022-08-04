convert = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
}

def to_rna(dna_strand):
    rna_strand = ""
    for nucleotide in dna_strand:
        rna_strand += convert[nucleotide]
    return rna_strand
        