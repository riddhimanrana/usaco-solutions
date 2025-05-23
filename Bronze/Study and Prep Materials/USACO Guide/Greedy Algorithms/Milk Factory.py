# N Processing stations
# N-1 walkways connecting the stations
# SAMPLE:
# 3 # processing stations
# 1 2 # 
# 3 2

# PSEUDOCODE:
# read N
# read conveyers
# conveyers = []
# routes = []
# stations = [0] * N
# for i in range(N):
#   move = []
#   for x in range(2):
#       move.append(conveyers[i][x])
#   for j in range(N):
#       if conveyers[j][0] == i + 1:
#           for x in range(2):
#               move.append(conveyers[j][x])
#   conveyers.append(move)
# for i in range(N):
#   for j in routes[i]:
#       num = j + 1
#       added = routes.count(j+1)
#       stations[routes(num.index())] += added
#   stations[i] += added
# answer = max(stations)
# print(answer)

N = int(input())
conveyers = []
routes = []