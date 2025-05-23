import sys

sys.stdin = open('blocks.in', 'r')
sys.stdout = open('blocks.out', 'w')
n = int(input())
data = [input().split() for x in range(n)]

final_count = [0] * 26
alpha = [x for x in 'abcdefghijklmnopqrstuvwxyz']
for x in data:
  count = []
  for i in alpha:
    count.append(max(x[0].count(i), x[1].count(i)))
  for i in range(len(count)):
    final_count[i] += count[i]

for x in final_count:
  print(x)
