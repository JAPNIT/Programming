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

for i in range(1):
    #dividing into training and testing set - DO STRATIFICATION
    random.shuffle(data)
    train = data[:170]
    test = data[170:]
    print(test[:])
    
    #distance calcuation - euclidean 
    def dist_calculation(data1, data2):
        dist = 0
        for i in range(1,11):
            v1 = data1[i]
            v2 = data2[i]
            dist += pow(float(v1) - float(v2), 2)
        return pow(dist,.5)
    
    #Knn -- find the optimum k after stratification
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

    count = 0
    total = 0
    for i in test:
        total += 1
        prediction = Knn(i,train)
        if prediction == i[10]:
            count += 1
    
    print(count)
    print(total)
print((count/total) * 100)

