# 최빈수 구하기
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    count = [0] * (len(numbers) + 1)
    for num in numbers:
        count[num] += 1

    max_v = float("-inf")
    max_index = 0
    for idx, i in enumerate(count):
        if (i > max_v) or (i == max_v and idx > max_index):
            max_v = i
            max_index = idx

    print(f"#{test_case} {max_index}")
