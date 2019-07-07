numbers = list(input("Enter the numbers: ").split(" "))
print(numbers)

def min_iter(n):
    minimum = int(n[0])
    for i in n:
        if int(i) < minimum:
            minimum = int(i)
    print(minimum)

def min_recur(n,x):
    if len(n) == 0:
        return x
    if int(n[0]) < x:
        x = int(n[0])
    return min_recur(n[1:],x)

print("Iteratively: ")
min_iter(numbers)
print("Recursively: ")
print(min_recur(numbers,int(numbers[0])))
