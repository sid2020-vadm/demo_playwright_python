import os
import shutil

# writing to file
def write_to_file(file_path):
    with open(file_path,'w') as file:
        file.write("write in to file")

#append to file
def append_to_file(file_path):
    with open(file_path,'a') as file:
        file.write("append to file")

#read text file
def read_text_file(file_path, mode="all"):
    with open(file_path,'r') as file:
        if mode == "all":
            file.read()
        elif mode == "line":
            file.readline()
        elif mode=="lines":
            file.readlines()
        else:
            raise  ValueError("invalid mode")

# renaming a file
def rename_file(source, target):
    os.rename(source,target)




