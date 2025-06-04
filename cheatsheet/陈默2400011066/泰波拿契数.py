def tbnq(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return tbnq(n-1)+tbnq(n-2)+tbnq(n-3)
n=int(input())
print(tbnq(n))