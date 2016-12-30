# Superb explanation of the difference between Classes and Instances
# Video Tutorial: https://www.youtube.com/watch?v=ZDa-Z5JzLYM

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 60000)


print(emp_1)
print(emp_2)
#
# Output:
# $ <__main__.Employee object at 0x104d2b860>
# $ <__main__.Employee object at 0x104d2b898>


print(emp_1.email)
print(emp_2.email)
#
# Output:
# Corey.Schafer@company.com
# Test.User@company.com

# Both statements below have the same result
# but the first one calling 'fullname()' on instance (emp_1) of class 'Employee'
# while the second is calling 'fullname()' directly on the class 'Employee' itself
# --> in first case emp_1 is automatically passed in as 'self' argument to 'fullname()'
# --> in second case emp_1 have to be passed manually
print(emp_1.fullname())
print(Employee.fullname(emp_1))
#
# Output:
# Corey Schafer
# Corey Schafer

