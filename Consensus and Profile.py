from Bio import SeqIO
import numpy as np
fasta_seqs=SeqIO.parse(open('rosalind_input.txt'),'fasta')
char_mapping={'A':0,'C':1,'G':2,'T':3}
reversed_char_mapping={0:'A',1:'C',2:'G',3:'T'}
collection_matrix=None
for fasta_seq in fasta_seqs:
    if collection_matrix is None:
        collection_matrix = np.zeros((4, len(fasta_seq.seq)),dtype=int)
    seq=fasta_seq.seq
    for j,l in enumerate(seq):
        collection_matrix[char_mapping[l]][j]+=1
print(''.join([reversed_char_mapping[x] for x in collection_matrix.argmax(axis=0)]))
for k in char_mapping:
    print(f"{k}: {' '.join(map(str,collection_matrix[char_mapping[k]]))}")

