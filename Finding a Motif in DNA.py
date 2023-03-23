dna,motif=input(),input()
print(' '.join(map(str,list(filter(lambda x:dna[x-1:x-1+len(motif)]==motif,list(range(1,len(dna)-len(motif)+1)))))))