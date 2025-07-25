from collections import deque


for i in range(10):
    matrix = [[0] * 100 for _ in range(100)]
    n = int(input())

    numbers = []
    while len(numbers) < 10000:
        numbers += list(map(int, input().split()))
    arr = deque(numbers)
    for i in range(100):
        for j in range(100):
            matrix[i][j] = arr.popleft()

    row_sum = 0
    column_sum = 0
    diagonal_sum = 0

    for i in range(100):
        temp = 0
        for j in range(100):
            temp += matrix[i][j]
        if temp > row_sum:
            row_sum = temp

    for i in range(100):
        temp = 0
        for j in range(100):
            temp += matrix[j][i]
        if temp > column_sum:
            column_sum = temp

    temp_1 = 0
    temp_2 = 0
    for i in range(100):
        temp_1 += matrix[i][i]
        temp_2 += matrix[i][99 - i]

        diagonal_sum = max(temp_1, temp_2)

    result = max(row_sum, column_sum, diagonal_sum)

    print(f"#{n} {result}")
