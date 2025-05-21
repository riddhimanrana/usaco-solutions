### UNDERSTANDING:
# Farmer John has N cows lined up in a circle
# For each i(1,2,...,N-1) the cow to the right of cow i is i + 1, cow to the right of cow N is cow 1
# ith cow has a bucket w/capacity a_i liters
# so basically in this circle the cow to the right of the end of the element is cow 1, and every cow to the right for other values are i + 1
# each minute the cows exchange milk based on a string of length N
# this string has characters "L" and characters "R"
# Caveat: all exchanges happen simultaneously:
# -> ex. a cow has a full bucket, but gives away a liter of milk, and also recieves a liter, her milk is preserved
# if a cow's total milk exceeds some value, then all of that excess milk is lost
# The goal is that FJ wants to find out the total amount of milk left w/the cows after M minutes

### FORMAT:
## Input:
# Line 1 is N and M
# Line 2 is a string of characters "L" or "R" which tells the cows which direction to pass their milk
# Line 3 is the capacities of each bucket
## Output:
# Output the sum of milk among all cows after M minutes as an integer

### SAMPLE:
## Sample 1
## Input
# 3 1
# RRL
# 1 1 1
## Output
# 2
## Explanation:
# -> Cow 2 and 3 pass each other 1 liter of milk
# -> Cow 1 passes milk to Cow 2, Cow 2 bucket overflows
# 1 liter of milk is lost so 2 is the output
## Sample 2
## Input
# 5 20
# LLLLL
# 3 3 2 3 3
## Output
# 14
## Explanation:
# -> Each cow passes 1 liter of milk to cow on the left and then gains a liter of milk from the cow on the right
# -> The milk always stays the same bcuz of this loop
# 0 liters of milk are lost so 14(the original amt. of milk) is the output
## Sample 2
## Input
# 9 5
# RRRLRRLLR
# 5 8 4 9 3 4 9 5 4
## Output
# 38
## Explanation:
# -> 51 liters of milk in the beginning
# -> After 5 minutes cow 3 loses 5 liters, cow 6 loses 3 liters, cow 7 loses 5 liters
# 13 liters of milk are lost so 38 is the output

## Efficiency:
# input 4-8: N <= 1000
# input 9-16: no constraints

# current usaco score: 820/1000

### CODE:

### NEW PLAN:
# usaco grading servers pls be nice and give me a 1000/1000
# 1. get the input
# MY IDEA::
# we basically have groups of cows that move in directions to make it more efficient
# we can group the cows based on their milk direction
# so first we'll group the cows based on their milk direction
# then we'll iterate over the groups and calculate the amount of milk that is spilled
# then we'll print the total amt. of milk left after M minutes
# 2. update the moves string and the capacities list basically following a rule set:
# -> if the first cow is passing milk to the right, then we check the last cow that is passing milk to the right and move it to the front of the line
# -> if the first cow is passing milk to the left, then we check the first cow that is passing milk to the right and move it to the front of the line
# 3. group the cows into group based on their milk direction
# -> iterate over the moves list and count the number of times the cow's milk direction changes
# -> add groups to the groups list based on each group that is being created
# -> each group should have only one direction change or none so like it can be LLLLL or it can be LLLRR because the direction only changes once, anymore and it breaks
# 4. calculate the amount of milk that is spilled
# -> if the group size is greater than 2(efficiency gains + makes more sense), we'll calculate the amount of milk that is spilled
# -> iterate over all the groups we've made and basically run some kind of while loop that calculates the amount of milk that is spilled to the right
# -> and calculate the amount of milk that is spilled to the left
# -> store these in a bucket variable and add them to the current bucket capacity and if it's over, reset bucket to M like my old code
# -> add this bucket to the overflow
# -> we basically do this a bunch of times
# 5. print the total amt. of milk left after M minutes
# -> just subtract the overflow from the total amt. of milk
# 6. profit aka 1000/1000

N, M = map(int, input().split()) # input N cows and M minutes
moves = input()
initialBuckets = list(map(int, input().split())) # starting buckets
currentBuckets = [] # new buckets array
totalMilk = sum(initialBuckets)
directionGroups = []

# update the moves string and the capacities list basically following a rule set
# if the first cow is passing milk to the right, then we check the last cow that is passing milk to the right and move it to the front of the line
# if the first cow is passing milk to the left, then we check the first cow that is passing milk to the right and move it to the front of the line
if moves[0] == "R": # if the first cow is passing milk to the right, then we check the last cow that is passing milk to the right and move it to the front of the line
  index = N - 1
  while index > 0 and moves[index] == "R":
    index -= 1
  moves = moves[index+1:N] + moves[0:index+1]
  currentBuckets = initialBuckets[index + 1:N] + initialBuckets[0:index + 1] # add to currentBuckets
else: # if the first cow is passing milk to the left, then we check the first cow that is passing milk to the right and move it to the front of the line
  index = 0
  while index < N and moves[index] == "L":
    index += 1
  moves = moves[index:N+1] + moves[0:index]
  currentBuckets = initialBuckets[index:N + 1] + initialBuckets[0:index] # add to currentBuckets
# print(moves) # debug
# print(capacities) # debug

index = 0 # iterate over the moves list
# group the cows into group based on their milk direction
while index < N: # iterate over the total groups
  start = index # start is set to the current index
  curr_move = moves[index] # curr is set to the current move
  directionChanges = 0 # counter is set to 0 by default to count the number of times the cow's milk direction changes
  while index < N and directionChanges < 2: # iterate over the moves list and count the number of times the cow's milk direction changes
    if moves[index] != curr_move: # so if the moves[i] is not equal to the current move, we add 1 to the counter
      directionChanges += 1
      if directionChanges == 2:
        break # if there's more than 2 changes in the cow's milk direction, then we break out of the loop
      if curr_move == "R": # update curr when the cow's milk direction changes
        curr_move = "L"
      else:
        curr_move = "R"
    index += 1 # keep iterating over the moves list
  directionGroups.append(moves[start:index]) # add groups to the groups list based on each group that is being created
# print(directionGroups) # debug
# print(capacities) # debug

overflow = 0 # store the total amount of spilled milk
index = 0 # keep track of the current position in the capacities list

if len(directionGroups) == 1 and directionGroups[0][0] == directionGroups[0][-1]: # if there's only one position and it's a circle (aka all cows are moving in the same direction)
  print(totalMilk) # no milk is spilled
else: #switch the statements and content
  for group in directionGroups: # iterate over each group in the positions list
    if len(group) > 2: # if the group size is greater than 2, we'll calculate the amount of milk that is spilled
      bucket = 0
      i = 0 # iterate over the group
      while i < len(group) and group[i + 1] == group[i]: # calculate the amount of milk that is passed to the right
        if bucket + currentBuckets[index + i] > M: # if the total amt. of milk passed exceeds M, then we set bucket to M
          bucket = M
          break
        bucket += currentBuckets[index + i] # add the capacity of the cow to the bucket
        i += 1 # continue iterating over the group
      overflow += bucket #add this bucket to the overflow
      #maybe think of a way to integrate left and right into one while loop
      bucket = 0 # samething for left, just reversed of the way we did right
      i = len(group) - 1
      while i >= 0 and group[i - 1] == group[i]:
        if bucket + currentBuckets[index + i] > M:
          bucket = M # reset the bucket to M
          break
        bucket += currentBuckets[index + i]
        i -= 1
      overflow += bucket #could create two different holds and add both at the end OR just keep subtracting from total (get rid of spill)
    index += len(group) # update the counter based on the length of the group

  print(totalMilk - overflow) # finally print the total amt. of milk left after M minutes
