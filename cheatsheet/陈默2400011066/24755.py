import math
ans=0
def count(target,now,prelevel):
    global ans
    if now==target:
        ans+=1
    if now>target:
        return
    if now<target:
        for i in range(1,2*prelevel+1):
            for j in range(math.comb(2*prelevel,i)):
               count(target,now+i,i)
n=int(input())
count(n,1,1)
print(ans)
