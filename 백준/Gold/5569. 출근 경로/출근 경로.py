w, h = map(int, input().strip().split())
arr = [[[0]*4 for i in range(h+1)] for j in range(w+1)]
for i in range(2, w+1):
    arr[i][1][0] = 1

for j in range(2, h+1):
    arr[1][j][2] = 1

for i in range(2, w+1):
    for j in range(2, h+1):
        arr[i][j][0] = arr[i-1][j][0] + arr[i-1][j][1]
        arr[i][j][1] = arr[i-1][j][2]
        arr[i][j][2] = arr[i][j-1][2] + arr[i][j-1][3]
        arr[i][j][3] = arr[i][j-1][0]

print(sum(arr[w][h]) % 100000)