# Lab #5
# Due Date: 10/22/2021, 11:59PM 
# REMINDERS: 
#        The work in this assignment must be your own original work and must be completed alone.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.isEmpty()
        True
        >>> x.insert(9)
        >>> x.insert(4)
        >>> x.insert(11)
        >>> x.insert(2)
        >>> x.insert(5)
        >>> x.insert(10)
        >>> x.insert(9.5)
        >>> x.insert(7)
        >>> x.getMin
        Node(2)
        >>> x.getMax
        Node(11)
        >>> 9.5 in x
        True
        >>> x.isEmpty()
        False
        >>> x.getHeight(x.root)   # Height of the tree
        3
        >>> x.getHeight(x.root.left.right)
        1
        >>> x.getHeight(x.root.right)
        2
        >>> x.getHeight(x.root.right.left)
        1
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
        >>> new_tree = x.mirror()
        11 : 10 : 9.5 : 9 : 7 : 5 : 4 : 2 : 
        >>> new_tree.root.right
        Node(4)
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
    '''
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    @property
    def printInorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)         


    def mirror(self):
        # Creates a new BST that is a mirror of self: Elements greater than the root are on the left side, and smaller values on the right side
        # Do NOT modify any given code
        if self.root is None:
            return None
        else:
            newTree = BinarySearchTree()
            newTree.root = self._mirrorHelper(self.root)
            newTree.printInorder
            return newTree

# This method checks if the binary search tree is empty.  It does so by checking the status of isEmpty.
    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False


# This alters the order of the children for a node by taking out a node and altering the stored variables of the children.
    def _mirrorHelper(self, node):
        nn = Node()
        if node is None:
            return None
        else:
            nn.value = node
            nn.left = node.right
            nn.right = node.left
    # This method obtains the minimum value in the search tree by moving down the left side of the search tree.
    @property
    def getMin(self):
        if self.isEmpty():
            return None
        else:
            node = self.root
            while node.left is not None and node.right is not None:
                if node.left.value < node.right.value:
                    node = node.left
                elif node.right.value > node.left.value:
                    node = node.right

        return node


# This method finds the largest value in the search tree by moving down the right of the search tree.
    @property
    def getMax(self): 
        if self.isEmpty():
            return None
        else:
            node = self.root
            while node.left is not None and node.right is not None:
                if node.left.value < node.right.value:
                    node = node.right
                elif node.right.value > node.left.value:
                    node = node.left
        return node

    # This method checks whether a value is contained in the search tree by iterating through it.  Returns true if found, and
    #returns false if not found.
    def __contains__(self,value):
        node = self.root
        while not (node.left is None and node.right is None):
            if node.value == value:
                return True
            if node.value > value:
                node = node.left
            elif node.value < value:
                node = node.right
        if node.value == value:
            return True
        return False



    # This method obtains the height of the node by iterating through all the combinations using a while loop.
    def getHeight(self, node):
        if not self.__contains__(node):
            return False
        else:
            count = 0
            while not (node.left is None and node.right is None):
                if node.left is None:
                    node = node.right
                    count += 1
                elif node.right is None:
                    node = node.left
                    count +=1




