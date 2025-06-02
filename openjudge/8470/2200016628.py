import sys

def calculate_overlap(s1, s2):
    """
    计算s1的后缀与s2的前缀的最大重叠长度。
    """
    max_overlap = 0
    # 从s1的长度-1开始到1（重叠长度至少为1）
    for i in range(1, min(len(s1), len(s2)) + 1):
        # 检查s1的最后i个字符是否与s2的前i个字符相同
        if s1[-i:] == s2[:i]:
            max_overlap = i
    return max_overlap

def solve():
    T = int(sys.stdin.readline())
    results = []

    for _ in range(T):
        N = int(sys.stdin.readline())
        fragments = []
        for i in range(N):
            fragments.append(sys.stdin.readline().strip())

        # Step 1: 消除冗余基因片段
        # is_redundant[i] 为 True 表示第 i 个片段是冗余的
        is_redundant = [False] * N
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                # 如果 fragments[i] 包含 fragments[j]，则 fragments[j] 是冗余的
                if fragments[i].find(fragments[j]) != -1:
                    is_redundant[j] = True
        
        # 过滤掉冗余片段
        filtered_fragments = [fragments[i] for i in range(N) if not is_redundant[i]]
        
        # 如果所有片段都被过滤掉（极端情况，所有片段都被包含），或者只剩下一个，直接返回最长片段的长度
        if not filtered_fragments:
            results.append(0) # 或者根据题目定义返回什么
            continue
        if len(filtered_fragments) == 1:
            results.append(len(filtered_fragments[0]))
            continue

        num_fragments = len(filtered_fragments)
        
        # Step 2: 计算任意两个基因片段之间的最大重叠长度
        # overlap_matrix[i][j] 表示 filtered_fragments[i] 的后缀与 filtered_fragments[j] 的前缀的最大重叠长度
        overlap_matrix = [[0] * num_fragments for _ in range(num_fragments)]
        for i in range(num_fragments):
            for j in range(num_fragments):
                if i == j:
                    continue
                overlap_matrix[i][j] = calculate_overlap(filtered_fragments[i], filtered_fragments[j])

        # Step 3: 状态压缩动态规划 (TSP)
        # dp[mask][last_node] 表示访问了 mask 中所有片段，且 last_node 是最后一个访问片段时的最小总长度
        
        # 最多 9 个基因片段，2^9 = 512 种状态
        # N=9, M=1024KB
        # dp 数组大小: 2^N * N * (int size)
        # 512 * 9 * 4 bytes = 18KB, 内存占用很小
        
        # 初始化 dp 数组为无穷大
        INF = float('inf')
        dp = [[INF] * num_fragments for _ in range(1 << num_fragments)]

        # 初始化起始状态：以每个片段作为第一个片段
        for i in range(num_fragments):
            dp[1 << i][i] = len(filtered_fragments[i])

        # 遍历所有可能的 mask (从只包含一个片段的 mask 开始)
        for mask in range(1, 1 << num_fragments):
            # 遍历 mask 中的每个 last_node
            for last_node in range(num_fragments):
                if not (mask & (1 << last_node)): # 如果 last_node 不在当前 mask 中，跳过
                    continue

                if dp[mask][last_node] == INF: # 如果当前状态不可达，跳过
                    continue

                # 遍历所有尚未访问的 next_node
                for next_node in range(num_fragments):
                    # 如果 next_node 已经在 mask 中，或者 next_node 就是 last_node，跳过
                    if (mask & (1 << next_node)): 
                        continue
                    
                    # 计算新的 mask
                    new_mask = mask | (1 << next_node)
                    
                    # 计算从 last_node 到 next_node 所需的额外长度
                    # 新片段长度 - 重叠长度
                    added_length = len(filtered_fragments[next_node]) - overlap_matrix[last_node][next_node]
                    
                    # 更新 dp 值
                    dp[new_mask][next_node] = min(dp[new_mask][next_node], dp[mask][last_node] + added_length)

        # 找到最终答案：所有片段都被访问 (mask 为 (1 << num_fragments) - 1)
        final_mask = (1 << num_fragments) - 1
        min_total_length = INF

        for last_node in range(num_fragments):
            min_total_length = min(min_total_length, dp[final_mask][last_node])
        
        results.append(min_total_length)

    sys.stdout.write("\n".join(map(str, results)) + "\n")

solve()