#Lab #7
#Due Date: 11/12/2021, 11:59PM
# REMINDERS: 
#        The work in this assignment must be your own original work and must be completed alone.

class MinBinaryHeap:
    def __init__(self):   # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    '''This method checks for the minimum value of the heap.  It does so by using the property of heaps that states that
    the root of the minimum heap is the root value.  The method checks if there are any values in the heap, and if so,
    returning to root of the heap.'''
    @property
    def getMin(self):
        if not self._heap:
            return None
        else:
            return self._heap[0]
    
    '''This method checks for the parent of the element by using integer division.  The method first checks whether the
    element is in the heap, and then does integer division using the heap rules on the index to determine the parent.'''
    def _parent(self,index):
        if len(self._heap) < index or index == 1:
            return None
        else:
            return self._heap[index//2-1]

    '''This method checks for the left child of an element.  A check is first done to see whether the left child actually
    exists, and then the index is multiplied by two to get the value of the left child.'''
    def _leftChild(self,index):
        if len(self._heap) < index * 2:
            return None
        else:
            return self._heap[index*2-1]

    '''This method checks for the right child of an element.  Like the previous method, a check is done to see whether
    the right child actually exists, and then index is multiplied by two and added to one in order to get the value of
    the right child.'''
    def _rightChild(self,index):
        if len(self._heap) < index * 2 + 1:
            return None
        else:
            return self._heap[index*2]

    '''This method inserts an element into the heap.  It first inserts an element into the end of the heap, and then 
    moves the element up if the parent is larger.  It continually does this until its parent is either the same size
    ore smaller.'''
    def insert(self,item):
        self._heap.append(item)
        pointer = len(self._heap)
        if not (self._leftChild(pointer) is None and self._rightChild(pointer) is None):
            if (self._parent(pointer) > self._heap[pointer - 1]) and pointer != 1:
                while not (self._leftChild(pointer) is None and self._rightChild(pointer) is None):
                    temp = self._heap[self._heap.index(item)]
                    index = pointer//2-1
                    self._heap[pointer - 1] = self._heap[pointer//2-1]
                    self._heap[index] = temp
                    pointer = pointer // 2
                    if (self._parent(pointer) <= self._heap[pointer - 1]) or pointer == 1:
                        break
            
    '''This function deletes the root node of the heap by switching it with the last element in the heap, and then deleting
    the last element in the heap.  After this, the new root node perculates down, moving down everytime there is is a child
    with a smaller value.  This continues until either all children are greater than it or there are no more children.'''
    def deleteMin(self):
        # Remove from an empty heap or a heap of size 1
        if len(self)==0:
            return None        
        elif len(self)==1:
            deleted=self._heap[0]
            self._heap=[]
            return deleted
        else:
            min = self.getMin
            temp = self._heap[0]
            self._heap[0] = self._heap[len(self._heap)-1]
            self._heap[len(self._heap)-1] = temp
            self._heap.pop()

            index = 1
            while not (self._leftChild(index) is None and self._rightChild(index) is None):
                if self._leftChild(index) is None:
                    temp = self._heap[index - 1]
                    temp_index = index * 2 + 1
                    self._heap[index - 1] = self._heap[temp_index - 1]
                    self._heap[temp_index - 1] = temp
                    index = index * 2 + 1
                elif self._rightChild(index) is None:
                    temp = self._heap[index - 1]
                    temp_index = index * 2
                    self._heap[index - 1] = self._heap[temp_index - 1]
                    self._heap[temp_index - 1] = temp
                    index = index * 2
                elif self._leftChild(index) <= self._rightChild(index):
                    temp = self._heap[index - 1]
                    temp_index = index * 2
                    self._heap[index - 1] = self._heap[temp_index - 1]
                    self._heap[temp_index - 1] = temp
                    index = index * 2
                elif self._leftChild(index) > self._rightChild(index):
                    temp = self._heap[index - 1]
                    temp_index = index * 2 + 1
                    self._heap[index - 1] = self._heap[temp_index - 1]
                    self._heap[temp_index - 1] = temp
                    index = index * 2 + 1
                else:
                    break

            return min


'''This method sorts the list in an ascending order.  It does so by placing all the elements in the list into a minimum
binary heap, and then removing the root node one by one, placing each element into a new list.'''
def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [-1, 0, 0, 1, 1, 2, 4, 4, 7, 7, 8, 9]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [-15, -15, -15, 0, 1, 2, 3.1, 4, 5, 8]
    '''
    h = MinBinaryHeap()
    newList = []
    for i in numList:
        h.insert(i)
    for i in range(len(numList)):
        m = h.deleteMin()
        newList.append(m)
    return newList
