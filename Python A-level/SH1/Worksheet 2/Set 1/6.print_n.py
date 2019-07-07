n = int(input("Enter a number: "))

def print_iter(n):
    for i in range(n+1):
        print (i)

def print_recur(x,n):
    print(x)
    if x==n:
        return True
    print_recur(x+1,n)

print("Result iteratively is: ")
print_iter(n)
print("Result recursively is: ")
print_recur(0,n)
