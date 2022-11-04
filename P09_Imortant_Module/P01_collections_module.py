from collections import Counter,defaultdict,OrderedDict
#start with capital letter represent class
#start with small letter represent function
print("#eg1")
li = [1,2,3,4,5,6,7]
print(Counter(li)) 

print("\n#eg2")
li1 = [1,2,3,3,4,1,5,6,3,7]
print(Counter(li1)) 

print("\n#eg3")
sentence = 'blah blah thinking about python'
print(Counter(sentence))

print("\n#eg4")
print(int())
dictionary = defaultdict(int,{'a':1,'b':2})
print(dictionary['a'])
print(dictionary['c'])# print default value int

print("\n#eg5")
dictionary = defaultdict(lambda:'does not exit',{'a':1,'b':2})
print(dictionary['a'])
print(dictionary['c'])# print default value lambda