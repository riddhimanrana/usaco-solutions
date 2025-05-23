
x = [int(i) for i in input().split()]
N = x[0]
M = x[1]

spotty = []
plain = []
count = 0

for i in range(N):
    spotty.append(input())
for i in range(N):
    plain.append(input())

for i in range(M):
    spotty_list = []
    plain_list = []
    
    for x in spotty:
        spotty_list.append(x[i])
    for x in plain:
        plain_list.append(x[i])
    print(spotty_list)
    print(plain_list)
    works = True
    for x in spotty_list:
        if x in plain_list:
            works = False
            break
    if works == True:
        count += 1
print(count)