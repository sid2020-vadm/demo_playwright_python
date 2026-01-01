# handling exception using try and except
# example 1
# print("started..")
# try:
#     print(x)
# except:
#     print("exception occured")
# print("finished..")

# example 2
# try:
#     print(x)
# except NameError:
#     print("variable x is not defined..")
# except:
#     print("some other exception")

# example 3
# 'except' block executed when there is exception
# 'else' block executed when there is no exception occurred
# try:
#     print("hello..")
# except:
#     print("something went wrong..")
# else:
#     print("nothing went wrong..")

# example4
# 'finally' block will always execute
# try:
#     print("hello..")
# except NameError:
#     print("Name Error")
# finally:
#     print("finally block")

#example5 - try,except,else,finally
# try:
#     a =int(input("enter a number: "))
#     res = 10/a
#
# except ZeroDivisionError:
#     print("can not be divisible by zero")
# except ValueError:
#     print("Enter valid number..")
# else:
#     print(f"result: {res}")
# finally:
#     print("finally block..")

# example 6 nested try block
# try:
#     file_path="E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata\/newfile.txt"
#     try:
#         with open(file_path,"r") as file:
#             file.write("write into file")
#     except:
#         print("not able to edit file..")
#     finally:
#         file.close()
# except:
#     print("file path not found")


# example 7 'raise' exceptions
# x=-1
# if(x<0):
#     raise Exception("number is less than zero")

# example 8
# x="hello"
# if not type(x) is int:
#     raise TypeError("only integers allowed..")

# example 9

def set(age):
    if age<0:
        raise  ValueError("age cannot be -ve ")
    print("Age is ",age)

try:
    set(-20)
except ValueError:
    print("invlaid data")