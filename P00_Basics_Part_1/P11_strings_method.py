#String Method
quote = "to be or not to be"
print(quote.capitalize())
# notice that the original message is unchanged, becuase strings are immutable
print(quote)
quote = quote.capitalize()
print(quote)
print(len(quote))  # len() is a function and not a string method
print(quote.upper())
print(quote.find("not"))
print(quote.replace("be", "me"))
