# complete path file we can run anywhere this from anywhere
my_file = open(
    '/home/saket/learning/python_programming/myowncode/P11_file_io/P01_test.txt')
# my_file = open('P01_test.txt')#terminal must be in that directory
print(my_file)
print(my_file.read())

print("\n#eg1")
print(my_file.read())  # not printing because cursor already reached to end

print("\n#eg2")
my_file.seek(0)  # cursor start from zero
print(my_file.read())

print("\n#eg3")
my_file.seek(5)  # cursor start from 5
print(my_file.read())

print("\n#eg4-> readline")
my_file.seek(0)
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())  # it will not print because cursor again at the end
print(my_file.readline())

print("\n#eg5-> readlines")
my_file.seek(0)
print(my_file.readlines())  # it print in a list
print(my_file.readlines())  # list is empty because cursor at the end

my_file.close()
