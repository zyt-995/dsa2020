numbers = [-3, 2, -1, 5, -4]
sorted_by_abs = sorted(numbers, key=abs)  # [1, 2, 3, 4, 5]
words = ["apple", "banana", "cherry", "date"]
sorted_by_length = sorted(words, key=len)  # ['date', 'apple', 'banana', 'cherry']
# 对元组列表按第二个元素排序
students = [("Alice", 25), ("Bob", 20), ("Charlie", 22)]
sorted_by_age = sorted(students, key=lambda x: x[1])
# [('Bob', 20), ('Charlie', 22), ('Alice', 25)]
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_by_score = sorted(scores.items(), key=lambda item: item[1])
# [('Charlie', 78), ('Alice', 85), ('Bob', 92)]
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
descending = sorted(numbers, reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1]

text = "python"
sorted_chars = sorted(text)  # ['h', 'n', 'o', 'p', 't', 'y']