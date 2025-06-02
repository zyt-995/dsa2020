def count_trees(m, pre, post):
    from functools import lru_cache
    
    n = len(pre)
    # 预计算
    C = [[0]*(m+1) for _ in range(m+1)]
    for i in range(m+1):
        C[i][0] = 1
        for j in range(1,i+1):
            C[i][j] = C[i-1][j-1] + C[i-1][j]
    
    @lru_cache(None)
    def f(l1, r1, l2, r2):
        k = r1 - l1 + 1
        # 单写只有一个节点的
        if k == 1:
            return 1
        
        i = l1 + 1
        j = l2
        ways_prod = 1
        t = 0
        while i <= r1:
            # 下一个子树的根节点
            child_root = pre[i]
            pos = pos_in_post[child_root]
            size = pos - j + 1
            ways_prod *= f(i, i + size - 1, j, pos)
            t += 1
            i += size
            j = pos + 1
        
        # 子节点过多
        if t > m:
            return 0
        
        return ways_prod * C[m][t]
    
    # 后序中把值映射到索引
    pos_in_post = { ch:i for i, ch in enumerate(post) }
    
    return f(0, n-1, 0, n-1)


if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        line = line.strip()
        if line == '0':
            break
        m, pre, post = line.split()
        m = int(m)
        print(count_trees(m, pre, post))
