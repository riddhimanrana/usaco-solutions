# CodeForces Problem
# n-1 tandem kayaks(can carry 2 ppl)
# and 2 single kayaks(can carry 1 person)
# 2 * n ppl in the group(including Vadim)
### INPUT:
# n
# 2n, weights of each person
## IDEA:
# find all the smallest absolute differences and put in list
# largest differences get to be in single kayak
# everyone else go in
# read n 
# weights[]
# sort weights
# absolute_diffs[]w
# if len(weights) % 2 == 0:
    # for i in range(len(weight)):
        # diff = abs(weights[i+1] weights[i+2])
        # absolute_diffs.append(diff)
# else:
    # for i in range(len(weight) - 1):
        # diff = abs(weights[i] weights[i+1])
        # absolute_diffs.append(diff)
# sort(absolute_diffs)
# absolute_diffs.pop(last 2)
# print(sum(absolute_diffs))

# 2
# 1 2 3 4

n = int(input())
weights = list(map(int, input().split()))
weights.sort()
absolute_diffs = []
if len(weights) % 2 == 0:
    for i in range(2*n):
        diff = abs(weights[i] - weights[i+1])
    
    