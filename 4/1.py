f = open("input.txt", 'r')
lines = [list(line.strip()) for line in f]
targetString = 'XMAS'
visited = set()
dirs =      [(-1,-1),    (-1, 0),   (-1, 1), 
            (0, -1),                (0, 1),
            (1, -1),    (1, 0),     (1, 1)]

def dfs(d, r, c, i, path):
    if (r < 0 or r == len(lines) or 
        c < 0 or c == len(lines[0]) or 
        i > 3 or
        lines[r][c] != targetString[i] or
        tuple(path) in visited):
        return
    
    if i == 3:
        path.append((r, c))
        visited.add(tuple(path))
        return
    
    if lines[r][c] == targetString[i]:
        i += 1
        path.append((r, c))
    
    dfs(d, r + d[0], c + d[1], i, path)
    return

for r in range(len(lines)):
    for c in range(len(lines[0])):
        for d in dirs:
            dfs(d, r, c, 0, [])
print(len(visited))