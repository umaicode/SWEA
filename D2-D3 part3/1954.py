T = int(input())

for test_case in range(1, T + 1):
    num = 1
    N = int(input())
    numbers = N * N
    matrix = [[0] * N for _ in range(N)]
    direction_row = [0, 1, 0, -1]
    direction_col = [1, 0, -1, 0]
    row, col = 0, 0
    direction = 0

    for _ in range(N * N):
        matrix[row][col] = num
        num += 1
        next_col = col + direction_col[direction]
        next_row = row + direction_row[direction]
        if (
            (0 <= next_row < N)
            and (0 <= next_col < N)
            and (matrix[next_row][next_col] == 0)
        ):
            row, col = next_row, next_col
        else:
            direction = (direction + 1) % 4
            row, col = row + direction_row[direction], col + direction_col[direction]
    print(matrix)
