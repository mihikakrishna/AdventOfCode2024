from collections import deque

def parseInput():
    f = open("input.txt", "r")
    lines =  [list(line.strip()) for line in f]
    for i in range(len(lines)):
        lines[i] = [int(char) for char in lines[i]]
    return lines

def nextCellIsValid(lines, r, c, dr, dc, sr, sc, seen):
    return (-1 < r + dr < len(lines) and 
            -1 < c + dc < len(lines[0]) and
            lines[r + dr][c + dc] == lines[r][c] + 1 and
            (r + dr, c + dc, sr, sc) not in seen)
    
def bfs(lines, queue, scores):
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    seen = set()
    while queue:
        for _ in range(len(queue)):
            r, c, sr, sc = queue.popleft()
            if lines[r][c] == 9 and (r, c, sr, sc) not in seen:
                seen.add((r, c, sr, sc))
                scores[(sr, sc)] += 1
            else:
                seen.add((r, c, sr, sc))
                for dr, dc in moves:
                    if nextCellIsValid(lines, r, c, dr, dc, sr, sc, seen):
                        queue.append((r + dr, c + dc, sr, sc))

lines = parseInput()
queue = deque([])
scores = {}
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == 0:
            queue.append((r, c, r, c))
            scores[(r, c)] = 0

bfs(lines, queue, scores)
totalScores = 0
for v in scores.values():
    totalScores += v
print(totalScores)