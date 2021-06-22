import sys
sys.stdin = open('input/1475.txt', 'r')

room = list(str(input()))
check = {}

for i in range(10):
    check[i] = 0

for n in room:
    check[int(n)] += 1

# 이어서 풀기