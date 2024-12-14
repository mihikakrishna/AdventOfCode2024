f = open("input.txt", "r")
line = f.read()
blocks = []
print(line)

for i in range(len(line)):
    char = "." if i % 2 else str(i//2)
    for _ in range(int(line[i])):
        blocks.append(char)

l, r = 0, len(blocks)-1

while l <= r:
    if blocks[l] == '.':
        blocks[l], blocks[r] = blocks[r], blocks[l]
        while blocks[r] == '.':
            r -= 1
    l += 1

checkSum = 0
for i in range(len(blocks)):
    checkSum += i * int(blocks[i]) if blocks[i] != '.' else 0
print(checkSum)