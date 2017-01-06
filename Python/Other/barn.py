barns,q=map(int,input().split(" "))
cows={}
count=0

for i in range(barns):
    stuff=list(map(int,input().split(" ")))
    stuff=list(set(stuff[1:]))
    for i in stuff:
        if i in cows.keys():
            cows[i] +=1
        else:
            cows[i] = 1

for i in range(q):
    label=int(input())
    try:
        print(cows[label])
    except:
        print (0)
    
        
    

        


 
 

