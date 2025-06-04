# 排序
numbers = [3, 1, 4]
numbers.sort()          # 原地排序：[1, 3, 4]
sorted_numbers = sorted(numbers)  # 返回新列表

# 反转
numbers.reverse()       # 原地反转：[4, 3, 1]

# 添加元素
numbers.append(5)       # [100, 2, 3, 4, 5]
numbers.insert(1, 200)  # [100, 200, 2, 3, 4, 5]

# 删除元素
del numbers[0]          # [200, 2, 3, 4, 5]
numbers.pop()           # 弹出最后一个元素（返回 5）
numbers.remove(2)       # 删除第一个值为 2 的元素

# 查找
print(text.find("World"))  # 输出: 7（找不到返回 -1）

# 判断开头/结尾
print(text.startswith("Hello"))  # True
print(text.endswith("!"))        # True

# 计数
print(text.count("l"))           # 输出: 3