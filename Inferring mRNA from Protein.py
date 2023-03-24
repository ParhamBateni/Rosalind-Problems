import Bio.Data.CodonTable
codon_table=Bio.Data.CodonTable.standard_dna_table.__dict__['forward_table']
reverse_codon_table={amino_acid:0 for amino_acid in codon_table.values()}
for k in codon_table:
    reverse_codon_table[codon_table[k]]=reverse_codon_table[codon_table[k]]+1
protein=input()
count_combs=3
for amino_acid in protein:
    count_combs*=reverse_codon_table[amino_acid]
    count_combs%=1_000_000
print(count_combs)
