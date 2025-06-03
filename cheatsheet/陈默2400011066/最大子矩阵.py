N = int(input())
arr = []
while len(arr) < N * N:
    arr += list(map(int, input().split()))
matrix = [arr[i*N : (i+1)*N] for i in range(N)]
ans=float('-inf')
prefix=[[0]*(N+1) for i in range(N)]
for j in range(N):
    for i in range(1,N+1):
        prefix[j][i]=prefix[j][i-1]+matrix[i-1][j]
ans=float("-inf")
for i in range(N):
    for j in range(i,N):
        sumlst=[]
        for k in range(N):
            temp=prefix[k][j+1]-prefix[k][i]
            sumlst.append(temp)
        curr=sumlst[0]
        maxsub=sumlst[0]
        for num in sumlst[1:]:
            curr=max(num,curr+num)
            maxsub=max(curr,maxsub)
        if maxsub>ans:
            ans=maxsub
print(ans)