while True:
    n,k=map(int,input().split())
    if n==-1 and k==-1:
        break
    else:
        a=[]
        for _ in range(n):
            a.append(input())
        visited=[False for _ in range(n)]
        count=0
        def huisu(i,m):
            global count
            if m==k:
                count=count+1
                return
            if i>=n:
                return
            huisu(i+1,m)
            for lie in range(n):
                if a[i][lie]=='#' and visited[lie]==False:
                    visited[lie]=True
                    huisu(i+1,m+1)
                    visited[lie]=False
                else:
                    continue
        huisu(0,0)
        print(count)