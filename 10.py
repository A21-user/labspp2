#global variables#

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Create a variable inside a function, with the same name as the global variable#


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



#also we can use global keyword#

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



#To change the value of a global variable inside a function#

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)