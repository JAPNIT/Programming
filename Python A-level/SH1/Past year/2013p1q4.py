global data
#Task 4.1
def task_4_1():
    for i in data:
        print(i + " " * (10 - len(i)), end="")
        print("@" * data[i])

#Task 4.2
def task_4_2(scale=1):
    for i in data:
        print(" " * 20 + "|" * (data[i]//scale))
        print(i + " " * (20 - len(i)), end="")
        print("|" * (data[i]//scale))
        print(" " * 20 + "|" * (data[i]//scale))

def task_4_3():
    maxi = None
    for i in data:
        if maxi == None:
            maxi = data[i]
        else:
            if data[i] > maxi:
                maxi = data[i]
    scale = maxi // 60
    task_4_2(scale)
    print()
    print("SCALE: Each symbol represents " + str(scale) + " units")
    

data = {}
while True:
    x = input("X value <ZZZ to end>: ")
    
    if x == "ZZZ":
        break
    
    freq = int(input("Enter frequency: "))
    data[x] = freq

print()
print("+" * 80)
print("FREQUENCY DISTRIBUTION")
print("+" * 80)
print()
print()

task_4_3()
