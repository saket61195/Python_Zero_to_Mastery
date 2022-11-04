# try:
#     with open("extra/temp.txt", mode='r') as my_file:
#         my_file.write("cool")
# except FileNotFoundError as err:
#     print("file not found")
#     raise err

#IO error
try:
    with open("extra/temoop.txt", mode='r') as my_file:
        my_file.write("cool")
except IOError as err:
    print("IO error")
    raise err

