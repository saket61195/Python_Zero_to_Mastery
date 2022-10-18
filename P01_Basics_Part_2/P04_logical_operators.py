#logical Operator
# and 	Returns True if both statements are true	
#       x < 5 and  x < 10	
# or	Returns True if one of the statements is true	
#       x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	
#       not(x < 5 and x < 10)	

is_megician = False
is_expert = False

if is_expert and is_megician:
    print("You are a Master magician")
elif is_megician and not is_expert:
    print("Atleast you're getting there")
elif not is_megician:
    print("you need magic power")