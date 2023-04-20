N = int(input())
grade = list(map(int, input().split()))

M = max(grade)
avg = float((sum(grade)/M * 100)/N)

print(avg)