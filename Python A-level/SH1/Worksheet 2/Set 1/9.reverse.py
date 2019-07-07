s = input("Enter the string: ")

def reverse_iter(s):
    reverse = ""
    for i in range(len(s)-1,-1,-1):
        reverse += s[i]
    print(reverse)

def reverse_recur(s):
    if s == "":
        return s
    return reverse_recur(s[1:]) + s[0]

print("Iteratively: ")
reverse_iter(s)
print("Recursively:")
print(reverse_recur(s))
