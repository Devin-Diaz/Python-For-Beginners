'''
LEETCODE 49: GROUP ANAGRAM


Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''

#EXPLANATION:

'''
Straight away the idea is to use a dictionary to be able to sort our output list with it's command anagrams. We will do this by
sorting a word in our input list in alphabetical order, and using that sorted word as our key pair. We check if that sorted word
already exists in our dictionary, it tells us that we already have anagrams under that type of word and we would append our original
word as a value pair with the key of the sorted word. If the sorted word doesn't exist in our dictionary, we initialize that key
with an empty list value pair, where the anagrams associated with that sorted word will be stored.

The goal is if it's an anagram, the word will always be sorted in the same format telling us that it's a value pair for that key that being
the sorted word. The following is a visual on a test case:

VISUAL:
                 0     1     2     3     
Input: strs = ["eat","tea","tan","ate"]
Output: [["nat","tan"], ["ate","eat","tea"]]


dict = {} currently empty

0. We begin iteration with "eat"
    we save the original word that being eat in variable word.
    We then sort eat --> aet

    aet doesn't exist in our map so we initialize it with an empty list
    {"aet" : []}

    now we append the original word with aet as it would be the first word associated with aet being the sorted wrd
    {"aet", ["eat"]}

dict = { "aet" : ["eat"] }

1. next we have tea
    we sort aet
    we check our dict if there is a key of aet, and indeed we do.
    so we append our original word tea with it's associated key that being the sorted word aet
    {"aet" : ["eat", "tea"]}

dict = { "aet" : ["eat", "tea"] }

2. next we have tan
    we sort tan --> ant
    we check our dict and see that ant isn't a key value pair,
    we initialize ant with an empty list
    we append the original word tan to it's associated key being the sorted word ant
    { "ant", ["tan"] }

dict = { "aet" : ["eat", "tea"],  "ant" : ["tan"]}

3. next we have ate
    ate sorted is aet
    we see that aet exists in our dict
    we append ate to the key value aet
    {"aet" : ["eat", "tea", "ate"]}

dict = { "aet" : ["eat", "tea", "ate"],  "ant" : ["tan"]}

Now that we have iterated thorugh all strings in our input list, we add all of our map values into a list:
[["nat","tan"], ["ate","eat","tea"]]

And we have concluded to our answer.
'''

#CODE: TC: O(N) , SC: O(N)

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    dict = {}

    for originalWord in strs:
        char_list = list(originalWord)
        char_list.sort()
        sortedWord = ''.join(char_list)

        if sortedWord not in dict:
            dict[sortedWord] = []
        
        dict[sortedWord].append(originalWord)
    
    return list(dict.values())



