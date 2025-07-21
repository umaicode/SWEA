T = int(input())

for test_case in range(1, T + 1):
    result = ""
    a, b = map(int, input().split())
    if a < b:
        result = "<"
    elif a > b:
        result = ">"
    else:
        result = "="

    print(f"#{test_case} {result}")
