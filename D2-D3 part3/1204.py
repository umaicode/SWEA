T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    count = [0] * (len(numbers) + 1)
    for num in numbers:
        count[num] += 1

    max_v = float("-inf")
    for idx, i in enumerate(count):
        if i > max_v:
            max_v = i

    maximum = max(count)
    print(count)
    k = count.index(maximum)
    print(f"#{n} {k}")
