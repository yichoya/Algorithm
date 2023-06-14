import sys

N = int(sys.stdin.readline())
for _ in range(N):
    n = sys.stdin.readline().rstrip()
    if n == "P=NP":
        print("skipped")
    else:
        a, b = map(int, n.split("+"))
        print(a + b)