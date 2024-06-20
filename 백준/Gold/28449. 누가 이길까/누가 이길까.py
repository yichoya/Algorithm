import sys
import bisect

n, m = map(int, sys.stdin.readline().split())
HI = sorted(map(int, sys.stdin.readline().split()))
ARC = sorted(map(int, sys.stdin.readline().split()))
res = [0, 0, 0]


for hi in HI:
    # ARC에서 현재 hi보다 수가 작은 모든 참가자 찾기
    wins = bisect.bisect_left(ARC, hi)
    total = len(ARC)
    loses = total - bisect.bisect_right(ARC, hi)
    ties = total - wins - loses

    res[0] += wins
    res[1] += loses
    res[2] += ties

print(*res)