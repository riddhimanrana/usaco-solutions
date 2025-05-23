# daisy chains has N flowers labels N lined up in a row
# flower i has p_i petals

n = int(input())
flowers = [int(x) for x in input().split()]
count = 0
for j in range(1, n+1):
   for i in range(0,n-(j-1)):
       sub = flowers[i:i+j]
       if sum(sub)/len(sub) in sub:
           count +=1
print(count)
# for the sample case, we want i and j as 2 more:
# 0, 2
# 1, 4
