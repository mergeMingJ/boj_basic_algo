import sys
sys.stdin = open('input/2577.txt', 'r')

A = int(input())
B = int(input())
C = int(input())

lst = {}

for i in range(10):
    lst[i] = 0
num = A*B*C

for char in str(num):
    lst[int(char)] += 1

for num in lst.values():
    print(num)