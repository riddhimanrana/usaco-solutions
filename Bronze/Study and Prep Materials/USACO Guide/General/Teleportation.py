import sys
sys.stdin = open('teleport.in', 'r')
sys.stdout = open('teleport.out', 'w')

# read the input
a, b, x, y = map(int, input().split())

# calculate the distance without using the teleporter
distance_without_teleporter = abs(b - a)

# calculate the distance using the teleporter
distance_with_teleporter = abs(a - x) + abs(b - y)
distance_otherway_teleporter = abs(a-y) + abs(b-x)

# print the minimum distance
print(min(distance_without_teleporter, distance_with_teleporter, distance_otherway_teleporter))