# HW3
# Due Date: 10/15/2021, 11:59PM
# REMINDER: The work in this assignment must be your own original work and must be completed alone.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


# =============================================== Part I ==============================================

class Stack:

    def __init__(self):
        self.top = None

    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top, out))

    __repr__ = __str__
    '''Checks whether the current stack is empty by checking that self.top is not none'''
    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False
    '''Checks the length of the stack using a while loop.'''
    def __len__(self):
        count = 0
        current = self.top
        while current is not None:
            count += 1
            current = current.next
        return count
    '''Pushes an element into the stack by replacing top node.'''
    def push(self, value):
        nn = Node(value)
        if self.isEmpty():
            self.top = nn
        else:
            nn.next = self.top
            self.top = nn
    '''Pops an element from the top of the stack by replacing top node.'''
    def pop(self):
        if self.isEmpty():
            return None
        else:
            value = self.top.value
            self.top = self.top.next
            return value
    '''Returns top value of stack.'''
    def peek(self):
        return self.top.value


# =============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None
    '''Returns expression'''
    @property
    def getExpr(self):
        return self.__expr
    '''Allows you to set expression'''
    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr = new_expr
        else:
            print('setExpr error: Invalid expression')
            return None
    '''Checks whether the inputted value is a number by using a try/except clause on the float method.'''
    def _isNumber(self, txt):
        try:
            float(txt)
            return True
        except:
            return False
    '''Obtains postfix notation of element. Does so by using the operations of obtaining postfix mentioned in the
    videos.  The string is split into a list and it is then iterated through , utilizing stacks to operate on the value.
    The precedence is stored in a list.'''
    def _getPostfix(self, txt):
        postfix = ""
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        infix = txt.split()
        precedence = {"^": 0, "*": 1, "/": 1, "+": 2, "-": 2, "(": 3}
        for i in infix:
            if self.isNumber(i):
                postfix += str(float(i)) + " "
            elif i == ")" and not postfixStack.isEmpty():
                while postfixStack.peek() != "(":
                    value = postfixStack.pop()
                    postfix += value + " "
                postfixStack.pop()
            elif postfixStack.isEmpty():
                postfixStack.push(i)
            else:
                if postfixStack.isEmpty() is not True and i == "(":
                    postfixStack.push(i)
                elif postfixStack.isEmpty() is not True and precedence[i] < precedence[postfixStack.peek()]:
                    postfixStack.push(i)
                elif postfixStack.isEmpty() is not True and postfixStack.peek() == True:
                    postfixStack.push(i)
                else:
                    while postfixStack.isEmpty() is not True and precedence[i] >= precedence[postfixStack.peek()]:
                        value = postfixStack.pop()
                        postfix += value + " "
                    postfixStack.push(i)
        while not postfixStack.isEmpty():
            value = postfixStack.pop()
            postfix += value + " "
        postfix = postfix.strip(" ")
        return postfix
    '''This method allows for calculations to be made on infix expressions using stacks.  Each element is placed in a
    stack one-by-one, and when an operator is observed, the two objects below the operator in the stack are operated on.
    This proceeds until there is only one element left in the stack.'''
    @property
    def calculate(self):
        expr = self._getPostfix(self.__expr)
        postfix = expr.split()
        calcStack = Stack()

        if not isinstance(self.__expr, str) or len(self.__expr) <= 0:
            print("Argument error in calculate")
            return None

        for i in postfix:
            if self.isNumber(i):
                calcStack.push(i)
            elif i == "+":
                a = float(calcStack.pop())
                b = float(calcStack.pop())
                calcStack.push(a+b)
            elif i == "-":
                a = float(calcStack.pop())
                b = float(calcStack.pop())
                calcStack.push(b-a)
            elif i == "*":
                a = float(calcStack.pop())
                b = float(calcStack.pop())
                calcStack.push(a*b)
            elif i == "/":
                a = float(calcStack.pop())
                b = float(calcStack.pop())
                calcStack.push(b/a)
            elif i == "^":
                a = float(calcStack.pop())
                b = float(calcStack.pop())
                calcStack.push(b ** a)


# =============================================== Part III ==============================================

class AdvancedCalculator:
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}
    '''Checks whether the variable is an appropriate variable using the isalpha and isalnum methods.'''
    def _isVariable(self, word):
        if not word[0].isalpha():
            return False
        elif not word.isalnum():
            return False
        return True
    '''This method replaces variables by iterating through each element, replacing the variable in the list with the 
    actual value when found.  The list is then concatenated.'''
    def _replaceVariables(self, expr):
        expr = expr.split()
        for i in range(len(expr)):
            if self._isVariable(expr[i]):
                if expr[i] not in self.states:
                    return None
                if not str(self.states[expr[i]]).isnumeric():
                    return None
                expr[i] = str(self.states[expr[i]])
        return " ".join(expr)
    '''This method calculates expressions by using the definitions provided to construct the "states" dictionary.  This is
    done by splitting each function as much as possibe, and then extracting the information into the dictionary.  This process
    is repeated until the reversevariables method is used to make it into an actual function, and then the Calculator class is used
    to calculate the answer.'''
    def calculateExpressions(self):
        try:
            process = {}
            calcObj = Calculator()  # method must use calcObj to compute each expression
            expressions = self.expressions.split(";")
            for i in range(len(expressions)-1):
                expression = expressions[i].split(" = ")
                if expression[1].isnumeric():
                    self.states[expression[0]] = expression[1]
                    process[expressions[i]] = self.states
                else:
                    expression = expressions[i].split(" = ")
                    expression[1] = self._replaceVariables(expression[1])
                    calcObj.setExpr(expression[1])
                    expression[1] = calcObj.calculate
                    self.states[expression[0]] = expression[1]
                    process[expressions[i]] = self.states
            variable_expression = expressions[-1].strip("return ")
            expression = self._replaceVariables(variable_expression)
            calcObj.setExpr(expression)
            answer = calcObj.calculate
            process["_return_"] = answer
            return process
        except:
            return None
