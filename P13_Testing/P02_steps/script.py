#step 3

#set default parameter
def do_stuff(num=0):
    try:
        if num:
            return int(num)+5
        else:
            return "please enter number"
    except ValueError as err:
        return err


print(do_stuff(4))