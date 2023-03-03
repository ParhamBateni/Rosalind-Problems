def combinations(x):
    combs=[]
    if len(x)==1:return [x]
    for i in range(len(x)):
        next_combs=combinations(x[:i]+x[i+1:])
        for c in next_combs:
            combs.append([x[i]]+c)
    return combs
ans=combinations(list(range(1,int(input())+1)))
print(len(ans))
for a in ans:
    print(*a)