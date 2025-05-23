# N cows
# 2 breeds: hollsteins and guernseys
# h for hollsteins and g for guernseys
# A is the string of breed identifiers FJ originally wanted
# B is the string of breed identifiers FJ got
# ask is to figure out the min number of times he needs to apply this machine to transform his current ordering B to a
# the machine can take any SUBSTRING of cwos and toggle their breeds(all Hs become Gs and all Gs become Hs in that specific SUBSTRING)
## INPUT:
# N(the number of cows he ordered)
# string A(what FJ wanted)
# string B(what FJ got)
## OUTPUT:
# print the min number of time the machine needs to be used to transform B into A
### Sample:
# 7
# GHHHGHH
# HHGGGHH
### Sample output:
# 2
#explanation: 

# PSEUDOCODE:
# read N
# read A
# read B
# consecutive_machine = 0
# machine_use = 0
# for i in range(N):
#   if B[i] != A[i]:
#       if consecutive_machine = 0:
#           machine_use += 1
#       consecutive_machine = 1
#   else:
#       consecitve_machine = 0
# print(machine_use)

import sys
sys.stdin = open('breedflip.in', 'r')
sys.stdout = open('breedflip.out', 'w')

N = int(input())
A, B = list(input()), list(input())

machine_uses = 0
consecutive_machine = 0
for i in range(N):
    if B[i] != A[i]:
        if consecutive_machine == 0:
            machine_uses += 1
        consecutive_machine += 1
    else:
        consecutive_machine = 0

print(machine_uses)