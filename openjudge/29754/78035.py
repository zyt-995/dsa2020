from collections import deque

def qiuqiu(n, m):
    dq = deque(range(1, n+1))
    ans = 0
    while len(dq) > 0:
        for _ in range((m-1) % len(dq)):
            dq.append(dq.popleft())
        removed = dq.popleft()
        if len(dq) == 0:
            break
        m *= 2
        for _ in range((m-1) % len(dq)):
            dq.appendleft(dq.pop())
        removed = dq.pop()
        m *= 2
    return removed

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(qiuqiu(n, m))
