#readfile
with open("extra/read_file.txt", mode='r') as my_file:
    print(my_file.read())
with open("extra/read_file.txt", mode='r') as my_file:
    print(my_file.readlines())

'''
we can give absolute path
or related path (wrt to the current folder)
../ means go back one folder
./ menas start from current folder

pathlib module: for windows, linex paths are different, so we can use this module so that our code works in all machines.
'''