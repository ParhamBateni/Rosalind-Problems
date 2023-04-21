from Bio import SeqIO
from Bio.Seq import reverse_complement
import numpy as np
def hamming_distance(x,y):
    return sum(np.array(list(x))!=np.array(list(y)))
fasta_seqs=SeqIO.parse(open('rosalind_input.txt'),'fasta')
seqs=[str(f.seq) for f in fasta_seqs]
correct_seqs=[]
wrong_seqs=[]
for seq1 in seqs:
    count_seen=-1
    for seq2 in seqs:
        if seq1==seq2 or seq1==reverse_complement(seq2):
            count_seen+=1
    if count_seen>=1:
        correct_seqs.append(seq1)
    else:
        wrong_seqs.append(seq1)
for seq1 in wrong_seqs:
    for seq2 in correct_seqs:
        if hamming_distance(seq1,seq2)==1:
            print(f'{seq1}->{seq2}')
            break
        elif hamming_distance(seq1,reverse_complement(seq2))==1:
            print(f'{seq1}->{reverse_complement(seq2)}')
            break