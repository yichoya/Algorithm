T = []

while True:
    t = list(map(int, input().split()))
    if(t == [0, 0, 0]):
        break
    T.append(t)

for i in T:
    i.sort()
    if(i[0]*i[0] + i[1]*i[1] == i[2]*i[2]):
        print("right")
    else:
        print("wrong")