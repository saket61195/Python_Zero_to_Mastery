#Short Circiting
is_Friend = False
is_User = True
print('or')
if is_Friend or is_User:
    print('best friend forever')
else:
    print('not best friend')

print('\nand')
if is_Friend and is_User:
    print('best friend forever')
else:
    print('not best friend')

print("\nshort circuit")    
if True and is_User:
    print('best friend forever')
else:
    print('not best friend')


print("\nshort circuit")    
if False and is_User:
    print('best friend forever')
else:
    print('not best friend')

