numbers = list(input("Enter the numbers: ").split(" "))
print(numbers)

def mean_iter(n):
    total = 0
    for i in n:
        total += int(i)
    print(total/len(numbers))

def mean_recur(n,x):
    if len(n) == 0:
        return 0
    return mean_recur(n[1:],x) + int(n[0])/x

print("Iteratively: ")
mean_iter(numbers)
print("Recursively: ")
print(mean_recur(numbers,len(numbers)))
