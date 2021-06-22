import sys
sys.stdin = open('input/10807.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    target = int(input())

    print(lst.count(target))