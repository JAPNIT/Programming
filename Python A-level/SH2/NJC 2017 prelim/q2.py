flag_one = False
while True:
    choices = ["1","2","3"]

    #menu
    print()
    print("1.Read menu data")
    print("2.Take Order")
    print("3.Quit")
    
    choice = input("Please enter your choice: ")

    if choice not in choices:
        print("Please enter a valid choice.")
        continue
    
    if choice == "1":
        flag_one = True
        file1 = open("MENU.txt","r")

        data = [] #format [index,item,price]
        
        for i in file1:
            i = i.strip("\n")
            i = i.split(" ")
            index = int(i[0])
            price = i[-1]
            price = price[1:]
            item = " ".join(i[1:-1])
            
            temp = -1
            for j in range(len(data)):
                if data[j][0] > index:
                    temp = j
                    break

            if temp == -1: #need to add at the end
                data.append([index,price,item])
            else:
                data.insert(temp-1,[index,price,item])
                

    if choice == "2":
        if not flag_one:
            print("Please run option 1 first.")
            continue
        else:
            full_order = []
            while True:
                order = input("Please enter a menu item index(or -1 to complete the order): ")
                if order == "-1":
                    break
                beg = 0
                end = len(data)-1
                flag_search = False
                while beg <= end:
                    mid = (beg+end)//2
                    if data[mid][0] == int(order):
                        flag_search = True
                        full_order.append(data[mid])
                        break
                    elif data[mid][0] > int(order):
                        end = mid - 1
                    else:
                        beg = mid + 1
                        
                if not flag_search:
                    print("Invalid menu index; that index does not exist.")
                    print()
                    continue

            price = 0
            print("{0:10}{1:10}".format("Index","Item"))
            for i in full_order:
                print("{0:10}{1:10}".format("0"*(3-len(str(i[0]))) + \
                                                   str(i[0]),i[2]))
                price += float(i[1])
            print()
            print("Total price: " + str(price))
                
  
                
    if choice == "3":
        break
