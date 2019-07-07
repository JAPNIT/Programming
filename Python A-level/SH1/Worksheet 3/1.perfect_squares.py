n = int(input("Enter a number: "))
file = open("perfect_square.txt","w")
for x in range(1,n+1):
    root = int(pow(x,.5))
    if root*root == x:
        file.write(str(x)+"\n")
file.close()
