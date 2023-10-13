def fibonacci(N):
    PISANO = 15 * 10**5
    MOD = 10**6
    fibo = [0] * PISANO

    if N < 2:
        return N
    else:
        fibo[1] = 1
        for i in range(2, PISANO):
            fibo[i] = (fibo[i - 1] + fibo[i - 2]) % MOD
        return fibo[N % PISANO]

N = int(input())
result = fibonacci(N)
print(result)