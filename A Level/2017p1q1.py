f = open("INVENTORY.txt","r")
Inventory = []
Itemtype = []
ItemCounts = {}

for i in f:
    i = i.strip('\n')
    Inventory.append(i)
    if i not in Itemtype:
        Itemtype.append(i)
    try:
        ItemCounts[i] += 1
    except:
        ItemCounts[i] = 1

for j in ItemCounts:
    print(j, end =" ")
    print(ItemCounts[j])

f.close()
