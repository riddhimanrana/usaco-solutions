# N Cows
# he is teaching his cows the bovine shuffle
# cows line up in a row in some order
# cows perform three shuffles in a row, and then be lined up in some possibly diff order
# he marks the location for his line of cows with possitions 1 -> N
# shuffles are as such. where a cow in position i moves to position ai
# farmer johns cows are each assigned distinct 7 digit integer id numbers
# we are given the ordering of the cows after 3 shuffles
# find their initial ordering
###INPUT:
# first line, N number of cows
# second line, N integers the shuffle position
# third line, order of N cows after 3 shuffle, specified by id number

### SAMPLE:
# 5
# 1 3 4 5 2
# 1234567 2222222 3333333 4444444 5555555
# explaination:
# 5 cows
# the cow in position 1 moves to position 1
# the cow in position 2 moves to position 3
# the cow in position 3 moves to position 4
# the cow in position 4 moves to position 5
# the cow in position 5 moves to position 2

###output:
#1234567
#5555555
#2222222
#3333333
#4444444

#import sys

#sys.stdin = open('shuffle.in', 'r')
#sys.stdout = open('shuffle.out', 'w')

# my plan:
# take the shuffle list, and make a new list, where the index is the shuffle number, and the value is the index
# then, take the cows list, and make a copy of it
# then, for each shuffle, replace the value in the cows list with the value in the shuffle list
# then, print the cows list

import sys
sys.stdin = open('blocks.in', 'r')
sys.stdout = open('blocks.out', 'w')

N = int(input())
shuffle = list(map(int, input().split()))
cows = list(map(int, input().split()))
cows_copy = cows.copy()

for i in range(N):
    cows[shuffle[i] - 1] = cows_copy[i]
for cow in cows:
    print(cow)