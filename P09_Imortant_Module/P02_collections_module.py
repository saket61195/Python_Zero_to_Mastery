from collections import Counter,defaultdict,OrderedDict

print("#eg1")
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2
d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d1==d2)


print("#eg2")
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2
d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1==d2)

print("#eg3")
d1 = {'c':100}
d1['a'] = 1
d1['b'] = 2
d2 = {'c':100}
d2['b'] = 2
d2['a'] = 1

print(d1==d2)
