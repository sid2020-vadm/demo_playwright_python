# 1. Arbitrary or Variable-length arguments
# 2. Positional or required arguments
# 3.Keyword arguments

# 1. Arbitrary or Variable-length arguments
def sum_fun(a,b):
    return a+b

print(sum_fun(2,3))

# def sum_fun2(*num):
def sum_fun2(*num:int):
    total = 0
    for i in num:
        total+=i
    return total

print(sum_fun2(2,3))
print(sum_fun2(2,6,4,2))

# 2. Positional or required arguments
def my_fun(i,j):
    print(i,j)

my_fun(5,3)
my_fun(j=5,i=3)

# 3.Keyword arguments
def my_fun3(i,j=10): #set default value to variable
    print(i,j)

my_fun3(2)

def my_fun4(i=20,j=10): #set default value to variables
    print(i,j)

my_fun4()

# 4 mixing of both positional and keyword arguments
def my_fun5(i,j=10,k=10):
    print(i,j)

my_fun5(10,30,k=10)

# 5 Function return multiple values
def largest(a,b):
    if a>b:
        return  a,b
    else:
        return b,a

res =print(largest(10,20))

print(type(res))






