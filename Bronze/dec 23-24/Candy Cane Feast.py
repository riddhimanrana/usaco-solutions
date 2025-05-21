# Candy Cane Feast Problem
### PROBLEM:
# so first we're given N cows each with some height, and M candy canes also with varying heights.(Constraints: 1 <= N, M <= 200,000)
# basically, we are given in the input, the order of the cows eating the candy cane
# at the start of this cycle, FJ hangs a candy cane that touches the ground at height 0 and goes up to its height, where there is a hook holding it.
# in the order of the cows given, the cows eat it, with the first eating from the bottom of the candy cane until its height.
# the next cow eats from the bottom of the candy cane(from whatever it's height), until it's height. If it can't reach, then it doesn't eat and goes to the next person, if they can't eat, they also skip.
# Farmer John doesn't care, so he only puts a new candy cane every time the cows cycle through all their turns.
# also, the cows must eat in the given input order that is specified in the input.
# also, the cows grow in height based on the units of candy cane they eat. So if a cow eats 2 units of candy cane, it grows by 2 units.
### INPUT:
# we're given N and M first(N is the no. of cows, M is the no. of candy canes)
# then we're given the height of N cows
# then we're given the height of M candy canes
### OUTPUT:
# We need to output the final heights of each of the N cows on seperate lines, after all the candy eating and everything.
### EXAMPLE:
# 3 2
# 3 2 5
# 6 1

### SOLUTION PATH:
# First read the input
# Then we need to keep track of the current candy cane height, and the current cow we're on
# First loop through the candy canes, and for each candy cane, loop through the cows

N, M = map(int, input().split())
cows = list(map(int, input().split()))
candy = list(map(int, input().split()))

for i in range(M):
    remaining_candy_height = candy[i]
    bottom_candy_height = 0
    for j in range(N):
        # can cow reach the current bottom of the candy cane? then do this check
        if cows[j] >= bottom_candy_height and cows[j] >= candy[i]:
            cows[j] += remaining_candy_height
            remaining_candy_height = 0
            break
        elif cows[j] >= bottom_candy_height and cows[j] < remaining_candy_height:
            eaten_amount = min(cows[j] - bottom_candy_height, remaining_candy_height)
            cows[j] += eaten_amount
            remaining_candy_height -= eaten_amount
            bottom_candy_height = candy[i] - remaining_candy_height
        elif cows[j] >= bottom_candy_height and cows[j] >= remaining_candy_height:
            eaten_amount = min(cows[j] - bottom_candy_height, remaining_candy_height)
            cows[j] += eaten_amount
            remaining_candy_height -= eaten_amount
            bottom_candy_height = candy[i] - remaining_candy_height
        # else: cow can't reach, skip

for cow in cows:
    print(cow)
