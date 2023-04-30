import sys

A, B, V = map(int, sys.stdin.readline().split())

# while height < V:
    # day += 1
    # height += A
    # if height >= V:
    #     print(day)
    #     break
    # height -= B

# V = Ax - B(x-1)
day = (V - B) / (A - B)
if day == int(day):
    print(int(day))
else:
    print(int(day) + 1)