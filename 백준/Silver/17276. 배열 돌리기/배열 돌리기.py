t = int(input())


def turn(n, d, graph: list):
    n -= 1
    count = abs(d) // 45
    minus = False
    if d < 0:
        minus = True

    for _ in range(count):
        if not minus:  # 양수 시계방향
            prev_list = list()

            for i in range(n + 1):  # 주대각선
                prev_list.append(graph[i][i])

            for i in range(n + 1):  # 주대각선 -> 가운데열
                prev_temp = graph[i][(n + 1) // 2]
                graph[i][(n + 1) // 2] = prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n + 1):  # 가운대열 -> 부대각선
                prev_temp = graph[i][n - i]
                graph[i][n - i] = prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n + 1):  # 부대각선 -> 가운데행
                prev_temp = graph[(n + 1) // 2][n - i]
                graph[(n + 1) // 2][n - i] = prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n + 1):  # 가운데행 -> 주대각선
                graph[n - i][n - i] = prev_list[i]
        else:
            prev_list = list()

            for i in range(n + 1):  # 주대각선
                prev_list.append(graph[i][i])

            for i in range(n + 1):  # 주대각선 -> 가운데행
                prev_temp = graph[(n + 1) // 2][i]
                graph[(n + 1) // 2][i] = prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n + 1):  # 가운데행 -> 부대각선
                prev_temp = graph[n - i][i]
                graph[n - i][i] = prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n + 1):  # 부대각선 -> 가운데열
                prev_temp = graph[n - i][(n + 1) // 2]
                graph[n - i][(n + 1) // 2] = prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n + 1):  # 가운대열 -> 주대각선
                graph[n - i][n - i] = prev_list[i]


for _ in range(t):
    n, d = map(int, input().split())
    graph = [list(map(int, input().split(' '))) for _ in range(n)]
    turn(n, d, graph)

    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=' ')
        print()