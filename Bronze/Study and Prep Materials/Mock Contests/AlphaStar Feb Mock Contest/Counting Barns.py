"""
Counting Barns
[ Memory: 256 MB, CPU: 2 sec ]

The best part of the day for Farmer John's cows is before the sun goes down. They can see the silhouettes of the barns as an N x M grid (1 <= N, M <= 1000). The silhouettes appear as '*'s while empty space appears as '.'s. All the barns are rectangular and stand on horizontal line. If a barn is located behind another barn, their silhouettes may overlap. The cows are arguing about the minimum number of barns the farm can have. Help them calculate the minimum number of barns on the farm.

INPUT FORMAT:

Line 1: Two integers: N and M
Lines 2...N+1: M characters: one row of the grid of silhouettes
OUTPUT FORMAT:

Line 1: One integer: the minimum number of barns on the farm

SAMPLE INPUT:

6 20
....................
.....**.....*.*.....
...****...******....
...****...******....
...****...******....
.*******..******...*
SAMPLE OUTPUT:

7
We can highlight all seven barns in three diagrams:
....................
.....**.....*.*.....
...1111...222222....
...1111...222222....
...1111...222222....
.**1111*..222222...3
....................
.....**.....5.6.....
...****...**5*6*....
...****...**5*6*....
...****...**5*6*....
.4444444..**5*6*...*
....................
.....77.....*.*.....
...**77...******....
...**77...******....
...**77...******....
.****77*..******...*
Note that each silhouette marker belongs to at least one barn! You can not achieve this with fewer than 7 rectangles.
"""

## PROBLEM 1
### IDEAS:
# start reading from bottom row
# if nothing in current index, move to next index
# if "*" in current index:
#   create a rect.
#   while loop idea:
#   check if there is a "*" for all the rightmost indexes of the rect.
#       if yes, cont rect., changes += 1
#       if no, continue w/this check process
#   check if there is a "*" for all the uppermost indexes of the rect.
#       if yes, cont rect., changes += 1
#       if no, continue w/this check process
#   if changes == 0 in the current while loop:
#       add 1 to the count of barns
#       make all the indexes of the rect "-" in the grid to signify that there is a rect here, and allow for barns to overlap
#       break the while loop
# if "-" in current index:
#   create a rect.
#   while loop idea:
#       check if there is a "*" for all the rightmost indexes of the rect.
#           if yes, cont rect., changes += 1
#           if no, continue w/this check process
#      check if there is a "*" for all the uppermost indexes of the rect.
#           if yes, cont rect., changes += 1
#           if no, continue w/this check process
#       if no * in the rect:(accoutn for there not being any * in the rect.)
#           break the while loop, and move to the next index
#       elif changes == 0 in the current while loop:(account for there beign a * in the rect., but no more opportunities)
#           add 1 to the count of barns
#           make all the indexes of the rect "-" in the grid to signify that there is a rect here, and allow for barns to overlap
#           break the while loop

### CODE:
# read input
"""
[['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '*', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '*', '*', '*', '*', '.', '.', '.', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.'],
 ['.', '.', '.', '*', '*', '*', '*', '.', '.', '.', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.'],
 ['.', '.', '.', '*', '*', '*', '*', '.', '.', '.', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.'],
 ['.', '*', '*', '*', '*', '*', '*', '*', '.', '.', '*', '*', '*', '*', '*', '*', '.', '.', '.', '*']]
"""

# Sample input
N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
max_horizontal = [0] * M
max_vertical = [0] * N

# Scan horizontally to find the longest sequence of '*'s in each column
for j in range(M):
    current_length =  0
    for i in range(N):
        if grid[i][j] == '*':
            current_length +=  1
        else:
            max_horizontal[j] = max(max_horizontal[j], current_length)
            current_length =  0
    max_horizontal[j] = max(max_horizontal[j], current_length)

# Scan vertically to find the longest sequence of '*'s in each row
for i in range(N):
    current_length =  0
    for j in range(M):
        if grid[i][j] == '*':
            current_length +=  1
        else:
            max_vertical[i] = max(max_vertical[i], current_length)
            current_length =  0
    max_vertical[i] = max(max_vertical[i], current_length)

# The minimum number of barns is the maximum of the maximum lengths found
print(max(max(max_horizontal), max(max_vertical)))