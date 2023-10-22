class MyClass:
   def my_method(self, arg1, arg2=None):
      if arg2:
         print(arg1 + arg2)
      else:
         print(arg1)

# Calling the method with one argument
obj = MyClass()
obj.my_method(10)

# Calling the method with two arguments
obj.my_method(10, 20) 