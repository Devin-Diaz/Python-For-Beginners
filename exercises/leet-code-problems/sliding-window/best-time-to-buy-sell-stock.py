'''
BEST TIME TO BUY AND SELL STOCK 

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''
#-----------------------------------------------------------------------------------------------------------------------------------------------


# This problem will require us to use sliding window technique. In this case will be using a dynamic sliding window, as our left and right pointers
# will be shifting. Our left pointer will be denoted startWindow and right pointer endWindow. These will act as the end points of our window.
# Both of these pointers will start at index 0. The only pointer that will be incremented by 1 on each iteration is endWindow, as this pointer
# will be in charge of expanding our window (traversing through our array).

'''
1.
given the example [7, 1, 5, 3, 6, 4]. both startWindow (L) and endWindow (R) will start at element 7, index 0.
this iteration doesn't mean much because both pointers are at the same number. So fast forward to the next iteration.



2.
endWindow(R) incremented by 1, so it is now at element 1, at index 1. We will denote startWindow with L and endWindow with R.
we check if L is greater than R, if so it tells us there is a lower price we can buy it. In this case it's true so the index of R becomes the index of L 
[7, 1, 5, 3, 6, 4]    
 L  R

[7, 1, 5, 3, 6, 4]  and now we iterate R since it's the pointer that always moves to keep giving us options.
    L
    R

[7, 1, 5, 3, 6, 4] as you can see we are beginning to form a window  7  | 1  5 |  3   6   4
    L  R                                                                  L  R

Now we will check the temporary profit, in this case 5 - 1. So our temp profit is 4, and this will get stored for our potential final output.
We now shift R once per usual



3. As we can see for the next iteration, element 1 is not greater than 3. We check the temp profit, 3 - 1 = 2. But that isn't greater than
our other temp profit of 4, so 4 remains as the max profit.

[7, 1, 5, 3, 6, 4]              WINDOW VISUAL:  7  | 1   5   3 |   6   4
    L     R                                          L       R

    

4. element 1 is not greater than 6, so no need to shift L pointer, now we check for temp profit 6 - 1 = 5.
This is greater than our original temp profit of 4, so now 5 becomes the new max profit. 

[7, 1, 5, 3, 6, 4]              WINDOW VISUAL:  7  | 1   5   3   6 |   4
    L        R                                       L            R

    

5. For the last iteration we move R to element 4. L is still at element 1. We check for temp profit, 4 - 1 = 3. However,
our current max profit is 5, so it'll stay that way and be our final outcome since there is no more elements to iterate through. 
    
'''

#CODE:
# TC = O(N)  SC = O(1)

def maxProfit(prices):
    left = 0
    right = 0
    max_profit = 0

    while right < len(prices):
        if prices[left] > prices[right]:
            left = right
        
        temp_profit = prices[right] - prices[left]
        max_profit = max(max_profit, temp_profit)

        right += 1

    return max_profit



#-----------------------------------------------------------------------------------------------------------------------------------------------
