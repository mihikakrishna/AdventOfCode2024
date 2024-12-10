f = open("input.txt", 'r')
lines = [list(line.strip()) for line in f]
result = 0

def isX(lines, r, c):
    if ((r - 1) < 0 or (r + 1) == len(lines) or
        (c - 1) < 0 or (c + 1) == len(lines[0])):
        return False
    
    if (lines[r - 1][c - 1] == lines[r - 1][c + 1] == 'M' and 
        lines[r + 1][c - 1] == lines[r + 1][c + 1] == 'S'):
        return True
    
    if (lines[r - 1][c - 1] == lines[r - 1][c + 1] == 'S' and 
        lines[r + 1][c - 1] == lines[r + 1][c + 1] == 'M'):
        return True
    
    if (lines[r - 1][c - 1] == lines[r + 1][c - 1] == 'M' and 
        lines[r - 1][c + 1] == lines[r + 1][c + 1] == 'S'):
        return True
    
    if (lines[r - 1][c - 1] == lines[r + 1][c - 1] == 'S' and 
        lines[r - 1][c + 1] == lines[r + 1][c + 1] == 'M'):
        return True
    
    return False
    

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == 'A':
            result += isX(lines, r, c)
        
print(result)
