#### PROBLEM 3
## Understnad the problem:
# Bessie and Elsie start out w/some amt of marbles
# Bessie holds out A of her marbles and Elsie guess if A is even or odd
# If Elsie is right, she gets A marbles
# If Elsie is wrong, Bessie gets A marbles(if Elsie has less than A marbles she loses all her marbles)
# After some amt. of turns Elsie has N marbles
# A player loses if they have no marbles
# Elsie understand's Bessie's habits and recognizes that on turn i there are K diff amt. of marbles Bessie can put out
# After M turns bessie gets bored and stops playing
# identify the lexicographically min. turn sequence so that Elsie won't lose regardleds of how bessie plays

### SAMPLE:
## INPUT:
# Line 1: T (1 <= T <= 10) the number of test cases
# Each test case has the following:
# -> Line 1: N, M, K showing the marbles Elsie has, the number of turns, and number of potential moves Bessie can make
# -> Next M lines: line I contains K space seperated integers showing the possible amts. of marbles Bessie can play on turn i
## OUTPUT:
# For each test case, output a single line w/the lexicographically min. sequence of turns that Elsie can play to ensure she won't lose
# If she will lose output -1
# put move sequence on a single line and of M space seperated tokens
# "Even" is lexicographically less than "Odd"
## SAMPLE:
# 2
# 10 3 2
# 2 5
# 1 3
# 1 3
# 10 3 3
# 2 7 5
# 8 3 4
# 2 5 6
### OUTPUT:
# Even Even Odd
# -1
## explanation: 2 test cases:
# 1st: Elsie has 10 marbles, Bessie plays 3 turns, and has 2 potential moves each turn
# -> Bessie can play 2 or 5 marbles on turn 1, 1 or 3 on turn 2, and 1 or 3 on turn 3
# -> Elsie can do the following to ensure she won't lose: play Even, Even, Odd
# 2nd: Elsie has 10 marbles, Bessie plays 3 turns, and has 3 potential moves each turn
# -> Bessie can play 2, 7, or 5 marbles on turn 1, 8, 3, or 4 on turn 2, and 2, 5, or 6 on turn 3
# -> Elsie can't ensure she won't lose

### SAMPLE 2:
## INPUT:
# 1
# 20 8 2
# 3 5
# 3 5
# 3 5
# 3 5
# 3 5
# 3 5
# 3 5
# 3 5
## OUTPUT:
# Even Even Even Odd Even Odd Even Odd

# thinking:
# i'm going to try to prioritize lexicographically min. moves that will ensure Elsie won't lose(they HAVE to both work that way)
# so prioritize even moves over odd moves


# 4/12 testcases passed
# im not considering smth that i should be considering
## CODE:
# compltely change the approach
T = int(input()) # no. of test cases

for i in range(T):
    N, M, K = map(int, input().split()) # number of marbles Elsie has, number of turns, and number of potential moves Bessie can make
    evens = [] # list of max even moves
    odds = [] # list of max odd moves
    optimalMoves = [] # list of optimal moves
    marbles = 0 # min. possible marbles
    marblesList = [] # list of min. possible marbles
    for j in range(M): # iterate over possible moves
        bessieMoves = input().split() # read possible bessie moves
        even = -9999
        odd = -9999
        for k in range(K):
            even = max(even, (2 * (int(bessieMoves[k]) % 2) - 1) * int(bessieMoves[k]))
            odd = max(odd, (-2 * (int(bessieMoves[k]) % 2) + 1) * int(bessieMoves[k]))
        evens.append(even)
        odds.append(odd)
        # even = 0, odd = 1
        optimalMoves.append(int(even > odd))
        marbles += min(even, odd)
        marblesList.append(marbles)

    # check if Elsie will lose
    elsieWin = True # default to true bcuz we're going to check if she can win
    for k in marblesList:
        if k >= N:
            print(-1)
            elsieWin = False
    # if she can win, print the optimal moves
    if elsieWin == True:
        final_sequence = ""
        mod = 0
        for l in range(len(optimalMoves)):
            if optimalMoves[l] == 0:
                final_sequence += "Even "
            elif marblesList[l] + mod + evens[l] - odds[l] < N:
                mod += evens[l] - odds[l]
                final_sequence += "Even "
            else:
                final_sequence += "Odd "
        print(final_sequence[:-1])
