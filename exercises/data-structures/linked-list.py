'''
SINGLY LINKED-LIST STUDY:

Imagine a treasure hunt where each clue leads you to the next location where the next clue is
hidden, until you finally find the treasure. A LinkedList works exactly like this treasure hunt.


A LinkedList is a collection of elements called 'Nodes', each node containing two main parts,

NODE [ data | next ] :

1. Data:
    This is the content of the clue in our treasure hunt. It represents the information or value
    that the node holds, this value can be a integer, character or any type of data.

2. Next Pointer (reference):
    This is the direction of the next clue that leads you to the next location. In a LinkedList, 
    the pointer "points" to the adjacent node in the list. If you are on the last clue or node 
    in the linked list, the final pointer will point to None (null) indicating that we are at
    the end of our LinkedList and no more nodes will follow. Every node has a reference to the next
    node assuming it exists. 

    
Terminology:

    HEAD:
        The head is the first node of the LinkedList. The head is where you start. Back to our
        treasure hunt example, the very first clue we find would be the head.

        If you have the head of the list, you can keep using next pointers to travel through all
        the nodes until eventually one of your next pointers hits null thus indicating you are at
        the end of the LinkedList

    
    TAIL:
        The tail is the last node of the LinkedList. This is usually used for more for doubly
        LinkedLists (will do this later on), however it's good to know what the tail element of
        a LinkedList is. Important to note that, None WOULD NOT be our tail, the tail of a LinkedList
        is the element before None. Tail is the last element in the list that actually contains data. 

    
    DIRECTION:
        With LinkedLists, we can only go forward as we traverse through the nodes. However if we wanted
        to go backwards that's where doubly LinkedLists would come in. However this study is on singly
        LinkedLists, but for future reference know that going forward AND backwards is a possibiliy. 

        
VISUAL:

    NODE =  [ | ]      NEXT = -->

            head                                        tail
    [ "Devin" | ref ]  -->  [ "Mark" | ref ] --> [ "Munez" | ref ] --> None

    Reading this in plain English the head of our list starts with a node containing the data "Devin" and contains
    a reference the points to the data "Mark". 
    = [ "Devin" | ref ]
    Starting to use a little syntax, if we did 

    
    head.next,    we would now be at 
    = [ "Mark" | ref ]

    
    If we wanted to get the specific data in our node we could do the following
    head.data = "Mark"

    
    Now that we are on the node mark, lets say we did the following:
    head.next.next

    --> we would end up at None.
    We traversed 2 points ahead, so we went to Munez node, and then went to the following reference which was None since
    that was the end of the LinkedList. 


    head, next, data, None, are your best friends when working with LinkedLists.

    Now let's get into the coding implementation. 
    
'''

#CODING: 

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    

    def add(self, target):
        new_node = Node(target)

        if self.head == None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next != None:
            last_node = last_node.next
        
        last_node.next = new_node
        

    def remove(self, target):

        temp_node = self.head

        while temp_node != None and temp_node.data != target:
            temp_node = temp_node.next
        
        if temp_node == self.head:
            self.head = self.head.next
            return
        
        current_node = self.head

        while current_node.next != None and current_node.next.data != target:
             current_node = current_node.next
        
        current_node.next = current_node.next.next

    
    def contains(self, target):
        temp_node = self.head

        while temp_node != None:
            if temp_node.data == target:
                return True
            temp_node = temp_node.next
        
        return False
             

    def isEmpty(self):
        return self.head == None
    

    def display(self):

        output = ""
        temp_node = self.head

        while temp_node != None:
            output += str(temp_node.data)
            output += " --> "
            temp_node = temp_node.next

        output += "None"

        return output
    




#IMPLEMENTATION OF OUR LINKED LIST DATA STRUCTURE:

list = LinkedList()

list.add(1)
list.add(2)
list.add(3)
list.add(4)

print(list.display())  # 1 --> 2 --> 3 --> 4 --> None

list.remove(2)
print(list.display())  # 1 --> 3 --> 4 --> None

print(list.contains(4))  # True

print(list.isEmpty())  # False


    




        
        
    
