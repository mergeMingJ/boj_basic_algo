import sys
sys.stdin = open('input/11328.txt', 'r')

T = int(input())
for t in range(T):
    string, new_str = map(str, input().split())

    origin=sorted(list(string))
    new = sorted(list(new_str))

    if origin == new:
        print('Possible')
    else:
        print('Impossible')