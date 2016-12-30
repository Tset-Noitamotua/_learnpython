# Class Variables vs. Instance Variables
# Viedo Tutorial: https://www.youtube.com/watch?v=BJ-VvGyQxho

"""
Class Variables: Are variables that are shared among ALL instances of a class and
                 have same values in each instance.
                 In this example 'anual_raise' is such a variable
 
Instance Variables: This variables can be unique for each instances
                    In this examples 'first', 'last' and 'pay' are such variables

"""

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # IMPORTANT: pay special attention to how the output changes when you change self.raise_amount
    #            to Employee.raise_amount
    #            --> self.raise_amount enables you to "apply_raise" per individual
    #            --> Employee.raise_amount will apply_raise to EVERY instance !!!!
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
emp_3 = Employee('Bitch', 'Fucker', 100000)

# Notice the different outputs of next statements!!!
# the first one does NOT have a 'raise_amount' variable because emp_1 is just an instance of class
print(emp_3.__dict__)
# $ {'last': 'Schafer', 'email': 'Corey.Schafer@company.com', 'first': 'Corey', 'pay': 50000}

# but here we see 'raise_amount': 1.04
print(Employee.__dict__)
# $ {'__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None, '__dict__':
# <attribute '__dict__' of 'Employee' objects>, 'raise_amount': 1.04, 'apply_raise': <function
# Employee.apply_raise at 0x1092456a8>, 'fullname': <function Employee.fullname at 0x109245730
# >, '__init__': <function Employee.__init__ at 0x109245620>, '__module__': '__main__'}

emp_3.raise_amount = 1.10
Employee.raise_amount = 1.06


print(Employee.raise_amount)
print(emp_1.apply_raise())
print(emp_2.apply_raise())
print('{0:.2f}'.format(emp_3.apply_raise()))

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_3.raise_amount)
print(Employee.raise_amount)

