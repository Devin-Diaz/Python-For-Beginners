'''
STACK DATA STRUCTURE:

A stack is a data structure/abstract data type. The stack follows the LIFO principle (last in, first out).

An example of an application of a stack is a web browser. As you open more links through the same tab, those
pages start stacking on top of each other with the most recent page being all the way at the top. However if 
we use the back button to go to a previous page, we remove that top element to go down one. 

Following our principle of last in first out, the first page accessed will be all the way at the bottom of our stack,
and the most recent page will be at the top and be the first removed if needed.

VISUAL:

Say we want to add the following elements in this exact order left to right.

1, 2, 3, 4, 5

in our stack visually it'll look like this:

|  5  |                                                             |     |
|  4  |      with a stack, we can't choose what element             |  4  |
|  3  |      we want to remove. We can only remove from             |  3  |
|  2  |      the top thus "first out". The bottom of the            |  2  | 
|  1  |      stack is a dead end. So if we removed an               |  1  |
-------      element it would look like the following ==>           -------


In Python stacks will differ slightly compared to other languages like Java, C++ etc.
The difference is in Python we use a list to implement the features of a stack. With other
lower level languages, the stack is it's own object with set of methods, but in Python we adopt
the methods of a list and utilize certain ones to convert a list, into a working stack.
The following are list methods we use for our stack

Correct terminology             Python method               Plain English
    push()                         append()                      adding an element to our stack
    pop()                            pop()                       remove element from stack
    peek()                   if not empty use index [-1]         checks top element of the stack without removing
    isEmpty()                len(stack) == 0 or not stack        boolean return type if stack is empty or not
    size()                         len(stack)                    returns the size of the stack

As we've seen that some methods aren't built in for a stack because of python's simplicity. peek(), isEmpty(),
and size() don't exist as methods. We can make them through functions if we wanted to though.

Up next there will be two sections. Me utilizing the stack as is with python functionality, then I will make
a simple ADT of a stack and utilize it with it's correct terminologies. 

'''

#--------------------------------------------------------------------------------------------------------------------

#PYTHON STACK IN APPLICATION: 

# Make a program that takes in numbers and then reverses them using 2 stacks.

stack_one = []
stack_two = []

stack_one.append(1)           #  | 3 |
stack_one.append(2)           #  | 2 |
stack_one.append(3)           #  | 1 |
print(stack_one)

                                                # | 1 | 
while(len(stack_one) != 0):                     # | 2 |
    stack_two.append(stack_one.pop())           # | 3 |

print(stack_two[-1])  # will return 1
print(stack_two)


#--------------------------------------------------------------------------------------------------------------------

'''
CODING THE ADT OF A STACK:

in other words creating a stack from scratch because python is to lazy to do it

'''

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.size() != 0:
            return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return self.size() == 0
    
    def __str__(self):
        return str(self.stack)

#--------------------------------------------------------------------------------------------------------------------


# OUR PERSONAL STACK IN APPLICATION:
    
#SAME PROBLEM, USE TWO STACKS TO REVERSE GIVEN NUMBERS
    
s1 = Stack()
s2 = Stack()

s1.push(1)
s1.push(2)
s1.push(3)
print(s1)

while not s1.isEmpty(): 
    s2.push(s1.pop())

print(s2.peek())
print(s2)


# We would get the same results as earlier [1, 2, 3] --> [3, 2, 1]

#--------------------------------------------------------------------------------------------------------------------

'''
You have now learned about stacks, congrats!
You have improved by 1% in the field of computer science!
'''
