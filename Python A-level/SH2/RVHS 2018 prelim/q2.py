class BSTNode():
    def __init__(self):
        self.id = None
        self.workshops = []
        self.left = None
        self.right = None

    def print(self):
        print("Id: " + self.id)
        print("Workshops: ")
        print(self.workshops)

class BST():
    def __init__(self):
        self.root = None

    def insert(self,ID, ws):
        newnode = BSTNode()
        newnode.id = ID
        for i in range(0,len(ws)):
            newnode.workshops.append(ws[i])

        #empty
        if self.root == None:
            self.root = newnode
        else:
            current = self.root
            while True:
                if current.id >= newnode.id:
                    if current.left == None:
                        current.left = newnode
                        break
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = newnode
                        break
                    else:
                        current = current.right

    def traversalhelper(self,x):
        if x:
            self.traversalhelper(x.left)
            x.print()
            self.traversalhelper(x.right)
            
    def inOrderTraversal(self):
        self.traversalhelper(self.root)

    def findWorkshopsById(self, employeeID):
        current = self.root
        while True:
            if current.id == employeeID:
                return current.workshops
                
            if current.id >= employeeID:
                if current.left == None:
                    return 0
                current = current.left
                
                
            else:
                if current.right == None:
                    return 0
                current = current.right
            
    global data
    data = []
    def workshoptraversalhelper(self,x,workshopname):
        global data
        if x:
            for i in x.workshops:
                if i[0] == workshopname:
                    data.append(x.id)
                    break
            self.workshoptraversalhelper(x.left,workshopname)
            self.workshoptraversalhelper(x.right,workshopname)
            
    def findIdsByWorkshop(self,workshopName):
        global data 
        data = []
        self.workshoptraversalhelper(self.root, workshopName)
        return data

    

    global cost
   

    def costfinder(self,x):
        global cost
        if x:
            for i in x.workshops:
                cost += int(i[1])
            self.costfinder(x.left)
            self.costfinder(x.right)
            
    def findTotalCost(self):
        global cost
        cost = 0
        self.costfinder(self.root)
        return cost
        


def CreateBST():
    file = open("T2_healthworkshops.txt","r")
    bst = BST()
    employeeids = []
    workshops = []
    for i in file:
        i = i.strip("\n")
        i = i.split("-")
        #print(i)
        ID = i[0]
        workshop = i[1]
        #print(workshops)
        workshop_data = []
        
        flag = False
        for i in workshop:
            if i == "[":
                flag = True
                s = ""
                continue
            
            if i == "]":
                flag = False
                s = s.split(",")
                #print(s)
                workshop_data.append(s)
                continue
            
            if flag:
                s += i
        employeeids.append(ID)
        workshops.append(workshop_data)
    
    for i in range(len(workshops)):
        bst.insert(employeeids[i],workshops[i])
    #bst.inOrderTraversal()
    file.close()
    return bst


def menu():
    while True:
        print("1) Read file to generate BST.")
        print("2) Find workshop(s) by user ID.")
        print("3) Find user ID(s) by workshop.")
        print("4) Display Users in Order.")
        print("5) Total cost.")
        print("6) Quit.")

        choices = ["1","2","3","4","5","6"]

        choice = input("Choose an action: ")

        if choice not in choices:
            print("Please enter valid choice")
            print()
            continue

        elif choice == "1":
            bst = CreateBST()

        elif choice == "2":
            
            while True:
                userid = input("Type a userId: ")
                if len(userid)>7:
                    print("Please enter valid user id.")
                    continue
                mapping = ["A","B","C","D","E","F","G","H","J","M","N","Q","R","S","T","Y","Z"]
                total = 0
                weights = [2,7,6,5,4,3,2]
                for i in range(len(userid)-1):
                    total += int(userid[i])*weights[i]
                total %= 17
                if mapping[total] != userid[-1]:
                    print("Please enter valid user id.")
                    continue
            
            print(bst.findWorkshopsById(userid))

        elif choice == "3":
            ws = input("Type a workshop name: ")
            print(bst.findIdsByWorkshop(ws))

        elif choice == "4":
            bst.inOrderTraversal()

        elif choice == "5":
            print(bst.findTotalCost())

        else:
            break
