#Task 1.1
f = open("WORDS1.txt","r").read()
flag = False
f = list(f.split("\n"))

maxi = 0
maxi_val = ""

for i in f:
    if flag:
        if int(i) > maxi:
            maxi = int(i)
            maxi_val = val
        flag = False
    else:
        val = i
        flag = True
        
print(maxi_val,maxi)

#Task 1.2
f = open("WORDS2.txt","r").read()
flag = False
f = list(f.split("\n"))

maxi = 0
maxi_val = []

for i in f:
    if flag:
        if int(i) > maxi:
            maxi = int(i)
        flag = False
    else:
        val = i
        flag = True

flag = False       
for i in f:
    if flag:
        if int(i) == maxi:
            print(val)
        flag = False
    else:
        val = i
        flag = True

