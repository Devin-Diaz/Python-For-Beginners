'''

A list in python is a collection of items which are ordered and mutable.
It allows duplicate elements and can hold a variety of object types. 
A list an python is essentially the same as an ArrayList from other programming
languages like Java.
'''

#-----------------------------------------------------------------------------------------

#syntax: name_of_list = [elements stored]

#Creating a list:
name_of_list = [1, 2, 3]

#-----------------------------------------------------------------------------------------

#With lists we can check the index of an element. The index of an element is
#the current position of the element. INDICES ALWAYS START AT 0. For example.

fruits = ['apple', 'banana', 'blueberries']    # elements 
#            0         1           2           # indices

#We can target elements if we pass in their indice with the following syntax
fruits[0]  # -> apple
fruits[2]  # -> blueberries

#--------------------------------------------------------------------------------------------------

#What's unique about lists in python is you can have different types in the same list
diff_elements = ['word', 7, "expression", 6.30, True]

#------------------------------------------------------------------------------------------------

'''
Lists come with a variety of different functions to be able to manipulate a list to our needs.
'''

#---------------------------------------------------------------------------------------------------

#append() - this is used to add elements to our list. We put the value we want to add to the list in
#the argument of the append method. This will add them to the right hand side. 

#append(element arg)

list = []

list.append(4)  # [4]
list.append(7)  # [4, 7]

#------------------------------------------------------------------------------------------------------

#remove() - this will remove an element from our list given that exists in the list or it will return a
#value error exception.

#remove(element arg)

list.remove(4)   # [7]

#-------------------------------------------------------------------------------------------------------

#copy() - this function copies a current array you have made.
original_list = [1, 2, 3, 4]
copy_list = list.copy()  # [1, 2, 3, 4]
# you can know manipulate copy_list and it won't affect original_list

#-----------------------------------------------------------------------------------------------------

#count() - this function counts how many of a specific elements is contained in the list.
#in the argument of the count function, you'd pass the element you want to find the count of.

#count(element arg)

nums = [1, 2, 4, 2, 2, 4, 6, 7, 4]
print(nums.count(2)) # the number 2 is found 3 times in the list nums 

#-----------------------------------------------------------------------------------------------------

#extend() - this function extends a current list with another list. In the parameter of extend, we add
#another list, and this list will get jointed together with the original list and become one big list.

#extend(list arg)

drinks = ['water', 'juice', 'milk']
carbonated_drinks = ['soda', 'celsius', "sparkling water"]
drinks.extend(carbonated_drinks)
print(drinks) # [water, juice, milk, soda, celsius, sparkling water]

#-------------------------------------------------------------------------------------------------------------

#index() - takes an input of an element in your list, and given that it exists in the list, it will return the
#index of that element you put in the argument of the method.

#index(integer arg)

names = ['devin', 'john', 'bob', 'shawn']
#           0        1      2       3

print(names.index("bob"))  # would return 2 for index 2
#if you're wondering using the "" for a element stored with '' doesn't matter, it'll recognize it as a string

#-------------------------------------------------------------------------------------------------------------

#insert() - very similar to the append() method, however with insert(), we can choose what position we want to
#store this element in our list. With append, we were directly adding it to the end of our list 
#now we can choose where, note that were not replacing an element if an element already exists in that position,
#the old element will shift left, or if it's the first element in the list it will shift right to make space,
#for the new element being inserted. 

#insert(integer arg, element arg)

cars = ['bmw', 'nissan', 'bugatti']
cars.insert(0, 'toyota')
print(cars) # -> [toyota, bmw, nissan, bugatti]
#                   0      1      2       3

cars.insert(2, 'mercedes')
print(cars) # -> [toyota, bmw, mercedes, nissan, buggati]
#                   0      1       2        3       4

#-------------------------------------------------------------------------------------------------------------

#pop() - can be used to remove an element at a specific position, or if used without an argument, it will
#remove the last element in the list. If you print the statement where you pop an element, it will return
#the element you popped

#pop(integer arg) or pop()

list = [4, 2, 4, 6, 8]
print(list.pop()) # -> 8
print(list) # -> [4, 2, 4, 6] 


fruits = ['banana', 'apple', 'cherry']
#             0        1         2
fruits.pop(1)
print(fruits) # -> [banana, cherry]

#-------------------------------------------------------------------------------------------------------------

#reverse() - reverses the elements of a list. This doesn't take any arguments. If you try printing the 
#statement with the reverse statement, it will return None 

numbers = [1, 2, 3]
numbers.reverse() 
print(numbers) # -> [3, 2, 1]

words = ['hello', 'devin', 'zebra']
words.reverse()
print(words) # -> [zebra, devin, hello]

#-------------------------------------------------------------------------------------------------------------

#sort() - sorts the elements in a list in ascending order. sort() doesn't take any arguments.

numbers = [4, 1, 7, 2]
numbers.sort() 
print(numbers) # -> [1, 2, 4, 7]

words = ['zebra', 'devin', 'claire', 'johnson']
words.sort()
print(words) # -> [claire, devin, johnson, zebra]

#-------------------------------------------------------------------------------------------------------------

'''
SPLICING A LIST:

splicing is a feature that allows you to access modify,
or extract elements from a list (or array) using a range
of indices. Hereare some of the following features:

Extracting a range of elements
Modifying elements in a given range
Delete elements in a given range
Step value splicing.

Our start index is INCLUSIVE and the end index is EXCLUSIVE.
Think of the colon notation as 'to'. 

EXAMPLE:  [5 : 7] <==> index 5 inclusive to index 7 exclusive

'''
#-------------------------------------------------------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8]   #elements
#          0  1  2  3  4  5  6  7    #indices

#extracting a range starting from index 2 to index 4
subset = numbers[2 : 5]
print(subset) # -> [3, 4, 5] elements


#deleting elements from index 0 to index 3
del numbers[0 : 4]
print(numbers) # -> [5, 6, 7, 8] elements

#deleting elements from index 0 to index 3 (alternative). That range we want to delete we replace w empty list
numbers[0 : 4] = []
print(numbers) # -> [5, 6, 7, 8] elements


#step value [start index (inclusive) : end index (exclusive) : increment #]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]   #elements
#          0  1  2  3  4  5  6  7    #indices

#iterate through list from index 0 to index 8, but we are going up 2 indices at a time. 
print(numbers[0 : 8 : 2]) # -> [0, 3, 5, 7] elements


#-----------------------------------------------------------------------------------------------------------------------









