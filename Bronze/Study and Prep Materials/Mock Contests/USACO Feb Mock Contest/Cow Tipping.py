### THINKING:
# Cases:
# farm = [[0, 0, 1]
#        [1, 1, 1]
#        [1, 1, 1]]
# i can control anything in farm[0] -> so if there is any 1's in farm 0, i should do that automatically myself, but do that last (horizontal control)
# i can control anything in farm[0 -> N-1][0] -> i can control any 1's manually here as well (vertical control)
# i can control anything in farm[0 -> size of rectangle height][0 -> size of rectangle length] -> this accounts for vertical and horizontal control AKA rectangles
# Solving Cases:
# Priority 1:
# if tipped over > not tipped over:
#   tip over all cows
# Priority 2:
#   iterative:
# if 1 in farm[0 -> rectangle height][0 -> rectangle length]:
#   flip all in this rectangle
# I GOT IT:::
# if there is 1 in farm[0 -> rectangle height][0 -> rectangle length]:
#   if no. of tipped(aka 1) > not tipped(aka 0):
#       flip everything, in rectangle, continue iteration
#   flip everythign in this rectangle, and go one rectangle height/length -1

### PSEUDOCODE:
# read N
# farm = []
# for _ in range(N):
#   row = list(int(input().split()))
#   farm.append(row)
# height = N
# width = N
# for i in range(N^2):
#   rectangle:
#   

import sys
sys.stdin = open("cowtip.in", "r")
sys.stdout = open("cowtip.out", "w")

N = int(input())

farm = []
for _ in range(N):
    # Separate each digit and convert to integers
    row = [int(digit) for digit in input()]
    farm.append(row)


# Iterate over the rows
machine = 0
for row_end in range(len(farm), 0, -1):
    # Iterate over the columns
    for col_end in range(len(farm[0]), 0, -1):
        # Append the rectangle to the array
        rectangle = []
        for row in farm[:row_end]:
            rectangle.append(row[:col_end])
        
        tipped = 0
        not_tipped = 0

        for row in rectangle:
            for cow in row:
                if cow == 1:
                    tipped += 1
                else:
                    not_tipped += 1
        if tipped > not_tipped:
            machine += 1
            for i in range(row_end):
                for j in range(col_end):
                    if rectangle[i][j] == 0:
                        rectangle[i][j] = 1
                    else:
                        rectangle[i][j] = 0
        # add a case for checking the directly horizontal line, and directly vertical line
        # if there are consecutive numbers that are different in the line, then it will do 2?
        # not enough time
    # Consecutive numbers at the end of the array
    # Add your code here

            # Merge the updated rectangle back into the main farm
            for i in range(row_end):
                for j in range(col_end):
                    farm[i][j] = rectangle[i][j]

print(machine)