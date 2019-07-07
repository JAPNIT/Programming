def gcd_iter(a, b):
    while b:
        a, b = b, a%b
    return a

def gcd_recur(a,b):
    if b==0:
        return a
    return gcd_recur(b,a%b)

numbers = list(map(int,input().split()))
a = numbers[0]
b = numbers[1]

for i in numbers[2:]:
    a = gcd_iter(a,b)
    b = i
print(a)
    
