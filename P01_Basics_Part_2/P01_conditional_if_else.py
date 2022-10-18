#Conditional logic
a = True 
b = True #change true to false for output difference
if a and b:
    print("Both a and b are true")
elif a:
    print("Only a is true")
elif b:
    print("Only b is true")
else:
    print("Both a and b are false")


is_old = False
is_licenced = True #change true to false for output difference
if is_old and is_licenced:
    print('You are old enough to drive')
elif is_licenced:
    print("You can Drive Now!")
else:
    print('You are not of the age')
print("ok ok i don't care about your condition")