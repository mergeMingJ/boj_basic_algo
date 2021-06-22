import sys, math
sys.stdin = open('input/13300.txt', 'r')

N, K = map(int, input().split())

boys = {}
girls= {}

for i in range(1,7):
    boys[i] = 0
    girls[i] = 0

for n in range(N):
    S, Y = map(int, input().split())

    if S == 0:
        girls[Y] +=1
    else:
        boys[Y]+=1
count = 0
for girl in girls.values():
    if girl > K:
        count += math.ceil(girl/K)
    elif girl==0:
        pass
    else:
        count+=1

for boy in boys.values():
    if boy > K:
        count += math.ceil(boy/K)
    elif boy == 0:
        pass
    else:
        count+=1
print(count)