f = open("EMPLOYEEDATA.txt","r")
id_no = []
name = []
for i in f:
    i = i.split("\"")
    name.append(i[3])
    name.append(i[7])
    id_no.append(i[1])
    id_no.append(i[5])

print(id_no)
print(name)

def search_by_id(id_no,name,n):
    beg = 0
    end = len(id_no) - 1

    while beg <= end:
        mid = (beg+end)//2
        if id_no[mid] == n:
            return name[mid]
        elif id_no[mid] > n:
            end = mid - 1
        else:
            beg = mid + 1
    print("Not found")
    return None

def search_by_name(id_no,name,n):
    for i in range(len(name)):
        if name[i] == n:
            return id_no[i]
    print("Not found")
    return None
