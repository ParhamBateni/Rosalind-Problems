import requests as r
base_url='http://www.uniprot.org/uniprot/'
id=input()
while id:
    corrected_id=id[:id.index('_')] if '_' in id else id
    resp=r.request(url=f'{base_url}{corrected_id}.fasta',method='get')
    seq_text=''.join((resp.text[resp.text.index('\n')+1:]).split('\n'))
    motif_indexes=[]
    for i in range(len(seq_text)-4):
        if seq_text[i]=='N' and seq_text[i+1]!='P' and seq_text[i+2] in ['S','T'] and seq_text[i+3]!='P':
            motif_indexes.append(i+1)
    if len(motif_indexes)>0:
        print(id)
        print(' '.join(map(str,motif_indexes)))
    id=input()