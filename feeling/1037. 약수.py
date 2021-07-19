import sys
sys.stdin = open('input/1037.txt', 'r')

N = int(input())
num = sorted(map(int, input().split()))

print(num[0]*num[N-1])
