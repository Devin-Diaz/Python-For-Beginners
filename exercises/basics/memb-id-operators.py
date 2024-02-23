'''

Certain programming tasks require certain operators when performed using sequences.
We will now introduce the idea of membership and identity operators and when they are most useful.
'''

#--------------------------------------------------------------------------------------------------

#One of these tasks involves determining whether a value can be found inside a container
    #For this we will use the following membership operators, the in and not in operators
        #These operators yield True or False depending on the statement. 
#Ex:

prices = [15, 10, 5, 20]

print(15 in prices) # True
print(20 not in prices) # False

#---------------------------------------------------------------------------------------------------

#Example using in to check if a name is on a roster.

employee_roster = ["Kevin", "Martha", "Melissa", "Sage", "Johnathon"]

def check_roster():
    name = input("Who are you: ")
    if name in employee_roster:
        print(f"{name}, welcome back.")
    else: 
        print(f"You are not on the current employee roster.")

check_roster() 

    #Will print "name" welcome back if inputted name is found in employee_roster
    #Note no need to use an elif not in statement
        
#----------------------------------------------------------------------------------------------------

#Example using not in to ensure uniqueness when creating a list, such as players choosing jersey numbers

list_numbers = [1, 2, 3, 4, 5]

def add_number():
    number = input("What number would you like?: ")
    if number not in list_numbers:
        print(f"Congratulations! {number} is your number!")
    else: 
        print("Sorry, that number is already taken.")

add_number()

#-----------------------------------------------------------------------------------------------------
        
#Another common task involves determining whether two variables are the same object
    #For this we will use the identity operators is and is not 
        #These operators like their membership counterparts yield True and False
#Ex. 

w = 500
x = 500 + 500
y = w + w
z = x

print(z is x) # True
print(z is not y) # True

#------------------------------------------------------------------------------------------------------