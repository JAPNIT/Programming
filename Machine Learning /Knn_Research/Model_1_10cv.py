#importing relevant modules
import csv, numpy, pandas, random, operator
from sklearn.preprocessing import Normalizer
from scipy import stats

#T test -- returns 1 if there is a difference and 0 otherwise.
def t_test(a1,a2):
    mean_1 = sum(a1)/len(a1)
    mean_2 = sum(a2)/len(a2)

    var_1 = numpy.var(a1)
    var_2 = numpy.var(a2)

    t_score = abs(mean_1-mean_2) / (pow((var_1/len(a1))+(var_2/len(a2)),0.5))

    if t_score > 2.88: #at 0.01 value of p -- 99% the results are not by chance
        return 1
    else:
        return 0

#Importing and Preprocessing Data
filename = '3.ecoli.csv'
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=' ', quoting=csv.QUOTE_NONE)
data = list(reader)

for i in range(len(data)-1):
    print(data[i][8])
    if data[i][8] == "cp":
        data[i][8] = '1'
    elif data[i][8] == "im" :
        data[i][8] = '2'
    elif data[i][8] == "pp" :
        data[i][8] = '3'
    elif data[i][8] == "imU" :
        data[i][8] = '4'
    elif data[i][8] == "om" :
        data[i][8] = '5'
    elif data[i][8] == "omL" :
        data[i][8] = '6'
    elif data[i][8] == "imL" :
        data[i][8] = '7'
    else:
        data[i][8] = '8'
print(data)
data = data[:len(data)-1]
data = numpy.array(data).astype('float')
data = numpy.array(data).astype('float')



global features
features = len(data[0]) - 1 #change

scaler = Normalizer().fit(data[:,:features]) #change
data[:,:features] = scaler.transform(data[:,:features]) #change

total_data = len(data)

#Segregating instances of each class
current_class = data[0][features]
classes = {}
class_number = 0
temp = []
for i in data:
    c = i[features]
    if c == current_class:
        temp.append(i)
        c = i[features]
    else:
        classes[class_number] = temp
        class_number += 1
        current_class = c
        temp = []
        temp.append(i)
classes[class_number] = temp
class_number += 1

def accuracy_calc(data,sample_size):
    accuracy = []
    class_size = [0 for i in range(class_number)]
    for y in range(10):
        
        one,two,three,four,five,six,seven,eight,nine,ten = ([] for i in range(10))

        for z in range(class_number):
            temp_array = classes[z]
            temp_array = temp_array[:(sample_size * len(temp_array)) // 100]
            class_size[z] = (sample_size * len(temp_array)) // 100
            numpy.random.shuffle(temp_array)
            for i in range(len(temp_array)):
                array = i % 10
                if array == 0:
                    one.append(temp_array[i])
                elif array == 1:
                    two.append(temp_array[i])
                elif array == 2:
                    three.append(temp_array[i])
                elif array == 3:
                    four.append(temp_array[i])
                elif array == 4:
                    five.append(temp_array[i])
                elif array == 5:
                    six.append(temp_array[i])
                elif array == 6:
                    seven.append(temp_array[i])
                elif array == 7:
                    eight.append(temp_array[i])
                elif array == 8:
                    nine.append(temp_array[i])
                elif array == 9:
                    ten.append(temp_array[i])

        count = 0

        for x in range(10):
            
            data_10 = [one,two,three,four,five,six,seven,eight,nine,ten]        
            test = []
            train = []

            for i in range(10):
                if i != x:
                    for k in range(len(data_10[i])):
                        train.append(data_10[i][k])
                else:
                    for k in range(len(data_10[i])):
                        test.append(data_10[i][k])
                        
            #distance calcuation - euclidean 
            def dist_calculation(data1, data2):
                global features
                dist = 0
                for i in range(0,features):
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
                    distances.append((dist,train[i][features]))
                distances.sort(key=operator.itemgetter(0))
                neighbours = [0,0,0,0,0,0,0]

                for i in range(k):
                    try:
                        neighbours[int(distances[i][1]-1)] += 1/distances[i][0]
                    except: #super close points -- approximate distance is 0
                        neighbours[int(distances[i][1]-1)] += 10000 
                maximum = max(neighbours)

                return neighbours.index(maximum) + 1
                
            correct_pred = 0
            for i in test:
                prediction = Knn(i,train)
                if prediction == i[features]:
                    correct_pred += 1
            count += correct_pred

            
            #print("The number of correct predictions for validation no."  + str(x+1) + " is: " + str(correct_pred) + "/" + str(len(test)))
        #print()
        accuracy.append(count/(sample_size * total_data / 100) * 100)
    return accuracy

no_sig_diff = 100
sig_diff = 0
sample_size = 100

baseline_accuracy = accuracy_calc(data,100)

while no_sig_diff - sig_diff > 1:
    
    sample_size = (no_sig_diff + sig_diff) // 2
    print("Sample size:" + str(sample_size))

    temp_accuracy = accuracy_calc(data,sample_size)
    print("Baseline accuracy(100% data):")
    print(baseline_accuracy)
    print()
    print("Accuracy of this sample size:")
    print(temp_accuracy)
    print()

    if t_test(baseline_accuracy,temp_accuracy): #if there is a difference
        sig_diff = sample_size
        print("There is a significant difference")
    else:
        no_sig_diff = sample_size
        print("There is no significant difference")
    print()
print("Instead of 100% of the data " + str(no_sig_diff) + "% of data can be used")


