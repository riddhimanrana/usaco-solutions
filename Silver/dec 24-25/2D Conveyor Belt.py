N = Q = 0
rr = []
cc = []
dd = []
grid = []
reversedReachable = []
reachableCount = 0
dq = []
fixedDirIndex = []
fixed = []
inReachCount = []
ans = []

# constants
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
DIR = ['U', 'R', 'D', 'L']

def idx(r, c):
    return r * N + c

def inBounds(r, c):
    return 0 <= r < N and 0 <= c < N

def makeReachable(u):
    global reachableCount
    if not reversedReachable[u]:
        reversedReachable[u] = True
        reachableCount += 1
        dq.append(u)

def processQueue():
    while dq:
        u = dq.pop(0)
        r, c = u // N, u % N
        for d in range(4):
            vr, vc = r - dr[d], c - dc[d]
            if not inBounds(vr, vc):
                continue
            v = idx(vr, vc)
            if reversedReachable[v]:
                continue

            if fixed[v]:
                dv = fixedDirIndex[v]
                rr, cc = vr + dr[dv], vc + dc[dv]
                if rr == r and cc == c:
                    makeReachable(v)
            else:
                if inReachCount[v] == 0:
                    makeReachable(v)
                inReachCount[v] += 1

# Main program
N, Q = map(int, input().split())
rr = []
cc = []
dd = []

for _ in range(Q):
    r, c, d = input().split()
    rr.append(int(r) - 1)
    cc.append(int(c) - 1)
    dd.append(d)

grid = [['?' for _ in range(N)] for _ in range(N)]

for i in range(Q):
    grid[rr[i]][cc[i]] = dd[i]

total = N * N
reversedReachable = [False] * total
fixed = [False] * total
fixedDirIndex = [0] * total
inReachCount = [0] * total

for r in range(N):
    for c in range(N):
        u = idx(r, c)
        ch = grid[r][c]
        if ch == '?':
            fixed[u] = False
        else:
            fixed[u] = True
            for d in range(4):
                if DIR[d] == ch:
                    fixedDirIndex[u] = d
                    break

reachableCount = 0

for r in range(N):
    for c in range(N):
        u = idx(r, c)
        if fixed[u]:
            d = fixedDirIndex[u]
            nr, nc = r + dr[d], c + dc[d]
            if not inBounds(nr, nc):
                makeReachable(u)
        else:
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if not inBounds(nr, nc):
                    makeReachable(u)
                    break

processQueue()

ans = [0] * Q
ans[Q-1] = total - reachableCount

for i in range(Q-1, 0, -1):
    r, c2 = rr[i], cc[i]
    u = idx(r, c2)

    if fixed[u]:
        fixed[u] = False
        inReachCount[u] = 0

        leadsOutside = False
        for d in range(4):
            nr, nc = r + dr[d], c2 + dc[d]
            if not inBounds(nr, nc):
                leadsOutside = True
                break

        if leadsOutside:
            makeReachable(u)
        else:
            count = 0
            for d in range(4):
                nr, nc = r + dr[d], c2 + dc[d]
                if not inBounds(nr, nc):
                    continue
                v = idx(nr, nc)
                if reversedReachable[v]:
                    count += 1
            if count > 0:
                inReachCount[u] = count
                makeReachable(u)

        processQueue()

    ans[i-1] = total - reachableCount

for x in ans:
    print(x)
