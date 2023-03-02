RNA_Protein_mapping="UUU F	CUU L	AUU I	GUU V	UUC F	CUC L	AUC I	GUC V	UUA L	CUA L	AUA I	GUA V	UUG L	CUG L	AUG M	GUG V	UCU S	CCU P	ACU T	GCU A	UCC S	CCC P	ACC T	GCC A	UCA S	CCA P	ACA T	GCA A	UCG S	CCG P	ACG T	GCG A	UAU Y	CAU H	AAU N	GAU D	UAC Y	CAC H	AAC N	GAC D	UAA Stop	CAA Q	AAA K	GAA E	UAG Stop	CAG Q	AAG K	GAG E	UGU C	CGU R	AGU S	GGU G	UGC C	CGC R	AGC S	GGC G	UGA Stop	CGA R	AGA R	GGA G	UGG W	CGG R	AGG R	GGG G "
RNA_Protein_mapping_dict={p[0]:p[1] for p in [x.split() for x in list(map(str.strip,RNA_Protein_mapping.split('\t')))]}
seq=input()
start=seq.find('AUG')
i=0
res=''
while i<len(seq)-3:
    if RNA_Protein_mapping_dict[seq[i:i + 3]]=='Stop':break
    res+=RNA_Protein_mapping_dict[seq[i:i+3]]
    i+=3
print(res)
