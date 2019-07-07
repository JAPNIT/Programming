import random
freq = [0 for i in range(20)]
for i in range(1000):
    n = random.randint(1,20)
    freq[n-1] += 1
print("integer" + " " * 3 + "Frequency")
for i in range(len(freq)):
    if i>=9:
        print(str(i+1) + " " * 8 + str(freq[i]))
    else:
        print(str(i+1) + " " * 9 + str(freq[i]))
    
