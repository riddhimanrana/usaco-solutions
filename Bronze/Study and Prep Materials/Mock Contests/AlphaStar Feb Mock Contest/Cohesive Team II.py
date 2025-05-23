"""
Cohesive Team II
[ Memory: 256 MB, CPU: 2 sec ]

The Summer Olympics are coming up. Farmer John wants to pick the best team for it. He lines up N (1 <= N <= 100,000) cows. The cows that are willing to participate in the Moolympics have with their hooves pointing to the number 1, while cows who are unwilling to participate all point to the number 0. A team can only be formed from consecutive cows all pointing to the number 1. There is no limit to the size of the team. It can be as small as 1 cow and as large as N cows. 

FJ is confident that he can convince up to 1 cow to be willing to participate in the Moolympics (in other words, FJ can convince 1 cow to point their hooves at 1 instead of 0).  

What is the maximum number of possible different teams FJ can choose from?

INPUT FORMAT:

Line 1: One integer: N
Line 2: An N-digit binary string representing the line of cows (1 is willing to participate, 0 is not)
OUTPUT FORMAT:

Line 1: The number of different teams that can be selected.

SAMPLE INPUT 1:


14 
00100111000101
SAMPLE OUTPUT 1:

13
If FJ convinces the 5th cow to be willing to participate, then he has the following string: 

00101111000101
There are 7 choices for teams of size 1, 3 choices for teams of size 2, 2 choices for teams of size 3, and 1 choice for a team of size 4. This leads to a total of 13 choices. 
SCORING:
Test cases 1-6: satisfy N <= 1000
Test cases 7-16: no additional constraints
NOTE: For C++ / Java users, the answer is guaranteed to fit in an integer.
"""

N = int(input())
cows = list(map(int, input()))
prefix_sum = [0] * (N + 2)
dp = [0] * (N + 2)
ones = [0] * (N + 2)
cows = [0] + cows + [0]
for i in range(1, N + 2):
    prefix_sum[i] = prefix_sum[i - 1] + cows[i]
    ones[i] = ones[i - 1] + (cows[i] == 1)
    dp[i] = max(dp[i - 1], ones[i])
    if cows[i] == 0:
        dp[i] = max(dp[i], dp[prefix_sum[i - 1]] + i - prefix_sum[i - 1])
print(dp[N])