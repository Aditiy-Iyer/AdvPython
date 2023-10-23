class MyClass:
   def my_method(self, arg1, arg2=None, arg3 = None):
      if arg3:
         print(arg1 + arg2 + arg3)
      elif arg2:
         print(arg1 + arg2)
      elif arg1:
         print(arg1)

# Calling the method with one argument
obj = MyClass()
obj.my_method(10)

# Calling the method with two arguments
obj.my_method(10, 20) 
# Calling the method with three arguments
obj.my_method(10, 20, 30) 