from Bio import SeqIO
from Bio.Seq import translate
fasta_seqs=SeqIO.parse(open('rosalind_input.txt','r'),'fasta')
seqs=[s.seq for s in fasta_seqs]
dna=seqs[0]
introns=seqs[1:]
for intron in introns:
    dna=dna.replace(intron,'')
print(translate(dna)[:-1])