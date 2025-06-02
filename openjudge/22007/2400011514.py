n = int(input())
solutions = []

def solve_n_queens():
    def backtrack(row, cols, diag1, diag2, path):
        if row == n:
            solutions.append(path.copy())
            return
        for col in range(n):
            d1 = row - col
            d2 = row + col
            if col not in cols and d1 not in diag1 and d2 not in diag2:
                cols.add(col)
                diag1.add(d1)
                diag2.add(d2)
                path.append(col)
                backtrack(row + 1, cols, diag1, diag2, path)
                path.pop()
                diag2.remove(d2)
                diag1.remove(d1)
                cols.remove(col)
    
    backtrack(0, set(), set(), set(), [])
    
solve_n_queens()

if not solutions:
    print("NO ANSWER")
else:
    for sol in solutions:
        print(' '.join(map(str, sol)) + ' ')