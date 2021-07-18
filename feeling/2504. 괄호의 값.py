import sys
sys.stdin = open('input/2504.txt', 'r')

# 다시!!!!!!

def solution(arr):
    stack = []
    for char in arr:
        if char == ')':
            t = 0
            while stack:
                top = stack.pop()
                if top == '(':
                    stack.append(2 if t == 0 else t * 2)
                    break
                elif top == '[':
                    return 0
                else:
                    t += top
        elif char == ']':
            t = 0
            while stack:
                top = stack.pop()
                if top == '[':
                    stack.append(3 if t == 0 else t * 3)
                    break
                elif top == '(':
                    return 0
                else:
                    t += top
        else:
            stack.append(char)

    return stack


arr = list(map(str, ('').join(input().split())))
stack = solution(arr)
if stack == 0:
    stack = []
if '(' in stack or '[' in stack:
    print(0)
else:
    print(sum(stack))