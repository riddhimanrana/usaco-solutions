# bucket 1 -> bucket 2 -> bucket 3
# bucket 3 -> bucket 1 -> bucket 2
# bucket 3 -> bucket 1 -> bucket 2
# 88 operations later...
# bucket 3 -> bucket 1 -> bucket 2

# sample input
# 10 3, 11 4, 12 5
# bucket 1: capacity, 10; milk, 3
# bucket 2: capacity, 11; milk, 4
# bucket 3: capacity, 12; milk, 5
# 3 4 5 initial
# 0 7 5 bkt 1 to 2
# 0 0 12 bkt 2 to 3
# 10 0 2 bkt 3 to 1 sim (this is the final state)
# 0 10 2 bkt 1 to 2 sim
# 0 0 12 bkt 2 to 3 sim

import sys
sys.stdin = open('mixmilk.in', 'r')
sys.stdout = open('mixmilk.out', 'w')

capacity = []
milk = []

for i in range(3):
    c, m = map(int, input().split())
    capacity.append(c)
    milk.append(m)
    
# bucket 1 to bucket 2
if milk[0] + milk[1] <= capacity[1]:
    milk[1] += milk[0]
    milk[0] = 0
else:
    milk[0] = (milk[1] + milk[0]) - capacity[1]
    milk[1] = capacity[1]

# bucket 2 to bucket 3
if milk[1] + milk[2] <= capacity[2]:
    milk[2] += milk[1]
    milk[1] = 0
else:
    milk[1] = (milk[2] + milk[1]) - capacity[2]
    milk[2] = capacity[2]

# bucket 3 to bucket 1
if milk[2] + milk[0] <= capacity[0]:
    milk[0] += milk[2]
    milk[2] = 0
else:
    milk[2] = (milk[0] + milk[2]) - capacity[0]
    milk[0] = capacity[0]

# bucket 1 to 2
if milk[0] + milk[1] <= capacity[1]:
    milk[1] += milk[0]
    milk[0] = 0
else:
    milk[0] = (milk[1] + milk[0]) - capacity[1]
    milk[1] = capacity[1]

for x in milk:
    print(x)