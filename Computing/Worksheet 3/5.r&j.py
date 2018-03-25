file = open("R&J.txt","r")
punc = [".","|","(",")",":",";","!",",","?","[","]","-"]
count = {}
for line in file:
    line = line.split()
    for word in line:
        word = word.lower()
        for i in word:
            if i in punc:
                word = word.strip(i)
        word = word.lower() 
        try:
            count[word] += 1
        except:
            count[word] = 1

file_op = open("R_&_J_Word_Frequencies.txt","w")
for i in count:
    l = i + "," + str(count[i]) + "\n"
    file_op.write(l)
    
file.close()
file_op.close()
