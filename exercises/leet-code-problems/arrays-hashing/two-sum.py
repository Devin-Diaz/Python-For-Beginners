'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

'''

#-------------------------------------------------------------------------------------------------------------------------------------------------

# BRUTE FORCE APPROACH:

'''
For this approach we will use nested for loops. Say we have the following test case.
We will use variables i and j for our loops.

[2, 7, 11, 15]    target = 12
 0  1   2   3

As we traverse through our array, we will evaluate whether or not the element at indices i and j add up to our target element.
Note that j = i + 1, bc/ we don't want to add the same element. We want to have two distinct numbers that add to our target sum.

1.
        2, 7, 5, 15
        i  j

        we check 2 + 7 = 9 NOT 12
2.

        2, 7, 5, 15
        i     j

        we check 2 + 5 = 7 NOT 12

3.

        2, 7, 5, 15
        i        j

        we check 2 + 15 = 17 NOT 12

4.        

        We reached the end in our nested loop so now we increment our outer loop w variable i by 1,
        and set up our j pointer according to i
        
        2, 7, 5, 15
           i  j


        
5.

        2, 7, 5, 15
           i  j
        
        we check 7 + 5 = 12. WE REACHED OUR ELEMENT.

6.

Now we retrieve the indices of elements 7 and 5 that add up to our TARGET ELEMENT:

0  1  2  3    ==> [1, 2] OUR FINAL ANSWER  
2, 7, 5, 15
   i  j

'''


#CODE: TC: O(N^2) SC: O(1)

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []

#-------------------------------------------------------------------------------------------------------------------------------------------------


#OPTIMAL APPROACH (DICTIONARY)
'''
This appraoch requires to take the complement of each element we come across while iterating thorugh our input array.
We find the complement by doing TARGET NUMBER - CURRENT NUMBER. 

In our dictionary we will be storing the original element as we iterate through our array. 

If we have a valid two sum,

We will find the complement stored in our dictionary indicating that the current number on the iteration and the complement number
in our dictionary is the two elements that add up to our TARGET NUMBER. We retrieve the indice of the current element, and we use
the value of the complement from the dictionary for the other indice for our final answer. 

This is a bit confusing so let the visual do the magic:


VISUAL:

dict = {}

TEST CASE: 
[2, 7,  5, 15]    TARGET = 12
 0  1   2   3

 
 0. 
        complement = 12    -     2      = 10
                   TARGET  -   CURRENT

        we check if element 10 exists as a KEY in our dictionary

        dict = {}   it's empty so nothing happens

        we add CURRENT to our dictionary with it's corresponding indice
        
        dict = {   2   :  0  }
               element : index

        
1.
        complement = 12    -     7      = 3
                   TARGET  -   CURRENT

        we check if element 3 exists as a KEY in our dictionary
                
                K : V
        dict = {2 : 0}    3 DOES NOT EXIST, so we continue

        we add CURRENT to our dictionary with it's corresponding indice
        
        dict = {2 : 0, 7 : 1}


2. 
        complement = 12    -     5      = 7
                   TARGET  -   CURRENT

        we check if element 7 exists as a KEY in our dictionary

        dict = {2 : 0, 7 : 1}    7 DOES EXIST, WE FOUND OUR 2 ELEMENTS THAT ADD TO TARGET

FINAL.

        We retrieve the indice of 5 which was our current element that being indice 2.
        We retrieve the indice of 7 via it's value in the dictionary that being 1.

        Thus our final answer is [1, 2]

'''

#CODE: TC: O(N)    SC: O(N)

def two_sum(nums, target):
    
    dict = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in dict:
            return [dict[complement], i]
        
        dict[complement] = i

    return []

#-------------------------------------------------------------------------------------------------------------------------------------------------



