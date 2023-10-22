class Employee:
   def func_message(self):
        print('Welcome to Employee')
class Department(Employee):
     def func_message(self):
        print('Welcome to Department.')
        print('This is inherited from Employee')
emp = Employee()
emp.func_message()
print('------------')
dept = Department()
dept.func_message()
