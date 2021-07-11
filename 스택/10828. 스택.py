import sys
sys.stdin = open('input/10828.txt', 'r')

N =int(sys.stdin.readline())

stack = []

for n in range(N):
    string = sys.stdin.readline()
    if ' ' in string:
        todo, x = string.split()
        x = int(x)
        # push X: 정수 X를 스택에 넣는 연산이다.
        if todo == 'push':
            stack.append(x)
    else:
        [todo] = string.split()
        # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if todo == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop(-1))
        # size: 스택에 들어있는 정수의 개수를 출력한다.
        elif todo == 'size':
            print(len(stack))
        # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
        elif todo == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        elif todo == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])