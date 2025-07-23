T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    str = ""
    for i in range(n):
        ch, num = input().split()
        num = int(num)

        str += ch * num

    print(f"#{test_case}")
    for i in range(0, len(str), 10):
        print(str[i : i + 10])
