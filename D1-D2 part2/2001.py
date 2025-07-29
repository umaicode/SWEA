T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_fly = float("-inf")
    for i in range(N - M - 1):
        for j in range(N - M - 1):

    # print(f"#{test_case} {max_fly}")
