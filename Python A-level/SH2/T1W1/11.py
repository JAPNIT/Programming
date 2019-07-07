class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, s):
        new_node = Node(s)

        #empty
        if self.root == None:
            self.root = new_node

        #not empty
        else:
            current = self.root
            left_flag = False
            
            while True:
                if current.data < s:
                    if current.right == None:
                        break
                    else:
                        current = current.right

                else:
                    if current.left == None:
                        left_flag = True
                        break
                    else:
                        current = current.left

            if left_flag:
                current.left = new_node
            else:
                current.right = new_node

    def exists(self, s):
        current = self.root
        while True:
            if current == None:
                return False
            elif s > current.data:
                current = current.right
            elif s == current.data:
                return True
            else:
                current = current.left

    def count_helper(self,node):
        if node:
            return 1 + self.count_helper(node.left) + self.count_helper(node.right)
        else:
            return 0

    def count(self):
        return self.count_helper(self.root)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def print(self):
        self.inorder(self.root)
        
Bst = BST()
Bst.insert(3)

Bst.insert(30)

Bst.insert(22)

Bst.insert(1)

Bst.insert(5)
Bst.insert(521)
Bst.insert(52)

#Bst.print()
print(Bst.count())

