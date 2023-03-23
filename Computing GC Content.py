from Bio import SeqIO
fasta_sequences=SeqIO.parse(open('rosalind_input.txt','r'),'fasta')
gc_values=[((str(x.seq).count('G')+str(x.seq).count('C'))/len(x.seq)*100,x.name) for x in fasta_sequences]
best_seq=max(gc_values)
print(best_seq[1])
print(best_seq[0])