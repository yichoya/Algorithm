import sys
from collections import deque

input = sys.stdin.readline

dxyz = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

def bfs(q, box, m, n, h):
	while q:
		x, y, z = q.popleft()
		for dx, dy, dz in dxyz:
			nx, ny, nz = x + dx, y + dy, z + dz
			if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and box[nx][ny][nz] == 0:
				box[nx][ny][nz] = box[x][y][z] + 1
				q.append((nx, ny, nz))

def solution():
	m, n, h = map(int, input().split())
	box = []
	q = deque()
	remain = 0

	for i in range(h):
		layer = []
		for j in range(n):
			row = list(map(int, input().split()))
			for k in range(m):
				if row[k] == 1:
					q.append((i, j, k))
				elif row[k] == 0:
					remain += 1
			layer.append(row)
		box.append(layer)

	if remain == 0:
		print(0)
		return

	if not q:
		print(-1)
		return

	bfs(q, box, m, n, h)

	day = 0
	for layer in box:
		for row in layer:
			for val in row:
				if val == 0:
					print(-1)
					return
			day = max(day, max(row))

	print(day - 1)

solution()