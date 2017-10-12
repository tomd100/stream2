

# def count_upper_case(message):
#     if not isinstance(message, str):
#         return 0
#     return sum([1 for c in message if c.isupper()])


# the way this works is that the list is passed to the sum function. 
# the for loop in the list is called the list comprehension. 

# def count_case(message):
#     return sum([2 for c in message if c.isupper()]) + sum([1 for c in message if c.islower()])

# def count_case(message):
#     return sum([int("12"[int(c.isupper())]) for c in message])
    
# def count_case(message):
    # return sum([int("12"[int( c  )]) for c in message])

# def count_case(message):
#     sum([int("125"[(index, row.index(val))[0]]) for index, row in enumerate(strs) if val in row])
#     return sum([int("12"[int( c  )]) for c in message])
        
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
str1 = list(alpha)
str2 = list(alpha.lower())
str3 = list(" ")

strs=[str1, str2, str3]

# print(any("a" in i for i in strs))

# print(strs)
val= " "
print(sum([int("125"[(index, row.index(val))[0]]) for index, row in enumerate(strs) if val in row]))



