import sys
sys.stdin = open('pails.in', 'r')
sys.stdout = open('pails.out', 'w')

X, Y, M = map(int, input().split())

maxMilk = 0

# Loop through small buckets 
for i in range(M // X + 1): # 4
   # loop through medium buckets
   for j in range(M // Y + 1): # 3
       milk = X * i + Y * j
       if milk <= M and milk > maxMilk:
           maxMilk = milk

print(maxMilk)