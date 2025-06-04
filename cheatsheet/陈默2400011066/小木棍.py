def stick(lst):
    total=sum(lst)
    minstick=max(lst)
    used=[False]*len(lst)
    sortedlst=sorted(lst,reverse=True)
    def dfs(start,curr,target,count):
        if count==total//target:
            return True
        if curr==target:
            return dfs(0,0,target,count+1)

        prefail=-1
        for i in range(start,len(lst)):
            if curr+sortedlst[i]>target or sortedlst[i]==prefail:
                prefail=sortedlst[i]
                continue
            else:
                if not used[i]:
                    used[i]=True
                    if dfs(i+1,curr+sortedlst[i],target,count):
                        return True
                    used[i]=False
                    prefail=sortedlst[i]
        return False
    for i in range(minstick,total+1):
        if total%i==0 and dfs(0,0,i,0):
            return i
while True:
    n=int(input())
    if n==0:
        break
    lst=list(map(int,input().split()))
    print(stick(lst))

