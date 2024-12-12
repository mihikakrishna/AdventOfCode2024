from collections import defaultdict

def findPrereqs():
    for rule in rules:
        page1, page2 = rule.split("|")
        prereqs[int(page1)].append(int(page2))

def findPageSum():
    pageSum = 0
    for update in updates:
        update = [int(u) for u in update]
        isCorrect = True
        for i in range(len(update)-1, 0, -1):
            if update[i] in prereqs[update[i-1]]:
                continue
            isCorrect = False
            break
        pageSum += update[len(update)//2] if isCorrect else 0
    return pageSum

f = open("input.txt", 'r')
lines = f.read().splitlines()
rules = lines[:lines.index('')]
updates = [l.split(',') for l in lines[lines.index('')+1:]]
prereqs = defaultdict(list)
findPrereqs()
pageSum = findPageSum()

print(pageSum)
