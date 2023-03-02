k,m,n=map(int,input().split())
s=k+m+n
print((1-((m+n)*(m+n-1)/(s*(s-1))))+m/s*(m-1)/(s-1)*3/4+2*m*n/(s*(s-1))*1/2)