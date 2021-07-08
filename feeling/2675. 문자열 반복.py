import sys
sys.stdin = open('input/2675.txt', 'r')

T = int(input())

for t in range(T):
    n, string = map(str, input().split())
    n = int(n)
    ans = ''

    for char in string:
        ans+=(char*n)
    print(ans)