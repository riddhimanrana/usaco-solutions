# bessie wants to figure out if she got a speeding ticket on her car
import sys
sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")

# 10/10 testcases, but I think this is a bit slow, my old code was even solver at 8/10 testcases

N, M = map(int, input().split())
speed_limit, bessie_speed = [], []

for i in range(N):
    miles, speed = map(int, input().split())
    speed_limit.extend([speed] * miles)

for i in range(M):
    miles, speed = map(int, input().split())
    bessie_speed.extend([speed] * miles)
ans = 0
for i in range(100):
    dif = bessie_speed[i] - speed_limit[i]
    ans = max(dif, ans)

print(ans)