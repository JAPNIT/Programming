"""
Do we need all smaples to train the Knn
if not then how many?
starting with a certain number of samples
a certain step size, if a not a significant difference, say not more than 2%
then half the step size
I can have a standard testing data.
"""

import csv, numpy, pandas, random, operator
from sklearn.preprocessing import Normalizer
from scipy import stats

#importing data set into variable data as a numpy list
filename = 'glass_data_input.csv'
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')

#preprocessing of data - Normalisation 
scaler = Normalizer().fit(data[:,1:10])
data[:,1:10] = scaler.transform(data[:,1:10])

frequency = {}
cul_freq = {0.0:0, 1.0:70 , 2.0:146, 3.0:163, 4.0:163, 5.0:176, 6.0:185, 7:214}
total_data = 0
distribution = {1.0:14, 2.0:15, 3.0:4, 5.0:3, 6.0:2, 7.0:6}
for i in data:
    total_data += 1
    try:
        frequency[i[10]] += 1
    except:
        frequency[i[10]] = 1
print("Distribution of classes in data(214 total): ")
print(frequency)
print("Therefore the distribution of classes in testing data(45 total): ")
print(distribution)

count = 0
total = 0
sample_size=50

for i in range(1,8):
    try:
        percentage = frequency[i] / total_data
        distribution[i] = int(percentage * sample_size)
    except:
        pass
    
print(distribution)

"""
for x in range(10):
    #stratification of data to divide train and test in 80-20 ratio
    test = []
    train = []
    for i in range(1,8):
        temp_array = []
        if i != 4: # no class 4
            temp = distribution[i]
            temp_array = data[cul_freq[i-1]:cul_freq[i]]
            numpy.random.shuffle(temp_array)
            for i in range(temp):
                test.append(temp_array[i])
            for i in range(temp,len(temp_array)):
               train.append(temp_array[i])
               #numpy.random.shuffle(train)
    #train = train[:x]

    #distance calcuation - euclidean 
    def dist_calculation(data1, data2):
        dist = 0
        for i in range(1,11):
            v1 = data1[i]
            v2 = data2[i]
            dist += pow(float(v1) - float(v2), 2)
        return pow(dist,.5)
    
    #Knn implementation
    def Knn(data, train, k=1):
        distances =[]
        for i in range(len(train)):
            dist = dist_calculation(data,train[i])
            distances.append((dist,train[i][10]))
        
        distances.sort(key=operator.itemgetter(0))
        neighbours = []
        for i in range(k):
            neighbours.append(distances[i][1])
        return stats.mode(neighbours)[0]

    correct_pred = 0
    for i in test:
        total += 1
        prediction = Knn(i,train)
        if prediction == i[10]:
            count += 1
            correct_pred += 1
    
    print("The number of correct predictions for validation no."  + str(x) + " is: " + str(correct_pred))
print("Average accuracy is: " + str((count/total) * 100))

"""
