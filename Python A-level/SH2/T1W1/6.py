def quick_sort(a):
    if len(a) < 2:
        return a

    pivot = a[0]
    left = []
    right = []

    for i in range(1,len(a)):
        if a[i] < pivot:
            left.append(a[i])
        else:
            right.append(a[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
