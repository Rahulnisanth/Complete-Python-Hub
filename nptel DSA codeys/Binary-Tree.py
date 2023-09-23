# USER-DEFINED BINARY TREE USING .py :
class Tree:
    def __init__(self, val=None):
        self.value = val
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None

    def minval(self):
        if self.left.isempty():
            return(self.value)
        else:
            return self.left.minval()

    def maxval(self):
        if self.right.isempty():
            return(self.value)
        else:
            return(self.right.maxval())

    def isempty(self):
        return(self.value == None)

    def isleaf(self):
        return(self.left == None and self.right == None)

    def copyright(self):
        self.value = self.right.value
        self.left  = self.right.left
        self.right = self.right.right
        return

    def inorder(self):
        if self.isempty():
            return([])
        else:
            return(self.left.inorder()+[self.value]+self.right.inorder())

    def makempty(self):
        self.value = None
        self.left = None
        self.right = None
        return

    def delete(self, val):
        if self.isempty():
            return
        if val < self.value:
            self.left.delete(val)
            return 
        if val > self.value:
            self.right.delete(val)
            return
        if self.value == val:
            if self.isleaf():
                self.makempty()
            elif self.left.isempty():
                self.copyright()
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return
        
    def insert(self, val):
        if self.isempty():
            self.value = val
            self.left = Tree()
            self.right = Tree()
        if self.value == val:
            return('!!Value already exists!!')
        if val < self.value:
            self.left.insert(val)
            return 
        if val > self.value:
            self.right.insert(val)
            return 
    
    def find(self, val):
        if self.isempty():
            return(False)
        if self.value == val:
            return(True)
        if val < self.value:
            return(self.left.find(val))
        if val > self.value:
            return(self.right.find(val))
        
    def __str__(self) -> str:
        return(str(self.inorder()))


# DRIVE PROGRAM :
# tree = Tree()

# for i in [1,2,3,4,67,8,9,10]:
#     tree.insert(i)

# print(tree)
# tree.delete(67)
# tree.insert(2.5)
# print(tree.find(2.5))
# print(tree.minval())
# print(tree.maxval())
# print(tree)
# tree.makempty()
# print(tree)
