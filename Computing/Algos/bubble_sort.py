array = list(map(int,input("Enter the numbers: ").split(" ")))
n = len(array)
k = int(input("Enter k: "))

for i in range(n):
    for j in range(n-i-1):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
print(array)
if n%2 == 0:
    x,y = int(n/2 - .5), int(n//2)
    print((array[x] + array[y])/2)
else:
    x = n//2
    print(array[x])
            
count = 0
while array[count] < k:
    count += 1
print(array[count-1])
