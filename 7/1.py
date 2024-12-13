from collections import defaultdict
f = open("input.txt", 'r')
lines = [line.strip() for line in f]

def splitLine(line):
    val, nums = line.split(":")
    return int(val), [int(n) for n in nums.strip().split(" ")]

def canBeSolved(val, nums, i, currVal):
    if i == len(nums):
        return currVal == val
    solved = (canBeSolved(val, nums, i+1, currVal + nums[i]) or
              canBeSolved(val, nums, i+1, currVal * nums[i]))
    return solved

res = 0
for line in lines:
    val, nums = splitLine(line)
    if canBeSolved(val, nums, 1, nums[0]):
        res += val
print(res)