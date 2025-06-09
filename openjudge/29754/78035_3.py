def last_cursed_person(n, m):
    if n == 1:
        return 1  # 仅剩1人时直接返回
    else:
        k = last_cursed_person(n - 1, 2 * m)
        return (m - k - 1) % n + 1

n,m = map(int,input().split())
print(last_cursed_person(n,m))

