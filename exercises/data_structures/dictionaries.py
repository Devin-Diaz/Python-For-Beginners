'''
A HashMap, known as a Dictionary in Python is a data structure that stores information called
values, and pairs them up with unique identifiers called keys. 

Some applications of dictionary's are the following:

**A Education Grading System:
The value would a student's ID, and associated with that specific ID, there is a coresponding value
that being that student's gpa.

VISUAL:

                    {key: student_id        value: GPA}
                        {38923                  4.0}
                        {58932                  3.3}

                        
**Countries and their capitals:
VISUAL:

                    {key: country        value: capital}
                        {Japan                 Tokyo}
                        {France                Paris}

                        
IMMUTABLE TYPES: int, float, bool, string, Unicode, and tuple. immutable
objects cannot be changed after it is created. 
                        

EMPHASIS ON KEYS: The type for your keys MUST BE IMMUTABLE. For example let's say I have the following.
--> {[1, 9], "devin"}
This would cause an ERROR bc/ a list is mutable. 

Now if we did something like this:
--> {tuple([1, 9]), "devin"} 
Now this would work because a tuple is immutable.


EMPHASIS ON VALUES: Values can be any object type. THEY CAN BE MUTABLE. For example we can have a dictionary
of a country and states within that country:

{"USA", ["Massachusettes", "Maine", "Delaware"]}


SPEED BENEFITS: HashMaps have can search for elements in O(1) constant time. This is a lot quicker
compared to arrays/linked-lists that have O(n) linear search time. 


Now let's get coding!
'''

#-----------------------------------------------------------------------------------------------------------------------------------

#two ways to create dictionary:
map = {}

#or
map = dict()

#KEYS MUST BE INITIALIZED FIRST BEFORE ASSINGING VALUES TO THEM IF NOT YOU WILL GET AN ERROR:


#-----------------------------------------------------------------------------------------------------------------------------------


#The following example is a dictionary for a person's name and age:
person_map = {}

#            {K        V}
person_map["Devin"] = 19
person_map["Bob"] = 21
person_map["Kunigami"] = 20


#to retrieve the values of a specific key we can do the following:
print(person_map["Devin"]) #--> 19

print(person_map) #{'Devin': 19, 'Bob': 21, 'Kunigami': 20}


#-----------------------------------------------------------------------------------------------------------------------------------


'''
Additional dictionary methods we can use:

    .keys() - will print out all current keys in our dictionary
    .values() - display all current vaues in dictionary
    .items() - returns all key-value pairs as a tuple.

'''

country_cities_map = dict()

us_cities = ["Boston", "New York", "Dorchester"]
country_cities_map["USA"] = us_cities

country_cities_map["SPAIN"] = []
country_cities_map["SPAIN"].append("Madrid")

print(country_cities_map.keys())     # --> dict_keys(['USA', 'SPAIN'])
print(country_cities_map.values())   # --> dict_values([['Boston', 'New York', 'Dorchester'], ['Madrid']])
print(country_cities_map.items())    # --> dict_items([('USA', ['Boston', 'New York', 'Dorchester']), ('SPAIN', ['Madrid'])])

print(country_cities_map)            # --> {'USA': ['Boston', 'New York', 'Dorchester'], 'SPAIN': ['Madrid']}


#-----------------------------------------------------------------------------------------------------------------------------------

'''

Congrats! You have now learned about maps/dictionaries in python. Keep rising!

'''