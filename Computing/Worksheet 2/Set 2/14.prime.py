n = int(input("Enter the number: "))

def prime_iter(n):
    for i in range(2,int(pow(n,.5))+1):
        if n%i == 0:
            return False
    return True

def prime_recur(n,k=3):
    if n==2:
        return True
    elif n%k == 0 or n%2==0:
        return False
    elif k >= int(pow(n,.5)):
        return True
    return prime_recur(n,k+1)

print("Iteratively: ")
if prime_iter(n):
    print("Prime")
else:
    print("Composite")
    
print("Recursively: ")
if prime_recur(n)==True:
    print("Prime")
else:
    print("Composite")
