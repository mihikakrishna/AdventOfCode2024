import re

line = open("input.txt", 'r').read()
pattern = r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)'
patternMatches = re.findall(pattern, line)

parseMatch = True
result = 0
def mul(a, b):
    return a * b
for match in patternMatches:
    if "don't" in match:
        parseMatch = False
    elif "do" in match:
        parseMatch = True
    else:
        result += eval(match) if parseMatch else 0
print(result)