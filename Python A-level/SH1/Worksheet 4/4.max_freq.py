import operator
file = open("word.txt","r")
count = {}
try:
    flag = True
    for line in file:
        if flag:
            word = line.strip("\n")
            flag = False
        else:
            count[word] = int(line)
            flag = True
except:
    pass
print(count)
print (max(count.items(), key=operator.itemgetter(1))[0])
file.close()
