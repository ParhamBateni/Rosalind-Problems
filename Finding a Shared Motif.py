from Bio import SeqIO


# def lcs(s, t, n, m):
#
#     dp = [['' for i in range(m + 1)] for j in range(2)]
#     res = ''
#
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if (s[i - 1] == t[j - 1]):
#                 dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + s[i-1]
#                 if (len(dp[i % 2][j]) > len(res)):
#                     res = dp[i % 2][j]
#             else:
#                 dp[i % 2][j] = ''
#     return res
def global_lcs(seqs):
    seqs=sorted(seqs,key=lambda x:len(x))
    min_seq=seqs[0]
    for d in range(len(min_seq),1,-1):
        for i in range(len(min_seq)-d):
            subseq=min_seq[i:i+d]
            is_common=True
            for seq in seqs[1:]:
                if subseq not in seq:
                    is_common=False
                    break
            if is_common:
                return subseq
    return ''
fasta_seqs=SeqIO.parse(open('rosalind_input.txt','r'),'fasta')
seqs=[f.seq for f in fasta_seqs]
print(global_lcs(seqs))

