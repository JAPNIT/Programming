def linear_search(a,t):
    for i in range(len(a)):
        if a[i] == t:
            return i
    return -1
