from collections import deque

def board_to_int(board):
    res = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] == 'b':
                res |= 1 << (i * 4 + j)
    return res

def generate_flip_masks():
    masks = []
    for i in range(4):
        for j in range(4):
            mask = 0
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1), (0,0)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < 4 and 0 <= ny < 4:
                    mask |= 1 << (nx * 4 + ny)
            masks.append(mask)
    return masks

def bfs(start):
    target1 = 0
    target2 = 0xFFFF  # 16个1的二进制
    if start in (target1, target2):
        return 0

    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)
    flip_masks = generate_flip_masks()

    while queue:
        current, steps = queue.popleft()
        for mask in flip_masks:
            new_state = current ^ mask
            if new_state in (target1, target2):
                return steps + 1
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, steps + 1))
    return "Impossible"

def main():
    board = [list(input().strip()) for _ in range(4)]
    start = board_to_int(board)
    print(bfs(start))

if __name__ == "__main__":
    main()