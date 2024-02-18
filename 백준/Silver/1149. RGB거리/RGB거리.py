import sys
n = int(input())
rgb = []
for _ in range(n):
    rgb.append(list(map(int, input().strip().split())))

for i in range(1, n):
    rgb[i][0] = min(rgb[i - 1][1], rgb[i - 1][2]) + rgb[i][0]  #red
    rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + rgb[i][1]  #green
    rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + rgb[i][2]  #blue

print(min(rgb[n - 1]))