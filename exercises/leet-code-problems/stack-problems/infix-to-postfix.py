'''
INFIX TO POSTFIX PROBLEM:

Postfix notation also known as reverse polish notation(RPN). So to start off what is RPN?

Reverse Polish Notation (RPN), also known as postfix notation, is a mathematical notation in which operators 
follow their operands. This is in contrast to the more common infix notation used in arithmetic, where operators 
are placed between operands.

For example, in infix notation, you would write an expression like 3 + 4. In RPN, this becomes 3 4 + 
The advantage of RPN is that it eliminates the need for parentheses to indicate the order of operations. 
For instance, the infix expression (3 + 4) * 5 becomes 3 4 + 5 *  in RPN

Operands --> elements
Operators --> +, -, /, *

Given an input String s, your goal is to change s, which is going to be an infix expression 
(regular math notation), and convert it into infix notation. Your return type should be a String.


EXAMPLE 1:
Input: "A+B-C"
Output: "AB+C-"

EXAMPLE 2:
Input: "(A+B)/(C-D)"
Output: "AB+CD-/

EXAMPLE 3:
Input: "A+((B+C)*(E-F)-G)/(H-I)"
Output: "ABC+EF-*G-HI-/+"

'''

# EXPLANATION && VISUAL

'''
VISUAL:

Let's use the following test case for our visual:

Input: "(A+B)/(C-D)"

1.   (

    In our first iteration, we have a '('  this will get pushed into our stack
    
    |   |
    |   |
    | ( |
    |___|

2.  A

    Next iteration we have an operand, so we append this to our output String

    output = "A"

3.   +  

    We find an operator '+' . First we peek the top of stack to see if there exists another operator with higher
    priority, if not, we push this into our stack. 

    In this case we don't have any other operators in our stack thus we push our current operator in stack

    |   |
    | + |
    | ( |
    |___|


4.   B

    Next we find another operand, that being B so we append this to our output String 

    output = "AB"

5. )

    We find a RIGHT parentheses, this means that we have to pop out every element in our stack until we hit
    a LEFT PARENTHESES. EVERY ELEMENT THAT IS POPPED FROM OUR STACK, GETS APPENDED TO OUR OUTPUT STRING
    Once we reach that left parentheses, we discard that LEFT parentheses as it has no more use


    |   |
    | + |  <--- gets popped and appended to output
    | ( |
    |___|

    output = "AB+"

    |   |   
    |   |  
    | ( |   <--- we reach a right parentheses so we pop this from our stack and move to next iteration
    |___|

    
    |   |      
    |   |  
    |   |   
    |___|


6. /

    Next we have an operator '/'. We peek the top of stack if any operators with higher priority.
    If not we push our current operator in the stack.

    Currently there is no operators with greater priority so we push into stack

    |   |         
    |   |  
    | / |   
    |___|
    

7.   (

    RIGHT parentheses gets pushed into stack

    |   |         
    | ( |  
    | / |   
    |___|

8.  C

    operand gets append to output

    output = AB+C

9.  -

    We find an operator '-' , we peek stack and see there is no operator with higher priority,
    so we push our current operator to stack
    

    | - |         
    | ( |  
    | / |   
    |___|

10.  D

    Append operand to output String

    output = "AB+CD"

11.  )

    We have a right parentheses so we pop elements from our stack and append them into output string
    until we reach a LEFT parentheses.

    | - |  <---- pop         
    | ( |  
    | / |   
    |___|  

    output = "AB+CD-"

    |   |           
    | ( |  <--- we reach a LEFT parentheses so we pop and discard this  
    | / |   
    |___|


    |   |        
    |   |  
    | / |   
    |___| 


12. Final step

    We have reached the end of our string length. So now we just have to pop the remaining elements in our
    stack to complete the conversion from infix notation to postfix.

    |   |        
    |   |  
    | / |   <--- pop and append to output   
    |___|    

    output = "AB+CD-/"

    |   |        
    |   |  
    |   |   
    |___| 

13.

    return output = "AB+CD-/" COMPLETE

'''

def toRPN(expression):
    result = ""
    stack = []

    def isOperand(c):
        return c.isalpha() or c.isdigit()

    def priority(c):
        if c == '(':
            return 0
        elif c in '+-':
            return 1
        else:
            return 2

    for c in expression:
        if isOperand(c):
            result += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            if stack and stack[-1] == '(':
                stack.pop()  
        else:
            while stack and priority(stack[-1]) >= priority(c):
                result += stack.pop()
            stack.append(c)

    while stack:
        result += stack.pop()

    return result