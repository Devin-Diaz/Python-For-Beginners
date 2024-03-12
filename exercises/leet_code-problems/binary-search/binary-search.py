'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

'''

# VISUAL AND EXPLANATION:

'''
Binary search is a searching algorithm for ordered collections. With this searching algorithm, we always start in the middle of our
collection to search for our target element. If we don't find our element in the middle on the first iteration, we determine whether
our current element is less than or greater than our target element. This will tell us how to adjust our array and limit our searching
space. Essentially we are going to be making sub arrays and keep splitting them in half until eventually we reach our target element. 


Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4


L = low, M = mid, H = high

1. First iteration:

low = 0
high = 5

mid = 0 + (5 - 0) / 2 = 2

                                          L       M            H        
                                        [-1 , 0 , 3 , 5 , 9 , 12]
                                          0   1   2   3   4    5

                                          
Our mid element is 3. Our target element is 9. We see that 3 is less than 9, so that portion of the array between L and M gets shrinked,
and now our new L would be at index 3 at element 5.



2. Second iteration:

low = 3
high = 5

mid = 3 + (5 - 3) / 2 = 4

                                                      L   M    H                      
                                        [-1 , 0 , 3 , 5 , 9 , 12]
                                          0   1   2   3   4    5

With our new mid calculated, we reach index 4 which is element 9. We've reached a conclusion, we have found our target element in
our sorted collection.

3. Conclusion:

We reached our target element 9, so we return its indice that being 4.



Math background:

The reason why we have a time complexity of O(log N) is bc/ we are always going to the middle index in each of our sub arrays.
Take the example we just did, we had 2 iterations to reach our target element.

log base 2 of (6) is roughly between 2 and 3. 

6 is the size of our list, and the answer of our log statement is the amount of iterations it took us to search for the element.

Thus O(log N) time complexity.

'''







# CODE: TC: O(log N)   SC: O(1)

def binary_search(target, nums):
    low = 0
    high = 0

    while low <= high:
        mid = low + (high - low) / 2

        if nums[mid] < target:
            low = mid + 1
        
        elif nums[mid] > target:
            high = mid - 1
        
        else:
            return mid
    
    return -1



