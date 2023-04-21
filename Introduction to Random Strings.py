from math import log10
from matplotlib import pyplot as plt
import numpy as np
s=input()
A=list(map(float,input().split()))
# A=np.arange(0.1,0.99,0.05)
log_probs=[]
for i in range(len(A)):
    log_prob=0
    for j in range(len(s)):
        if s[j] in ['A','T']:
            log_prob+=log10((1-A[i])/2)
        else:
            log_prob+=log10(A[i]/2)
    print(round(log_prob,3),end=' ' if i<len(A)-1 else '\n')
    log_probs.append(log_prob)

# plt.plot(A,log_probs,color='green')
# plt.show()