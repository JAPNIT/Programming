def binary_search_iter(a,n):
    beg = 0
    end = len(a)-1

    while beg <= end:
        mid = (beg+end)//2
        
        if a[mid] == n:
            return mid
        elif a[mid] > n:
            end = mid - 1
        elif a[mid] < n:
            beg = mid + 1
        
    return None

print(binary_search_iter([4,5,6,8,9],9))

def binary_search_recur(a,beg,end,n):
    if beg>end:
        return None

    mid = (beg+end)//2
    if a[mid] == n:
        return mid
    elif a[mid] > n:
        return binary_search_recur(a,beg,mid-1,n)
    else:
        return binary_search_recur(a,mid+1,end,n)

print(binary_search_recur([4,5,6,10,8,9],0,4,10))

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j+1] < a[j]:
                a[j],a[j+1] = a[j+1],a[j]

    return a

print(bubble_sort([7,3,4,1,9,18,10]))

def quick_sort(a):
    if len(a) <= 1:
        return a
    left = []
    right = []
    pivot = a[0]

    for i in range(1,len(a)):
        if a[i] <= pivot:
            left.append(a[i])
        else:
            right.append(a[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([7,3,4,1,9,18,10]))

def insertion_sort(a):
    for i in range(len(a)):
        val = a[i]

        j = i - 1

        while j>=0 and val < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = val
        print(a)
        
    return a

print(insertion_sort([10,1,5,9]))
