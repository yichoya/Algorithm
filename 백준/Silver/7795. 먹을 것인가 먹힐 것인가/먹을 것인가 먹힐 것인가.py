import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    a_list = list(map(int, sys.stdin.readline().rstrip().split()))
    b_list = list(map(int, sys.stdin.readline().rstrip().split()))

    a_list.sort()
    b_list.sort()

    ans = 0
    for a in a_list:
        l, r = 0, m
        while l < r:
            mid = (l + r) // 2
            if b_list[mid] < a:
                l = mid + 1
            else:
                r = mid

        ans += l

    print(ans)