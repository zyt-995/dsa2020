def qiuqiu(n, m):
    ring = list(range(1, n+1))
    pos = 0
    while len(ring) > 0:
        pos = (pos + m - 1) % len(ring)
        remove = ring.pop(pos)
        if len(ring) == 0:
            break
        m *= 2
        pos = (pos - m) % len(ring)
        remove = ring.pop(pos)
        m *= 2
    return remove

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(qiuqiu(n, m))
