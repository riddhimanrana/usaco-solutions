"""
Rotate and Reverse
[ Memory: 256 MB, CPU: 2 sec ]

Bessie the Cow is playing a game with her new favorite word of length N (1 <= N <= 1,000). In the game, Bessie has two operations:

Rotate: She can shift every letter of a word 1 position to the right, with the last letter becoming the first letter.
Reverse: She can reverse the order of all of the letters.
For T (1 <= T <= 10) different objective strings of length N, determine the minimum number of operations Bessie needs to turn her favorite string into the objective string. If it is not possible, print “impossible”.

INPUT FORMAT:

Line 1: One integer: N
Line 2: One string of length N
Line 3: One integer: T
Lines 4...T+3: One string of length N. 
OUTPUT FORMAT:

Lines 1...T: One integer (the minimum number of operations required to produce the ith objective string) or the word “impossible”

SAMPLE INPUT:


9
alphastar
3
staralpha
lphastara
alphabeta
SAMPLE OUTPUT:

4
3
impossible
Rotating "alphastar" 4 times results in "staralpha". Reversing "alphastar", rotating it, and reversing it again results in "lphastara". Finally, "alphastar" will never turn into "alphabeta". 

SCORING:

Test Cases 1-10: N <= 500
Test Cases 11-15: no additional constraints.
"""

def rotate(word, rotations):
    return word[-rotations:] + word[:-rotations]

def min_operations(favorite, objective):
    n = len(favorite)
    for rotations in range(n):
        if rotate(favorite, rotations) == objective:
            return rotations
    return -1

def min_reversals(favorite, objective):
    reversed_favorite = favorite[::-1]
    rotations_needed = min_operations(reversed_favorite, objective)
    if rotations_needed == -1:
        return -1
    else:
        return (rotations_needed + 1) % len(favorite)

def solve(N, favorite, T, objectives):
    results = []
    for objective in objectives:
        rotations = min_operations(favorite, objective)
        reversals = min_reversals(favorite, objective)
        if rotations == -1 and reversals == -1:
            results.append("impossible")
        elif rotations == -1:
            results.append(reversals)
        elif reversals == -1:
            results.append(rotations)
        else:
            results.append(min(rotations, reversals))
    return results

# Sample input
N = int(input())
favorite = input()
T = int(input())
objectives = [input() for x in range(T)]

# Output results
output = solve(N, favorite, T, objectives)
for result in output:
    print(result)
