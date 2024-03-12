'''
LEETCODE 739: DAILY TEMPERATURES

Given an array of integers temperatures represents the daily temperatures, return an array answer 
such that answer[i] is the number of  days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

'''

#VISUAL AND EXPLANATION:
'''
THIS SOLUTION IS TRICKY MAKE SURE TO STUDY OVER AND OVER. Lets begin:

For each element (weather) we need to find how many days, until we find another element (weather) that is greater
than our current weather. If we cannot find another day higher, the element for our output list will be 0
since there wasn't any days until we found a greater weather. 


We will use the case
Input: temperatures = [73,74,75,71,69,72,76,73]
                        0  1  2  3  4  5  6  7


1.  element = 73, i = 0, stack index = empty

    We begin iterating through our for loop, we check that our created stack is empty AND our current element
    is greater than the element based off the index in our stack.

    In this case our stack is empty, so we push i which denotes the current index of element 73 
    that being 0 into our stack

    |     |
    |     |
    |  0  |
    |_____|

2. element 74, i = 1, stack index = 0

    Our stack is not empty.
    Our current element is 74
    and in our stack we have index 0, so we use that to verify for previous element temps[0] = 73

    74 > 73 so we pop that index and use the following formula to calculate the indices (days) until
    we find a day with higher weather than the previous.


    |     |
    |     |
    |  0  |  <---- POP()
    |_____|

    output[stack index] = i - index 
    output[0] = 1 - 0 = 1

    output = [1, 0, 0, 0, 0, 0, 0, 0]
              0  1  2  3  4  5  6  7

              
    We push our current i denoting the index of element 74
              
    |     |
    |     |
    |  1  |  <--- PUSH()
    |_____|

    

3. element 75, i = 2, stack index = 1

    current element is 75, the element based off the index in our stack temps[2] = 74

    75 > 74, so we repeat the process

    |     |
    |     |
    |  1  |  <--- POP()
    |_____|

    output[stack index] = i - stack index
    output[1] = 2 - 1

     output = [1, 1, 0, 0, 0, 0, 0, 0]
               0  1  2  3  4  5  6  7


    Push i which denotes index of current element

    |     |
    |     |
    |  2  |  <--- PUSH()
    |_____|


4. element 71, i = 3, stack index = 2

    current element is 71, element with the index of our stack temps[2] = 75

    71 IS NOT GREATER THAN 75

    We don't do anything other then push i denoting our current element into the stack


    |     |
    |  3  |  <--- PUSH()
    |  2  |  
    |_____|

    

5. element 69, i = 4, stack index = 3

    current element is 69, we check our top most index in the stack for our prev element temps[3] = 71

    69 IS NOT GREATER THAN 71

    We don't do anything besides push i

    |  4  |  <--- PUSH()
    |  3  |  
    |  2  |  
    |_____|

    
6. element 72, i = 5, stack index = 4

    current element is 72, stack index element is temps[4] = 69.

    72 IS GREATER THAN 69 so we use our formula. We pop our current stack index


    |  4  |  <--- POP()
    |  3  |  
    |  2  |  
    |_____| 

    output[stack index] = i - stack index
    output[4] = 5 - 4 = 1

     output = [1, 1, 0, 0, 1, 0, 0, 0]
               0  1  2  3  4  5  6  7

    
    |     |  
    |  3  |  
    |  2  |  
    |_____|

    However this step isn't done, in our code this will be a while condition so now we check for our current
    element that being 72 still, but we check it with our NEW STACK INDEX OF --> 3   i is still = 5


    
    current element is 72, stack index element temps[3] = 71
    72 IS GREATER THAN 71

    We pop our top most index from the stack

    |     |  
    |  3  |  <--- POP()
    |  2  |  
    |_____|

    output[stack index] = i - stack index
    output[3] = 5 - 3 = 2

     output = [1, 1, 0, 2, 1, 0, 0, 0]
               0  1  2  3  4  5  6  7

    
    |     |  
    |     |  
    |  2  |  
    |_____|

    

    our current element that being 72 still, but we check it with our 
    NEW STACK INDEX OF --> 2   i is still = 5

    current element 72, stack index element is 75.

    72 IS NOT GREATER THAN 75
    We push i into our stack

    |     |  
    |  5  |  <--- PUSH() 
    |  2  |  
    |_____|



            
7. element 76, i = 6, stack index = 5

    current element = 76, stack index element = temps[5] = 72

    76 IS GREATER THAN 72
    POP top most element per usual 

    |     |  
    |  5  |  <--- POP() 
    |  2  |  
    |_____|


    output[5] = 6 - 5 = 1

     output = [1, 1, 0, 2, 1, 1, 0, 0]
               0  1  2  3  4  5  6  7

    |     |  
    |     |  
    |  2  |  
    |_____|

               
    We aren't done yet with this iteration.

    current element is 76, i = 6, new stack element is temps[2] = 75

    76 IS GREATER THAN 75

    |     |  
    |     |  
    |  2  |  <--- POP()
    |_____|

    output[2] = 6 - 2 = 4

    
     output = [1, 1, 4, 2, 1, 1, 0, 0]
               0  1  2  3  4  5  6  7
    

    We push our current i to the stack

    |     |  
    |     |  
    |  6  |  <--- PUSH()
    |_____|

    

8. element 73, i = 7, stack index = 6

    73 IS NOT GREATER THAN temps[6] = 76

    |     |  
    |  7  |  <--- PUSH()
    |  6  |  <--- PUSH()
    |_____|
    
9. 
    We've arrived at the end of our input list. Our final output comes to 

    output = [1, 1, 4, 2, 1, 1, 0, 0]  
               0  1  2  3  4  5  6  7

    nice!

'''

# CODE: TC: O(N)  SC: O(N)


def dailyTemps(temps):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
     
    stack = []
    output = [0] * len(temps)

    for i in range(len(temps)):
        while len(stack) != 0 and temps[i] > temps[stack[-1]]:
            index = stack.pop()
            output[index] = i - index
        
        stack.append(i)
    
    return output






          
    








