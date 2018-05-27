import time
start = time.time()

x=0
y=0
x1=0
y1=0
i=1
locations=[[0,0]]
f = open('Day3(input).txt')


        
    
for direction in f.read().strip():
    if i%2!=0:
        if direction==">":
            x+=1
        elif direction=="<":
            x-=1
        elif direction=="^":
            y+=1
        else:
            y-=1
        locations.append([x,y])
        i+=1
        
    else:
        if direction==">":
            x1+=1
        elif direction=="<":
            x1-=1
        elif direction=="^":
            y1+=1
        else:
            y1-=1
        locations.append([x1,y1])
        i+=1
        
locations.sort()

presents=0

for i in xrange(len(locations)):
    if i==0 or locations[i] != locations[i-1]:
        presents+=1
        
elapsed = (time.time() - start)
print elapsed
print presents
