numbers = list(input("Enter the numbers: ").split(" "))
print(numbers)

def sum_iter(n):
    total = 0
    for i in n:
        total += int(i)
    print(total)

def sum_recur(n):
    if len(n) == 0:
        return 0
    return sum_recur(n[1:]) + int(n[0])

print("Iteratively: ")
sum_iter(numbers)
print("Recursively: ")
print(sum_recur(numbers))
