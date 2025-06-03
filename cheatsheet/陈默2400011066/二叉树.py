from math import log2
def count(n,m):
    k=int(log2(n/m))
    end=(2**k)*m+2**k-1
    if end<=n:
        return 2**(k+1)-1
    else:
        return 2**k+n-m*(2**k)
while True:
    m,n=map(int,input().split())
    if n==0 and m==0:
        break
    print(count(n,m))