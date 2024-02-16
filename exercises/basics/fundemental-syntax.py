# 1. PRINT STATEMENT - display message on screen and console

# can also be done with single quotations, however single quotes should be used for short strings
# double quotes should be used for natural language messages
print("Hello World!")
print('Bob')



#-----------------------------------------------------------------------------------------------------------------------------------------------



# 2. F-STRINGS - the idea behind f-strings is to make string interpolation simpler
# string interpolation - Instead of writing seperate parts and then adding them in a string, we can intergrate values directly into the string

age = 22
print("Devin is " + str(age) + " years old") # NO STRING INTERPOLATION, it's not pretty as we had to cast our integer variable age to a string 

print(f"Devin is {age} years old") # WITH STRING INTERPOLATION



#-----------------------------------------------------------------------------------------------------------------------------------------------



# 3. CONDITIONALS - associated with boolean(T/F) type

a = 10
b = 20

result = a == b # is a equal to b? FALSE
result = a != b # a does not equal b? TRUE
result = a < b # a less than b? TRUE
result = a > b # a greater than b? FALSE



#-----------------------------------------------------------------------------------------------------------------------------------------------


# 4. AND OR STATEMENTS.

# AND -> and means that two conditions MUST BOTH BE TRUE. If only 1 of the two 2 conditions is false then the and statement is deemed false.
# OR -> or means only 1 of the 2 conditions must be true for the statement to be true

# sorry in advanced for those who suffered in discrete mathematics


#  p    q    p and q         p    q     p or q   
#  T    T       T            T    T        T
#  T    F       F            T    F        T
#  F    T       F            F    T        T
#  F    F       F            F    F        F

x = 5 + 5 and 7 + 3 # TRUE
x = 0 < 1 or 1 > 2  # FALSE



#-----------------------------------------------------------------------------------------------------------------------------------------------


# 4. Conditionals and If statements

a = 10
b = 20

#if true do this, if not try this, if not, do this no matter what bc/ it's the last statement
if a > b:
    print("a is larger than b")
elif b > a:
    print(f"b is larger than a")
else: print('equal')



#-----------------------------------------------------------------------------------------------------------------------------------------------



# 5. Regular For Loop - do multiple actions based on given iterations

#( starting number, ending number(exclusive), size of increment)

for i in range(6):  # print numbers 0 - 5. The number in the parameter is always exclusive when it's in this format
    print(i)

for i in range(2, 5): # print numbers 2 - 4. Recall only the ending number of our range is exclusive 
    print(i)

for i in range(0, 6, 2): #print numbers 0, 2, 4. The third number in our parameter of range (#, #, 2), is by how much i increments by on each iteration. 
    print(i)



#-----------------------------------------------------------------------------------------------------------------------------------------------



# 6. For Each Loops - same concept as a for loop, but we iterate through each element of our type
    
# for every letter x in john, print out x. The 
name = "john"
for x in name:
    print(name, end=' ') # j o h n | the end= keyword would keep all printed letters x on the same line

list = ["John", "Cena"]
for elements in list:
    print(elements) # bc/ were not using an end= statement, every time we print an element from our list, it will be on a seperate line
#John
#Cena
    


#-----------------------------------------------------------------------------------------------------------------------------------------------



# 7. While Loops - keep doing an action until a condition is no longer met.

# While loops must have a line of code that changes something in it's condition that will eventually lead to its termination.
# In this example, we subtract 1 from val until ultimately, it is no longer greater than 0. If we don't do this,
# Our program will keep running forever until eventually it gives up on us :(

val = 3
while val > 0:
    print(f"{val} > 0", end=', ')
    val -= 1 

# output:   3 > 0, 2 > 0, 1 > 0



#-----------------------------------------------------------------------------------------------------------------------------------------------
    


# 8. Lists - a group of items that can have the same or different type that have a label of their current position (indices)
# In fancy terms this is a data structure. Note in other programming languages, a list (or array) is restricted to one data type,
# however in python, you can have a list containing both strings, ints, chars,...etc.
# Indices - position where an element is in the list. LISTS ALWAYS START AT INDEX 0.
     
    
list_example1 = ["Devin", 10, 21.0]
#          0      1    2       <- indices of the elements

print(list_example1[0]) # retrieve and print, "the element in list at the index of 0"



#It's important not to confuse the length of a list and it's total indices.

list_example2 = [1, 2, 3, 4, 5] # list of size = 5
#                0  1  2  3  4  # total indices = 4

# The reason why is let's say we tried the following...
x = list_example2[5] # this would be an ArrayIndexOutOfBoundsException. Index 5 DOES NOT exist


#Important functions of a list.
list_example3 = [] #creating an empty list
list_example3.append(1) # append = add element to list
list_example3.append(2) # append = add element to list
list_example3.append(3) # append = add element to list
list_example3.append(4) # append = add element to list
#[1, 2, 3, 4]

list.remove(2) # removes element 2 from our list
#[1, 3, 4]

list.pop() # pops out the RIGHT-MOST element in our list
#[1, 3]

#insert at index 1 an element 2
list.insert(1, 2)
#[1, 2, 3]

# lists have many different functions. Remember, google and documentations are the friends you need for success



#-----------------------------------------------------------------------------------------------------------------------------------------------



# 9. Math review - PEMMDAS - Parentheses(), Exponents **, (Mod %, multiplication *, (order doesn't matter)), Division /, Addition +, Subtraction -

#Mod % - gives remainder if any after division
print(17 % 5) # = 2

#Exponents ** or pow() - we can do this manually or use a built in function
x = 2**3 # x would return 2^3 = 8

#pow(base number, exponent number, mod number)
x = pow(2, 3, 5) # (2^3) % 5 = 8 % 5 = 2

#PEMMDAS in action:
result = (4 * (2 + 3) ** 2 / 2 - 1 ) % 7 # = 0.0



#-----------------------------------------------------------------------------------------------------------------------------------------------



# 10. Functions - a way to avoid reusing code, and have an optimal solution for many different types of inputs

# define function called say_hello, that prints Hello! when called upon
def say_hello():
    print('Hello!')

say_hello() # calling our function, and will output: Hello!


#define a function greet_user, that takes an input in the parameter called name, and prints out Hello (person's name) ! 
def greet_user(name):
    print(f"Hello {name}!")

greet_user("devin") #calling our function greet_user, output: "Hello devin!"


#define a function called add, that takes 2 inputs in the parameter, and returns the sum of those numbers
def add(x, y):
    return x + y

print(add(2, 1)) # calling function add and printing it's output: 3


#define a void function that updates a boolean statement from false to true or vice versa
def boolUpdater(statement):
    if statement == True:
        statement = False
    
    else:
        statement = True

x = False
boolUpdater(x) 
# this would not return nor print out anything thus making it void, 
# but it will update our variable x which is now TRUE, after function call.


# When we have a RETURN statement in our function, we must use a print statement to view what were actually returning.
# If we have print statements within our function, there's no need to call our function in a print statement because,
# why we would we put a print statement within a print statement.
# If the parameter of a function is empty, you do not need to put anything in the arguments when you call the function
# A void function means, nothing is returned. Data is STILL being updated, but on termination of the function, no output will be given




#-----------------------------------------------------------------------------------------------------------------------------------------------








