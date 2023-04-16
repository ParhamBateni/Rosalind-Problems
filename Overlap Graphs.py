from Bio import SeqIO
fasta_sequence_dict=SeqIO.to_dict(SeqIO.parse(open('rosalind_input.txt'),'fasta'))
ids=list(fasta_sequence_dict.keys())
edges=[]
for i in range(len(ids)):
    for j in range(len(ids)):
        seq1=fasta_sequence_dict[ids[i]].seq
        seq2=fasta_sequence_dict[ids[j]].seq
        if seq1[-3:]== seq2[:3] and seq1!=seq2:
            edges.append(f'{ids[i]} {ids[j]}')
print('\n'.join(edges))