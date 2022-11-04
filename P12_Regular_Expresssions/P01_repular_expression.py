import re

string = 'search inside of this text please!'
a = re.search("this",string)
print("\n#eg0")
print(a)

# the below 4 commands will give error if the searching string does not exist.
print(a.span())
print(a.start())
print(a.end())
print(a.group())

string1 = 'search this inside of this text please!'

print("\n#eg1")
b = re.search("this",string1)
print(b.start())
print(b.end())

print("\n#eg2")
pattern = re.compile("this")
c = pattern.search(string1)
print(c)
k = pattern.findall(string1)
print(k)

print("\n#eg3")
pattern1 = re.compile("search this inside of this text please!")
d = pattern1.fullmatch(string1)
print(d)

print("\n#eg4")
pattern2 = re.compile("Hello search this inside of this text please?")
# this should be exact match, otherwise returns none
e = pattern2.fullmatch(string1)
print(e)

print("\n#eg5")
pattern3 = re.compile("inside of this")
# it starts matching from the first character otherwise returns none
f = pattern3.match("inside of this text")
print(f)
g = pattern3.match("inside of text")
print(g)
