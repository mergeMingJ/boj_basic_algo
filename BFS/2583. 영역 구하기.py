import sys
sys.stdin = open('input/2583.txt', 'r')
import collections

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

M, N, K = map(int, input().split())

area = [[1 for _ in range(N)] for _ in range(M)]
visit = [[0 for _ in range(N)] for _ in range(M)]
cnt = 0
ans = []
Q = collections.deque()

for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            area[y][x] = 0

for m in range(M):
    for n in range(N):
        total = [1]
        if area[m][n] == 1 and visit[m][n] == 0:
            Q.append([m, n])
            visit[m][n] = 1

            while Q:
                x, y = Q.popleft()

                for k in range(4):
                    tx, ty = x+dx[k], y+dy[k]

                    if tx < 0 or tx >= M or ty < 0 or ty >= N or visit[tx][ty] != 0 or area[tx][ty] == 0:
                        continue
                    else:
                        Q.append([tx, ty])
                        if len(Q) > 1:
                            visit[tx][ty] = visit[x][y] + len(Q)
                        else:
                            visit[tx][ty] = visit[x][y] + 1
                    total.append(visit[tx][ty])
            cnt+=1
            ans.append(max(total))

print(cnt)
print(*sorted(ans))

