def pyramid(n):
    for i in range(1, n+1):
        stars = '*' * (2 * i - 1)
        print(stars.center(2 * n- 1 ))

rows = int(input("Number of Rows: "))
pyramid(rows)
