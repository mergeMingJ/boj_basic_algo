import sys
sys.stdin = open('input/1926.txt', 'r')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]



n, m = map(int, input().split())

arr = [[int(char) for char in input().split()] for _ in range(n)]
visit = [[0]*m for _ in range(n)]
Q = []
check = 0
result = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visit[i][j] == 0:
            Q.append([i, j])
            visit[i][j] = 1
            check += 1

            while Q:
                x, y = Q.pop(0)
                for t in range(4):
                    tx = x + dx[t]
                    ty = y + dy[t]

                    if tx < 0 or tx >= n or ty < 0 or ty >= m or visit[tx][ty] != 0 or arr[tx][ty] == 0:
                        continue
                    else:
                        Q.append([tx,ty])
                        if len(Q) > 1:
                            visit[tx][ty] = visit[x][y] + len(Q)
                        else:
                            visit[tx][ty] = visit[x][y] + 1
print(check)
for p in range(n):
    result.append(max(visit[p]))
print(max(result))
