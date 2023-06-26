import sys

burgers = []
drinks = []
for _ in range(3):
    burgers.append(int(sys.stdin.readline()))
for _ in range(2):
    drinks.append(int(sys.stdin.readline()))

set = min(burgers) + min(drinks) - 50
print(set)