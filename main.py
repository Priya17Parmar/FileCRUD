## Project - CRUD operations with python

# from pathlib import Path
# def readfileandfolder():
#     p = Path('')
#     items = list(p.rglob('*'))  ## sari files lko list me store krane ke liye 
#     for index,file in enumerate(items):
#         print(f"{index +1}- (file)") 
# def create__file():
#     readfileandfolder()  ## path me jo file and folder he uske liye
#     file_name = input("Enter your file name:") 
#     p = Path(file_name) # path me  dalkr check krenge file exist krti he ya nhi 
#     if p.exists():
#         print("File alreay  exists")
#     else:
#         with open(file_name,'w') as file: ## file exist nhi  krti islie file create krenge 
#             content = input("Enter your  file content")
#             file.write(content)
#             print('File Added')
# print("Press 1 for creating a file")
# print("Press 2 for reading a file")
# print("Press 3 for updating a file")
# print("Press 4 for deleting a file")

# option = int(input("Enter your choice:"))
# if option == 1:
#     create__file()


##  for Read 

# from pathlib import Path
# def readfileandfolder():
#     p = Path('')
#     items = list(p.rglob('*'))  ## sari files lko list me store krane ke liye 
#     for index,file in enumerate(items):
#         print(f"{index +1}- (file)") 
# def create_file():
#     readfileandfolder()
#     file_name = input("Enter the file  name :")
#     p = Path(file_name)
#     if p.exists():
#         print("file  already exist")
#     else:
#         with open(file_name,'w') as file:
#             content = input("Enter your content")
#             print(file.write(content))
# def read_file():
#     readfileandfolder()
#     file_name = input("Enter your file name :")
#     p = Path(file_name)
#     if p.exists():
#         with open(file_name , 'r') as file:
#             print(file.read())
#     else:
#         print("File is not found")
# print("Press 1 for creating a file")
# print("Press 2 for reading a file")
# print("Press 3 for updating a file")
# print("Press 4 for deleting a file")

# option = int(input("Enter your choice:"))
# if option == 1:
#     create_file()
# if option == 2:
#     read_file()




### Exception Handling - 
# there are two block 
# try - pehle try krna he
# except - 


# from pathlib import Path
# def readfileandfolder():
#     try:
#         p = Path('')
#         items = list(p.rglob('*'))  ## sari files lko list me store krane ke liye 
#         for index,file in enumerate(items):
#             print(f"{index +1}- (file)") 
#     except Exception as e:
#         print(e)

# def create_file():
#     try:
#         readfileandfolder()
#         file_name = input("Enter the file  name :")
#         p = Path(file_name)
#         if p.exists():
#             print("file  already exist")
#         else:
#             with open(file_name,'w') as file:
#                 content = input("Enter your content")
#                 print(file.write(content))
#     except Exception as e2:
#         print(e2)
# def read_file():
#     try:
#         readfileandfolder()
#         file_name = input("Enter your file name :")
#         p = Path(file_name)
#         if p.exists():
#             with open(file_name , 'r') as file:
#                 print(file.read())
#         else:
#             print("File is not found")
#     except Exception as e3:
#         print(e3)
# print("Press 1 for creating a file")
# print("Press 2 for reading a file")
# print("Press 3 for updating a file")
# print("Press 4 for deleting a file")

# option = int(input("Enter your choice:"))
# if option == 1:
#     create_file()
# if option == 2:
#     read_file()




### For update 

# from pathlib import Path
# import os ## ye file ko delete krne ke liye
# def readfileandfolder():
#     p = Path('')
#     items = list(p.rglob('*'))  ## sari files lko list me store krane ke liye 
#     for index,file in enumerate(items):
#         print(f"{index +1}- (file)") 

# def create_file():
#     readfileandfolder()
#     file_name = input("Enter the file  name :")
#     p = Path(file_name)
#     if p.exists():
#         print("file  already exist")
#     else:
#         with open(file_name,'w') as file:
#             content = input("Enter your content")
#             print(file.write(content))

# def read_file():
#     readfileandfolder()
#     file_name = input("Enter your file name :")
#     p = Path(file_name)
#     if p.exists():
#         with open(file_name , 'r') as file:
#             print(file.read())
#     else:
#         print("File is not found")

# def update_file():
#     try:
#         readfileandfolder()
#         file_name = input("Enter the name of your file:")
#         p = Path(file_name)
#         if p.exists():
#             print("press 1 to overwrite the content")
#             print("press 2 to append the comtent")
#             option = int(input("Enter your choice:"))
#             if option == 1:
#                 with open(file_name,'w') as file:
#                     content = input("Enter your content")
#                     file.write(content)
#                     print("Content changed")
#             elif option == 2:
#                 with open(file_name,'a') as file:
#                     content = input("Enter the updated content")
#                     file.write(content)
#                     print("Done")
#             else:
#                 print("Invalid syntax")
#         else:
#             print("File does not exist")
#     except Exception as e:
#         print(e)


# def delete_file():
#     try:
#         readfileandfolder()
#         file_name = input("Enter the name of file")
#         p = Path(file_name)
#         if p.exists():
#             os.remove(p)  ## it is removing the path of file 
#             print("File deleted")
#         else:
#             print("File does not exist")
#     except Exception as e:
#         print(e)

# while True:

#     print("Press 1 for creating a file")
#     print("Press 2 for reading a file")
#     print("Press 3 for updating a file")
#     print("Press 4 for deleting a file")
#     print("Press 0 for existing...")

#     option = int(input("Enter your choice:"))
#     if option == 1:
#         create_file()
#     if option == 2:
#         read_file()
#     if option == 3:
#         update_file()
#     if option == 4:
#         delete_file()
#     if option == 0:
#         break



## for Renaming
from pathlib import Path
import os ## ye file ko delete krne ke liye
def readfileandfolder():
    p = Path('')
    items = list(p.rglob('*'))  ## sari files lko list me store krane ke liye 
    for index,file in enumerate(items):
        print(f"{index +1}- {file}") 

def create_file():
    readfileandfolder()
    file_name = input("Enter the file  name :")
    p = Path(file_name)
    if p.exists():
        print("file  already exist")
    else:
        with open(file_name,'w') as file:
            content = input("Enter your content")
            print(file.write(content))

def read_file():
    readfileandfolder()
    file_name = input("Enter your file name :")
    p = Path(file_name)
    if p.exists():
        with open(file_name , 'r') as file:
            print(file.read())
    else:
        print("File is not found")

def update_file():
    try:
        readfileandfolder()
        file_name = input("Enter the name of your file:")
        p = Path(file_name)
        if p.exists():
            print("press 1 to overwrite the content")
            print("press 2 to append the comtent")
            option = int(input("Enter your choice:"))
            if option == 1:
                with open(file_name,'w') as file:
                    content = input("Enter your content")
                    file.write(content)
                    print("Content changed")
            elif option == 2:
                with open(file_name,'a') as file:
                    content = input("Enter the updated content")
                    file.write(content)
                    print("Done")
            else:
                print("Invalid syntax")
        else:
            print("File does not exist")
    except Exception as e:
        print(e)


def delete_file():
    try:
        readfileandfolder()
        file_name = input("Enter the name of file")
        p = Path(file_name)
        if p.exists():
            os.remove(p)  ## it is removing the path of file 
            print("File deleted")
        else:
            print("File does not exist")
    except Exception as e:
        print(e)

def rename_file():
    try:
        readfileandfolder()
        file_name = input("Enter your file name:")
        p = Path(file_name)
        if p.exists():
            new_file = input("Enter new name of your file:-")
            p.rename(new_file)
            print("File renamed")
        else:
            print("File is not found")
    except Exception as e:
        print(e)

def create_folder():
    try:
        readfileandfolder()
        folder_name = input("Enter name of your folder:-")
        p = Path(folder_name)
        if p.exists():
            print("Folder already exsist")
        else:
            p.mkdir() ## jb exist nhi krega to create krenge
            print("Folder created")
    except Exception as e:
        print(e)


def delete_folder():
    try:
        readfileandfolder()
        folder_name = input("Enter your folder name :-")
        p = Path(folder_name)
        if p.exists():
            p.rmdir()
            print("Folder removed")
        else:
            print("Fplder is not found")
    except Exception as e:
        print(e)

            


while True:

    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("Press 3 for updating a file")
    print("Press 4 for deleting a file")
    print("Press 5 for renaming a file")
    print("Press 6 for creating a folder")
    print("Press 7 for deleting a folder")
    print("Press 8 for creating file in a folder")
    print("Press 0 for existing...")

    option = int(input("Enter your choice:"))
    if option == 1:
        create_file()
    if option == 2:
        read_file()
    if option == 3:
        update_file()
    if option == 4:
        delete_file()
    if option == 5:
        rename_file()   
    if option == 6:
        create_folder()
    if option == 7:
        delete_folder()
    if option == 0:
        break

