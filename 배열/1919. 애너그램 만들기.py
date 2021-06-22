import sys
sys.stdin = open('input/1919.txt', 'r')
from string import ascii_lowercase


lst = list(input())
new_lst = list(input())

origin = {}
check = {}

count = 0
for spell in ascii_lowercase:
    origin[spell] = 0
    check[spell] = 0

for char in lst:
    origin[char]+=1

for char in new_lst:
    check[char]+=1

for spell in ascii_lowercase:
    if origin[spell] != check[spell]:
        count += abs(origin[spell]-check[spell])

print(count)