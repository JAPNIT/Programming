def convertor(x,unit,dimensions):
    while dimensions > 0:
        if unit == "cm":
            x = x/10
        if unit == "m":
            x = x/(10**3)
        if unit == "km":
            x = x/(10**6)
        dimensions -= 1
    return str(x)

# Taking the input
qt = float(input("Enter the quantity: "))
dimensions = input("Select either length, area, or volume: ")
u1 = input("Select a base unit (mm,cm,m,km)): ")
u2 = input("Select the unit you want to convert to (mm,cm,m,km): ")

# 1cm = 10mm 1m = 10^3mm 1km = 10^6mm
# Conversion of input into mm
if dimensions == "length":
    i = 1
elif dimensions == "area":
    i = 2
elif dimensions == "volume":
    i = 3

print (str(qt) + " " + str(u1) + "^" + str(i) + " = ", end = "")
       
i1 = i

while i1 > 0:
    if u1 == "cm":
        qt *= 10
    elif u1 == "m":
        qt *= 1000
    elif u1 == "km":
        qt *= 1000000
    i1 -= 1

# Printing the answer
print (convertor(qt,u2,i) + " " + str(u2) + "^" +str(i))




