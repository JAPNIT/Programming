def index(a):
    mapping = "0123456789ABCDEF"
    a = a.upper()
    for i in range(len(mapping)):
        if mapping[i] == a:
            return i 
def base_n_to_denary(value_str,n):
    number = 0
    power = len(value_str) - 1
    for i in range(len(value_str)):
        number += index(value_str[i]) * pow(n,power)
        power -= 1
    return number

scores = [] #format [class, index, score]
file_2a = open("2A_SCORES.txt","r")
for i in file_2a:
    i = i.strip("\n")
    i = i.split(",")
    scores.append(["2A",i[0],base_n_to_denary(i[1],2)])
file_2a.close()

file_2b = open("2B_SCORES.txt","r")
for i in file_2b:
    i = i.strip("\n")
    i = i.split(",")
    scores.append(["2B",i[0],base_n_to_denary(i[1],8)])
file_2b.close()

file_2c = open("2C_SCORES.txt","r")
for i in file_2c:
    i = i.strip("\n")
    i = i.split(",")
    scores.append(["2C",i[0],base_n_to_denary(i[1],16)])
file_2c.close()

#print(a,b,c)


def sort_student_scores(a):
    if len(a) < 2:
        return a
    pivot = a[0]
    left = []
    right = []

    for i in range(1,len(a)):
        if pivot[2] < a[i][2]:
            right.append(a[i])
        else:
            left.append(a[i])

    return sort_student_scores(right) + [pivot] + sort_student_scores(left)

scores = sort_student_scores(scores)

#average
avg = 0
for i in scores:
    avg += i[2]
avg /= len(scores)

#maximum
maximum = scores[0][2]
#minimum
minimum = scores[-1][2]

print("Mathematics result for classes 2A, 2B and 2C:")
print()
print("The highest examination score: " + str(float(maximum)))
print("The average examination score: " + str(round(avg,1)))
print("The lowest examination score: " + str(float(minimum)))
print()
print("The top 3 students are: ")
print()
print("{0:^10}{1:^10}{2:^10}".format("Class","Index","Mark"))
for i in range(3):
   print("{0:^10}{1:^10}{2:^10}".format(scores[i][0],\
                                        scores[i][1],\
                                        scores[i][2])) 










    
