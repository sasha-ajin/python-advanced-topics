"""Operator Overloading means giving extended meaning beyond 
their predefined operational meaning. For example operator + is used 
to add two integers as well as join two strings and merge two lists. 
It is achievable because ‘+’ operator is overloaded by int class and 
str class. You might have noticed that the same built-in operator 
or function shows different behavior for objects of different classes, 
this is called Operator Overloading. 
"""

"""Let's check out how operators work"""
print(1 + 2)  # 3

"""Concatenate two strings"""
print("First" + "Second")  # FirstSecond

"""Product two numbers"""
print(3 * 4)  # 12

"""Repeat the String"""
print("Operator" * 4)  # OperatorOperatorOperatorOperator

### Overloading + operator###
"""When we use an operator on user defined data types then automatically 
a special function or magic function associated with that operator is invoked. 
Changing the behavior of operator is as simple as changing the behavior of 
method or function. You define methods in your class and operators work according 
to that behavior defined in methods. When we use + operator, the magic method 
__add__ is automatically invoked in which the operation for + operator is defined. 
There by changing this magic method’s code, we can give extra 
meaning to the + operator. 
"""
class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, o):
        return self.a + o.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("Sasha")
ob4 = A("Ajint")

print(ob1 + ob2)  # 3
print(ob3 + ob4)  # SashaAjint

"""Now let's check how it's going to work with integer parameters"""
class complex:
    def __init__(self, number):
        self.number = number

    # adding two objects
    def __add__(self, other):
        return self.number + other.number


Ob1 = complex(1)
Ob2 = complex(2)
Ob3 = Ob1 + Ob2
print(Ob3)  # 3

### Overloading Comparison Operators ###

"""Python does not limit operator overloading to arithmetic operators only.
We can overload comparison operators as well.

Suppose we wanted to implement the less than symbol < symbol in our Point class.

Let us compare the magnitude of these points from the origin and return the 
result for this purpose. It can be implemented as follows.
"""
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

p1 = Point(1,1)
p2 = Point(-2,-3)
p3 = Point(1,-1)

print(p1<p2)
print(p2<p3)
print(p1<p3)
"""Output:
True
False
False
"""

### Overloading other operators ###
"""
Subtraction         p1.__sub__(p2)
Multiplication      p1.__mul__(p2)
Power               p1.__pow__(p2)
Division		    p1.__truediv__(p2)

Less than                   p1.__lt__(p2)
Less than or equal to		p1.__le__(p2)
Equal to		            p1.__eq__(p2)
Not equal to		        p1.__ne__(p2)
Greater than		        p1.__gt__(p2)
Greater than or equal to    p1.__ge__(p2)
"""
