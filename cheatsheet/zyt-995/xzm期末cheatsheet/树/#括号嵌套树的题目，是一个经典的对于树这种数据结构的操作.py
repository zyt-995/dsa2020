#括号嵌套树的题目，是一个经典的对于树这种数据结构的操作
class Tree:
    def __init__(self,value,next=None,father=None):#注意，传入的东西必须是一个不可变数据类型
        self.value=value
        self.next = next if next is not None else []#标准的建立next的方法
        self.father=father
    def addtree(self,son):
        self.next.append(son)
    def pre(self,op):
        op(self)
        for son in self.next:
            son.pre(op)
    def post(self,op):
        for son in self.next:
            son.post(op)
        op(self)
s=input()
stack=[]
root=Tree(s[0])
stack.append(root)
for i in range(1,len(s)):
    if s[i]=='(' :
        continue
    elif s[i]==')' or s[i]==',':
        stack.pop()
    else:
        father=stack[-1]
        son=Tree(s[i])
        father.addtree(son)
        stack.append(son)
root.pre(lambda x:print(x.value,end=''))
print()
root.post(lambda x:print(x.value,end=''))