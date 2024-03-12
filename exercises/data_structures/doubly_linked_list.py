'''
DOUBLY LINKED-LIST STUDY:

**IF YOU HAVEN'T ALREADY READ SINGLY-LINKED-LIST FIRST**


A doubly linked list is the exact same as a singly linked list, the only vital difference is we have an additional pointer
called prev. prev stands for previous. Recall from our singly linked list, a list is comprised of a sequence of nodes. Each node
containing a value and a reference (link) to the next node in the sequence. A doubly linked list has the exact same, however now
we have an additional nexterence (link) that connects to the previous node before our current node. Let's compare the visual between
a singly and doubly linked list:


        SINGLY LINKED LIST:

                HEAD
        [ "Devin" | next ]  -->  [ "Mark" | next ] --> [ "Munez" | next ] --> None


        DOUBLY LINKED LIST
                
                            HEAD                                                           TAIL
        None <--> [ prev | "Devin" | next ]  <-->  [ prev | "Mark" | next ] <--> [ prev | "Munez" | next ] <--> None

        say we did 
            Mark.prev.data = "Devin"
            tail.next = None
            head.next.next.next.prev.data = "Mark"


        
Note that now we are utilizing our tail pointer for our doubly linked list. This is because now we can traverse forwards and backwards
with our linked list unlike our singly linked list where we could only go forwards. Because of our new reference pointer "prev" we
now have flexibility with how we traverse our linked list, so having a pointer tail that tells us where the last node with content is 
located is very much useful compared to having it with a singly linked list. 

Now let's get into the code:
'''

#DOUBLY LINKED LIST (DLL) CODE:

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return

        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
    
    def prepend(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode

    def remove(self, data):
        current = self.head

        while current is not None and current.data is not data:
            current = current.next
        
        if current is None:
            return
        
        if current.next is None:
            self.head = current.next
        else:
            current.prev.next = current.next
        
        if current.prev is None:
            self.tail = current.prev
        else:
            current.next.prev = current.prev
    
    def contains(self, data):
        current = self.head

        while current is not None:
            if data == current.data:
                return True
            current = current.next

        return False


    def isEmpty(self):
        return self.head and self.tail is None


    def size(self):
        counter = 0
        current = self.head

        while current is not None:
            counter += 1
            current = current.next
        
        return counter
    

    def displayRegular(self):

        output = ""
        current = self.head

        output += "None"
        output += " <--> "

        while current is not None:
            output += str(current.data)
            output += " <--> "
            current = current.next

        output += "None"

        return output
    
    def displayReverse(self):
        output = ""
        current = self.tail

        output += "None"
        output += " <--> "

        while current is not None:
            output += str(current.data)
            output += " <--> "
            current = current.prev

        output += "None"

        return output



dll = DoublyLinkedList()

dll.append(5)
dll.append(10)
dll.append(15)
dll.append(20)

print(dll.contains(20)) # True
print(dll.isEmpty()) # False
print(dll.size()) # 4

print(dll.displayRegular()) # None <--> 5 <--> 10 <--> 15 <--> 20 <--> None
print(dll.displayReverse()) # None <--> 20 <--> 15 <--> 10 <--> 5 <--> None



