def f(n,m):
    if n==1:
        return [1]+[0]*(m - 1)
    else:
        l= f(n - 1, m)
        l_new= [0] * m
        s=l[m-1]
        for i in range(1, m):
            if i>1:
                s+=l[i-1]
            l_new[i]=l[i-1]
        l_new[0]=s
        return l_new
n,m=map(int,input().split())
print(sum(f(n, m)))