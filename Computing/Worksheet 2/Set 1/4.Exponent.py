base = int(input("Enter the base: "))
expo = int(input("Enter the exponent: "))

def expo_iter(n1,n2):
    ans = 1
    for i in range(expo):
        ans *= base
    return ans

def expo_recur(base,expo):
    if expo == 1:
         return base
    else:
         return base * expo_recur(base,expo-1)

print("The answer iteratively is:")
print (expo_iter(base,expo))

print("The answer recursively is:")
print (expo_recur(base,expo))
