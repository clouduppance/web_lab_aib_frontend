def calc_possibilities(N, M):
    if N > 50 or N < 1 or M > 50 or M < 1:
        return "Превышение лимитов доски"
    
    board = [[0] * M for _ in range(N)]
    board[0][0] = 1
    
    for i in range(N):
        for j in range(M):
            if i - 2 >= 0 and j - 1 >= 0:
                board[i][j] += board[i - 2][j - 1]
            if i - 1 >= 0 and j - 2 >= 0:
                board[i][j] += board[i - 1][j - 2]
    
    return board[N - 1][M - 1]


if __name__ == '__main__':
    N, M = map(int, input().split())
    print(calc_possibilities(N, M))