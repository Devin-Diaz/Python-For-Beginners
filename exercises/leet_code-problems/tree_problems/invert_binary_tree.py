'''
LEETCODE 226: INVERT BINARY TREE:

Given the root of a binary tree, invert the tree, and return its root.



EXAMPLE 1: 

Input: root = [4,2,7,1,3,6,9]

           (4)                              
        /       \
    (2)           (7)     
   /   \         /   \  
 (1)   (3)    (6)     (9)


 Output: [4,7,2,9,6,3,1]
    
           (4)
        /       \
    (7)           (2)     
   /   \         /   \  
 (9)   (6)    (3)     (1)



EXAMPLE 2:

Input: root = [2,1,3]

           (2)                              
        /       \
    (1)           (3) 


Output: [2,3,1]

           (2)                              
        /       \
    (3)           (1) 

'''


'''
VISUAL AND EXPLANATION:

We will utilize recursion for this approach. We start with a base case that tells us if our current root is None, it means
that we never had a binary tree to begin with OR we have reached the end of the binary tree.

For the recursion aspect we will be calling our own original function twice. One recursive call focusing on the left hand side of
the binary tree, and the other recursive call focusing on the right hand side.


Let's use the following input binary tree:
Input: root = [4,2,7,1,3,6,9]

           (4)                              
        /       \
    (2)           (7)     
   /   \         /   \  
 (1)   (3)    (6)     (9)



0.
    We start by saving our left and right child nodes in a variable. So on our first pass through the function, before we even hit our
    recursive calls, we will be saving the left and right child nodes of the root node. We will denote recursive calls with IT()

    left = (2)    right = (7)


(LEFT HAND SIDE)
1.
    We start by recursing through the left node (2) and essentially this is what we are doing.

           IT(4)
          /
        IT(7)
       /
    IT(9)
    /
  None

  Here we did 3 recursive calls until we reached None. 
  Our root.left pointer of the root node now points to the right node that being (7).
  The root.left pointer of (7) now points to its right node that being (9).
  We now check for the left.pointer of (9) and we see that it's None since there are no more nodes to traverse to

2.

           IT(4)
          /
        IT(7)
       /
    IT(9)
    /   \
  None  None

  We take a step back and check the right pointer of (9) and see that it's None, so we are done with this sub tree.

3.  

    We now take another step back and check the right pointer node of (7):

           IT(4)
          /
        IT(7)
       /     \
    IT(9)     IT(6)
    /   \      /
  None  None  None

    The right pointer of node (7) gets set to the left node (6)
    We now check the left pointer of (6) and we see that it is None indicating no more nodes to traverse to

4. 
    We now take a step back and check the right pointer of Node (6)
    We notice that it's none indicating there are no more nodes to traverse to


           IT(4)
          /
        IT(7)
       /     \
    IT(9)     IT(6)
    /   \      /   \
  None  None  None  None


(RIGHT HAND SIDE)

5.

    IT(4)
        \
         IT(2)
            \
            IT(1)
               \       
              None

6. 

    IT(4)
        \
         IT(2)
             \
            IT(1)
            /   \       
         None   None

7.

    IT(4)
        \
         IT(2)
         /    \
      IT(3)      IT(1)
                 /   \       
              None   None

8. 

    IT(4)
        \
         IT(2)
         /     \
      IT(3)     IT(1)
      /   \      /    \       
    None   None  None  None

Final. 

                   IT(4)
          /                       \
        IT(7)                    IT(2)
       /     \               /          \
    IT(9)     IT(6)        IT(3)       IT(1)
    /   \      /   \       /    \        /  \
  None  None  None  None  None   None   None   None



           (4)
        /       \
    (7)           (2)     
   /   \         /   \  
 (9)   (6)    (3)     (1)
          
    

 We can see that we made a total of 15 recursive calls including the ones that lead to None.
 Thus we have a time complexity of O(N)

'''

#CODE:

