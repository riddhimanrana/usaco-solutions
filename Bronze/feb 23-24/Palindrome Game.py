### UNDERSTANDING:
# Bessie and Elsie are playign a game w/a pile of stones that contains S stones in the beginning
# Bessie and Elsie take alternative turns, Bessie goes first, Elsie 2nd, so on...
# For each cow's turn, they must remove x stones from the pile
# x is any positive integer palindrome that the cow chooses
# if a pile is empty when a cow's turn starts, that cow loses(aka if it's 0 when they cow starts)
# IMPORTANT: palindrome that has leading 0 isn't allowed, aka 990 isn't a palindrome cuz 099 isn't allowed

### FORMAT:
## Input:
# Line 1: T(the number of test cases)
# T lines of testcases w/1 line per testcase
## Output:
# for each testcase you need to output "B" if Bessie wins or "E" otherwise on new lines

### SAMPLE:
## Input:
# 3 <- 3 testcaes
# 8 <- Bessie can remove all the stones w/the first move, bcuz 8 is a plaindrome
# 10 <- Bessie can't remove all stones on first move, and Bessie will always lose
# 12 <- Bessie can remove 2, Elsie can remove any number, but Bessie still wins because 1 - 9 inclusive are all palindrome no.
## Output:
# B
# E
# B

### CODE:

T = int(input()) # number of testcases
for i in range(T):
    S = input()
    if S[-1] == '0': # check for leading zeroes, then Bessie can't win ever bcuz of her order in this list
        print("E")
    else: # otherwise, because of Bessie's order she can always win in some way or the other
        print("B")
