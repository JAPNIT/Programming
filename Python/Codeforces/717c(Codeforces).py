num= int(input())
work=[]
for i in range(num):
    work.append(int(input()))
laziness= work.copy()
time= 0

laziness.sort()
work.sort()
work=work[::-1]

for i in range(len(work)):
    time += work[i] * laziness[i]

print (time % (10007))

