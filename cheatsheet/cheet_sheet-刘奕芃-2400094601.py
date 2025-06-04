#导弹拦截问题
n = int(input())
heights = list(map(int, input().split()))
dp = [1] * n  # 初始化每个位置的最长拦截数为1

for i in range(n):
    for j in range(i):
        if heights[j] >= heights[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))



#贪心背包问题
T, M = map(int, input().split())
herbs = [tuple(map(int, input().split())) for _ in range(M)]
dp = [0] * (T + 1)
for time, value in herbs:
    for j in range(T, time - 1, -1):
        dp[j] = max(dp[j], dp[j - time] + value)
print(dp[T])



#字符串递归
s = input()
d = {}  # 全局字典，用于缓存子问题的解

def steps(s):
    if s in d:  # 如果当前字符串已计算过，直接返回缓存结果
        return d[s]
    if len(s) < 2:  # 空串或单字符，无需操作
        d[s] = 0
        return 0
    if s[0] == s[-1]:  # 首尾字符相同，处理内部子串
        d[s] = steps(s[1:-1])
        return d[s]
    else:  # 首尾字符不同，尝试三种操作
        d[s] = min(
            steps(s[1:-1]),  # 修改操作（将首尾改为相同字符）
            steps(s[1:]),    # 删除左端或插入右端
            steps(s[:-1])    # 删除右端或插入左端
        ) + 1
        return d[s]

print(steps(s))  # 输出最终结果



#二分背包
def main():
    # 读取N和M
    n, m = map(int, input().split())
    
    # 读取N天的开销
    costs = [int(input()) for _ in range(n)]
    
    # 二分查找逻辑（与之前相同）
    left = max(costs)
    right = sum(costs)
    
    def is_possible(mid):
        count = 1
        current_sum = 0
        for cost in costs:
            if current_sum + cost > mid:
                count += 1
                current_sum = cost
            else:
                current_sum += cost
            if count > m:
                return False
        return count <= m
    
    while left < right:
        mid = (left + right) // 2
        if is_possible(mid):
            right = mid
        else:
            left = mid + 1
    
    print(left)

if __name__ == "__main__":
    main()


#二分查找月度开销
def main():
    # 读取N和M
    n, m = map(int, input().split())
    
    # 读取N天的开销
    costs = [int(input()) for _ in range(n)]
    
    # 二分查找逻辑（与之前相同）
    left = max(costs)
    right = sum(costs)
    
    def is_possible(mid):
        count = 1
        current_sum = 0
        for cost in costs:
            if current_sum + cost > mid:
                count += 1
                current_sum = cost
            else:
                current_sum += cost
            if count > m:
                return False
        return count <= m
    
    while left < right:
        mid = (left + right) // 2
        if is_possible(mid):
            right = mid
        else:
            left = mid + 1
    
    print(left)

if __name__ == "__main__":
    main()

#merge sort
def count_inversions(arr):
    # 归并排序并计算逆序对数量
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_merge = merge(left, right)
        total = inv_left + inv_right + inv_merge
        return merged, total

    def merge(left, right):
        result = []
        i = j = 0
        inv = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                inv += len(left) - i
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inv

    total = merge_sort(arr)
    return total

# 读取输入
N = int(input())
speeds = list(map(int, input().split()))

# 计算赶超事件的数量
inversions = count_inversions(speeds)
print(N*(N-1)//2-inversions[1])

#joseph
def josephus_simulation(n, k):
    # 初始化囚犯列表
    prisoners = list(range(1, n + 1))
    result = []
    index = 0  # 开始的位置

    while len(prisoners) > 1:
        # 计算下一个要处决的囚犯的索引
        index = (index + k - 1) % len(prisoners)
        # 将该囚犯添加到结果列表中
        result.append(prisoners[index])
        # 将该囚犯从列表中移除
        prisoners.pop(index)

    # 最后剩下的囚犯不会被处决
    return result

# 读取输入
n, k = map(int, input().split())

# 调用函数并输出结果
output = josephus_simulation(n, k)
print(' '.join(map(str, output)))

#汉诺塔
def hanoi(n, source, auxiliary, target):
    if n == 1:
        # 当只剩一个盘子时，直接从源座移到目标座
        print(f"{source}->{target}")
    else:
        # 步骤1：将 n-1 个盘子从源座移到辅助座（目标座作为辅助）
        hanoi(n - 1, source, target, auxiliary)
        # 步骤2：移动第 n 个盘子从源座到目标座
        print(f"{source}->{target}")
        # 步骤3：将 n-1 个盘子从辅助座移到目标座（源座作为辅助）
        hanoi(n - 1, auxiliary, source, target)

# 主程序：读取输入并调用函数
n = int(input())  # 输入盘子数目 n (n < 8)
hanoi(n, 'A', 'B', 'C')  # 初始调用：A 为源座，B 为辅助座，C 为目标座

#木材加工
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    logs = list(map(int, data[2:2+n]))
    
    # 计算最大长度和总长度
    max_len = max(logs)
    total = sum(logs)
    
    # 特判：总长度不足K，直接输出0
    if total < k:
        print(0)
        return
    
    left, right = 1, max_len
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for log in logs:
            count += log // mid  # 累加当前mid能切出的小段数
        
        if count >= k:
            result = mid        # 当前mid可行，记录结果
            left = mid + 1      # 尝试更大的长度
        else:
            right = mid - 1     # 尝试更小的长度
    
    # 输出最终结果（result或0）
    print(result if result >= 1 else 0)

if __name__ == "__main__":
    main()

#康托图像
def main():
    n = int(input().strip())
    s = '*'  # 初始状态（0步操作）
    for _ in range(n):
        new_s = []
        for char in s:
            if char == '*':
                new_s.append("*-*")  # 保留区间分成左中右三段
            else:
                new_s.append("---")  # 已删除部分保持删除状态
        s = ''.join(new_s)
    print(s)

if __name__ == "__main__":
    main()


#第一个不重复字符
from collections import Counter
def first_unique_char(s: str) -> int:
    # 统计每个字符的出现次数
    char_count = Counter(s)
    
    # 按顺序遍历字符串，找到第一个计数为1的字符
    for idx, char in enumerate(s):
        if char_count[char] == 1:
            return idx
    
    return -1  # 无唯一字符时返回-1

# 测试样例
print(first_unique_char("perpendicular"))  # 输出: 5


#矩形切割
def matrix(a,b):
    n=0
    while a!=0 and b!=0 :
        a,b= max(a,b)-min(a,b),min(a,b)
        n+=1
    return n
inp = input()
inp = inp.split()
a = int(inp[0])
b = int(inp[1])
print(matrix(a,b))


#波兰表达式
tokens = input().split()
reversed_tokens = tokens[::-1]
stack = []

for token in reversed_tokens:
    if token in '+-*/':
        a = stack.pop()
        b = stack.pop()
        if token == '+':
            stack.append(a + b)
        elif token == '-':
            stack.append(a - b)
        elif token == '*':
            stack.append(a * b)
        elif token == '/':
            stack.append(a / b)
    else:
        stack.append(float(token))

result = stack[0]
print("{0:.1f}".format(result))

#约瑟夫2
a=input().split()
n=int(a[0])
k=int(a[1])
last=[True for i in range(n+1)]
pos=n
killed=0
while(killed<n-1):
    order=0 #order is a number within k
    while(order<k):
        pos=pos%n+1
        if last[pos]:
            order+=1
    # find kth person and kill it (little period)
    killed+=1
    last[pos]=False
    print(pos,end=' ')



#幻方问题
n = int(input())
size = 2 * n - 1
# 初始化幻方矩阵
matrix = [[None for _ in range(size)] for _ in range(size)]

# 第一个数字的位置：第一行中间
row, col = 0, (size - 1) // 2
matrix[row][col] = 1

# 填充幻方
for k in range(2, size * size + 1):
    # 计算右上方位置（处理边界越界）
    next_row = (row - 1) % size
    next_col = (col + 1) % size
    
    # 检查是否需要下移（右上方被占或当前在右上角）
    if matrix[next_row][next_col] is not None or (row == 0 and col == size - 1):
        row = (row + 1) % size  # 下移一行，列不变
    else:
        row, col = next_row, next_col  # 移动到右上方
    
    matrix[row][col] = k

# 打印幻方
for r in matrix:
    print(' '.join(map(str, r)))



#同盘子放苹果问题
m, n = map(int, input().split())

# Handle the case where there are no apples
if m == 0:
    print(1)
else:
    # Initialize a DP table with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base case: 0 apples can be distributed in 1 way for any number of plates
    for j in range(n + 1):
        dp[0][j] = 1
    
    # Base case: 1 plate can hold all apples in 1 way
    for i in range(m + 1):
        dp[i][1] = 1
    
    # Fill the DP table
    for j in range(2, n + 1):  # Iterate over the number of plates
        for i in range(1, m + 1):  # Iterate over the number of apples
            # Case 1: At least one plate is empty
            dp[i][j] = dp[i][j-1]
            # Case 2: All plates have at least one apple (only if i >= j)
            if i >= j:
                dp[i][j] += dp[i-j][j]
    
    # The result is the value in dp[m][n]
    print(dp[m][n])



#螺旋
def main():
    import sys
    data = sys.stdin.readline().split()
    R = int(data[0])
    C = int(data[1])
    s = " ".join(data[2:])  # 处理可能包含空格的输入
    
    # 将字符转换为5位二进制字符串
    bin_str = ""
    for char in s:
        if char == ' ':
            bin_str += '00000'
        else:
            num = ord(char) - ord('A') + 1
            bin_str += format(num, '05b')
    
    # 补充0使长度等于矩阵大小
    total_bits = R * C
    if len(bin_str) < total_bits:
        bin_str += '0' * (total_bits - len(bin_str))
    
    # 生成螺旋顺序的坐标列表
    matrix = [[''] * C for _ in range(R)]
    top, bottom = 0, R - 1
    left, right = 0, C - 1
    order = []
    
    while top <= bottom and left <= right:
        # 从左到右遍历顶行
        for j in range(left, right + 1):
            order.append((top, j))
        top += 1
        
        # 从上到下遍历右列
        for i in range(top, bottom + 1):
            order.append((i, right))
        right -= 1
        
        if top <= bottom:  # 确保还有行未遍历
            # 从右到左遍历底行
            for j in range(right, left - 1, -1):
                order.append((bottom, j))
            bottom -= 1
        
        if left <= right:  # 确保还有列未遍历
            # 从下到上遍历左列
            for i in range(bottom, top - 1, -1):
                order.append((i, left))
            left += 1
    
    # 按螺旋顺序填充矩阵
    for idx, (i, j) in enumerate(order):
        matrix[i][j] = bin_str[idx]
    
    # 按行连接矩阵元素
    result = ""
    for row in matrix:
        result += "".join(row)
    print(result)

if __name__ == "__main__":
    main()



#两座孤岛的最短距离
n = int(input())
grid = []
for _ in range(n):
    s = input().strip()
    grid.append([int(c) for c in s])

# 标记两个孤岛为2和3
def dfs(i, j, label):
    if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
        grid[i][j] = label
        dfs(i + 1, j, label)
        dfs(i - 1, j, label)
        dfs(i, j + 1, label)
        dfs(i, j - 1, label)

label = 2
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            dfs(i, j, label)
            label += 1
            if label > 3:
                break
    if label > 3:
        break

from collections import deque
queue = deque()
distance = [[-1] * n for _ in range(n)]

# 初始化队列：第一个孤岛的所有点
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            queue.append((i, j))
            distance[i][j] = 0

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    i, j = queue.popleft()
    for dx, dy in dirs:
        ni, nj = i + dx, j + dy
        if 0 <= ni < n and 0 <= nj < n:
            # 遇到第二个孤岛，直接输出当前距离
            if grid[ni][nj] == 3:
                print(distance[i][j])
                exit()
            # 扩展未访问的0
            if grid[ni][nj] == 0 and distance[ni][nj] == -1:
                distance[ni][nj] = distance[i][j] + 1
                queue.append((ni, nj))



#寒假生活
n=int(input())
act=[]
for _ in range(n):
    s,e=input().split()
    act.append((int(e),int(s)))
act.sort()

endtime=-1
count=0
for e,s in act:
    if s>endtime:
        count+=1
        endtime=e
print(count)



#宝藏二叉树
n = int(input())
values = list(map(int, input().split()))

if n == 0:
    print(0)
    exit()

# 初始化dp数组，dp[i][0]表示选节点i，dp[i][1]表示不选
dp = [[0, 0] for _ in range(n + 1)]

# 从最后一个节点逆序处理到根节点
for i in range(n, 0, -1):
    left = 2 * i
    right = 2 * i + 1
    
    # 处理选中的情况
    selected = values[i-1]
    if left <= n:
        selected += dp[left][1]
    if right <= n:
        selected += dp[right][1]
    
    # 处理不选的情况
    unselected = 0
    left_max = 0
    if left <= n:
        left_max = max(dp[left][0], dp[left][1])
    right_max = 0
    if right <= n:
        right_max = max(dp[right][0], dp[right][1])
    unselected = left_max + right_max
    
    dp[i][0] = selected
    dp[i][1] = unselected

print(max(dp[1][0], dp[1][1]))



#合并果子
import heapq

n = int(input())
fruits = list(map(int, input().split()))

# 使用堆结构初始化所有果堆
heapq.heapify(fruits)
total = 0

# 循环合并直到只剩一堆
while len(fruits) > 1:
    # 取出两个最小的堆
    a = heapq.heappop(fruits)
    b = heapq.heappop(fruits)
    # 合并后累加体力消耗
    cost = a + b
    total += cost
    # 将新堆重新加入堆中
    heapq.heappush(fruits, cost)

print(total)



#八皇后问题
def solve_n_queens():
    def is_safe(row, col):
        # 检查列冲突
        for i in range(row):
            if board[i] == col:
                return False
            # 检查对角线冲突（行差=列差）
            if abs(board[i] - col) == abs(i - row):
                return False
        return True

    def print_solution():
        nonlocal count
        count += 1
        print(f"No. {count}")
        for i in range(8):
            line = []
            for j in range(8):
                line.append('1' if board[i] == j else '0')
            print(' '.join(line))

    def backtrack(row=0):
        if row == 8:
            print_solution()
            return
        for col in range(8):
            if is_safe(row, col):
                board[row] = col  # 放置皇后
                backtrack(row + 1)  # 递归下一行
                board[row] = -1   # 回溯

    count = 0
    board = [-1] * 8  # 初始化棋盘，-1表示空
    backtrack()
    print(f"Total solutions: {count}")

# 执行函数输出所有解
solve_n_queens()



#分派问题
import math

def can_divide(mid_volume, volumes, total_people):
    """检查给定体积mid_volume是否能分给所有人"""
    count = 0
    for v in volumes:
        count += math.floor(v / mid_volume)  # 每块派能切出的整数块数
    return count >= total_people  # 总块数需≥总人数

def main():
    # 读取输入
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])          # 派的数量
    f = int(data[1])          # 朋友数量
    radii = list(map(int, data[2:2+n]))  # 半径列表
    
    # 计算每个派的体积（圆柱体体积 = πr²h, h=1）
    volumes = [math.pi * r * r for r in radii]
    total_people = f + 1      # 总人数（朋友 + 自己）
    
    # 二分查找范围：0 到最大派的体积
    left, right = 0, max(volumes)
    # 精度控制：1e-5确保输出精确到小数点后三位
    while right - left > 1e-5:
        mid = (left + right) / 2
        if can_divide(mid, volumes, total_people):
            left = mid  # 可行，尝试更大的体积
        else:
            right = mid  # 不可行，减小体积
    
    # 输出结果（精确到三位小数）
    print("{:.3f}".format(left))

if __name__ == "__main__":
    main()



#24点问题
def solve24(nums):
    # 定义精度阈值，避免浮点数计算误差
    PRECISION = 1e-6
    
    # 递归求解函数
    def dfs(nums):
        n = len(nums)
        # 当只剩一个数字时，检查是否等于24
        if n == 1:
            return abs(nums[0] - 24) < PRECISION
        
        # 尝试所有数字组合
        for i in range(n):
            for j in range(n):
                if i == j:  # 跳过相同的索引
                    continue
                
                # 创建新列表，包含未被选中的数字
                new_nums = [nums[k] for k in range(n) if k != i and k != j]
                
                # 尝试所有可能的运算
                a, b = nums[i], nums[j]
                
                # 加法
                new_nums.append(a + b)
                if dfs(new_nums): 
                    return True
                new_nums.pop()
                
                # 减法1：a - b
                new_nums.append(a - b)
                if dfs(new_nums): 
                    return True
                new_nums.pop()
                
                # 减法2：b - a
                new_nums.append(b - a)
                if dfs(new_nums): 
                    return True
                new_nums.pop()
                
                # 乘法
                new_nums.append(a * b)
                if dfs(new_nums): 
                    return True
                new_nums.pop()
                
                # 除法1：a / b (b ≠ 0)
                if abs(b) > PRECISION: 
                    new_nums.append(a / b)
                    if dfs(new_nums): 
                        return True
                    new_nums.pop()
                
                # 除法2：b / a (a ≠ 0)
                if abs(a) > PRECISION:
                    new_nums.append(b / a)
                    if dfs(new_nums): 
                        return True
                    new_nums.pop()
        
        # 所有组合尝试失败
        return False
    
    return dfs(nums)

# 主程序
while True:
    data = input().split()
    nums = list(map(int, data))
    
    # 检查退出条件
    if nums == [0, 0, 0, 0]:
        break
    
    # 求解并输出结果
    print("YES" if solve24(nums) else "NO")



#白细胞计数
def main():
    n = int(input().strip())
    samples = []
    for _ in range(n):
        samples.append(float(input().strip()))
    
    # 对样本排序
    samples.sort()
    
    # 去除最小值和最大值
    valid_samples = samples[1:-1]  # 去掉第一个和最后一个
    
    # 计算平均值
    avg = sum(valid_samples) / len(valid_samples)
    
    # 计算误差（最大绝对差）
    max_diff = 0
    for sample in valid_samples:
        diff = abs(sample - avg)
        if diff > max_diff:
            max_diff = diff
    
    # 格式化输出，保留两位小数
    print(f"{avg:.2f} {max_diff:.2f}")

if __name__ == "__main__":
    main()



#求二叉树深度
n = int(input().strip())
nodes = [None] * (n + 1)  # 索引0不使用，1~n存储节点信息

# 读取每个节点的左右子节点信息
for i in range(1, n + 1):
    left, right = map(int, input().split())
    nodes[i] = (left, right)

def calc_depth(node_id):
    if node_id == -1:  # 空节点深度为0
        return 0
    left_child, right_child = nodes[node_id]  # 获取左右子节点
    # 当前节点深度 = 左右子树最大深度 + 1
    return max(calc_depth(left_child), calc_depth(right_child)) + 1

print(calc_depth(1))  # 从根节点（编号1）开始计算



#树的深度
from collections import deque

def main():
    n = int(input().strip())
    if n == 0:
        print(0)
        return
    
    # 存储每个节点的左右子节点
    tree = [None] * n
    # 标记节点是否有父节点（用于找根节点）
    has_parent = [False] * n
    
    # 读取输入并构建树结构
    for i in range(n):
        left, right = map(int, input().split())
        tree[i] = (left, right)
        if left != -1:
            has_parent[left] = True
        if right != -1:
            has_parent[right] = True
    
    # 寻找根节点（没有父节点的节点）
    root = None
    for i in range(n):
        if not has_parent[i]:
            root = i
            break
    
    # 层序遍历计算最大宽度
    queue = deque([root])
    max_width = 0
    
    while queue:
        level_size = len(queue)  # 当前层的节点数
        max_width = max(max_width, level_size)  # 更新最大宽度
        
        # 遍历当前层的所有节点
        for _ in range(level_size):
            node = queue.popleft()
            left, right = tree[node]
            
            # 将子节点加入队列
            if left != -1:
                queue.append(left)
            if right != -1:
                queue.append(right)
    
    print(max_width)

if __name__ == "__main__":
    main()



#回文切割
def main():
    import sys
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    results = []
    index = 1
    for _ in range(t):
        s = data[index].strip()
        index += 1
        n = len(s)
        if n == 0:
            results.append("0")
            continue
        
        # 预处理回文串信息：is_pal[i][j] 表示 s[i..j] 是否为回文
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    is_pal[i][j] = True
                elif j == i + 1:
                    is_pal[i][j] = (s[i] == s[j])
                else:
                    is_pal[i][j] = (s[i] == s[j] and is_pal[i+1][j-1])
        
        # 动态规划计算最小切割次数
        dp = [float('inf')] * n  # dp[i] 表示 s[0..i] 的最小切割次数
        for i in range(n):
            # 检查所有可能的回文子串 s[j..i]
            for j in range(0, i+1):
                if is_pal[j][i]:
                    if j == 0:  # 整个子串是回文，无需切割
                        dp[i] = 0
                    else:
                        # 在 j-1 和 j 之间切割：dp[j-1] + 1
                        dp[i] = min(dp[i], dp[j-1] + 1)
        
        results.append(str(dp[n-1]))
    
    # 输出所有结果
    print("\n".join(results))

if __name__ == "__main__":
    main()




#数字三角形
def main():
    n = int(input().strip())
    triangle = []
    for i in range(n):
        row = list(map(int, input().split()))
        triangle.append(row)
    
    # 从底向上计算最大路径和
    dp = triangle[-1][:]  # 初始化dp数组为最后一行
    for i in range(n-2, -1, -1):  # 从倒数第二行向上遍历
        for j in range(len(triangle[i])):
            # 状态转移方程：当前值 + 下方左右节点的较大值
            dp[j] = triangle[i][j] + max(dp[j], dp[j+1])
    
    print(dp[0])

if __name__ == "__main__":
    main()




#简单背包
def main():
    import sys
    data = sys.stdin.read().split()
    index = 0
    results = []
    
    while index < len(data):
        n = int(data[index])
        m = int(data[index+1])
        index += 2
        
        # 终止条件
        if n == 0 and m == 0:
            break
        
        # 读取物品体积
        volumes = list(map(int, data[index:index+m]))
        index += m
        
        # 初始化动态规划数组
        dp = [0] * (n + 1)
        dp[0] = 1  # 容量为0时方案数为1（不选任何物品）
        
        # 动态规划计算方案数
        for v in volumes:
            # 只考虑能放入背包的物品
            if v > n:
                continue
            # 完全背包：从小到大遍历容量
            for j in range(v, n + 1):
                dp[j] += dp[j - v]
        
        results.append(str(dp[n]))
    
    # 输出所有结果
    print("\n".join(results))

if __name__ == "__main__":
    main()



#猜二叉树
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(inorder, postorder):
    if not postorder:
        return None
    root_val = postorder[-1]
    root = TreeNode(root_val)
    idx = inorder.index(root_val)
    left_in = inorder[:idx]
    right_in = inorder[idx+1:]
    left_post = postorder[:len(left_in)]
    right_post = postorder[len(left_in):-1]
    root.left = build_tree(left_in, left_post)
    root.right = build_tree(right_in, right_post)
    return root

def level_order(root):
    if not root:
        return ""
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return "".join(result)

# 主程序
n = int(input().strip())
outputs = []
for _ in range(n):
    inorder = input().strip()
    postorder = input().strip()
    root = build_tree(inorder, postorder)
    outputs.append(level_order(root))

for res in outputs:
    print(res)



#合并果子
import heapq

n = int(input())
fruits = list(map(int, input().split()))

# 使用堆结构初始化所有果堆
heapq.heapify(fruits)
total = 0

# 循环合并直到只剩一堆
while len(fruits) > 1:
    # 取出两个最小的堆
    a = heapq.heappop(fruits)
    b = heapq.heappop(fruits)
    # 合并后累加体力消耗
    cost = a + b
    total += cost
    # 将新堆重新加入堆中
    heapq.heappush(fruits, cost)

print(total)



#二叉树
def count_nodes_in_subtree(m, n):
    count = 0
    left = m
    right = m
    while left <= n:
        count += min(right,n) - left + 1
        left = 2 * left
        right = 2 * right + 1
    return count

# 处理输入
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    print(count_nodes_in_subtree(m, n))



#重建二叉树
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return []
    
    root = preorder[0]
    root_idx = inorder.index(root)
    
    left_inorder = inorder[:root_idx]
    right_inorder = inorder[root_idx+1:]
    
    left_preorder = preorder[1:1+len(left_inorder)]
    right_preorder = preorder[1+len(left_inorder):]
    
    left_postorder = build_tree(left_preorder, left_inorder)
    right_postorder = build_tree(right_preorder, right_inorder)
    
    return left_postorder + right_postorder + [root]

def main():
    import sys
    for line in sys.stdin:
        preorder, inorder = line.strip().split()
        postorder = build_tree(list(preorder), list(inorder))
        print(''.join(postorder))

if __name__ == "__main__":
    main()



#最近临近祖先查询
from collections import deque

n, r = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

parent = [None] * (n + 1)
depth = [0] * (n + 1)
visited = [False] * (n + 1)

q = deque([r])
visited[r] = True
parent[r] = None
depth[r] = 1

while q:
    u = q.popleft()
    for v in edges[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            depth[v] = depth[u] + 1
            q.append(v)

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    # 生成x的祖先集合
    x_ancestors = set()
    current = x
    while current is not None:
        x_ancestors.add(current)
        current = parent[current]
    # 遍历y的路径寻找第一个公共祖先
    lca = r  # 默认值为根，但循环中会被覆盖
    current = y
    while current is not None:
        if current in x_ancestors:
            lca = current
            break
        current = parent[current]
    print(lca)



#树的转换
class Node:
    def __init__(self):
        self.children = []

class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None

def build_tree(s):
    root = Node()
    stack = [root]
    for c in s:
        if c == 'd':
            new_node = Node()
            stack[-1].children.append(new_node)
            stack.append(new_node)
        elif c == 'u':
            if len(stack) > 1:
                stack.pop()
    return root

def get_original_height(node):
    if not node.children:
        return 0
    max_h = 0
    for child in node.children:
        max_h = max(max_h, get_original_height(child))
    return max_h + 1

def convert_to_binary(node):
    if not node:
        return None
    b_node = TreeNode()
    if node.children:
        b_node.left = convert_to_binary(node.children[0])
        current = b_node.left
        for child in node.children[1:]:
            current.right = convert_to_binary(child)
            current = current.right
    return b_node

def binary_tree_height(node):
    if node is None:
        return -1
    left = binary_tree_height(node.left)
    right = binary_tree_height(node.right)
    return max(left, right) + 1

s = input().strip()
root = build_tree(s)
h1 = get_original_height(root)
binary_root = convert_to_binary(root)
h2 = binary_tree_height(binary_root)
print(f"{h1} => {h2}")



#奇数拆分
n = int(input())
result = []

def backtrack(start, current_sum, path):
    if current_sum == n:
        result.append(path)
        return
    max_next = n - current_sum
    # 生成候选数：从start+2开始，到max_next，步长为2
    next_start = start + 2
    for next_num in range(next_start, max_next + 1, 2):
        # 确保下一个数是正奇数
        if next_num % 2 == 1:
            backtrack(next_num, current_sum + next_num, path + [next_num])

# 初始调用，start为-1，这样第一个候选数为1
backtrack(-1, 0, [])

# 按字典序输出
for each in result:
    print(' '.join(map(str, each)))
print(len(result))




#小木棍
def find_min_length(segments):
    segments.sort(reverse=True)
    total = sum(segments)
    max_len = segments[0] if segments else 0

    # 生成所有可能的L候选，按从小到大顺序
    for L in range(max_len, total + 1):
        if total % L != 0:
            continue
        group_num = total // L
        used = [False] * len(segments)
        if backtrack(segments, L, group_num, used, 0, 0):
            return L
    return total  # 所有段只能组成一根原木棍

def backtrack(segments, L, groups_left, used, current_sum, start_idx):
    if groups_left == 0:
        return True
    if current_sum == L:
        return backtrack(segments, L, groups_left - 1, used, 0, 0)
    
    for i in range(start_idx, len(segments)):
        if not used[i]:
            if current_sum + segments[i] > L:
                continue
            # 剪枝：跳过与前一个相同且未使用的元素
            if i > 0 and segments[i] == segments[i-1] and not used[i-1]:
                continue
            # 剪枝：如果当前组未选任何元素，但跳过相同元素
            if current_sum == 0 and i > 0 and segments[i] == segments[i-1] and not used[i-1]:
                continue
            
            used[i] = True
            if backtrack(segments, L, groups_left, used, current_sum + segments[i], i + 1):
                return True
            used[i] = False
            # 剪枝：无法找到当前组的第一个元素，后续无法组成
            if current_sum == 0:
                break
    return False

# 处理输入输出
import sys

for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    segments = list(map(int, sys.stdin.readline().split()))
    print(find_min_length(segments))



#简单整数规划问题
max_n = 50
dp = [[0] * (max_n + 1) for _ in range(max_n + 1)]

# 初始化基础情况
for j in range(max_n + 1):
    dp[0][j] = 1  # 总和为0时，有一种划分方式

# 填充动态规划表
for i in range(1, max_n + 1):
    for j in range(1, max_n + 1):
        if j > i:
            dp[i][j] = dp[i][i]
        else:
            dp[i][j] = dp[i - j][j] + dp[i][j - 1]

# 处理输入并输出结果
import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    if n == 0:
        break
    print(dp[n][n])




#位查询
import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr +=1
    M = int(input[ptr])
    ptr +=1
    nums = list(map(int, input[ptr:ptr+N]))
    ptr += N

    # Preprocess for each bit position 0 to 15
    max_bit = 15
    cnt = []
    pre_sum = []
    for i in range(max_bit +1):
        mask = 1 << (i +1)
        cnt_i = [0] * mask
        for x in nums:
            r = x % mask
            cnt_i[r] +=1
        # Compute prefix sums
        pre_sum_i = [0] * mask
        pre_sum_i[0] = cnt_i[0]
        for r in range(1, mask):
            pre_sum_i[r] = pre_sum_i[r-1] + cnt_i[r]
        cnt.append(cnt_i)
        pre_sum.append(pre_sum_i)

    delta_sum = 0
    for _ in range(M):
        op = input[ptr]
        ptr +=1
        if op == 'C':
            d = int(input[ptr])
            ptr +=1
            delta_sum = (delta_sum + d) % 65536
        else:
            i = int(input[ptr])
            ptr +=1
            mask = 1 << (i +1)
            d_prime = delta_sum % mask
            low = ( (1 << i) - d_prime ) % mask
            high = (mask -1 - d_prime) % mask

            pre_sum_i = pre_sum[i]
            mask_i = mask
            if low <= high:
                if low >0:
                    total = pre_sum_i[high] - pre_sum_i[low-1]
                else:
                    total = pre_sum_i[high]
            else:
                part1 = pre_sum_i[mask_i -1] - (pre_sum_i[low-1] if low >0 else 0)
                part2 = pre_sum_i[high]
                total = part1 + part2
            print(total)

if __name__ == "__main__":
    main()



#阿侬诺
from collections import deque

def main():
    T = int(input())
    for _ in range(T):
        R, C = map(int, input().split())
        maze = []
        start = None
        end = None
        for i in range(R):
            row = input().strip()
            maze.append(row)
            for j in range(C):
                if row[j] == 'S':
                    start = (i, j)
                elif row[j] == 'E':
                    end = (i, j)
        # 初始化BFS
        visited = [[False for _ in range(C)] for _ in range(R)]
        queue = deque()
        queue.append((start[0], start[1], 0))
        visited[start[0]][start[1]] = True
        found = False
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y, steps = queue.popleft()
            if (x, y) == end:
                print(steps)
                found = True
                break
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    if maze[nx][ny] != '#' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, steps + 1))
        if not found:
            print("oop!")

if __name__ == "__main__":
    main()



#城堡问题
def solve():
    import sys
    sys.setrecursionlimit(1000000)
    
    m = int(input())
    n = int(input())
    grid = []
    for _ in range(m):
        row = list(map(int, input().split()))
        grid.append(row)
    
    visited = [[False for _ in range(n)] for _ in range(m)]
    directions = [ (0, -1), (-1, 0), (0, 1), (1, 0) ]  # West, North, East, South
    wall = [1, 2, 4, 8]  # Corresponding to West, North, East, South
    
    def dfs(x, y):
        stack = [(x, y)]
        visited[x][y] = True
        size = 0
        while stack:
            cx, cy = stack.pop()
            size += 1
            for i in range(4):
                dx, dy = directions[i]
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and not (grid[cx][cy] & wall[i]):
                    visited[nx][ny] = True
                    stack.append((nx, ny))
        return size
    
    room_count = 0
    max_room_size = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                room_size = dfs(i, j)
                room_count += 1
                if room_size > max_room_size:
                    max_room_size = room_size
    
    print(room_count)
    print(max_room_size)

solve()



#棋盘问题
def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    while True:
        n = int(input[ptr])
        k = int(input[ptr+1])
        ptr += 2
        if n == -1 and k == -1:
            break
        board = []
        for _ in range(n):
            line = input[ptr].strip()
            ptr += 1
            board.append(list(line))
        
        count = 0
        
        def backtrack(row, mask, placed):
            nonlocal count
            remaining = k - placed
            # 剩余行数不足时剪枝
            if (n - row) < remaining:
                return
            # 成功放置k个棋子
            if placed == k:
                count += 1
                return
            # 所有行处理完毕
            if row >= n:
                return
            
            # 尝试在当前行放置棋子
            for col in range(n):
                if board[row][col] == '#' and not (mask & (1 << col)):
                    backtrack(row + 1, mask | (1 << col), placed + 1)
            # 不放置当前行，继续处理下一行
            backtrack(row + 1, mask, placed)
        
        backtrack(0, 0, 0)
        print(count)

if __name__ == "__main__":
    main()



#PKU爱消除
def remove_pku(s):
    stack = []  # 初始化栈
    for char in s:  # 遍历每个字符
        stack.append(char)  # 压入当前字符
        # 循环检查栈顶是否形成 "PKU"
        while len(stack) >= 3 and stack[-1] == 'U' and stack[-2] == 'K' and stack[-3] == 'P':
            # 弹出栈顶的三个字符（消除 "PKU"）
            stack.pop()  # 移除 'U'
            stack.pop()  # 移除 'K'
            stack.pop()  # 移除 'P'
    return ''.join(stack)  # 将栈内字符拼接为字符串
s=str(input())
print(remove_pku(s))




#二分问题 aggressive cow
n,c=map(int,input().split())
stalls=sorted(int(input()) for _ in range(n))

low,high=0,stalls[-1]-stalls[0]
def can_place_cow(dist):
    count=1
    last=stalls[0]
    for i in range(1,n):
        if stalls[i]-last>=dist:
            count+=1
            last=stalls[i]
            if count==c:
                return True
    return False

while low<high:
    mid=(low+high+1)//2
    if can_place_cow(mid):
        low=mid
    else:
        high=mid-1
print(low)



#不简单的出战统计
n = int(input().strip())
c = 1  # 初始化 C₀ = 1
for i in range(1, n + 1):
    c = (4 * i - 2) * c // (i + 1)  # 整数除法确保精确
print(c)



#薛定谔的二叉树
import sys

def has_duplicate(s):
    """检查序列是否有重复字符"""
    return len(s) != len(set(s))

def count_tree(pre, post):
    n = len(pre)
    if n == 0:
        return 1  # 空树只有一种情况
    if pre[0] != post[-1]:
        return 0  # 根节点不匹配
    if n == 1:
        return 1  # 单节点树只有一种情况
    
    try:
        # 在 post[0:n-1] 中查找 pre[1] 的位置
        idx = post.index(pre[1], 0, n-1)
    except ValueError:
        return 0  # 未找到，无效序列
    
    left_size = idx + 1  # 左子树节点数
    right_size = n - 1 - left_size  # 右子树节点数
    
    if right_size == 0:
        # 只有一个子树（左或右），两种可能
        subtree = count_tree(pre[1:1+left_size], post[0:left_size])
        return 2 * subtree
    else:
        # 两个子树，递归计算左右子树
        left_count = count_tree(pre[1:1+left_size], post[0:left_size])
        right_count = count_tree(pre[1+left_size:], post[left_size:n-1])
        return left_count * right_count

# 处理多组输入
for line in sys.stdin:
    data = line.split()
    if len(data) < 2:
        continue  # 跳过无效行
    pre_str, post_str = data[0], data[1]
    
    # 检查重复字符或长度不等
    if has_duplicate(pre_str) or has_duplicate(post_str) or len(pre_str) != len(post_str):
        print(0)
    else:
        print(count_tree(pre_str, post_str))



#树转儿子兄弟
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.firstChild = None  # 左指针，指向第一个子节点
        self.nextSibling = None  # 右指针，指向下一个兄弟节点

def build_tree(tree_dict, node_val):
    """递归构建儿子-兄弟二叉树"""
    node = TreeNode(node_val)
    if node_val in tree_dict and tree_dict[node_val]:
        children = tree_dict[node_val]
        # 第一个孩子作为左孩子
        node.firstChild = build_tree(tree_dict, children[0])
        # 剩余孩子作为右兄弟链
        cur = node.firstChild
        for child_val in children[1:]:
            cur.nextSibling = build_tree(tree_dict, child_val)
            cur = cur.nextSibling
    return node

def postorder_traversal(root):
    """后序遍历二叉树"""
    if not root:
        return []
    left = postorder_traversal(root.firstChild)  # 遍历左子树（第一个孩子）
    right = postorder_traversal(root.nextSibling)  # 遍历右子树（兄弟链）
    return left + right + [root.val]  # 左 → 右 → 根

def main():
    import sys
    data = sys.stdin.read().splitlines()
    tree_dict = {}
    root_val = None
    
    # 解析输入
    for line in data:
        if not line.strip():
            continue
        parts = line.split()
        if not parts:
            continue
        if root_val is None:  # 第一行的第一个字母是根
            root_val = parts[0]
        tree_dict[parts[0]] = parts[1:]  # 存储父节点和子节点列表
    
    # 构建二叉树并遍历
    if root_val is None:
        print("")
    else:
        root = build_tree(tree_dict, root_val)
        result = postorder_traversal(root)
        print("".join(result))

if __name__ == "__main__":
    main()