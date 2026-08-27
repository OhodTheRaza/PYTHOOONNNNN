n = int(input("Enter the numbers of rows you want: "))
for rows in range(n):
    for columns in range(rows + 1):
        print("*",end=" ")
    print()
    