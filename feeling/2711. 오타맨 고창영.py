import sys
sys.stdin = open('input/2711.txt', 'r')

T = int(input())

for t in range(T):
    i, word = map(str, input().split())
    string = ''
    i = int(i)
    word = list(word)

    word.pop(i-1)
    for char in word:
        string+=char
    print(string)