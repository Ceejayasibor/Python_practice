'''Calculate rolling mean and rolling variance as you get a stream of number updates.'''

#Wedford's Algorithm
#new_mean (i.e mean for n) = old_mean (i.e. mean for n-1) + delta/n where delta = x - old_mean
#M2 is the numerator for the variance which is summation of the squares of the differences between x and mean i.e sum of (x -mean)squared from i=1 to n
#new_M2 (i.e. M2 for n) = old_M2 (i.e M2 for n-1) + delta*dellta2
#delta = x -old_mean
#delta = x - new_mean

class RunningStats():
    def __init__(self):
        self.n = 0
        self.mean = 0
        self.M2 = 0

    def update(self, x):
        self.n +=1
        delta = x - self.mean
        self.mean += delta/self.n
        delta2 = x - self.mean
        self.M2 += delta*delta2
        self.variance = self.M2/(self.n - 1)

    def get_mean(self):
        if self.n < 1:
            return 0
        return self.mean

    def get_variance(self):
        if self.n < 2:
            return 0
        return self.variance
    

rs = RunningStats()

for x in [1,2,3,4,5,6]:
    rs.update(x)
    print(rs.get_mean())
    print(rs.get_variance())



'''Get rolling Median'''

#Solution 1
import heapq

class MedianFinder():
    def __init_(self):
        self.small =[] #Max heap, implement by -ve sign.
        self.large= [] #Min heap
        #All elements in self.small must be <= items in self.large
        #len(self.small) - len(self.large) <= 1, cannot be -ve.

        def addNum(self, num):
            heapq.heappush(self.small, -num)
            
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def getMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0])/2
    

#Solution 2 - Slight Optimization
import heapq

class MedianFinder():
    def __init__(self):
        self.small = [] #max heap implemented using -ve of values
        self.large = [] #min heap
        #All elements in self.small must be <= elemnts in self.large
        #len(self.small) - len(self.large) <= 1, cannot be -ve

        def addNum(self, num):
            heapq.heappush(self.small, -num)

            #This ensures ordering by always removing the biggest element from self.small to slef.large, rebalancing after. 
            #Also implicitly ensures len(self.small) is not more than 1 greater than len(self.large), always removes biggest element in every iteration.
            #Hence the 2 conditions on all elements in small being <= elements in large and the length of small being at most 1 greater than large are inherent;y fulfilled.
            
            heapq.heappush(self.large, heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, heapq.heappop(self.large))

        def getMedian(self):
            if len(self.small) > len(self.large):
                return -self.small[0]
            return (-self.small[0] + self.large[0])/2


#Write a function to calculate the cost of shares bough, with the price increases 0.1 per unit share bought.

#This calculates initial cost + n number of shares bought, where initial cost is not part of n shares.
#i.e. 100, then 5 shares: 100, 100.1, 100.2, 100.3, 100.4, 100.5
def cost_of_shares(initial_price, shares, price_impact_per_share=0.1):
    total_cost = initial_price
    price = initial_price

    for _ in range(shares):
        price += price_impact_per_share
        total_cost += price

    return total_cost

print(cost_of_shares(100, 5))

#This calculates the total cost of shares including initial cost as part of n shares bought- initial is first share.
#i.e. 5 shares including 100: 100, 100.1, 100.2, 100.3, 100.4, 100.5
def cost_of_shares(initial_price, shares, price_impact_per_share=0.1):
    total_cost = 0
    price = initial_price

    for _ in range(shares):
        total_cost += price
        price += price_impact_per_share

    return total_cost

print(cost_of_shares(100, 5))


def cost_of_shares(p, n, impact=0.1):
    return ((n*p) + impact * ((n-1)*n)/2)

print(cost_of_shares(100, 5))
# This is using formula for sum of arithmetic progression with first term as p, d= impact.

'''Moving average of last k prices.'''

from collections import deque

def moving_Average(nums, k):
    q = deque()
    total = 0
    res = []

    for x in nums:
        q.append(x)
        total += x

        if len(q) > k:
            total -= q.popleft()

        if len(q) ==k:
            res.apend(total/k)

    return res




from collections import deque
def moving_average(nums, k):
    q = deque()
    total = 0


    for num in nums:
        q.append(num)
        total += num

    if len(q) > k:
        q.popleft()
        total -=q.popleft()

    if len(q) == k:
        return (total/k)
