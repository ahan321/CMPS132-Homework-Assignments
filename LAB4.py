class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class SortedLinkedList:
    def __init__(self):  # You are not allowed to modify the constructor
        self.head = None
        self.tail = None

    def __str__(self):  # You are not allowed to modify this method
        temp = self.head
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = ' -> '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__ = __str__

    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        return count

    '''This function adds a value to the linked list.  It does so by first creating a new node, and then running a series
    of checks on the linkedlist.  Firstly, the inputted value is checked to be either a float or an int.  Once the new node
    is created a check is done to see if the linkedlist is empty.  If so, the head and tail are set to the new node.
    Otherwise, the value is checked against the head value to see if its less than it.  If so, the node is added to the beginning
    of the linkedlist.  If the value is greater than or equal to the tail value, it is added to the end of the linked list.  Lastly,
    It is assumed that the value should go somewhere within the list, hence a while loop is used to search through the linked list,
    and when the location is found, the node is appended.'''
    def add(self, value):
        if type(value) == int or type(value) == float:
            newNode = Node(value)
            if self.isEmpty():
                self.head = newNode
                self.tail = newNode
            elif value <= self.head.value:
                newNode.next = self.head
                self.head = newNode
            elif value >= self.tail.value:
                self.tail.next = newNode
                self.tail = newNode
            else:
                pointer = self.head
                while pointer.next.value < value:
                    pointer = pointer.next
                newNode.next = pointer.next
                pointer.next = newNode

    '''This function works by running certain checks.  It starts by creating a new sorted linked list.  If the first element
    of the original linked list is equivalent to none, it is assumed that the linked list is empty and hence none is returned.
    After this, a check is done to see if the value is a float or a negative integer, and two instances of that node is then added.
    After this, a check is done to see if the value is zero, and a single 0 is added if so.  Lastly, it is assumed that the value
    is a positive integer, and then the correct number of the node is then added according to its value.'''
    def replicate(self):
        nll = SortedLinkedList()
        if self.head is None:
            return None
        pointer = self.head
        while pointer is not None:
            if type(pointer.value) == float or (type(pointer.value) == int and pointer.value < 0):
                nll.add(pointer.value)
                nll.add(pointer.value)
            elif pointer.value == 0:
                nll.add(0)
            else:
                for i in range(pointer.value):
                    nll.add(pointer.value)
            pointer = pointer.next
        return nll

    '''This function works by first checking if the linked list is empty, and returning none if so.  Afterwards, the pointer
    is then moved through the list using a while loop, and if the next item in the linked list matches the current value, then
    the next value of the list is removed, and the pointer stays at the same location.  If the next node and current node doesn't
    match, then the pointer moves on.'''
    def removeDuplicates(self):
        if self.head is None:
            return None
        else:
            pointer = self.head
            while pointer.next is not None:
                if pointer.value == pointer.next.value:
                    pointer.next = pointer.next.next
                else:
                    pointer = pointer.next