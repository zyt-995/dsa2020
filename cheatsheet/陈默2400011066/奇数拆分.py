def sep(start,N):
    if N==0:#基准条件一定不要丢
        return [[]]
    if N<start:
        return None
    if N==start and N%2==1:
        return [[N]]
    ans=[]
    for i in range(start,N+1,2):
        if sep(i+2,N-i):
            for k in sep(i+2,N-i):
                ans.append([i]+k)
    if ans:
       return ans
    return None
N=int(input())
ans=sep(1,N)
for i in ans:
    print(" ".join(map(str,i)))
print(len(ans))

