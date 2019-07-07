def bubble_sort(a):
    for i in range(len(a)):
        swap = False
        for j in range(len(a) - i - 1):
            if a[j+1] < a[j]:
                a[j+1],a[j] = a[j],a[j+1]
                swap = True
        if not swap:
            break
    return a
