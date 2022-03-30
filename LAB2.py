# LAB2
# Due Date: 09/17/2021, 11:59PM
# REMINDER: The work in self assignment must be your own original work and must be completed alone.

import random
import math

class Vendor:

    def __init__(self, name):
        '''
            In self class, self refers to Vendor objects
            
            name: str
            vendor_id: random int in the range (999, 999999)
        '''
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        '''
            Creates and initializes (instantiate) an instance of VendingMachine 
        '''
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        '''
            machine: VendingMachine
            item: int
            amount : int/float

            Call _restock for the given VendingMachine object
        '''
        return machine._restock(item, amount)
        


class VendingMachine:
    '''
        In self class, self refers to VendingMachine objects

        >>> john_vendor = Vendor('John Doe')
        >>> west_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> john_vendor.restock(west_machine, 215, 9)
        'Invalid item'
        >>> west_machine.isStocked
        True
        >>> john_vendor.restock(west_machine,156, 1)
        'Current item stock: 4'
        >>> west_machine.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Please deposit $1.5'
        >>> west_machine.purchase(156,2)
        'Please deposit $3.0'
        >>> west_machine.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> west_machine.deposit(3)
        'Balance: $3'
        >>> west_machine.purchase(156,3)
        'Please deposit $1.5'
        >>> west_machine.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.deposit(300)
        'Balance: $300'
        >>> west_machine.purchase(876)
        'Invalid item'
        >>> west_machine.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> west_machine.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> west_machine.purchase(156,3)
        'Please deposit $4.5'
        >>> west_machine.deposit(4.5)
        'Balance: $4.5'
        >>> west_machine.purchase(156,3)
        'Item dispensed'
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Item out of stock'
        >>> west_machine.deposit(6)
        'Balance: $6'
        >>> west_machine.purchase(254,3)
        'Item dispensed'
        >>> west_machine.deposit(9)
        'Balance: $9'
        >>> west_machine.purchase(879,3)
        'Item dispensed'
        >>> west_machine.isStocked
        False
        >>> west_machine.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> west_machine.purchase(156,2)
        'Machine out of stock'
        >>> west_machine.purchase(665,2)
        'Invalid item'
        >>> east_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> east_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> east_machine.deposit(10)
        'Balance: $10'
        >>> east_machine.cancelTransaction()
        'Take your $10 back'
        >>> east_machine.purchase(156)
        'Please deposit $1.5'
        >>> east_machine.cancelTransaction()
    '''
    # This function initializes the vending machine by creating the dict and setting the balance.
    def __init__(self):
        self.items = {156:[1.5,3],254: [2.0,3], 384: [2.5, 3], 879: [3.0, 3]}
        self.acc_bal = 0

    # This long function allows for the purchase of items.  It checks all the cases shown in the PDF
    # and resolves them accordingy.  Stock and balance are also adjusted accordingly.
    def purchase(self, item, qty=1):
        if item not in self.items:
            return "Invalid item"
        count = 0
        for i in range(len(list(self.items.items()))):
            if list(self.items.items())[i][1] == 0:
                count += 1
        if count == len(list(self.items.items())):
            return "Machine out of stock"
        if self.items[item][1] == 0:
            return "Item out of stock"
        if self.items[item][1] == 0:
            return f"current {item} stock: {self.items[item][1]}, try again"
        if self.acc_bal < self.items[item][0]:
            return f"Please deposit ${self.items[item][0]- self.acc_bal}"
        if self.acc_bal == self.items[item][0]:
            self.acc_bal = 0
            existing_stock = self.items[item].pop()
            existing_stock -= qty
            self.items[item].append(existing_stock)
            return "Item dispensed"
        if self.acc_bal > self.items[item][0]:
            existing_stock = self.items[item].pop()
            existing_stock -= qty
            money = self.acc_bal - self.items[item][0]
            self.acc_bal = 0
            return f"Item dispensed, take your ${money} back"

    # This function allows for the deposit of funds by first checking the stock of the machine, before adding money.
    def deposit(self, amount):
        count = 0
        for i in range(len(list(self.items.items()))):
            if list(self.items.items())[i][1] == 0:
                count += 1
        if count == len(list(self.items.items())):
            return f"Machine out of stock. Take your ${amount} back"
        else:
            self.acc_bal += amount
            return f"Balance: ${self.acc_bal}"

    # This function allows for the restock of items by popping and appending the dictionary.
    def _restock(self, item, stock):
        if item in self.items:
            existing_stock = self.items[item].pop()
            existing_stock += stock
            self.items[item].append(existing_stock)
            return f"Current item stock: {existing_stock}"
        else:
            return "Invalid item"

    # This function returns whether there is stock in the machine.
    @property
    def isStocked(self):
        for i in range(len(list(self.items.items()))):
            if list(self.items.items())[i][1] != 0:
                return True
        return False
        
    @property
    def getStock(self):
        return self.items


    def cancelTransaction(self):
        if self.acc_bal > 0:
            money = acc_bal
            self.acc_bal = 0
            return f"Take your ${money} back"
       


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = 4*line1
        >>> line3
        y = 1.825x + 15.1
        >>> line1==line2
        False
        >>> line3==line2
        True
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> line5==9
        False
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
    '''
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    # This function uses the distance formula in order to return the distance between both points.
    @property
    def getDistance(self):
        return round(math.sqrt((self.point2.x-self.point1.x)**2+(self.point2.y-self.point1.y)**2),3)
       
    # This function finds the slppe using the slope formula.
    @property
    def getSlope(self):
        return round(((self.point2.y - self.point1.y)/(self.point2.x - self.point1.x)),3)

    # This function iterates through different permutations of the string in order to determine which matches the given input, and then returns as a string.

    def __str__(self):
        if self.getSlope == 0 and self.getSlope*self.point2.x == 0:
            return 0
        if self.getSlope == 0 and self.point2.y-self.getSlope*self.point2.x < 0:
            return f"y = -{round(-1*(self.point2.y-self.getSlope*self.point2.x))}"
        if self.getSlope == 0 and self.point2.y-self.getSlope*self.point2.x > 0:
            return f"y = {round(self.point2.y-self.getSlope*self.point2.x)}"
        if self.point2.y-self.getSlope*self.point2.x < 0:
            return f"y = {self.getSlope}x - {round(-1*(self.point2.y-self.getSlope*self.point2.x))}"
        if self.point2.y-self.getSlope*self.point2.x == 0:
            return f"y = {self.getSlope}x"
        if self.point2.y-self.getSlope*self.point2.x > 0:
            return f"y = {self.getSlope}x + {round(self.point2.y-self.getSlope*self.point2.x)}"
        else:
            return "Undefined"


    # This function works in a similar manner to the previous function, except it is meant mainly to return a string.
    def __repr__(self):
        if self.getSlope == 0 and self.getSlope*self.point2.x == 0:
            return 0
        if self.getSlope == 0 and self.point2.y-self.getSlope*self.point2.x < 0:
            return f"y = -{round(-1*(self.point2.y-self.getSlope*self.point2.x))}"
        if self.getSlope == 0 and self.point2.y-self.getSlope*self.point2.x > 0:
            return f"y = {round(self.point2.y-self.getSlope*self.point2.x)}"
        if self.point2.y-self.getSlope*self.point2.x < 0:
            return f"y = {self.getSlope}x - {round(-1*(self.point2.y-self.getSlope*self.point2.x))}"
        if self.point2.y-self.getSlope*self.point2.x == 0:
            return f"y = {self.getSlope}x"
        if self.point2.y-self.getSlope*self.point2.x > 0:
            return f"y = {self.getSlope}x + {round(self.point2.y-self.getSlope*self.point2.x)}"
        else:
            return "Undefined"

    # This function checks whether two Line objects are the same.
    @property
    def __eq__(self, line2):
        if self.point2.x == line2.point2.x and self.point2.y == line2.point2.y and self.point1.x == line2.point1.x and self.point1.y == line2.point1.y:
            return True
        else:
            return False

    # This function multiplies a line and an integer by multiplying each point.
    def __mul__(self, other):
        return Line(Point2D(self.point1.x*other,self.point1.y*other),Point2D(self.point2.x*other,self.point2.y*other))

    # This function allows for the multiplication operation to be reversed.
    def __rmul__(self,other):
        return self*other
        