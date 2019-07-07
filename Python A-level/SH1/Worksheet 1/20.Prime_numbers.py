n = int(input("Enter the prime number you want "))

flag = True
count = 0
number = 1
while count != n:
    number += 1
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            flag = False
            break
    if flag:
        count +=1 
    flag = True

print("The " + str(n) + "th prime number is: " + str(number))
