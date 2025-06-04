'''
描述
An ascending sorted sequence of distinct values is one in which some form of a less-than operator is used to order the elements from smallest to largest. For example, the sorted sequence A, B, C, D implies that A < B, B < C and C < D. in this problem, we will give you a set of relations of the form A < B and ask you to determine whether a sorted order has been specified or not.

输入
Input consists of multiple problem instances. Each instance starts with a line containing two positive integers n and m. the first value indicated the number of objects to sort, where 2 <= n <= 26. The objects to be sorted will be the first n characters of the uppercase alphabet. The second value m indicates the number of relations of the form A < B which will be given in this problem instance. Next will be m lines, each containing one such relation consisting of three characters: an uppercase letter, the character "<" and a second uppercase letter. No letter will be outside the range of the first n letters of the alphabet. Values of n = m = 0 indicate end of input.
输出
For each problem instance, output consists of one line. This line should be one of the following three:

Sorted sequence determined after xxx relations: yyy...y.
Sorted sequence cannot be determined.
Inconsistency found after xxx relations.

where xxx is the number of relations processed at the time either a sorted sequence is determined or an inconsistency is found, whichever comes first, and yyy...y is the sorted, ascending sequence.
样例输入
4 6
A<B
A<C
B<C
C<D
B<D
A<B
3 2
A<B
B<A
26 1
A<Z
0 0
样例输出
Sorted sequence determined after 4 relations: ABCD.
Inconsistency found after 2 relations.
Sorted sequence cannot be determined.
'''

def main():
    import sys
    data = sys.stdin.read().splitlines()
    index = 0
    results = []
    while index < len(data):
        line = data[index].strip()
        index += 1
        if line == "0 0":
            break
        n, m = map(int, line.split())
        nodes = [chr(ord('A') + i) for i in range(n)]
        graph = {node: [] for node in nodes}
        indegree = {node: 0 for node in nodes}
        solved = False
        break_index = -1
        
        for i in range(m):
            s = data[index].strip()
            index += 1
            a, b = s[0], s[2]
            if b in graph[a]:
                pass
            else:
                graph[a].append(b)
                indegree[b] += 1
            
            indegree_copy = indegree.copy()
            queue = [node for node in nodes if indegree_copy[node] == 0]
            topo_order = []
            has_multiple = False
            while queue:
                if len(queue) > 1:
                    has_multiple = True
                u = queue.pop(0)
                topo_order.append(u)
                for v in graph[u]:
                    indegree_copy[v] -= 1
                    if indegree_copy[v] == 0:
                        queue.append(v)
            
            if len(topo_order) < len(nodes):
                results.append(f"Inconsistency found after {i+1} relations.")
                solved = True
                break_index = i
                break
            elif not has_multiple and len(topo_order) == len(nodes):
                seq = ''.join(topo_order)
                results.append(f"Sorted sequence determined after {i+1} relations: {seq}.")
                solved = True
                break_index = i
                break
        
        if solved:
            for j in range(i+1, m):
                index += 1
        else:
            results.append("Sorted sequence cannot be determined.")
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()















'''
class Graph():
    def __init__(self):
        self.vertlist={}

class Vertex():
    def __init__(self,key):
        self.nbrs={}
        self.id=key 
        self.indgree=self.outdegree=0
        self.pre=[]
        self.dis=0
    
    def addNei(self,nbr,weight=1):#nbr不是节点是名字
        self.nbrs[nbr]=weight

def Check():
    for t in range(m):
        for item in g.vertlist.values():
            if item.id in sequence:
                continue   
            is_fir=True
            for father in item.pre:
                if father not in sequence:
                    is_fir=False
                    break
                if len(sequence) and father==sequence[-1] and len(sequence)==t+1:
                    is_fir=False
                    break 
            if is_fir:
                sequence.append(item.id)
        if len(sequence)>t+1:
            has_problem=False


while True:
    m,n=map(int,input().split())
    g=Graph()
    if m+n==0:
        break 
    solved=False
    datas=[]
    for _ in range(n):
        data=list(input())
        if solved:
            continue
        datas.append(data)
        if data[0] not in g.vertlist:
            g.vertlist[data[0]]=Vertex(data[0])
        if data[2] not in g.vertlist:
            g.vertlist[data[2]]=Vertex(data[2])
        data[0]=g.vertlist[data[0]]
        data[0].addNei(data[2])
        data[2]=g.vertlist[data[2]]
        data[2].pre.append(data[0].id)
        sequence=[]
        if len(g.vertlist)==m and n>=m-1:
            sequence=[]
            has_problem=False
            Check()
            if len(sequence)==m and has_problem==False:
                print("Sorted sequence determined after "+str(len(datas))+" relations: "+"".join(sequence)+".")
                solved=True
            if len(sequence)==m and has_problem:
                if len(datas)==n:
                    print("Sorted sequence cannot be determined.")
            if len(sequence)<m:
                print(f"Inconsistency found after {len(datas)} relations.")
                solved=True
        elif len(datas)==n :
            Check()
            if len(sequence)==len(g.vertlist):              
                print("Sorted sequence cannot be determined.")
            if len(sequence)<len(g.vertlist):
                print(f"Inconsistency found after {len(datas)} relations.")
        else:
            Check()
            if len(sequence)<len(g.vertlist):
                print(f"Inconsistency found after {len(datas)} relations.")
                solved=True
'''




            
        
        

        
