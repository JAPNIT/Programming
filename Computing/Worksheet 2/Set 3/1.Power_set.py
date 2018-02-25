n=list(map(int,input("Enter the numbers: ").split(' ')))

def pow_set_iter(n):
    pow_set = []
    for i in range(len(n)):
        for j in range(len(n)):
            pow_set.append(set([n[i],n[j]]))
    return pow_set

print(pow_set_iter(n))

def pow_set_recur(n):
    
    if len(n) == 0:
        return []

    else:
        return pow_set_recur(n[1:len(n)])
    
