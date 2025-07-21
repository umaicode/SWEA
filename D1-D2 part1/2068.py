T = int(input())

for test_case in range(1, T + 1):
    result = 0
    ls = input().split()
    numbers = list(map(int, ls))
    result = max(numbers)

    print(f"#{test_case} {result}")
