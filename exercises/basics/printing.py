
# 1. print statement - display message on screen and console

# can also be done with single quotations, however single quotes should be used for short strings
# double quotes should be used for natural language messages
print("Hello World!")
print('Bob')




# 2. f-strings - the idea behind f-strings is to make string interpolation simpler
# string interpolation - Instead of writing seperate parts and then adding them in a string, we can intergrate values directly into the string

age = 22
print("Devin is " + str(age) + " years old") # NO STRING INTERPOLATION, it's not pretty as we had to cast our integer variable age to a string 

print(f"Devin is {age} years old") # WITH STRING INTERPOLATION



# 3. Conditionals - associated with boolean(T/F) type

a = 10
b = 20

result = a == b # is a equal to b? FALSE
result = a != b # a does not equal b? TRUE
result = a < b # a less than b? TRUE
result = a > b # a greater than b? FALSE




# 4. Conditionals and If statements

a = 10
b = 20

#if true do this, if not try this, if not, do this no matter what bc/ it's the last statement
if a > b:
    print("a is larger than b")
elif b > a:
    print(f"b is larger than a")
else: print('equal')


# 5. For Loops - do multiple actions based on given iterations

for i in range(6):  # print numbers 0 - 5. The number in the parameter is always inclusive when it's in this format
    print(i)

for i in range(2, 5): # print numbers 2 - 4. Recall only the ending number of our range is inclusive 
    print(i)

for i in range(0, 6, 2): #
    print(i)






















