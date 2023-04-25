# def longest_increasing_subsequence(s,subseq=[],i=0):
#     if i==len(s):
#         return subseq
#     ans1=[]
#     if not subseq or subseq[-1]<s[i]:
#         ans1=longest_increasing_subsequence(s,subseq+[s[i]],i+1)
#     ans2=longest_increasing_subsequence(s,subseq,i+1)
#     if len(ans1)>len(ans2):
#         return ans1
#     else:
#         return ans2
# def longest_decreasing_subsequence(s,subseq=[],i=0):
#     if i==len(s):
#         return subseq
#     ans1=[]
#     if not subseq or subseq[-1]>s[i]:
#         ans1=longest_decreasing_subsequence(s,subseq+[s[i]],i+1)
#     ans2=longest_decreasing_subsequence(s,subseq,i+1)
#     if len(ans1)>len(ans2):
#         return ans1
#     else:
#         return ans2
#
def longest_increasing_subsequence(s):
    subseqs=[[m] for m in s]
    for i in range(1,len(s)):
        for j in range(i):
            if s[i]>s[j] and len(subseqs[i])<len(subseqs[j])+1:
                subseqs[i]=subseqs[j]+[s[i]]
    return sorted(subseqs,key=lambda x:len(x),reverse=True)[0]

def longest_decreasing_subsequence(s):
    subseqs=[[m] for m in s]
    for i in range(1,len(s)):
        for j in range(i):
            if s[i]<s[j] and len(subseqs[i])<len(subseqs[j])+1:
                subseqs[i]=subseqs[j]+[s[i]]
    return sorted(subseqs,key=lambda x:len(x),reverse=True)[0]

n=int(input())
perm=list(map(int,input().split()))
print(' '.join(map(str,longest_increasing_subsequence(perm))))
print(' '.join(map(str,longest_decreasing_subsequence(perm))))
