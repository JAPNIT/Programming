seat= input()
number= int(seat[:-1])
letter= seat[-1]
time=0
pair="first or second"

if number%2 == 0:
    Q=number/2
    if Q%2==0:
        pair="second"
    else:
        pair="first"

else:
    Q=int(number/2 - 0.5)
    if Q%2==0:
        pair="first"
    else:
        pair="second"

print(pair)
print(number//2)
if pair == "first":
    time+= 6 * ((number//2)) + (number//2)
else:
    time+= 6 * ((number//2)-1) + (number//2)-1
    
print(time)

order=["f","e","d","a","b","c"]

time += order.index(letter) + 1

print(time)

        
