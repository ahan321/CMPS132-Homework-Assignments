# HW5
# Due Date: 11/19/2021, 11:59PM
# REMINDER: 
#       The work in this assignment must be your own original work and must be completed alone.


class Node:
    def __init__(self, content):
        self.value = content
        self.next = None

    def __str__(self):
        return ('CONTENT:{}\n'.format(self.value))

    __repr__=__str__


class ContentItem:
    '''
        >>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
        >>> content2 = ContentItem(1004, 50, "Content-Type: 1", "110010")
        >>> content3 = ContentItem(1005, 18, "Content-Type: 2", "<html><p>'CMPSC132'</p></html>")
        >>> content4 = ContentItem(1005, 18, "another header", "111110")
        >>> hash(content1)
        0
        >>> hash(content2)
        1
        >>> hash(content3)
        2
        >>> hash(content4)
        1
    '''
    def __init__(self, cid, size, header, content):
        self.cid = cid
        self.size = size
        self.header = header
        self.content = content

    def __str__(self):
        return f'CONTENT ID: {self.cid} SIZE: {self.size} HEADER: {self.header} CONTENT: {self.content}'

    __repr__=__str__

    def __eq__(self, other):
        if isinstance(other, ContentItem):
            return self.cid == other.cid and self.size == other.size and self.header == other.header and self.content == other.content
        return False

    '''This function determines the hash value of the ContentItem. It does this by iterating through the characters in
    it, using the ord() function to obtain the ASCII codes.  These ASCII codes are summed up, and the modulus of three is
    obtained to get the hash value.'''
    def __hash__(self):
        count = 0
        for i in self.header:
            count += ord(i)
        return count % 3



class CacheList:
    ''' 
        # An extended version available on Canvas. Make sure you pass this doctest first before running the extended version

        >>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
        >>> content2 = ContentItem(1004, 50, "Content-Type: 1", "110010")
        >>> content3 = ContentItem(1005, 180, "Content-Type: 2", "<html><p>'CMPSC132'</p></html>")
        >>> content4 = ContentItem(1006, 18, "another header", "111110")
        >>> content5 = ContentItem(1008, 2, "items", "11x1110")
        >>> lst=CacheList(200)
        >>> lst
        REMAINING SPACE:200
        ITEMS:0
        LIST:
        <BLANKLINE>
        >>> lst.put(content1, 'mru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> lst.put(content2, 'lru')
        'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'
        >>> lst.put(content4, 'mru')
        'INSERTED: CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110'
        >>> lst.put(content5, 'mru')
        'INSERTED: CONTENT ID: 1008 SIZE: 2 HEADER: items CONTENT: 11x1110'
        >>> lst.put(content3, 'lru')
        "INSERTED: CONTENT ID: 1005 SIZE: 180 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>"
        >>> lst.put(content1, 'mru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> 1006 in lst
        True
        >>> contentExtra = ContentItem(1034, 2, "items", "other content")
        >>> lst.update(1008, contentExtra)
        'UPDATED: CONTENT ID: 1034 SIZE: 2 HEADER: items CONTENT: other content'
        >>> lst
        REMAINING SPACE:170
        ITEMS:3
        LIST:
        [CONTENT ID: 1034 SIZE: 2 HEADER: items CONTENT: other content]
        [CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>
        >>> lst.clear()
        'Cleared cache!'
        >>> lst
        REMAINING SPACE:200
        ITEMS:0
        LIST:
        <BLANKLINE>
    '''
    def __init__(self, size):
        self.head = None
        self.maxSize = size
        self.remainingSpace = size
        self.numItems = 0

    def __str__(self):
        listString = ""
        current = self.head
        while current is not None:
            listString += "[" + str(current.value) + "]\n"
            current = current.next
        return 'REMAINING SPACE:{}\nITEMS:{}\nLIST:\n{}'.format(self.remainingSpace, self.numItems, listString)  

    __repr__=__str__

    def __len__(self):
        return self.numItems

    '''This function inserts content into the CacheList. It does this by following the rules outlined in the homework
    specifications. If the size of the content is larger than the maximum size of the linked list, the insertion is not
    allowed to proceed.  If another node is found with the same cid in the CacheList, the insertion is also not allowed,
    but the node is moved to the head. If the content is larger than the space remaining, either the MRU or LRU eviction
    methods are used depending on the function inputs.  Lastly, the node is added in the beginning.'''
    def put(self, content, evictionPolicy):
        if content.size > self.maxSize:
            return "Insertion not allowed"
        elif self.__contains__(content.cid):
            n_prev = None
            n = self.head
            while self.head.value.cid != content.cid:
                n_prev = n
                n = n.next
            n_prev.next = n.next
            n.next = self.head
            self.head = n
            return f"Content {content.id} already in cache, insertion not allowed"
        elif content.size > self.maxSize:
            return "Insertion not allowed"
        else:
            if content.size > self.remainingSpace and evictionPolicy == "lru":
                while content.size > self.remainingSpace:
                    self.lruEvict()
            elif content.size > self.remainingSpace and evictionPolicy == "mru":
                while content.size > self.remainingSpace:
                    self.mruEvict()
            n = Node(content)
            n.next = self.head
            self.head = n
            self.remainingSpace -= content.size
            self.numItems += 1
            return f"INSERTED: {content}"

    
    '''Function checks to see if the given CID is already in the CacheList.  Does so by iterating down the linked list,
    and if the CID matches, True is returned.  Otherwise, False is returned.'''
    def __contains__(self, cid):
        if self.numItems == 0:
            return False
        n = self.head
        while n is not None:
            if n.value.cid == cid:
                return True
            n = n.next
        return False

    '''Function updates CacheList based on rules specified in Homework.  The function iterates through the linked list,
    and if the size of the content is larger than the space remaining or the given CID is not in the linked list, nothing
    is altered (except in the first case, where the node is moved to the top without being altered.  If the node is 
    found and doesn't break any of the above rules, then the content is updated and the node is moved to the top.'''
    def update(self, cid, content):
        n_prev = None
        n = self.head
        while n.value.cid != cid:
            if n.next is None:
                return "Cache miss!"
            n_prev = n
            n = n.next
        if content.size > self.remainingSpace + n.value.size:
            n_prev.next = n.next
            n.next = self.head
            self.head = n
            return "Cache miss!"
        n_prev.next = n.next
        n.next = self.head
        self.head = n
        self.head.value = content
        return f"UPDATED: {content}"


    '''Function evicts items by changing the head of the node.'''
    def mruEvict(self):
        self.remainingSpace += self.head.value.size
        self.numItems -= 1
        self.head = self.head.next

    '''Function evicts items my moving to the bottom of the linked list and then unlinking the last node.'''
    def lruEvict(self):
        if self.head.next is None:
            self.clear()
            return
        n = self.head
        while n.next.next is not None:
            n = n.next
        self.remainingSpace += n.next.value.size
        self.numItems -= 1
        n.next = None

    '''Function clears cache and returns linked list to original state.'''
    def clear(self):
        self.head = None
        self.remainingSpace = self.maxSize
        self.numItems = 0
        return "Cleared cache!"


class Cache:
    """
        # An extended version available on Canvas. Make sure you pass this doctest first before running the extended version

        >>> cache = Cache()
        >>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
        >>> content2 = ContentItem(1003, 13, "Content-Type: 0", "0xD")
        >>> content3 = ContentItem(1008, 242, "Content-Type: 0", "0xF2")

        >>> content4 = ContentItem(1004, 50, "Content-Type: 1", "110010")
        >>> content5 = ContentItem(1001, 51, "Content-Type: 1", "110011")
        >>> content6 = ContentItem(1007, 155, "Content-Type: 1", "10011011")

        >>> content7 = ContentItem(1005, 18, "Content-Type: 2", "<html><p>'CMPSC132'</p></html>")
        >>> content8 = ContentItem(1002, 14, "Content-Type: 2", "<html><h2>'PSU'</h2></html>")
        >>> content9 = ContentItem(1006, 170, "Content-Type: 2", "<html><button>'Click Me'</button></html>")

        >>> cache.insert(content1, 'lru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> cache.insert(content2, 'lru')
        'INSERTED: CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD'
        >>> cache.insert(content3, 'lru')
        'Insertion not allowed'

        >>> cache.insert(content4, 'lru')
        'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'
        >>> cache.insert(content5, 'lru')
        'INSERTED: CONTENT ID: 1001 SIZE: 51 HEADER: Content-Type: 1 CONTENT: 110011'
        >>> cache.insert(content6, 'lru')
        'INSERTED: CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011'

        >>> cache.insert(content7, 'lru')
        "INSERTED: CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>"
        >>> cache.insert(content8, 'lru')
        "INSERTED: CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>"
        >>> cache.insert(content9, 'lru')
        "INSERTED: CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>"
        >>> cache
        L1 CACHE:
        REMAINING SPACE:177
        ITEMS:2
        LIST:
        [CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>
        L2 CACHE:
        REMAINING SPACE:45
        ITEMS:1
        LIST:
        [CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011]
        <BLANKLINE>
        L3 CACHE:
        REMAINING SPACE:16
        ITEMS:2
        LIST:
        [CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>]
        [CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>]
        <BLANKLINE>
        <BLANKLINE>
    """

    def __init__(self):
        self.hierarchy = [CacheList(200), CacheList(200), CacheList(200)]
        self.size = 3
    
    def __str__(self):
        return ('L1 CACHE:\n{}\nL2 CACHE:\n{}\nL3 CACHE:\n{}\n'.format(self.hierarchy[0], self.hierarchy[1], self.hierarchy[2]))
    
    __repr__=__str__


    def clear(self):
        for item in self.hierarchy:
            item.clear()
        return 'Cache cleared!'

    '''Function inserts new content into the hierarchy by using the hash value to locate the CacheList, and then using
    the put() function to insert the node.'''
    def insert(self, content, evictionPolicy):
        return self.hierarchy[hash(content)].put(content,evictionPolicy)

    '''Function obtains items by iterating through the linked list, and if the value is found, the value is returned.'''
    def __getitem__(self, content):
        x = self.hierarchy[hash(content)]
        if content.cid in x:
            n = x.head
            while n is not None:
                if n.value.cid == content.cid:
                    return n.value
                n = n.next
        else:
            return "Cache miss!"



    '''Function updates the value of a node by utilizing the update function in the linkedlist.'''
    def updateContent(self, content):
        x = self.hierarchy[hash(content)]
        out = x.update(content.cid,content)
        if out == "Cache miss!":
            return "Cache miss!"
        else:
            return content
            