import time
start = time.time()

x=0
y=0
locations=[[0,0]]
f = open('Day3(input).txt')
for direction in f.read().strip():

    if direction==">":
        x+=1
    elif direction=="<":
        x-=1
    elif direction=="^":
        y+=1
    else:
        y-=1
    locations.append([x,y])


locations.sort()

presents=0

for i in xrange(len(locations)):
    if i==0 or locations[i] != locations[i-1]:
        presents+=1
        
elapsed = (time.time() - start)
print elapsed
print presents
