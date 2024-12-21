from collections import defaultdict
import math

lines = []
antennaMap = {}
used = set()

def parseInput():
    f = open("input.txt", 'r')
    return [list(line.strip()) for line in f]

def getAntennae():
    antennaMap = defaultdict(list)
    used = set()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == '.':
                continue
            antennaMap[lines[r][c]].append((r, c))
    return antennaMap, used

def findAntinode(p1, p2, t):
    x, y =  (1 - t)*p1[0] + t*p2[0], (1 - t)*p1[1] + t*p2[1]
    if -1 < x < len(lines) and -1 < y < len(lines[0]):
        return x, y
    return (-1, -1)

def findUniquelocations():
    uniqueLocations = 0
    for v in antennaMap.values():
        for i in range(len(v)):
            for j in range(len(v)):
                if i == j:
                    continue
                node1 = findAntinode(v[i], v[j], 2)
                node2 = findAntinode(v[j], v[i], 2)
                if node1 != (-1, -1) and node1 not in used:
                    used.add(node1)
                    uniqueLocations += 1
                if node2 != (-1, -1) and node2 not in used:
                    used.add(node2)
                    uniqueLocations += 1
    return uniqueLocations
            
lines = parseInput()
antennaMap, used = getAntennae()
uniqueLocations = findUniquelocations()

print(uniqueLocations)