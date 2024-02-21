'''
LEETCODE 242: VALID ANAGRAM

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

'''
#------------------------------------------------------------------------------------------------------------------



# Lazy approach
'''
We use built in python functions for this approach. We sort both s and t strings from our input. 
Once the strings are sorted in acsending alphabetical order, we then compare if they are equal or not. If so it'll be true thus,
valid anagram. If not it'll return false, indicating it is not a valid anagram.

E.G:

s = rat     t = car
sorted(s) = art         sorted(t) = acr
art != acr thus invalid anagram



This will have the following complexities:

TC: O(n log n)
SC: O(1)
'''

#Code

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return sorted(s) == sorted(t)


#Summary: 
#This has the TC of O(n log n) bc/ worst case scenario, that's the time it would take to 
#sort a string using the sorted() function. We use the sorted function twice on two different 
#strings thus O(n log n) + O(n log n) = O(n log n)

#The SC is O(1) bc/ our input doesn't affect the size of our program as we progress.

#------------------------------------------------------------------------------------------------------------------



'''
1. Compare input string lengths:

We start by checking if the length of the string inputs are equal. If not that
automatically tells us we have an invalid anagram. If they are equal, we proceed.

2. List to keep track of frequency:

What's key about this problem is that all given inputs will be lowercase letters. that is vital information.
In the alphabet there are 26 letters, we will construct a list of size 26, with each index having a starting 
element of 0. We will call this list freq for frequency denoting the frequency of each character in the strings.

VISUAL = [0, 0, 0, 0...., 0]    elements
          0  1  2  3      25    indices

3. ASCII background information:

ASCII - American Standard Code For Information Exchange, os a common character encoding format for text data
in computers and on the internet. This information is cool but we only care about the solution for this problem.

Recall that this problem only has inputs for strings literals that are lowercase. In ASCII land the first lowercase
letter, that being a,

'a' has a value of 97.

The last letter being z, 

'z' has a value of 122.

In this problem we will be working with the values 97 - 122 to ensure that we have a valid anagram. However the char
'a' with a value of 97 will play a vital role. Since we can NEVER HAVE A NEGATIVE INDEX in our list, each character
in our string literals whether it's in string s or string t, we will subtract 'a' from it, so will always be at a
greater than or equal index of 0 in our freq list. I will elaborate more:


4. Using ASCII during iteration

Say we have,

String s = "car" and String t = "rac"

a. car has length 3 == rac has length 3 : TRUE, procced

b. Now we will iterate over the length of S or T, this is fine bc/ both have the same length, can be either or,

c. create frequency array with a length of 26

d. begin iteration:

FIRST ITERATION:
String s
freq['c' - 'a' ] += 1  ==  freq[99 - 97] += 1   -->  freq[2] = 1 

String t
freq['r' - 'a' ] -= 1  ==  freq[114 - 97] -= 1   -->  freq[17] = -1

SECOND ITERATION
String s
freq['a' - 'a' ] += 1  ==  freq[97 - 97] += 1   -->  freq[0] = 1

String t
freq['a' - 'a' ] -= 1  ==  freq[97 - 97] -= 1   -->  freq[0] = 0

THIRD ITERATION
String s
freq['r' - 'a' ] += 1  ==  freq[114 - 97] += 1   -->  freq[17] = 0

String t
freq['c' - 'a' ] -= 1  ==  freq[99 - 97] -= 1   -->  freq[2] = 0


e. CHECK FREQ LIST

[0,...0, ...0,...0]
 0    2    17    25

As we can see all indices that we reached via ASCII balanced out to 0, since at some point we added by 1 or
subtracted by 1 whenever we reached that same index, whether it was from String s or String t, because both
string literals had the same characters, we were able to balance out the list to 0 if we incremented or
decremented at that index. 


ANOTHER CASE:
Now if it weren't a valid anagram, say we had 

s = "abc" and t = "baa"
Where s is goes up by 1 and t goes down by 1

[-1, 0, 1,...0]
  0  1  2    26

S goes up by 1 through a bringing it to 1
T goes down by 1 through b bringing it to -1

S goes up by 1 through b bringing it to 0
T goes down by 1 thorugh a bringing it to 0

S goes up by 1 through c bringing it to 1
T goes down by 1 through a bringing it to -1

Not a valid anagram because there is at least one index that is not 0.
'''

#CODE:

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    if len(s) != len(t): return False
    freq = [0] * 26

    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1 #ord() function gives us the ASCII value
        freq[ord(t[i]) - ord('a')] -= 1
    
    for x in freq:
        if x != 0:
            return False
        
    return True


#------------------------------------------------------------------------------------------------------------------