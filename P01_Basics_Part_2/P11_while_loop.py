#While Loop
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("done")

#While with break
i = 0
while i < 5:
    print(i)
    i += 1
    break
else:
    print("done")
    
#Infinte Loop
while True:
    response = input("say something: ")
    if (response == 'bye'):
        break
