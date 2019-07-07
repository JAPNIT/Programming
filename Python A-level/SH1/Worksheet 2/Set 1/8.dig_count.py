n = int(input("Enter a number: "))

def dig_iter(n):
    count = 0
    while n>0:
        n = n//10
        count += 1
    print(count)

def dig_recur(n,count):
    if n==0:
        print(count)
        return 0
    dig_recur(n//10,count+1)
    
print("Iteratively the number of digits are: ")
dig_iter(n)
print("Recursively the number of digits are: ")
dig_recur(n,0)
