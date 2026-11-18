text = """
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
"""

grid = [list(map(int, line.split())) for line in text.strip().splitlines()]
rows, cols = len(grid), len(grid[0])
visited = [[False] * cols for _ in range(rows)]

def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:  
        return
    if grid[r][c] == 0 or visited[r][c]:         
        return
    visited[r][c] = True
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)

islands = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 1 and not visited[r][c]:
            dfs(r, c)
            islands += 1

print("Islands:", islands)
