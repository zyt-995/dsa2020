t,m=map(int,input().split())
time=[]
val=[]
for i in range(m):
    ti,va=map(int,input().split())
    time.append(ti)
    val.append(va)
vol=[0]*(t+1)
for i in range(m):
    for j in range(t,time[i]-1,-1):
        vol[j]=max(vol[j],vol[j-time[i]]+val[i])
print(vol[-1])
