n=int(input("enter no of rows"))
snum=1
for i in range(n):
    for j in range(i+1):
        print(snum,end=" ")
        snum=snum+1
    print()