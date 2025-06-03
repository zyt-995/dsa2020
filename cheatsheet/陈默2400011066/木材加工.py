def cut(lst,currl):
    count = 0
    for i in lst:
        count += i//currl
    return count
n,k=map(int,input().split())
logs=[]
for i in range(n):
    l=int(input())
    logs.append(l)
start=0
end=max(logs)
while start<end:
    mid=(start+end+1)//2
    if cut(logs,mid)<k:
        end=mid-1
    else:
        start=mid
print(start)

