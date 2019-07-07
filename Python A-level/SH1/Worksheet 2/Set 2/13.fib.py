n = int(input("Enter the number: "))

def fib_iter(n):
    a=0
    b=1
    for i in range(n-2):
        term = a + b
        a = b
        b = term
    print(term)

def fib_recur(n):
    if n <= 2:
        return n-1
    return fib_recur(n-1) + fib_recur(n-2)

print("Iteratively: ")
fib_iter(n)
print("Recursively: ")
print(fib_recur(n))
