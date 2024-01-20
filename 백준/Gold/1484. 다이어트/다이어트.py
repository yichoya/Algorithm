import sys
input = sys.stdin.readline
g = int(input())
res = []
for i in range(1, g):
    x = i**2 - g
    if x > 0 and (x**0.5).is_integer():
        res.append(i)
if len(res) == 0:
    print(-1)
else:
    print('\n'.join(map(str, res)))