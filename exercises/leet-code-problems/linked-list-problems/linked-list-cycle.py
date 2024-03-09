'''
LEETCODE 141: LINKED LIST CYCLE

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by 
continuously following the next pointer. Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.


EXAMPLE 1:

(3) --> (2) --> (0) --> (-4)
         ^                |
         |                |
         |-----------------

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).


EXAMPLE 2:

(1) --> (2)
 ^       |
 |       |
 |---------        

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

'''

# VISUAL AND EXPLANATION:

# TWO POINTER APPROACH

'''
For this problem we will have to utilize a two pointer technique. Our first pointer will be called slow, and
our second pointer fast. 

slow - will be traversing through the linked list linearly, one node at a time. 
fast - will be traversing 2 nodes at a time. 

The logic behind this is, if a pointer is going 2x the rate as the other, if THERE IS A CYCLE, there will be a 
point in the linked list where both pointers arrive at the same node 

Let's use the following test case:

(3) --> (2) --> (0) --> (-4)
         ^                |
         |                |
         |-----------------

0. 
    these are where are pointers begin
    
    slow
    fast
    (3) --> (2) --> (0) --> (-4)
             ^               |
             |               |
             |-----------------

         
1. 
    On the first iteration our points will adjust, recall slow 1x and fast 2x

            slow    fast
    (3) --> (2) --> (0) --> (-4)
            ^                |
            |                |
            |-----------------

    We check if they are at the same node, in this case NO


2. 
    second iteration, we adjust

                    slow
                    fast
    (3) --> (2) --> (0) --> (-4)
             ^                |
             |                |
             |-----------------

    We check and YES both nodes are the same indicating that there is a cycle in our linked list.
    Thus true.

3. 
    Of course if we didn't find a cycle it would mean we reached a None statement while traversing with our
    fast pointers while iterating. Thus it would be a false by default.

'''

# CODE: TC: O(N)   SC: O(1)

def hasCycle(head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = head
        fast = head

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if(slow == fast):
                  return True
            
        return False

#------------------------------------------------------------------------------------------------------------------

# HASHSET APPRAOCH:

#VISUAL AND EXPLANATION:

'''
Let's use the following test case: 


(3) --> (2) --> (0) --> (-4)
         ^                |
         |                |
         |-----------------


Now we will create a hashset that will keep track of every node we will iterate over. This appraoch
will check if a node already exists in our hashset, if it does it tells us there WAS a cycle because we
are iterating over the linked list again. If we never find a node that is already contained in the hashset,
it tells us that we iterated cleanly throught the linked list telling us that THERE IS NO CYCLE. 

Let's do it step by step

hashset = {}

1. 
     *
    (3) --> (2) --> (0) --> (-4)
            ^                |
            |                |
            |-----------------

        On our first iteration we check node (3)

        set = {}

        we see that our set doesn't contain anything so we just add the node and keep traversing

        set = { (3) }

2. 
             *
    (3) --> (2) --> (0) --> (-4)
            ^                |
            |                |
            |-----------------

        
        Our second iteration we see that (2) is not contained in our set

        set { (3) }

        so we add our current node that being (2) and we move on to the next node

        set = {(3), (2)}

3.
                     *
    (3) --> (2) --> (0) --> (-4)
            ^                |
            |                |
            |-----------------


        (0) not contained so we move on

        set = { (3), (2), (0) }


4.
                              *
    (3) --> (2) --> (0) --> (-4)
            ^                |
            |                |
            |-----------------


    (-4) not contained

    set = { (3), (2), (0), (-4) }

    
5. 
             *
    (3) --> (2) --> (0) --> (-4)
            ^                |
            |                |
            |-----------------

    
    We check our set and see that (2) is already contained

                  *
    set = { (3), (2), (0), (-4) }

    Therefore we do have a cycle in our linked list thus we return true.

6.
    Of course if we didn't we'd return false by default.


    
Now let's get into the code!

'''

# TC: O(N)     SC: O(N)

def listCycle(head):
      
    curr = head
    hashset = set()
      
    while curr is not None:
        if curr in hashset:
                return True
        curr = curr.next
    
    return False




#------------------------------------------------------------------------------------------------------------------
