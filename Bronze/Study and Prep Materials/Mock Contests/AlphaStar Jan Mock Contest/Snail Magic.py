### PROBLEM: 3
"""
Snail Magic
[ Memory: 256 MB, CPU: 2 sec ]


A magical snail is traveling in a straight line along some very rough terrain in Farmer John’s field. The amount of time it takes for the snail to travel one unit of distance is equal to the absolute difference in height between its current position and its future position, plus one.

For example, if the snail was walking on terrain with height 5 and the next unit of terrain had a height of 7, it would take the snail 3 units of time to travel one unit of distance. If the snail were walking on completely flat terrain, it would take the snail 1 unit of time to travel one unit of distance.

This magical snail can instantly teleport up to X (1 <= X <= 10) units of distance, but there are a few constraints:

The snail can only teleport from one position to another position of equal height
The snail can only teleport at most twice (it requires a lot of energy to teleport)
Given N (1 <= N <= 100) numbers H_i (1 <= H_i <= 1000) describing the height of the next N units of terrain, determine the minimum amount of time required for the snail to travel from the its current position (with height H_1) to its final position (with height H_N).

Note the snail may move forward or backwards.
INPUT FORMAT:

Line 1: Two space separated integers: N, X
Line 2: N space separated integers: H_1,H_2,...,H_N
OUTPUT FORMAT:

Line 1: The minimum amount of time required to travel from position 1 to position N.

SAMPLE INPUT:

4 3
2 3 4 1
SAMPLE OUTPUT:

8
The snail can never teleport (as the terrain heights are all unique). Traveling from height 2 to height 3 takes 2 units of time. Traveling from height 3 to height 4 takes 2 units of time. Traveling from height 4 to height 1 takes 4 units of time. Total, the snail requires 2 + 2 + 4 = 8 units of time.

SAMPLE INPUT:

5 4
1 10 1 10 1
SAMPLE OUTPUT:

0
The snail can teleport from the 1st 1 to the 3rd 1 (equal height and at most 4 units away). Alternatively, the snail can teleport from the 1st 1 to the 2nd 1 to the 3rd 1. Both of these paths result in the snail instantly arriving at its destination.

SCORING:

For test cases 1-5, the snail teleports at most once
For test cases 6-10, the snail only moves forward
For test cases 11-15, there are no additional constraints
"""

# pseudocode:
# read N, X
# read heights as array
# iterate for every single block
# check if there are any duplicates
# find the locations of the duplicates, and store the location numbers in an array sorted in ascending order

# read no. of blocks and max teleport distance
N, X = map(int, input().split())
heights = list(map(int, input().split()))

# Create a dictionary to store the indices of each height
heights_dict = {}
for i, height in enumerate(heights):
    if height not in heights_dict:
        heights_dict[height] = []
    heights_dict[height].append(i)

# Calculate the time to move between two positions
def calc_time(start, end):
    time = 0
    for i in range(start, end):
        time += abs(heights[i] - heights[i+1]) + 1
    return time

# Find the minimum time considering all possible teleportations
min_time = calc_time(0, N-1)  # time without teleportation
for indices in heights_dict.values():
    for i in range(len(indices)):
        for j in range(i+1, len(indices)):
            if indices[j] - indices[i] <= X:
                time = calc_time(0, indices[i]) + calc_time(indices[j], N-1)
                min_time = min(min_time, time)

print(min_time)