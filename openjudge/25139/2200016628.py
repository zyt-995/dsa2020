import itertools


def solve_single_equation():
    s1, s2, s3 = input().split()

    # 提取当前等式中出现的所有不同的字母，并进行排序
    unique_letters_in_equation = sorted(list(set(s1 + s2 + s3)))
    # k 是字母总数,最多不超过5个
    k = len(unique_letters_in_equation)

    # 枚举所有排列
    digits = range(10) #准备数字 0~9
    found_solutions = [] #保存所有合法解的列表

    # 对 digits 的 k 个位置进行排列组合，生成所有可能的 k 个不同数字分配方案。总共最多 P(10,5) = 30240 种。
    for p_digits in itertools.permutations(digits, k):
        mapping = {}

        #构建从每个字母到数字的映射
        for i in range(k):
            mapping[unique_letters_in_equation[i]] = p_digits[i]

        # 字母替换为数字字符串
        s1_val_str = "".join(str(mapping[char]) for char in s1)
        s2_val_str = "".join(str(mapping[char]) for char in s2)
        s3_val_str = "".join(str(mapping[char]) for char in s3)

        # 检查前导零
        if (len(s1_val_str) > 1 and s1_val_str[0] == '0') or \
                (len(s2_val_str) > 1 and s2_val_str[0] == '0') or \
                (len(s3_val_str) > 1 and s3_val_str[0] == '0'):
            continue

        num1 = int(s1_val_str)
        num2 = int(s2_val_str)
        num3 = int(s3_val_str)

        # 判断加法是否成立
        if num1 + num2 == num3:
            # 构建排序键
            sort_key_values = []
            canonical_letters = ['A', 'B', 'C', 'D', 'E']
            for char_code in canonical_letters:
                sort_key_values.append(mapping.get(char_code, 10))#不存在的字母赋值为 10（高于任何合法数字0-9）

            found_solutions.append(
                (tuple(sort_key_values), s1_val_str, s2_val_str, s3_val_str)
            )

    if not found_solutions:
        print("No Solution")
    else:
        # 如果有合法解，按 sort_key 排序后取第一个（最小解）
        found_solutions.sort(key=lambda x: x[0])
        best_sol = found_solutions[0]
        print(f"{best_sol[1]}+{best_sol[2]}={best_sol[3]}")

n = int(input())
for _ in range(n):
    solve_single_equation()