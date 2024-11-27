import sys
n = int(sys.stdin.readline().rstrip())
solutions = list(map(int, sys.stdin.readline().rstrip().split()))
solutions.sort()
ans = [1e9, 1e9, 1e9]
for i in range(n):
    s = i + 1
    e = n - 1
    while s < e:
        if abs(solutions[i] + solutions[s] + solutions[e]) < abs(sum(ans)):
            ans = [solutions[i], solutions[s], solutions[e]]

        if solutions[i] + solutions[s] + solutions[e] == 0:
            break
        elif solutions[i] + solutions[s] + solutions[e] < 0:
            s += 1
        else:
            e -= 1
print(*ans)