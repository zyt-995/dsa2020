from math import log2
def num(m,n):
    k=int(log2(n/m))
    if m*2**k+2**k-1<=n:
        return 2**(k+1)-1
    else:
        return 2**k+n-m*2**k
while True:
    m,n=map(int,input().split())
    if m==n==0:
        break
    else:
        print(num(m,n))