from collections import defaultdict
f = open("input.txt", 'r')
lines = [list(line.strip()) for line in f]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dirIdx = 0
visited = set()

def getStartPos(lines):
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == '^':
                return (r, c)
            
def getNextPos(r, c, dirs, dirIdx):
    return r + dirs[dirIdx][0], c + dirs[dirIdx][1]

start = getStartPos(lines)
r, c = start
while ( 0 <= r < len(lines) and 
        0 <= c < len(lines[0])):
        visited.add((r, c))
        nr, nc = getNextPos(r, c, dirs, dirIdx)
        if  (0 <= nr < len(lines) and 0 <= nc < len(lines[0]) and lines[nr][nc] == '#'):
            dirIdx = (1 + dirIdx) % len(dirs)
            nr, nc = getNextPos(r, c, dirs, dirIdx)
        r, c = nr, nc
print(len(visited))