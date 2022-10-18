# break
i = 0
while i < 5:
    print(i)
    i += 1
    if i==3:
        break
else:
    print("done")

print('\n')
# continue
for i in range(9):
    if i == 3:
        continue
    print(i, end=' ')

#pass
for x in [1, 3, 2]:
  pass


# 'continue' will skip the lines below it and continue to loop.
for i in range(0, 5):
    print(i)
    continue
    print("I will never be printed")

for i in range(10):
    # it can be used to avoid error and when we have not yet decided on the code to write.
    pass
