file_ip = open("iris_input.txt","r").read().split('\n')
file_op = open("iris_output.txt","w")
list_iris = [tuple(map(str, i.split(','))) for i in file_ip]
for x in list_iris:
    file_op.write(str(x))
    file_op.write("\n")
file_op.close()
