rows_no=int(input("enter no of rows"))
for i in range(1, rows_no + 1):

    # printing i spaces at the
    # beginning of each row
    for k in range(1, i):
        print(" ", end="")

    # printing i to rows value
    # at the end of each row
    for j in range(i, rows_no + 1):
        print(j, end=" ")

    print()

    # for loop for printing lower half
for i in range(rows_no - 1, 0, -1):

    # printing i spaces at the
    # beginning of each row
    for k in range(1, i):
        print(" ", end="")

    # printing i to rows value
    # at the end of each row
    for j in range(i, rows_no + 1):
        print(j, end=" ")

    print()