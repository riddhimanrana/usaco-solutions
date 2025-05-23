### PROBLEM 1
## Input:
# Line 1: N, M, K, D
# Line N+1: length m string showing the field
# cows are represented by 'C'
# empty space is represented by '.'
## OUTPUT:
# find the min number of steps required for Farmer John to travel to bottom right corner from top left

# N: height of the field
# M: width of the field
# K: number of cows
# D: How far he must be from each cow minimum

"""pseudocode
read N, M, K, D
read field and make into 2d array
for every empty space make it into a 0
for every cow make it into a 1
then for every cow, check surroundings and make into 1
if there is overlap between two cows thats fine
theoretically, now find the number of 0's in the array and print that OUTPUT

python pseudocode
read N, M, K, D

"""
"""old solution using 2d array
N, M, K, D = map(int, input().split())

D -= 1
# print(N, M, K, D) # debug

field = [list(input().strip()) for _ in range(N)]
steps = 0
for i in range(N):
    for j in range(M):
        # cows
        if field[i][j] == "C":
            field[i][j] = 1
            # from field[i][j], make any blocks D-1 spaces away from it into 1(horizontal, vertical, and diagonal)
            # above
            if i-1 >= 0:
                field[i-D][j] = 1
            # below
            if i+1 < N:
                field[i+D][j] = 1
            # left
            if j-1 >= 0:
                field[i][j-D] = 1
            # right
            if j+1 < M:
                field[i][j+D] = 1
            # top-left
            if i-1 >= 0 and j-1 >= 0:
                field[i-D][j-D] = 1
            # top-right
            if i-1 >= 0 and j+1 < M:
                field[i-D][j+D] = 1
            # bottom-left
            if i+1 < N and j-1 >= 0:
                field[i+D][j-D] = 1
            # bottom-right
            if i+1 < N and j+1 < M:
                field[i+D][j+D] = 1

        elif field[i][j] == ".":
            field[i][j] = 0

# find the 0's in the array
for i in range(N):
    for j in range(M):
        if field[i][j] == 0:
            steps += 1

print(steps - 1)

# current output:
[0, 1, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 1, 1, 1, 0]
[0, 1, 1, 1, 0, 1, 1, 0, 0]
[0, 1, 1, 0, 0, 1, 1, 1, 0]
[0, 0, 0, 0, 0, 1, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
# expected:
[0, 1, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 0, 1, 1, 1, 0]
[0, 1, 1, 1, 0, 1, 1, 1, 0]
[0, 1, 1, 1, 0, 1, 1, 1, 0]
[0, 1, 1, 1, 0, 1, 1, 1, 0]
[0, 0, 0, 0, 0, 1, 1, 1, 0]



[0, 1, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 0, 1, 1, 1, 0]
[0, 1, 1, 1, 0, 1, 1, 1, 0]
[0, 1, 1, 1, 0, 1, 1, 1, 0]
[0, 1, 1, 1, 0, 1, 1, 1, 0]
[0, 0, 0, 0, 0, 1, 1, 1, 0]
"""

# new solution:
# implementation is slow, but it works
N, M, K, D = map(int, input().split())
field = [list(input().strip()) for _ in range(N)]
dist = [[float('inf')]*M for _ in range(N)]
dist[0][0] = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = [(0, 0)]
while queue:
    x, y = queue.pop(0)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == float('inf'):
            if all(abs(nx - i) >= D or abs(ny - j) >= D for i in range(N) for j in range(M) if field[i][j] == 'C'):
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

print(dist[N-1][M-1])