#####################################################################
#创建字典
# 空字典
empty_dict = {}  # 或 dict()

# 带初始值的字典
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# 使用 dict() 构造函数
person = dict(name="Bob", age=25, city="London")

# 从键值对列表创建
pairs = [("name", "Charlie"), ("age", 35)]
person = dict(pairs)

# 使用字典推导式
squares = {x: x**2 for x in range(3)}  # {0: 0, 1: 1, 2: 4}
#################################################################
#访问字典
# 通过键访问值（键不存在时会报错）
name = person["name"]

# 使用 get() 方法（键不存在时返回默认值）
age = person.get("age", 0)  # 若键不存在，返回 0

# 检查键是否存在
if "city" in person:
    print("City:", person["city"])
################################################################
#修改字典
# 添加或更新键值对
person["age"] = 31  # 更新现有键
person["job"] = "Engineer"  # 添加新键

# 使用 update() 方法合并字典
new_info = {"city": "Paris", "hobbies": ["reading", "coding"]}
person.update(new_info)
#################################################################
#删除字典
# 删除指定键值对
del person["age"]

# 弹出指定键并返回值（键不存在时返回默认值）
job = person.pop("job", "Unknown")

# 弹出并返回最后插入的键值对（Python 3.7+）
last_item = person.popitem()

# 清空字典
person.clear()
###################################################################
#遍历字典
# 遍历键
for key in person:  # 或 person.keys()
    print(key)

# 遍历值
for value in person.values():
    print(value)

# 遍历键值对
for key, value in person.items():
    print(key, value)
####################################################################
# 浅拷贝（只复制顶层对象，嵌套对象共享引用）
copy1 = person.copy()
copy2 = dict(person)

# 深拷贝（递归复制所有嵌套对象）
import copy
deep_copy = copy.deepcopy(person)
#####################################################################
#字典推导式
# 从列表生成字典
numbers = [1, 2, 3]
squares = {x: x**2 for x in numbers}  # {1: 1, 2: 4, 3: 9}

# 过滤字典
ages = {"Alice": 25, "Bob": 30, "Charlie": 22}
adults = {name: age for name, age in ages.items() if age >= 25}