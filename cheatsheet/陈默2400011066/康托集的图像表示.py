def kangtuo(n):
    if n==0:
        return "*"
    return kangtuo(n-1)+"-"*(3**(n-1))+kangtuo(n-1)
n=int(input())
print(kangtuo(n))