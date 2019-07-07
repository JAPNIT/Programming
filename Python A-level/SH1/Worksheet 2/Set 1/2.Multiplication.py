n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

def mult_iter(n1,n2):
    prod = 0
    for i in range(n2):
        prod += n1
    return prod

def mult_recur(n1,n2):
    if n2 == 1:
         return n1
    else:
         return n1 + mult_recur(n1,n2-1)

print("The answer iteratively is:")
print (mult_iter(n1,n2))

print("The answer recursively is:")
print (mult_recur(n1,n2))
