# HW2
# Due Date: 09/24/2021, 11:59PM
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random


class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    #Initializes object
    def __init__(self, cid, cname, credits):
        self.cid = cid
        self.cname = cname
        self.credits = credits

    # Allows this object to be represented as a string.
    def __str__(self):
        return str(self.cid) + "(" + str(self.credits) + "): " + str(self.cname)

    __repr__ = __str__
    # Allows the equality operator to be used.
    def __eq__(self, other):
        if self.cid is Course and self.cid is Course:
            if self.cid  == other.cid:
                return True
        return False


class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': (CMPSC132(3): Programming in Python II, 400), 'CMPSC360': (CMPSC360(3): Discrete Mathematics, 200)}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': (CMPSC132(3): Programming in Python II, 400)}
        >>> isinstance(C.courseOfferings['CMPSC132'][0], Course)
        True
    '''
    #Initializes Object
    def __init__(self):
        self.courseOfferings = {}
    # Adds a course to the catalog if it doesn't exist.
    def addCourse(self, cid, cname, credits, capacity):
        if cid in self.courseOfferings:
            return "Course already added"
        i = Course(cid, cname, credits)
        self.courseOfferings[cid] = (i, capacity)
        return "Course added successfully"
    # Removes course if it exists.
    def removeCourse(self, cid):
        if cid not in self.courseOfferings:
            return "Course not found"
        self.courseOfferings.pop(cid)
        return "Course removed successfully"


class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> isinstance(semester.courses['CMPSC132'], Course)
        True
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132, MATH 230
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.courses
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''
    # Initializes the object
    def __init__(self, sem_num):
        self.sem_num = sem_num
        self.courses = {}
    # Makes the object inot a string.
    def __str__(self):
        key = self.courses.keys()
        courses = ""
        for i in key:
            courses += i
            courses.append(", ")
        courses.strip(", ")
        return courses

    __repr__ = __str__
    # Adds course to the semester if it exists.
    def addCourse(self, course):
        if course.cid in self.courses:
            return "Course already added"
        self.courses[course.cid] = course
    # Drops course if it doesn't exist.
    def dropCourse(self, course):
        if course not in self.courses:
            return "No such course"
        self.courses.pop(course)

    # Counts up total credits of semester.
    @property
    def totalCredits(self):
        attributes = self.courses.values()
        count = 0
        for i in attributes:
            count += i.credits
            return count
    # Checks if student is full time.
    @property
    def isFullTime(self):
        count = self.totalCredits
        if count >= 12:
            return True
        return False

    
class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    
    # Initializes the object.
    def __init__(self, amount):
        self. amount = amount
        self.loan_id = self.__getloanID
    # Represents the object as a string
    def __str__(self):
        return "Balance: $" + str(self.amount)

    __repr__ = __str__

    # Crafts the loan ID using random.randrange
    @property
    def __getloanID(self):
        return random.randrange(10000,100000,1)


class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''
    # Intitializes object
    def __init__(self, name, ssn):
        self.name = name
        self.__ssn = ssn
    # Makes object into string
    def __str__(self):
        ssn = self.__ssn
        new_ssn = ""
        for i in range(7):
            if ssn[i].isnumeric():
                new_ssn += "*"
            elif ssn[i].isnumeric() == False:
                new_ssn += "-"
        new_ssn += ssn[7:]

        return "Person(" + self.name + ", " + new_ssn + ")"

    __repr__ = __str__
    # Obtains SSN of individual from other classes.
    def get_ssn(self):
        return self.__ssn
    # Allows equality operator to be used.
    def __eq__(self, other):
        if isinstance(self, Person) and isinstance(other, Person):
            if self.__ssn == other.get_ssn():
                return True
            return False


class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC132}
    '''
    # Initializes the object
    def __init__(self, name, ssn, supervisor=None):
        self.name = name
        self.ssn = ssn
        self.__supervisor = supervisor

    # Allows the object to be represented as a string
    def __str__(self):
        return "Staff(" + self.name + ", " + self.ssn + ", " + self.__supervisor + ")"

    __repr__ = __str__

    @property
    #Generates the ID number of individual
    def id(self):
        initials = ""
        for i in range(self.name):
            if self.name[i].upper():
                initials.append(self.name[i])
        ssn = self.ssn[:-4]
        return "905" + initials + ssn

    @property
    # OBtains supervisor of individual.
    def getSupervisor(self):
        return self.__supervisor

    # Sets supervisor for staff member
    def setSupervisor(self, new_supervisor):
        self.__supervisor = new_supervisor
        if new_supervisor is not Staff:
            return None
        self.__supervisor = new_supervisor
        return "Completed!"

    #Allows a hold to be placed on student
    def applyHold(self, student):
        if student is not Student:
            return None
        student.hold = True
        return "Completed!"

    # Removes hold on student
    def removeHold(self, student):
        if student is not Student:
            return None
        student.hold = False
        return "Completed!"

    # Unenrolls student from class
    def unenrollStudent(self, student):
        if student is not Student:
            return None
        student.active = False
        return "Completed!"

    # Creates a new student from a Person object
    def createStudent(self, person):
        return Student(person.name, person.get_ssn(), "Freshman")




class Student(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132, CMPSC360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: No courses}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
    '''
    # Initializes object
    def __init__(self, name, ssn, year):
        random.seed(1)
        self.name = name
        self.ssn = ssn
        self.year = year
        self.semesters = {}
        self.hold = False
        self.account = self.__createStudentAccount()
        self.active = True

    # Allows object to be string
    def __str__(self):
        return f"Student({self.name}, {self.id}, {self.year}"

    __repr__ = __str__
    # creates a studentaccount class.
    def __createStudentAccount(self):
        if not self.active:
            return None
        return StudentAccount(self.name, self.ssn, self.year)
    #Allows the id to be created
    @property
    def id(self):
        initials = ""
        for i in range(self.name):
            if self.name[i].upper():
                initials += self.name([i])
        ssn = self.ssn[:-4]
        return initials + ssn
    # Registers semester on the object.
    def registerSemester(self):
        if not self.active or not self.hold:
            return None
        if self.semesters == {}:
            self.semesters.update({1: Semester(1)})
            return None
        last_sem = self.semesters[-1].sem_num
        self.semesters.update({last_sem+1: Semester(last_sem+1)})
        if len(self.semesters) == 1 or len(self.semesters) == 2:
            self.year = "Freshman"
        elif len(self.semesters) == 3 or len(self.semesters) == 4:
            self.year = "Sophomore"
        if len(self.semesters) == 3 or len(self.semesters) == 4:
            self.year = "Junior"
        if len(self.semesters) == 5 or len(self.semesters) == 6:
            self.year = "Senior"
    # enrolls in course.
    def enrollCourse(self, cid, catalog, semester):
        if not self.active or not self.hold:
            return "Course added successfully"
        if cid not in catalog.courseOfferings:
            return "“Course not found"
        if cid in self.semesters[semester]:
            return "Course already enrolled"
        self.semesters[semester].addCourse(cid)
        return "Course added successfully"


    def dropCourse(self, cid):
        if not self.active or not self.hold:
            return "Course added successfully"
        if cid not in self.semesters[len(self.semesters)]:
            return "“Course not found"
        self.semesters[len(self.semesters)].pop(cid)
        return "Course dropped successfully"

    def getLoan(self, amount):
        if not self.active:
            return "Unsuccessful operation"
        if not self.semesters[len(self.semesters)].active:
            return "Not full-time"
        loan = Loan(amount)
        self.account.loans.update({loan.loan_id: loan})





class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4, 600)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2, 500)
        'Course added successfully'
        >>> C.addCourse('CMPEN270', 'Digital Design', 4, 300)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''
    
    def __init__(self, student):
        self.student = student
        self.balance = 1000
        self.loans = {}


    def __str__(self):
        return f"Name: {self.student.name}\nID: {self.student.id}\nBalance: {self.balance}"

    __repr__ = __str__


    def makePayment(self, amount):
        self.balance -= amount


    def chargeAccount(self, amount):
        self.balance += amount




#############################################################################################
