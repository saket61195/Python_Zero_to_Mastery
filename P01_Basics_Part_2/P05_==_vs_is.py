print('\n==')
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

# is keywword  if both value located at the same memory location on that case the result will be true
print('\nis keyword')
print(True is 1)
print('' is 1)
print('1' is '1')
print([] is 1)
print(10 is 10.0)
print([] is []) #two differnent list located with same name located at differnt place in memory
a = [1,2,3]
b = [1,2,3]
print(a is b)
print(a is a)
print(a == b)