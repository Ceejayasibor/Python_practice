#You have number of simulations = number of games you play (not number of die rolls)
#Game is keep rolling, if you get a 6, your score for that game is 0. Game score = total  score across all rolls in  agame solution.
#Grand_total_score is score across all games/number of simulations. 
#The expected value will always be zero for this as you'll always get a 6 on each game, even if it's after 1,000,000rolls.

import random
def simulate_game(num_of_simulations):
    grand_total_score = 0

    for _ in range(num_of_simulations):
        game_score = 0

        while True:
            roll = random.randint(1,6)

            if roll == 6:
                game_score = 0
                break
            
            game_score += roll
        
        grand_total_score += game_score
    
    return grand_total_score/num_of_simulations

num_of_simulations = 1000000
print(simulate_game(num_of_simulations))


#You have number of simulations = number of games you play (not number of die rolls)
#Game is keep rolling, if you get a 6, your score for that game is 0. Game score = total  score across all rolls in  agame solution.
#Grand_total_score is score across all games/number of simulations.
# Add a roll to stop if grand total score/score is >=15 



import random
def simulate_game(num_of_simulations):
    grand_total_score = 0

    for _ in range(num_of_simulations):
        game_score = 0

        while True:
            roll = random.randint(1, 6)
            if roll == 6:
                game_score=0
                break
            
            game_score+=roll

            if game_score >= 15: #Has to be within while clause, cause you only stop/reset game when you get 6 and the score is for each game.
                break

        grand_total_score += game_score

     
    return grand_total_score/num_of_simulations
    
num_of_simulations = 1000000
print(simulate_game(num_of_simulations))


#Write a function to simulate a game when you roll a die for a large number of simulations: n, to determine the stop threshold to maximise payout.
#Remember if you get a 6, total for that game = 0 and add to you grand total score, else keep rolling and adding to your score.


import random
def simulate_game(num_of_simulations, stop_threshold):
    grand_total_score = 0

    for game_count in range(num_of_simulations):
        game_score = 0

        while True:
            roll = random.randint(1, 6)
            if roll == 6:
                game_score = 0
                break
            
            game_score+=roll 
        
            if game_score >= stop_threshold:
                break
        
        grand_total_score += game_score
    
    return grand_total_score/num_of_simulations

for t in range(1, 30):
    avg = simulate_game(100000, t)
    print(t, avg)
# If I always stop at a score of t threshold, what is the average score for each t over 100,000 simulations/games.


import random
def simulate_with_strategy(num_simulations, stop_at_n_rolls):
    grand_total_score = 0

    for _ in range(num_simulations):
        game_score = 0
        
        # We loop for a maximum of 'stop_at_n_rolls'
        for roll_count in range(stop_at_n_rolls):
            roll = random.randint(1, 6)
            if roll == 6:
                game_score = 0
                break
            
            game_score += roll
        
        # Add the result of THIS game (either 0 or the accumulated sum) to our bucket
        grand_total_score += game_score

    # Calculate the average walk-away score
    return grand_total_score / num_simulations

# Example: If I play 10,000 games and stop after exactly 3 rolls
avg = simulate_with_strategy(10000, 3)
print(f"Average score stopping after 3 rolls: {avg}")



#Roll a die, if you get 1, you lose everything. Find the optimal stopping threshold i.e. game score.
import random
def simulate_game(iterations, stop_threshold):
    total_simulations_score = 0

    for game in range(iterations):
        game_score = 0

        while True:
            roll = random.randint(1,6)
            if roll == 1:
                game_score = 0
                break
           
            game_score+=roll

            if game_score >= stop_threshold:
                break

        total_simulations_score += game_score
    
    return total_simulations_score/iterations

for stop_threshold in range (1,30):
    avg = simulate_game(1000000, stop_threshold)
    print(stop_threshold, avg)

#After running this, optimal stopping threshold is between 19 and 21, preferably between 19 and 20.



#Numpy
import numpy as np

def simulate_game(iterations, stop_threshold):
    grand_total_score = []

    for game in range(iterations):
        game_score = 0

        while True:
            roll = np.random.randint(1,6)
            if roll == 6:
                game_score = 0
                break

            game_score += roll

            if game_score >= stop_threshold:
                break

        grand_total_score.append(game_score)

    
    return np.mean(grand_total_score)


for stop_threshold in range(1, 31):
    avg = simulate_game(1000000, stop_threshold)
    print(stop_threshold, avg)


#Pandas 
import pandas as pd
import numpy as np #To use np.random.randint

def simulate_game(iterations, stop_threshold):
    grand_total_score = []


    for game in range(iterations):
        game_score = 0

        while True:
            roll = np.random.randint(1, 6)
            if roll == 6:
                game_score = 0
                break

            game_score += roll

            if game_score >= stop_threshold:
                break
        
        grand_total_score.append(game_score)
    
    df = pd.DataFrame(grand_total_score, columns=[game_score])
    return df[game_score].mean

for stop_threshold in range(1, 31):
    avg = simulate_game(1000000, stop_threshold)
    print(stop_threshold, avg)



#Coin_Game

import random
class Coin_Game():
    def simulate_coin_game(self, n, stop_threshold):
        self.grand_total_score = 0

        for _ in range(n):
            self.game_score = 0

            while True:
                flip = random.choice(["H", "T"])
                if flip == "H":
                    self.game_score = 0
                    break

                self.game_score +=1


                if self.game_score >= stop_threshold:
                    break

            self.grand_total_score += self.game_score 
        
        return self.grand_total_score/n

for stop_threshold in range(1, 11):
    avg = Coin_Game().simulate_coin_game(1000000, stop_threshold)
    print(stop_threshold, avg)




import random
def simulate_card_game(iterations: int, stop_threshold: int) -> float:
    grand_total_score = 0

    for _ in range(iterations):
        game_score = 0

        while True:
            card_draw = random.randint(1, 10)
            if card_draw == 10:
                game_score = 0
                break

            game_score += card_draw

            if game_score >= stop_threshold:
                break


        grand_total_score += game_score

    return grand_total_score/iterations

for stop_threshold in range(1,31):
    avg =  simulate_card_game(1000000, stop_threshold)
    print(stop_threshold, avg)



def maxSubArray(nums, k):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum+nums[i])
        max_sum = max(current_sum, max_sum)

    return max_sum

nums = [2, -1, 3, -4, 5]
k = 2

print(maxSubArray(nums, k))


'''  Closest date from today with all distinct digits.
# 0 1 2 3 4 5 6 7 8 9

XX/XX/XXXX
17/06/2345

'''


