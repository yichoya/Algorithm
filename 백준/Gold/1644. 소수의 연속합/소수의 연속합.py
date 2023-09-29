import sys, math

N = int(sys.stdin.readline())

prime = [1] * (N + 1)
prime[0], prime[1] = 0, 0

for i in range(2, int(math.sqrt(N)) + 1):
    if prime[i]:
        for j in range(i * 2, N + 1, i):
            prime[j] = 0
#print(prime)
prime_nums = []
for i in range(1, N + 1):
    if prime[i]:
        prime_nums.append(i)

cnt = 0
sum = 0
end = 0

for start in range(len(prime_nums)):
    while sum < N and end < len(prime_nums):
        sum += prime_nums[end]
        end += 1

    if sum == N:
        cnt += 1
        
    sum -= prime_nums[start]

print(cnt)