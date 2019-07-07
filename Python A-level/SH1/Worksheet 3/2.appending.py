n = int(input("Enter the first number: "))
m = int(input("Enter the second number "))
file = open("perfect_square.txt","a")
for x in range(n,n+m):
    file.write(str(x)+"\n")
file.close()
