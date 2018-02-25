#Input
ten = int(input("Number of 10-cent coins inserted "))
twenty = int(input("Number of 20-cent coins inserted "))
fifty = int(input("Number of 50-cent coins inserted "))
one = int(input("Number of 1-dollar coins inserted "))
choice = float(input("Enter the price of the drink - 0.8 or 1.2 "))

total = .1 * ten + .2 * twenty + .5 * fifty + 1 * one

ten = 0
twenty = 0
fifty = 0
one = 0

print ("Amount inserted: " + str(total)) #Amount Inserted

# Deducting the drink price
if (choice == 1.2):
    total -= 1.2
elif (choice == .8):
    total -= .8
else:
    print ("enter a valid input")

print ("The machine returns: " + str(total))

# Returning the change
total *= 10

while total >= 10:
    total -= 10
    one += 1

while total >= 5:
    total -= 5
    fifty += 1

while total >= 2:
    total -= 2
    twenty += 1

while total >= 1:
    total -= 1
    ten += 1
    
print (str(one) + " x 1 dollar coins")
print (str(fifty) + " x .50 dollar coins")
print (str(twenty) + " x .20 dollar coins")
print (str(ten) + " x .10 dollar coins")
    

