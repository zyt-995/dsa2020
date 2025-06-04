#########################################################
#创建集合
# 空集合（必须用 set()，不能用 {}，因为 {} 创建的是字典）
empty_set = set()

# 带初始值的集合
fruits = {"apple", "banana", "cherry"}

# 从列表/元组创建集合（自动去重）
numbers = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# 使用集合推导式
squares = {x**2 for x in range(3)}  # {0, 1, 4}
#######################################################
# 添加单个元素
fruits.add("date")

# 添加多个元素（从可迭代对象）
fruits.update(["elderberry", "fig"])
# 删除指定元素（元素不存在时会报错）
fruits.remove("banana")

# 删除指定元素（元素不存在时不报错）
fruits.discard("grape")

# 随机删除并返回一个元素
random_fruit = fruits.pop()

# 清空集合
fruits.clear()
############################################################
#集合运算
#并集
a = {1, 2, 3}
b = {3, 4, 5}
union = a | b  # 或 a.union(b)  # {1, 2, 3, 4, 5}
#交集
intersection = a & b  # 或 a.intersection(b)  # {3}