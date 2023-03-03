def create_vocabulary(alphabet,size):
    vocab=[]
    if size==1:return alphabet
    sub_vocab=create_vocabulary(alphabet,size-1)
    for letter in alphabet:
        for s in sub_vocab:
            if isinstance(s,list):
                vocab.append([letter]+s)
            else:
                vocab.append([letter]+[s])
    return vocab
print('\n'.join([''.join(x) for x in create_vocabulary(input().split(),int(input()))]))