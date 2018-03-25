n = int(input("Enter a number: "))

def sum_iter(n):
    total = 0
    for i in range(n+1):
        total += i
    print(total)

def sum_recur(n):
    if n==0:
        return 0
    return n + sum_recur(n-1)

print("Result iteratively is: ")
sum_iter(n)
print("Result recursively is: ")
print(sum_recur(n))
