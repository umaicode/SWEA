T = int(input())

for test_case in range(1, T + 1):
    result = 0
    ls = input().split()
    numbers = list(map(int, ls))
    for number in numbers:
        if number % 2 == 0:
            continue
        else:
            result += number

    print(f"#{test_case} {result}")
