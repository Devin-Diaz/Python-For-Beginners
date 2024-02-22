'''

A set is an unordered collection of unique elements. A set has the following properties
Elements are unordered with no position or index
Elements are unique, no elements in the set share the same value
Sets are mutable:
    Set elements themselves are immutable 
'''

#----------------------------------------------------------------------------------------------

#Because sets are unordered, we are not able to check the index of an element. 
    #For example:
list1 = [6, 7, 8, 9]
set1 = set(list1)

set1[0] # will produce a runtime error

#----------------------------------------------------------------------------------------------

#syntax: set(elements stored)

#Creating a set: 
set([4, 5, 6, 7]) # {4, 5, 6, 7}

#or 

set_ex = {4, 5, 6, 7} # {4, 5, 6, 7}

#----------------------------------------------------------------------------------------------

#Removing duplicate items from lists by passing them through set()

list_example = [55, 6, 17, 18, 17, 55]
list_names = ["Anthony", "Joseph", "James", "Robert", "Joseph"]

print(set(list_example)) # {55, 6, 17, 18}
print(set(list_names)) # {"Anthony", "Joseph", "James", "Robert"}

#----------------------------------------------------------------------------------------------

#Like lists sets are mutable and elements can be added or removed

#We will now go over some very useful set methods.

#All of the below examples of applying the methods will use the following sets

example_set1 = set([5, 6, 7, 8, 9])
example_set2 = set([1, 2, 3, 4, 5])
example_set3 = set(["House", "Apartment", "Condo", "Duplex"])

#----------------------------------------------------------------------------------------------

# len(set) - returns the length of the set
#Ex. 

len(example_set1) # 5
len(example_set2) # 5
len(example_set3) # 4

#----------------------------------------------------------------------------------------------

# set1.update(set2)- adds the elements of set2 to set 1
#Ex. 

example_set1.update(example_set2) # {5, 6, 7, 8, 9, 1, 2, 3, 4}

#Note 5 is not added as sets can only contain unique elements

#----------------------------------------------------------------------------------------------

# set.add(value) - adds value to the set
#Ex. 

example_set1.add(19) # {5, 6, 7, 8, 9, 19}
example_set3.add("Vacation Home") # {"House", "Apartment", "Condo", "Duplex", "Vacation Home"}

#Note sets are unordered and placement of elements does not matter

#-----------------------------------------------------------------------------------------------

# set.remove(value) - removes value to the set

example_set1.remove(7) # {5, 6, 8, 9}
example_set2.remove(1) # {2, 3, 4, 5}
example_set3.remove(6) # KeyError as value is not found

#-----------------------------------------------------------------------------------------------

#Other useful methods

# set.pop() - removes a random element from the set
# set.clear() - clears all elements from a set

#-----------------------------------------------------------------------------------------------

#Python set objects support typical set theory operations such as intersections and unions

#We will now go over a few common set operations supported in Python

#We will be using the same sets as before

example_set1 = set([5, 6, 7, 8, 9])
example_set2 = set([1, 2, 3, 4, 5])
example_set3 = set(["House", "Apartment", "Condo", "Duplex"])

#------------------------------------------------------------------------------------------------

# set.intersection(set_a, set_b, set_c, ...) returns a new set containing the elements in common
#Ex. 

example_set1.intersection(example_set2) # {5}

#------------------------------------------------------------------------------------------------

# set.union(set_a, set_b, set_v, ...) returns a new set containing unique elements in all sets
#Ex.

example_set1.union(example_set2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

#------------------------------------------------------------------------------------------------

# set.difference(set_a, set_b, ...) - returns a new set containing only elements in set not found 
                                    # in the given sets 
#Ex.

example_set1.difference(example_set2) # {6, 7, 8, 9}

#------------------------------------------------------------------------------------------------

# set_a.symmetric_difference(set_b) - returns a set of elements that appear in exactly one set

example_set1.symmetric_difference(example_set2) # {6, 7, 8, 9, 1, 2, 3, 4}