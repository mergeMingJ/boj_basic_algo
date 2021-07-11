import sys
sys.stdin = open('input/10773.txt', 'r')

N = int(input())

stack = []

for n in range(N):
    num = int(input())

    if num == 0:
        stack.pop(-1)
    else:
        stack.append(num)
print(sum(stack))