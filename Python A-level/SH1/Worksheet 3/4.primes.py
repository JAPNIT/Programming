n = int(input("Enter a number: "))
file = open("primenumbers.txt","r")
prime = []
for i in file:
    if i != "\n":
        prime.append(int(i))

#if n is divisible by any prime untill its square root its not a composite

def prime_check(n,prime):
    for i in prime:
        if int(i) > int(pow(n,.5)):
            break
        if n%i == 0:
            print("Composite")
            return 0
    print("Prime")

prime_check(n,prime)
file.close()
