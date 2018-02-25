n = input("Enter the number: ")

def dig_iter(n):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
    for i in range(len(n)):
        x = int(n[i])
        print (numbers[x], end=" ")
    print("")

def dig_recur(n):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
    x = int(n[0])
    if len(n) == 1:
        return numbers[x]
    else:
        return numbers[x] + " " + dig_recur(n[1:len(n)])

print("Iteratively: ")
dig_iter(n)

print("Recursively: ")
print(dig_recur(n))
