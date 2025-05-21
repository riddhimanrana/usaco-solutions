### UNDERSTANDING:
# FJ has N farms numbered 1 to N
# FJ closes farm i at time c_i
# Bessie wakes up at time S and wants to maximize her productivity by visitng as many famrs a possible before they close
# Bessie plants to visit farm i on time t_i + s
# She needs to arraive at a farm before FJ closes it to visit it
# Bessie has Q queries and each query gives you 2 integers, S, and V
# V is the number of farms she wants to visit and S is the time she wakes up
# My job is to output if Bessie can/can't visit at least V farms if she wakes up at time S

### FORMAT:
## Input:
# Line 1: N(number of farms) and Q(no. of queries)
# Line 2: Farm closing time for each farm
# Line 3: Bessie Farm visiting start time
# Q Lines: V(amt. of farms Bessie wants to visit), S(time Bessie wakes up)

### SAMPLE:
## Input
# 5 5
# 3 5 7 9 12
# 4 2 3 3 8
# 1 5
# 1 6
# 3 3
# 4
# 5 1
## Output
# YES
# NO
# YES
# YES
# NO
## Explanation:
# Query 1: Bessie visits the farms at time t = [9,7,8,8,13]
# -> Bessie can only visit farm 4 on time but she also only wants to visit 1 farm so output is YES
# Query 2: Bessie can't visit any of the farms so output is NO
# Query 3: Bessie can visit farms 3, 4, and 5 on time so output is YES
# Query 4: Bessie can bisit farms 2, 3, 4, and 5 on time and she only wants to visit 4 so output is YES as well
# Query 5: Bessie can visit farms 2, 3,4, and 5 on time but she wants to visit 5 so output is NO

N, Q = map(int, input().split()) # getting input N, Q
closingTime = list(map(int, input().split())) # getting the closing time of the farms
bessieTime = list(map(int, input().split())) # annd the time bessie plans to visit each farm

visitingTime = [] # storing times that bessie can actually visit
for i in range(N):
    if closingTime[i] - bessieTime[i] >= 0: # maximize more efficiency by removing things that i dont rly need to solve this
        visitingTime.append(closingTime[i] - bessieTime[i])
visitingTime.sort()

total = len(visitingTime)
farmCounts = [0] * visitingTime[-1]
index = 0
counter = 0
previous_counter = 0
current_time = visitingTime[0]

while index < visitingTime[-1] and counter < len(visitingTime):
    if index < current_time:
        farmCounts[index] = total
        index += 1
    else:
        previous_counter = counter
        counter += 1

        while counter < len(visitingTime) and index >= visitingTime[counter]:
            counter += 1

        total -= (counter - previous_counter)
        current_time = visitingTime[counter]


for i in range(Q): # iterate over Q queries
    farm_count = 0
    V, S = map(int, input().split())

    if S > len(farmCounts) - 1:
        print("NO")
    elif farmCounts[S] >= V:
        print("YES")
    else:
        print("NO")
