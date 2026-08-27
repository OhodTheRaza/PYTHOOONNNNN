rows = int(input("Enter the numbers of rows you want: "))
half = (rows+1)//2
for i in range(1, half + 1):
    print(" " * (half-i)+str(i)*(2*i-1))
for j in range(half -1, 0, -1):
    print(" " * (half-j)+str(j)*(2*j-1))