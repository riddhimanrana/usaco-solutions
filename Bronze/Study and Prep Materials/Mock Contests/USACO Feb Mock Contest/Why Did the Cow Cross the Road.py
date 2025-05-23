#### SUCCESSS!!! 10/10 testcases ####

### THINKING:
# 4 arrays:
# cow_id = [3,3,6,2,4,3,4,3]
## I scored 799.2/1000 on this contest
# 10/10 on first
# 10/10 on second
# and 4/10 on third
# I thinK i could have gotten an 8/10 or higher on third but I think it just need a bit more time(maybe 15 minutes)

# cow_pos = [1,0,0,1,1,0,0,1]
# current_cows = [2,3,4,6] # unique cows
# current_pos = [0,0,0,0] # default values
# keep track of the cow_id to its position
# find the first iteration of a certain variable, and use that to insert into current_pos
### PSEUDOCODE:
# read N
# cow_id, cow_pos = split(N times)
# current_cows = list(set(cow_id))
# current_pos: .index w/current_cows and cow_id
# count = 0
# for i in range(N):
#   if cow_pos[i] != current_pos.index(cow_pos[i]):
#       current_cows[current_cows.index(cow_id[i])] = cow_pos[i]
#       count += 1
# print(count)
import sys
sys.stdin = open("crossroad.in", "r")
sys.stdout = open("crossroad.out", "w")

N = int(input())
cow_id = [0] * N
cow_pos = [0] * N
for i in range(N):
    cow_id[i], cow_pos[i] = map(int, input().split())

current_cows = list(set(cow_id))
current_pos = [0] * len(current_cows)
for i in range(len(current_cows)):
    current_pos[i] = cow_pos[cow_id.index(current_cows[i])]
count = 0
for i in range(N):
    if cow_pos[i] != current_pos[current_cows.index(cow_id[i])]:
        current_pos[current_cows.index(cow_id[i])] = cow_pos[i]
        count += 1
print(count)