def readfile():
    file = open("T1_gamescore.txt","r")
    data = []
    for i in file:
        i = i.strip("\n")
        i = i.split(":")
        player = i[0]
        scores = i[1]
        scores = scores.split(",")
        player = player.split(",")
        player.append(int(scores[0]))
        for j in range(1,len(scores)):
            player.append(int(scores[j]) - int(scores[j-1]))
        data.append(player)
       
    file.close()
    return data

results = readfile()

def count_class(s):
    count = 0
    for i in results:
        if i[1] == s:
            count += 1
    return count

for clss in ["warrior","mage","priest"]:
    print("Number of " + clss + ":" + str(count_class(clss)))

def top_class_by_season(n):
    classes = {}
    data = [] #[sum, number]
    count = 0
    for i in results:
        score = i[n+1]
        clss = i[1]
        try:
            key = classes[clss]
            data[key][0] += score
            data[key][1] += 1
        except:
            classes[clss] = count
            count += 1
            data.append([score, 1])
    #print(data,classes)
    averages = []
    for i in data:
        averages.append(i[0]/i[1])
        
    max_val = 0
    index = -1
    for i in range(len(averages)):
        if averages[i] > max_val:
            max_val = averages[i]
            index = i
    for i in classes:
        if classes[i] == index:
            return i
        
for i in range(1,13):
    print("Top clas in season " + str(i) + " :")
    print(top_class_by_season(i))

def quicksort(a):
    if len(a) < 2:
        return a
    pivot = a[0]
    left = []
    right = []

    for i in range(1,len(a)):
        if a[0][1] < a[i][1]:
            right.append(a[i])
        else:
            left.append(a[i])
    return quicksort(right) + [pivot] + quicksort(left)

def top_n_players_by_season(n,s):
    data = []
    for i in results:
        data.append([i[0],i[s+1]])
    print(data[0])
    data = quicksort(data)
    for i in range(n):
        print(data[i][0])
top_n_players_by_season(10,4)

def find_stagnant_players():
    names = []
    for i in results:
        name = i[0]
        for j in range(2,len(i)):
            if i[j] == 0:
                print(i)
                names.append(name)
                break
    return names
print(find_stagnant_players())


        
            
