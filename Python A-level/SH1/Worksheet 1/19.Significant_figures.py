number = list(input("Enter the number: "))
sig_fig = int(input("Enter the number of significant figures: "))

count = 0

for x in number:
    count+=1
    if count == sig_fig+1:
        if int(number[count]) >= 5:
            value = int(number[count-1]) + 1
            number[count-1] = str(value)
        break
            
for x in number[:count]:
    print(x,end="")
