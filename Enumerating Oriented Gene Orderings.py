def signed_permutation(l):
    if l[0] == l[-1]:
        return [[l[0]], [-l[0]]]
    permutation_result=[]
    for i in range(len(l)):
        reduced_permutation = signed_permutation(l[:i]+l[i+1:])
        for p in reduced_permutation:
            permutation_result.append(p + [l[i]])
            permutation_result.append(p + [-l[i]])

    return permutation_result


n = int(input())

result = signed_permutation(list(range(1,n+1)))
print(len(result))
print('\n'.join([' '.join(map(str, x)) for x in result]))
