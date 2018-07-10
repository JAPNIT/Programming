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
for i in data:
    try:
        frequency[i[10]] += 1
    except:
        frequency[i[10]] = 1
        
one,two,three,four,five,six,seven,eight,nine,ten = ([] for i in range(10))

for i in range(1,8):
    temp_array = []
    if i != 4: # no class 4
        temp_array = data[cul_freq[i-1]:cul_freq[i]]
        numpy.random.shuffle(temp_array)
        for i in range(frequency[i]):
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
            
    
print("Distribution of classes in data(214 total): ")
print(frequency)

count = 0

for x in range(10):

    data = [one,two,three,four,five,six,seven,eight,nine,ten]
    #stratification of data to divide train and test in 80-20 ratio
    test = []
    train = []

    for i in range(10):
        if i != x:
            for k in range(len(data[i])):
                train.append(data[i][k])
        else:
            for k in range(len(data[i])):
                test.append(data[i][k])
                
    #distance calcuation - euclidean 
    def dist_calculation(data1, data2):
        dist = 0
        for i in range(1,10):
            v1 = data1[i]
            v2 = data2[i]
            dist += pow(float(v1) - float(v2), 2)
        return pow(dist,.5)
    
    #Knn 
    def Knn(data, train, k=7):
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
        prediction = Knn(i,train)
        if prediction == i[10]:
            correct_pred += 1
    count += correct_pred
    
    print("The number of correct predictions for validation no."  + str(x+1) + " is: " + str(correct_pred) + "/" + str(len(test)))
print("Average accuracy is: " + str(count/214 * 100))



