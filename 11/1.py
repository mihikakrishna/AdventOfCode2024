def parseInput():
    f = open("input.txt", "r")
    return f.read().split(" ")

def blink(line):
    i = 0
    while i < len(line):
        if line[i] == '0':
            line[i] = '1'
        elif(len(line[i]) % 2 == 0):
            prev = str(int(line[i][:len(line[i])//2]))
            nxt = str(int(line[i][len(line[i])//2:]))
            line.insert(i, nxt)
            line.insert(i, prev)
            del line[i+2]
            i += 1
        else:
            line[i] = str(int(line[i]) * 2024)
        i += 1


line = parseInput()
for _ in range(25):
    blink(line)
print(len(line))
