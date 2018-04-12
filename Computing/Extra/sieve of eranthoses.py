n = int(input("Enter the number"))
prime = list(range(2,n+1))

try:
    for i in prime:
        for j in prime:
            if j%i == 0 and j!=i:
                prime.remove(j) # expensive in time
except:
    pass

print(prime)

#Better Way

n = int(input("Enter the number"))

primes = []

for i in range(0,n+1):
    primes.append(True)

#0 and 1 are not prime
primes[0] = False
primes[1] = False

current_prime = 0 #initially used as an index, not prime

while current_prime < n:
    #find the current prime
    for i in range(current_prime, len(primes)):
        if primes[i]:
            current_prime = i
            break
    for i in range(2 * current_prime, len(primes), current_prime):
        primes[i] = False
    current_prime = current_prime + 1

for i in range(len(primes)):
    if primes[i]:
        print (i)








