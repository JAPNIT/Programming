f = open("ANIMALS.txt","r")
animals = []
for i in f:
    val = ""
    flag = False
    for x in i: 
        if x == "=":
            flag = True
            continue
        if flag:
            val += x
    val = val[1:len(val)-2]

    ## OR

    i = i.strip().split("\"")
    animals.append(i[1])

n = input()

beg = 0
end = len(animals) - 1
count = 0
while beg <= end:
    count +=1
    mid = (end+beg) // 2
    if animals[mid] == n:
        print(mid)
        break
    elif animals[mid] > n:
        end = mid - 1
    elif animals[mid] < n:
        beg = mid + 1
print("Number of calls: " + str(count))
