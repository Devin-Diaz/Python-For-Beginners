'''
OVERVIEW:

A queue is a data structure/abstract data type. A queue follows the FIFO principle (First in, First out)

An example of a queue in application is a line of people waiting to pay. Typically whoever arrives first
at the line is going to be the first person to leave. The second person in the line will the second person
to leave the line once they are done paying. Thus the concept First in, First out. 

In software related examples, web server request handling utilizes a queue data structure of some sort. Web servers use
queues to manage incoming requests from users, processnig them sequentially or based on priority to ensure 
the servers resources are utilized efficiently and all users are provided with fair service.


VISUAL:

Say we want to add the following elements in this exact order left to right:

1, 2, 3, 4, 5

In our queue visually it'll look like the following:


To insert elements they enter from the right side. "The beginning of the line is on the right of the queue"
(First in)

    
        -------------                    4*
        1  2  3  4*    <--- (inserting from right side) 
        -------------

 
        -------------                     5*   
        1  2  3  4  5*  <--- (inserting from right side)
        -------------


        
To remove an element we remove from the left side of the queue. "The end and exit of the line is on the left"
(First out)


           
                1*                   --------------     
    (removing left side) <----          2  3  4  5 
                                    --------------

                                    
                2*                   --------------     
    (removing left side) <----             3  4  5 
                                     --------------


                                                                         
In Python queues will differ slightly compared to other languages like Java, C++ etc.
The difference is in Python we use a list to implement the features of a queue or we can use different 
collections to import a queue object. With other lower level languages, the queue is it's own object with set of methods, 
but in Python we adopt the methods of a list and utilize certain ones to convert a list, into a working queue.
However in modern versions of Python like Python3, you can import a queue object. 


    Correct ADT terminology:                          Plain English:

    enqueue(arg) / offer(arg)           adds an element to the end of the queue
    dequeue() / poll()                  removes an element from the front of the queue
        contains(arg)                   Checks if an element exists in the queue  
          peek()                        returns the element at the front of the queue without removing it
        isEmpty()                       Checks if the queue is empty or not (boolean condition)
          size()                        Returns the size of the queue 


Now we will code the ADT implementation of a queue

'''

#--------------------------------------------------------------------------------------------------------------------------------------

#QUEUE ADT IMPLEMENTATION:

class Queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        if not self.isEmpty():
            return self.data.pop(0)        
        
    def size(self):
        return len(self.data)
    
    def peek(self):
        if not self.isEmpty():
            return self.data[0]
    
    def isEmpty(self):
        return self.size == 0

    def printQueue(self):
        print(self.data)

#--------------------------------------------------------------------------------------------------------------------------------------

#QUEUE TESTER:

queue = Queue()

#adding elements
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(1)

queue.printQueue() #[3, 2, 1]

print(queue.dequeue()) #3

queue.printQueue() #[2, 1]

print(queue.peek()) #2
print(queue.isEmpty()) #False
queue.dequeue() 
print(queue.size()) #1 

#--------------------------------------------------------------------------------------------------------------------------------------

#Congrats, you have learned queues in Python!


