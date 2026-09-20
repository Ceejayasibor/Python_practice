#Best time to buy and sell stock
#Time complexity = O(n), Space complexity = O(1), Kandane's algorithm
class Solution():
    def maxProfit(self, prices: list[int])-> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
        return max_profit
    
print(Solution().maxProfit([7,1,5,3,6,4]))
    
#Time complexity = O(n), Space complexity = O(1), Kandane's algorithm
class Solution():
    def maxProfit(self, prices: list[int])-> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
    
print(Solution().maxProfit([7,1,5,3,6,4]))


#Time complexity = O(n), Space complexity = O(1).
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price                    # found a cheaper buy day
            elif price - min_price > max_profit:
                max_profit = price - min_price       # found a better profit

        return max_profit
    print(Solution().maxProfit([7,1,5,3,6,4]))


#Brute force method, Time complexity = O(n²), Space complexity = O(n²) - worst case is storing all profits. 
class Solution():
    def maxProfit(self, prices: list[int])-> int:
        profit_store = []
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > 0:
                    profit_store.append(profit)
        return max(profit_store) if profit_store else 0

    
print(Solution().maxProfit([7,1,5,3,6,4]))

