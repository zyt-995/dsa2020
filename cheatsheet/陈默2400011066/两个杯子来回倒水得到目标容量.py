#此题使用bfs
from collections import deque
def bfs(A,B,C):
    queue = deque([((0,0),[])])
    visited = {(0,0)}
    while queue:
        (a,b),path = queue.popleft()
        if a == C or b==C:
            print(len(path))
            for p in path:
                print(p)
            return
        #fill(1)
        if (A,b) not in visited:
            visited.add((A,b))
            queue.append(((A,b),path+["FILL(1)"]))
        #fill(2)
        if (a,B) not in visited:
            visited.add((a,B))
            queue.append(((a,B),path+["FILL(2)"]))
        #drop(1)
        if (0,b) not in visited:
            visited.add((0,b))
            queue.append(((0,b),path+["DROP(1)"]))
        #drop(2)
        if (a,0) not in visited:
            visited.add((a,0))
            queue.append(((a,0),path+["DROP(2)"]))
        #pour(2,1)
        i=min(a+b,A)
        j=max(0,b-A+a)
        if (i,j) not in visited:
            visited.add((i,j))
            queue.append(((i,j),path+["POUR(2,1)"]))
        i=max(0,a-B+b)
        j=min(a+b,B)
        if (i,j) not in visited:
            visited.add((i,j))
            queue.append(((i,j),path+["POUR(1,2)"]))
    print("impossible")
    return
A,B,C=map(int,input().split())
bfs(A,B,C)