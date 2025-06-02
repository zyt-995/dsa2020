n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 预处理，计算每个位的前缀和
pre = [[] for _ in range(16)]
sum_ = [[] for _ in range(16)]

for i in range(16):
    bits = i + 1
    mod = 1 << bits  # 2^(i+1)
    cnt = [0] * mod
    for x in arr:
        r = x % mod
        cnt[r] += 1
    pre[i] = cnt
    # 构建前缀和数组
    s = [0] * (mod + 1)
    for k in range(1, mod + 1):
        s[k] = s[k - 1] + cnt[k - 1]
    sum_[i] = s

add = 0
for _ in range(m):
    parts = input().split()
    if parts[0] == 'C':
        d = int(parts[1])
        add = (add + d) % 65536
    else:
        i = int(parts[1])
        bits = i + 1
        mod = 1 << bits
        s_val = add % mod
        two_i = 1 << i

        # 计算sum_a
        if s_val >= two_i:
            sum_a = sum_[i][mod] - sum_[i][0]
        else:
            a_start = two_i - s_val
            if a_start < 0:
                a_start = 0
            sum_a = sum_[i][mod] - sum_[i][a_start]

        # 计算sum_b
        sum_b = 0
        if s_val >= two_i + 1:
            a_start_b = mod + two_i - s_val
            sum_b = sum_[i][mod] - sum_[i][a_start_b]

        total = sum_a + sum_b
        print(total)
    