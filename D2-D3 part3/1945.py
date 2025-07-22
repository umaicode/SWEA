T = int(input())


for test_case in range(1, T + 1):
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while N > 1:
        if N % 2 == 0:
            a += 1
            N = N // 2
        if N % 3 == 0:
            b += 1
            N = N // 3
        if N % 5 == 0:
            c += 1
            N = N // 5
        if N % 7 == 0:
            d += 1
            N = N // 7
        if N % 11 == 0:
            e += 1
            N = N // 11
        if N == 0:
            break

    print(f"#{test_case} {a} {b} {c} {d} {e}")
