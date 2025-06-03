n=int(input())
lst=list(map(int,input().split()))
selected=[0]*(n+1)
unselected=[0]*(n+1)
for i in range(n,0,-1):
    maxval=lst[i-1]
    left=2*i
    right=2*i+1
    if left<=n:
        maxval+=unselected[left]
    if right<=n:
        maxval+=unselected[right]
    selected[i]=maxval
    maxval1=0
    if left<=n:#注意这里，两个相连节点不是非要选一个
        maxval1+=max(selected[left],unselected[left])
    if right<=n:
        maxval1+=max(selected[right],unselected[right])
    unselected[i]=maxval1
print(max(selected[1],unselected[1]))