def binary_search(a,t):
    beg = 0
    end = len(t) - 1
    while beg <= end:
        mid = (beg+end)//2
        if a[mid] == t:
            return mid
        elif a[mid] > t:
            end = mid - 1
        else:
            beg = mid + 1
    return -1
