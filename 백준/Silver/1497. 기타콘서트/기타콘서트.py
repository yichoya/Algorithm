import sys

n, m = map(int, sys.stdin.readline().split())
data = []
for _ in range(n):
    g, s = sys.stdin.readline().split()
    songs = s.replace('Y', '1').replace('N', '0')
    data.append((g, songs))

song_max, guitar_min = -1, 1234567890
def recur(idx, cnt, res):
    global song_max, guitar_min

    song_cnt = res.bit_count()
    if song_cnt == song_max and cnt < guitar_min:
        guitar_min = cnt

    if song_cnt > song_max:
        song_max = song_cnt
        guitar_min = cnt

    if idx == n or song_cnt == m:
        return

    recur(idx + 1, cnt + 1, res | int(data[idx][1], 2))
    recur(idx + 1, cnt, res)


recur(0, 0, 0)
if guitar_min == 0:
    print(-1)
else: print(guitar_min)