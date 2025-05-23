# this is a codeforces problem, but it is still good nonetheless and uses the same concept
N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# here we find the distance between two points, and make a function to make our life easier
def find_distance(x1, y1, x2, y2):
  return (x2-x1)**2 + (y2-y1)**2

# finally we calcualte all the diffs and append them to an array
distances = []
# for the number of possibilites
for i in range(N):
    # we calculate 
    for j in range(i+1, N):
        distances.append(find_distance(x[i], y[i], x[j], y[j]))

# useful tactic to prevent overcounting(a very important concept)
# so first we take N numbers that we need to find every possiblity
# for example with 3 numbers we have to do
# c1 -> c2, c1 -> c3
# and c2 -> c3
# to replicate this in code, we would first find respecitve distances for the number
# c1, has 2 possibilites
# so in my code i do:
# for i in range(N): # accounting for the first coordiante
# then i do for j in range(i+1, N): # accounting for the coordinates all the way to the end(c1->c2, c1->c3)
# we finnd the distance using the funciton, append it to a list, and in the end, we print the max distance

# finally we print the max distance squared as asked of us in the problem
print(round(max(distances)))