n = int(input("Enter the integer "))

def fact_iter(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def fact_recur(n):
    if n == 1: # base case 
        return 1
    else:
        return n * fact_recur(n-1) # recursive step

print("The answer iteratively is:")
print (fact_iter(n))

print("The answer recursively is:")
print (fact_recur(n))
