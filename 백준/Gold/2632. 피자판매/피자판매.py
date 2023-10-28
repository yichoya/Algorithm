from collections import defaultdict
import sys

def makePizza(cnt, pizza, pizzaDict):
    for i in range(cnt):
        pizzaSum = pizza[i]
        pizzaDict[pizzaSum] += 1
        for j in range(1, cnt - 1):
            pizzaSum += pizza[(i + j) % cnt]
            pizzaDict[pizzaSum] += 1

    pizzaDict[0] += 1
    pizzaDict[sum(pizza)] += 1
    
size = int(sys.stdin.readline())
m, n = map(int, sys.stdin.readline().split())
pizzaA, pizzaB = [], [] 
pizzaADict, pizzaBDict = defaultdict(int), defaultdict(int)

for i in range(1, m + 1):
    pizzaA.append(int(sys.stdin.readline()))

for i in range(n):
    pizzaB.append(int(sys.stdin.readline()))

makePizza(m, pizzaA, pizzaADict)
makePizza(n, pizzaB, pizzaBDict)

res = 0
for i in range(size + 1):
    res += pizzaADict[i] * pizzaBDict[size - i]
print(res)