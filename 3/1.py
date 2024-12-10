import re

line = open("input.txt", 'r').read()
pattern = r'mul\(\d{1,3},\d{1,3}\)'
patternMatches = re.findall(pattern, line)
result = 0
def mul(a, b):
    return a * b
for match in patternMatches:
    result += eval(match) 
print(result)