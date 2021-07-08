import sys
sys.stdin = open('input/1459.txt', 'r')

x, y, w, s = map(int, input().split())
x, y = max(x, y), min(x, y)

# if 2*w > s:
#     if x >= y:
#         walk = y*s
#         walk += (x-y)*w
#     else:
#         walk = x * s
#         walk += (y - x) * w
# else:
#     walk = (x+y)*w
#
# print(walk)

X, Y, W, S = map(int, input().split())
X, Y = min(X, Y), max(X, Y)
if S < W*2:
    s, b = min(X, Y), max(X, Y)
    if S <= W:
        m = (X+Y) % 2
        print((Y-m)*S + m*W)
    else:
        print(X*S + (Y-X)*W)
else:
    print((X+Y)*W)
