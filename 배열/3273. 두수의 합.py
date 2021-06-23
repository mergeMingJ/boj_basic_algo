import sys
sys.stdin = open('input/3273.txt', 'r')

N = int(input())
arrs = sorted(list(map(int, input().split())))
x = int(input())
count = 0

for n in range(N-1):
    for m in range(n+1, N, -1):
        if arrs[n]+arrs[m] == x:
            count+=1
            break
print(count)
