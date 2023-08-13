import sys

word = list(map(str, sys.stdin.readline().strip()))
res = [''] * len(word)

def solution(s, start):
    global res

    if not s: return

    # 현재 배열의 제일 작은 알파벳을 찾는다.
    target = min(s)
    idx = s.index(target)

    # res에 제일 작은 알파벳 위치에 제일 작은 알파벳을 추가.
    res[start + idx] = target
    print("".join(res))

    solution(s[idx + 1:], start + idx + 1) # 뒷 배열 확인
    solution(s[:idx], start) # 앞 배열 확인

solution(word, 0)