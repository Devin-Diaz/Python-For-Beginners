'''
LEETCODE 206: REVERSING LINKED LIST

Given the head of a singly linked list, reverse the list, and return the reversed list.


EXAMPLE 1:

Input:  1 --> 2 --> 3 --> 4 
Output: 4 <-- 3 <-- 2 <-- 1

EXAMPLE 2:

Input:  1 --> 2
Output: 2 <-- 1


EXAMPLE 3:

Input:  []
Output: []

'''


#ITERATIVE APPRAOCH:

'''
VISUAL / EXPLANATION

In majority of LinkedLists problems, we are given a head of a LinkedList so we can begin to traverse through the 
nodes of the LinkedList. To start this problem we will create 2 nodes.

For this visual we will use the following test case:

INPUT:  1 --> 2 --> 3
OUTPUT: 3 <-- 2 <-- 1

                         data   next
I'll denote nodes with   ( )    -->


0. 
    First node were gonna call prev and set it equal to None.
    prev = None

    prev will eventually end up as the head for our reverse linked list.

    Second node we will create will call curr and this is going to be set to the head of our input linked list
    curr = head

    curr = ( 1 ) --> 

    
1. 
    Now we will begin iterating through our LinkedList through curr. So in plain english,
    "While the node at curr does not equal None"

    
2. 
    Within our while loop, we will save the pointer reference of our current element. So in our current
    iteration,

     curr   next  = (SAVING THIS FOR LATER)
    ( 1 )   ---->   ( 2 ) --> ( 3 ) ---> None

            We are going to save that pointer arrow that leads gives us the data of ( 2 )
            This may seem confusing but keep reading,
    
                
    After we have that pointer reference saved, we will point that very same arrow to that other node we
    created in STEP 0. So our new visual would look like

    prev        curr
    None  <---  ( 1 )   ( 2 ) ---> ( 3 ) ---> None

    Note that we broke that pointer reference connection from the Nodes ( 1 ) and ( 2 ). As we traverse through
    the other nodes we will begin to adjust that, but now need to set up for those future iterations.

    Now we update the positions of prev & curr to the adjacent node.

    
    prev gets the position of curr now

                 prev
                 curr
    None  <---  ( 1 )   ( 2 ) --> ( 3 ) ---> None

    And remember that next pointer we saved that had a reference to node ( 2 ). We use that pointer to go to
    the adjacent node that being ( 2 )

                 prev    curr
    None  <---  ( 1 )   ( 2 ) --> ( 3 ) ---> None

    Note that the reason why we used that saved reference from the beginning instead of the current next pointer
    of ( 1 ) is because the next of ( 1 ) is now pointing to None. We already manipulated the pointer of ( 1 )
    so we needed a saved version before we did that so we could keep advancing in our LinkedList despite 
    adjusting the pointer reference. 

    That is essentially the process of the loop, now we keep doing this same process for the following nodes:


3. 
    a.
                    prev    curr    next
        None  <---  ( 1 )   ( 2 )   ---->  ( 3 ) ---> None
                                (save next ref that points to 3)
    
    b. 

                    prev          curr
        None  <---  ( 1 ) <-----  ( 2 )    ( 3 )  ---> None
                     (manipulate pointer to point to prev)
    
    c. 
                                  prev
                                  curr
        None  <---  ( 1 ) <-----  ( 2 )    ( 3 )  ---> None
                     (move our prev to curr

    d. 
                                   prev     curr
        None  <---  ( 1 ) <-----  ( 2 )    ( 3 ) ---> None
                                        (use our saved pointer ref to update our curr Node)


4. 
    a.                            prev      curr   next
        None  <---  ( 1 ) <-----  ( 2 )    ( 3 )   --->  None
                                              (save next ref that points to None)

    b. 
                                   prev       curr   
        None  <---  ( 1 ) <-----  ( 2 ) <---- ( 3 )     None
                                        manipulate pointer to prev
    
    c. 
                                             prev
                                             curr   
        None  <---  ( 1 ) <-----  ( 2 ) <---- ( 3 )     None
                                          (adjust prev)  

    d.

                                              prev      curr   
        None  <---  ( 1 ) <-----  ( 2 ) <---- ( 3 )     None
                                                 adjust curr to our saved ref from earlier

5.
    Our current node is now at None indicating we are at the end of the LinkedList.
    Therefore we have arrived at a conclusion and have reversed our linked list.

    FINAL ANSWER:    None  <----  ( 1 ) <-----  ( 2 ) <---- ( 3 )

'''

#CODE: TC: O(N)    SC: O(1)

def reverseList(head):
    prev = None
    curr = head

    while curr is not None:
        temp_next = curr.next
        curr.next = prev
        prev = curr
        curr = temp_next
    
    return prev

#-----------------------------------------------------------------------------------------------------------------

#RECURSIVE APPRAOCH:

'''
For this appraoch we will use the same test case:

INPUT:  1 --> 2 --> 3
OUTPUT: 3 <-- 2 <-- 1


We will be making a seperate recursive function that will do all the work for us, then we will be
calling and returning this recursive function into for our final answer in the main function,
and that will conclude our answer. 

Our recursive function will take two inputs, 

head node of input function   and    another node called prev which is set to None.

This solution is very similar to the iterative solution. 

Let's denote this function with f

1.
    the first call would look like 

                head    prev
            f ( ( 1 ) , None )

            We check our BASE CASE:
                if head is None, we return Prev and end the recursion
                else we keep going through the function

            We save the next pointer ref of ( 1 )
         
                  (save)
            ( 1 ) ----> ( 2 ) 

            will denote the saved pointer ref with a node called temp_next

            now we manipulate our pointer and make it point to prev

             prev           head
             None   <----  ( 1 )    ( 2 ) ---->  ( 3 ) ---> None

            
            Now we call our recursive function with the following inputs

            f ( temp_next , head)  = f ( ( 2 ) , ( 1 ) )

            
2. 
        head     prev
    f ( ( 2 ) , ( 1 ) )

    head ( 2 ) is NOT None so we continue 

    save next pointer ref = temp_next
    ( 2 ) ---> ( 3 )

    manipulate our current next pointer
    
                           prev          head
             None   <----  ( 1 )  <----  ( 2 )    ( 3 ) ---> None
    
    call our recursive function

    f ( temp_ next , head )   = f ( ( 3 ) , ( 2 ) )


3. 
         head     prev
    f ( ( 3 ) , ( 2 ) )

    head ( 3 ) is NOT None so we continue 

    save next pointer ref = temp_next
    ( 3 ) ---> ( None )

    manipulate our current next pointer
    
                                         prev           head
             None   <----  ( 1 )  <----  ( 2 )   <----  ( 3 )      None
    
    call our recursive function

    f ( temp_ next , head )   = f ( ( None ) , ( 3 ) )


4. 

          head      prev
    f ( ( None ) , ( 3 ) )

    head is None therefore we terminate our recursive function


5. 

    OUR FINAL ANSWER IS:    None  <----  ( 1 )  <----  ( 2 )   <----  ( 3 )

'''

#CODE:  TC: O(N)    SC: O(1)

def reverseList(head):
    return reverseListHelper(head, None)

def reverseListHelper(head, prev):

    if head is None:
        return prev
    
    temp_next = head.next
    head.next = prev

    return reverseListHelper(temp_next, head)


#-----------------------------------------------------------------------------------------------------------------








