#writing
# with open("extra/write_file.txt", mode='w') as my_file:
#     my_file.write("hey there i am writig somting!")


#writing and reading
# with open("extra/write_file.txt", mode='r+') as my_file:
#     my_file.write("hey there i am writig somting!")
#     print(my_file.readlines())

#writing and reading
with open("extra/write_file.txt", mode='r+') as my_file:
    # text = my_file.write("0hey there i am writig somting!")
    text = my_file.write("opos")
    print(text)#it will print number of character wrote in the file
