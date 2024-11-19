def solution(board, h, w):
    target = board[h][w]
    answer = 0
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(4):
        nx, ny = h + dir[i][0], w + dir[i][1]
        if 0 <= nx < len(board) and 0 <= ny < len(board):
            if board[nx][ny] == target:
                answer += 1
    return answer