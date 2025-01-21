x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z) #is equals print(x, y, z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y) # print(x + y) its not correct

x = "awesome"
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)