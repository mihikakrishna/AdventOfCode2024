from collections import defaultdict
import itertools
f = open("input.txt", 'r')
lines = f.read().splitlines()
rules = lines[:lines.index('')]
updates = [l.split(',') for l in lines[lines.index('')+1:]]
prereqs = defaultdict(list)

def findPrereqs():
    for rule in rules:
        page1, page2 = rule.split("|")
        prereqs[int(page1)].append(int(page2))

def isIncorrect(update):
    for i in range(len(update)-1, 0, -1):
        if update[i] in prereqs[update[i-1]]:
            continue
        return True
    return False

def findIncorrectUpdates():
    incorrectUpdates = []
    for update in updates:
        update = [int(u) for u in update]
        if isIncorrect(update):
            incorrectUpdates.append(update)
    return incorrectUpdates

def getMiddleNum(update):
    updateSet = set(update)
    for num in update:
        intersection = set.intersection(updateSet, set(prereqs[num]))
        if len(intersection) == len(update)//2:
            return num

findPrereqs()
incorrectUpdates = findIncorrectUpdates()

pageSum = 0
for update in incorrectUpdates:
    pageSum += getMiddleNum(update)
    
print(pageSum)
