"""
**FROM LEETCODE** 
DONT SUE ME


Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

#REMAKE THIS FOR IT TO BE MORE CLEAR

# TC: O(n^2) approach
# SC: O(1)
# We used nested for loops. Say we have the list [1, 2, 3, 2]. Our outer loop denoted i starts at element 1, then we drop to the,
# inner for loop denoted by j. We always have to make sure that j is always an element ahead of our current element at i bc/ we do not
# want a duplicate to be the same number, the numbers must be distinct. So i is at 1, and j is at 2. j will iterate to the end of the list.
# We realize that their is no duplicate of 1 so i is incremented. Now i is 2 and j is 3. We begin iterating with j again to the end of the list,
# and we see that we find a match, we have a 2 at index i, and another 2 at index j, thus this list contains a duplicate. 

def containsDuplicate1(nums):
    for i in range(len(nums)):  #n
        for j in range(i + 1, len(nums)): #n
            if nums[i] == nums[j]:
                return True
    return False



#------------------------------------------------------------------------------------------------------------------------------------------------

#REMAKE THIS AS WELL

# TC: O(n) approach
# SC: O(n)

# We use a hashset data structure to keep track of list of elements. We iterate through our list of ints, we check if our hashset already
# contains the element of our current iteration. If it does not contain it, we add it to the hashset, if it does we return true and terminate
# algorithm. Example:

# list = [1, 2, 3, 2]       #HashSet = {1, 2, 3}  , when we reach index 3 of our list, we realize 2 is already contained in our hashet thus duplicate

def containsDuplicate2(nums):
    hashset = set()
    for n in nums:
        if n in hashset: return True
        hashset.add(n)
    return False



#------------------------------------------------------------------------------------------------------------------------------------------------









