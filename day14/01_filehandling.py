# textfile
# example1
# file= open("E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata\myfile.txt",'w')
# file.write("Welcome to file \n File handling")
# file.close()

# example2
# with open("E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata\myfile.txt",'w') as file:
#     file.write("welcome to file \n file handling")

# example3
# file= open("E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata\myfile.txt",'a')
# file.write("append this line.")
# file.close()

# example4
# read() -- entire data
#readline() -- read single line
#readlines() --read all lines in list format
# file= open("E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata\myfile.txt",'r')
# content=file.read()
# print(content)
# file.close()

# renaming file name
# import os
# os.rename("E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata\myfile.txt",
#           "E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata\myfile1.txt")
# print("file rename")

#deleting file
# import os
# path = "E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata\myfile1.txt"
# if os.path.exists(path):
#     os.remove(path)
# else:
#     print("file doesn't exist")


#create directory and/or folder
# import os
# os.mkdir("E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata/mydir")
# print("directory created")

# verify directory exist or not
# import os
# path = "E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata/mydir"
# if os.path.exists(path):
#     print("directory exist")
# else:
#     print("not exist")

#  rename directory
# import os
# os.rename("E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata/mydir",
#           "E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata/mydir_new")
# print("rename directory")

# remove empty directory
# import os
# os.rmdir("E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata/mydir_new")

#remove empty/ non-empty directory
# import shutil
# shutil.rmtree("E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata/mydir_new")

# current working directory
import os
print(os.getcwd())




