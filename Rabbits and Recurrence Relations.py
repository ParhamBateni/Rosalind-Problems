# def f(n,k):
#     return 0 if n==1 else g(n-1,k)+f(n-1,k)
# def g(n,k):
#     return 2 if n==1 else f(n-1,k)//2*2*k
def t(n,k):
    return 1 if n in [1,2] else t(n-1,k)+t(n-2,k)*k
n,k=map(int,input().split())
# print((f(n,k)+g(n,k))//2)
print(t(n,k))
