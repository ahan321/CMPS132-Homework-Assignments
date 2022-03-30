# HW4
# Due Date: 11/05/2021, 11:59PM
# REMINDER: 
#       The work in this assignment must be your own original work and must be completed alone.
#       You might add additional methods to encapsulate and simplify the operations, but they must be
#       thoroughly documented


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return ("Node({})".format(self.value))

    __repr__ = __str__


class BinarySearchTree:

    def __init__(self):
        self.root = None

    '''This function acts as the first insert function.  It essentially checks whether there are any values in the BST,
    and if so, the _insert recursive function is called.  If not, then the node is inserted into the root.'''

    def insert(self, value):
        if self.root is None:
            split_value = []
            for i in value:
                split_value.append(i)
            split_value = sorted(list(split_value))
            ord_value = "".join(split_value)
            self.root = Node({ord_value: [value]})
        else:
            self._insert(self.root, value)

    '''This is a function I created in order to make checking for alphabetical order easier.  It is used both in the _insert
    method and in the getAnagrams method in the Anagrams class.  This could have been implemented seperately in both classes,
    but I felt that this would cut down on redundant code.'''

    def alphabetical_order(self, w1, w2):
        if w1 == w2:
            return "same"
        shortest_length = 0
        if len(w1) > len(w2):
            shortest_length = len(w2)
        else:
            shortest_length = len(w1)
        for i in range(shortest_length):
            if ord(w1[i]) < ord(w2[i]):
                return "left"
            elif ord(w1[i]) > ord(w2[i]):
                return "right"
        if len(w1) > len(w2):
            return "right"
        else:
            return "left"

    '''This function is a recursive function that is entered through the original insert function. After entering this function,
    recursion is enacted to find if the value already exists in the bst.  If not, reaching the NONE node will result in the node
    being added.'''

    def _insert(self, node, value):
        split_value = []
        for i in value:
            split_value.append(i)
        split_value = sorted(split_value)
        ord_value = "".join(split_value)

        if self.alphabetical_order(ord_value, list(node.value.keys())[0]) == "left":
            if (node.left == None):
                node.left = Node({ord_value: [value]})
            else:
                self._insert(node.left, value)
        elif self.alphabetical_order(ord_value, list(node.value.keys())[0]) == "right":
            if (node.right == None):
                node.right = Node({ord_value: [value]})
            else:
                self._insert(node.right, value)
        else:
            nlst = node.value[ord_value]
            nlst.append(value)
            node.value[ord_value] = nlst

    def isEmpty(self):
        return self.root == None

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


class Anagrams:
    def __init__(self, word_size):
        self.word_size = word_size
        self._bst = BinarySearchTree()

    '''This method reads through the mentioned file and categorizes the words.  The contents are then inserted into the 
    bst based on their length.'''

    def create(self, file_name):
        with open(file_name) as f:
            contents = f.read()
            lines = contents.splitlines()
            for i in lines:
                line = i.split()
                for j in line:
                    if len(j) <= self.word_size:
                        self._bst.insert(i)

    '''This function obtains the anagram of a word by searching through the bst for the word that is being searched for.  
    Once found, the anagrams are then mentioned.  If not found, "No match" is returned.'''

    def getAnagrams(self, word):
        sorted_word = sorted(word)
        sorted_word = "".join(sorted_word)
        if self._bst.isEmpty():
            return "No match"
        node = self._bst.root
        while node is not None:
            if list(node.value.keys())[0] == sorted_word:
                return node.value[sorted_word]
            elif self._bst.alphabetical_order(sorted_word, list(node.value.keys())[0]) == "right":
                node = node.right
            elif self._bst.alphabetical_order(sorted_word, list(node.value.keys())[0]) == "left":
                node = node.left
        return "No match"
