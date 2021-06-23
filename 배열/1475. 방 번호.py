import sys
sys.stdin = open('input/1475.txt', 'r')
import math

room = list(str(input()))
check = {}

for i in range(10):
    check[i] = 0

for n in room:
    check[int(n)] += 1

count = math.ceil((check[6]+check[9])/2)


for i in range(10):
    if i == 6 or i == 9:
        pass
    else:
        if count >= check[i]:
            pass
        else:
            count = check[i]

print(count)
