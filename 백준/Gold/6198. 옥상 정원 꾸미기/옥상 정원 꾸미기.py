import sys

n = int(sys.stdin.readline())
towers = []
for i in range(n):
    towers.append(int(sys.stdin.readline()))

stack = []
cnt = 0

for t in towers:
    while stack and stack[-1] <= t:
        stack.pop()
    stack.append(t)
    cnt += len(stack) - 1

print(cnt)