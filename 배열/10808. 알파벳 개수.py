from string import ascii_lowercase


inputs = "baekjoon"

lst = {}


for char in ascii_lowercase:
    lst[char] = 0

for spell in inputs:
    lst[spell]+=1


for result in lst.values():
    print(result, end=" ")