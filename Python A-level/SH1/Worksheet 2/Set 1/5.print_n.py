n = int(input("Enter a number: "))

def print_iter(n):
    for i in range(n,-1,-1):
        print (i)

def print_recur(n):
    if n==-1:
        return True
    print(n)
    print_recur(n-1)

print("Result iteratively is: ")
print_iter(n)
print("Result recursively is: ")
print_recur(n)
