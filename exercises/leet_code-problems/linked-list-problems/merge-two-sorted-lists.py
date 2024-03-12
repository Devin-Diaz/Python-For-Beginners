''''
LEETCODE 21: MERGE TWO SORTED LINKED LISTS


You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by 
splicing together the nodes of  the first two lists. Return the head of 
the merged linked list.

EXAMPLE 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]


EXAMPLE 2:

Input: list1 = [], list2 = []
Output: []


Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

'''

#VISUAL AND EXPLANATION:

'''
For this explanation we will use the following test case:

Input: list1 = [1, 3], list2 = [2, 4]
Output: [1, 2, 3, 4]


1. 
    To start this process, we will create a new node, this can be called anything. The reason we do this 
    is because if we were to start our output linked list with either list1 or list2, things would get 
    messy really fast. So we start fresh with a random node that act as our starter point. Later on we will
    return the next pointer as our head for output. We will denote our starter node as starter

       starter
    ( random num )

    Now we another node starting object called curr so we can traverse through our starting point. 


              starter
    curr = ( random num )


2. 
    now we begin iterating through our list1 and list2, reading in plain English, we do
    "while list1 and list2 is not None"

    We now have 2 conditions that check whether the element in list1 is less than element at list2
    or vice versa in our second condition.

    
3. 
              *                             *
    list1 = ( 1 ) --> ( 3 )       list2 = ( 2 ) --> ( 4 )

    our first node in list1 is less than the node at list2 with value of 3. Therefore we do the following
    operations:

    we set the next pointer of our random number


            curr
    ( random number ) --> ( 1 ) 

    
    we update the list we adjusted, in this case list1

                        *
    list1 = ( 1 ) --> ( 3 )

    now we update our curr pointer for our is to be output list

                           curr
    ( random number ) --> ( 1 ) 


4. 
                        *                   *
    list1 = ( 1 ) --> ( 3 )       list2 = ( 2 ) --> ( 4 )

    In our next iteration, we compare nodes with the values 3 and 2. 2 is less therefore we use the node at
    list2 to keep building off our is to be output list.

                           curr
    ( random number ) --> ( 1 ) --> ( 2 )

    Now we update our list2 since we used a node from it,

                        *
    list2 = ( 2 ) --> ( 4 )

    we update our curr variable

                                    curr
    ( random number ) --> ( 1 ) --> ( 2 )


    
5. 
                        *                                      *
    list1 = ( 1 ) --> ( 3 ) --> None       list2 = ( 2 ) --> ( 4 ) --> None


    value 3 is less than 4, so we set our curr next pointer to that node, 


                                    curr
    ( random number ) --> ( 1 ) --> ( 2 ) --> ( 3 )

    we do our updates to list and our is to be output list

                                  *
    list1 = ( 1 ) --> ( 3 ) --> None

    We update our curr variable

                                              curr
    ( random number ) --> ( 1 ) --> ( 2 ) --> ( 3 )


6. 
    We've reached None for one of our lists. We break out of our while statement and reach our last 2 conditions.

7. 
    We check which list isn't at None yet, in this case our list2 hasn't reached None yet, so all we do is
    append the remainder of list2 to the end because it's already implied that any remaining nodes are greater
    than what we already have in our is to be output linked list.

    list2 = ( 2 ) -->  | ( 4 ) --> None |  this is the remaining portion that will be added to our output list

                                              curr
    ( random number ) --> ( 1 ) --> ( 2 ) --> ( 3 ) --> ( 4 ) --> None

8. 
    As we can see we merged our 2 linked list into one in order. However that ( random number ) node is
    still at the head of the list. We don't want this because it's irrelevant to our problem. All we have
    to do is return the next reference of our head because the next node is where our ordered merged linklist
    begins. So our output ends up being

    ( 1 ) --> ( 2 ) --> ( 3 ) --> ( 4 ) --> None

    We've arrived at our answer
'''
from data_structures.singly_linked_list import Node




#CODE:   TC: O(N)    SC: O(1)

def mergeSortedList(list1, list2):

    starter_node = Node(1)
    curr = starter_node

    while list1 and list2 is not None:
        
        if list1.data < list.data:
            curr.next = list1
            list1 = list1.next

        else:
            curr.next = list2
            list2 = list2.next
        
        curr = curr.next
    
    if list1 is not None:
        curr.next = list1
    
    if list2 is not None:
        curr.next = list2
    
    return starter_node.next


