# PROBLEM: 2
# problem:
"""
Rings in Rings in Rings
[ Memory: 256 MB, CPU: 2 sec ]


Bessie is playing with rings from her collection of N (1 <= N <= 100,000) rings. Each ring has a diameter X_i (1 <= X_i <= 100). A ring can fit inside another ring if the inner ring’s diameter is at least K (1 <= K <= 100) units smaller than the outer ring’s diameter.

Bessie is going to craft several square boxes to store her rings. Determine the minimum area necessary for Bessie to store all of her rings. A ring can fit into a square box that has side length at least as large as its diameter. A ring cannot go inside the same box as another ring unless the ring can fit inside the smallest ring already inside that box.
INPUT FORMAT:

Line 1: One integer: N
Line 2: N integers: the diameters of each ring
Line 3: One integer: K
OUTPUT FORMAT:

Line 1: One integer: the minimum area required to store the rings

SAMPLE INPUT:

5
5 3 2 1 4
2
SAMPLE OUTPUT:

41
We need a 5x5 box and a 4x4 box. This results in a total area of 41. The 5x5 box can store the rings of diameter 1, 3, and 5. The 4x4 box can store the rings of diameter 2 and 4.

SCORING:

For test cases 1-3, N <= 100
For test cases 4-8, N <= 10,000
For test cases 9-10, there are no additional constraints
"""

# Plan:
# read N, diameters, K
# sort diameters in descending order
# take the first diameter and find all numbers that are K less than it and iterate through the next number
# so for example with the sample input, we have 5, 3, 2, 1, 4
# we take 5 and find all numbers that are 2 less than it, so 3, 2, 1
# take the largest of those numbers and find all numbers that are K less than that so 1, but if there were more numbers we would just keep iterating on This
# now take the next stack of numbers left: 4, 2
# find all numbers that are K less than 4, so 2
# find all numbers that are K less than 2, so 0 but that doesn't exist so we just take 2
# now the there are 2 boxexs, so we take the diameter of the largest ring in each box and square it and add them together
# finally print the output

# code:
# read inputs
N = int(input())
diameters = list(map(int, input().split()))
K = int(input())

# sort descending
diameters.sort(reverse=True)

# create a list of nests
nests = []

# Iterate through each diameter:
for diameter in diameters:
    # Try to fit the ring in an existing nest
    for nest in nests:
        if diameter <= nest[-1] - K:  # Check if it fits in the nest
            nest.append(diameter)  # Add it to the nest
            break
    else:  # If the ring didn't fit in any nest, create a new nest
        nests.append([diameter])

# Calculate the minimum area required for each nest:
total_area = 0
for nest in nests:
    largest_diameter = nest[0]  # largest is the first
    box_area = largest_diameter**2  # square for box size
    total_area += box_area

# final output
print(total_area) 