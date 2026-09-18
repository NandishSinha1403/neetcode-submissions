class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # least = min(prices)   
        # min_i = prices.index(least)
        # if min_i == len(prices)-1:
        #     return 0
        # maxafter = max(prices[min_i:])
        # return maxafter-least

        # most = max(prices)
        # max_i = prices.index(most)
        # if max_i == 0:
        #     return 0

        # minbefore = min(prices[0:max_i])
        # return most-minbefore
        if len(prices) <= 1:
            return 0
        temp = []
        k = 1
        for i in (prices[1:]):
            minbefore = min(prices[0:k+1]) #this is the problem come back to this and try to optimise this line
            if minbefore >= i:
                temp.append(0)
            else:
                temp.append(i-minbefore)
            k+=1
        return max(temp)