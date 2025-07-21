T = int(input())

for test_case in range(1, T + 1):
    str = input()

    year = str[0:4]
    month = str[4:6]
    date = str[6::]

    num_year = int(year)
    num_month = int(month)
    num_date = int(date)

    if num_month > 12 or num_month == 0:
        print(f"#{test_case} -1")
        continue

    if (
        num_month == 1
        or num_month == 3
        or num_month == 5
        or num_month == 7
        or num_month == 8
        or num_month == 10
        or num_month == 12
    ):

        if num_date > 31:
            print(f"#{test_case} -1")
            continue

    if num_month == 4 or num_month == 6 or num_month == 9 or num_month == 11:
        if num_date > 30:
            print(f"#{test_case} -1")
            continue

    if num_month == 2:
        if num_date > 28:
            print(f"#{test_case} -1")
            continue

    print(f"#{test_case} {year}/{month}/{date}")
