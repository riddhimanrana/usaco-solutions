# Simulations Problem: Shell Game
# 10/10 test cases passed
# this has to use an older input/output system because its pre-2020 problem
import sys
sys.stdin = open('shell.in', 'r')
sys.stdout = open('shell.out', 'w')

N = int(input())

positions = {}
for i in range(N):
    a, b, g = map(int, input().split())
    positions[i] = [a, b, g]

guesses = []
for i in range(1, 4): # iterate 3 times
    counter = 0
    current_cup = i
    for j in range(N):
        if positions[j][0] == current_cup:
            current_cup = positions[j][1]
        elif positions[j][1] == current_cup:
            current_cup = positions[j][0]
        if positions[j][2] == current_cup:
            counter += 1
    guesses.append(counter)


print(max(guesses))

# my thinking:
# assume the pebble cup is 1, and the other two are 0
# evaluate if she gets it right or not, by checking the guess against variable G
# if she gets it right, add 1 to the counter
# finally add the counter to an array of guesses
# do this for each cup number such as 1, 2, or 3.
# finally print the max of the guesses array