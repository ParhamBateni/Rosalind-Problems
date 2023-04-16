from math import comb
k,n=map(int,input().split())
print(sum([comb(2**k,i)*((1/4)**i)*((3/4)**(2**k-i))for i in range(n,2**k+1)]))