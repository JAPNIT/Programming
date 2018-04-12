a = list(map(int,input("Enter numbers: ").split(" ")))
x = int(input("Enter number: "))

beg = 0
end = len(a) 
mid = 0
while beg < end:
    mid = int((beg+end)/2)
    if a[mid] == x:
        print(mid)
        break
    elif a[mid] > x:
        end = mid - 1
    elif a[mid] < x:
        beg = mid + 1


def bubble_sort():

    for 
    swap = 0
