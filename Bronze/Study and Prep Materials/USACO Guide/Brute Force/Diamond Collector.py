# bessie has N diamonds of different sizes
# she wants the diamonds to be relatively similar in sizes
# she won't pick 2 diamonds if theire sizes differ by more than K
### INPUT:
# N, K
# N lines of diamond sizes
# output maximum number of diamonds bessie can showcase
### OUTPUT:
# 4(expected)
N, K = map(int, input().split())
diamonds = [int(input()) for i in range(N)]

maxDiamonds = 0
for i in range(N):
    weights = 0
    for j in range(N):
        if diamonds[j] >= diamonds[i] and diamonds[j] <= diamonds[i] + K:
            weights += 1
    maxDiamonds = max(maxDiamonds, weights)

print(maxDiamonds)