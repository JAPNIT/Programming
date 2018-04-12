#importing relevant modules
import csv, numpy, pandas, random, operator
from sklearn.preprocessing import Normalizer
from scipy import stats
import matplotlib.pyplot as plt

#T test -- returns 1 if there is a difference and 0 otherwise.
def t_test(a1,a2):
    mean_1 = sum(a1)/len(a1)
    mean_2 = sum(a2)/len(a2)

    var_1 = numpy.var(a1)
    var_2 = numpy.var(a2)

    t_score = abs(mean_1-mean_2) / (pow((var_1/len(a1))+(var_2/len(a2)),0.5))

    if t_score > 2.601: #at 0.01 value of p -- 99% the results are not by chance
        return 1
    else:
        return 0

#Importing and Preprocessing Data
filename = '3.ecoli.csv'
raw_data = open(filename, 'rt').read().split('\n')
#reader = csv.reader(raw_data, delimiter='  ', quoting=csv.QUOTE_NONE)
data = [list(map(str, i.split("  "))) for i in raw_data]


data = data[:len(data)-1]
del data[47][1]
for i in range(len(data)):
    #print(data[i][8])
    if data[i][8] == " cp":
        data[i][8] = 1
    elif data[i][8] == " im" :
        data[i][8] = 2
    elif data[i][8] == " pp" :
        data[i][8] = 3
    elif data[i][8] == "imU" :
        data[i][8] = 4
    elif data[i][8] == " om" :
        data[i][8] = 5
    elif data[i][8] == "omL" :
        data[i][8] = 6
    elif data[i][8] == "imS" :
        data[i][8] = 7
    elif data[i][8] == "imL":
        data[i][8] = 8
    else:
        print(i)

for i in data:
    del i[0]
data = numpy.array(data).astype('float')


global features
features = len(data[0]) - 2

scaler = Normalizer().fit(data[:,1:features+1])
data[:,1:features+1] = scaler.transform(data[:,1:features+1])

total_data = len(data)

#Segregating instances of each class
current_class = data[0][features+1]
classes = {}
class_number = 0
temp = []
for i in data:
    c = i[features+1]
    if c == current_class:
        temp.append(i)
        c = i[features+1]
    else:
        classes[class_number] = temp
        class_number += 1
        current_class = c
        temp = []
        temp.append(i)
classes[class_number] = temp
class_number += 1

accuracy_matrix = [[0 for i in range(100)] for j in range(100)]

# -- start --

for y in range(100):
    print(y)
    test = []
    train_data = []
    test_dist = []

    # 80-20 split between test data set and train data set
    for z in range(class_number):
        temp_array = classes[z]
        numpy.random.shuffle(temp_array)
        temp_array= temp_array[:int((20 * len(temp_array)) / 100)]
        for i in temp_array:
            test.append(i)
            test_dist.append(i[0])

    for i in data:
        if i[0] not in test_dist:
            train_data.append(i)
    
    # Going from 1% to 100% for each training set ----------
    for sample_size in range(1,101):
        
        train = []
        
        #Segregating instances of each class in the training set
        current_class = train_data[0][features+1]
        train_data_classes = {}
        class_number = 0
        temp = []
        for i in train_data:
            c = i[features+1]
            if c == current_class:
                temp.append(i)
                c = i[features+1]
            else:
                train_data_classes[class_number] = temp
                class_number += 1
                current_class = c
                temp = []
                temp.append(i)
        train_data_classes[class_number] = temp
        class_number += 1
        
        for z in range(class_number):
            temp_array = train_data_classes[z]
            numpy.random.shuffle(temp_array)
            temp_array= temp_array[:int((sample_size * len(temp_array)) / 100)]
            for i in temp_array:
                train.append(i)
   
       #distance calcuation - euclidean 
        def dist_calculation(data1, data2):
            global features
            dist = 0
            for i in range(0,features+1):
                v1 = data1[i]
                v2 = data2[i]
                dist += pow(float(v1) - float(v2), 2)
            return pow(dist,.5)

        #Knn 
        def Knn(data, train):
            k = len(train)
            distances =[]
            for i in range(len(train)):
                dist = dist_calculation(data,train[i])
                distances.append((dist,train[i][features+1]))
                #print(train[i][features+1])
            distances.sort(key=operator.itemgetter(0))
            neighbours = [0 for i in range(class_number+1)]
            
            for i in range(k):
                try:
                    neighbours[int(distances[i][1]-1)] += 1/distances[i][0]
                except: #super close points -- approximate distance is 0
                    print(int(distances[i][1]-1))
                    neighbours[int(distances[i][1]-1)] += 10000
                    
            maximum = max(neighbours)

            return neighbours.index(maximum) + 1
            
        correct_pred = 0
        for i in test:
            prediction = Knn(i,train)
            if prediction == i[features+1]:
                correct_pred += 1

        accuracy = correct_pred/len(test)
        accuracy_matrix[sample_size-1][y] = accuracy


#Finding the ideal dataset size based on the tscore comparisons
no_sig_diff = 100
sig_diff = 0
current_size = 100

while no_sig_diff - sig_diff > 1:
    
    current_size = (no_sig_diff + sig_diff) // 2
    if t_test(accuracy_matrix[99],accuracy_matrix[current_size-1]): #if there is a difference
        sig_diff = current_size
    else:
        no_sig_diff = current_size

print("Instead of 100% of the data " + str(no_sig_diff) + "% of data can be used")

# Plotting the graph
avg_accuracy = [0 for i in range(100)]

print("Variances")

for i in range(100):
    temp = sum(accuracy_matrix[i])
    avg_accuracy[i] = temp
    variance_acc = numpy.var(accuracy_matrix[i])
    print(variance_acc)    

for i in avg_accuracy:
    print(i)

#for i in range(1,101):
    #print("Average accuracy of " + str(i+1) + "% of data set")    

x = [ i for i in range(1,101)]
plt.scatter(x,avg_accuracy)
plt.show()













