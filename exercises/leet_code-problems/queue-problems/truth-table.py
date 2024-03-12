'''
TRUTH TABLE POSSIBILITIES:

Given n variables, list all possible True/False combinations possible.

EXAMPLE 1:

Input: n = 2
Output:
        T  T
        T  F
        F  T
        F  F

        
EXAMPLE 2:
        
Input: n = 3
Output:
        T  T  T
        T  T  F
        T  F  T
        T  F  F
        F  T  T
        F  T  F
        F  F  T
        F  F  F

        
EXAMPLE 3:

Input: n = 0
Output: ""

'''
# VISUAL AND EXPLANATION:

'''
Let's use the following test case where n = 3. Given n we know how many outputs we are suppose to get given
the following formula: 2^N. For this test case we have 2^3 = 8, thus we have 8 different possibilities for
3 truth values. Let's get into the visual.

We start by creating a queue and giving it an empty string for a queue of size 1. We do this in order to get started 
with our iterations. With each iteration from our outer loop, we save the size of our queue to see how many possibilities 
we can add to and create. Right now it may be confusing but keep reading.


Now we get into our loops:


0. i = 0,  size of queue = 1

        j = 0

                (this got dequeued)
                combination = ""

                (these will get enqueued)
                "" + "T"
                "" + "F"

        so currently in our queue we have
        ["T", "F"]

        We move on to the next iteration

1. i = 1, size of queue = 2

        j = 0

                (this got dequeued)
                combination = "T"

                (these will get enqueued)
                "T" + "T"
                "T" + "F"

        j = 1

                (this got dequeued)
                combination = "F"

                (these will get enqueued)
                "F" + "T"
                "F" + "F"

        so currently in our queue we have:
        ["TT", "TF", "FT", "FF"]

2. i = 2, size of queue = 4

        j = 0

                (this got dequeued)
                combination = "TT"

                (these will get enqueued)
                "TT" + "T"
                "TT" + "F"
        
        j = 1

                (this got dequeued)
                combination = "TF"

                (these will get enqueued)
                "TF" + "T"
                "TF" + "F"
        
        j = 2

                (this got dequeued)
                combination = "FT"

                (these will get enqueued)
                "FT" + "T"
                "FT" + "F"
        
        j = 3

                (this got dequeued)
                combination = "FF"

                (these will get enqueued)
                "FF" + "T"
                "FF" + "F"

        
        so currently in our queue we have
        ["TTT", "TTF", "TFT", "TFF", "FTT", "FTF", "FFT", "FFF"]

        size of queue = 8

                
3. 
        i = 3 and 3 is not less than 3 thus we have reached the end and as we can see we now have 8 
        different possibilities.

        Formated nicely we have:

        "T T T" 
        "T T F" 
        "T F T" 
        "T F F"
        "F T T" 
        "F T F"
        "F F T"
        "F F F"

        We have arrived at our conclusion.

        Now let's get into the code:
'''


#CODE:
# TC: O(2^N)  SC: O(2^N)

from data_structures.queue import Queue

def truth_table(n):
    queue = Queue()
    queue.enqueue("")

    for i in range(n):
        size = queue.size()
        for j in range(size):
            combination = queue.dequeue()
            queue.enqueue(combination + "T")
            queue.dequeue(combination + "F")
    
    for strs in queue:
        print(strs)

    

#--------------------------------------------------------------------------------------------------------------------