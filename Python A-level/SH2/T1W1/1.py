filename = input("Please enter the file name:")

while True:
    try:
        file_ip = open(filename, "r").readlines()
        break
    except:
        filename = input("Please enter a valid file name:")

lines = len(file_ip) 
words = len(file_ip[0]) - 1

file_op = open("LOG.TXT","w")
file_op.write("Statistics for:" + str(filename)+"\n")
file_op.write("Total Lines:" + str(lines)+"\n")
file_op.write("Items per Line:" + str(words)+"\n")
file_op.close()
