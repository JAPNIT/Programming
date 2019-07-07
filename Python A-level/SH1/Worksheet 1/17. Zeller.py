day = int(input("Day born? "))
month = int(input("Month born? "))
year = input("Year born? ")

if month == 1 or month ==2:
    month += 12
    
yy = int(year[2:4])
century = int(year[:2])

zeller = (day + (13*(month+1)//5) + yy + (yy//4) + (century//4) - 2 * century)%7

days = ["sat","sun","mon","tue","wed","thur","fri"]

print(days[int(zeller)])
