import sys
sys.stdin = open('input/9506.txt', 'r')

while True:
    number = int(input())
    lst = []
    ans = ''
    if number == -1:
        break
    else:
        for i in range(1, number):
            if number % i == 0:
                lst.append(i)
        if sum(lst) == number:
            print(number, " = ", " + ".join(str(i) for i in lst), sep="")
        else:
            print(number, "is NOT perfect.")
