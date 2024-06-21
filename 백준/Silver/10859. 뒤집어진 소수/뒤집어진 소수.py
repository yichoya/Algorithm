import sys
input = sys.stdin.readline

def isPrime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


n = str(input().rstrip())


if isPrime(int(n)):
    # 180도 회전한 숫자
    m = ''
    for j in reversed(n):
        if j in ['3', '4', '7']:
            print("no")
            exit()
        if j == '6': m += '9'
        elif j == '9': m += '6'
        else: m += j

    if isPrime(int(m)):
        print("yes")
    else: print("no")
else: print("no")