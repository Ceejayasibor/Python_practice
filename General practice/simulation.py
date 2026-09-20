import pandas as pd
import numpy as np

def SimulateGame(iterations, stop_threshold):
    grand_total_score = []

    for game in range(iterations):
        game_score = 0

        while True:
            roll = np.random.randint(1,6)
            if roll == 6:
                game_score = 0
                break

            game_score += roll
        

        grand_total_score.append(game_score)


    df = pd.Dataframe(grand_total_score, columns=[game_score])
    return df[game_score].mean


for stop_threshold in range(1, 31):
    avg = SimulateGame(1000000, stop_threshold)
    print (stop_threshold, avg)



import heapq

class MeanFinder():
    def __int__(self):
        self.small = [] #Max Heap, implemented with -ve
        self.large = [] #Min Heap

    def addNum(self, num):
        heapq.heappush(self.small, -num)

    if self.small and self.large and (-self.small[0] > self.large[0]):
        heapq.heappush(self.large, -heapq.heappop(self.small))

    if len(self.small) > len(self.large) + 1:
        heapq.heappush(self.large, -heapq.heappop(self.small))

    if len(self.large) > len(self.small):
        heapq.heappush(self.small, -heapq.heappop(self.large))

    
    def getMedian(self): 
        if self.small > self.large:
            return -self.smal[0]
        return (-self.small[0] + self.large[0])/2
    


'''Probability of 2 Consecutive Heads'''

import random

def prob_two_consec_heads(iterations = 1000000):
    grand_total = 0

    for _ in range(iterations):
        game_score = 0
        count = 0

        while True:
            flip = random.choice(['H', 'T'])
            count += 1
            
            if flip == 'T':
                game_score = 0

            game_score+=1
        
            if game_score  == 2:
                break
            
        grand_total += count
    
    return grand_total/iterations



import random

def prob_two_consec_heads(trials=100000):
    success = 0

    for _ in range(trials):
        prev = 0
        while True:
            flip = random.randint(0, 1)
            if flip == 1 and prev == 1:
                success += 1
                break
            prev = flip

    return success / trials







            

