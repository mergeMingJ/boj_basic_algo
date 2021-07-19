import sys
sys.stdin = open('input/9095.txt', 'r')

T = int(input())

dp = [0, 1, 2, 4]
for _ in range(4, 14):
    dp.append(sum(dp[-3:]))

for t in range(T):
    N = int(input())
    print(dp[N])
