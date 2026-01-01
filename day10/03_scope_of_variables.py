# global and local variables
# global -- variables created outside of function
# local -- variables created within function
from pygments.styles.dracula import pink

# example 1
x = 20  # global variable


def my_fun1():
    y = 10  # local variable
    print(x) # 20 access global variable inside function
    print(y) # 10


my_fun1()

print(x)

# example 2
a=100 #global variable

def my_fun2():
    a=200 #local variable
    print(a) #o/p 200 local variable
my_fun2()

print(a) # o/p 100

# example 3
b=100
def my_fun3():
    global b # declare 'b' as global variable using keyword 'global'
    b=200
    print(b) # o/p 200 value of global variable is modified inside the function

my_fun3() #o/p b=200

print(b) # o/p b=200

# example 4
def my_fun4():
    global z # declare 'z' as global variable and can be accessed inside as well as outside function
    z=150
    print(z)

my_fun4()

print(z)

